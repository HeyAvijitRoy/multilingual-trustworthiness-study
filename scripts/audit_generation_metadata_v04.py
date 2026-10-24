#!/usr/bin/env python3
"""Preserve and audit fixed raw-log prefixes. No inference, labels or scoring."""
from collections import Counter
from datetime import datetime,timezone
import hashlib
import json
import os
from pathlib import Path
import generation_only_v04 as gen

LANGUAGES=('en','bn','bn_cs')
PRIMARY=('openai','local_a','local_b')
PUBLIC=gen.ROOT/'manuscript/acm_trust2027/GENERATION_INTEGRITY.json'


def complete_prefix(data):
    """Exclude only an unfinished final write; reject corrupt closed records."""
    end=data.rfind(b'\n')+1
    prefix=data[:end]
    records=[json.loads(line) for line in prefix.split(b'\n') if line.strip()]
    return prefix,records,len(data)-end


def validate_request_record(row,cell,config,model):
    if row.get('prompt_text')!=cell['prompt_text'] or row.get('system_prompt')!=config['system_prompt']:
        raise ValueError('stored prompt/system text differs from frozen independent request')
    expected={'model':model,'max_output_tokens':config['max_output_tokens'],'tools_enabled':False,'external_grounding':False}
    if row.get('request_parameters')!=expected:raise ValueError('stored inference settings differ from frozen configuration')


def triplets(keys):
    by_task={}
    for task,language in keys:by_task.setdefault(task,set()).add(language)
    return {task for task,languages in by_task.items() if languages==set(LANGUAGES)}


def audit():
    config,manifest,freeze,annotations,prompts=gen.verify();gen.authorize(config,manifest)
    root=gen.four.output_root(config)
    started=gen.four.historical.utc_now();stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    dest=gen.ROOT/'.local/generation_metadata_checkpoints'/stamp;dest.mkdir(parents=True,mode=0o700)
    models={};completed_sets={};pins=gen.provenance()
    for provider in gen.four.PARTITIONS:
        path=root/(provider+'.jsonl');data=path.read_bytes() if path.exists() else b''
        acquired=gen.four.historical.utc_now();prefix,rows,tail=complete_prefix(data)
        saved=dest/(provider+'.jsonl');saved.write_bytes(prefix);os.chmod(saved,0o600)
        selected=gen.cells(config,freeze,annotations,prompts,provider)
        expected={(c['task_id'],c['language']):c for c in selected}
        done,errors=gen.four.validated_records(saved,config,provider,selected,pins)
        model=next(m for m in config['models'] if m['partition']==provider)
        for row in rows:validate_request_record(row,expected[row['task_id'],row['language']],config,model)
        actual_order=[(r['task_id'],r['language']) for r in rows if r['status']=='success']
        expected_order=[(c['task_id'],c['language']) for c in selected]
        if actual_order!=expected_order[:len(actual_order)]:raise ValueError('successful cells do not follow the frozen per-model order')
        keys=set(done);complete=triplets(keys);completed_sets[provider]=complete
        counts=Counter(language for _,language in keys)
        planned_domain=Counter(c['domain'] for c in selected);actual_domain=Counter(r['domain'] for r in done.values())
        models[provider]={'model_id':model['model_id'],'role':'primary' if provider in PRIMARY else 'exploratory','success':len(done),'planned':len(selected),
          'by_language':{l:counts[l] for l in LANGUAGES},'complete_task_triplets':len(complete),'planned_tasks':len({c['task_id'] for c in selected}),
          'paired_en_bn_tasks':len({t for t,l in keys if l=='en'}&{t for t,l in keys if l=='bn'}),
          'paired_bn_bn_cs_tasks':len({t for t,l in keys if l=='bn'}&{t for t,l in keys if l=='bn_cs'}),
          'by_domain':{d:{'success':actual_domain[d],'planned':planned_domain[d]} for d in sorted(planned_domain)},
          'failed_response_records':errors,'truncated':sum(bool(r.get('truncated')) for r in done.values()),
          'empty_visible_text':sum(not r['response_text'].strip() for r in done.values()),
          'finish_status_counts':dict(Counter(str(r.get('finish_status')) for r in done.values())),
          'prefix_acquired_at_utc':acquired,'prefix_file':str(saved.relative_to(gen.ROOT)),'prefix_sha256':hashlib.sha256(prefix).hexdigest(),
          'prefix_bytes':len(prefix),'prefix_records':len(rows),'incomplete_final_write_bytes_excluded':tail,
          'checks_passed':['stored prompt/system text matches freeze','recorded inference settings match freeze','frozen seeded cell order','task/language membership','model identity and provenance','response SHA256','no duplicate successful cell']}
    matched=set.intersection(*(completed_sets[p] for p in PRIMARY))
    result={'status':'PASS','started_at_utc':started,'completed_at_utc':gen.four.historical.utc_now(),
      'execution_amendment_id':gen.AMENDMENT_ID,'manifest_sha256':gen.four.digest(gen.MANIFEST),'audit_script_sha256':gen.four.digest(Path(__file__)),
      'primary_completed':sum(models[p]['success'] for p in PRIMARY),'primary_planned':1413,'exploratory_completed':models['google']['success'],'exploratory_planned':60,
      'tasks_with_all_nine_primary_responses':len(matched),'tasks_with_all_twelve_matched_responses':len(matched&completed_sets['google']),
      'models':models,'production_scoring_authorized':False,
      'interpretation':'Objective collection/integrity metadata only. A preserved response or language triplet does not establish semantic completion, safety, RIU fulfillment or trustworthiness.',
      'capture_limit':'Each model uses an immutable newline-complete raw-log prefix; model captures occur sequentially, not at one globally atomic instant. Active final writes are excluded explicitly. Attempt/quota/budget state remains in the separate live checkpoint.',
      'private_raw_checkpoint':str(dest.relative_to(gen.ROOT))}
    encoded=json.dumps(result,indent=2)+'\n';(dest/'AUDIT.json').write_text(encoded);os.chmod(dest/'AUDIT.json',0o600)
    temp=PUBLIC.with_suffix('.tmp');temp.write_text(encoded);temp.replace(PUBLIC)
    lines=['# Generation integrity checkpoint','', 'Completed: '+result['completed_at_utc']+'. Collection continues after this checkpoint.','',
      '| Model | EN | BN | BN-CS | Preserved / planned | Complete language triplets |',
      '|---|---:|---:|---:|---:|---:|']
    for model in models.values():
        c=model['by_language'];lines.append(f"| {model['model_id']} | {c['en']} | {c['bn']} | {c['bn_cs']} | {model['success']} / {model['planned']} | {model['complete_task_triplets']} / {model['planned_tasks']} |")
    lines += ['',f"Tasks with all nine primary responses: **{len(matched)}/157**. Tasks with all twelve matched primary/exploratory responses: **{len(matched&completed_sets['google'])}/20**.",'',
      'Each per-model checkpoint preserves the exact newline-complete bytes used for its counts and hashes. Full raw prefixes remain private and unchanged under the checkpoint path recorded in GENERATION_INTEGRITY.json. Active incomplete final writes are excluded and counted explicitly; completed malformed records fail the audit. Model captures occur sequentially, rather than at one globally atomic instant.','',
      'Checks cover recorded prompt/system text, inference settings, frozen seeded order, task/language membership, model identity/provenance, response hashes and duplicate successful cells. They verify data integrity, not semantic completion, correctness, safety or RIU fulfillment. No production scoring occurs.','',
      'Partial language-pair and triplet counts describe collection coverage only. Models have different completion stages and local models share a sequential GPU schedule. Do not interpret partial counts as model rankings or language effects. The separate live generation checkpoint reports attempts, quotas and budget with its own timestamp.','',
      'Staff can create another immutable prefix checkpoint with `python3 scripts/audit_generation_metadata_v04.py`; no model API calls are made. R1 does not need to run this command.']
    PUBLIC.with_suffix('.md').write_text('\n'.join(lines)+'\n')
    return result

if __name__=='__main__':
    r=audit();print(json.dumps({k:r[k] for k in ('status','completed_at_utc','primary_completed','exploratory_completed','tasks_with_all_nine_primary_responses','private_raw_checkpoint')},indent=2))
