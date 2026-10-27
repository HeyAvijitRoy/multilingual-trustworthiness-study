#!/usr/bin/env python3
"""Step 05: check result integrity and write the study status.

Verifies that every primary study cell has exactly one response and one valid score,
that response and prompt hashes match the corpus, and that scores match the response
they were made from. Writes results/status.json and results/STATUS.md. No network.

    python3 scripts/05_status.py

Exits 1 if any integrity problem is found (the problems are listed in both outputs).
"""
import sys
from collections import Counter

from common import (LANGS, RESULTS, SCORING_PROCEDURE, load_annotations, load_models, load_prompts, read_json, read_jsonl,
                    sha256_text, study_cells, utc_now, validate_ratings, write_json)


def check_model(model, cells, annotations, prompts):
    key, errors = model['key'], []
    responses = read_jsonl(RESULTS / f'responses/{key}.jsonl')
    scores = read_jsonl(RESULTS / f'scores/{key}.jsonl')
    by_cell = Counter((r['task_id'], r['language']) for r in responses)
    errors += [f'{key}: duplicate response {c}' for c, n in by_cell.items() if n > 1]
    if model['role'] == 'primary':
        errors += [f'{key}: missing response {c}' for c in cells if c not in by_cell]
    errors += [f'{key}: response outside the study {c}' for c in by_cell if c not in cells]
    hashes = {}
    for r in responses:
        cell = (r['task_id'], r['language'])
        if r['response_sha256'] != sha256_text(r['response_text']):
            errors.append(f'{key}: response text changed {cell}')
        if cell in cells and r['prompt_sha256'] != sha256_text(prompts[r['task_id']]['prompt_' + r['language']]):
            errors.append(f'{key}: prompt hash differs from corpus {cell}')
        if r['model_id'] != model['model_id'] or r['returned_model'] != model['model_id']:
            errors.append(f'{key}: model identity differs {cell}')
        hashes[cell] = r['response_sha256']
    scored = Counter((s['task_id'], s['language']) for s in scores)
    errors += [f'{key}: duplicate score {c}' for c, n in scored.items() if n > 1]
    errors += [f'{key}: unscored response {c}' for c in hashes if c not in scored]
    for s in scores:
        cell = (s['task_id'], s['language'])
        if hashes.get(cell) != s['response_sha256']:
            errors.append(f'{key}: score does not match a stored response {cell}')
        if s['procedure'] != SCORING_PROCEDURE:
            errors.append(f'{key}: score from procedure {s["procedure"]} {cell}')
        try:
            validate_ratings(annotations[s['task_id']], s['ratings'])
        except ValueError as exc:
            errors.append(f'{key}: invalid ratings {cell}: {exc}')
    summary = {'model_id': model['model_id'], 'role': model['role'], 'responses': len(responses), 'scored': len(scores),
               'by_language': {lang: sum(r['language'] == lang for r in responses) for lang in LANGS},
               'truncated': sum(r['truncated'] for r in responses),
               'generation_errors': len(read_jsonl(RESULTS / f'responses/{key}.errors.jsonl')),
               'scoring_errors_open': len(read_jsonl(RESULTS / f'scores/{key}.errors.jsonl')),
               'generation_cost_usd': round(sum(r['cost_usd'] for r in responses), 2),
               'scoring_cost_usd': round(sum(s['cost_usd'] for s in scores), 2)}
    return summary, errors


def validation_summary():
    out = {}
    for path in sorted((RESULTS / 'validation').glob('*.result.json')):
        r = read_json(path)
        out[path.name.removesuffix('.result.json')] = {k: r[k] for k in ('fixtures', 'ordinal_alpha', 'critical_exact', 'safety_exact', 'passes')}
    cost = sum(r['cost_usd'] for p in (RESULTS / 'validation').glob('*.jsonl') for r in read_jsonl(p))
    return out, round(cost, 2)


def render(status):
    lines = ['# Study status', '', f"Generated {status['generated_at_utc'][:16].replace('T', ' ')} UTC by `scripts/05_status.py`.", '',
             '## Responses and scores', '', '| Model | Role | Responses | EN / BN / BN-CS | Scored | Truncated | Generation USD | Scoring USD |',
             '|---|---|---:|---|---:|---:|---:|---:|']
    for key, m in status['models'].items():
        lang = ' / '.join(str(m['by_language'][x]) for x in LANGS)
        lines.append(f"| {m['model_id']} | {m['role']} | {m['responses']} | {lang} | {m['scored']} | {m['truncated']} | "
                     f"{m['generation_cost_usd']:.2f} | {m['scoring_cost_usd']:.2f} |")
    lines += ['', '## Judge validation', '', '| Set | Fixtures | Ordinal alpha | Critical exact | Safety exact | Meets thresholds |',
              '|---|---:|---:|---:|---:|---|']
    for name, v in status['validation'].items():
        lines.append(f"| {name} | {v['fixtures']} | {v['ordinal_alpha']:.4f} | {v['critical_exact']:.4f} | {v['safety_exact']:.4f} | "
                     f"{'yes' if v['passes'] else 'no'} |")
    lines += ['', f"Recorded API cost: USD {status['total_cost_usd']:.2f} (generation, scoring and validation records in `results/`).", '',
              '## Integrity', '', 'All checks pass.' if not status['problems'] else
              '\n'.join(f'- {p}' for p in status['problems'][:50]), '', '## Notes', '']
    lines += [f'- {n}' for n in status['notes']]
    return '\n'.join(lines) + '\n'


def main():
    models, annotations, prompts = load_models(), load_annotations('gold'), load_prompts()
    cells = {(c['task_id'], c['language']) for c in study_cells()}
    status = {'generated_at_utc': utc_now(), 'models': {}, 'problems': []}
    for key, model in models.items():
        summary, errors = check_model(model, cells, annotations, prompts)
        status['models'][key], status['problems'] = summary, status['problems'] + errors
    status['validation'], validation_cost = validation_summary()
    status['total_cost_usd'] = round(validation_cost + sum(m['generation_cost_usd'] + m['scoring_cost_usd']
                                                           for m in status['models'].values()), 2)
    gemini = status['models'].get('gemini', {})
    status['notes'] = [
        f"Gemini is exploratory: {gemini.get('responses', 0)} of 60 planned responses (20 matched tasks x 3 languages); "
        'collection stopped and Gemini is excluded from the primary analysis.',
        'QA sample study (independent human check of a sample of study scores): '
        + ('done, see results/qa/.' if (RESULTS / 'qa').exists() else 'pending.'),
    ]
    write_json(RESULTS / 'status.json', status)
    (RESULTS / 'STATUS.md').write_text(render(status), encoding='utf-8')
    print(render(status))
    return 1 if status['problems'] else 0


if __name__ == '__main__':
    sys.exit(main())
