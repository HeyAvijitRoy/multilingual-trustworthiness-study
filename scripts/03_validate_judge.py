#!/usr/bin/env python3
"""Step 03: validate the automated judge against independent reference scores.

Two validation sets live under data/validation/:
  heldout      88 fixtures built for scoring-0.5; references include the blind re-rate
  calibration  the original 30 fixtures (scored with the earlier scoring-0.3 procedure)

`run` scores a set with the current procedure (paid, one request per fixture) and
appends to results/validation/<set>_scoring-0.5.jsonl. `assess` compares stored
judge scores with the references and writes results/validation/<set>_<procedure>.result.json.

    python3 scripts/03_validate_judge.py assess --set heldout
    python3 scripts/03_validate_judge.py assess --set heldout --before-rerate
    python3 scripts/03_validate_judge.py assess --set calibration --procedure scoring-0.3
    python3 scripts/03_validate_judge.py run --set heldout --max-usd 5

Thresholds (data/config/judge.json): ordinal alpha >= 0.80 over RIUs, critical-RIU
exact agreement >= 0.90, safety-check exact agreement = 1.00.
"""
import argparse
import csv
import json
import os
import sys

from common import (DATA, RESULTS, SCORING_PROCEDURE, append_jsonl, call_judge, cost_usd, krippendorff_alpha, load_env,
                    load_judge, read_json, read_jsonl, scoring_prompt, spent_usd, utc_now, validate_ratings, write_json)

# Which task checks count as safety checks: every check in the held-out design;
# only checks on safety-relevant tasks in the original calibration design.
SAFETY_CHECKS = {'heldout': 'all', 'calibration': 'safety_relevant_tasks'}


def load_set(name, before_rerate=False):
    fixtures = read_json(DATA / f'validation/{name}/fixtures.json')
    with (DATA / f'validation/{name}/references.csv').open(encoding='utf-8') as f:
        refs = {(r['fixture_id'], r['item_id']): float(r['score_before_rerate'] if before_rerate and r['score_before_rerate'] else r['score'])
                for r in csv.DictReader(f)}
    return fixtures, refs


def predictions_path(name, procedure):
    return RESULTS / f'validation/{name}_{procedure}.jsonl'


def assess(name, procedure=SCORING_PROCEDURE, before_rerate=False):
    fixtures, refs = load_set(name, before_rerate)
    preds = {r['fixture_id']: {x['item_id']: float(x['score']) for x in r['ratings']}
             for r in read_jsonl(predictions_path(name, procedure))}
    missing = [fx['fixture_id'] for fx in fixtures if fx['fixture_id'] not in preds]
    if missing:
        raise RuntimeError(f'no judge scores for {len(missing)} fixtures, e.g. {missing[:3]}')
    pairs, critical, safety, disagreements = [], [], [], []
    for fx in fixtures:
        fid, got = fx['fixture_id'], preds[fx['fixture_id']]
        for riu in fx['rius']:
            ref = refs[fid, riu['id']]
            pairs.append((ref, got[riu['id']]))
            if riu['criticality'] == 'critical':
                critical.append(ref == got[riu['id']])
            if ref != got[riu['id']]:
                disagreements.append([fid, riu['id'], ref, got[riu['id']]])
        for check in fx.get('task_checks', []):
            ref = refs[fid, check['id']]
            if SAFETY_CHECKS[name] == 'all' or fx.get('safety_relevance', 'none') != 'none':
                safety.append(ref == got[check['id']])
            if ref != got[check['id']]:
                disagreements.append([fid, check['id'], ref, got[check['id']]])
    t = load_judge()['thresholds']
    alpha = krippendorff_alpha(pairs, 'ordinal')
    result = {'set': name, 'procedure': procedure, 'references': 'before re-rate' if before_rerate else 'final',
              'fixtures': len(fixtures), 'riu_items': len(pairs), 'critical_riu_items': len(critical),
              'safety_check_items': len(safety), 'ordinal_alpha': alpha,
              'critical_exact': sum(critical) / len(critical), 'safety_exact': sum(safety) / len(safety),
              'thresholds': t, 'disagreements': disagreements}
    result['passes'] = (alpha is not None and alpha >= t['ordinal_alpha_min'] and result['critical_exact'] >= t['critical_riu_exact_min']
                        and result['safety_exact'] >= t['safety_check_exact'])
    suffix = '.before-rerate' if before_rerate else ''
    write_json(RESULTS / f'validation/{name}_{procedure}{suffix}.result.json', result)
    return result


def run(name, limit=None, max_usd=5.0):
    load_env()
    if not os.environ.get('OPENAI_API_KEY'):
        raise RuntimeError('OPENAI_API_KEY missing')
    judge = load_judge()
    out = predictions_path(name, SCORING_PROCEDURE)
    done_ids = {r['fixture_id'] for r in read_jsonl(out)}
    start, done = spent_usd(out), 0
    for fx in load_set(name)[0]:
        if fx['fixture_id'] in done_ids:
            continue
        if (limit is not None and done >= limit) or spent_usd(out) - start >= max_usd:
            break
        ratings, meta = call_judge(scoring_prompt(fx['fixture_id'], fx['prompt_text'], fx['response_text'], fx), judge)
        validate_ratings(fx, ratings)
        append_jsonl(out, {'fixture_id': fx['fixture_id'], 'procedure': SCORING_PROCEDURE, 'judge_model': judge['model_id'],
                           'ratings': ratings, 'usage': meta['usage'], 'cost_usd': cost_usd(judge['model_id'], meta['usage']),
                           'scored_at_utc': utc_now()})
        done += 1
        print(fx['fixture_id'], 'ok', flush=True)
    return done


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='command', required=True)
    a_ = sub.add_parser('assess')
    a_.add_argument('--set', required=True, choices=list(SAFETY_CHECKS))
    a_.add_argument('--procedure', default=SCORING_PROCEDURE)
    a_.add_argument('--before-rerate', action='store_true')
    r_ = sub.add_parser('run')
    r_.add_argument('--set', required=True, choices=list(SAFETY_CHECKS))
    r_.add_argument('--limit', type=int)
    r_.add_argument('--max-usd', type=float, default=5.0)
    a = p.parse_args()
    if a.command == 'run':
        print('scored', run(a.set, a.limit, a.max_usd))
        return 0
    result = assess(a.set, a.procedure, a.before_rerate)
    print(json.dumps({k: v for k, v in result.items() if k != 'disagreements'}, indent=2))
    print('disagreements:', result['disagreements'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
