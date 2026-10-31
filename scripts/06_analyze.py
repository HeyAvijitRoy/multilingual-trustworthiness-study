#!/usr/bin/env python3
"""Step 06: compute the pre-registered analysis and write results/analysis/.

Per response: RIU coverage, strict RIU coverage, critical coverage, critical omission
rate (critical RIUs coded omitted or non_answer), critical unmet/zero rates, strict
complete-task and core-task success, plus task-check outcomes.

Language effects are paired within task, averaged within domain, then over the five
domains equally; the panel estimate averages the three primary models equally.
95% CIs come from a task-clustered bootstrap stratified by domain (10,000 replicates,
seed 20261023) that carries all languages and models of each sampled task.
Primary estimand: critical omission rate, BN minus EN. Gemini is reported descriptively only.

    python3 scripts/06_analyze.py [--replicates 10000]

Writes results/analysis/results.json, results/analysis/summary.md and figures.
"""
import argparse
import sys
from collections import defaultdict

import numpy as np

from common import LANGS, RESULTS, load_annotations, load_models, load_study, read_jsonl, utc_now, validate_ratings, write_json, initial_ratings

METRICS = ('critical_omission_rate', 'critical_coverage', 'riu_coverage', 'strict_complete_task_success',
           'strict_riu_coverage', 'critical_unmet_rate', 'critical_zero_rate', 'core_task_success')
CONTRASTS = (('bn', 'en'), ('bn_cs', 'bn'), ('bn_cs', 'en'))
DESCRIPTIVE = METRICS + ('unsupported_content_pass', 'non_answer')
SEED = 20261023


def response_metrics(rec, ratings):
    validate_ratings(rec, ratings)
    by_id = {r['item_id']: r for r in ratings}
    rius = [(riu, by_id[riu['id']]) for riu in rec['rius']]
    checks = [(c, by_id[c['id']]) for c in rec.get('task_checks', [])]
    scores = [float(r['score']) for _, r in rius]
    crit = [(float(r['score']), r['reason']) for riu, r in rius if riu['criticality'] == 'critical']
    checks_pass = all(float(r['score']) == 1 for _, r in checks)
    out = {'riu_coverage': sum(scores) / len(scores),
           'strict_riu_coverage': sum(s == 1 for s in scores) / len(scores),
           'strict_complete_task_success': float(all(s == 1 for s in scores) and checks_pass),
           'unsupported_content_pass': float(all(float(r['score']) == 1 for c, r in checks if c['kind'] == 'unsupported_content')),
           'non_answer': float(all(r['reason'] == 'non_answer' for _, r in rius)),
           'critical_coverage': None, 'critical_omission_rate': None, 'critical_unmet_rate': None,
           'critical_zero_rate': None, 'core_task_success': None}
    if crit:
        out.update({'critical_coverage': sum(s for s, _ in crit) / len(crit),
                    'critical_omission_rate': sum(reason in {'omitted', 'non_answer'} for _, reason in crit) / len(crit),
                    'critical_unmet_rate': sum(s < 1 for s, _ in crit) / len(crit),
                    'critical_zero_rate': sum(s == 0 for s, _ in crit) / len(crit),
                    'core_task_success': float(all(s == 1 for s, _ in crit) and checks_pass)})
    return out


def load_rows(before_review=False):
    """{(model, task_id, language): metrics} for every scored response, plus truncated cells."""
    annotations, rows, truncated = load_annotations('gold'), {}, set()
    for key in load_models():
        trunc = {(r['task_id'], r['language']) for r in read_jsonl(RESULTS / f'responses/{key}.jsonl') if r['truncated']}
        for s in read_jsonl(RESULTS / f'scores/{key}.jsonl'):
            ratings = initial_ratings(s) if before_review else s['ratings']
            rows[key, s['task_id'], s['language']] = response_metrics(annotations[s['task_id']], ratings)
            if (s['task_id'], s['language']) in trunc:
                truncated.add((key, s['task_id'], s['language']))
    return rows, truncated


class Stratum:
    """A set of tasks with fixed bootstrap resamples shared by every metric and contrast."""

    def __init__(self, tasks, replicates):
        self.domains = sorted({t['domain'] for t in tasks})
        self.ids = {d: [t['task_id'] for t in tasks if t['domain'] == d] for d in self.domains}
        rng = np.random.default_rng(SEED)
        self.samples = {d: rng.integers(0, len(self.ids[d]), size=(replicates, len(self.ids[d]))) for d in self.domains}

    def diffs(self, rows, model, metric, a, b, domain):
        out = []
        for t in self.ids[domain]:
            ra, rb = rows.get((model, t, a)), rows.get((model, t, b))
            va, vb = (ra or {}).get(metric), (rb or {}).get(metric)
            out.append(np.nan if va is None or vb is None else va - vb)
        return np.array(out, dtype=float)

    def effect(self, rows, models, metric, a, b):
        by_model, reps, pairs = {}, {}, {}
        for m in models:
            point, boot, n = [], [], 0
            for d in self.domains:
                x = self.diffs(rows, m, metric, a, b, d)
                valid = ~np.isnan(x)
                n += int(valid.sum())
                point.append(x[valid].mean() if valid.any() else np.nan)
                xs, vs = np.where(valid, x, 0.0)[self.samples[d]], valid[self.samples[d]]
                with np.errstate(invalid='ignore', divide='ignore'):
                    boot.append(xs.sum(axis=1) / vs.sum(axis=1))
            by_model[m] = float(np.mean(point)) if not np.isnan(point).any() else None
            reps[m], pairs[m] = np.mean(boot, axis=0), n
        pooled = float(np.mean(list(by_model.values()))) if all(v is not None for v in by_model.values()) else None
        panel = np.mean([reps[m] for m in models], axis=0)

        def ci(r):
            r = r[~np.isnan(r)]
            return [float(np.percentile(r, 2.5)), float(np.percentile(r, 97.5))] if len(r) else [None, None]

        return {'estimate': pooled, 'ci95': ci(panel), 'by_model': by_model,
                'by_model_ci95': {m: ci(reps[m]) for m in models}, 'paired_tasks': pairs}

    def table(self, rows, models):
        return {f'{metric}:{a}-{b}': self.effect(rows, models, metric, a, b) for metric in METRICS for a, b in CONTRASTS}


def descriptive(rows, models, tasks):
    ids = {t['task_id'] for t in tasks}
    out = {}
    for m in models:
        for lang in LANGS:
            cells = [v for (mm, t, l), v in rows.items() if mm == m and l == lang and t in ids]
            out[f'{m}:{lang}'] = {'n': len(cells), **{k: (float(np.mean([c[k] for c in cells if c[k] is not None]))
                                                          if any(c[k] is not None for c in cells) else None) for k in DESCRIPTIVE}}
    return out


def analyze(replicates=10_000):
    study, models = load_study(), load_models()
    primary = [k for k, m in models.items() if m['role'] == 'primary']
    rows, truncated = load_rows()
    tasks = study['tasks']
    extended = set(study['extended_context_tasks'])
    full = Stratum(tasks, replicates)
    no_trunc = {k: v for k, v in rows.items() if k not in truncated}
    report = {
        'generated_at_utc': utc_now(), 'replicates': replicates, 'seed': SEED, 'models': primary,
        'responses_scored': {m: sum(k[0] == m for k in rows) for m in models},
        'truncated_cells': sorted(['/'.join(k) for k in truncated]),
        'descriptive': descriptive(rows, primary, tasks),
        'exploratory_descriptive': descriptive(rows, [k for k in models if k not in primary], tasks),
        'effects': full.table(rows, primary),
        'by_domain': {d: Stratum([t for t in tasks if t['domain'] == d], replicates).table(rows, primary)
                      for d in full.domains},
        'by_difficulty': {x: Stratum([t for t in tasks if t['difficulty'] == x], replicates).table(rows, primary)
                          for x in ('easy', 'medium', 'hard')},
        'extended_context_only': Stratum([t for t in tasks if t['task_id'] in extended], replicates).table(rows, primary),
        'excluding_extended_context': Stratum([t for t in tasks if t['task_id'] not in extended], replicates).table(rows, primary),
        'excluding_truncated': full.table(no_trunc, primary),
    }
    report['primary'] = report['effects']['critical_omission_rate:bn-en']
    review_count = sum(len(v['changes']) for m in models for s in read_jsonl(RESULTS / f'scores/{m}.jsonl')
                       for v in s.get('reviews', []))
    if review_count:
        initial, _ = load_rows(before_review=True)
        report['review'] = {'corrected_items': review_count, 'initial_effects': full.table(initial, primary)}
    return report


def fmt(v, digits=3):
    return 'NA' if v is None else f'{v:+.{digits}f}'


def fmt_ci(ci):
    return 'NA' if ci[0] is None else f'[{ci[0]:+.3f}, {ci[1]:+.3f}]'


def summary(report, models):
    names = {k: m['model_id'] for k, m in models.items()}
    p = report['primary']
    lines = ['# Results: preliminary 157-task study', '',
             f"Generated {report['generated_at_utc'][:10]} by `scripts/06_analyze.py` "
             f"({report['replicates']:,} bootstrap replicates, seed {report['seed']}).", '',
             '## Primary estimand', '',
             'Critical omission rate, BN minus EN (positive = more critical omission in Bengali); paired by task, '
             'domain-equal, three primary models weighted equally.', '',
             '| Model | Estimate | 95% CI | Paired tasks |', '|---|---:|---|---:|']
    for m in report['models']:
        lines.append(f"| {names[m]} | {fmt(p['by_model'][m])} | {fmt_ci(p['by_model_ci95'][m])} | {p['paired_tasks'][m]} |")
    lines += [f"| **Panel** | **{fmt(p['estimate'])}** | **{fmt_ci(p['ci95'])}** | |", '',
              '## Language means by model', '',
              '| Model | Language | Critical omission | Critical coverage | RIU coverage | Strict complete-task | CHECK-01 pass |',
              '|---|---|---:|---:|---:|---:|---:|']
    for key, d in report['descriptive'].items():
        m, lang = key.split(':')
        lines.append(f"| {names[m]} | {lang} | {d['critical_omission_rate']:.3f} | {d['critical_coverage']:.3f} | "
                     f"{d['riu_coverage']:.3f} | {d['strict_complete_task_success']:.3f} | {d['unsupported_content_pass']:.3f} |")
    lines += ['', '## Secondary contrasts (panel and by model)', '',
              '| Outcome | Contrast | Panel [95% CI] | ' + ' | '.join(names[m] for m in report['models']) + ' |',
              '|---|---|---|' + '---|' * len(report['models'])]
    for name in ('critical_omission_rate', 'critical_coverage', 'riu_coverage', 'strict_complete_task_success'):
        for a, b in CONTRASTS:
            e = report['effects'][f'{name}:{a}-{b}']
            lines.append(f"| {name.replace('_', ' ')} | {a} − {b} | {fmt(e['estimate'])} {fmt_ci(e['ci95'])} | "
                         + ' | '.join(fmt(e['by_model'][m]) for m in report['models']) + ' |')
    lines += ['', '## Primary estimand by stratum', '', '| Stratum | Panel [95% CI] | '
              + ' | '.join(names[m] for m in report['models']) + ' |', '|---|---|' + '---|' * len(report['models'])]
    strata = [(f'domain: {d}', t) for d, t in report['by_domain'].items()]
    strata += [(f'difficulty: {d}', t) for d, t in report['by_difficulty'].items()]
    strata += [('extended context only', report['extended_context_only']),
               ('excluding extended context', report['excluding_extended_context']),
               ('excluding truncated responses', report['excluding_truncated'])]
    for label, table in strata:
        e = table['critical_omission_rate:bn-en']
        lines.append(f"| {label} | {fmt(e['estimate'])} {fmt_ci(e['ci95'])} | " + ' | '.join(fmt(e['by_model'][m]) for m in report['models']) + ' |')
    lines += ['', '## Exploratory: Gemini (20 tasks, descriptive only)', '',
              '| Language | n | Critical omission | Critical coverage | RIU coverage |', '|---|---:|---:|---:|---:|']
    for key, d in report['exploratory_descriptive'].items():
        if d['n']:
            lines.append(f"| {key.split(':')[1]} | {d['n']} | {d['critical_omission_rate']:.3f} | {d['critical_coverage']:.3f} | {d['riu_coverage']:.3f} |")
    if report.get('review'):
        lines += ['', '## Score review', '',
                  f"{report['review']['corrected_items']} item ratings were corrected after review of the 17 QA disagreements. "
                  'These tables use corrected ratings; original ratings and review reasons remain in the score records. '
                  'This targeted review is not a full revalidation of the judge. Human QA agreement in results/qa/ uses the initial judge ratings.', '',
                  '| Outcome / contrast | Initial [95% CI] | After review [95% CI] |', '|---|---|---|']
        for key in ('critical_omission_rate:bn-en', 'critical_coverage:bn-en',
                    'strict_complete_task_success:bn-en', 'riu_coverage:bn_cs-bn'):
            before, after = report['review']['initial_effects'][key], report['effects'][key]
            lines.append(f"| {key} | {fmt(before['estimate'])} {fmt_ci(before['ci95'])} | "
                         f"{fmt(after['estimate'])} {fmt_ci(after['ci95'])} |")
    lines += ['', f"Truncated responses retained in the primary analysis: {', '.join(report['truncated_cells']) or 'none'}.",
              'Scores originate from the automated judge, with recorded review corrections where present; '
              'the QA sample study is in results/qa/.']
    return '\n'.join(lines) + '\n'


def figures(report, models, out_dir):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    out_dir.mkdir(parents=True, exist_ok=True)
    names = {k: m['model_id'].split('/')[-1] for k, m in models.items()}
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.6), sharey=True)
    labels = [names[m] for m in report['models']] + ['Panel']
    for ax, (a, b) in zip(axes, CONTRASTS):
        e = report['effects'][f'critical_omission_rate:{a}-{b}']
        est = [e['by_model'][m] for m in report['models']] + [e['estimate']]
        cis = [e['by_model_ci95'][m] for m in report['models']] + [e['ci95']]
        y = np.arange(len(labels))[::-1]
        ax.errorbar(est, y, xerr=[[v - c[0] for v, c in zip(est, cis)], [c[1] - v for v, c in zip(est, cis)]],
                    fmt='o', color='#2b5c8a', capsize=3)
        ax.axvline(0, color='#888', lw=0.8)
        ax.set_title(f'{a.upper().replace("_", "-")} − {b.upper().replace("_", "-")}', fontsize=10)
        ax.set_yticks(y, labels)
        ax.set_xlabel('Δ critical omission rate')
    fig.suptitle('Critical omission rate: paired language differences (95% CI)', fontsize=11)
    fig.tight_layout()
    fig.savefig(out_dir / 'critical_omission_effects.png', dpi=200)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7, 3.6))
    width = 0.25
    for i, lang in enumerate(LANGS):
        vals = [report['descriptive'][f'{m}:{lang}']['critical_coverage'] for m in report['models']]
        ax.bar(np.arange(len(vals)) + (i - 1) * width, vals, width, label=lang.upper().replace('_', '-'))
    ax.set_xticks(np.arange(len(report['models'])), [names[m] for m in report['models']])
    ax.set_ylim(0.5, 1.0)
    ax.set_ylabel('Mean critical coverage')
    ax.legend(frameon=False, ncol=3)
    fig.tight_layout()
    fig.savefig(out_dir / 'critical_coverage_by_language.png', dpi=200)
    plt.close(fig)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--replicates', type=int, default=10_000)
    a = p.parse_args()
    models = load_models()
    report = analyze(a.replicates)
    out = RESULTS / 'analysis'
    write_json(out / 'results.json', report)
    text = summary(report, models)
    (out / 'summary.md').write_text(text, encoding='utf-8')
    figures(report, models, out)
    print(text)
    return 0


if __name__ == '__main__':
    sys.exit(main())
