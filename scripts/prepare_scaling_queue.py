"""Prepare/check a deterministic 500-task annotation work queue, without annotating."""
import argparse
from collections import Counter
import json
from pathlib import Path
from validate_pilot_annotations import ANN, FILES, read_jsonl, validate_freeze
from validate_prompt_corpus import load_rows

TARGET = ANN/'SCALING_QUEUE.json'

def queue():
    validate_freeze()
    pilot = {r['task_id']: r for f in FILES for r in read_jsonl(ANN/f)}
    prompts = sorted(load_rows(), key=lambda r: r['task_id'])
    represented = {(r['domain'], r['subdomain'], r['difficulty']) for r in prompts if r['task_id'] in pilot}
    selected = set()
    rows = []
    for row in prompts:
        key = (row['domain'], row['subdomain'], row['difficulty'])
        expansion = row['task_id'] not in pilot and key not in represented and key not in selected
        if expansion: selected.add(key)
        rows.append({k:row[k] for k in ['task_id', 'domain', 'subdomain', 'difficulty']} | {
            'annotation_status': pilot[row['task_id']]['status'] if row['task_id'] in pilot else 'not-annotated',
            'next_step': {'frozen': 'gold-frozen', 'human-reviewed': 'gold-sign-off'}.get(pilot[row['task_id']]['status'], 'human-validation') if row['task_id'] in pilot else ('expansion-calibration' if expansion else 'after-calibration-gate')})
    return {'schema_version':'0.2','gate':'pending-expanded-calibration',
            'selection_rule':'First task_id in each domain/subdomain/difficulty stratum absent from the original pilot; calibrate before production batches.',
            'tasks':rows}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    result=queue(); encoded=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if args.check:
        if not TARGET.exists() or TARGET.read_text(encoding='utf-8')!=encoded:
            raise SystemExit('Scaling queue is missing or stale; run scripts/prepare_scaling_queue.py')
    else: TARGET.write_text(encoded, encoding='utf-8', newline='\n')
    print('Scaling queue verified:',len(result['tasks']),'tasks;',dict(Counter(r['next_step'] for r in result['tasks'])))
if __name__=='__main__': main()
