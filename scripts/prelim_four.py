#!/usr/bin/env python3
"""Isolated four-model amendment driver. A candidate manifest cannot run a study.

Reuses the historical frozen task loader and cloud adapters. All amended outputs
live under .local; nothing here edits the original October 23 protocol/panel.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import platform
import time
from typing import Any
from urllib.parse import urlparse
import urllib.error
import urllib.request
import uuid

import prelim_eval_157 as historical

ROOT = Path(__file__).resolve().parents[1]
AMENDMENT = ROOT / "data/evaluation/amendments/prelim-157-four-model-0.3"
CONFIG = AMENDMENT / "MODELS.json"
MANIFEST = AMENDMENT / "FREEZE_CANDIDATE.json"
PARTITIONS = ("openai", "google", "local_a", "local_b")
ORDER_OFFSETS = dict(zip(PARTITIONS, (1, 3, 4, 5)))
PANELS = {
    'prelim-157-four-model-0.2': {'openai':'gpt-6-astra','google':'gemini-4-argon'},
    'prelim-157-four-model-0.3': {'openai':'gpt-6.1-sol','google':'gemini-3.8-flash'},
}
EXACT_CLOUD_IDS = PANELS['prelim-157-four-model-0.3']


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def output_root(config: dict[str, Any]) -> Path:
    # Keep raw data outside version control and prevent historic path collisions.
    path = (ROOT / config["output_directory"]).resolve()
    if not path.is_relative_to((ROOT / ".local").resolve()):
        raise RuntimeError("amendment outputs must be in ignored .local/")
    if path == (ROOT / ".local").resolve() or path.name == "prelim_157":
        raise RuntimeError("amendment requires its own output namespace")
    return path


def verify_candidate(config_path: Path = CONFIG, manifest_path: Path = MANIFEST):
    freeze, _, annotations, prompts = historical.verify_freeze()
    config, manifest = read(config_path), read(manifest_path)
    if config["protocol_id"] not in PANELS:
        raise RuntimeError("unexpected amendment protocol ID")
    if manifest["protocol_id"] != config["protocol_id"]:
        raise RuntimeError("manifest/config protocol mismatch")
    if manifest["historical_snapshot_sha256"] != digest(historical.FREEZE_PATH):
        raise RuntimeError("historical task snapshot hash mismatch")
    if (manifest.get("task_count"), manifest.get("prompt_instances_per_model"),
            manifest.get("planned_model_count"), manifest.get("planned_response_count")) != (157, 471, 4, 1884):
        raise RuntimeError("unexpected amended study dimensions")
    if [m["partition"] for m in config["models"]] != list(PARTITIONS):
        raise RuntimeError("exactly four ordered partitions required")
    panel=PANELS[config['protocol_id']]
    for model in config["models"]:
        p = model["partition"]
        if p in panel and model["model_id"] != panel[p]:
            raise RuntimeError(f"requested cloud model may not be substituted: {p}")
        if p in EXACT_CLOUD_IDS:
            expected_reasoning = ({"effort": "medium", "mode": "standard"} if p == "openai"
                                  else {"thinking_level": "medium"})
            if model.get("reasoning") != expected_reasoning or model.get("sampling_controls") != "omitted":
                raise RuntimeError("cloud configuration differs from the implemented fixed controls")
    if config["run_count_per_prompt"] != 1 or config["tools_enabled"] or config["external_grounding"]:
        raise RuntimeError("one stateless generation with no tools/grounding required")
    if config["system_prompt"] != "Answer the user's request directly.":
        raise RuntimeError("common system instruction changed")
    if config["max_output_tokens"] != 32768:
        raise RuntimeError("output allowance requires an explicit new protocol version")
    output_root(config)
    return config, manifest, freeze, annotations, prompts


def readiness(config: dict[str, Any], manifest: dict[str, Any]) -> list[str]:
    blockers = []
    if manifest.get("status") != "frozen-before-model-generation":
        blockers.append("amendment is a candidate, not an approved freeze")
    if manifest.get("pending_decisions"):
        blockers.extend(manifest["pending_decisions"])
    # A human-authored approval record is evidence, not an automatic acceptance.
    if not manifest.get("study_lead_approval_record"):
        blockers.append("study-lead protocol approval is not recorded")
    if config['protocol_id'].endswith('0.3') and not manifest.get('judge_approval_record'):
        blockers.append('explicit approval of the new primary judge is not recorded')
    for model in config["models"]:
        p = model["partition"]
        if not model.get("availability_evidence"):
            blockers.append(f"{p}: account/runtime model availability not verified")
        if config['protocol_id'].endswith('0.3') and p in EXACT_CLOUD_IDS:
            if not model.get('allowed_returned_model_ids') or not model.get('wire_validation_evidence'):
                blockers.append(f'{p}: synthetic wire validation and exact returned model versions not pinned')
            if p=='google':
                try:
                    if model.get('billing_policy')!='free-tier-only-no-paid-fallback':raise RuntimeError('free-tier-only policy required')
                    from gemini_quota import QuotaLedger
                    QuotaLedger(ROOT/model['quota_config'])
                except (RuntimeError,ValueError,KeyError,OSError) as exc:blockers.append('google: '+str(exc))
        if p.startswith("local_"):
            for field in ("model_id", "weights_revision", "tokenizer_revision", "quantization",
                          "engine", "engine_version", "context_tokens", "chat_template_sha256",
                          "weights_sha256", "tokenizer_sha256", "decoding", "feasibility_evidence",
                          "context_fit_evidence", "adapter_smoke_evidence"):
                if model.get(field) in (None, "", {}):
                    blockers.append(f"{p}: unpinned {field}")
            if model.get("engine") not in (None, "openai-compatible-local-server"):
                blockers.append(f"{p}: no study adapter for selected engine {model['engine']}")
    return blockers


def require_frozen(config, manifest, config_path=CONFIG, manifest_path=MANIFEST):
    blockers = readiness(config, manifest)
    if blockers:
        raise RuntimeError("study generation blocked: " + "; ".join(blockers))
    amendment=config_path.parent
    required = {str(config_path.relative_to(ROOT)),
                str((amendment / "PROTOCOL.md").relative_to(ROOT)),
                str((amendment / "ANALYSIS_PLAN.md").relative_to(ROOT)),
                str((amendment / "SCORING_PLAN.md").relative_to(ROOT)),
                str(Path(__file__).resolve().relative_to(ROOT)),
                str(Path(historical.__file__).resolve().relative_to(ROOT))}
    for name in ('prelim_four_judge.py','analyze_prelim_four.py','research_approvals.py',
                 'local_gpu_runtime.py','local_gpu_server.py','prelim_judge_157.py','analyze_prelim_157.py'):
        required.add('scripts/'+name)
    required.add(str((amendment/'JUDGE.json').relative_to(ROOT)))
    if config['protocol_id'].endswith('0.3'):
        required.update({'scripts/cloud_four_adapters.py','scripts/gemini_quota.py','scripts/plot_prelim_four.py','scripts/audit_four_qa.py'})
        from prelim_judge_157 import FIXTURE_PLAN,FIXTURES,ANSWER_KEY
        required.update(str(p.relative_to(ROOT)) for p in (FIXTURE_PLAN,FIXTURES,ANSWER_KEY,historical.FREEZE_PATH))
        if not manifest.get('judge_approval_record'):raise RuntimeError('explicit primary-judge approval evidence missing')
        required.add(manifest['judge_approval_record'])
    for model in config["models"]:
        for field in ("availability_evidence", "feasibility_evidence", "context_fit_evidence", "adapter_smoke_evidence",'wire_validation_evidence','quota_config'):
            if model.get(field):
                required.add(model[field])
        if model.get('quota_config'):
            required.add(read(ROOT/model['quota_config'])['evidence_path'])
    pins = manifest.get("artifact_sha256", {})
    if not required.issubset(pins):
        raise RuntimeError("freeze does not pin the config and all scientific plans")
    for rel, expected in pins.items():
        path = (ROOT / rel).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file() or digest(path) != expected:
            raise RuntimeError(f"amendment artifact changed or absent: {rel}")
    approval = (ROOT / manifest["study_lead_approval_record"]).resolve()
    if not approval.is_relative_to(ROOT) or not approval.is_file():
        raise RuntimeError("study-lead approval evidence is missing")
    if str(approval.relative_to(ROOT)) not in pins:
        raise RuntimeError("approval record must be hash-pinned")


def generation_readiness(config, manifest, config_path=CONFIG, manifest_path=MANIFEST):
    blockers = readiness(config, manifest)
    if not blockers:
        try:
            require_frozen(config, manifest, config_path, manifest_path)
            require_execution_gates(config,manifest,config_path,manifest_path)
        except (RuntimeError, ValueError, OSError) as exc:
            blockers.append(str(exc))
    return blockers


def require_execution_gates(config,manifest,config_path=CONFIG,manifest_path=MANIFEST):
    from research_approvals import require_spending_approval
    from prelim_four_judge import ScoringContext
    require_spending_approval(config,manifest,'generation')
    if config['protocol_id'].endswith('0.3'):
        from gemini_quota import QuotaLedger
        QuotaLedger(ROOT/next(m for m in config['models'] if m['partition']=='google')['quota_config'])
    if not ScoringContext(config_path,manifest_path).gate()['gate_pass']:
        raise RuntimeError('all study generation requires the passing four-model automated-judge gate')
    for model in config['models']:
        env=model.get('env_key') or model.get('endpoint_env')
        if env and not os.environ.get(env):
            raise RuntimeError('required panel credential/runtime setting is absent: '+env)


def cells_for(config, freeze, annotations, prompts, partition, language=None):
    # Historical helper uses provider offset 1 for OpenAI. Adjust seed so the
    # four offsets are fixed without mutating that helper's provider registry.
    seed = int(config["request_order_seed"]) + ORDER_OFFSETS[partition] - 1
    cells = historical.build_cells(freeze, annotations, prompts, "openai", seed, language)
    for cell in cells:
        cell["provider"] = partition
    return cells


def provenance(config_path=CONFIG, manifest_path=MANIFEST):
    result={"amendment_config_sha256": digest(config_path),
            "amendment_manifest_sha256": digest(manifest_path),
            "snapshot_sha256": digest(historical.FREEZE_PATH),
            "runner_sha256": digest(Path(__file__)),
            "adapter_sha256": digest(Path(historical.__file__)),
            "snapshot_id": read(manifest_path)["snapshot_id"]}
    if read(config_path)['protocol_id'].endswith('0.3'):
        result['cloud_adapter_sha256']=digest(ROOT/'scripts/cloud_four_adapters.py')
        result['quota_script_sha256']=digest(ROOT/'scripts/gemini_quota.py')
    return result


def validated_records(path, config, partition, expected_cells, pins):
    model = next(m for m in config["models"] if m["partition"] == partition)
    expected = {(c["task_id"], c["language"]): c for c in expected_cells}
    successes = {}
    errors = 0
    if not path.exists():
        return successes, errors
    for row in historical.read_jsonl_records(path):
        key = (row.get("task_id"), row.get("language"))
        if (row.get("protocol_id") != config["protocol_id"] or row.get("provider") != partition
                or row.get("requested_model") != model["model_id"] or row.get("run_index") != 1
                or any(row.get(k) != v for k, v in pins.items())
                or key not in expected or row.get("prompt_sha256") != expected[key]["prompt_sha256"]):
            raise RuntimeError(f"foreign/stale generation record in {path.name}")
        if row["status"] == "success":
            if config['protocol_id'].endswith('0.3') and partition in EXACT_CLOUD_IDS:
                from cloud_four_adapters import validate_identity
                validate_identity(model,row)
            text = row.get("response_text")
            if not isinstance(text, str) or row.get("response_sha256") != hashlib.sha256(text.encode("utf-8")).hexdigest():
                raise RuntimeError(f"response integrity mismatch in {path.name}")
            if key in successes:
                raise RuntimeError(f"duplicate successful cell in {path.name}: {key}")
            successes[key] = row
        elif row["status"] == "api_error":
            errors += 1
        else:
            raise RuntimeError(f"unknown record status in {path.name}")
    return successes, errors


def validate_attempt_history(path, config, partition, expected_cells, pins, successes):
    """An interrupted or successful-but-unserialized request cannot be replayed.

    Preserve its exact received payload (when available) for explicit recovery,
    rather than produce a second outcome after a process crash.
    """
    if not path.exists():
        return
    expected = {(c["task_id"], c["language"]): c for c in expected_cells}
    model = next(m for m in config["models"] if m["partition"] == partition)
    started, finished = {}, {}
    for row in historical.read_jsonl_records(path):
        key = (row.get("task_id"), row.get("language"))
        if (key not in expected or row.get("provider") != partition or row.get("run_index") != 1
                or row.get("protocol_id") != config["protocol_id"]
                or row.get("requested_model") != model["model_id"]
                or row.get("prompt_sha256") != expected[key]["prompt_sha256"]
                or any(row.get(k) != v for k, v in pins.items()) or not row.get("attempt_id")):
            raise RuntimeError(f"foreign/stale attempt record in {path.name}")
        identifier = row["attempt_id"]
        if row["status"] == "started":
            if identifier in started:
                raise RuntimeError("duplicate request-start event")
            started[identifier] = row
        else:
            if row["status"] not in {"success", "http_error", "transport_error", "runtime_error"}:
                raise RuntimeError("unknown attempt outcome status")
            if identifier not in started or identifier in finished:
                raise RuntimeError("attempt outcome has no unique request-start event")
            if any(row.get(k)!=started[identifier].get(k) for k in
                   ("task_id", "language", "prompt_sha256")):
                raise RuntimeError("attempt outcome belongs to a different cell")
            finished[identifier] = row
            if row["status"] == "success":
                source = successes.get(key)
                received = row.get("received_response", {}).get("response_text")
                if source is None or received != source.get("response_text"):
                    raise RuntimeError("successful attempt lacks its matching response record; reconcile preserved payload before resume")
    if set(started) != set(finished):
        raise RuntimeError("interrupted request has an ambiguous outcome; investigate attempt log before resume")


@contextmanager
def partition_lock(root: Path, partition: str):
    """Prevent two processes from generating the same cells or interleaving JSONL.

    A process killed without cleanup leaves an explicit lock to investigate;
    automatically stealing a lock can duplicate a billed/outcome generation.
    """
    root.mkdir(parents=True, exist_ok=True)
    path = root / f"{partition}.lock"
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise RuntimeError(f"partition locked; investigate before removing {path.name}") from exc
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as lock:
            json.dump({"pid": os.getpid(), "started_at": historical.utc_now()}, lock)
        yield
    finally:
        path.unlink()


class RejectLocalRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise historical.ProviderHTTPError(code, {"error": "local endpoint redirect refused"})


def local_http_json(url, headers, body, timeout):
    request = urllib.request.Request(url, data=json.dumps(body, ensure_ascii=False).encode(),
                                     headers=headers, method="POST")
    opener = urllib.request.build_opener(RejectLocalRedirects())
    try:
        with opener.open(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8")), response.status
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            payload = json.loads(raw)
        except ValueError:
            payload = {"error_text": raw}
        raise historical.ProviderHTTPError(exc.code, payload) from exc


def local_chat(model, prompt, system, timeout, max_tokens):
    """Adapter for a separately pinned local OpenAI-compatible chat server.

    The loopback server uses the same native CUDA runtime as the benchmarks.
    Selecting a checkpoint still requires recorded real synthetic smoke evidence.
    Never infer or strip private reasoning from an unpinned template.
    """
    endpoint = os.environ.get(model["endpoint_env"], "")
    parsed = urlparse(endpoint)
    if parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}:
        raise RuntimeError("local adapter requires an explicit loopback HTTP endpoint")
    if parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise RuntimeError("local endpoint must not contain credentials/query/fragment")
    if model.get("engine") != "openai-compatible-local-server":
        raise RuntimeError("this local inference engine has no validated study adapter")
    body = {"model": model["model_id"], "messages": [
        {"role": "system", "content": system}, {"role": "user", "content": prompt}],
        "max_tokens": max_tokens, "stream": False, **model["decoding"]}
    from local_gpu_runtime import canonical_request_id
    body['request_id']=canonical_request_id(body)
    if set(model["decoding"]) - {"temperature", "top_p", "seed", "stop", "chat_template_kwargs"}:
        raise RuntimeError("unsupported local decoding setting")
    payload, status = local_http_json(endpoint.rstrip("/") + "/chat/completions",
        {"Content-Type": "application/json"}, body, timeout)
    def invalid(message):
        # Keep the received response as evidence even when it cannot be scored.
        raise historical.ProviderHTTPError(status, {"validation_error": message,
                                                   "provider_raw_response": payload})
    choices = payload.get("choices", [])
    if len(choices) != 1:
        invalid("local server must return exactly one choice")
    choice = choices[0]
    if choice.get("finish_reason") not in {"stop", "length", "content_filter"}:
        invalid("unknown local finish reason")
    message = choice["message"]
    if message.get("reasoning_content") or message.get("reasoning"):
        invalid("local reasoning not disabled under the pinned template")
    text = message.get("content")
    if not isinstance(text, str):
        invalid("local server did not return visible response text")
    if payload.get("model") != model["model_id"]:
        invalid("local server returned a different model ID")
    if model.get('weights_revision'):
        actual=payload.get('runtime_provenance',{})
        if (payload.get('revision')!=model['weights_revision'] or actual.get('context_tokens')!=model['context_tokens']
                or actual.get('engine_version')!=model['engine_version'] or actual.get('precision')!='bfloat16'
                or actual.get('enable_thinking') is not False or actual.get('cpu_offload') is not False):
            invalid('local runtime provenance differs from pinned model configuration')
        for name,expected in {**model['weights_sha256'],**model['tokenizer_sha256']}.items():
            if actual.get('artifact_sha256',{}).get(name)!=expected:
                invalid('local loaded artifact hash mismatch')
        if model.get('chat_template_sha256') and actual.get('artifact_sha256',{}).get('chat_template.jinja')!=model['chat_template_sha256']:
            invalid('local chat template differs from pinned configuration')
        if any(actual.get(k)!=v for k,v in model.get('runtime_parameters',{}).items()):
            invalid('local runtime parameters differ from pinned configuration')
    return {"http_status": status, "response_text": text, "returned_model": payload["model"],
            "provider_response_id": payload.get("id"), "finish_status": choice.get("finish_reason"),
            "usage": payload.get("usage"), "provider_raw_meta": {"timings": payload.get("timings")},
            "provider_raw_response": payload}


def run_partition(config, manifest, freeze, annotations, prompts, partition, limit=None, dry_run=False,
                  config_path=CONFIG, manifest_path=MANIFEST):
    selected = cells_for(config, freeze, annotations, prompts, partition)
    if dry_run:
        print(f"{partition}: dry-run only; {len(selected)} frozen prompt instances; no request sent")
        return
    require_frozen(config, manifest, config_path, manifest_path)
    require_execution_gates(config,manifest,config_path,manifest_path)
    model = next(m for m in config["models"] if m["partition"] == partition)
    if partition in EXACT_CLOUD_IDS and not os.environ.get(model["env_key"]):
        raise RuntimeError(f"required API key not set: {model['env_key']}")
    root = output_root(config)
    pins = provenance(config_path, manifest_path)
    revised=config['protocol_id'].endswith('0.3')
    quota=None
    if revised and partition=='google':
        from gemini_quota import QuotaLedger
        quota=QuotaLedger(ROOT/model['quota_config'])
    with partition_lock(root, "local_runtime" if partition.startswith("local_") else partition):
        done, _ = validated_records(root / f"{partition}.jsonl", config, partition, selected, pins)
        validate_attempt_history(root / "attempts" / f"{partition}.jsonl",
                                 config, partition, selected, pins, done)
        prior_attempts={}
        for event in historical.read_jsonl_records(root/'attempts'/f'{partition}.jsonl'):
            if event['status']=='started':
                key=(event['task_id'],event['language'])
                prior_attempts[key]=prior_attempts.get(key,0)+1
        pending = [c for c in selected if (c["task_id"], c["language"]) not in done]
        if limit is not None:
            pending = pending[:limit]
        caller = historical.CALLERS[partition] if partition in EXACT_CLOUD_IDS else local_chat
        if revised and partition=='google':
            from cloud_four_adapters import call_google
            caller=call_google
        # Intentionally sequential. Local models share memory; cloud concurrency
        # can be added after a separate throughput check without changing cells.
        for cell in pending:
            used=prior_attempts.get((cell['task_id'],cell['language']),0)
            if used>=4:
                print(f"{partition} {cell['task_id']} {cell['language']}: four-attempt budget exhausted",flush=True)
                continue
            started = time.monotonic()
            attempts = []
            result = None
            base = {"protocol_id": config["protocol_id"], "snapshot_id": manifest["snapshot_id"],
                    **pins, **cell, "requested_model": model["model_id"],
                    "runner_python_version": platform.python_version(),
                    "system_prompt": config["system_prompt"],
                    "request_parameters": {"model": model, "max_output_tokens": config["max_output_tokens"],
                                           "tools_enabled": False, "external_grounding": False}}
            for attempt in range(used+1, 5):
                attempt_start = historical.utc_now()
                attempt_id = uuid.uuid4().hex
                if quota:
                    from gemini_quota import QuotaDeferred,input_reservation
                    try:quota.reserve(attempt_id,input_reservation(cell['prompt_text'],config['system_prompt']),
                                      config['protocol_id'],cell['prompt_sha256'])
                    except QuotaDeferred as exc:
                        pause={**pins,'task_id':cell['task_id'],'language':cell['language'],
                               'state':'quota_deferred','reason':exc.reason,'retry_at_utc':exc.retry_at_utc,
                               'retry_at_epoch':exc.retry_at,'at_utc':historical.utc_now()}
                        historical.append_jsonl(root/'quota_deferrals.jsonl',pause)
                        if attempts:
                            historical.append_jsonl(root/f'{partition}.jsonl',
                                {**base,'generated_at_utc':historical.utc_now(),'attempts':attempts,
                                 'latency_seconds':time.monotonic()-started,'status':'api_error'})
                        print(f"google {cell['task_id']} {cell['language']}: {exc}",flush=True)
                        return pause
                historical.append_jsonl(root / "attempts" / f"{partition}.jsonl",
                    {**base, "attempt": attempt, "attempt_id": attempt_id,
                     "started_at_utc": attempt_start, "status": "started"})
                try:
                    received = caller(model, cell["prompt_text"], config["system_prompt"],
                                    model.get('timeout_seconds',config["timeout_seconds"]), config["max_output_tokens"])
                    if revised and partition in EXACT_CLOUD_IDS:
                        from cloud_four_adapters import validate_identity
                        validate_identity(model,received)
                    result=received
                    outcome = {"attempt": attempt, "started_at_utc": attempt_start, "status": "success"}
                except historical.ProviderHTTPError as exc:
                    outcome = {"attempt": attempt, "started_at_utc": attempt_start,
                               "status": "http_error", "http_status": exc.status,
                               "provider_error": redact_credentials(exc.payload, config)}
                except (TimeoutError, urllib.error.URLError) as exc:
                    outcome = {"attempt": attempt, "started_at_utc": attempt_start,
                               "status": "transport_error", "error_type": type(exc).__name__}
                except (RuntimeError, ValueError, KeyError, TypeError) as exc:
                    outcome = {"attempt": attempt, "started_at_utc": attempt_start,
                               "status": "runtime_error", "error_type": type(exc).__name__}
                attempts.append(outcome)
                historical.append_jsonl(root / "attempts" / f"{partition}.jsonl",
                    {**base, **outcome, "attempt_id": attempt_id, "finished_at_utc": historical.utc_now(),
                     **({"received_response": result} if result is not None else {})})
                if quota:
                    quota.finish(attempt_id,usage=result.get('usage') if result else None,
                                 error_status=outcome.get('http_status'),error_payload=outcome.get('provider_error'),
                                 backoff_seconds=2**attempt)
                if result is not None:
                    break
                retryable = outcome["status"] == "transport_error" or (
                    outcome["status"] == "http_error" and historical.should_retry(outcome["http_status"]))
                if not retryable or attempt == 4:
                    break
                time.sleep(2 ** attempt)
            row = {**base, "generated_at_utc": historical.utc_now(), "attempts": attempts,
                   "latency_seconds": round(time.monotonic() - started, 6),
                   "status": "success" if result is not None else "api_error", **(result or {})}
            if result is not None:
                row["response_sha256"] = hashlib.sha256(row["response_text"].encode("utf-8")).hexdigest()
                row["truncated"] = historical.is_truncated(row)
            historical.append_jsonl(root / f"{partition}.jsonl", row)
            print(f"{partition} {cell['task_id']} {cell['language']}: {row['status']}", flush=True)


def redact_credentials(payload, config):
    """Provider errors sometimes echo request values; never log a live API key."""
    encoded = json.dumps(payload, ensure_ascii=False)
    for model in config["models"]:
        key = os.environ.get(model.get("env_key", ""))
        if key:
            encoded = encoded.replace(key, "[REDACTED]")
    return json.loads(encoded)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG)
    parser.add_argument("--manifest", type=Path, default=MANIFEST,
                        help="default candidate cannot generate; pass the later approved FREEZE.json explicitly")
    parser.add_argument('--env-file',type=Path,help='Optional explicit local credentials file; values never logged')
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check")
    sub.add_parser("readiness")
    sub.add_parser("plan")
    p = sub.add_parser("run")
    p.add_argument("--provider", choices=PARTITIONS, required=True)
    p.add_argument("--limit", type=int)
    p.add_argument("--dry-run", action="store_true")
    p.add_argument('--wait-for-quota',action='store_true',help='Resume Google across quota windows/days with persistent accounting')
    args = parser.parse_args()
    from research_approvals import load_api_environment
    load_api_environment(args.env_file)
    args.config, args.manifest = args.config.resolve(), args.manifest.resolve()
    config, manifest, freeze, annotations, prompts = verify_candidate(args.config, args.manifest)
    if args.command in {"check", "readiness"}:
        blockers = generation_readiness(config, manifest, args.config, args.manifest)
        print(json.dumps({"historical_integrity": "PASS", "candidate_structure": "PASS",
                          "generation_ready": not blockers, "blockers": blockers}, indent=2))
        return 3 if args.command == "readiness" and blockers else 0
    if args.command == "plan":
        for partition in PARTITIONS:
            cells = cells_for(config, freeze, annotations, prompts, partition)
            done, errors = validated_records(output_root(config) / f"{partition}.jsonl",
                                            config, partition, cells, provenance(args.config, args.manifest))
            validate_attempt_history(output_root(config) / "attempts" / f"{partition}.jsonl",
                                     config, partition, cells, provenance(args.config, args.manifest), done)
            print(f"{partition}: planned={len(cells)} success={len(done)} missing={len(cells)-len(done)} failed_records={errors}")
        print("total planned=1884; candidate plan is not authorization to generate")
        return 0
    if args.limit is not None and args.limit <= 0:
        parser.error("--limit must be positive")
    if args.wait_for_quota and (args.provider!='google' or args.limit is not None or args.dry_run):
        parser.error('--wait-for-quota requires Google, no --limit and no --dry-run')
    while True:
        state=run_partition(config, manifest, freeze, annotations, prompts, args.provider, args.limit, args.dry_run,
                            args.config, args.manifest)
        if not state:return 0
        if not args.wait_for_quota:return 75
        while time.time()<state['retry_at_epoch']:
            print('Google quota continuation waiting until '+state['retry_at_utc'],flush=True)
            time.sleep(max(0,min(60,state['retry_at_epoch']-time.time())))


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError) as exc:
        raise SystemExit(str(exc))
