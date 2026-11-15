#!/usr/bin/env python3
"""Step 10 (post hoc): Qwen and Gemma with thinking enabled, on a task subset.

In the main study Sol answered with medium reasoning effort while Qwen and Gemma ran with
thinking disabled. This step asks whether enabling thinking changes the Bengali gap of the
open-weight models. It regenerates EN and BN responses for a seeded subset of tasks with
critical RIUs (by default 6 per domain: 1 easy, 2 medium, 3 hard), scores them with the
validated judge procedure, and compares the BN - EN gap with and without thinking on the
same tasks.

Differences from the main run, recorded in the outputs:
- the chat template is applied with enable_thinking=True;
- decoding uses each checkpoint's own sampling settings (generation_config) with a fixed
  seed per cell, because greedy decoding in thinking mode tends to repeat until the token
  limit;
- the reasoning trace is stored separately and only the final answer is scored;
- with --batch-size above 1 (used for Gemma), cells run in left-padded batches seeded once
  per batch, so a sample depends on its batch; the batch seed, size and members are
  recorded in each response's "batch" field.

Stored study responses and scores are not touched; outputs go to results/thinking/.

    python3 scripts/10_thinking_subset.py plan --model qwen
    python3 scripts/10_thinking_subset.py generate --model qwen --verify-weights
    python3 scripts/10_thinking_subset.py generate --model gemma --verify-weights --batch-size 8
    python3 scripts/10_thinking_subset.py score --max-usd 10
    python3 scripts/10_thinking_subset.py analyze

Generation and scoring resume where they stopped. Analysis uses every task that has both
an EN and a BN response for a model, so it can be run on a partial set.
"""
import argparse
import hashlib
import importlib.util
import os
import random
import time

import numpy as np

from common import (RESULTS, SCORING_PROCEDURE, append_jsonl, call_judge, cost_usd, load_annotations, load_env, load_judge,
                    load_models, load_prompts, load_study, read_jsonl, scoring_prompt, sha256_text, spent_usd, utc_now,
                    validate_ratings, write_json)

OUT = RESULTS / 'thinking'
SEED = 20261023
REPLICATES = 2000
MODELS = ('qwen', 'gemma')
LANGS = ('en', 'bn')
PER_DOMAIN = {'easy': 1, 'medium': 2, 'hard': 3}
METRICS = ('critical_coverage', 'strict_complete_task_success', 'critical_omission_rate', 'critical_unmet_rate')
END_MARKERS = ('</think>', '<channel|>', '[/THINK]')
START_MARKERS = ('<think>', '<|channel>thought', '[THINK]')


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, RESULTS.parent / 'scripts' / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def subset_tasks(per_domain=PER_DOMAIN):
    """Seeded task subset, drawn per domain and difficulty from tasks with critical RIUs."""
    gold = load_annotations('gold')
    study_ids = [t['task_id'] for t in load_study()['tasks']]
    pool = [gold[t] for t in study_ids if any(u['criticality'] == 'critical' for u in gold[t]['rius'])]
    rng = random.Random(SEED)
    chosen = []
    for domain in sorted({r['domain'] for r in pool}):
        for level, n in per_domain.items():
            cands = sorted(r['task_id'] for r in pool if r['domain'] == domain and r['difficulty'] == level)
            rng.shuffle(cands)
            chosen += cands[:n]
    rng.shuffle(chosen)
    return chosen


def cells(key, tasks):
    """EN and BN for each task, adjacent, so a stopped run still leaves complete pairs."""
    prompts = load_prompts()
    done = {(r['task_id'], r['language']) for r in read_jsonl(OUT / f'responses_{key}.jsonl')}
    return [{'task_id': t, 'language': lang, 'prompt_text': prompts[t]['prompt_' + lang]}
            for t in tasks for lang in LANGS if (t, lang) not in done]


def cell_seed(model_seed, task_id, lang):
    return model_seed + int(hashlib.sha256(f'{task_id}/{lang}'.encode()).hexdigest()[:8], 16) % 1_000_000


def split_thinking(raw, special_tokens):
    """Return (thinking, answer, finished_thinking) from the raw decoded output."""
    ends = [(raw.rfind(m), m) for m in END_MARKERS if m in raw]
    if ends:
        pos, marker = max(ends)
        thinking, answer = raw[:pos], raw[pos + len(marker):]
        finished = True
    elif any(m in raw for m in START_MARKERS):
        thinking, answer, finished = raw, '', False
    else:
        thinking, answer, finished = '', raw, True
    for tok in sorted(special_tokens, key=len, reverse=True):
        answer = answer.replace(tok, '')
        thinking = thinking.replace(tok, '')
    for m in START_MARKERS + END_MARKERS:
        thinking = thinking.replace(m, '')
    return thinking.strip(), answer.strip(), finished


def make_thinking_model(gen):
    class ThinkingModel(gen.LocalModel):
        """The study's local runtime with thinking enabled and the checkpoint's sampling settings."""

        def generate(self, prompt, seed):
            torch, cfg = self.torch, self.model_cfg
            max_new = self.study['max_output_tokens']
            ids = self.tokenizer.apply_chat_template(
                [{'role': 'system', 'content': self.study['system_prompt']}, {'role': 'user', 'content': prompt}],
                tokenize=True, add_generation_prompt=True, enable_thinking=True, return_dict=False)
            if len(ids) + max_new > cfg['context_tokens']:
                raise RuntimeError('input plus output allowance exceeds the context window')
            gc = self.model.generation_config
            sampling = {'do_sample': True, 'temperature': gc.temperature, 'top_p': gc.top_p, 'top_k': gc.top_k}
            torch.manual_seed(seed)
            inputs = torch.tensor([ids], dtype=torch.long, device='cuda')
            with torch.inference_mode():
                result = self.model.generate(input_ids=inputs, attention_mask=torch.ones_like(inputs), max_new_tokens=max_new,
                                             use_cache=True, eos_token_id=self.eos, pad_token_id=self.pad,
                                             prefill_chunk_size=cfg['prefill_chunk_size'], **sampling)
            output = result[0, len(ids):].tolist()
            raw = self.tokenizer.decode(output, skip_special_tokens=False)
            thinking, answer, finished = split_thinking(raw, self.tokenizer.all_special_tokens)
            ended = bool(output and output[-1] in self.eos)
            thinking_tokens = len(self.tokenizer.encode(thinking, add_special_tokens=False)) if thinking else 0
            return {'response_text': answer, 'thinking_text': thinking, 'thinking_finished': finished,
                    'returned_model': cfg['model_id'], 'finish_status': 'stop' if ended else 'length',
                    'truncated': not ended and len(output) >= max_new, 'sampling': sampling,
                    'usage': {'input_tokens': len(ids), 'output_tokens': len(output), 'thinking_tokens': thinking_tokens}}

        def generate_batch(self, prompts, seed):
            """Several prompts in one left-padded generate call, seeded once per batch.

            Rows share one random stream, so a row's sample depends on the batch it ran in;
            the batch seed and composition are recorded with each response.
            """
            torch, cfg = self.torch, self.model_cfg
            max_new = self.study['max_output_tokens']
            all_ids = [self.tokenizer.apply_chat_template(
                [{'role': 'system', 'content': self.study['system_prompt']}, {'role': 'user', 'content': p}],
                tokenize=True, add_generation_prompt=True, enable_thinking=True, return_dict=False) for p in prompts]
            width = max(len(ids) for ids in all_ids)
            if width + max_new > cfg['context_tokens']:
                raise RuntimeError('input plus output allowance exceeds the context window')
            gc = self.model.generation_config
            sampling = {'do_sample': True, 'temperature': gc.temperature, 'top_p': gc.top_p, 'top_k': gc.top_k}
            inputs = torch.tensor([[self.pad] * (width - len(ids)) + ids for ids in all_ids], dtype=torch.long, device='cuda')
            mask = torch.tensor([[0] * (width - len(ids)) + [1] * len(ids) for ids in all_ids], dtype=torch.long, device='cuda')
            torch.manual_seed(seed)
            with torch.inference_mode():
                result = self.model.generate(input_ids=inputs, attention_mask=mask, max_new_tokens=max_new,
                                             use_cache=True, eos_token_id=self.eos, pad_token_id=self.pad, **sampling)
            rows = []
            for ids, row in zip(all_ids, result[:, width:].tolist()):
                stop = next((i for i, tok in enumerate(row) if tok in self.eos), None)
                output = row if stop is None else row[:stop + 1]
                raw = self.tokenizer.decode(output, skip_special_tokens=False)
                thinking, answer, finished = split_thinking(raw, self.tokenizer.all_special_tokens)
                ended = stop is not None
                thinking_tokens = len(self.tokenizer.encode(thinking, add_special_tokens=False)) if thinking else 0
                rows.append({'response_text': answer, 'thinking_text': thinking, 'thinking_finished': finished,
                             'returned_model': cfg['model_id'], 'finish_status': 'stop' if ended else 'length',
                             'truncated': not ended and len(output) >= max_new, 'sampling': sampling,
                             'usage': {'input_tokens': len(ids), 'output_tokens': len(output),
                                       'thinking_tokens': thinking_tokens}})
            return rows
    return ThinkingModel


# ---------------------------------------------------------------- generation

def plan(key, tasks):
    todo = cells(key, tasks)
    print(f'{key}: {len(tasks)} tasks, {len(todo)} cells to generate')
    for c in todo[:10]:
        print(' ', c['task_id'], c['language'])


def record(key, model, cell, seed, result, latency, batch=None):
    rec = {'task_id': cell['task_id'], 'language': cell['language'], 'model': key, 'thinking': True,
           'model_id': model['model_id'], 'returned_model': result['returned_model'], 'seed': seed,
           'sampling': result['sampling'], 'prompt_sha256': sha256_text(cell['prompt_text']),
           'response_text': result['response_text'], 'response_sha256': sha256_text(result['response_text']),
           'thinking_text': result['thinking_text'], 'thinking_finished': result['thinking_finished'],
           'finish_status': result['finish_status'], 'truncated': result['truncated'],
           'usage': result['usage'], 'latency_seconds': latency, 'generated_at_utc': utc_now()}
    if batch is not None:
        rec['batch'] = batch
    return rec


def generate_batched(key, model, client, todo, batch_size, out, errors):
    """Run cells in batches; on CUDA out-of-memory, retry the batch as two halves."""
    torch = client.torch
    queue = [todo[i:i + batch_size] for i in range(0, len(todo), batch_size)]
    while queue:
        group = queue.pop(0)
        seed = cell_seed(model['seed'], group[0]['task_id'], group[0]['language'])
        started = time.perf_counter()
        try:
            results = client.generate_batch([c['prompt_text'] for c in group], seed)
        except torch.OutOfMemoryError:
            torch.cuda.empty_cache()
            if len(group) == 1:
                raise
            half = len(group) // 2
            print(f'out of memory at batch size {len(group)}; retrying as {half} + {len(group) - half}', flush=True)
            queue[:0] = [group[:half], group[half:]]
            continue
        except RuntimeError as exc:
            for cell in group:
                append_jsonl(errors, {'task_id': cell['task_id'], 'language': cell['language'], 'model': key,
                                      'error': str(exc)[:500], 'at_utc': utc_now()})
                print(cell['task_id'], cell['language'], 'FAILED', str(exc)[:200], flush=True)
            continue
        latency = round(time.perf_counter() - started, 3)
        members = [f"{c['task_id']}/{c['language']}" for c in group]
        for i, (cell, result) in enumerate(zip(group, results)):
            batch = {'size': len(group), 'index': i, 'seed_scope': 'batch', 'members': members}
            append_jsonl(out, record(key, model, cell, seed, result, latency, batch))
            u = result['usage']
            print(cell['task_id'], cell['language'], 'ok', f"{u['output_tokens']} tokens ({u['thinking_tokens']} thinking)",
                  f'batch {len(group)} {latency:.0f}s', flush=True)
        torch.cuda.empty_cache()


def generate(key, tasks, limit=None, verify_weights=False, batch_size=1):
    gen = _load('generate', '02_generate.py')
    model = load_models()[key]
    if model['provider'] != 'local':
        raise RuntimeError(f'{key} is not a local model')
    client = make_thinking_model(gen)(model, load_study(), verify_weights)
    OUT.mkdir(parents=True, exist_ok=True)
    out, errors = OUT / f'responses_{key}.jsonl', OUT / f'responses_{key}.errors.jsonl'
    if batch_size > 1:
        todo = cells(key, tasks)
        generate_batched(key, model, client, todo if limit is None else todo[:limit], batch_size, out, errors)
        return
    done = 0
    for cell in cells(key, tasks):
        if limit is not None and done >= limit:
            break
        seed = cell_seed(model['seed'], cell['task_id'], cell['language'])
        started = time.perf_counter()
        try:
            result = client.generate(cell['prompt_text'], seed)
        except RuntimeError as exc:
            append_jsonl(errors, {'task_id': cell['task_id'], 'language': cell['language'], 'model': key,
                                  'error': str(exc)[:500], 'at_utc': utc_now()})
            print(cell['task_id'], cell['language'], 'FAILED', str(exc)[:200], flush=True)
            continue
        latency = round(time.perf_counter() - started, 3)
        append_jsonl(out, record(key, model, cell, seed, result, latency))
        done += 1
        u = result['usage']
        print(cell['task_id'], cell['language'], 'ok', f"{u['output_tokens']} tokens ({u['thinking_tokens']} thinking)",
              f'{latency:.0f}s', flush=True)


# ---------------------------------------------------------------- scoring

def score(limit=None, max_usd=10.0):
    load_env()
    if not os.environ.get('OPENAI_API_KEY'):
        raise RuntimeError('OPENAI_API_KEY missing')
    judge, annotations, prompts = load_judge(), load_annotations('gold'), load_prompts()
    paths = [OUT / f'scores_{k}.jsonl' for k in MODELS]
    start, done = spent_usd(*paths), 0
    for key in MODELS:
        out, errors = OUT / f'scores_{key}.jsonl', OUT / f'scores_{key}.errors.jsonl'
        scored = {(r['task_id'], r['language']) for r in read_jsonl(out)}
        for resp in read_jsonl(OUT / f'responses_{key}.jsonl'):
            if (resp['task_id'], resp['language']) in scored:
                continue
            if limit is not None and done >= limit:
                return
            if spent_usd(*paths) - start >= max_usd:
                raise RuntimeError(f'run spend reached ${max_usd}')
            rec = annotations[resp['task_id']]
            prompt = scoring_prompt(resp['task_id'], prompts[resp['task_id']]['prompt_' + resp['language']],
                                    resp['response_text'], rec)
            try:
                ratings, meta = call_judge(prompt, judge)
                validate_ratings(rec, ratings)
            except (RuntimeError, ValueError) as exc:
                append_jsonl(errors, {'task_id': resp['task_id'], 'language': resp['language'], 'model': key,
                                      'error': str(exc)[:500], 'at_utc': utc_now()})
                print(key, resp['task_id'], resp['language'], 'FAILED', str(exc)[:200], flush=True)
                continue
            append_jsonl(out, {'task_id': resp['task_id'], 'language': resp['language'], 'model': key, 'thinking': True,
                               'response_sha256': resp['response_sha256'], 'procedure': SCORING_PROCEDURE,
                               'judge_model': judge['model_id'], 'ratings': ratings, 'usage': meta['usage'],
                               'cost_usd': cost_usd(judge['model_id'], meta['usage']), 'scored_at_utc': utc_now()})
            done += 1
            print(key, resp['task_id'], resp['language'], 'ok', flush=True)


# ---------------------------------------------------------------- analysis

def metric_rows(path, annotations, response_metrics, use_initial, initial_ratings):
    rows = {}
    for s in read_jsonl(path):
        ratings = initial_ratings(s) if use_initial else s['ratings']
        rows[s['task_id'], s['language']] = response_metrics(annotations[s['task_id']], ratings)
    return rows


def boot(values, rng):
    values = np.asarray(values, dtype=float)
    idx = rng.integers(0, len(values), (REPLICATES, len(values)))
    means = values[idx].mean(axis=1)
    return [round(float(np.percentile(means, 2.5)), 3), round(float(np.percentile(means, 97.5)), 3)]


def analyze():
    an = _load('analyze', '06_analyze.py')
    annotations = load_annotations('gold')
    rng = np.random.default_rng(SEED)
    report = {'generated_utc': utc_now(), 'seed': SEED, 'replicates': REPLICATES,
              'note': 'Post hoc. Thinking-on responses use the checkpoint sampling settings; thinking-off responses are the '
                      'stored study responses (greedy). Scores are initial judge ratings for both, so no review '
                      'corrections enter the comparison.', 'models': {}}
    lines = ['# Qwen and Gemma with thinking enabled (post hoc subset)', '',
             'Generated by `scripts/10_thinking_subset.py`. Paired BN − EN differences on the same tasks, with thinking off '
             '(stored study responses, greedy decoding) and on (checkpoint sampling settings, one seeded sample per cell). '
             f'95% CIs are percentile intervals from {REPLICATES:,} task resamples (seed {SEED}). Both arms use initial '
             'judge ratings.', '']
    for key in MODELS:
        on = metric_rows(OUT / f'scores_{key}.jsonl', annotations, an.response_metrics, True, an.initial_ratings)
        off = metric_rows(RESULTS / f'scores/{key}.jsonl', annotations, an.response_metrics, True, an.initial_ratings)
        tasks = sorted({t for t, _ in on if (t, 'en') in on and (t, 'bn') in on})
        if not tasks:
            continue
        responses = read_jsonl(OUT / f'responses_{key}.jsonl')
        model_report = {'tasks': len(tasks),
                        'truncated': sum(r['truncated'] for r in responses),
                        'unfinished_thinking': sum(not r['thinking_finished'] for r in responses),
                        'median_thinking_tokens': float(np.median([r['usage']['thinking_tokens'] for r in responses])),
                        'metrics': {}}
        lines += [f'## {key} ({len(tasks)} tasks with EN and BN)', '',
                  '| Metric | Off: EN / BN | Off: BN − EN | On: EN / BN | On: BN − EN | Change in gap (on − off) |',
                  '|---|---|---|---|---|---|']
        for metric in METRICS:
            use = [t for t in tasks if on[t, 'en'][metric] is not None]
            if not use:
                continue
            d_off = [off[t, 'bn'][metric] - off[t, 'en'][metric] for t in use]
            d_on = [on[t, 'bn'][metric] - on[t, 'en'][metric] for t in use]
            dd = [b - a for a, b in zip(d_off, d_on)]
            m = {'tasks': len(use),
                 'off_en': round(float(np.mean([off[t, 'en'][metric] for t in use])), 3),
                 'off_bn': round(float(np.mean([off[t, 'bn'][metric] for t in use])), 3),
                 'on_en': round(float(np.mean([on[t, 'en'][metric] for t in use])), 3),
                 'on_bn': round(float(np.mean([on[t, 'bn'][metric] for t in use])), 3),
                 'gap_off': round(float(np.mean(d_off)), 3), 'gap_off_ci95': boot(d_off, rng),
                 'gap_on': round(float(np.mean(d_on)), 3), 'gap_on_ci95': boot(d_on, rng),
                 'change': round(float(np.mean(dd)), 3), 'change_ci95': boot(dd, rng)}
            model_report['metrics'][metric] = m
            ci = lambda c: f'[{c[0]:+.3f}, {c[1]:+.3f}]'
            lines.append(f"| {metric.replace('_', ' ')} | {m['off_en']:.3f} / {m['off_bn']:.3f} | {m['gap_off']:+.3f} "
                         f"{ci(m['gap_off_ci95'])} | {m['on_en']:.3f} / {m['on_bn']:.3f} | {m['gap_on']:+.3f} "
                         f"{ci(m['gap_on_ci95'])} | {m['change']:+.3f} {ci(m['change_ci95'])} |")
        lines += ['', f"Thinking-on responses: {len(responses)}; median thinking tokens {model_report['median_thinking_tokens']:.0f}; "
                  f"truncated {model_report['truncated']}; thinking not finished {model_report['unfinished_thinking']}.", '']
        report['models'][key] = model_report
    lines += ['This check is post hoc, uses a task subset and one sample per cell, and is not part of the prespecified analysis.', '']
    write_json(OUT / 'results.json', report)
    (OUT / 'summary.md').write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='command', required=True)
    for name in ('plan', 'generate'):
        s = sub.add_parser(name)
        s.add_argument('--model', required=True, choices=MODELS)
        s.add_argument('--limit', type=int)
        if name == 'generate':
            s.add_argument('--verify-weights', action='store_true')
            s.add_argument('--batch-size', type=int, default=1,
                           help='cells per generate call; above 1, one seed per batch (recorded per response)')
    s = sub.add_parser('score')
    s.add_argument('--limit', type=int)
    s.add_argument('--max-usd', type=float, default=10.0)
    sub.add_parser('analyze')
    args = p.parse_args()
    tasks = subset_tasks()
    if args.command == 'plan':
        plan(args.model, tasks)
    elif args.command == 'generate':
        generate(args.model, tasks, args.limit, args.verify_weights, args.batch_size)
    elif args.command == 'score':
        score(args.limit, args.max_usd)
    else:
        analyze()


if __name__ == '__main__':
    main()
