#!/usr/bin/env python3
"""Preliminary 157-task model evaluation runner.

Standard-library only. Commands:
  python3 scripts/prelim_eval_157.py check
  python3 scripts/prelim_eval_157.py plan
  python3 scripts/prelim_eval_157.py run --provider openai
  python3 scripts/prelim_eval_157.py run --provider anthropic
  python3 scripts/prelim_eval_157.py run --provider google
  python3 scripts/prelim_eval_157.py run --provider all

API keys are read only from environment variables named in
PRELIM_157_MODELS.json. Raw outputs are append-only JSONL.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import random
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "data" / "evaluation"
FREEZE_PATH = EVAL_DIR / "PRELIM_157_FREEZE.json"
MODEL_PATH = EVAL_DIR / "PRELIM_157_MODELS.json"
PROTOCOL_PATH = EVAL_DIR / "PRELIM_157_PROTOCOL.md"
ANALYSIS_PATH = EVAL_DIR / "PRELIM_157_ANALYSIS_PLAN.md"
OUTPUT_DIR = ROOT / "data" / "outputs" / "prelim_157"

LANG_FIELDS = {"en": "prompt_en", "bn": "prompt_bn", "bn_cs": "prompt_bn_cs"}
PROVIDER_INDEX = {"openai": 1, "anthropic": 2, "google": 3}


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def snapshot_task_ids(freeze: dict[str, Any]) -> list[str]:
    ids = list(freeze["pilot_task_ids"])
    ids.extend(x["task_id"] for x in freeze["expansion_tasks"])
    return ids


def load_annotations(freeze: dict[str, Any]) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for rel in freeze["annotation_file_pins"]:
        path = ROOT / rel
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            rec = json.loads(line)
            task_id = rec["task_id"]
            if task_id in records:
                raise RuntimeError(f"duplicate annotation task_id: {task_id}")
            records[task_id] = rec
    return records


def load_prompts(freeze: dict[str, Any]) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    prompt_files = [
        rel for rel in freeze["prompt_corpus_sha256"]
        if rel.endswith(".csv") and Path(rel).name != "manifest.csv"
    ]
    for rel in prompt_files:
        with (ROOT / rel).open("r", encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                task_id = row["task_id"]
                if task_id in rows:
                    raise RuntimeError(f"duplicate prompt task_id: {task_id}")
                rows[task_id] = row
    return rows


def verify_freeze() -> tuple[dict[str, Any], dict[str, Any], dict[str, dict[str, Any]], dict[str, dict[str, str]]]:
    freeze = read_json(FREEZE_PATH)
    models = read_json(MODEL_PATH)

    if freeze["status"] != "frozen-before-model-generation":
        raise RuntimeError("preliminary snapshot is not frozen")
    if freeze["task_count"] != 157 or freeze["prompt_instance_count"] != 471:
        raise RuntimeError("unexpected preliminary snapshot size")
    if models["run_count_per_prompt"] != 1:
        raise RuntimeError("preliminary run count must remain 1")

    # Prompt corpus SHA-256 pins.
    for rel, expected in freeze["prompt_corpus_sha256"].items():
        actual = sha256_file(ROOT / rel)
        if actual != expected:
            raise RuntimeError(f"prompt-corpus hash mismatch: {rel}: {actual} != {expected}")

    # Frozen pilot annotation SHA-256 pins.
    for rel, expected in freeze["pilot_annotation_sha256"].items():
        actual = sha256_file(ROOT / rel)
        if actual != expected:
            raise RuntimeError(f"pilot annotation hash mismatch: {rel}: {actual} != {expected}")

    # All 35 accepted annotation file Git-blob pins.
    for rel, meta in freeze["annotation_file_pins"].items():
        data = (ROOT / rel).read_bytes()
        actual = git_blob_sha1(data)
        if actual != meta["git_blob_sha"]:
            raise RuntimeError(f"annotation blob mismatch: {rel}: {actual} != {meta['git_blob_sha']}")
        if len(data) != meta["size_bytes"]:
            raise RuntimeError(f"annotation size mismatch: {rel}")

    annotations = load_annotations(freeze)
    prompts = load_prompts(freeze)
    ids = snapshot_task_ids(freeze)
    if len(ids) != 157 or len(set(ids)) != 157:
        raise RuntimeError("snapshot membership is not exactly 157 unique tasks")
    if set(ids) != set(annotations):
        missing = sorted(set(ids) - set(annotations))
        extra = sorted(set(annotations) - set(ids))
        raise RuntimeError(f"annotation membership mismatch; missing={missing}, extra={extra}")

    pilot_ids = set(freeze["pilot_task_ids"])
    for task_id in ids:
        rec = annotations[task_id]
        expected_status = "frozen" if task_id in pilot_ids else "human-reviewed"
        if rec.get("status") != expected_status:
            raise RuntimeError(
                f"snapshot annotation has unexpected status: {task_id}: "
                f"{rec.get('status')} != {expected_status}"
            )
        if task_id not in prompts:
            raise RuntimeError(f"missing frozen prompt row: {task_id}")
        row = prompts[task_id]
        for lang, field in LANG_FIELDS.items():
            prompt = row[field]
            actual = sha256_bytes(prompt.encode("utf-8"))
            expected = rec["prompt_sha256"][lang]
            if actual != expected:
                raise RuntimeError(
                    f"task prompt hash mismatch: {task_id}/{lang}: {actual} != {expected}"
                )

    if models["snapshot"] != "data/evaluation/PRELIM_157_FREEZE.json":
        raise RuntimeError("model config points to a different snapshot")

    return freeze, models, annotations, prompts


def artifact_hashes() -> dict[str, str]:
    return {
        "snapshot_sha256": sha256_file(FREEZE_PATH),
        "model_config_sha256": sha256_file(MODEL_PATH),
        "generation_protocol_sha256": sha256_file(PROTOCOL_PATH),
        "analysis_plan_sha256": sha256_file(ANALYSIS_PATH),
    }


def build_cells(
    freeze: dict[str, Any],
    annotations: dict[str, dict[str, Any]],
    prompts: dict[str, dict[str, str]],
    provider: str,
    seed: int,
    language: str | None = None,
) -> list[dict[str, Any]]:
    ids = snapshot_task_ids(freeze)
    cells: list[dict[str, Any]] = []
    for task_id in ids:
        rec = annotations[task_id]
        for lang, field in LANG_FIELDS.items():
            if language and lang != language:
                continue
            prompt_text = prompts[task_id][field]
            cells.append(
                {
                    "task_id": task_id,
                    "domain": rec["domain"],
                    "difficulty": rec["difficulty"],
                    "language": lang,
                    "prompt_text": prompt_text,
                    "prompt_sha256": rec["prompt_sha256"][lang],
                    "run_index": 1,
                    "provider": provider,
                }
            )
    rng = random.Random(seed + PROVIDER_INDEX[provider])
    rng.shuffle(cells)
    return cells


def http_json(
    url: str,
    headers: dict[str, str],
    body: dict[str, Any],
    timeout: int,
) -> tuple[dict[str, Any], int]:
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            return json.loads(raw.decode("utf-8")), resp.status
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", errors="replace")
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            payload = {"error_text": raw}
        payload["_http_status"] = e.code
        raise ProviderHTTPError(e.code, payload) from e


class ProviderHTTPError(RuntimeError):
    def __init__(self, status: int, payload: dict[str, Any]):
        super().__init__(f"HTTP {status}: {payload}")
        self.status = status
        self.payload = payload


def call_openai(model: dict[str, Any], prompt: str, system: str, timeout: int, max_tokens: int) -> dict[str, Any]:
    key = os.environ[model["env_key"]]
    body = {
        "model": model["model_id"],
        "instructions": system,
        "input": prompt,
        "reasoning": {"effort": "medium", "mode": "standard"},
        "max_output_tokens": max_tokens,
    }
    payload, status = http_json(
        "https://api.openai.com/v1/responses",
        {"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        body,
        timeout,
    )
    text_parts: list[str] = []
    if isinstance(payload.get("output_text"), str):
        text_parts.append(payload["output_text"])
    else:
        for item in payload.get("output", []):
            if item.get("type") != "message":
                continue
            for part in item.get("content", []):
                if part.get("type") == "output_text" and isinstance(part.get("text"), str):
                    text_parts.append(part["text"])
    return {
        "http_status": status,
        "response_text": "".join(text_parts),
        "provider_response_id": payload.get("id"),
        "returned_model": payload.get("model"),
        "finish_status": payload.get("status"),
        "usage": payload.get("usage"),
        "provider_raw_meta": {
            "incomplete_details": payload.get("incomplete_details"),
            "error": payload.get("error"),
        },
    }


def call_anthropic(model: dict[str, Any], prompt: str, system: str, timeout: int, max_tokens: int) -> dict[str, Any]:
    key = os.environ[model["env_key"]]
    body = {
        "model": model["model_id"],
        "max_tokens": max_tokens,
        "system": system,
        "messages": [{"role": "user", "content": prompt}],
        "output_config": {"effort": "medium"},
    }
    payload, status = http_json(
        "https://api.anthropic.com/v1/messages",
        {
            "x-api-key": key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
        },
        body,
        timeout,
    )
    text_parts = [
        block.get("text", "")
        for block in payload.get("content", [])
        if block.get("type") == "text"
    ]
    return {
        "http_status": status,
        "response_text": "".join(text_parts),
        "provider_response_id": payload.get("id"),
        "returned_model": payload.get("model"),
        "finish_status": payload.get("stop_reason"),
        "usage": payload.get("usage"),
        "provider_raw_meta": {
            "stop_sequence": payload.get("stop_sequence"),
        },
    }


def call_google(model: dict[str, Any], prompt: str, system: str, timeout: int, max_tokens: int) -> dict[str, Any]:
    key = os.environ[model["env_key"]]
    body = {
        "systemInstruction": {"parts": [{"text": system}]},
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "maxOutputTokens": max_tokens,
            "thinkingConfig": {"thinkingLevel": "medium"},
        },
    }
    payload, status = http_json(
        f"https://generativelanguage.googleapis.com/v1beta/models/{model['model_id']}:generateContent",
        {"x-goog-api-key": key, "Content-Type": "application/json"},
        body,
        timeout,
    )
    candidates = payload.get("candidates", [])
    first = candidates[0] if candidates else {}
    parts = first.get("content", {}).get("parts", [])
    text_parts = [
        p.get("text", "")
        for p in parts
        if isinstance(p.get("text"), str) and not p.get("thought", False)
    ]
    return {
        "http_status": status,
        "response_text": "".join(text_parts),
        "provider_response_id": payload.get("responseId"),
        "returned_model": payload.get("modelVersion") or model["model_id"],
        "finish_status": first.get("finishReason"),
        "usage": payload.get("usageMetadata"),
        "provider_raw_meta": {
            "finish_message": first.get("finishMessage"),
            "prompt_feedback": payload.get("promptFeedback"),
        },
    }


CALLERS = {
    "openai": call_openai,
    "anthropic": call_anthropic,
    "google": call_google,
}


def load_latest_success_keys(path: Path) -> set[tuple[str, str, str, int]]:
    done: set[tuple[str, str, str, int]] = set()
    if not path.exists():
        return done
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("status") == "success":
            done.add(
                (
                    row["task_id"],
                    row["language"],
                    row["requested_model"],
                    int(row["run_index"]),
                )
            )
    return done


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
        f.flush()
        os.fsync(f.fileno())


def should_retry(status: int) -> bool:
    return status == 429 or 500 <= status <= 599


def run_provider(
    provider: str,
    freeze: dict[str, Any],
    models: dict[str, Any],
    annotations: dict[str, dict[str, Any]],
    prompts: dict[str, dict[str, str]],
    limit: int | None,
    language: str | None,
    dry_run: bool,
) -> None:
    model = next(m for m in models["models"] if m["provider"] == provider)
    env_key = model["env_key"]
    if not dry_run and not os.environ.get(env_key):
        raise RuntimeError(f"missing required environment variable: {env_key}")

    output_path = OUTPUT_DIR / f"{provider}.jsonl"
    done = load_latest_success_keys(output_path)
    cells = build_cells(
        freeze,
        annotations,
        prompts,
        provider,
        int(models["request_order_seed"]),
        language=language,
    )

    pending = [
        cell for cell in cells
        if (cell["task_id"], cell["language"], model["model_id"], cell["run_index"]) not in done
    ]
    if limit is not None:
        pending = pending[:limit]

    print(f"{provider}: {len(done)} successful cells already present; {len(pending)} selected now")
    if dry_run:
        for cell in pending[:10]:
            print(f"  {cell['task_id']} {cell['language']} {cell['prompt_sha256'][:12]}")
        return

    hashes = artifact_hashes()
    caller = CALLERS[provider]
    system = models["system_prompt"]
    timeout = int(models["timeout_seconds"])
    max_tokens = int(models["max_output_tokens"])

    for idx, cell in enumerate(pending, 1):
        started = time.monotonic()
        attempt = 0
        last_error: dict[str, Any] | None = None
        while attempt < 4:
            attempt += 1
            try:
                result = caller(model, cell["prompt_text"], system, timeout, max_tokens)
                last_error = None
                elapsed = time.monotonic() - started
                row = {
                    "snapshot_id": freeze["snapshot_id"],
                    **hashes,
                    "task_id": cell["task_id"],
                    "domain": cell["domain"],
                    "difficulty": cell["difficulty"],
                    "language": cell["language"],
                    "prompt_sha256": cell["prompt_sha256"],
                    "prompt_text": cell["prompt_text"],
                    "provider": provider,
                    "requested_model": model["model_id"],
                    "returned_model": result["returned_model"],
                    "run_index": cell["run_index"],
                    "system_prompt": system,
                    "request_parameters": {
                        "reasoning": model["reasoning"],
                        "max_output_tokens": max_tokens,
                        "sampling_controls": model["sampling_controls"],
                        "tools_enabled": False,
                        "external_grounding": False,
                    },
                    "generated_at_utc": utc_now(),
                    "latency_seconds": round(elapsed, 6),
                    "attempt_count": attempt,
                    "status": "success",
                    "http_status": result["http_status"],
                    "provider_response_id": result["provider_response_id"],
                    "finish_status": result["finish_status"],
                    "usage": result["usage"],
                    "response_text": result["response_text"],
                    "provider_raw_meta": result["provider_raw_meta"],
                }
                append_jsonl(output_path, row)
                print(
                    f"[{idx}/{len(pending)}] {provider} {cell['task_id']} "
                    f"{cell['language']} success ({elapsed:.1f}s)"
                )
                break
            except ProviderHTTPError as e:
                last_error = {"type": "http", "status": e.status, "payload": e.payload}
                if attempt < 4 and should_retry(e.status):
                    time.sleep(2 ** attempt)
                    continue
                break
            except (TimeoutError, urllib.error.URLError) as e:
                last_error = {"type": type(e).__name__, "message": str(e)}
                if attempt < 4:
                    time.sleep(2 ** attempt)
                    continue
                break

        else:
            last_error = last_error or {"type": "unknown"}

        if last_error is not None:
            elapsed = time.monotonic() - started
            row = {
                "snapshot_id": freeze["snapshot_id"],
                **hashes,
                "task_id": cell["task_id"],
                "domain": cell["domain"],
                "difficulty": cell["difficulty"],
                "language": cell["language"],
                "prompt_sha256": cell["prompt_sha256"],
                "prompt_text": cell["prompt_text"],
                "provider": provider,
                "requested_model": model["model_id"],
                "run_index": cell["run_index"],
                "system_prompt": system,
                "request_parameters": {
                    "reasoning": model["reasoning"],
                    "max_output_tokens": max_tokens,
                    "sampling_controls": model["sampling_controls"],
                    "tools_enabled": False,
                    "external_grounding": False,
                },
                "generated_at_utc": utc_now(),
                "latency_seconds": round(elapsed, 6),
                "attempt_count": attempt,
                "status": "api_error",
                "error": last_error,
            }
            append_jsonl(output_path, row)
            print(
                f"[{idx}/{len(pending)}] {provider} {cell['task_id']} "
                f"{cell['language']} API ERROR"
            )


def command_check() -> None:
    freeze, models, annotations, prompts = verify_freeze()
    print("PRELIM-157 preflight PASS")
    print(f"snapshot: {freeze['snapshot_id']}")
    print(f"tasks: {len(snapshot_task_ids(freeze))}")
    print(f"prompt instances/model: {len(snapshot_task_ids(freeze)) * 3}")
    print(f"models: {', '.join(m['model_id'] for m in models['models'])}")
    for k, v in artifact_hashes().items():
        print(f"{k}: {v}")


def command_plan(provider: str, language: str | None) -> None:
    freeze, models, annotations, prompts = verify_freeze()
    providers = [m["provider"] for m in models["models"]] if provider == "all" else [provider]
    total = 0
    for p in providers:
        model = next(m for m in models["models"] if m["provider"] == p)
        output_path = OUTPUT_DIR / f"{p}.jsonl"
        done = load_latest_success_keys(output_path)
        cells = build_cells(freeze, annotations, prompts, p, int(models["request_order_seed"]), language)
        remaining = sum(
            (c["task_id"], c["language"], model["model_id"], c["run_index"]) not in done
            for c in cells
        )
        print(f"{p}: planned={len(cells)} success={len(done)} remaining={remaining}")
        total += remaining
    print(f"remaining selected cells: {total}")


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("check")

    plan = sub.add_parser("plan")
    plan.add_argument("--provider", choices=["openai", "anthropic", "google", "all"], default="all")
    plan.add_argument("--language", choices=["en", "bn", "bn_cs"])

    run = sub.add_parser("run")
    run.add_argument("--provider", choices=["openai", "anthropic", "google", "all"], required=True)
    run.add_argument("--language", choices=["en", "bn", "bn_cs"])
    run.add_argument("--limit", type=int)
    run.add_argument("--dry-run", action="store_true")

    args = parser.parse_args()
    if args.command == "check":
        command_check()
        return 0
    if args.command == "plan":
        command_plan(args.provider, args.language)
        return 0
    if args.command == "run":
        freeze, models, annotations, prompts = verify_freeze()
        providers = [m["provider"] for m in models["models"]] if args.provider == "all" else [args.provider]
        for p in providers:
            run_provider(
                p, freeze, models, annotations, prompts,
                limit=args.limit, language=args.language, dry_run=args.dry_run
            )
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
