"""Shared, stateless BF16 CUDA runtime for diagnostics and the local adapter.

No CPU offload, downloads, remote code, tools or truncation. Heavy dependencies
are imported only on runtime construction; ordinary validation stays stdlib-only.
"""
from __future__ import annotations
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import resource
import subprocess
import threading
import time

ROOT = Path(__file__).resolve().parents[1]
SYSTEM = "Answer the user's request directly."


def canonical_request_id(body):
    material={k:v for k,v in body.items() if k!='request_id'}
    return hashlib.sha256(json.dumps(material,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as source:
        for block in iter(lambda: source.read(8 * 1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


# Capture the imported source, rather than a potentially later on-disk edit.
RUNTIME_SOURCE_SHA256=sha256(Path(__file__))


def snapshot_path(model_id, revision):
    if len(revision) != 40 or any(c not in '0123456789abcdef' for c in revision):
        raise ValueError('exact 40-character cached revision required')
    path = Path.home()/'.cache/huggingface/hub'/('models--'+model_id.replace('/', '--'))/'snapshots'/revision
    if not path.is_dir():
        raise RuntimeError('pinned cached checkpoint unavailable; downloads disabled')
    return path


def verify_artifacts(model_id, revision):
    snapshot = snapshot_path(model_id, revision)
    prior = json.loads((ROOT/'data/evaluation/amendments/prelim-157-four-model-0.2/CANDIDATE_CACHE_METADATA.json').read_text())
    expected = next(c for c in prior['candidates'] if c['model_id'] == model_id and c['cached_revision'] == revision)
    hashes = {p.name: sha256(p) for p in sorted(snapshot.iterdir())
              if p.is_file() and (p.suffix in {'.json', '.jinja', '.safetensors', '.txt'})}
    for name, field in [('config.json', 'config_sha256'), ('chat_template.jinja', 'template_sha256'),
                        ('tokenizer_config.json', 'tokenizer_config_sha256'), ('tokenizer.json', 'tokenizer_json_sha256')]:
        if hashes[name] != expected[field]:
            raise RuntimeError('cached provenance mismatch: '+name)
    weights = sorted(snapshot.glob('*.safetensors'))
    if not weights or sum(p.stat().st_size for p in weights) != expected['cached_weight_file_bytes']:
        raise RuntimeError('weight file membership/size differs from cache inventory')
    registry = ROOT/'data/evaluation/amendments/prelim-157-four-model-0.2/gpu/UPSTREAM_ARTIFACTS.json'
    upstream = next(m for m in json.loads(registry.read_text())['models']
                    if m['model_id'] == model_id and m['returned_revision'] == revision)
    files = {f['name']: f for f in upstream['files']}
    if {p.name for p in weights} != {n for n in files if n.endswith('.safetensors')}:
        raise RuntimeError('weight membership differs from exact upstream revision')
    verified = {}
    for path in snapshot.iterdir():
        if path.name not in hashes or path.name not in files:
            continue
        meta = files[path.name]
        if path.stat().st_size != meta['size']:
            raise RuntimeError('upstream size mismatch: '+path.name)
        if meta.get('lfs'):
            matches = hashes[path.name] == meta['lfs']['sha256']
        else:
            data = path.read_bytes()
            matches = hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest() == meta['blob_id']
        if not matches:
            raise RuntimeError('upstream integrity mismatch: '+path.name)
        verified[path.name] = True
    return snapshot, {'model_id': model_id, 'revision': revision, 'artifact_sha256': hashes,
                      'upstream_integrity_checked': verified, 'upstream_registry_sha256': sha256(registry),
                      'cache_blob_names_are_not_assumed_lfs_sha256': True,
                      'weight_bytes': sum(p.stat().st_size for p in weights)}


class VisibleExtractionError(RuntimeError):
    def __init__(self,raw,ids):
        super().__init__('unexpected generated reasoning channel; visible parser refuses it')
        self.raw_output={'response_raw_text':raw,'output_token_ids':ids}


def extract_visible(tokenizer, ids):
    raw = tokenizer.decode(ids, skip_special_tokens=False)
    if any(marker in raw for marker in ('<think>', '</think>', '<|channel>thought', '[THINK]')):
        raise VisibleExtractionError(raw,ids)
    return tokenizer.decode(ids, skip_special_tokens=True), raw


class GPURuntime:
    def __init__(self, model_id, revision, context_tokens=40960, prefill_chunk_size=1024):
        import torch
        from transformers import AutoModelForMultimodalLM, AutoTokenizer
        self.torch, self.model_id, self.revision = torch, model_id, revision
        if not torch.cuda.is_available() or not torch.cuda.is_bf16_supported():
            raise RuntimeError('CUDA BF16 runtime required; never fall back to CPU')
        torch.set_num_threads(8)
        torch.manual_seed(20261023)
        self.snapshot, self.provenance = verify_artifacts(model_id, revision)
        self.tokenizer = AutoTokenizer.from_pretrained(self.snapshot, local_files_only=True, trust_remote_code=False)
        torch.cuda.reset_peak_memory_stats()
        started = time.perf_counter()
        self.model = AutoModelForMultimodalLM.from_pretrained(
            self.snapshot, local_files_only=True, trust_remote_code=False, dtype=torch.bfloat16,
            device_map={'': 'cuda:0'}, attn_implementation='sdpa').eval()
        torch.cuda.synchronize()
        self.load_seconds = time.perf_counter()-started
        config = getattr(self.model.config, 'text_config', self.model.config)
        self.native_context = config.max_position_embeddings
        if context_tokens > self.native_context:
            raise RuntimeError('configured context exceeds native checkpoint support')
        self.context_tokens = context_tokens
        self.prefill_chunk_size=prefill_chunk_size
        if any(p.device.type != 'cuda' for p in self.model.parameters()):
            raise RuntimeError('CPU/offloaded model parameters are forbidden in this configuration')
        native = self.model.generation_config.eos_token_id
        eos = native if isinstance(native, list) else [native]
        self.eos = sorted({int(x) for x in eos+[self.tokenizer.eos_token_id] if x is not None})
        self.pad = self.tokenizer.pad_token_id if self.tokenizer.pad_token_id is not None else self.eos[0]
        self.provenance.update(
            engine='transformers-bf16-cuda', engine_version=importlib.metadata.version('transformers'),
            versions={name: importlib.metadata.version(name) for name in
                      ['torch', 'transformers', 'accelerate', 'tokenizers', 'safetensors', 'huggingface-hub']},
            cuda_build=torch.version.cuda, gpu=torch.cuda.get_device_name(0),
            parameter_count=self.model.num_parameters(), precision='bfloat16', quantization='none',
            context_tokens=context_tokens, native_context_tokens=self.native_context,
            enable_thinking=False, do_sample=False, seed=20261023, eos_token_ids=self.eos,
            pad_token_id=self.pad, attention_backend='sdpa', cpu_offload=False,
            cuda_allocator_config=os.environ.get('PYTORCH_ALLOC_CONF',os.environ.get('PYTORCH_CUDA_ALLOC_CONF','default')),
            prefill_chunk_size=self.prefill_chunk_size,
            runtime_script_sha256=RUNTIME_SOURCE_SHA256, source_hash_capture='module import', load_seconds=self.load_seconds,
            load_peak_allocated_bytes=torch.cuda.max_memory_allocated(),
            load_peak_reserved_bytes=torch.cuda.max_memory_reserved())

    def render(self, prompt, system=SYSTEM):
        if system != SYSTEM:
            raise ValueError('unexpected common system instruction')
        return self.tokenizer.apply_chat_template(
            [{'role': 'system', 'content': system}, {'role': 'user', 'content': prompt}],
            tokenize=True, add_generation_prompt=True, enable_thinking=False, return_dict=False)

    def generate(self, prompt, max_new_tokens=512, system=SYSTEM, force_length=False):
        torch = self.torch
        ids = self.render(prompt, system)
        if max_new_tokens <= 0 or len(ids)+max_new_tokens > self.context_tokens:
            raise ValueError('context_exhausted: input plus output allowance exceeds configured context')
        inputs = torch.tensor([ids], dtype=torch.long, device='cuda')
        moments, samples, stop = [], [], threading.Event()
        class Stream:
            first = True
            def put(self, value):
                if self.first:
                    self.first = False
                else:
                    torch.cuda.synchronize()
                    moments.append(time.perf_counter())
            def end(self): pass
        def sample_gpu():
            while not stop.is_set():
                try:
                    p = subprocess.run(['nvidia-smi', '--query-gpu=utilization.gpu,memory.used',
                                        '--format=csv,noheader,nounits'], capture_output=True, text=True, timeout=5)
                    if p.returncode == 0:
                        row = p.stdout.strip().splitlines()[0].split(',')
                        samples.append({'utilization_percent': float(row[0]), 'memory_used_mib': float(row[1])})
                except (OSError, ValueError, IndexError, subprocess.TimeoutExpired): pass
                stop.wait(.5)
        thread = threading.Thread(target=sample_gpu, daemon=True)
        torch.cuda.synchronize()
        torch.cuda.reset_peak_memory_stats()
        thread.start()
        started = time.perf_counter()
        try:
            kwargs = {'max_new_tokens': max_new_tokens, 'do_sample': False, 'use_cache': True,
                      'eos_token_id': self.eos, 'pad_token_id': self.pad, 'streamer': Stream(),
                      'prefill_chunk_size':self.prefill_chunk_size}
            if force_length:
                kwargs['min_new_tokens'] = max_new_tokens
            with torch.inference_mode():
                result = self.model.generate(input_ids=inputs, attention_mask=torch.ones_like(inputs), **kwargs)
            torch.cuda.synchronize()
            elapsed = time.perf_counter()-started
            output = result[0, len(ids):].tolist()
            visible, raw = extract_visible(self.tokenizer, output)
            eos = bool(output and output[-1] in self.eos)
            ttft = moments[0]-started if moments else None
            return {'response_text': visible, 'response_raw_text': raw, 'output_token_ids': output,
                    'input_sha256': hashlib.sha256(prompt.encode()).hexdigest(), 'input_tokens': len(ids),
                    'output_tokens': len(output), 'max_new_tokens': max_new_tokens,
                    'forced_length_diagnostic': force_length,
                    'finish_reason': 'stop' if eos else 'length', 'ended_on_eos': eos,
                    'truncated': not eos and len(output) >= max_new_tokens,
                    'latency_seconds': elapsed, 'time_to_first_token_seconds': ttft,
                    'effective_prefill_tokens_per_second': len(ids)/ttft if ttft else None,
                    'decode_tokens_per_second': (len(moments)-1)/(moments[-1]-moments[0]) if len(moments)>1 else None,
                    'peak_allocated_gpu_bytes': torch.cuda.max_memory_allocated(),
                    'peak_reserved_gpu_bytes': torch.cuda.max_memory_reserved(),
                    'system_rss_high_water_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024,
                    'gpu_samples': samples,
                    'measurement_note': 'TTFT includes prefill and first decode; GPU synchronized streaming has timing overhead.'}
        finally:
            stop.set()
            thread.join(timeout=6)
