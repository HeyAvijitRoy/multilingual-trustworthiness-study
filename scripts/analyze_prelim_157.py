#!/usr/bin/env python3
"""Aggregate preliminary 157-task scores under the frozen analysis plan.

Usage:
  python3 scripts/analyze_prelim_157.py
  python3 scripts/analyze_prelim_157.py --allow-missing

Writes:
  data/outputs/prelim_157/analysis/prelim_157_results.json
  data/outputs/prelim_157/analysis/prelim_157_summary.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "data" / "evaluation"
FREEZE_PATH = EVAL_DIR / "PRELIM_157_FREEZE.json"
ANALYSIS_PLAN_PATH = EVAL_DIR / "PRELIM_157_ANALYSIS_PLAN.md"
OUTPUT_DIR = ROOT / "data" / "outputs" / "prelim_157"
SCORES_DIR = OUTPUT_DIR / "scores"
ANALYSIS_DIR = OUTPUT_DIR / "analysis"
PROVIDERS = ["openai", "anthropic", "google"]
LANGS = ["en", "bn", "bn_cs"]
BOOTSTRAP_N = 10_000
BOOTSTRAP_SEED = 20261023


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot_ids(freeze: dict[str, Any]) -> list[str]:
    return list(freeze["pilot_task_ids"]) + [x["task_id"] for x in freeze["expansion_tasks"]]


def load_annotations(freeze: dict[str, Any]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for rel in freeze["annotation_file_pins"]:
        for line in (ROOT / rel).read_text(encoding="utf-8").splitlines():
            if line.strip():
                rec = json.loads(line)
                out[rec["task_id"]] = rec
    return out


def load_latest_scores() -> dict[tuple[str, str, str, int], dict[str, Any]]:
    latest: dict[tuple[str, str, str, int], dict[str, Any]] = {}
    for provider in PROVIDERS:
        path = SCORES_DIR / f"{provider}.jsonl"
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("status") != "success":
                continue
            key = (
                row["requested_model"],
                row["task_id"],
                row["language"],
                int(row["run_index"]),
            )
            latest[key] = row
    return latest


def item_lookup(rec: dict[str, Any]) -> dict[str, dict[str, Any]]:
    out = {}
    for riu in rec["rius"]:
        out[riu["id"]] = {"kind": "riu", **riu}
    for check in rec.get("task_checks", []):
        out[check["id"]] = {
            "kind": "check",
            "check_kind": check["kind"],
            "id": check["id"],
            "rule": check["rule"],
        }
    return out


def response_metrics(rec: dict[str, Any], score_row: dict[str, Any]) -> dict[str, Any]:
    specs = item_lookup(rec)
    ratings = {r["item_id"]: r for r in score_row["ratings"]}
    if set(ratings) != set(specs):
        raise RuntimeError(f"score item mismatch for {rec['task_id']}")

    riu_ratings = [(specs[i], ratings[i]) for i in specs if specs[i]["kind"] == "riu"]
    crit = [(s, r) for s, r in riu_ratings if s["criticality"] == "critical"]
    checks = [(specs[i], ratings[i]) for i in specs if specs[i]["kind"] == "check"]

    scores = [float(r["score"]) for _, r in riu_ratings]
    crit_scores = [float(r["score"]) for _, r in crit]
    crit_reasons = [r["reason"] for _, r in crit]

    all_checks_pass = all(float(r["score"]) == 1.0 for _, r in checks)
    unsupported_pass = all(
        float(r["score"]) == 1.0
        for s, r in checks
        if s.get("check_kind") == "unsupported_content"
    )
    format_pass = all(
        float(r["score"]) == 1.0
        for s, r in checks
        if s.get("check_kind") == "format"
    )

    non_answer = bool(scores) and all(r["reason"] == "non_answer" for _, r in riu_ratings)
    incorrect_count = sum(r["reason"] == "incorrect" for _, r in riu_ratings)

    out = {
        "riu_coverage": sum(scores) / len(scores),
        "strict_riu_coverage": sum(x == 1.0 for x in scores) / len(scores),
        "strict_complete_task_success": float(all(x == 1.0 for x in scores) and all_checks_pass),
        "unsupported_content_pass": float(unsupported_pass),
        "format_adherence": float(format_pass),
        "non_answer": float(non_answer),
        "incorrect_riu_count": incorrect_count,
        "critical_coverage": None,
        "critical_omission_rate": None,
        "critical_unmet_rate": None,
        "critical_zero_rate": None,
        "core_task_success": None,
        "critical_count": len(crit),
    }
    if crit:
        out.update({
            "critical_coverage": sum(crit_scores) / len(crit_scores),
            "critical_omission_rate": sum(
                reason in {"omitted", "non_answer"} for reason in crit_reasons
            ) / len(crit_reasons),
            "critical_unmet_rate": sum(x < 1.0 for x in crit_scores) / len(crit_scores),
            "critical_zero_rate": sum(x == 0.0 for x in crit_scores) / len(crit_scores),
            "core_task_success": float(all(x == 1.0 for x in crit_scores) and all_checks_pass),
        })
    return out


def percentile(values: list[float], q: float) -> float:
    if not values:
        return float("nan")
    xs = sorted(values)
    pos = (len(xs) - 1) * q
    lo = math.floor(pos)
    hi = math.ceil(pos)
    if lo == hi:
        return xs[lo]
    frac = pos - lo
    return xs[lo] * (1 - frac) + xs[hi] * frac


def effect(
    rows: dict[tuple[str, str, str], dict[str, Any]],
    task_domain: dict[str, str],
    models: list[str],
    metric: str,
    lang_a: str,
    lang_b: str,
    sampled: dict[str, list[str]] | None = None,
) -> tuple[float | None, dict[str, float | None]]:
    domains = sorted(set(task_domain.values()))
    by_model: dict[str, float | None] = {}
    for model in models:
        domain_effects: list[float] = []
        for domain in domains:
            task_ids = sampled[domain] if sampled is not None else [
                t for t, d in task_domain.items() if d == domain
            ]
            diffs: list[float] = []
            for task_id in task_ids:
                a = rows.get((model, task_id, lang_a))
                b = rows.get((model, task_id, lang_b))
                if not a or not b:
                    continue
                va = a.get(metric)
                vb = b.get(metric)
                if va is None or vb is None:
                    continue
                diffs.append(float(va) - float(vb))
            if diffs:
                domain_effects.append(sum(diffs) / len(diffs))
        by_model[model] = (
            sum(domain_effects) / len(domain_effects)
            if len(domain_effects) == len(domains) else None
        )
    vals = [x for x in by_model.values() if x is not None]
    pooled = sum(vals) / len(vals) if len(vals) == len(models) else None
    return pooled, by_model


def bootstrap_ci(
    rows: dict[tuple[str, str, str], dict[str, Any]],
    task_domain: dict[str, str],
    models: list[str],
    metric: str,
    lang_a: str,
    lang_b: str,
) -> dict[str, Any]:
    point, by_model = effect(rows, task_domain, models, metric, lang_a, lang_b)
    if point is None:
        return {"estimate": None, "ci95": [None, None], "by_model": by_model}

    tasks_by_domain: dict[str, list[str]] = defaultdict(list)
    for task_id, domain in task_domain.items():
        tasks_by_domain[domain].append(task_id)
    rng = random.Random(BOOTSTRAP_SEED)
    reps: list[float] = []
    for _ in range(BOOTSTRAP_N):
        sampled = {
            domain: [rng.choice(ids) for _ in range(len(ids))]
            for domain, ids in tasks_by_domain.items()
        }
        val, _ = effect(rows, task_domain, models, metric, lang_a, lang_b, sampled)
        if val is not None:
            reps.append(val)
    return {
        "estimate": point,
        "ci95": [percentile(reps, 0.025), percentile(reps, 0.975)],
        "bootstrap_replicates": len(reps),
        "by_model": by_model,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-missing", action="store_true")
    args = parser.parse_args()

    freeze = read_json(FREEZE_PATH)
    annotations = load_annotations(freeze)
    score_rows = load_latest_scores()
    ids = snapshot_ids(freeze)
    models = sorted({k[0] for k in score_rows})
    expected = 157 * 3 * 3

    task_metrics: dict[tuple[str, str, str], dict[str, Any]] = {}
    for (model, task_id, language, run_index), row in score_rows.items():
        if run_index != 1 or task_id not in annotations or language not in LANGS:
            continue
        task_metrics[(model, task_id, language)] = response_metrics(annotations[task_id], row)

    observed = len(task_metrics)
    if not args.allow_missing and observed != expected:
        raise RuntimeError(
            f"expected {expected} scored response cells, found {observed}; "
            "use --allow-missing only for explicitly reported API missingness"
        )
    if not models:
        raise RuntimeError("no scored model responses found")

    task_domain = {task_id: annotations[task_id]["domain"] for task_id in ids}

    specs = [
        ("critical_omission_rate", "bn", "en"),
        ("critical_coverage", "bn", "en"),
        ("riu_coverage", "bn", "en"),
        ("strict_complete_task_success", "bn", "en"),
        ("critical_omission_rate", "bn_cs", "bn"),
        ("critical_coverage", "bn_cs", "bn"),
        ("riu_coverage", "bn_cs", "bn"),
        ("critical_omission_rate", "bn_cs", "en"),
        ("critical_coverage", "bn_cs", "en"),
    ]

    effects: dict[str, Any] = {}
    for metric, a, b in specs:
        key = f"{metric}:{a}-{b}"
        effects[key] = bootstrap_ci(task_metrics, task_domain, models, metric, a, b)

    counts_by_model_language: dict[str, int] = defaultdict(int)
    for model, task_id, language in task_metrics:
        counts_by_model_language[f"{model}:{language}"] += 1

    report = {
        "snapshot_id": freeze["snapshot_id"],
        "snapshot_sha256": sha256_file(FREEZE_PATH),
        "analysis_plan_sha256": sha256_file(ANALYSIS_PLAN_PATH),
        "task_count": 157,
        "models": models,
        "scored_cells": observed,
        "expected_cells": expected,
        "missing_cells": expected - observed,
        "counts_by_model_language": dict(sorted(counts_by_model_language.items())),
        "bootstrap": {
            "replicates": BOOTSTRAP_N,
            "seed": BOOTSTRAP_SEED,
            "cluster": "task_id",
            "stratification": "domain",
            "domain_equal_weighting": True,
            "model_equal_weighting": True,
        },
        "primary_estimand": "critical_omission_rate:bn-en",
        "effects": effects,
    }

    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)
    json_path = ANALYSIS_DIR / "prelim_157_results.json"
    md_path = ANALYSIS_DIR / "prelim_157_summary.md"
    json_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    def fmt(x: float | None) -> str:
        return "NA" if x is None else f"{x:.4f}"

    lines = [
        "# Preliminary 157-task evaluation results",
        "",
        f"- Snapshot: `{freeze['snapshot_id']}`",
        f"- Scored cells: {observed} / {expected}",
        f"- Models: {', '.join(models)}",
        "- Weighting: task means within domain, five domains equally weighted; pooled panel gives models equal weight.",
        f"- Bootstrap: {BOOTSTRAP_N:,} task-clustered, domain-stratified replicates; seed {BOOTSTRAP_SEED}.",
        "",
        "## Frozen primary estimand",
        "",
    ]
    primary = effects["critical_omission_rate:bn-en"]
    lines += [
        "**Critical Omission Rate, BN - EN**",
        "",
        f"- Pooled effect: {fmt(primary['estimate'])}",
        f"- 95% bootstrap CI: [{fmt(primary['ci95'][0])}, {fmt(primary['ci95'][1])}]",
        f"- Model-specific effects: " + ", ".join(
            f"{m}={fmt(v)}" for m, v in primary["by_model"].items()
        ),
        "",
        "Positive values mean more literal critical omissions in Bengali.",
        "",
        "## Key secondary effects",
        "",
        "| Effect | Estimate | 95% CI |",
        "|---|---:|---:|",
    ]
    for key in [
        "critical_coverage:bn-en",
        "riu_coverage:bn-en",
        "strict_complete_task_success:bn-en",
        "critical_omission_rate:bn_cs-bn",
        "critical_coverage:bn_cs-bn",
        "riu_coverage:bn_cs-bn",
        "critical_omission_rate:bn_cs-en",
        "critical_coverage:bn_cs-en",
    ]:
        e = effects[key]
        lines.append(
            f"| {key} | {fmt(e['estimate'])} | [{fmt(e['ci95'][0])}, {fmt(e['ci95'][1])}] |"
        )
    lines += [
        "",
        "These are preliminary 157-task results and do not replace the planned final 500-task evaluation.",
    ]
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(md_path.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
