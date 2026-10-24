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

import prelim_eval_157 as generation
import prelim_judge_157 as judge

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "data" / "evaluation"
FREEZE_PATH = EVAL_DIR / "PRELIM_157_FREEZE.json"
MODEL_PATH = EVAL_DIR / "PRELIM_157_MODELS.json"
ANALYSIS_PLAN_PATH = EVAL_DIR / "PRELIM_157_ANALYSIS_PLAN.md"
OUTPUT_DIR = ROOT / "data" / "outputs" / "prelim_157"
SCORES_DIR = OUTPUT_DIR / "scores"
ANALYSIS_DIR = OUTPUT_DIR / "analysis"
PROVIDERS = ["openai", "anthropic", "google"]
LANGS = ["en", "bn", "bn_cs"]
BOOTSTRAP_N = 10_000
BOOTSTRAP_SEED = 20261023
# Every contrast for the four explicitly named key outcomes, plus the strict
# ordinal-coverage and unmet/zero diagnostics required by scoring protocol 0.3.
EFFECT_SPECS = [
    (metric, a, b)
    for metric in (
        "critical_omission_rate", "critical_coverage", "riu_coverage",
        "strict_complete_task_success", "strict_riu_coverage",
        "critical_unmet_rate", "critical_zero_rate", "core_task_success",
    )
    for a, b in (("bn", "en"), ("bn_cs", "bn"), ("bn_cs", "en"))
]


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
        for row in generation.read_jsonl_records(path):
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
    judge.validate_ratings(rec, score_row["ratings"])
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
        "format_adherence": float(format_pass) if any(s.get("check_kind") == "format" for s, _ in checks) else None,
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
                t for t, d in sorted(task_domain.items()) if d == domain
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
            if domains and len(domain_effects) == len(domains) else None
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
    tasks_by_domain: dict[str, list[str]] = defaultdict(list)
    for task_id, domain in sorted(task_domain.items()):
        tasks_by_domain[domain].append(task_id)
    rng = random.Random(BOOTSTRAP_SEED)
    reps: list[float] = []
    model_reps: dict[str, list[float]] = {m: [] for m in models}
    for _ in range(BOOTSTRAP_N):
        sampled = {
            domain: [rng.choice(ids) for _ in range(len(ids))]
            for domain, ids in sorted(tasks_by_domain.items())
        }
        val, model_vals = effect(rows, task_domain, models, metric, lang_a, lang_b, sampled)
        for model, value in model_vals.items():
            if value is not None:
                model_reps[model].append(value)
        if val is not None:
            reps.append(val)
    return {
        "paired_counts": paired_counts(rows, task_domain, models, metric, lang_a, lang_b),
        "estimate": point,
        "ci95": [percentile(reps, 0.025), percentile(reps, 0.975)] if reps else [None, None],
        "by_model_ci95": {m: [percentile(v, 0.025), percentile(v, 0.975)] if v else [None, None] for m, v in model_reps.items()},
        "by_model_bootstrap_replicates": {m: len(v) for m, v in model_reps.items()},
        "bootstrap_replicates": len(reps),
        "by_model": by_model,
    }


def paired_counts(
    rows: dict[tuple[str, str, str], dict[str, Any]],
    task_domain: dict[str, str],
    models: list[str],
    metric: str,
    lang_a: str,
    lang_b: str,
) -> dict[str, Any]:
    """Count actual matched tasks, keeping missing cells and undefined metrics separate."""
    counts: dict[str, Any] = {}
    for model in models:
        per_domain = {domain: {"paired_tasks": 0, "missing_cell_tasks": 0, "undefined_metric_tasks": 0}
                      for domain in sorted(set(task_domain.values()))}
        for task_id, domain in sorted(task_domain.items()):
            a, b = rows.get((model, task_id, lang_a)), rows.get((model, task_id, lang_b))
            if a is None or b is None:
                per_domain[domain]["missing_cell_tasks"] += 1
            elif a.get(metric) is None or b.get(metric) is None:
                per_domain[domain]["undefined_metric_tasks"] += 1
            else:
                per_domain[domain]["paired_tasks"] += 1
        counts[model] = {
            "paired_tasks": sum(d["paired_tasks"] for d in per_domain.values()),
            "missing_cell_tasks": sum(d["missing_cell_tasks"] for d in per_domain.values()),
            "undefined_metric_tasks": sum(d["undefined_metric_tasks"] for d in per_domain.values()),
            "by_domain": per_domain,
        }
    return counts


def effect_table(
    rows: dict[tuple[str, str, str], dict[str, Any]],
    task_domain: dict[str, str],
    models: list[str],
) -> dict[str, Any]:
    return {f"{metric}:{a}-{b}": bootstrap_ci(rows, task_domain, models, metric, a, b)
            for metric, a, b in EFFECT_SPECS}


def reporting_tables(
    rows: dict[tuple[str, str, str], dict[str, Any]],
    annotations: dict[str, dict[str, Any]],
    models: list[str],
    truncated_cells: set[tuple[str, str, str]],
) -> dict[str, Any]:
    """Apply frozen estimators to prespecified strata; never select by results."""
    task_domain = {task: rec["domain"] for task, rec in sorted(annotations.items())}
    by_domain = {
        domain: effect_table(rows, {t: d for t, d in task_domain.items() if d == domain}, models)
        for domain in sorted(set(task_domain.values()))
    }
    by_difficulty = {
        difficulty: effect_table(rows, {t: d for t, d in task_domain.items()
                                       if annotations[t]["difficulty"] == difficulty}, models)
        for difficulty in ("easy", "medium", "hard")
        if any(rec["difficulty"] == difficulty for rec in annotations.values())
    }
    extended = {t: d for t, d in task_domain.items()
                if t.startswith("SYN") and t[3:].isdigit() and 91 <= int(t[3:]) <= 100}
    ordinary = {t: d for t, d in task_domain.items() if t not in extended}
    without_truncation = {key: value for key, value in rows.items() if key not in truncated_cells}
    complete_tasks = {task for task in task_domain
                      if all((model, task, language) in rows for model in models for language in LANGS)}
    complete_panel_rows = {key: value for key, value in rows.items() if key[1] in complete_tasks}
    return {
        "by_domain": by_domain,
        "by_difficulty": by_difficulty,
        "extended_context_sensitivity": {
            "extended_task_ids": sorted(extended),
            "extended_only": effect_table(rows, extended, models) if extended else {},
            "excluding_extended": effect_table(rows, ordinary, models) if ordinary else {},
            "interpretation": "Extended-only estimates cover the represented synthesis tasks; ordinary-task estimates retain equal weighting of represented domains.",
        },
        "missingness_sensitivity": {
            "policy": "Restrict to tasks with all three scored languages for every frozen model; preserve the original task/domain bootstrap universe and require all domains. No imputation or model substitution.",
            "complete_panel_task_ids": sorted(complete_tasks),
            "complete_panel_task_count": len(complete_tasks),
            "effects_complete_panel_tasks": effect_table(complete_panel_rows, task_domain, models),
        },
        "truncation_sensitivity": {
            "policy": "Primary estimates retain truncated successful responses. Sensitivity excludes a language pair if either response was truncated; no cell is imputed.",
            "truncated_scored_cells": len(set(rows) & truncated_cells),
            "effects_excluding_truncated": effect_table(without_truncation, task_domain, models),
        },
    }


def generation_status(
    freeze: dict[str, Any],
    model_cfg: dict[str, Any],
    score_rows: dict[tuple[str, str, str, int], dict[str, Any]],
    output_dir: Path | None = None,
) -> tuple[dict[str, Any], set[tuple[str, str, str]]]:
    """Describe missingness from raw evidence, not from missing scores alone."""
    ids = sorted(snapshot_ids(freeze))
    missing: list[dict[str, Any]] = []
    by_model_language: dict[str, Any] = {}
    truncated_cells: set[tuple[str, str, str]] = set()
    dates: list[str] = []
    for config in model_cfg["models"]:
        model, provider = config["model_id"], config["provider"]
        attempts: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
        for row in generation.read_jsonl_records((output_dir or OUTPUT_DIR) / f"{provider}.jsonl"):
            if (row.get("requested_model") == model and row.get("task_id") in ids
                    and row.get("language") in LANGS and int(row.get("run_index", 0)) == 1
                    and row.get("snapshot_id") == freeze["snapshot_id"]):
                attempts[(row["task_id"], row["language"])].append(row)
        for language in LANGS:
            counters = {"expected_cells": len(ids), "successful_generations": 0, "scored_cells": 0,
                        "unresolved_api_failure_cells": 0, "unattempted_cells": 0,
                        "generated_unscored_cells": 0, "other_unresolved_cells": 0,
                        "api_error_records": 0, "truncated_successful_cells": 0}
            for task in ids:
                history = attempts.get((task, language), [])
                successes = [r for r in history if r.get("status") == "success"]
                counters["api_error_records"] += sum(r.get("status") == "api_error" for r in history)
                scored = (model, task, language, 1) in score_rows
                counters["scored_cells"] += scored
                if successes:
                    source = successes[-1]
                    counters["successful_generations"] += 1
                    if source.get("generated_at_utc"):
                        dates.append(source["generated_at_utc"])
                    if generation.is_truncated(source):
                        counters["truncated_successful_cells"] += 1
                        truncated_cells.add((model, task, language))
                    reason = "generated_unscored" if not scored else None
                elif not history:
                    reason = "unattempted"
                elif any(r.get("status") == "api_error" for r in history):
                    reason = "unresolved_api_failure"
                else:
                    reason = "other_unresolved"
                if reason:
                    counters[f"{reason}_cells"] += 1
                    missing.append({"model": model, "provider": provider, "task_id": task,
                                    "language": language, "reason": reason})
            generated = counters["successful_generations"]
            counters["unresolved_api_failure_rate"] = counters["unresolved_api_failure_cells"] / len(ids) if ids else None
            counters["truncation_rate_among_successes"] = counters["truncated_successful_cells"] / generated if generated else None
            by_model_language[f"{model}:{language}"] = counters
    return {
        "by_model_language": dict(sorted(by_model_language.items())),
        "missing_cell_details": sorted(missing, key=lambda r: (r["model"], r["task_id"], r["language"])),
        "generation_date_range_utc": [min(dates), max(dates)] if dates else [None, None],
        "definitions": "API failure is transport/provider missingness; valid refusals/nonanswers remain successful model outcomes. Error records preceding a successful retry are not unresolved failure cells.",
    }, truncated_cells


def outcome_summary(
    rows: dict[tuple[str, str, str], dict[str, Any]], models: list[str]
) -> dict[str, Any]:
    """Separate response outcomes and denominators from paired language effects."""
    out: dict[str, Any] = {}
    for model in models:
        for language in LANGS:
            cells = [r for (m, _, lang), r in sorted(rows.items()) if m == model and lang == language]
            stats = {}
            for metric in ("riu_coverage", "strict_riu_coverage", "critical_coverage", "critical_omission_rate",
                           "critical_unmet_rate", "critical_zero_rate", "strict_complete_task_success",
                           "core_task_success", "unsupported_content_pass", "format_adherence", "non_answer"):
                values = [r[metric] for r in cells if r.get(metric) is not None]
                stats[metric] = {"mean": sum(values) / len(values) if values else None,
                                 "defined_cells": len(values)}
            stats["incorrect_riu_count"] = sum(r["incorrect_riu_count"] for r in cells)
            out[f"{model}:{language}"] = stats
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-missing", action="store_true")
    args = parser.parse_args()

    freeze, model_cfg, annotations, _ = generation.verify_freeze()
    score_rows = load_latest_scores()
    ids = snapshot_ids(freeze)
    models = sorted(m["model_id"] for m in model_cfg["models"])
    expected = len(ids) * len(LANGS) * len(models)
    task_metrics: dict[tuple[str, str, str], dict[str, Any]] = {}
    for (model, task_id, language, run_index), row in score_rows.items():
        if run_index != 1 or task_id not in ids or language not in LANGS or model not in models:
            raise RuntimeError(f"score outside historical frozen panel: {(model, task_id, language, run_index)}")
        if row.get("snapshot_id") != freeze["snapshot_id"]:
            raise RuntimeError(f"score snapshot mismatch: {model}/{task_id}/{language}")
        if row.get("prompt_sha256") != annotations[task_id]["prompt_sha256"][language]:
            raise RuntimeError(f"score prompt hash mismatch: {model}/{task_id}/{language}")
        task_metrics[(model, task_id, language)] = response_metrics(annotations[task_id], row)
    observed = len(task_metrics)
    if not args.allow_missing and observed != expected:
        raise RuntimeError(f"expected {expected} scored response cells, found {observed}; use --allow-missing only for explicitly reported API missingness")
    if not task_metrics:
        raise RuntimeError("no scored model responses found")
    if not judge.gate():
        raise RuntimeError("analysis requires a current passing automated-judge calibration gate")
    for provider in PROVIDERS:
        path = OUTPUT_DIR / f"{provider}.jsonl"
        generation.validate_generation_records(path, freeze, model_cfg, annotations, provider)
        judge.validate_score_records(SCORES_DIR / f"{provider}.jsonl", judge.load_successful_generations(provider))

    status, truncated = generation_status(freeze, model_cfg, score_rows)
    if args.allow_missing:
        unexplained = [r for r in status["missing_cell_details"] if r["reason"] != "unresolved_api_failure"]
        if unexplained:
            raise RuntimeError(f"--allow-missing permits unresolved API failures only; found {len(unexplained)} unattempted, unscored or otherwise unresolved cells")
    task_domain = {task: annotations[task]["domain"] for task in ids}
    effects = effect_table(task_metrics, task_domain, models)
    report = {
        "snapshot_id": freeze["snapshot_id"],
        "snapshot_sha256": sha256_file(FREEZE_PATH),
        "analysis_plan_sha256": sha256_file(ANALYSIS_PLAN_PATH),
        "model_config_sha256": sha256_file(MODEL_PATH),
        "analysis_script_sha256": sha256_file(Path(__file__)),
        "source_output_files_sha256": {
            path.relative_to(OUTPUT_DIR).as_posix(): sha256_file(path)
            for provider in PROVIDERS
            for path in (OUTPUT_DIR / f"{provider}.jsonl", SCORES_DIR / f"{provider}.jsonl")
            if path.exists()
        },
        "generated_at_utc": generation.utc_now(),
        "task_count": len(ids),
        "score_status": "provisional_automated_unreviewed",
        "limitations": ["Human scoring QA and adjudication must be resolved before reporting final preliminary aggregates.",
                        "Secondary intervals are effect-estimation summaries, not additional primary significance tests.",
                        "Bootstrap draws with an undefined domain/model estimate are excluded and their valid replicate counts are reported; sparse strata may have undefined intervals."],
        "models": models,
        "scored_cells": observed,
        "expected_cells": expected,
        "missing_cells": expected - observed,
        "counts_by_model_language": {f"{model}:{lang}": sum(m == model and l == lang for m, _, l in task_metrics)
                                     for model in models for lang in LANGS},
        "generation_status": status,
        "outcome_summary": outcome_summary(task_metrics, models),
        "outcome_summary_weighting": "Descriptive unweighted response means with defined-cell denominators; language effects use the prespecified domain-equal estimator.",
        "bootstrap": {"replicates": BOOTSTRAP_N, "seed": BOOTSTRAP_SEED, "cluster": "task_id",
                      "stratification": "domain", "domain_equal_weighting": True, "model_equal_weighting": True},
        "primary_estimand": "critical_omission_rate:bn-en",
        "effects": effects,
        **reporting_tables(task_metrics, annotations, models, truncated),
    }
    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)
    json_path = ANALYSIS_DIR / "prelim_157_results.json"
    md_path = ANALYSIS_DIR / "prelim_157_summary.md"
    json_path.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    md_path.write_text(render_summary(report), encoding="utf-8")
    print(md_path.read_text(encoding="utf-8"))
    return 0


def render_summary(report: dict[str, Any]) -> str:
    """Include estimates, model uncertainty and paired denominators in exportable tables."""
    def fmt(value: float | None) -> str:
        return "NA" if value is None else f"{value:.4f}"

    def effect_lines(table: dict[str, Any]) -> list[str]:
        lines = ["| Effect | Model/panel | Paired tasks | Estimate | 95% CI | Valid bootstrap draws |",
                 "|---|---|---:|---:|---:|---:|"]
        for name, result in table.items():
            lines.append(f"| {name} | Pooled panel | See model rows | {fmt(result['estimate'])} | [{fmt(result['ci95'][0])}, {fmt(result['ci95'][1])}] | {result['bootstrap_replicates']} |")
            for model, estimate in result["by_model"].items():
                interval = result["by_model_ci95"][model]
                lines.append(f"| {name} | {model} | {result['paired_counts'][model]['paired_tasks']} | {fmt(estimate)} | [{fmt(interval[0])}, {fmt(interval[1])}] | {result['by_model_bootstrap_replicates'][model]} |")
        return lines

    lines = ["# Preliminary 157-task evaluation results", "",
             f"- Snapshot: `{report['snapshot_id']}`",
             f"- Scored cells: {report['scored_cells']} / {report['expected_cells']}",
             f"- Models: {', '.join(report['models'])}",
             "- Status: provisional automated scores; human scoring QA/adjudication is unresolved.",
             "- Weighting: task means within domain, domains equally weighted; pooled panel weights all frozen models equally.",
             f"- Bootstrap: {BOOTSTRAP_N:,} task-clustered, domain-stratified draws; seed {BOOTSTRAP_SEED}.",
             "- Primary: Critical Omission Rate BN - EN; positive values mean more literal omissions in Bengali. All other effects are secondary.",
             "", "## Primary and secondary language effects", ""]
    lines += effect_lines(report["effects"])
    lines += ["", "## Generation, missingness and truncation", "",
              "| Model/language | Expected | Generated | Scored | Unresolved API failure | Unattempted | Generated unscored | Truncated | Failure rate | Truncation rate among successes |",
              "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for key, counts in report["generation_status"]["by_model_language"].items():
        lines.append(f"| {key} | {counts['expected_cells']} | {counts['successful_generations']} | {counts['scored_cells']} | {counts['unresolved_api_failure_cells']} | {counts['unattempted_cells']} | {counts['generated_unscored_cells']} | {counts['truncated_successful_cells']} | {fmt(counts['unresolved_api_failure_rate'])} | {fmt(counts['truncation_rate_among_successes'])} |")
    lines += ["", report["generation_status"]["definitions"], "",
              "Generation date range (UTC): " + " to ".join(x or "NA" for x in report["generation_status"]["generation_date_range_utc"]), ""]
    for title, strata in (("Domain", report["by_domain"]), ("Difficulty", report["by_difficulty"])):
        lines += [f"## {title} strata", ""]
        for name, table in strata.items():
            lines += [f"### {name}", ""] + effect_lines(table) + [""]
    extended = report["extended_context_sensitivity"]
    lines += ["## Extended-context sensitivity", "",
              "Represented extended tasks: " + (", ".join(extended["extended_task_ids"]) or "None"), "",
              extended["interpretation"], "", "### Extended tasks only", ""]
    lines += effect_lines(extended["extended_only"])
    lines += ["", "### Excluding extended tasks", ""] + effect_lines(extended["excluding_extended"])
    missingness = report["missingness_sensitivity"]
    lines += ["", "## Missingness sensitivity", "", missingness["policy"], "",
              f"Tasks with all three languages scored for every panel model: {missingness['complete_panel_task_count']}.", ""]
    lines += effect_lines(missingness["effects_complete_panel_tasks"])
    truncation = report["truncation_sensitivity"]
    lines += ["", "## Truncation sensitivity", "", truncation["policy"], ""]
    lines += effect_lines(truncation["effects_excluding_truncated"])
    lines += ["", "## Interpretation limits", ""] + [f"- {text}" for text in report["limitations"]]
    lines += ["", "These are preliminary 157-task results and do not replace the planned final 500-task evaluation.", ""]
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
