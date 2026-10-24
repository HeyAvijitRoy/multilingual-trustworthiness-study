#!/usr/bin/env python3
"""Four-model statistics using the shared frozen metric/bootstrap implementation.

Raw scores remain untouched. Optional resolved adjudications are source-linked;
their structural validity does not establish authentic independent human review.
"""
import argparse
import hashlib
import json
from pathlib import Path

import analyze_prelim_157 as shared
import prelim_four as four
import prelim_judge_157 as judge
import prelim_eval_157 as generation
from prelim_four_judge import ScoringContext


def apply_adjudications(path,scores,annotations):
    result=dict(scores);last={};applied=0
    for row in generation.read_jsonl_records(path):
        key=(row['requested_model'],row['task_id'],row['language'],int(row['run_index']))
        if key not in scores: raise RuntimeError('adjudication has no raw automated source score')
        source=scores[key]
        if row.get('raw_score_record_sha256')!=judge.canonical_record_sha256(source) or row.get('response_sha256')!=source['response_sha256']:
            raise RuntimeError('adjudication source hash mismatch')
        if row.get('status')!='resolved' or not row.get('reviewer_id') or not row.get('reviewed_at'):
            raise RuntimeError('unresolved or unattributed adjudication')
        log=(four.ROOT/row['review_log']).resolve()
        if not log.is_relative_to(four.ROOT) or not log.is_file() or four.digest(log)!=row.get('review_log_sha256'):
            raise RuntimeError('adjudication human review evidence missing or changed')
        if row.get('supersedes_adjudication_sha256')!=last.get(key):
            raise RuntimeError('adjudication revision chain mismatch')
        judge.validate_ratings(annotations[row['task_id']],row['ratings'])
        last[key]=judge.canonical_record_sha256(row)
        result[key]={**source,'ratings':row['ratings'],'adjudication_record_sha256':last[key]};applied+=1
    return result,{'applied_records':applied,'resolved_cells':len(last),
                   'adjudications_file_sha256':four.digest(path),
                   'independent_human_authenticity_certified':False}


def analyze(ctx,out_dir,allow_missing=False,adjudications=None):
    ctx.frozen()
    gate=ctx.gate()
    if not gate['gate_pass']: raise RuntimeError('four-model judge gate is absent/failed/stale')
    models=[m['model_id'] for m in ctx.config['models']]
    if len(set(models))!=4 or any(not m for m in models): raise RuntimeError('exactly four pinned models required')
    raw={}
    for partition in four.PARTITIONS:
        for row in ctx.scores(partition).values():
            raw[(row['requested_model'],row['task_id'],row['language'],int(row['run_index']))]=row
    expected=157*3*4
    if not raw: raise RuntimeError('no four-model scores; no results produced')
    if not allow_missing and len(raw)!=expected: raise RuntimeError('expected 1884 scores; report API missingness explicitly')
    scores=raw;adjudication_status={'applied_records':0,'resolved_cells':0,'independent_human_authenticity_certified':False}
    if adjudications: scores,adjudication_status=apply_adjudications(adjudications,raw,ctx.annotations)
    task_metrics={(model,task,lang):shared.response_metrics(ctx.annotations[task],row)
                  for (model,task,lang,run),row in scores.items()}
    model_cfg={'models':[{'provider':m['partition'],'model_id':m['model_id']} for m in ctx.config['models']]}
    freeze={**ctx.freeze,'snapshot_id':ctx.manifest['snapshot_id']}
    status,truncated=shared.generation_status(freeze,model_cfg,scores,output_dir=ctx.root)
    if allow_missing and any(c['reason']!='unresolved_api_failure' for c in status['missing_cell_details']):
        raise RuntimeError('--allow-missing permits documented API failures, not unattempted/unscored cells')
    domains={task:rec['domain'] for task,rec in ctx.annotations.items()}
    report={**ctx.pins,'generated_at_utc':generation.utc_now(),'task_count':157,
            'models':models,'scored_cells':len(scores),'expected_cells':expected,'missing_cells':expected-len(scores),
            'score_status':'provisional_pending_independent_human_QA',
            'primary_estimand':'critical_omission_rate:bn-en','adjudication_status':adjudication_status,
            'generation_status':status,'outcome_summary':shared.outcome_summary(task_metrics,models),
            'counts_by_model_language':{f'{model}:{lang}':sum(m==model and l==lang for m,_,l in task_metrics)
                                        for model in models for lang in shared.LANGS},
            'outcome_summary_weighting':'Descriptive response means; effects use five equal domain weights and four equal model weights.',
            'bootstrap':{'replicates':shared.BOOTSTRAP_N,'seed':shared.BOOTSTRAP_SEED,'cluster':'task_id',
                         'stratification':'domain','domain_equal_weighting':True,'model_equal_weighting':True},
            'limitations':['Preliminary 157-task four-model evaluation, separate from the historical panel and final 500-task study.',
                           'Independent human QA/sign-off remains required; structural review-file checks are not identity certification.',
                           'BF16/quantization/runtime/reasoning differences preclude capacity-matched causal comparisons.',
                           'Secondary intervals are descriptive and retain the frozen multiplicity convention.'],
            'effects':shared.effect_table(task_metrics,domains,models),
            **shared.reporting_tables(task_metrics,ctx.annotations,models,truncated),
            'source_output_files_sha256':{p.relative_to(ctx.root).as_posix():four.digest(p)
                  for partition in four.PARTITIONS for p in [ctx.root/(partition+'.jsonl'),ctx.root/'scores'/(partition+'.jsonl')]
                  if p.exists()},'analysis_plan_sha256':four.digest(four.AMENDMENT/'ANALYSIS_PLAN.md'),
            'analysis_script_sha256':four.digest(Path(__file__))}
    # Exclusive derived snapshot: preserve earlier reports when data/reviews grow.
    out_dir.mkdir(parents=True,exist_ok=False)
    (out_dir/'prelim_four_results.json').write_text(json.dumps(report,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
    markdown=shared.render_summary(report).replace('# Preliminary 157-task evaluation results',
                                                   '# Preliminary 157-task four-model evaluation results')
    (out_dir/'prelim_four_summary.md').write_text(markdown,encoding='utf-8')
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config',type=Path,default=four.CONFIG);p.add_argument('--manifest',type=Path,default=four.MANIFEST)
    p.add_argument('--allow-missing',action='store_true');p.add_argument('--adjudications',type=Path)
    p.add_argument('--out-dir',type=Path,required=True)
    args=p.parse_args();ctx=ScoringContext(args.config,args.manifest)
    destination=args.out_dir.resolve()
    if not destination.is_relative_to(ctx.root/'analysis'):p.error('analysis snapshot must be under the amended local analysis directory')
    report=analyze(ctx,destination,args.allow_missing,args.adjudications)
    print(json.dumps({'scored_cells':report['scored_cells'],'expected_cells':1884,'status':report['score_status'],'output':str(destination)}))


if __name__=='__main__':
    try: raise SystemExit(main())
    except (RuntimeError,ValueError) as exc: raise SystemExit(str(exc))
