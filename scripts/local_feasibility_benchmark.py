#!/usr/bin/env python3
"""CPU diagnostics only: never generate from study prompts.

Requires an isolated torch/Transformers environment. Uses existing cached files
only, pins a caller-supplied revision, writes a new append-only JSONL, and records
exact weight/template hashes. Corpus access is token counting only. Raw synthetic
outputs belong under ignored .local/, separately from study output paths.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
from pathlib import Path
import resource
import time

SYSTEM = "Answer the user's request directly."
DIAGNOSTICS = {
    "en": "Fictional diagnostic: An archive stores 12 files with 3 copies per file. State the total number of copies, then exactly three numbered read-only checks of backup integrity, at most five words per check. Do not delete data or share passwords. Answer in English, at most 30 words total.",
    "bn": "কাল্পনিক পরীক্ষা: একটি সংগ্রহশালায় ১২টি ফাইল আছে; প্রতিটি ফাইলের ৩টি অনুলিপি আছে। মোট অনুলিপির সংখ্যা বলুন, তারপর ব্যাকআপের অখণ্ডতা যাচাইয়ের জন্য ঠিক তিনটি নম্বরযুক্ত পরীক্ষা দিন যেগুলো তথ্য পরিবর্তন করে না। প্রতি পরীক্ষায় সর্বোচ্চ পাঁচটি শব্দ লিখুন। তথ্য মুছবেন না বা পাসওয়ার্ড অন্যকে দেবেন না। বাংলায় মোট ৩০ শব্দের মধ্যে উত্তর দিন।",
    "bn_cs": "Fictional diagnostic: একটি archive-এ ১২টি file আছে; প্রতিটি file-এর ৩টি copy আছে। মোট copy-এর সংখ্যা বলুন, তারপর backup integrity যাচাইয়ের জন্য ঠিক তিনটি numbered read-only check দিন; প্রতি check-এ সর্বোচ্চ পাঁচটি শব্দ। data delete বা password share করবেন না। বাংলায় মোট ৩০ শব্দের মধ্যে উত্তর দিন, প্রয়োজনে English technical term রাখুন।",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True,
                        choices=["Qwen/Qwen3.5-2B", "Qwen/Qwen3.5-4B", "Qwen/Qwen3.5-9B",
                                 "google/gemma-4-E2B-it", "google/gemma-4-E4B-it"])
    parser.add_argument("--revision", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--threads", type=int, default=16)
    parser.add_argument("--max-new-tokens", type=int, default=128)
    parser.add_argument("--long-context-tokens", type=int, default=4096)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    # Guard against accidentally mixing diagnostic records with study responses.
    if not args.output.resolve().is_relative_to(root / ".local"):
        parser.error("diagnostic output must be below ignored project .local/")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    destination = args.output.open("x", encoding="utf-8")

    def record(value: dict) -> None:
        value["observed_at_utc"] = datetime.now(timezone.utc).isoformat()
        destination.write(json.dumps(value, ensure_ascii=False) + "\n")
        destination.flush()

    import torch
    from transformers import AutoModelForMultimodalLM, AutoTokenizer
    torch.set_num_threads(args.threads)
    torch.set_num_interop_threads(1)
    torch.manual_seed(20261023)
    snapshot = (Path.home() / ".cache/huggingface/hub"
                / ("models--" + args.model.replace("/", "--")) / "snapshots" / args.revision)
    if not snapshot.is_dir():
        raise RuntimeError("Exact cached revision unavailable; downloads are disabled")
    files = sorted(snapshot.glob("*.safetensors"))
    record({"type": "provenance", "diagnostic_version": "synthetic-backup-0.2",
            "benchmark_script_sha256": sha256(Path(__file__)),
            "model_id": args.model, "revision": args.revision,
            "device": "cpu", "dtype": "float32", "quantization": "none",
            "threads": args.threads, "do_sample": False, "seed": 20261023,
            "enable_thinking": False, "max_new_tokens": args.max_new_tokens,
            "versions": {name: importlib.metadata.version(name) for name in
                         ["torch", "transformers", "accelerate", "tokenizers", "safetensors"]},
            "hashes": {p.name: sha256(p) for p in
                       [snapshot / "config.json", snapshot / "chat_template.jinja",
                        snapshot / "tokenizer_config.json", snapshot / "tokenizer.json"] + files},
            "weight_file_bytes": sum(p.stat().st_size for p in files)})
    tokenizer = AutoTokenizer.from_pretrained(snapshot, local_files_only=True)

    def template(prompt: str) -> list[int]:
        return tokenizer.apply_chat_template(
            [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}],
            tokenize=True, add_generation_prompt=True, enable_thinking=False,
            return_dict=False)

    # Read frozen prompts only to assess context, never to generate or select by outcomes.
    counts = []
    for path in sorted((root / "data/prompts").glob("*.csv")):
        with path.open(encoding="utf-8-sig", newline="") as source:
            for row in csv.DictReader(source):
                for language in ("en", "bn", "bn_cs"):
                    field = "prompt_" + language
                    if row.get(field):
                        counts.append((len(template(row[field])), row.get("task_id"), language))
    record({"type": "corpus_token_counts_only", "prompt_instances": len(counts),
            "longest": max(counts), "historical_max_output_tokens": 32768,
            "required_context_at_least": max(counts)[0] + 32768,
            "note": "No study-prompt generation. Template and tokenizers differ across families."})
    started = time.perf_counter()
    model = AutoModelForMultimodalLM.from_pretrained(
        snapshot, local_files_only=True, dtype=torch.float32, device_map="cpu",
        attn_implementation="sdpa")
    model.eval()
    native_eos = model.generation_config.eos_token_id
    eos_ids = list(native_eos) if isinstance(native_eos, list) else [native_eos]
    if tokenizer.eos_token_id is not None:
        eos_ids.append(tokenizer.eos_token_id)
    eos_ids = sorted({int(value) for value in eos_ids if value is not None})
    pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else eos_ids[0]
    record({"type": "loaded", "seconds": time.perf_counter() - started,
            "effective_eos_token_ids": eos_ids,
            "pad_token_id": pad_id,
            "rss_high_water_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024})

    class TimingStreamer:
        def __init__(self):
            self.times = []
            self.first_put = True

        def put(self, value):
            if self.first_put:
                self.first_put = False  # generate() initially sends prompt tokens.
            else:
                self.times.append(time.perf_counter())

        def end(self):
            pass

    prompts = list(DIAGNOSTICS.items())
    # A distinct synthetic long-input retrieval check; 4k is a smoke probe only.
    filler = "Archive entry: routine item, no action required. "
    prefix = "The unique lookup key is ORCHID-731.\n"
    while len(template(prefix)) < args.long_context_tokens:
        prefix += filler * 32
    prompts.append(("synthetic_long_context", prefix + "\nReply only with the unique lookup key."))
    for language, prompt in prompts:
        ids = template(prompt)
        inputs = torch.tensor([ids], dtype=torch.long)
        streamer = TimingStreamer()
        started = time.perf_counter()
        with torch.inference_mode():
            result = model.generate(input_ids=inputs, attention_mask=torch.ones_like(inputs),
                                    max_new_tokens=args.max_new_tokens, do_sample=False,
                                    eos_token_id=eos_ids,
                                    pad_token_id=pad_id,
                                    use_cache=True, streamer=streamer)
        elapsed = time.perf_counter() - started
        output_ids = result[0, len(ids):].tolist()
        ttft = streamer.times[0] - started if streamer.times else None
        decode = (len(streamer.times) - 1) / (streamer.times[-1] - streamer.times[0]) \
            if len(streamer.times) > 1 else None
        record({"type": "synthetic_generation", "diagnostic": language,
                "input_text": prompt if language != "synthetic_long_context" else None,
                "input_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
                "input_tokens": len(ids), "output_tokens": len(output_ids),
                "visible_output_raw": tokenizer.decode(output_ids, skip_special_tokens=False),
                "e2e_seconds": elapsed, "time_to_first_token_seconds": ttft,
                "effective_prefill_input_tokens_per_second": len(ids) / ttft if ttft else None,
                "decode_tokens_per_second": decode,
                "hit_output_limit": len(output_ids) == args.max_new_tokens,
                "ended_on_eos": bool(output_ids and output_ids[-1] in eos_ids),
                "rss_high_water_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024,
                "peak_gpu_memory_bytes": None,
                "scope": "diagnostic only; no human capability validation; no study score"})
        print(json.dumps({"diagnostic": language, "seconds": elapsed,
                          "output_tokens": len(output_ids)}), flush=True)


if __name__ == "__main__":
    main()
