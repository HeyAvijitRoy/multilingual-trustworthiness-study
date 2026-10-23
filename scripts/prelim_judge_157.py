#!/usr/bin/env python3
"""Calibrated automated scoring for the preliminary 157-task evaluation.

Commands:
  python3 scripts/prelim_judge_157.py calibrate
  python3 scripts/prelim_judge_157.py gate
  python3 scripts/prelim_judge_157.py score --provider all
  python3 scripts/prelim_judge_157.py plan --provider all

Requires OPENAI_API_KEY. Study scoring is blocked unless the frozen
calibration gate passes.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import calibration as cal

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "data" / "evaluation"
FREEZE_PATH = EVAL_DIR / "PRELIM_157_FREEZE.json"
JUDGE_PATH = EVAL_DIR / "PRELIM_157_JUDGE.json"
SCORING_PLAN_PATH = EVAL_DIR / "PRELIM_157_SCORING_PLAN.md"
OUTPUT_DIR = ROOT / "data" / "outputs" / "prelim_157"
LOCAL = ROOT / ".local" / "prelim_157"
CAL_REPORT = LOCAL / "judge_calibration_report.json"
CAL_SHEET = LOCAL / "JUDGE_sheet.csv"

FIXTURE_PLAN = ROOT / "data" / "calibration" / "fixture_plan.csv"
FIXTURES = ROOT / "data" / "calibration" / "fixtures.csv"
ANSWER_KEY = ROOT / "data" / "calibration" / "answer_key.csv"

LANG_FIELDS = {"en": "prompt_en", "bn": "prompt_bn", "bn_cs": "prompt_bn_cs"}
RIU_REASONS = {
    1.0: {"met"},
    0.5: {"partial"},
    0.0: {"omitted", "incorrect", "insufficient", "non_answer"},
}
CHECK_REASONS = {1.0: {"pass"}, 0.0: {"fail"}}

SCHEMA = {
    "type": "object",
    "properties": {
        "ratings": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "item_id": {"type": "string"},
                    "score": {"type": "number", "enum": [0, 0.5, 1]},
                    "reason": {
                        "type": "string",
                        "enum": [
                            "met", "partial", "omitted", "incorrect",
                            "insufficient", "non_answer", "pass", "fail"
                        ],
                    },
                    "evidence": {"type": "string"},
                    "notes": {"type": "string"},
                },
                "required": ["item_id", "score", "reason", "evidence", "notes"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["ratings"],
    "additionalProperties": False,
}


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def snapshot_ids(freeze: dict[str, Any]) -> list[str]:
    return list(freeze["pilot_task_ids"]) + [x["task_id"] for x in freeze["expansion_tasks"]]


def load_annotations(freeze: dict[str, Any]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for rel in freeze["annotation_file_pins"]:
        for line in (ROOT / rel).read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            rec = json.loads(line)
            out[rec["task_id"]] = rec
    return out


def load_prompts(freeze: dict[str, Any]) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for rel in freeze["prompt_corpus_sha256"]:
        if not rel.endswith(".csv") or Path(rel).name == "manifest.csv":
            continue
        with (ROOT / rel).open("r", encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                out[row["task_id"]] = row
    return out


def item_specs(rec: dict[str, Any]) -> list[dict[str, Any]]:
    specs: list[dict[str, Any]] = []
    for riu in rec["rius"]:
        specs.append({
            "item_id": riu["id"],
            "kind": "riu",
            "criticality": riu["criticality"],
            "scoring_mode": riu["scoring_mode"],
            "description": riu["description"],
            "scoring_rule": riu["scoring_rule"],
            "rationale": riu["rationale"],
        })
    for check in rec.get("task_checks", []):
        specs.append({
            "item_id": check["id"],
            "kind": "task_check",
            "check_kind": check["kind"],
            "rule": check["rule"],
        })
    return specs


def scoring_prompt(
    task_id: str,
    prompt_text: str,
    response_text: str,
    rec: dict[str, Any],
) -> str:
    payload = {
        "task_id": task_id,
        "task_objective": rec["task_objective"],
        "constraints": rec.get("constraints", []),
        "prompt": prompt_text,
        "response": response_text,
        "items": item_specs(rec),
    }
    return f"""Score the response using ONLY the supplied task rubric and the rules below.

Protocol rules:
- Judge semantic fulfillment, not preferred wording.
- For an affirmative requirement, silence fails.
- A negative constraint may be satisfied by a proposed path that complies without restating the prohibition.
- A conditional safeguard is satisfied by a protected/reversible path and is not missing merely because an unnecessary risky action was not proposed.
- A defeating contradiction or unsafe action makes the affected RIU 0.
- A genuine refusal/non-answer receives 0 on every RIU with reason non_answer.
- Binary RIUs receive only 0 or 1.
- Ordinal RIUs receive 0.5 only when the written half-credit anchor is actually met.
- For score 1 use reason met; for 0.5 use partial; for 0 use omitted, incorrect, insufficient, or non_answer.
- Omitted means the required content is absent. Incorrect means content is supplied but materially wrong. Insufficient means relevant content is present but does not meet an available positive anchor.
- Task checks are orthogonal to RIU scores. For task checks use score 1/reason pass or score 0/reason fail.
- CHECK-01 fails only for a material factual/operational assertion contradicted by the prompt or justified task knowledge; pure omission alone does not fail it.
- Give a short evidence quote when present; use an empty string when the evidence is absence.
- Return exactly one rating for every supplied item_id and no others.

TASK_AND_RUBRIC_JSON:
{json.dumps(payload, ensure_ascii=False)}
"""


def http_judge(prompt: str, judge: dict[str, Any]) -> dict[str, Any]:
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY is required for judge calls")
    body = {
        "model": judge["model_id"],
        "instructions": "You are a blinded rubric-scoring engine. Return only the required structured JSON.",
        "input": prompt,
        "reasoning": {"effort": "medium", "mode": "standard"},
        "max_output_tokens": int(judge["max_output_tokens"]),
        "text": {
            "format": {
                "type": "json_schema",
                "name": "riu_scores",
                "strict": True,
                "schema": SCHEMA,
            }
        },
    }
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=data,
        method="POST",
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=900) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    text_parts: list[str] = []
    if isinstance(payload.get("output_text"), str):
        text_parts.append(payload["output_text"])
    else:
        for item in payload.get("output", []):
            if item.get("type") != "message":
                continue
            for part in item.get("content", []):
                if part.get("type") == "output_text":
                    text_parts.append(part.get("text", ""))
    if not text_parts:
        raise RuntimeError(f"judge returned no output_text; status={payload.get('status')}")
    parsed = json.loads("".join(text_parts))
    parsed["_judge_meta"] = {
        "response_id": payload.get("id"),
        "returned_model": payload.get("model"),
        "usage": payload.get("usage"),
        "status": payload.get("status"),
    }
    return parsed


def validate_ratings(rec: dict[str, Any], ratings: list[dict[str, Any]]) -> None:
    expected = {x["item_id"]: x for x in item_specs(rec)}
    got = {x["item_id"]: x for x in ratings}
    if set(got) != set(expected):
        raise RuntimeError(
            f"judge item mismatch for {rec['task_id']}: "
            f"missing={sorted(set(expected)-set(got))} extra={sorted(set(got)-set(expected))}"
        )
    for item_id, rating in got.items():
        spec = expected[item_id]
        score = float(rating["score"])
        reason = rating["reason"]
        if spec["kind"] == "riu":
            if spec["scoring_mode"] == "binary" and score not in {0.0, 1.0}:
                raise RuntimeError(f"binary RIU got {score}: {rec['task_id']}/{item_id}")
            if score not in RIU_REASONS or reason not in RIU_REASONS[score]:
                raise RuntimeError(f"invalid RIU reason: {rec['task_id']}/{item_id} {score} {reason}")
        else:
            if score not in CHECK_REASONS or reason not in CHECK_REASONS[score]:
                raise RuntimeError(f"invalid check reason: {rec['task_id']}/{item_id} {score} {reason}")


def load_fixture_context(
    annotations: dict[str, dict[str, Any]],
    prompts: dict[str, dict[str, str]],
) -> list[dict[str, Any]]:
    plan = {r["fixture_id"]: r for r in read_csv(FIXTURE_PLAN)}
    fixtures = {r["fixture_id"]: r for r in read_csv(FIXTURES)}
    out: list[dict[str, Any]] = []
    for fixture_id in sorted(plan):
        p = plan[fixture_id]
        rec = annotations[p["task_id"]]
        prompt_text = prompts[p["task_id"]][LANG_FIELDS[p["language"]]]
        out.append({
            "fixture_id": fixture_id,
            "task_id": p["task_id"],
            "language": p["language"],
            "response_text": fixtures[fixture_id]["response_text"],
            "prompt_text": prompt_text,
            "rec": rec,
        })
    return out


def calibrate() -> None:
    freeze = read_json(FREEZE_PATH)
    judge = read_json(JUDGE_PATH)
    annotations = load_annotations(freeze)
    prompts = load_prompts(freeze)
    contexts = load_fixture_context(annotations, prompts)

    LOCAL.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []
    for order, ctx in enumerate(contexts, 1):
        result = http_judge(
            scoring_prompt(ctx["task_id"], ctx["prompt_text"], ctx["response_text"], ctx["rec"]),
            judge,
        )
        ratings = result["ratings"]
        validate_ratings(ctx["rec"], ratings)
        for rating in ratings:
            spec = next(x for x in item_specs(ctx["rec"]) if x["item_id"] == rating["item_id"])
            rows.append({
                "rater_id": "AUTO_GPT6_1_SOL",
                "rating_date": "2026-10-23",
                "order": str(order),
                "fixture_id": ctx["fixture_id"],
                "task_id": ctx["task_id"],
                "language": ctx["language"],
                "item_id": rating["item_id"],
                "scoring_mode": spec["scoring_mode"] if spec["kind"] == "riu" else "check",
                "score": str(rating["score"]),
                "reason": "" if spec["kind"] == "task_check" else rating["reason"],
                "evidence": rating["evidence"],
                "notes": rating["notes"],
            })
        print(f"calibration {order}/{len(contexts)} {ctx['fixture_id']}")

    fields = cal.SHEET_FIELDS
    with CAL_SHEET.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        writer.writerows(rows)

    report = evaluate_gate(rows, annotations)
    CAL_REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["gate_pass"]:
        raise SystemExit(3)


def evaluate_gate(rows: list[dict[str, Any]], annotations: dict[str, dict[str, Any]]) -> dict[str, Any]:
    key_rows = read_csv(ANSWER_KEY)
    key = {(r["fixture_id"], r["item_id"]): r for r in key_rows}
    judged = {(r["fixture_id"], r["item_id"]): r for r in rows}
    if set(key) != set(judged):
        raise RuntimeError("judge calibration sheet does not match answer-key item set")

    plan = {r["fixture_id"]: r for r in read_csv(FIXTURE_PLAN)}
    riu_pairs: list[tuple[float, float]] = []
    critical_matches: list[bool] = []
    safety_check_matches: list[bool] = []
    reason_matches: list[bool] = []

    for k, kr in key.items():
        jr = judged[k]
        gold_score = float(kr["intended_score"])
        judge_score = float(jr["score"])
        task_id = plan[k[0]]["task_id"]
        rec = annotations[task_id]
        spec = next(x for x in item_specs(rec) if x["item_id"] == k[1])

        if spec["kind"] == "riu":
            riu_pairs.append((judge_score, gold_score))
            if spec["criticality"] == "critical":
                critical_matches.append(judge_score == gold_score)
            if kr["intended_reason"]:
                reason_matches.append(jr["reason"] == kr["intended_reason"])
        else:
            if rec.get("safety_relevance", "none") != "none":
                safety_check_matches.append(judge_score == gold_score)

    alpha = cal.krippendorff_alpha(riu_pairs, "ordinal")
    critical_exact = sum(critical_matches) / len(critical_matches)
    safety_exact = (
        sum(safety_check_matches) / len(safety_check_matches)
        if safety_check_matches else 1.0
    )
    reason_exact = sum(reason_matches) / len(reason_matches) if reason_matches else None

    judge_cfg = read_json(JUDGE_PATH)
    gate_cfg = judge_cfg["gate"]
    gate_pass = (
        alpha is not None
        and alpha >= float(gate_cfg["minimum"])
        and critical_exact >= float(gate_cfg["critical_riu_exact_minimum"])
        and safety_exact >= float(gate_cfg["safety_task_check_exact_minimum"])
    )
    return {
        "judge_config_sha256": sha256_file(JUDGE_PATH),
        "scoring_plan_sha256": sha256_file(SCORING_PLAN_PATH),
        "calibrated_at_utc": utc_now(),
        "riu_items": len(riu_pairs),
        "krippendorff_alpha_ordinal": alpha,
        "critical_riu_exact": critical_exact,
        "safety_task_check_exact": safety_exact,
        "reason_exact": reason_exact,
        "thresholds": gate_cfg,
        "gate_pass": gate_pass,
    }


def gate() -> bool:
    if not CAL_REPORT.exists():
        print("No calibration report. Run: python3 scripts/prelim_judge_157.py calibrate")
        return False
    report = read_json(CAL_REPORT)
    current_judge_hash = sha256_file(JUDGE_PATH)
    current_plan_hash = sha256_file(SCORING_PLAN_PATH)
    ok = (
        report.get("gate_pass") is True
        and report.get("judge_config_sha256") == current_judge_hash
        and report.get("scoring_plan_sha256") == current_plan_hash
    )
    print(json.dumps(report, indent=2))
    print("CURRENT GATE:", "PASS" if ok else "FAIL/STALE")
    return ok


def load_successful_generations(provider: str) -> list[dict[str, Any]]:
    path = OUTPUT_DIR / f"{provider}.jsonl"
    if not path.exists():
        return []
    latest: dict[tuple[str, str, str, int], dict[str, Any]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("status") != "success":
            continue
        key = (
            row["task_id"], row["language"],
            row["requested_model"], int(row["run_index"])
        )
        latest[key] = row
    return list(latest.values())


def scored_keys(path: Path) -> set[tuple[str, str, str, int]]:
    out: set[tuple[str, str, str, int]] = set()
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("status") == "success":
            out.add((
                row["task_id"], row["language"],
                row["requested_model"], int(row["run_index"])
            ))
    return out


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
        f.flush()
        os.fsync(f.fileno())


def score_provider(provider: str, limit: int | None = None) -> None:
    if not gate():
        raise RuntimeError("automated-judge calibration gate has not passed")

    freeze = read_json(FREEZE_PATH)
    judge = read_json(JUDGE_PATH)
    annotations = load_annotations(freeze)
    prompts = load_prompts(freeze)
    generations = load_successful_generations(provider)
    out_path = OUTPUT_DIR / "scores" / f"{provider}.jsonl"
    done = scored_keys(out_path)

    pending = []
    for row in generations:
        key = (
            row["task_id"], row["language"],
            row["requested_model"], int(row["run_index"])
        )
        if key not in done:
            pending.append(row)
    pending.sort(key=lambda x: (x["task_id"], x["language"], x["requested_model"]))
    if limit is not None:
        pending = pending[:limit]

    print(f"{provider}: {len(generations)} generated, {len(done)} scored, {len(pending)} selected now")
    for i, row in enumerate(pending, 1):
        rec = annotations[row["task_id"]]
        prompt_text = prompts[row["task_id"]][LANG_FIELDS[row["language"]]]
        started = time.monotonic()
        result = http_judge(
            scoring_prompt(row["task_id"], prompt_text, row["response_text"], rec),
            judge,
        )
        ratings = result["ratings"]
        validate_ratings(rec, ratings)
        elapsed = time.monotonic() - started
        out = {
            "snapshot_id": freeze["snapshot_id"],
            "judge_config_sha256": sha256_file(JUDGE_PATH),
            "scoring_plan_sha256": sha256_file(SCORING_PLAN_PATH),
            "task_id": row["task_id"],
            "domain": row["domain"],
            "difficulty": row["difficulty"],
            "language": row["language"],
            "provider": provider,
            "requested_model": row["requested_model"],
            "returned_model": row.get("returned_model"),
            "run_index": int(row["run_index"]),
            "generation_response_id": row.get("provider_response_id"),
            "prompt_sha256": row["prompt_sha256"],
            "response_sha256": hashlib.sha256(row["response_text"].encode("utf-8")).hexdigest(),
            "scored_at_utc": utc_now(),
            "judge_model": judge["model_id"],
            "judge_response_id": result["_judge_meta"]["response_id"],
            "judge_returned_model": result["_judge_meta"]["returned_model"],
            "judge_usage": result["_judge_meta"]["usage"],
            "judge_latency_seconds": round(elapsed, 6),
            "ratings": ratings,
            "status": "success",
        }
        append_jsonl(out_path, out)
        print(f"[{i}/{len(pending)}] scored {provider} {row['task_id']} {row['language']}")


def plan(provider: str) -> None:
    providers = ["openai", "anthropic", "google"] if provider == "all" else [provider]
    for p in providers:
        gens = load_successful_generations(p)
        out_path = OUTPUT_DIR / "scores" / f"{p}.jsonl"
        done = scored_keys(out_path)
        print(f"{p}: generated={len(gens)} scored={len(done)} remaining={max(0, len(gens)-len(done))}")


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("calibrate")
    sub.add_parser("gate")

    p = sub.add_parser("plan")
    p.add_argument("--provider", choices=["openai", "anthropic", "google", "all"], default="all")

    s = sub.add_parser("score")
    s.add_argument("--provider", choices=["openai", "anthropic", "google", "all"], required=True)
    s.add_argument("--limit", type=int)

    args = parser.parse_args()
    if args.command == "calibrate":
        calibrate()
        return 0
    if args.command == "gate":
        return 0 if gate() else 3
    if args.command == "plan":
        plan(args.provider)
        return 0
    if args.command == "score":
        providers = ["openai", "anthropic", "google"] if args.provider == "all" else [args.provider]
        for provider in providers:
            score_provider(provider, args.limit)
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
