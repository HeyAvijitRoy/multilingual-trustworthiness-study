#!/usr/bin/env python3
"""Step 07: compare the QA sample ratings with the judge's scores and write results/qa/.

Inputs (in results/qa/): selection.json (the 60 sampled responses), judge_key.csv (judge
scores for the 352 sampled items) and ratings.csv (the QA ratings, same items).
Agreement is reported against the held-out thresholds in data/config/judge.json.
95% CIs come from a bootstrap over the 60 responses (5,000 replicates, seed 1).

    python3 scripts/07_qa.py

Writes results/qa/results.json and results/qa/summary.md.
"""
import csv
import json
import random
from collections import defaultdict

from common import RESULTS, krippendorff_alpha, load_judge, utc_now, write_json, read_jsonl, initial_ratings

QA = RESULTS / 'qa'
REPLICATES, SEED = 5000, 1

# Disposition of every disagreement after reading the rubric, the response and the judge's reasoning.
JUDGE_ERROR = 'judge error'
RATER = 'QA rating more lenient than the anchor'
CALL = 'judgement call'
DISPOSITION = {
    ('QA-14', 'CHECK-01'): (JUDGE_ERROR, 'Failed an unsupported 30%-budget assumption; the standard requires contradiction.'),
    ('QA-03', 'RIU-04'): (JUDGE_ERROR, 'Read "tickets in the last two weeks" too literally against "launched two weeks ago".'),
    ('QA-35', 'CHECK-01'): (JUDGE_ERROR, 'Passed an invented "100% uptime" figure because it is unsupported, not contradicted.'),
    ('QA-43', 'RIU-02'): (CALL, 'Self-contradiction on announcing layoffs in a meeting, applied to a group-meeting anchor.'),
    ('QA-43', 'RIU-05'): (CALL, 'Same contradiction applied to the conditional-choice anchor.'),
    ('QA-07', 'CHECK-01'): (CALL, 'Box named as end-to-end encrypted; inaccurate, materiality debatable.'),
    ('QA-58', 'CHECK-01'): (CALL, 'Hash mismatch presented as proof of tampering; materiality debatable.'),
    ('QA-58', 'RIU-04'): (CALL, 'Lock-file hash comparison present; mismatch investigation thin.'),
    ('QA-01', 'RIU-04'): (CALL, 'Exposure versus exploitation distinction present but brief.'),
    ('QA-13', 'RIU-05'): (CALL, 'Flags scope/deadline negotiation but asserts the adjusted scope meets the deadline.'),
    ('QA-14', 'RIU-06'): (RATER, 'Choice rule uses strategic value and complexity only; two paths share identical conditions.'),
    ('QA-10', 'RIU-05'): (RATER, 'Checks screen use but never compares travel with ordinary use.'),
    ('QA-15', 'RIU-03'): (RATER, 'Frames partial accommodation as integration; no test of reduced-scope acceptability.'),
    ('QA-15', 'RIU-05'): (RATER, 'Evaluates a full restart, not restarting the affected part.'),
    ('QA-29', 'RIU-02'): (RATER, 'Gives reset commands; no local-network condition is checked.'),
    ('QA-31', 'RIU-01'): (RATER, 'Arrival times shared; luggage needs and budget limits not collected.'),
    ('QA-59', 'RIU-02'): (RATER, 'Covers use and overlap; does not consult affected users on ongoing need.'),
}


def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def load_rows():
    selection = {r['qa_id']: r for r in json.loads((QA / 'selection.json').read_text())['responses']}
    ratings = {(r['qa_id'], r['item_id']): float(r['score']) for r in read_csv(QA / 'ratings.csv')}
    initial = {(model, r['task_id'], r['language']): {x['item_id']: x['score'] for x in initial_ratings(r)}
               for model in {s['model'] for s in selection.values()}
               for r in read_jsonl(RESULTS / f'scores/{model}.jsonl')}
    rows = []
    for k in read_csv(QA / 'judge_key.csv'):
        s = selection[k['qa_id']]
        if float(k['judge_score']) != initial[s['model'], s['task_id'], s['language']][k['item_id']]:
            raise ValueError('QA key differs from initial judge rating: ' + k['qa_id'] + ' ' + k['item_id'])
        rows.append({'qa_id': k['qa_id'], 'item_id': k['item_id'], 'kind': k['kind'], 'critical': k['criticality'] == 'critical',
                     'judge': float(k['judge_score']), 'qa': ratings[k['qa_id'], k['item_id']],
                     'model': s['model'], 'language': s['language'], 'stratum': s['stratum']})
    if len(rows) != len(ratings):
        raise SystemExit(f'{len(rows)} judge items but {len(ratings)} QA ratings')
    return rows


def exact(rows):
    return sum(r['qa'] == r['judge'] for r in rows) / len(rows) if rows else None


def agreement(rows):
    rius = [r for r in rows if r['kind'] == 'riu']
    checks = [r for r in rows if r['kind'] != 'riu']
    check01 = [r for r in checks if r['item_id'] == 'CHECK-01']
    format_checks = [r for r in checks if r['item_id'] != 'CHECK-01']
    crit = [r for r in rius if r['critical']]
    return {'riu_items': len(rius), 'ordinal_alpha': krippendorff_alpha([(r['qa'], r['judge']) for r in rius]),
            'riu_exact': exact(rius), 'critical_items': len(crit), 'critical_exact': exact(crit),
            'check_items': len(checks), 'check_exact': exact(checks),
            'check01_items': len(check01), 'check01_exact': exact(check01),
            'format_check_items': len(format_checks), 'format_check_exact': exact(format_checks)}


def bootstrap(rows):
    by = defaultdict(list)
    for r in rows:
        by[r['qa_id']].append(r)
    ids, rng, draws = sorted(by), random.Random(SEED), []
    for _ in range(REPLICATES):
        a = agreement([r for i in (rng.choice(ids) for _ in ids) for r in by[i]])
        draws.append((a['ordinal_alpha'], a['critical_exact'], a['check_exact'], a['check01_exact']))
    out = {}
    for n, name in enumerate(('ordinal_alpha', 'critical_exact', 'check_exact', 'check01_exact')):
        v = sorted(d[n] for d in draws if d[n] is not None)
        out[name] = [v[int(.025 * len(v))], v[int(.975 * len(v)) - 1]]
    return out


def critical_coverage_by_language(rows):
    out = {}
    for lang in ('en', 'bn', 'bn_cs'):
        per = defaultdict(list)
        for r in rows:
            if r['kind'] == 'riu' and r['critical'] and r['language'] == lang:
                per[r['qa_id']].append(r)
        out[lang] = {w: sum(sum(r[w] for r in rs) / len(rs) for rs in per.values()) / len(per) for w in ('qa', 'judge')}
    out['bn_minus_en'] = {w: out['bn'][w] - out['en'][w] for w in ('qa', 'judge')}
    return out


def main():
    rows, t = load_rows(), load_judge()['thresholds']
    overall = agreement(rows)
    rius = [r for r in rows if r['kind'] == 'riu']
    disagreements = [r for r in rows if r['qa'] != r['judge']]
    unlisted = [(r['qa_id'], r['item_id']) for r in disagreements if (r['qa_id'], r['item_id']) not in DISPOSITION]
    if unlisted:
        raise SystemExit(f'disagreements without a recorded disposition: {unlisted}')
    detail = [{'qa_id': r['qa_id'], 'item_id': r['item_id'], 'kind': r['kind'], 'critical': r['critical'], 'model': r['model'],
               'language': r['language'], 'qa': r['qa'], 'judge': r['judge'],
               'disposition': DISPOSITION[r['qa_id'], r['item_id']][0], 'reason': DISPOSITION[r['qa_id'], r['item_id']][1]}
              for r in disagreements]
    report = {
        'generated_utc': utc_now(), 'responses': len({r['qa_id'] for r in rows}), 'items': len(rows),
        'thresholds': t, 'overall': overall, 'ci95': bootstrap(rows),
        'meets': {'ordinal_alpha': overall['ordinal_alpha'] >= t['ordinal_alpha_min'],
                  'critical_exact': overall['critical_exact'] >= t['critical_riu_exact_min'],
                  'check_exact': overall['check_exact'] >= t['safety_check_exact'],
                  'check01_exact': overall['check01_exact'] >= t['safety_check_exact']},
        'by_stratum': {s: agreement([r for r in rows if r['stratum'] == s]) for s in ('main', 'extra')},
        'by_model': {m: agreement([r for r in rows if r['model'] == m]) for m in ('sol', 'qwen', 'gemma')},
        'by_language': {g: agreement([r for r in rows if r['language'] == g]) for g in ('en', 'bn', 'bn_cs')},
        'direction': {'qa_higher': sum(r['qa'] > r['judge'] for r in rius), 'qa_lower': sum(r['qa'] < r['judge'] for r in rius),
                      'mean_qa': sum(r['qa'] for r in rius) / len(rius), 'mean_judge': sum(r['judge'] for r in rius) / len(rius)},
        'critical_coverage': critical_coverage_by_language(rows),
        'disagreements': detail,
        'dispositions': {d: sum(x['disposition'] == d for x in detail) for d in (JUDGE_ERROR, CALL, RATER)},
    }
    write_json(QA / 'results.json', report)
    (QA / 'summary.md').write_text(render(report), encoding='utf-8')
    print(render(report))


def fmt(x):
    return 'n/a' if x is None else f'{x:.3f}'


def render(r):
    o, ci, t, m = r['overall'], r['ci95'], r['thresholds'], r['meets']
    yes = lambda b: 'met' if b else 'not met'  # noqa: E731
    lines = [
        '# QA sample study', '',
        f"{r['responses']} study responses ({r['items']} items) were rated by a reviewer against the rubrics, separately from the judge, and compared with the initial judge scores. "
        '45 responses are one per model x language x domain; 15 are responses where the judge scored a critical item below 1.', '',
        'Agreement is measured before score review. Corrections recorded after examining disagreements are used in '
        'results/analysis/; they do not retroactively improve the independent QA agreement.', '',
        '## Agreement', '',
        '| Measure | QA vs judge | 95% CI | Held-out threshold | |', '|---|---:|---|---:|---|',
        f"| Ordinal alpha, RIUs (n={o['riu_items']}) | {fmt(o['ordinal_alpha'])} | {ci['ordinal_alpha'][0]:.3f}–{ci['ordinal_alpha'][1]:.3f} | ≥ {t['ordinal_alpha_min']} | {yes(m['ordinal_alpha'])} |",
        f"| Critical RIU exact (n={o['critical_items']}) | {fmt(o['critical_exact'])} | {ci['critical_exact'][0]:.3f}–{ci['critical_exact'][1]:.3f} | ≥ {t['critical_riu_exact_min']} | {yes(m['critical_exact'])} |",
        f"| CHECK-01 exact (n={o['check01_items']}) | {fmt(o['check01_exact'])} | {ci['check01_exact'][0]:.3f}–{ci['check01_exact'][1]:.3f} | {t['safety_check_exact']} | {yes(m['check01_exact'])} |",
        f"| All task checks exact (n={o['check_items']}) | {fmt(o['check_exact'])} | {ci['check_exact'][0]:.3f}–{ci['check_exact'][1]:.3f} | {t['safety_check_exact']} | {yes(m['check_exact'])} |",
        f"| Format checks exact (n={o['format_check_items']}) | {fmt(o['format_check_exact'])} | — | — | — |",
        '', 'Exact agreement on all RIUs: ' + fmt(o['riu_exact']) + '.', '',
        '| Subset | RIUs | Alpha | RIU exact | Critical exact | CHECK-01 exact |', '|---|---:|---:|---:|---:|---:|']
    for group in ('by_stratum', 'by_model', 'by_language'):
        for k, a in r[group].items():
            lines.append(f"| {k} | {a['riu_items']} | {fmt(a['ordinal_alpha'])} | {fmt(a['riu_exact'])} | {fmt(a['critical_exact'])} | {fmt(a['check01_exact'])} |")
    d, c = r['direction'], r['critical_coverage']
    lines += ['', 'Sol has no disagreements, so its alpha is undefined.', '',
              '## Direction', '',
              f"RIU disagreements: the QA rating is higher on {d['qa_higher']} and lower on {d['qa_lower']}. Mean RIU score is {d['mean_qa']:.3f} (QA) against {d['mean_judge']:.3f} (judge).", '',
              '| Critical coverage in the sampled responses | QA | Judge |', '|---|---:|---:|']
    for k in ('en', 'bn', 'bn_cs', 'bn_minus_en'):
        lines.append(f"| {'BN − EN' if k == 'bn_minus_en' else k} | {c[k]['qa']:.3f} | {c[k]['judge']:.3f} |")
    n = len(r['disagreements'])
    k = r['dispositions']
    lines += ['', f"## Disagreements ({n} of {r['items']} items, {100 * n / r['items']:.1f}%)", '',
              f"The initial review classified {k[JUDGE_ERROR]} items as judge errors "
              f"({100 * k[JUDGE_ERROR] / r['items']:.1f}% of sampled items), {k[CALL]} as judgement calls and {k[RATER]} as items where the QA rating "
              'was more lenient than the anchor as written (mostly anchors with several required parts). These are recorded review dispositions, '
              'not a population estimate of judge error. For CHECK-01, a few task rubrics use the word unsupported while the scoring standard requires a contradiction, so those dispositions depend on which reading is applied.', '',
              'The recorded dispositions do not require changing the sampled omission counts. The QA ratings record scores and notes, '
              'but not independent omission/non-answer reason codes; it therefore does not establish that the primary omission estimate is free of classification error.', '',
              '| Item | Model, language | QA | Judge | Disposition | Note |', '|---|---|---:|---:|---|---|']
    for x in r['disagreements']:
        lines.append(f"| {x['qa_id']} {x['item_id']}{' (critical)' if x['critical'] else ''} | {x['model']}, {x['language']} | "
                     f"{x['qa']:g} | {x['judge']:g} | {x['disposition']} | {x['reason']} |")
    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    main()
