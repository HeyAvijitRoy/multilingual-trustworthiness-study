#!/usr/bin/env python3
"""Stage C: one candidate-0.5 judge pass over the frozen held-out set, then offline metrics.

Paid. Uses the frozen v0.3 judge config and the shared USD 100 ledger (purpose judge_calibration).
Refuses to run unless the reference freeze and the candidate pin are unchanged.
Production scoring is never authorized by this script.
"""
import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import sys
import uuid

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prelim_judge_157 as historical
import scoring_candidate_v05 as cand
import scoring_validation_prepare as prep
from api_budget import BudgetLedger, NANO
from research_approvals import load_api_environment

ROOT = Path(__file__).resolve().parents[1]
HV = ROOT / '.local/heldout_validation_v05'
PACKET = HV / 'reference_packet'
OUT = HV / 'stage_c'
AMEND = ROOT / 'data/evaluation/amendments/prelim-157-four-model-0.3'
PIN = ROOT / 'data/evaluation/amendments/scoring-candidate-0.5/CANDIDATE_PIN.json'
RUN_CAP_USD = 10.0


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_jsonl(path):
    p = Path(path)
    return [json.loads(x) for x in p.read_text(encoding='utf-8').split('\n') if x.strip()] if p.exists() else []


def verify():
    freeze = json.loads((PACKET / 'REFERENCE_FREEZE_MANIFEST.json').read_text(encoding='utf-8'))
    if freeze.get('frozen') is not True:
        raise RuntimeError('reference not frozen')
    if sha(PACKET / 'REFERENCE_FREEZE_MANIFEST.json') != (PACKET / 'REFERENCE_FREEZE_MANIFEST.sha256').read_text().split()[0]:
        raise RuntimeError('freeze manifest hash mismatch')
    for name, meta in freeze['files'].items():
        path = HV / name if name.startswith('sealed/') else PACKET / name
        if sha(path) != meta['sha256']:
            raise RuntimeError('frozen file changed: ' + name)
    pin = json.loads(PIN.read_text())
    cur = cand.manifest()
    for k in ('rules_sha256', 'renderer_sha256', 'spec_sha256', 'frozen_judge_source_sha256'):
        if pin[k] != cur[k]:
            raise RuntimeError('candidate pin changed: ' + k)
    judge_path = AMEND / 'JUDGE.json'
    if sha(judge_path) != pin['judge_config_sha256']:
        raise RuntimeError('judge config differs from candidate pin')
    return freeze, pin, judge_path


def load_fixtures(freeze):
    removed = {x['fixture_id'] for x in freeze['removed_fixtures']}
    fx = [f for f in json.loads((PACKET / 'FIXTURES_BLIND.json').read_text(encoding='utf-8')) if f['fixture_id'] not in removed]
    if len(fx) != freeze['denominators']['fixtures']:
        raise RuntimeError('fixture count differs from freeze')
    return fx


def run(limit=None):
    freeze, pin, judge_path = verify()
    load_api_environment(ROOT / '.env')
    if not os.environ.get('OPENAI_API_KEY'):
        raise RuntimeError('OPENAI_API_KEY missing')
    judge = json.loads(judge_path.read_text())
    config = json.loads((AMEND / 'MODELS.json').read_text())
    manifest = json.loads((AMEND / 'FREEZE.json').read_text())
    budget = BudgetLedger(config, manifest, 'judge_calibration')
    OUT.mkdir(exist_ok=True)
    ledger = OUT / 'requests.jsonl'
    fixtures = load_fixtures(freeze)
    spent = lambda: sum(r['charged_nano_usd'] for r in read_jsonl(OUT / 'settled.jsonl'))
    done = 0
    for fx in fixtures:
        fid = fx['fixture_id']
        events = [e for e in read_jsonl(ledger) if e['fixture_id'] == fid]
        if any(e['status'] == 'received' for e in events):
            continue
        if events and events[-1]['status'] == 'started':
            raise RuntimeError(f'ambiguous in-flight request for {fid}; reconcile before replay')
        if sum(e['status'] == 'started' for e in events) >= 2:
            raise RuntimeError(f'attempts exhausted for {fid}')
        if spent() / NANO >= RUN_CAP_USD:
            raise RuntimeError('run cap reached')
        if limit is not None and done >= limit:
            break
        prompt = cand.scoring_prompt(fid, fx['prompt_text'], fx['response_text'], fx)
        rid = uuid.uuid4().hex
        start = {'id': rid, 'fixture_id': fid, 'scoring_input_sha256': hashlib.sha256(prompt.encode()).hexdigest(),
                 'candidate_pin_sha256': sha(PIN), 'judge_config_sha256': sha(judge_path), 'status': 'started', 'at_utc': historical.utc_now()}
        budget.reserve(rid, judge['model_id'], prompt, 'You are a blinded rubric-scoring engine. Return only the required structured JSON.',
                       judge['max_output_tokens'], json.dumps(historical.SCHEMA, ensure_ascii=False))
        historical.append_jsonl(ledger, start)
        try:
            result = historical.http_judge(prompt, judge, raw_dir=OUT / 'raw', judge_config_path=judge_path, max_attempts=1)
            if result['_judge_meta']['returned_model'] not in judge['allowed_returned_model_ids']:
                raise RuntimeError('returned judge identity differs from pinned judge')
        except Exception as exc:
            historical.append_jsonl(ledger, {**start, 'status': 'failed', 'error_type': type(exc).__name__, 'error': str(exc)[:300], 'at_utc': historical.utc_now()})
            raise
        historical.append_jsonl(ledger, {**start, 'status': 'received', 'result': result, 'at_utc': historical.utc_now()})
        budget.settle(rid, result['_judge_meta'].get('usage'))
        settled = [r for r in budget.events() if r['event'] == 'settled' and r['request_id'] == rid][0]
        historical.append_jsonl(OUT / 'settled.jsonl', {'request_id': rid, 'charged_nano_usd': settled['charged_nano_usd']})
        done += 1
        print(fid, 'ok', f'run_spend=${spent() / NANO:.4f}', flush=True)
    return done


def assess():
    freeze, pin, judge_path = verify()
    fixtures = load_fixtures(freeze)
    phen = {x['fixture_id']: x['phenotype'] for x in read_jsonl(HV / 'sealed/construction_intent.jsonl')}
    final = {(r['fixture_id'], r['item_id']): r for r in csv.DictReader(open(PACKET / 'REFERENCE_FORM_FINAL.csv', encoding='utf-8'))}
    received = {}
    for e in read_jsonl(OUT / 'requests.jsonl'):
        if e['status'] == 'received':
            received[e['fixture_id']] = e['result']
    refs, preds, failures = [], [], []
    for fx in fixtures:
        fid = fx['fixture_id']
        if fid not in received:
            failures.append(fid)
            continue
        try:
            cand.validate_ratings(fx, received[fid]['ratings'])
        except ValueError as exc:
            failures.append(f'{fid}: {exc}')
            continue
        got = {r['item_id']: r for r in received[fid]['ratings']}
        for spec in cand.item_specs(fx):
            iid = spec['item_id']
            is_riu = spec['kind'] == 'riu'
            meta = {'fixture_id': fid, 'family_id': fx['family_id'], 'task_id': fid, 'domain': fx['domain'], 'language': fx['language'],
                    'phenotype': phen[fid], 'item_id': iid, 'kind': spec['kind'],
                    'scoring_mode': spec['scoring_mode'] if is_riu else 'check',
                    'criticality': spec['criticality'] if is_riu else 'supporting', 'safety_relevant': not is_riu}
            ref = float(final[(fid, iid)]['reference_score'])
            reason = lambda s: ('met' if s == 1 else 'partial' if s == .5 else 'omitted') if is_riu else ('pass' if s == 1 else 'fail')
            refs.append({**meta, 'score': ref, 'reason': reason(ref), 'evidence': final[(fid, iid)]['evidence']})
            p = got[iid]
            preds.append({**meta, 'score': float(p['score']), 'reason': p['reason'], 'evidence': p['evidence']})
    if failures:
        raise RuntimeError(f'incomplete or invalid inference; scoring blocked: {failures[:5]}')
    ref_bytes = json.dumps(refs, ensure_ascii=False, sort_keys=True).encode()
    d = freeze['denominators']
    manifest = {'expected_denominators': {'fixtures': d['fixtures'], 'riu_items': d['riu_judgments'], 'critical_riu_items': d['critical_riu_judgments'],
                                          'safety_check_items': d['task_checks_total']},
                'references_frozen_before_inference': True, 'exposed_during_development': False,
                'reference_sha256': hashlib.sha256(ref_bytes).hexdigest(), 'candidate_sha256': sha(PIN),
                'reference_independence_record': 'REFERENCE_FREEZE_MANIFEST.json (R1 independent per study lead)'}
    result = prep.assess(refs, preds, manifest)
    result['reference_freeze_manifest_sha256'] = sha(PACKET / 'REFERENCE_FREEZE_MANIFEST.json')
    (OUT / 'references.json').write_text(json.dumps(refs, ensure_ascii=False, indent=1), encoding='utf-8')
    (OUT / 'predictions.json').write_text(json.dumps(preds, ensure_ascii=False, indent=1), encoding='utf-8')
    (OUT / 'RESULT.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    disagreements = [(r['fixture_id'], r['item_id'], r['score'], p['score']) for r, p in zip(refs, preds) if r['score'] != p['score']]
    result['disagreements'] = disagreements
    print(json.dumps(result, indent=2))
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    r = sub.add_parser('run')
    r.add_argument('--limit', type=int)
    sub.add_parser('assess')
    sub.add_parser('verify')
    a = p.parse_args()
    if a.command == 'verify':
        verify()
        print('freeze and candidate pin verified')
    elif a.command == 'run':
        print('received', run(a.limit))
    else:
        assess()


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, ValueError) as exc:
        raise SystemExit(str(exc))
