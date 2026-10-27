#!/usr/bin/env python3
"""Step 04: score every response with the validated judge procedure (scoring-0.5).

For each response in results/responses/<model>.jsonl, sends one blinded judge request
(task rubric, prompt and response only; no model identity) and appends the validated
ratings to results/scores/<model>.jsonl. Paid; resumable; a failed request is logged
to results/scores/<model>.errors.jsonl and retried on the next run.

    python3 scripts/04_score.py plan
    python3 scripts/04_score.py run --model all --max-usd 40
"""
import argparse
import os
import sys

from common import (RESULTS, SCORING_PROCEDURE, append_jsonl, call_judge, cost_usd, load_annotations, load_env, load_judge,
                    load_models, load_prompts, read_jsonl, scoring_prompt, spent_usd, utc_now, validate_ratings)


def pending(key):
    done = {(r['task_id'], r['language']) for r in read_jsonl(RESULTS / f'scores/{key}.jsonl')}
    return [r for r in read_jsonl(RESULTS / f'responses/{key}.jsonl') if (r['task_id'], r['language']) not in done]


def run(keys, limit=None, max_usd=40.0):
    load_env()
    if not os.environ.get('OPENAI_API_KEY'):
        raise RuntimeError('OPENAI_API_KEY missing')
    judge, annotations, prompts = load_judge(), load_annotations('gold'), load_prompts()
    paths = [RESULTS / f'scores/{k}.jsonl' for k in keys]
    start, done = spent_usd(*paths), 0
    for key in keys:
        out, errors = RESULTS / f'scores/{key}.jsonl', RESULTS / f'scores/{key}.errors.jsonl'
        for resp in pending(key):
            if limit is not None and done >= limit:
                return done
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
            append_jsonl(out, {'task_id': resp['task_id'], 'language': resp['language'], 'model': key,
                               'response_sha256': resp['response_sha256'], 'procedure': SCORING_PROCEDURE,
                               'judge_model': judge['model_id'], 'ratings': ratings, 'usage': meta['usage'],
                               'cost_usd': cost_usd(judge['model_id'], meta['usage']), 'scored_at_utc': utc_now()})
            done += 1
            print(key, resp['task_id'], resp['language'], 'ok', flush=True)
    return done


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='command', required=True)
    sub.add_parser('plan')
    r = sub.add_parser('run')
    r.add_argument('--model', default='all', choices=['all', *load_models()])
    r.add_argument('--limit', type=int)
    r.add_argument('--max-usd', type=float, default=40.0)
    a = p.parse_args()
    keys = list(load_models())
    if a.command == 'plan':
        for key in keys:
            print(f'{key}: {len(pending(key))} responses to score')
        return 0
    print('scored', run(keys if a.model == 'all' else [a.model], a.limit, a.max_usd))
    return 0


if __name__ == '__main__':
    sys.exit(main())
