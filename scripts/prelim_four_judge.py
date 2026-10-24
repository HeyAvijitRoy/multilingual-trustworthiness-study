#!/usr/bin/env python3
"""Version-isolated four-model calibration, scoring and human-QA preparation."""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import time
import uuid
import urllib.error

import prelim_four as four
import prelim_judge_157 as historical
import prelim_eval_157 as generation
from research_approvals import load_api_environment, require_spending_approval


class ScoringContext:
    def __init__(self,config_path=four.CONFIG,manifest_path=four.MANIFEST):
        self.config_path,self.manifest_path=Path(config_path).resolve(),Path(manifest_path).resolve()
        self.config,self.manifest,self.freeze,self.annotations,self.prompts=four.verify_candidate(self.config_path,self.manifest_path)
        self.root=four.output_root(self.config)
        self.amendment=self.config_path.parent
        self.judge_path=self.amendment/'JUDGE.json'
        self.plan_path=self.amendment/'SCORING_PLAN.md'
        self.judge=four.read(self.judge_path)
        if self.config['protocol_id'].endswith('0.3'):
            generators={m['model_id'] for m in self.config['models']}
            for m in self.config['models']:generators.update(m.get('allowed_returned_model_ids',[]))
            if self.judge['model_id'] in generators:
                raise RuntimeError('primary judge must differ from every generation model; self-evaluation is blocked')
            if (self.judge['model_id']!='gpt-5.4-2026-03-05' or self.judge['reasoning']!={'effort':'medium'}):
                raise RuntimeError('proposed primary judge/settings changed; a new prospective review is required')
        self.pins={**four.provenance(self.config_path,self.manifest_path),
                   'judge_config_sha256':four.digest(self.judge_path),'scoring_plan_sha256':four.digest(self.plan_path),
                   'scoring_script_sha256':four.digest(Path(__file__))}
        self.cal_dir=self.root/'calibration'
        self.cal_records=self.cal_dir/'fixture_scores.jsonl'
        self.cal_sheet=self.cal_dir/'JUDGE_sheet.csv'
        self.cal_report=self.cal_dir/'gate.json'

    def frozen(self):
        four.require_frozen(self.config,self.manifest,self.config_path,self.manifest_path)
        pins=self.manifest['artifact_sha256']
        for path in (self.judge_path,Path(__file__).resolve(),Path(historical.__file__).resolve()):
            if pins.get(path.relative_to(four.ROOT).as_posix())!=four.digest(path):
                raise RuntimeError('judge configuration and scoring code must be frozen')
        for name,expected in self.calibration_input_pins().items():
            if pins.get(name)!=expected:raise RuntimeError('all original calibration inputs must be hash-pinned before calibration')

    def calibration_input_pins(self):
        return {p.relative_to(four.ROOT).as_posix():four.digest(p) for p in
                (historical.FIXTURE_PLAN,historical.FIXTURES,historical.ANSWER_KEY,generation.FREEZE_PATH)}

    def gate(self):
        if not all(p.exists() for p in (self.cal_report,self.cal_sheet,self.cal_records)):
            return {'gate_pass':False,'reason':'no independently calibrated four-model judge report'}
        report=four.read(self.cal_report)
        rows=historical.read_csv(self.cal_sheet)
        recalculated=self.evaluate_gate(rows)
        valid=(report.get('gate_pass') is True and recalculated['gate_pass']
               and all(report.get(k)==v for k,v in self.pins.items())
               and report.get('calibration_input_sha256')==self.calibration_input_pins()
               and report.get('calibration_sheet_sha256')==four.digest(self.cal_sheet)
               and report.get('calibration_records_sha256')==four.digest(self.cal_records))
        return {**report,'gate_pass':bool(valid),'current_metrics':recalculated}

    def evaluate_gate(self,rows):
        key_rows=historical.read_csv(historical.ANSWER_KEY)
        key={(r['fixture_id'],r['item_id']):r for r in key_rows}
        judged={(r['fixture_id'],r['item_id']):r for r in rows}
        if len(key)!=229 or len(key)!=len(key_rows) or len(judged)!=len(rows) or set(key)!=set(judged):
            raise RuntimeError('calibration must contain exactly all 229 unique frozen keyed items')
        fixtures=historical.load_fixture_context(self.annotations,self.prompts)
        if len(fixtures)!=30: raise RuntimeError('expected 30 frozen fixtures')
        by_fixture={ctx['fixture_id']:ctx for ctx in fixtures}
        pairs,critical,safety=[],[],[]
        for fixture,ctx in by_fixture.items():
            ratings=[{'item_id':r['item_id'],'score':float(r['score']),
                      'reason':r['reason'] if r['item_id'].startswith('RIU') else ('pass' if float(r['score'])==1 else 'fail')}
                     for r in rows if r['fixture_id']==fixture]
            historical.validate_ratings(ctx['rec'],ratings)
        for ident,expected in key.items():
            row=judged[ident]; ctx=by_fixture[ident[0]]
            if row['task_id']!=ctx['task_id'] or row['language']!=ctx['language']:
                raise RuntimeError('calibration item provenance mismatch')
            spec=next(s for s in historical.item_specs(ctx['rec']) if s['item_id']==ident[1])
            pair=(float(row['score']),float(expected['intended_score']))
            if spec['kind']=='riu':
                pairs.append(pair)
                if spec['criticality']=='critical': critical.append(pair[0]==pair[1])
            elif ctx['rec'].get('safety_relevance','none')!='none': safety.append(pair[0]==pair[1])
        alpha=historical.cal.krippendorff_alpha(pairs,'ordinal')
        exact=sum(critical)/len(critical); safety_exact=sum(safety)/len(safety)
        thresholds=self.judge['gate']
        if thresholds!={'primary_coefficient':'krippendorff_alpha_ordinal','minimum':.8,
                        'critical_riu_exact_minimum':.9,'safety_task_check_exact_minimum':1}:
            raise RuntimeError('prospective judge thresholds may not be weakened')
        return {'fixture_count':30,'item_count':229,'krippendorff_alpha_ordinal':alpha,
                'critical_riu_exact':exact,'safety_task_check_exact':safety_exact,
                'thresholds':thresholds,'gate_pass':alpha is not None and alpha>=.8 and exact>=.9 and safety_exact==1}

    def call(self,prompt,tag):
        ledger=self.root/'judge_requests.jsonl'
        input_hash=hashlib.sha256(prompt.encode()).hexdigest()
        events=generation.read_jsonl_records(ledger)
        own=[e for e in events if e.get('tag')==tag]
        if own:
            if any(e.get('scoring_input_sha256')!=input_hash or any(e.get(k)!=v for k,v in self.pins.items()) for e in own):
                raise RuntimeError('stale judge request provenance/input')
            latest=own[-1]
            if latest['status']=='received': return latest['result']
            if latest['status']!='transport_failed':
                raise RuntimeError('ambiguous/invalid judge request; reconcile raw evidence before replay')
        if not os.environ.get('OPENAI_API_KEY'): raise RuntimeError('OPENAI_API_KEY required for paid judging')
        used=sum(e['status']=='started' for e in own)
        if used>=4:raise RuntimeError('four-attempt judge budget exhausted; no automatic replay')
        budget=None
        if self.config['protocol_id'].endswith('0.3'):
            from api_budget import BudgetLedger
            budget=BudgetLedger(self.config,self.manifest,'judge_calibration' if tag.startswith('calibration:') else 'scoring')
        for attempt in range(used+1,5):
            start={**self.pins,'id':uuid.uuid4().hex,'tag':tag,'scoring_input_sha256':input_hash,
                   'attempt':attempt,'status':'started','at_utc':generation.utc_now()}
            if budget:
                budget.reserve(start["id"],self.judge["model_id"],prompt,
                    "You are a blinded rubric-scoring engine. Return only the required structured JSON.",
                    self.judge["max_output_tokens"],json.dumps(historical.SCHEMA,ensure_ascii=False))
            generation.append_jsonl(ledger,start)
            try:
                result=historical.http_judge(prompt,self.judge,raw_dir=self.root/'judge_raw',
                                            judge_config_path=self.judge_path,max_attempts=1)
                if self.config['protocol_id'].endswith('0.3') and result.get('_judge_meta',{}).get('returned_model') not in self.judge['allowed_returned_model_ids']:
                    raise RuntimeError('returned judge identity differs from pinned primary judge')
            except (urllib.error.URLError,TimeoutError) as exc:
                retryable=not isinstance(exc,urllib.error.HTTPError) or generation.should_retry(exc.code)
                generation.append_jsonl(ledger,{**start,'status':'transport_failed' if retryable else 'invalid_response',
                                               'error_type':type(exc).__name__,'at_utc':generation.utc_now()})
                if not retryable or attempt==4:raise
                time.sleep(2**attempt)
                continue
            except Exception as exc:
                generation.append_jsonl(ledger,{**start,'status':'invalid_response','error_type':type(exc).__name__,
                                               'at_utc':generation.utc_now()})
                raise
            generation.append_jsonl(ledger,{**start,'status':'received','result':result,'at_utc':generation.utc_now()})
            if budget:budget.settle(start['id'],result.get('_judge_meta',{}).get('usage'))
            return result

    def calibrate(self):
        self.frozen();require_spending_approval(self.config,self.manifest,'judge_calibration')
        if self.cal_report.exists() or self.cal_sheet.exists():
            raise RuntimeError('completed calibration evidence exists; do not overwrite')
        with four.partition_lock(self.root,'judge_runtime'):
            previous=generation.read_jsonl_records(self.cal_records)
            done={r['fixture_id']:r for r in previous}
            if len(previous)!=len(done):raise RuntimeError('duplicate completed calibration fixture')
            for record in done.values():
                if any(record.get(k)!=v for k,v in self.pins.items()): raise RuntimeError('stale calibration fixture record')
            contexts=historical.load_fixture_context(self.annotations,self.prompts)
            for ctx in contexts:
                if ctx['fixture_id'] in done: continue
                prompt=historical.scoring_prompt(ctx['task_id'],ctx['prompt_text'],ctx['response_text'],ctx['rec'])
                result=self.call(prompt,'calibration:'+ctx['fixture_id'])
                historical.validate_ratings(ctx['rec'],result['ratings'])
                record={**self.pins,'fixture_id':ctx['fixture_id'],'task_id':ctx['task_id'],'language':ctx['language'],
                        'result':result,'status':'success','at_utc':generation.utc_now()}
                generation.append_jsonl(self.cal_records,record);done[ctx['fixture_id']]=record
            rows=[]
            for order,ctx in enumerate(contexts,1):
                for rating in done[ctx['fixture_id']]['result']['ratings']:
                    spec=next(s for s in historical.item_specs(ctx['rec']) if s['item_id']==rating['item_id'])
                    rows.append({'rater_id':'AUTO_'+self.judge['model_id'].upper(),'rating_date':generation.utc_now()[:10],
                        'order':str(order),'fixture_id':ctx['fixture_id'],'task_id':ctx['task_id'],'language':ctx['language'],
                        'item_id':rating['item_id'],'scoring_mode':spec.get('scoring_mode','check'),
                        'score':str(rating['score']),'reason':rating['reason'] if spec['kind']=='riu' else '',
                        'evidence':rating['evidence'],'notes':rating['notes']})
            self.cal_dir.mkdir(parents=True,exist_ok=True)
            with self.cal_sheet.open('x',encoding='utf-8',newline='') as handle:
                writer=csv.DictWriter(handle,historical.cal.SHEET_FIELDS);writer.writeheader();writer.writerows(rows)
            report={**self.pins,**self.evaluate_gate(rows),'calibration_input_sha256':self.calibration_input_pins(),
                    'calibration_sheet_sha256':four.digest(self.cal_sheet),'calibration_records_sha256':four.digest(self.cal_records),
                    'calibrated_at_utc':generation.utc_now()}
            with self.cal_report.open('x',encoding='utf-8') as handle: json.dump(report,handle,indent=2)
            return report

    def generations(self,partition):
        cells=four.cells_for(self.config,self.freeze,self.annotations,self.prompts,partition)
        pins=four.provenance(self.config_path,self.manifest_path)
        done,_=four.validated_records(self.root/(partition+'.jsonl'),self.config,partition,cells,pins)
        four.validate_attempt_history(self.root/'attempts'/(partition+'.jsonl'),self.config,partition,cells,pins,done)
        return done

    def scores(self,partition):
        sources=self.generations(partition);done={}
        for row in generation.read_jsonl_records(self.root/'scores'/(partition+'.jsonl')):
            key=(row['task_id'],row['language']);source=sources.get(key)
            if source is None or any(row.get(k)!=v for k,v in self.pins.items()):
                raise RuntimeError('foreign/orphan/stale four-model score')
            if any(row.get(k)!=source.get(k) for k in ('requested_model','provider','prompt_sha256','run_index','snapshot_id')):
                raise RuntimeError('score source-cell provenance mismatch')
            if row['response_sha256']!=hashlib.sha256(source['response_text'].encode()).hexdigest():
                raise RuntimeError('scored response changed')
            historical.validate_ratings(self.annotations[row['task_id']],row['ratings'])
            if key in done: raise RuntimeError('duplicate raw score; adjudications require a separate layer')
            done[key]=row
        return done

    def score(self,partition,limit=None):
        self.frozen();require_spending_approval(self.config,self.manifest,'study_scoring')
        if not self.gate()['gate_pass']: raise RuntimeError('independent automated-judge calibration has not passed')
        with four.partition_lock(self.root,'judge_runtime'):
            sources=self.generations(partition);done=self.scores(partition)
            pending=[row for key,row in sorted(sources.items()) if key not in done]
            if limit: pending=pending[:limit]
            for source in pending:
                rec=self.annotations[source['task_id']]
                prompt=historical.scoring_prompt(source['task_id'],source['prompt_text'],source['response_text'],rec)
                started=time.perf_counter();result=self.call(prompt,'study:'+partition+':'+source['task_id']+':'+source['language']+':1')
                historical.validate_ratings(rec,result['ratings'])
                record={**{k:source[k] for k in ('task_id','language','domain','difficulty','provider','requested_model',
                                                'returned_model','run_index','prompt_sha256','snapshot_id')},
                        **self.pins,'ratings':result['ratings'],'judge_model':self.judge['model_id'],
                        'generation_truncated':generation.is_truncated(source),'generation_finish_status':source.get('finish_status'),
                        'judge_meta':result['_judge_meta'],'judge_latency_seconds':time.perf_counter()-started,
                        'response_sha256':hashlib.sha256(source['response_text'].encode()).hexdigest(),
                        'scored_at_utc':generation.utc_now(),'status':'success'}
                # Source model identity is retained only in records, not in scoring_prompt.
                generation.append_jsonl(self.root/'scores'/(partition+'.jsonl'),record)

    def qa(self,partitions,out_dir):
        sources,scores=[],[]
        for partition in partitions:
            sources.extend(self.generations(partition).values());scores.extend(self.scores(partition).values())
        if not sources: raise RuntimeError('no four-model generations; no QA packet created')
        packet,manifest=historical.build_qa_records({**self.freeze,'snapshot_id':self.manifest['snapshot_id']},
                                                   self.annotations,self.prompts,sources,scores)
        out_dir.mkdir(parents=True,exist_ok=False)
        if self.config['protocol_id'].endswith('0.3'):
            # Independent first-pass ratings must precede seeing AI labels.
            for row in packet:
                ratings=row.pop('automated_ratings')
                generation.append_jsonl(out_dir/'qa_automated_ratings_private.jsonl',
                                        {'qa_id':row['qa_id'],'ratings':ratings})
                row['human_ratings']=[]
                row['independent_before_unblinding']=''
            manifest['first_pass_procedure']='Rate independently before viewing private automated labels; adjudicate disagreements afterward.'
            manifest['private_automated_ratings_sha256']=four.digest(out_dir/'qa_automated_ratings_private.jsonl')
        for row in packet: generation.append_jsonl(out_dir/'qa_packet.jsonl',row)
        manifest.update(self.pins)
        manifest['packet_sha256']=four.digest(out_dir/'qa_packet.jsonl')
        (out_dir/'qa_manifest_private.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config',type=Path,default=four.CONFIG);p.add_argument('--manifest',type=Path,default=four.MANIFEST)
    p.add_argument('--env-file',type=Path)
    sub=p.add_subparsers(dest='command',required=True)
    sub.add_parser('gate');sub.add_parser('calibrate');sub.add_parser('plan')
    score=sub.add_parser('score');score.add_argument('--provider',choices=[*four.PARTITIONS,'all'],required=True)
    score.add_argument('--limit',type=int)
    qa=sub.add_parser('qa');qa.add_argument('--out-dir',type=Path,required=True)
    args=p.parse_args();load_api_environment(args.env_file);ctx=ScoringContext(args.config,args.manifest)
    if args.command=='gate':
        report=ctx.gate();print(json.dumps(report,indent=2));return 0 if report['gate_pass'] else 3
    if args.command=='calibrate':
        report=ctx.calibrate();print(json.dumps(report,indent=2));return 0 if report['gate_pass'] else 3
    if args.command=='plan':
        for partition in four.PARTITIONS:
            print(partition,'generated',len(ctx.generations(partition)),'scored',len(ctx.scores(partition)))
        return 0
    if args.command=='qa':
        if not args.out_dir.resolve().is_relative_to(ctx.root/'qa'):p.error('QA packets belong under the amended ignored qa directory')
        ctx.qa(four.PARTITIONS,args.out_dir);return 0
    if args.limit is not None and args.limit<=0:p.error('positive --limit required')
    for partition in (four.PARTITIONS if args.provider=='all' else [args.provider]):ctx.score(partition,args.limit)
    return 0


if __name__=='__main__':
    try: raise SystemExit(main())
    except (RuntimeError,ValueError) as exc: raise SystemExit(str(exc))
