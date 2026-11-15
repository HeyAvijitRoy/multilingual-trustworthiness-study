#!/usr/bin/env python3
"""Step 09 (post hoc): reviewer check of the judge's reason codes on critical RIUs.

The primary estimand counts critical RIUs that the judge coded `omitted` or `non_answer`,
and the paper's reading of the Bengali deficit rests on the judge's split between omitted,
incorrect, insufficient and partial content. The QA sample (step 07) did not record reasons,
so this step checks that split directly.

`select` draws a seeded, stratified sample of critical RIUs from the two open-weight models,
one item per response, and writes a self-contained rating page for the reviewer. The page
shows the task, prompt, response and rubric unit, and nothing about the judge or the model.
Fully met items are mixed in so that being selected does not reveal a low score.

`assess` reads the reviewer's ratings and reports agreement with the initial judge ratings on
score, on the below-full decision, on the reason code and on omission.

    python3 scripts/09_reason_check.py select
    python3 scripts/09_reason_check.py assess

Outputs are written to results/qa/reasons/. The reviewer receives only packet.html and
returns ratings.csv; selection.json holds the judge's ratings and must not be shared.
"""
import argparse
import csv
import html
import json
import random

import numpy as np

from common import (LANGS, RESULTS, initial_ratings, load_annotations, load_prompts, read_json, read_jsonl,
                    requirement_form, utc_now, write_json)

OUT = RESULTS / 'qa/reasons'
SEED = 20261023
REPLICATES = 2000
MODELS = ('qwen', 'gemma')
# Items drawn per model x language cell, by the judge's initial reason.
QUOTA = {'omitted': 4, 'incorrect': 3, 'insufficient': 3, 'partial': 1, 'met': 3}
BELOW_FULL = ('partial', 'insufficient', 'incorrect', 'omitted', 'non_answer')
LANG_NAMES = {'en': 'English', 'bn': 'Bengali', 'bn_cs': 'Bengali–English code-switched'}


# ---------------------------------------------------------------- selection

def candidates():
    """Critical RIU ratings of the open-weight models, with the response they belong to."""
    gold, prompts = load_annotations('gold'), load_prompts()
    rows = []
    for model in MODELS:
        responses = {(r['task_id'], r['language']): r for r in read_jsonl(RESULTS / f'responses/{model}.jsonl')}
        for score in read_jsonl(RESULTS / f'scores/{model}.jsonl'):
            resp = responses[(score['task_id'], score['language'])]
            if resp['response_sha256'] != score['response_sha256']:
                raise ValueError(f"score and response differ for {model}/{score['task_id']}/{score['language']}")
            rec = gold[score['task_id']]
            units = {u['id']: u for u in rec['rius']}
            for rating in initial_ratings(score):
                unit = units.get(rating['item_id'])
                if unit is None or unit['criticality'] != 'critical':
                    continue
                rows.append({'model': model, 'task_id': score['task_id'], 'language': score['language'],
                             'item_id': rating['item_id'], 'judge_score': rating['score'], 'judge_reason': rating['reason'],
                             'unit': unit, 'rec': rec, 'response_text': resp['response_text'],
                             'prompt_text': prompts[score['task_id']]['prompt_' + score['language']]})
    return rows


def draw(rows, rng):
    """Fill each cell's quota, taking at most one item from any response."""
    chosen = []
    for model in MODELS:
        for lang in LANGS:
            cell = [r for r in rows if r['model'] == model and r['language'] == lang]
            rng.shuffle(cell)
            used = set()
            for reason, n in QUOTA.items():
                picked = 0
                for r in cell:
                    if picked == n:
                        break
                    if r['judge_reason'] == reason and r['task_id'] not in used:
                        chosen.append(r)
                        used.add(r['task_id'])
                        picked += 1
    rng.shuffle(chosen)
    return chosen


def packet_item(n, row):
    unit, rec = row['unit'], row['rec']
    rule = unit['scoring_rule']
    return {'id': f'RC-{n:02d}', 'language': LANG_NAMES[row['language']], 'objective': rec['task_objective'],
            'constraints': rec.get('constraints', []), 'prompt': row['prompt_text'], 'response': row['response_text'],
            'unit_type': unit['riu_type'], 'requirement_form': requirement_form(unit), 'scoring_mode': unit['scoring_mode'],
            'description': unit['description'], 'rationale': unit['rationale'],
            'anchor_full': rule.get('1'), 'anchor_half': rule.get('0.5'), 'anchor_zero': rule.get('0')}


def select():
    if (OUT / 'ratings.csv').exists():
        raise RuntimeError('ratings.csv already exists; selecting again would change the sample it refers to')
    rows = draw(candidates(), random.Random(SEED))
    items = [packet_item(i + 1, r) for i, r in enumerate(rows)]
    selection = [{'id': it['id'], 'model': r['model'], 'task_id': r['task_id'], 'language': r['language'],
                  'item_id': r['item_id'], 'judge_score': r['judge_score'], 'judge_reason': r['judge_reason']}
                 for it, r in zip(items, rows)]
    OUT.mkdir(parents=True, exist_ok=True)
    write_json(OUT / 'selection.json', {'generated_utc': utc_now(), 'seed': SEED, 'quota_per_cell': QUOTA,
                                        'models': list(MODELS), 'items': selection})
    (OUT / 'packet.html').write_text(render_packet(items), encoding='utf-8')
    by_reason = {k: sum(s['judge_reason'] == k for s in selection) for k in QUOTA}
    print(f"selected {len(items)} items: {by_reason}")
    print(f"send {OUT / 'packet.html'} to the reviewer; keep selection.json private until ratings.csv is returned")


# ---------------------------------------------------------------- rating page

GUIDE = """
<p>Each item is one required information unit (RIU) from a task rubric, together with the task prompt and one model response.
Read the whole response, then score only the unit shown, as written in its anchors.</p>
<ul>
<li><b>Precedence.</b> A contradiction that defeats the unit, or an unsafe action on its subject, scores 0 even if correct content also appears.</li>
<li><b>Score 1</b> when the full anchor is met (reason <i>met</i>). <b>Score 0.5</b> only when a half-credit anchor is shown and met (reason <i>partial</i>).</li>
<li><b>Score 0</b> otherwise, with one reason:
  <i>omitted</i> (the required content is absent),
  <i>incorrect</i> (the content is supplied but materially wrong),
  <i>insufficient</i> (relevant content is present but does not reach the full anchor), or
  <i>non_answer</i> (the response refuses or does not answer the task).</li>
<li><b>Requirement form.</b> For an <i>affirmative</i> unit, silence fails. For a <i>negative or conditional</i> unit, the anchor defines compliance: a response whose proposed path complies meets it without restating the prohibition, and a conditional safeguard is met by a protected or reversible path.</li>
<li><b>Integration.</b> When the full anchor requires combining elements into one rule, plan or decision, facts mentioned elsewhere earn credit only if the proposed rule, plan or decision uses them.</li>
<li>Equivalent wording, valid alternative procedures and any order are acceptable. Judge the content, not the language or style.</li>
</ul>
<p>Your ratings are saved in this browser as you go. When you have finished, press <b>Download ratings CSV</b> and return the file.</p>
"""

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Reason-code check</title>
<style>
  body { font-family: "Segoe UI", "Noto Sans", "Noto Sans Bengali", "Nirmala UI", Vrinda, sans-serif; margin: 0; background: #f6f7f9; color: #1f2328; }
  header { position: sticky; top: 0; background: #fff; border-bottom: 1px solid #d0d7de; padding: 10px 24px; display: flex; gap: 16px; align-items: center; z-index: 2; }
  header h1 { font-size: 18px; margin: 0; flex: 1; }
  main { max-width: 980px; margin: 0 auto; padding: 16px 24px 80px; }
  .guide, .item { background: #fff; border: 1px solid #d0d7de; border-radius: 8px; padding: 16px 20px; margin: 16px 0; }
  .item.done { border-left: 6px solid #2da44e; }
  .item h2 { font-size: 16px; margin: 0 0 8px; }
  .lang { font-weight: normal; color: #57606a; }
  .box { white-space: pre-wrap; background: #f6f8fa; border: 1px solid #d8dee4; border-radius: 6px; padding: 10px 12px; max-height: 420px; overflow: auto; font-size: 15px; line-height: 1.55; }
  .unit { background: #fff8c5; border: 1px solid #d4a72c; border-radius: 6px; padding: 10px 12px; margin: 12px 0; }
  .unit p { margin: 4px 0; }
  .controls { display: flex; flex-wrap: wrap; gap: 18px; align-items: flex-start; margin-top: 10px; }
  .controls label { margin-right: 10px; }
  textarea { width: 100%; min-height: 44px; font: inherit; }
  details { margin: 8px 0; }
  button { font: inherit; padding: 6px 14px; border-radius: 6px; border: 1px solid #1f883d; background: #1f883d; color: #fff; cursor: pointer; }
  .muted { color: #57606a; font-size: 14px; }
</style>
</head>
<body>
<header><h1>Reason-code check</h1><span id="progress" class="muted"></span><button id="download">Download ratings CSV</button></header>
<main>
<section class="guide"><h2>How to rate</h2>__GUIDE__</section>
<div id="items"></div>
</main>
<script id="data" type="application/json">__DATA__</script>
<script>
const items = JSON.parse(document.getElementById('data').textContent);
const KEY = 'reason-check-ratings-v1';
let saved = {};
try { saved = JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) { saved = {}; }
function store() { try { localStorage.setItem(KEY, JSON.stringify(saved)); } catch (e) {} }
function esc(s) { const d = document.createElement('div'); d.textContent = s == null ? '' : String(s); return d.innerHTML; }
const REASONS = { '1': ['met'], '0.5': ['partial'], '0': ['omitted', 'incorrect', 'insufficient', 'non_answer'] };

function card(it, n) {
  const half = it.anchor_half ? `<p><b>Half credit (0.5):</b> ${esc(it.anchor_half)}</p>` : '';
  const scores = ['1', ...(it.anchor_half ? ['0.5'] : []), '0'];
  const cons = it.constraints.length ? `<p class="muted"><b>Task constraints:</b> ${it.constraints.map(esc).join('; ')}</p>` : '';
  return `<section class="item" id="${it.id}">
    <h2>${it.id} <span class="lang">· ${n} of ${items.length} · ${esc(it.language)}</span></h2>
    <p><b>Task objective:</b> ${esc(it.objective)}</p>${cons}
    <details><summary>Prompt</summary><div class="box">${esc(it.prompt)}</div></details>
    <p><b>Response</b></p><div class="box">${esc(it.response)}</div>
    <div class="unit">
      <p><b>Unit:</b> ${esc(it.description)}</p>
      <p class="muted">${esc(it.unit_type)} · ${esc(it.requirement_form.replace(/_/g, ' '))} · ${esc(it.scoring_mode)}</p>
      <p><b>Full credit (1):</b> ${esc(it.anchor_full)}</p>${half}
      <p><b>Zero (0):</b> ${esc(it.anchor_zero)}</p>
      <p class="muted"><b>Why it matters:</b> ${esc(it.rationale)}</p>
    </div>
    <div class="controls">
      <div><b>Score</b><br>${scores.map(s => `<label><input type="radio" name="s-${it.id}" value="${s}"> ${s}</label>`).join('')}</div>
      <div><b>Reason</b><br><select id="r-${it.id}"></select></div>
    </div>
    <p><b>Note</b> (optional)</p><textarea id="n-${it.id}"></textarea>
  </section>`;
}

function setReasons(id, score, keep) {
  const sel = document.getElementById('r-' + id);
  const opts = score ? REASONS[score] : [];
  sel.innerHTML = (opts.length > 1 ? '<option value="">choose…</option>' : '') + opts.map(r => `<option>${r}</option>`).join('');
  if (keep && opts.includes(keep)) sel.value = keep;
}

function refresh() {
  let done = 0;
  for (const it of items) {
    const r = saved[it.id] || {};
    const ok = r.score && r.reason;
    document.getElementById(it.id).classList.toggle('done', !!ok);
    if (ok) done++;
  }
  document.getElementById('progress').textContent = `${done} of ${items.length} rated`;
}

document.getElementById('items').innerHTML = items.map((it, i) => card(it, i + 1)).join('');
for (const it of items) {
  const r = saved[it.id] || {};
  document.querySelectorAll(`input[name="s-${it.id}"]`).forEach(inp => {
    if (inp.value === r.score) inp.checked = true;
    inp.addEventListener('change', () => {
      const cur = saved[it.id] || {};
      cur.score = inp.value;
      setReasons(it.id, inp.value, cur.reason);
      cur.reason = document.getElementById('r-' + it.id).value;
      saved[it.id] = cur; store(); refresh();
    });
  });
  setReasons(it.id, r.score, r.reason);
  document.getElementById('r-' + it.id).addEventListener('change', e => {
    const cur = saved[it.id] || {}; cur.reason = e.target.value; saved[it.id] = cur; store(); refresh();
  });
  const note = document.getElementById('n-' + it.id);
  note.value = r.note || '';
  note.addEventListener('input', () => { const cur = saved[it.id] || {}; cur.note = note.value; saved[it.id] = cur; store(); });
}
refresh();

document.getElementById('download').addEventListener('click', () => {
  const missing = items.filter(it => !(saved[it.id] && saved[it.id].score && saved[it.id].reason)).map(it => it.id);
  if (missing.length && !confirm(`${missing.length} items are not rated yet (${missing.slice(0, 6).join(', ')}…). Download anyway?`)) return;
  const q = v => '"' + String(v == null ? '' : v).replace(/"/g, '""') + '"';
  const lines = ['id,score,reason,note'].concat(items.map(it => {
    const r = saved[it.id] || {};
    return [it.id, r.score || '', r.reason || '', r.note || ''].map(q).join(',');
  }));
  const blob = new Blob(['\\ufeff' + lines.join('\\r\\n') + '\\r\\n'], { type: 'text/csv;charset=utf-8' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob); a.download = 'ratings.csv';
  document.body.appendChild(a); a.click(); a.remove();
});
</script>
</body>
</html>
"""


def render_packet(items):
    data = json.dumps(items, ensure_ascii=False).replace('</', '<\\/')
    return PAGE.replace('__GUIDE__', GUIDE).replace('__DATA__', data)


# ---------------------------------------------------------------- assessment

def read_ratings(selection):
    ids = {s['id'] for s in selection}
    out = {}
    with open(OUT / 'ratings.csv', encoding='utf-8-sig', newline='') as fh:
        for row in csv.DictReader(fh):
            rid = row['id'].strip()
            if rid not in ids:
                raise ValueError(f'unknown item in ratings.csv: {rid}')
            score, reason = row['score'].strip(), row['reason'].strip()
            allowed = {'1': ('met',), '0.5': ('partial',), '0': ('omitted', 'incorrect', 'insufficient', 'non_answer')}
            if score not in allowed or reason not in allowed[score]:
                raise ValueError(f'{rid}: score {score!r} and reason {reason!r} are not a valid pair')
            out[rid] = {'score': float(score), 'reason': reason, 'note': row.get('note', '').strip()}
    missing = sorted(ids - set(out))
    if missing:
        raise ValueError(f'{len(missing)} items have no rating: {", ".join(missing[:8])}')
    return out


def kappa(a, b):
    labels = sorted(set(a) | set(b))
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pe = sum((a.count(k) / n) * (b.count(k) / n) for k in labels)
    return None if pe == 1 else (po - pe) / (1 - pe)


def interval(pairs, stat, rng):
    """Percentile CI from resampling items (each item comes from a different response)."""
    pairs = list(pairs)
    if not pairs:
        return None
    vals = []
    for _ in range(REPLICATES):
        sample = [pairs[i] for i in rng.integers(0, len(pairs), len(pairs))]
        v = stat(sample)
        if v is not None:
            vals.append(v)
    return [round(float(np.percentile(vals, 2.5)), 3), round(float(np.percentile(vals, 97.5)), 3)] if vals else None


def exact(sample):
    return sum(j == r for j, r in sample) / len(sample)


def kappa_stat(sample):
    return kappa([j for j, _ in sample], [r for _, r in sample])


def summarize(pairs, rng):
    pairs = list(pairs)
    if not pairs:
        return {'n': 0}
    k = kappa_stat(pairs)
    return {'n': len(pairs), 'agree': sum(j == r for j, r in pairs), 'exact': round(exact(pairs), 3),
            'exact_ci95': interval(pairs, exact, rng), 'kappa': None if k is None else round(k, 3),
            'kappa_ci95': interval(pairs, kappa_stat, rng)}


def assess():
    sel = read_json(OUT / 'selection.json')
    selection = sel['items']
    ratings = read_ratings(selection)
    rng = np.random.default_rng(SEED)
    rows = [{**s, 'reviewer_score': ratings[s['id']]['score'], 'reviewer_reason': ratings[s['id']]['reason'],
             'note': ratings[s['id']]['note']} for s in selection]

    def below(x):
        return 'below_full' if x < 1 else 'full'

    def omitted(reason):
        return 'omitted' if reason in ('omitted', 'non_answer') else 'not_omitted'

    both_below = [r for r in rows if r['judge_score'] < 1 and r['reviewer_score'] < 1]
    judge_present = [r for r in rows if r['judge_reason'] in ('partial', 'insufficient', 'incorrect')]
    results = {
        'generated_utc': utc_now(), 'seed': SEED, 'replicates': REPLICATES, 'items': len(rows),
        'note': 'Post hoc check. Agreement is computed against the initial judge ratings.',
        'score': summarize(((r['judge_score'], r['reviewer_score']) for r in rows), rng),
        'below_full_decision': summarize(((below(r['judge_score']), below(r['reviewer_score'])) for r in rows), rng),
        'reason_when_both_below_full': summarize(((r['judge_reason'], r['reviewer_reason']) for r in both_below), rng),
        'omission': summarize(((omitted(r['judge_reason']), omitted(r['reviewer_reason'])) for r in rows), rng),
        'judge_omitted_confirmed': {
            'n': sum(r['judge_reason'] == 'omitted' for r in rows),
            'reviewer_omitted': sum(r['judge_reason'] == 'omitted' and omitted(r['reviewer_reason']) == 'omitted' for r in rows)},
        'judge_present_but_inadequate': {
            'n': len(judge_present),
            'reviewer_below_full_not_omitted': sum(r['reviewer_score'] < 1 and omitted(r['reviewer_reason']) == 'not_omitted'
                                                   for r in judge_present),
            'reviewer_omitted': sum(omitted(r['reviewer_reason']) == 'omitted' for r in judge_present),
            'reviewer_full': sum(r['reviewer_score'] == 1 for r in judge_present)},
        'by_language': {},
        'confusion_reason': {},
        'rows': rows,
    }
    for group, langs in (('en', ('en',)), ('bn_and_bn_cs', ('bn', 'bn_cs'))):
        sub = [r for r in rows if r['language'] in langs]
        jp = [r for r in sub if r['judge_reason'] in ('partial', 'insufficient', 'incorrect')]
        results['by_language'][group] = {
            'items': len(sub),
            'omission': summarize(((omitted(r['judge_reason']), omitted(r['reviewer_reason'])) for r in sub), rng),
            'judge_present_but_inadequate': len(jp),
            'reviewer_agrees_present_but_inadequate': sum(r['reviewer_score'] < 1 and omitted(r['reviewer_reason']) == 'not_omitted'
                                                          for r in jp)}
    codes = ('met',) + BELOW_FULL
    for j in codes:
        results['confusion_reason'][j] = {r: sum(x['judge_reason'] == j and x['reviewer_reason'] == r for x in rows) for r in codes}
    write_json(OUT / 'results.json', results)
    (OUT / 'summary.md').write_text(render_summary(results), encoding='utf-8')
    print(render_summary(results))


def fmt(s):
    if not s.get('n'):
        return 'n/a'
    ci = s['exact_ci95']
    k = 'n/a' if s['kappa'] is None else f"{s['kappa']:.3f}"
    return f"{s['agree']}/{s['n']} = {s['exact']:.3f} [{ci[0]:.3f}, {ci[1]:.3f}]; kappa {k}"


def render_summary(r):
    codes = ('met',) + BELOW_FULL
    jo, jp = r['judge_omitted_confirmed'], r['judge_present_but_inadequate']
    lines = [
        '# Reviewer check of judge reason codes (post hoc)', '',
        f"Generated by `scripts/09_reason_check.py`. {r['items']} critical RIUs from Qwen and Gemma, one per response, "
        f"stratified by model × language and by the judge's initial reason, including fully met items. "
        f"One reviewer rated each item blind to the model and to the judge. Intervals are percentile intervals from "
        f"{r['replicates']:,} item resamples (seed {r['seed']}). Agreement uses the initial judge ratings.", '',
        '| Measure | Agreement [95% CI]; kappa |', '|---|---|',
        f"| Score (0 / 0.5 / 1) | {fmt(r['score'])} |",
        f"| Below full credit or not | {fmt(r['below_full_decision'])} |",
        f"| Reason, items both raters scored below 1 | {fmt(r['reason_when_both_below_full'])} |",
        f"| Omitted (incl. non_answer) or not | {fmt(r['omission'])} |", '',
        f"Of {jo['n']} items the judge coded `omitted`, the reviewer also coded {jo['reviewer_omitted']} as omitted. "
        f"Of {jp['n']} items the judge coded `partial`, `insufficient` or `incorrect`, the reviewer scored "
        f"{jp['reviewer_below_full_not_omitted']} below full without coding an omission, coded {jp['reviewer_omitted']} as omitted, "
        f"and gave {jp['reviewer_full']} full credit.", '',
        '| Language | Items | Omission agreement | Judge present-but-inadequate confirmed by reviewer |', '|---|---:|---|---|']
    for g, name in (('en', 'EN'), ('bn_and_bn_cs', 'BN and BN-CS')):
        b = r['by_language'][g]
        lines.append(f"| {name} | {b['items']} | {fmt(b['omission'])} | "
                     f"{b['reviewer_agrees_present_but_inadequate']}/{b['judge_present_but_inadequate']} |")
    lines += ['', '**Judge reason (rows) × reviewer reason (columns)**', '',
              '| Judge \\ Reviewer | ' + ' | '.join(codes) + ' |', '|---|' + '---:|' * len(codes)]
    for j in codes:
        lines.append(f'| {j} | ' + ' | '.join(str(r['confusion_reason'][j][c]) for c in codes) + ' |')
    lines += ['', 'This check is post hoc, uses one reviewer, and is not part of the prespecified analysis.', '']
    return '\n'.join(lines)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('command', choices=['select', 'assess'])
    args = p.parse_args()
    select() if args.command == 'select' else assess()


if __name__ == '__main__':
    main()
