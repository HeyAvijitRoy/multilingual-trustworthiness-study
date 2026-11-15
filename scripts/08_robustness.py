#!/usr/bin/env python3
"""Step 08: robustness checks on the main result; writes results/robustness/.

1. Judge-vs-QA agreement by language and by model, with the signed QA-minus-judge difference.
2. Response length by model and language, and the Bengali effect on critical coverage with
   task fixed effects, with and without log word count as a covariate.
3. Reasons for critical RIUs below full credit, all models and languages.
4. Paired BN-EN and BN-CS-EN difference in CHECK-01 (unsupported-content) pass rate.
5. Sensitivity of the headline contrasts to CHECK-01 (success outcomes without the check) and
   to dropping each domain in turn, using the prespecified domain-equal paired estimator
   (10,000 bootstrap replicates, seed 20261023).

The other 95% CIs (checks 1, 2 and 4) are task-clustered bootstrap percentiles
(2,000 replicates, seed 20261023).

    python3 scripts/08_robustness.py

Writes results/robustness/results.json, summary.md and the manuscript figures
(fig_omission_effects.png, fig_critical_coverage.png, fig_reasons.png).
"""
import importlib.util
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import LANGS, RESULTS, load_annotations, load_study, read_json, read_jsonl, write_json, utc_now  # noqa: E402

spec = importlib.util.spec_from_file_location('qa07', Path(__file__).with_name('07_qa.py'))
qa07 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qa07)

spec6 = importlib.util.spec_from_file_location('analyze06', Path(__file__).with_name('06_analyze.py'))
an06 = importlib.util.module_from_spec(spec6)
spec6.loader.exec_module(an06)

OUT = RESULTS / 'robustness'
REPLICATES, SEED = 2000, 20261023
PRIMARY = ('sol', 'qwen', 'gemma')


def ci(draws):
    v = sorted(draws)
    return [v[int(.025 * len(v))], v[int(.975 * len(v)) - 1]]


# ---- 1. QA agreement by language / model -------------------------------------------------
def qa_by_group(rows):
    out = {}
    for label, sel in (('all 60', lambda r: True), ('stratified 45', lambda r: r['stratum'] == 'main')):
        part = [r for r in rows if sel(r)]
        for key in ('language', 'model'):
            for g in sorted({r[key] for r in part}):
                sub = [r for r in part if r[key] == g]
                a = qa07.agreement(sub)
                rius = [r for r in sub if r['kind'] == 'riu']
                a['responses'] = len({r['qa_id'] for r in sub})
                a['mean_qa_minus_judge'] = sum(r['qa'] - r['judge'] for r in rius) / len(rius)
                out[f'{label}|{key}={g}'] = a
    return out


def qa_gap(rows):
    """BN - EN critical coverage on the sampled responses, QA versus judge (stratified 45 and all 60)."""
    out = {}
    for label, sel in (('all 60', lambda r: True), ('stratified 45', lambda r: r['stratum'] == 'main')):
        part = [r for r in rows if sel(r)]
        out[label] = qa07.critical_coverage_by_language(part)
    return out


# ---- shared study data ---------------------------------------------------------------------
def load_study_rows():
    ann = load_annotations('gold')
    recs = {}
    for key in PRIMARY:
        resp = {(r['task_id'], r['language']): r for r in read_jsonl(RESULTS / f'responses/{key}.jsonl')}
        for s in read_jsonl(RESULTS / f'scores/{key}.jsonl'):
            by = {r['item_id']: r for r in s['ratings']}
            rius = ann[s['task_id']]['rius']
            crit = [by[x['id']] for x in rius if x['criticality'] == 'critical']
            checks = {c['id']: float(by[c['id']]['score']) for c in ann[s['task_id']].get('task_checks', [])}
            r = resp[s['task_id'], s['language']]
            recs[key, s['task_id'], s['language']] = {
                'domain': ann[s['task_id']]['domain'],
                'words': len(r['response_text'].split()), 'chars': len(r['response_text']),
                'out_tokens': r['usage']['output_tokens'],
                'crit_cov': (sum(float(c['score']) for c in crit) / len(crit)) if crit else None,
                'check01': checks.get('CHECK-01'),
                'reasons': [(float(c['score']), c['reason']) for c in crit]}
    return recs


# ---- 2. length -------------------------------------------------------------------------------
def length_table(recs):
    out = {}
    for m in PRIMARY:
        for lang in LANGS:
            v = [r for (mm, t, l), r in recs.items() if mm == m and l == lang]
            out[f'{m}:{lang}'] = {k: float(np.median([r[k] for r in v])) for k in ('words', 'chars', 'out_tokens')}
    return out


def fe_effect(tasks, recs, model, covariate):
    """Task-fixed-effects estimate of BN vs EN on critical coverage, optionally controlling for log words."""
    y, x, g = [], [], []
    for t in tasks:
        pair = [recs.get((model, t, l)) for l in ('en', 'bn')]
        if any(p is None or p['crit_cov'] is None for p in pair):
            continue
        for lang, p in zip((0, 1), pair):
            y.append(p['crit_cov']); x.append([lang, np.log(max(p['words'], 1))]); g.append(t)
    y, x, g = np.array(y), np.array(x, float), np.array(g)
    for t in set(g):
        m = g == t
        y[m] -= y[m].mean(); x[m] -= x[m].mean(axis=0)
    cols = [0, 1] if covariate else [0]
    beta = np.linalg.lstsq(x[:, cols], y, rcond=None)[0]
    return float(beta[0])


def length_effects(recs, tasks):
    rng, out = random.Random(SEED), {}
    for m in ('qwen', 'gemma', 'sol'):
        for cov in (False, True):
            est = fe_effect(tasks, recs, m, cov)
            draws = [fe_effect([rng.choice(tasks) for _ in tasks], recs, m, cov) for _ in range(REPLICATES)]
            out[f'{m}|{"with_length" if cov else "no_length"}'] = {'bn_minus_en': est, 'ci95': ci(draws)}
    return out


# ---- 3. reasons -----------------------------------------------------------------------------
def reason_table(recs):
    out = {}
    for m in PRIMARY:
        for lang in LANGS:
            c, n = Counter(), 0
            for (mm, t, l), r in recs.items():
                if mm == m and l == lang:
                    for s, why in r['reasons']:
                        n += 1
                        if s < 1:
                            c['partial' if s == .5 else why] += 1
            out[f'{m}:{lang}'] = {'critical_judgments': n, 'below_full': sum(c.values()),
                                  **{k: c.get(k, 0) for k in ('partial', 'insufficient', 'incorrect', 'omitted', 'non_answer')}}
    return out


# ---- 4. CHECK-01 ----------------------------------------------------------------------------
def check01_effects(recs, tasks):
    def eff(ts, m, a, b):
        d = [recs[m, t, a]['check01'] - recs[m, t, b]['check01'] for t in ts
             if recs[m, t, a]['check01'] is not None and recs[m, t, b]['check01'] is not None]
        return sum(d) / len(d)
    rng, out = random.Random(SEED), {}
    for m in PRIMARY:
        for a, b in (('bn', 'en'), ('bn_cs', 'en')):
            est = eff(tasks, m, a, b)
            draws = [eff([rng.choice(tasks) for _ in tasks], m, a, b) for _ in range(REPLICATES)]
            out[f'{m}|{a}-{b}'] = {'estimate': est, 'ci95': ci(draws)}
    return out


# ---- 5. sensitivity --------------------------------------------------------------------------
def sensitivity_rows():
    """Study rows with two extra metrics that ignore the task checks."""
    ann = load_annotations('gold')
    rows, _ = an06.load_rows()
    for m in PRIMARY:
        for s in read_jsonl(RESULTS / f'scores/{m}.jsonl'):
            by = {r['item_id']: float(r['score']) for r in s['ratings']}
            rius = ann[s['task_id']]['rius']
            crit = [by[x['id']] for x in rius if x['criticality'] == 'critical']
            row = rows[m, s['task_id'], s['language']]
            row['strict_no_checks'] = float(all(by[x['id']] == 1 for x in rius))
            row['core_no_checks'] = float(all(v == 1 for v in crit)) if crit else None
    return rows


def sensitivity(replicates=10_000):
    rows, tasks = sensitivity_rows(), load_study()['tasks']
    full = an06.Stratum(tasks, replicates)
    out = {'check01': {}, 'drop_domain': {}}
    for metric in ('strict_complete_task_success', 'strict_no_checks', 'core_task_success', 'core_no_checks'):
        for a, b in (('bn', 'en'), ('bn_cs', 'en')):
            out['check01'][f'{metric}:{a}-{b}'] = full.effect(rows, list(PRIMARY), metric, a, b)
    for d in sorted({t['domain'] for t in tasks}):
        sub = an06.Stratum([t for t in tasks if t['domain'] != d], replicates)
        out['drop_domain'][d] = {k: sub.effect(rows, list(PRIMARY), k, 'bn', 'en')
                                 for k in ('critical_omission_rate', 'critical_coverage', 'strict_complete_task_success')}
    return out


# ---- 6. token premium ------------------------------------------------------------------------
def token_premium():
    """Per-task ratio of recorded token counts, BN or BN-CS over EN, summarised by the median across tasks.
    Output tokens exclude reasoning tokens, so all models are compared on visible output.
    Input tokens include a fixed system instruction and chat-template overhead, which understates the prompt premium."""
    use = {}
    for m in PRIMARY:
        for r in read_jsonl(RESULTS / f'responses/{m}.jsonl'):
            visible = r['usage']['output_tokens'] - (r['usage'].get('output_tokens_details') or {}).get('reasoning_tokens', 0)
            use[m, r['task_id'], r['language']] = (r['usage']['input_tokens'], visible, len(r['response_text'].split()))
    tasks = sorted({k[1] for k in use})
    out = {}
    for m in PRIMARY:
        for lang in ('bn', 'bn_cs'):
            for name, idx in (('input', 0), ('output', 1)):
                v = [use[m, t, lang][idx] / use[m, t, 'en'][idx] for t in tasks if (m, t, lang) in use and (m, t, 'en') in use]
                out[f'{m}|{lang}|{name}'] = float(np.median(v))
            v = [(use[m, t, lang][1] / use[m, t, lang][2]) / (use[m, t, 'en'][1] / use[m, t, 'en'][2]) for t in tasks]
            out[f'{m}|{lang}|output_per_word'] = float(np.median(v))
    return out


def word_ratio(tasks_all=None):
    """Median BN/EN response word ratio, raw and divided by the same task's BN/EN prompt word ratio."""
    from common import load_prompts
    pr = load_prompts()
    pw = {t: len(p['prompt_bn'].split()) / len(p['prompt_en'].split()) for t, p in pr.items()}
    out = {'prompt_bn_en_median': float(np.median(list(pw.values())))}
    for m in PRIMARY:
        w = {(r['task_id'], r['language']): len(r['response_text'].split()) for r in read_jsonl(RESULTS / f'responses/{m}.jsonl')}
        ts = sorted({k[0] for k in w})
        out[m] = {'raw': float(np.median([w[t, 'bn'] / w[t, 'en'] for t in ts])),
                  'prompt_normalised': float(np.median([w[t, 'bn'] / w[t, 'en'] / pw[t] for t in ts]))}
    return out

# ---- figures --------------------------------------------------------------------------------
NAMES = {'sol': 'Sol', 'qwen': 'Qwen', 'gemma': 'Gemma'}
LANG_LABEL = {'en': 'EN', 'bn': 'BN', 'bn_cs': 'BN-CS'}
COLORS = {'en': '#1f6f8b', 'bn': '#d1495b', 'bn_cs': '#edae49'}


def figures(report, recs, tasks):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 9})
    eff = read_json(RESULTS / 'analysis/results.json')['effects']

    fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.4), sharey=True)
    labels = [NAMES[m] for m in PRIMARY] + ['Panel']
    for ax, (a, b) in zip(axes, (('bn', 'en'), ('bn_cs', 'bn'), ('bn_cs', 'en'))):
        e = eff[f'critical_omission_rate:{a}-{b}']
        est = [e['by_model'][m] for m in PRIMARY] + [e['estimate']]
        cis = [e['by_model_ci95'][m] for m in PRIMARY] + [e['ci95']]
        y = np.arange(len(labels))[::-1]
        ax.errorbar(est, y, xerr=[[v - c[0] for v, c in zip(est, cis)], [c[1] - v for v, c in zip(est, cis)]],
                    fmt='o', color='#2b5c8a', capsize=2.5, ms=4)
        ax.axvline(0, color='#888', lw=0.8)
        ax.set_title(f'{LANG_LABEL[a]} − {LANG_LABEL[b]}', fontsize=9)
        ax.set_yticks(y, labels)
        ax.set_xlabel('Δ critical omission rate')
    fig.tight_layout()
    fig.savefig(OUT / 'fig_omission_effects.png', dpi=300)
    plt.close(fig)

    rng = random.Random(SEED)
    fig, ax = plt.subplots(figsize=(3.4, 2.6))
    for i, lang in enumerate(LANGS):
        for j, m in enumerate(PRIMARY):
            v = np.array([recs[m, t, lang]['crit_cov'] for t in tasks if recs[m, t, lang]['crit_cov'] is not None])
            draws = [float(np.mean(v[[rng.randrange(len(v)) for _ in v]])) for _ in range(REPLICATES)]
            lo, hi = ci(draws)
            x = j + (i - 1) * 0.22
            ax.errorbar(x, v.mean(), yerr=[[v.mean() - lo], [hi - v.mean()]], fmt='o', color=COLORS[lang], capsize=2, ms=4,
                        label=LANG_LABEL[lang] if j == 0 else None)
    ax.set_xticks(range(3), [NAMES[m] for m in PRIMARY])
    ax.set_ylim(0.70, 1.0)
    ax.set_ylabel('Mean critical coverage')
    ax.legend(frameon=False, ncol=3, loc='lower left', fontsize=8, handletextpad=0.2, columnspacing=0.8)
    fig.tight_layout()
    fig.savefig(OUT / 'fig_critical_coverage.png', dpi=300)
    plt.close(fig)

    cats = ('partial', 'insufficient', 'incorrect', 'omitted')
    cols = ('#9ecae1', '#4a90b8', '#d1495b', '#2b2d42')
    fig, ax = plt.subplots(figsize=(3.4, 2.6))
    keys = [(m, l) for m in PRIMARY for l in LANGS]
    x = np.arange(len(keys)) + np.repeat(np.arange(3) * 0.35, 3)
    bottom = np.zeros(len(keys))
    for c, col in zip(cats, cols):
        vals = np.array([report['reasons'][f'{m}:{l}'][c] for m, l in keys], float)
        ax.bar(x, vals, 0.8, bottom=bottom, color=col, label=c.capitalize())
        bottom += vals
    ax.set_xticks(x, [LANG_LABEL[l] for _, l in keys], fontsize=7)
    for j, m in enumerate(PRIMARY):
        ax.text(x[3 * j + 1], -17, NAMES[m], ha='center', va='top', fontsize=8)
    ax.set_ylabel('Critical RIUs below full credit\n(of 348)')
    ax.legend(frameon=False, fontsize=7, loc='upper left')
    ax.set_ylim(0, 85)
    fig.tight_layout()
    fig.subplots_adjust(bottom=0.2)
    fig.savefig(OUT / 'fig_reasons.png', dpi=300)
    plt.close(fig)


def f(v, d=3):
    return f'{v:+.{d}f}' if v is not None else 'n/a'


def main():
    OUT.mkdir(exist_ok=True)
    qa_rows = qa07.load_rows()
    recs = load_study_rows()
    tasks = sorted({t for (_, t, _) in recs})
    report = {'generated_utc': utc_now(), 'replicates': REPLICATES, 'seed': SEED,
              'qa_agreement_by_group': qa_by_group(qa_rows), 'qa_bn_en_gap': qa_gap(qa_rows),
              'length_median': length_table(recs), 'length_effects': length_effects(recs, tasks),
              'reasons': reason_table(recs), 'check01_effects': check01_effects(recs, tasks),
              'sensitivity': sensitivity(), 'token_premium': token_premium(), 'word_ratio': word_ratio()}
    write_json(OUT / 'results.json', report)
    figures(report, recs, tasks)

    L = ['# Robustness checks', '', f'Generated by `scripts/08_robustness.py`. Intervals are task-clustered bootstrap percentiles (seed {SEED}): {REPLICATES:,} replicates, except the task-check and leave-one-domain-out sensitivity tables, which use the 10,000-replicate estimator of the main analysis.', '',
         '## Judge agreement with the QA ratings, by language and model', '',
         'The stratified set has 45 responses (one per model x language x domain); "all 60" adds 15 chosen for low critical scores.', '',
         '| Set | Group | Responses | RIUs | Alpha | RIU exact | Critical exact | Mean QA − judge (RIUs) |', '|---|---|---:|---:|---:|---:|---:|---:|']
    for k, a in report['qa_agreement_by_group'].items():
        s, g = k.split('|')
        al = f"{a['ordinal_alpha']:.3f}" if a['ordinal_alpha'] is not None else 'n/a'
        L.append(f"| {s} | {g} | {a['responses']} | {a['riu_items']} | {al} | {a['riu_exact']:.3f} | {a['critical_exact']:.3f} | {f(a['mean_qa_minus_judge'])} |")
    L += ['', '### BN − EN critical coverage on the sampled responses', '', '| Set | QA | Judge |', '|---|---:|---:|']
    for s, g in report['qa_bn_en_gap'].items():
        L.append(f"| {s} | {f(g['bn_minus_en']['qa'])} | {f(g['bn_minus_en']['judge'])} |")
    L += ['', '## Response length (median)', '', '| Model | Language | Words | Characters | Output tokens |', '|---|---|---:|---:|---:|']
    for k, v in report['length_median'].items():
        m, lang = k.split(':')
        L.append(f"| {m} | {lang} | {v['words']:.0f} | {v['chars']:.0f} | {v['out_tokens']:.0f} |")
    L += ['', '## Bengali effect on critical coverage with and without a length control', '',
          'Task fixed effects; BN minus EN; log word count as the covariate.', '', '| Model | No control [95% CI] | With log-words control [95% CI] |', '|---|---|---|']
    for m in ('sol', 'qwen', 'gemma'):
        a, b = report['length_effects'][f'{m}|no_length'], report['length_effects'][f'{m}|with_length']
        L.append(f"| {m} | {f(a['bn_minus_en'])} [{f(a['ci95'][0])}, {f(a['ci95'][1])}] | {f(b['bn_minus_en'])} [{f(b['ci95'][0])}, {f(b['ci95'][1])}] |")
    L += ['', '## Critical RIUs below full credit, by reason', '', '| Model | Language | Critical judgments | Below full | Partial | Insufficient | Incorrect | Omitted | Non-answer |', '|---|---|---:|---:|---:|---:|---:|---:|---:|']
    for k, v in report['reasons'].items():
        m, lang = k.split(':')
        L.append(f"| {m} | {lang} | {v['critical_judgments']} | {v['below_full']} | {v['partial']} | {v['insufficient']} | {v['incorrect']} | {v['omitted']} | {v['non_answer']} |")
    L += ['', '## CHECK-01 (unsupported content) pass rate, paired difference vs EN', '', '| Model | BN − EN [95% CI] | BN-CS − EN [95% CI] |', '|---|---|---|']
    for m in PRIMARY:
        a, b = report['check01_effects'][f'{m}|bn-en'], report['check01_effects'][f'{m}|bn_cs-en']
        L.append(f"| {m} | {f(a['estimate'])} [{f(a['ci95'][0])}, {f(a['ci95'][1])}] | {f(b['estimate'])} [{f(b['ci95'][0])}, {f(b['ci95'][1])}] |")
    S = report['sensitivity']
    L += ['', '## Success outcomes with and without the task checks (BN − EN and BN-CS − EN, panel [95% CI])', '',
          '| Outcome | BN − EN | BN-CS − EN |', '|---|---|---|']
    names = {'strict_complete_task_success': 'Strict success (all RIUs = 1 and all checks pass)', 'strict_no_checks': 'Strict success, RIUs only',
             'core_task_success': 'Core success (critical RIUs = 1 and all checks pass)', 'core_no_checks': 'Core success, critical RIUs only'}
    for k, n in names.items():
        a, b = S['check01'][f'{k}:bn-en'], S['check01'][f'{k}:bn_cs-en']
        L.append(f"| {n} | {f(a['estimate'])} [{f(a['ci95'][0])}, {f(a['ci95'][1])}] | {f(b['estimate'])} [{f(b['ci95'][0])}, {f(b['ci95'][1])}] |")
    L += ['', '## BN − EN with each domain dropped in turn (panel [95% CI])', '', '| Domain dropped | Critical omission rate | Critical coverage | Strict success |', '|---|---|---|---|']
    for d, v in S['drop_domain'].items():
        cells = [v[k] for k in ('critical_omission_rate', 'critical_coverage', 'strict_complete_task_success')]
        L.append(f'| {d} | ' + ' | '.join(f"{f(c['estimate'])} [{f(c['ci95'][0])}, {f(c['ci95'][1])}]" for c in cells) + ' |')
    L += ['', '## Token premium relative to EN (median of per-task ratios)', '',
          'Input tokens include a fixed system instruction and template overhead, so the prompt premium is understated.', '',
          '| Model | Language | Input tokens | Output tokens | Output tokens per word |', '|---|---|---:|---:|---:|']
    for m in PRIMARY:
        for lang in ('bn', 'bn_cs'):
            g = report['token_premium']
            L.append(f"| {m} | {lang} | ×{g[f'{m}|{lang}|input']:.2f} | ×{g[f'{m}|{lang}|output']:.2f} | ×{g[f'{m}|{lang}|output_per_word']:.2f} |")
    W = report['word_ratio']
    L += ['', f"## Response words, BN / EN (median per-task ratio; Bengali prompts have ×{W['prompt_bn_en_median']:.2f} the words of English prompts)", '',
          '| Model | Raw | Divided by prompt ratio |', '|---|---:|---:|']
    for m in PRIMARY:
        L.append(f"| {m} | ×{W[m]['raw']:.2f} | ×{W[m]['prompt_normalised']:.2f} |")
    (OUT / 'summary.md').write_text('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
