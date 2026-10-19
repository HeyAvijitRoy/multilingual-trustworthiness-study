"""Scoring-calibration fixtures and two-rater agreement for the frozen pilot gold.

Standard library only; no model calls, and it never writes response text.

  python3 scripts/calibration.py check                       # validate plan, fixtures, key, preregistration
  python3 scripts/calibration.py sheets --rater R2 --rater R3  # blind packet + score sheet per rater
  python3 scripts/calibration.py agreement SHEET_A SHEET_B [--out REPORT.md]

Fixture preparation follows ANNOTATION_PROTOCOL.md. Sheets are written to
data/calibration/sheets/; distribute each rater's pair privately and keep the answer
key away from raters until both sheets are returned.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import csv
import datetime as dt
import json
from pathlib import Path
import random
import re
from validate_pilot_annotations import ROOT, ANN, FILES, read_jsonl, validate_freeze, validate_gold_freeze
from validate_prompt_corpus import load_rows

CAL = ROOT / 'data' / 'calibration'
LANGS = {'en': 'prompt_en', 'bn': 'prompt_bn', 'bn_cs': 'prompt_bn_cs'}
PHENOMENA = ['full_credit', 'omission', 'partial_reasoning', 'incorrect_number',
             'contradiction', 'conditional_safeguard', 'format_failure']
REASONS = {1.0: {'met'}, 0.5: {'partial'}, 0.0: {'omitted', 'incorrect', 'insufficient', 'non_answer'}}
PLAN_FIELDS = ['fixture_id', 'task_id', 'language', 'phenomenon', 'target_items']
FIXTURE_FIELDS = ['fixture_id', 'author_id', 'authored_date', 'response_text']
KEY_FIELDS = ['fixture_id', 'item_id', 'intended_score', 'intended_reason', 'author_id', 'note']
SHEET_FIELDS = ['rater_id', 'rating_date', 'order', 'fixture_id', 'task_id', 'language', 'item_id',
                'scoring_mode', 'score', 'reason', 'evidence', 'notes']
PREREG_KEYS = {'set_by', 'set_date', 'primary_coefficient', 'decision_statistic', 'minimum',
               'unresolved_disagreement_policy', 'notes'}
COEFFICIENTS = {'krippendorff_alpha_ordinal', 'krippendorff_alpha_nominal', 'cohen_kappa'}
AI_AUTHOR = re.compile(r'\b(ai|claude|gpt|llm|model|agent|codex)\b', re.I)


def fail(context, message):
    raise ValueError(f'{context}: {message}')


def read_csv(path, fields):
    with open(path, encoding='utf-8', newline='') as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != fields:
            fail(path.name, f'expected columns {fields}, found {reader.fieldnames}')
        return list(reader)


def iso_date(value, context):
    try:
        return dt.date.fromisoformat(value)
    except (TypeError, ValueError):
        fail(context, f'date must be YYYY-MM-DD, got {value!r}')


def gold():
    """Frozen pilot records by task, with each scorable item (RIUs and task checks)."""
    validate_freeze()
    validate_gold_freeze()
    records = {r['task_id']: r for f in FILES for r in read_jsonl(ANN / f)}
    for rec in records.values():
        if rec['status'] != 'frozen':
            fail(rec['task_id'], 'calibration requires frozen gold')
    return records


def items(rec):
    out = [{'id': u['id'], 'kind': 'riu', 'mode': u['scoring_mode'], 'criticality': u['criticality'],
            'text': u['description'], 'rule': u['scoring_rule']} for u in rec['rius']]
    out += [{'id': c['id'], 'kind': 'check', 'mode': 'check', 'criticality': 'check',
             'text': f"[{c['kind']}] {c['rule']}", 'rule': None} for c in rec['task_checks']]
    return out


def load_plan(records, cal=CAL):
    plan = read_csv(cal / 'fixture_plan.csv', PLAN_FIELDS)
    seen = set()
    for row in plan:
        ctx = f"plan/{row['fixture_id']}"
        if not re.fullmatch(r'F\d{2}', row['fixture_id']) or row['fixture_id'] in seen:
            fail(ctx, 'fixture IDs must be unique F01, F02, ...')
        seen.add(row['fixture_id'])
        if row['task_id'] not in records: fail(ctx, 'task is not in the frozen pilot')
        if row['language'] not in LANGS: fail(ctx, f'language must be one of {sorted(LANGS)}')
        if row['phenomenon'] not in PHENOMENA: fail(ctx, f'phenomenon must be one of {PHENOMENA}')
        valid = {i['id']: i for i in items(records[row['task_id']])}
        if row['target_items'] != '*':
            for target in row['target_items'].split(';'):
                if target not in valid: fail(ctx, f'unknown target item {target}')
                if row['phenomenon'] == 'partial_reasoning' and valid[target]['mode'] != 'ordinal':
                    fail(ctx, f'{target} has no half-credit anchor')
    return {row['fixture_id']: row for row in plan}


def load_fixtures(plan, cal=CAL):
    fixtures = {}
    for row in read_csv(cal / 'fixtures.csv', FIXTURE_FIELDS):
        ctx = f"fixtures/{row['fixture_id']}"
        if row['fixture_id'] not in plan: fail(ctx, 'not in fixture_plan.csv')
        if row['fixture_id'] in fixtures: fail(ctx, 'duplicate fixture')
        if not row['author_id'].strip(): fail(ctx, 'author_id is required')
        if AI_AUTHOR.search(row['author_id']): fail(ctx, 'fixtures must be human-authored')
        iso_date(row['authored_date'], ctx)
        if not row['response_text'].strip(): fail(ctx, 'response_text is empty')
        fixtures[row['fixture_id']] = row
    return fixtures


def load_key(plan, records, cal=CAL):
    key = {}
    for row in read_csv(cal / 'answer_key.csv', KEY_FIELDS):
        ctx = f"key/{row['fixture_id']}/{row['item_id']}"
        if row['fixture_id'] not in plan: fail(ctx, 'unknown fixture')
        item = {i['id']: i for i in items(records[plan[row['fixture_id']]['task_id']])}.get(row['item_id'])
        if item is None: fail(ctx, 'unknown item')
        score = parse_score(row['intended_score'], item['mode'], ctx)
        if item['kind'] == 'riu' and row['intended_reason'] not in REASONS[score]:
            fail(ctx, f'reason must be one of {sorted(REASONS[score])} for score {score:g}')
        if (row['fixture_id'], row['item_id']) in key: fail(ctx, 'duplicate key row')
        key[(row['fixture_id'], row['item_id'])] = score
    return key


def load_prereg(cal=CAL):
    prereg = json.loads((cal / 'AGREEMENT_PREREG.json').read_text(encoding='utf-8'))
    if set(prereg) != PREREG_KEYS: fail('prereg', f'fields must be {sorted(PREREG_KEYS)}')
    if prereg['primary_coefficient'] not in COEFFICIENTS: fail('prereg', f'coefficient must be one of {sorted(COEFFICIENTS)}')
    if prereg['minimum'] is not None:
        if not prereg['set_by'] or not prereg['set_date']: fail('prereg', 'a threshold needs set_by and set_date')
        iso_date(prereg['set_date'], 'prereg')
        if not isinstance(prereg['minimum'], (int, float)) or not -1 <= prereg['minimum'] <= 1:
            fail('prereg', 'minimum must be a number in [-1, 1]')
        if prereg['decision_statistic'] not in {'point_estimate', 'ci_lower_95'}:
            fail('prereg', 'decision_statistic must be point_estimate or ci_lower_95')
    return prereg


def parse_score(value, mode, ctx):
    allowed = {'ordinal': {0.0, 0.5, 1.0}}.get(mode, {0.0, 1.0})
    try:
        score = float(value)
    except (TypeError, ValueError):
        fail(ctx, f'score missing or not a number: {value!r}')
    if score not in allowed: fail(ctx, f'{mode} item allows {sorted(allowed)}, got {value}')
    return score


# ---------------------------------------------------------------- agreement statistics

def krippendorff_alpha(pairs, metric='nominal'):
    """Alpha for two coders with no missing values; None when expected disagreement is zero."""
    if not pairs: return None
    cats = sorted({v for pair in pairs for v in pair})
    coincidence = Counter()
    for a, b in pairs:
        coincidence[a, b] += 1; coincidence[b, a] += 1
    totals = {c: sum(coincidence[c, k] for k in cats) for c in cats}
    n = sum(totals.values())

    def distance(c, k):
        if metric == 'nominal': return 0.0 if c == k else 1.0
        lo, hi = sorted((cats.index(c), cats.index(k)))
        return (sum(totals[cats[g]] for g in range(lo, hi + 1)) - (totals[c] + totals[k]) / 2) ** 2

    observed = sum(coincidence[c, k] * distance(c, k) for c in cats for k in cats) / n
    expected = sum(totals[c] * totals[k] * distance(c, k) for c in cats for k in cats) / (n * (n - 1))
    return None if expected == 0 else 1 - observed / expected


def cohen_kappa(pairs):
    if not pairs: return None
    n = len(pairs)
    observed = sum(a == b for a, b in pairs) / n
    left, right = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    expected = sum(left[c] * right[c] for c in left) / n ** 2
    return None if expected == 1 else (observed - expected) / (1 - expected)


def exact(pairs):
    return sum(a == b for a, b in pairs) / len(pairs) if pairs else None


STATS = {'krippendorff_alpha_ordinal': lambda p: krippendorff_alpha(p, 'ordinal'),
         'krippendorff_alpha_nominal': lambda p: krippendorff_alpha(p, 'nominal'),
         'cohen_kappa': cohen_kappa}


def bootstrap_ci(rows, stat, reps=2000, seed=20261019):
    """Percentile 95% CI resampling whole fixtures, since items within a fixture are not independent."""
    by_fixture = defaultdict(list)
    for row in rows: by_fixture[row['fixture_id']].append((row['a'], row['b']))
    ids = sorted(by_fixture)
    if len(ids) < 2: return None
    rng, values = random.Random(seed), []
    for _ in range(reps):
        value = stat([p for f in (rng.choice(ids) for _ in ids) for p in by_fixture[f]])
        if value is not None: values.append(value)
    if len(values) < reps * 0.9: return None
    values.sort()
    return values[int(0.025 * len(values))], values[int(0.975 * len(values)) - 1]


def fmt(value):
    return 'NA' if value is None else f'{value:.3f}'


# ---------------------------------------------------------------- subcommands

def check(cal=CAL):
    records = gold()
    plan = load_plan(records, cal)
    fixtures = load_fixtures(plan, cal)
    key = load_key(plan, records, cal)
    prereg = load_prereg(cal)
    by_lang = defaultdict(set)
    for row in plan.values(): by_lang[row['language']].add(row['phenomenon'])
    gaps = {lang: sorted(set(PHENOMENA) - by_lang[lang]) for lang in LANGS if set(PHENOMENA) - by_lang[lang]}
    if gaps: fail('plan', f'every language needs every phenomenon; missing {gaps}')
    print(f'Calibration plan PASSED: {len(plan)} fixtures; '
          f'{dict(Counter(r["language"] for r in plan.values()))}; all {len(PHENOMENA)} phenomena in every language')
    print(f'Fixtures authored: {len(fixtures)}/{len(plan)}; answer-key rows: {len(key)}')
    print('Agreement threshold:', f"{prereg['minimum']} ({prereg['primary_coefficient']}, {prereg['decision_statistic']}; "
          f"set by {prereg['set_by']} on {prereg['set_date']})" if prereg['minimum'] is not None
          else 'NOT SET - the study lead must record it before any rating starts')
    return plan, fixtures, records


def sheets(raters, cal=CAL):
    plan, fixtures, records = check(cal)
    if len(fixtures) != len(plan): fail('sheets', f'{len(plan) - len(fixtures)} fixtures are not authored yet')
    if len(set(raters)) < 2: fail('sheets', 'at least two distinct raters are required')
    prompts = {r['task_id']: r for r in load_rows()}
    out = cal / 'sheets'; out.mkdir(exist_ok=True)
    for rater in raters:
        authored = sorted(f for f, row in fixtures.items() if row['author_id'] == rater)
        if authored: print(f'WARNING: {rater} authored {authored}; an author is not blind to the intended scores')
        order = sorted(plan)
        random.Random(f'{rater}-calibration').shuffle(order)
        md = [f'# Calibration scoring packet for {rater}', '',
              'Score every item for every response, using only the anchors shown and `ANNOTATION_PROTOCOL.md`. '
              'Work alone; do not discuss responses with the other rater until both sheets are returned. '
              'Record scores in the matching CSV: `score` is 0/1 for binary items, 0/0.5/1 for ordinal items, '
              'and 1 (pass) or 0 (fail/flagged) for task checks. `reason` for units is one of '
              'met, partial, omitted, incorrect, insufficient, non_answer. Quote the deciding span in `evidence`.', '']
        rows = []
        for number, fid in enumerate(order, 1):
            row, rec = plan[fid], records[plan[fid]['task_id']]
            md += ['---', '', f'## {number}. Response {fid} ({row["task_id"]}, {row["language"]})', '',
                   '**Prompt**', ''] + [f'> {line}' for line in prompts[row['task_id']][LANGS[row['language']]].split('\n')]
            md += ['', '**Response**', ''] + [f'> {line}' for line in fixtures[fid]['response_text'].split('\n')]
            md += ['', '**Items**', '']
            for item in items(rec):
                if item['kind'] == 'check':
                    md.append(f"- **{item['id']}** (check): {item['text']}")
                else:
                    md.append(f"- **{item['id']}** ({item['mode']}): 1 = {item['rule']['1']}")
                    if item['rule']['0.5']: md.append(f"  - 0.5 = {item['rule']['0.5']}")
                    md.append(f"  - 0 = {item['rule']['0']}")
                rows.append({'rater_id': rater, 'rating_date': '', 'order': number, 'fixture_id': fid,
                             'task_id': row['task_id'], 'language': row['language'], 'item_id': item['id'],
                             'scoring_mode': item['mode'], 'score': '', 'reason': '', 'evidence': '', 'notes': ''})
            md.append('')
        (out / f'{rater}_packet.md').write_text('\n'.join(md), encoding='utf-8')
        with open(out / f'{rater}_sheet.csv', 'w', encoding='utf-8', newline='') as handle:
            writer = csv.DictWriter(handle, SHEET_FIELDS); writer.writeheader(); writer.writerows(rows)
        print(f'Wrote sheets/{rater}_packet.md and sheets/{rater}_sheet.csv ({len(rows)} items)')


def read_sheet(path, plan, records):
    rows = read_csv(Path(path), SHEET_FIELDS)
    raters = {r['rater_id'] for r in rows}
    if len(raters) != 1 or not rows[0]['rater_id'].strip(): fail(path, 'a sheet must belong to exactly one rater')
    expected = {(f, i['id']): i for f, p in plan.items() for i in items(records[p['task_id']])}
    scored = {}
    for row in rows:
        ctx = f"{rows[0]['rater_id']}/{row['fixture_id']}/{row['item_id']}"
        item = expected.get((row['fixture_id'], row['item_id']))
        if item is None: fail(ctx, 'unknown fixture/item')
        if (row['fixture_id'], row['item_id']) in scored: fail(ctx, 'duplicate row')
        iso_date(row['rating_date'], ctx)
        score = parse_score(row['score'], item['mode'], ctx)
        if item['kind'] == 'riu' and row['reason'] not in REASONS[score]:
            fail(ctx, f'reason must be one of {sorted(REASONS[score])} for score {score:g}')
        scored[row['fixture_id'], row['item_id']] = {**row, 'score': score}
    missing = sorted(set(expected) - set(scored))
    if missing: fail(path, f'{len(missing)} items unscored, e.g. {missing[:3]}')
    return rows[0]['rater_id'], scored


def agreement(path_a, path_b, out=None, cal=CAL):
    records = gold()
    plan = load_plan(records, cal)
    fixtures = load_fixtures(plan, cal)
    prereg = load_prereg(cal)
    key = load_key(plan, records, cal)
    (ra, a), (rb, b) = read_sheet(path_a, plan, records), read_sheet(path_b, plan, records)
    if ra == rb: fail('agreement', 'the two sheets come from the same rater')
    meta = {(f, i['id']): (i, records[p['task_id']]['domain'], p['language'])
            for f, p in plan.items() for i in items(records[p['task_id']])}
    rows = [{'fixture_id': f, 'item': iid, 'a': a[f, iid]['score'], 'b': b[f, iid]['score'],
             'ra': a[f, iid]['reason'], 'rb': b[f, iid]['reason'], 'info': meta[f, iid]} for f, iid in sorted(meta)]
    units = [r for r in rows if r['info'][0]['kind'] == 'riu']
    checks = [r for r in rows if r['info'][0]['kind'] == 'check']
    pairs = lambda rs: [(r['a'], r['b']) for r in rs]
    strict = lambda rs: [{**r, 'a': r['a'] == 1, 'b': r['b'] == 1} for r in rs]

    lines = [f'# Calibration agreement: {ra} vs {rb}', '',
             f'Generated {dt.date.today().isoformat()} by `scripts/calibration.py agreement`. '
             f'{len(fixtures)} fixtures; {len(units)} paired unit scores; {len(checks)} paired task checks. '
             'CIs are 95% percentile bootstrap intervals over fixtures. NA means the coefficient is undefined '
             '(for example, constant labels); it is not perfect agreement.', '',
             '## Unit scores', '',
             '| Slice | n | Exact | Cohen κ | α ordinal (95% CI) | Strict (score = 1) κ |', '|---|---:|---:|---:|---:|---:|']
    slices = [('All units', units)]
    for label, idx in [('language', 2), ('domain', 1)]:
        for value in sorted({r['info'][idx] for r in units}):
            slices.append((f'{label}: {value}', [r for r in units if r['info'][idx] == value]))
    for label, field in [('mode', 'mode'), ('criticality', 'criticality')]:
        for value in sorted({r['info'][0][field] for r in units}):
            slices.append((f'{label}: {value}', [r for r in units if r['info'][0][field] == value]))
    for label, rs in slices:
        ci = bootstrap_ci(rs, STATS['krippendorff_alpha_ordinal'])
        alpha = fmt(krippendorff_alpha(pairs(rs), 'ordinal'))
        lines.append(f"| {label} | {len(rs)} | {fmt(exact(pairs(rs)))} | {fmt(cohen_kappa(pairs(rs)))} | "
                     f"{alpha} ({'NA' if ci is None else f'{ci[0]:.3f} to {ci[1]:.3f}'}) | {fmt(cohen_kappa(pairs(strict(rs))))} |")

    for mode in ['binary', 'ordinal']:
        rs = [r for r in units if r['info'][0]['mode'] == mode]
        cats = [0.0, 1.0] if mode == 'binary' else [0.0, 0.5, 1.0]
        lines += ['', f'### Confusion matrix, {mode} units (rows {ra}, columns {rb})', '',
                  '| | ' + ' | '.join(f'{c:g}' for c in cats) + ' |', '|---' * (len(cats) + 1) + '|']
        counts = Counter(pairs(rs))
        lines += [f'| **{x:g}** | ' + ' | '.join(str(counts[x, y]) for y in cats) + ' |' for x in cats]

    reason_pairs = [(r['ra'], r['rb']) for r in units]
    check_pairs = pairs(checks)
    lines += ['', '## Reasons and task checks', '',
              f'- Reason codes (nominal): exact {fmt(exact(reason_pairs))}, Cohen κ {fmt(cohen_kappa(reason_pairs))}',
              f'- Task checks (pass/fail): n {len(checks)}, exact {fmt(exact(check_pairs))}, Cohen κ {fmt(cohen_kappa(check_pairs))}']

    key_rows = [r for r in units if (r['fixture_id'], r['item']) in key]
    if key_rows:
        lines += ['', "## Raters against the authors' intended scores", '',
                  "The key tests whether anchors produce the score the fixture was written to elicit.", '']
        for rater, side in [(ra, 'a'), (rb, 'b')]:
            lines.append(f"- {rater}: exact {fmt(exact([(r[side], key[r['fixture_id'], r['item']]) for r in key_rows]))} "
                         f"over {len(key_rows)} keyed units")
        both = [r for r in key_rows if r['a'] == r['b'] != key[r['fixture_id'], r['item']]]
        lines += [f"- Both raters agree with each other but not the key: {len(both)}"
                  + (' — ' + ', '.join(f"{r['fixture_id']}/{r['item']}" for r in both) if both else '')]

    disputes = [r for r in rows if r['a'] != r['b']]
    blocking = [r for r in disputes if r['info'][0]['criticality'] == 'critical']
    lines += ['', '## Disagreements', '',
              f'{len(disputes)} items differ; **{len(blocking)} on critical units block the production freeze until adjudicated.**', '',
              f'| Fixture | Item | Language | Criticality | {ra} | {rb} |', '|---|---|---|---|---:|---:|']
    lines += [f"| {r['fixture_id']} | {r['item']} | {r['info'][2]} | {r['info'][0]['criticality']} | {r['a']:g} | {r['b']:g} |"
              for r in disputes]

    first_rating = min(iso_date(s['rating_date'], 'sheet') for s in [*a.values(), *b.values()])
    lines += ['', '## Preregistered threshold', '']
    if prereg['minimum'] is None:
        lines.append('**NOT EVALUATED:** no threshold was recorded in `AGREEMENT_PREREG.json`.')
    elif iso_date(prereg['set_date'], 'prereg') > first_rating:
        lines.append(f"**NOT EVALUATED:** the threshold was set {prereg['set_date']}, after rating began "
                     f"{first_rating}. The protocol requires it to be set before calibration.")
    else:
        stat = STATS[prereg['primary_coefficient']]
        value = stat(pairs(units))
        if prereg['decision_statistic'] == 'ci_lower_95':
            ci = bootstrap_ci(units, stat); value = None if ci is None else ci[0]
        verdict = 'UNDEFINED' if value is None else ('MEETS' if value >= prereg['minimum'] else 'BELOW')
        lines.append(f"**{verdict}:** {prereg['primary_coefficient']} ({prereg['decision_statistic']}) = {fmt(value)} "
                     f"against minimum {prereg['minimum']} (set by {prereg['set_by']}, {prereg['set_date']}).")
        lines.append(f"Separately, {len(blocking)} critical-unit disagreements must be adjudicated. {prereg['unresolved_disagreement_policy']}")
    report = '\n'.join(lines) + '\n'
    if out: Path(out).write_text(report, encoding='utf-8')
    print(report)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('check')
    sheet = sub.add_parser('sheets'); sheet.add_argument('--rater', action='append', required=True)
    agree = sub.add_parser('agreement'); agree.add_argument('sheet_a'); agree.add_argument('sheet_b'); agree.add_argument('--out')
    args = parser.parse_args()
    if args.command == 'check': check()
    elif args.command == 'sheets': sheets(args.rater)
    else: agreement(args.sheet_a, args.sheet_b, args.out)


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as exc:
        raise SystemExit(f'Calibration FAILED: {exc}')
