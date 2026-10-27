#!/usr/bin/env python3
"""Step 02: generate model responses for every study cell.

One stateless request per (task, language, model), in the seeded cell order, with
the system prompt and 32,768-token output allowance from data/config/study.json.
Sol runs through the OpenAI Responses API (paid); Qwen and Gemma run in-process on
a CUDA GPU in BF16 with greedy decoding and thinking disabled. Resumable: cells
already in results/responses/<model>.jsonl are skipped; failures go to
results/responses/<model>.errors.jsonl.

    python3 scripts/02_generate.py plan --model sol
    python3 scripts/02_generate.py run --model sol --max-usd 10
    python3 scripts/02_generate.py run --model qwen [--verify-weights]

Gemini (exploratory, 20 tasks) is not regenerated; its responses are kept as collected.
"""
import argparse
import hashlib
import os
import random
import sys
import time
from pathlib import Path

from common import (LANGS, RESULTS, TransientError, append_jsonl, cost_usd, load_env, load_models, load_study,
                    openai_responses, output_text, read_jsonl, sha256_text, spent_usd, study_cells, utc_now,
                    with_retries)

THINK_MARKERS = ('<think>', '</think>', '<|channel>thought', '[THINK]')


def ordered_cells(model):
    """Cells in the study's seeded order: shuffle of snapshot order with seed + model offset."""
    study = load_study()
    cells = study_cells()
    random.Random(study['seed'] + model['order_offset']).shuffle(cells)
    return cells


def pending(model):
    done = {(r['task_id'], r['language']) for r in read_jsonl(RESULTS / f"responses/{model['key']}.jsonl")}
    return [c for c in ordered_cells(model) if (c['task_id'], c['language']) not in done]


class OpenAIModel:
    def __init__(self, model, study):
        self.model, self.study = model, study

    def generate(self, prompt):
        body = {'model': self.model['model_id'], 'instructions': self.study['system_prompt'], 'input': prompt,
                'reasoning': self.model['reasoning'], 'max_output_tokens': self.study['max_output_tokens'],
                'service_tier': self.model['service_tier']}
        payload = with_retries(lambda: openai_responses(body, self.model['timeout_seconds']))
        if payload.get('status') not in {'completed', 'incomplete'} or payload.get('error'):
            raise RuntimeError(f"provider status {payload.get('status')}: {payload.get('error')}")
        if payload.get('model') != self.model['model_id']:
            raise RuntimeError(f"returned model {payload.get('model')}")
        details = payload.get('incomplete_details') or {}
        return {'response_text': output_text(payload), 'returned_model': payload['model'],
                'finish_status': payload['status'], 'usage': payload.get('usage'),
                'truncated': payload['status'] == 'incomplete' and details.get('reason') == 'max_output_tokens'}


def file_sha256(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(8 << 20), b''):
            digest.update(block)
    return digest.hexdigest()


class LocalModel:
    """BF16 CUDA runtime from the pinned Hugging Face cache; no downloads, offload or remote code."""

    def __init__(self, model, study, verify_weights=False):
        import torch
        from transformers import AutoModelForMultimodalLM, AutoTokenizer
        self.torch, self.model_cfg, self.study = torch, model, study
        if not torch.cuda.is_available() or not torch.cuda.is_bf16_supported():
            raise RuntimeError('CUDA BF16 required')
        torch.set_num_threads(8)
        torch.manual_seed(model['seed'])
        snapshot = (Path.home() / '.cache/huggingface/hub' / ('models--' + model['model_id'].replace('/', '--'))
                    / 'snapshots' / model['revision'])
        pinned = {**model['tokenizer_sha256'], 'chat_template.jinja': model['chat_template_sha256'],
                  **(model['weights_sha256'] if verify_weights else {})}
        for name, expected in pinned.items():
            if file_sha256(snapshot / name) != expected:
                raise RuntimeError(f'{name} differs from the pinned checkpoint')
        self.tokenizer = AutoTokenizer.from_pretrained(snapshot, local_files_only=True, trust_remote_code=False)
        self.model = AutoModelForMultimodalLM.from_pretrained(
            snapshot, local_files_only=True, trust_remote_code=False, dtype=torch.bfloat16,
            device_map={'': 'cuda:0'}, attn_implementation=model['attention_backend']).eval()
        if any(p.device.type != 'cuda' for p in self.model.parameters()):
            raise RuntimeError('model parameters must all be on the GPU')
        native = self.model.generation_config.eos_token_id
        eos = native if isinstance(native, list) else [native]
        self.eos = sorted({int(x) for x in eos + [self.tokenizer.eos_token_id] if x is not None})
        self.pad = self.tokenizer.pad_token_id if self.tokenizer.pad_token_id is not None else self.eos[0]

    def generate(self, prompt):
        torch, cfg = self.torch, self.model_cfg
        max_new = self.study['max_output_tokens']
        ids = self.tokenizer.apply_chat_template(
            [{'role': 'system', 'content': self.study['system_prompt']}, {'role': 'user', 'content': prompt}],
            tokenize=True, add_generation_prompt=True, enable_thinking=False, return_dict=False)
        if len(ids) + max_new > cfg['context_tokens']:
            raise RuntimeError('input plus output allowance exceeds the context window')
        inputs = torch.tensor([ids], dtype=torch.long, device='cuda')
        with torch.inference_mode():
            result = self.model.generate(input_ids=inputs, attention_mask=torch.ones_like(inputs), max_new_tokens=max_new,
                                         do_sample=False, use_cache=True, eos_token_id=self.eos, pad_token_id=self.pad,
                                         prefill_chunk_size=cfg['prefill_chunk_size'])
        output = result[0, len(ids):].tolist()
        raw = self.tokenizer.decode(output, skip_special_tokens=False)
        if any(m in raw for m in THINK_MARKERS):
            raise RuntimeError('model emitted a reasoning channel with thinking disabled')
        ended = bool(output and output[-1] in self.eos)
        return {'response_text': self.tokenizer.decode(output, skip_special_tokens=True), 'returned_model': cfg['model_id'],
                'finish_status': 'stop' if ended else 'length', 'truncated': not ended and len(output) >= max_new,
                'usage': {'input_tokens': len(ids), 'output_tokens': len(output)}}


def run(model, limit=None, max_usd=10.0, verify_weights=False):
    study = load_study()
    if model['provider'] == 'openai':
        load_env()
        if not os.environ.get('OPENAI_API_KEY'):
            raise RuntimeError('OPENAI_API_KEY missing')
        client = OpenAIModel(model, study)
    elif model['provider'] == 'local':
        client = LocalModel(model, study, verify_weights)
    else:
        raise RuntimeError(f"{model['key']} is not generated by this study")
    out = RESULTS / f"responses/{model['key']}.jsonl"
    errors = RESULTS / f"responses/{model['key']}.errors.jsonl"
    start_spend = spent_usd(out)
    done = 0
    for cell in pending(model):
        if limit is not None and done >= limit:
            break
        if spent_usd(out) - start_spend >= max_usd:
            raise RuntimeError(f'run spend reached ${max_usd}')
        started = time.perf_counter()
        try:
            result = client.generate(cell['prompt_text'])
        except (RuntimeError, TransientError) as exc:
            append_jsonl(errors, {'task_id': cell['task_id'], 'language': cell['language'], 'model': model['key'],
                                  'error': str(exc)[:500], 'at_utc': utc_now()})
            print(cell['task_id'], cell['language'], 'FAILED', str(exc)[:200], flush=True)
            continue
        append_jsonl(out, {'task_id': cell['task_id'], 'language': cell['language'], 'model': model['key'],
                           'model_id': model['model_id'], 'returned_model': result['returned_model'],
                           'prompt_sha256': sha256_text(cell['prompt_text']), 'response_text': result['response_text'],
                           'response_sha256': sha256_text(result['response_text']), 'finish_status': result['finish_status'],
                           'truncated': result['truncated'], 'usage': result['usage'],
                           'cost_usd': cost_usd(model['model_id'], result['usage']),
                           'latency_seconds': round(time.perf_counter() - started, 3), 'generated_at_utc': utc_now()})
        done += 1
        print(cell['task_id'], cell['language'], 'ok', flush=True)
    return done


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='command', required=True)
    for name in ('plan', 'run'):
        s = sub.add_parser(name)
        s.add_argument('--model', required=True, choices=['sol', 'qwen', 'gemma'])
        if name == 'run':
            s.add_argument('--limit', type=int)
            s.add_argument('--max-usd', type=float, default=10.0)
            s.add_argument('--verify-weights', action='store_true')
    a = p.parse_args()
    model = load_models()[a.model]
    if a.command == 'plan':
        todo = pending(model)
        print(f"{a.model}: {len(study_cells()) - len(todo)} done, {len(todo)} pending")
        for lang in LANGS:
            print(f'  {lang}: {sum(c["language"] == lang for c in todo)} pending')
        return 0
    print('generated', run(model, a.limit, a.max_usd, a.verify_weights))
    return 0


if __name__ == '__main__':
    sys.exit(main())
