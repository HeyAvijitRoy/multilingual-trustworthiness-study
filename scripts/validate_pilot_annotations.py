"""Validate RIU pilot annotation files.

Run from repository root:
    python scripts/validate_pilot_annotations.py
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANN = ROOT / "data" / "annotations"

FILES = [
    "pilot_technical.jsonl",
    "pilot_cybersecurity.jsonl",
    "pilot_procedural.jsonl",
    "pilot_decision_support.jsonl",
    "pilot_information_synthesis.jsonl",
]

REQUIRED = {
    "task_id",
    "domain",
    "difficulty",
    "task_objective",
    "expected_output_type",
    "safety_relevance",
    "requirement_visibility",
    "constraints",
    "rius",
    "notes",
    "status",
}

RIU_REQUIRED = {
    "id",
    "riu_type",
    "criticality",
    "description",
    "scoring_rule",
    "rationale",
}

DOMAINS = {
    "technical_troubleshooting",
    "cybersecurity_digital_safety",
    "procedural_instructional",
    "decision_support",
    "information_synthesis",
}

RIU_TYPES = {
    "fact",
    "action",
    "evidence",
    "constraint",
    "warning",
    "qualification",
    "comparison",
    "uncertainty",
}

def main() -> None:
    rows = []

    for filename in FILES:
        path = ANN / filename
        if not path.exists():
            raise AssertionError(f"Missing annotation file: {filename}")

        file_rows = []
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as exc:
                raise AssertionError(f"{filename}:{line_no}: invalid JSON: {exc}") from exc
            file_rows.append(rec)

        if len(file_rows) != 5:
            raise AssertionError(f"{filename}: expected 5 records, found {len(file_rows)}")
        rows.extend(file_rows)

    if len(rows) != 25:
        raise AssertionError(f"Expected 25 pilot records, found {len(rows)}")

    ids = [r["task_id"] for r in rows]
    if len(ids) != len(set(ids)):
        raise AssertionError("Duplicate task IDs in pilot annotations")

    domain_counts = Counter(r["domain"] for r in rows)
    if set(domain_counts) != DOMAINS:
        raise AssertionError(f"Unexpected domain set: {domain_counts}")
    if any(count != 5 for count in domain_counts.values()):
        raise AssertionError(f"Expected 5 records/domain: {domain_counts}")

    for rec in rows:
        missing = REQUIRED - set(rec)
        if missing:
            raise AssertionError(f"{rec.get('task_id','UNKNOWN')}: missing fields {sorted(missing)}")

        if rec["difficulty"] not in {"easy", "medium", "hard"}:
            raise AssertionError(f"{rec['task_id']}: invalid difficulty")
        if rec["requirement_visibility"] not in {"explicit", "implicit", "mixed"}:
            raise AssertionError(f"{rec['task_id']}: invalid requirement_visibility")
        if rec["safety_relevance"] not in {"none", "low", "moderate", "high"}:
            raise AssertionError(f"{rec['task_id']}: invalid safety_relevance")
        if rec["status"] != "pilot-internal-reviewed":
            raise AssertionError(f"{rec['task_id']}: unexpected status {rec['status']}")
        if not isinstance(rec["constraints"], list):
            raise AssertionError(f"{rec['task_id']}: constraints must be a list")
        if not isinstance(rec["rius"], list) or len(rec["rius"]) < 3:
            raise AssertionError(f"{rec['task_id']}: expected at least 3 RIUs")

        riu_ids = []
        critical = 0
        for riu in rec["rius"]:
            missing_riu = RIU_REQUIRED - set(riu)
            if missing_riu:
                raise AssertionError(
                    f"{rec['task_id']}: RIU missing fields {sorted(missing_riu)}"
                )
            riu_ids.append(riu["id"])
            if riu["riu_type"] not in RIU_TYPES:
                raise AssertionError(
                    f"{rec['task_id']} {riu['id']}: invalid type {riu['riu_type']}"
                )
            if riu["criticality"] not in {"critical", "supporting"}:
                raise AssertionError(
                    f"{rec['task_id']} {riu['id']}: invalid criticality"
                )
            if riu["criticality"] == "critical":
                critical += 1

        expected_ids = [f"RIU-{i:02d}" for i in range(1, len(riu_ids) + 1)]
        if riu_ids != expected_ids:
            raise AssertionError(
                f"{rec['task_id']}: non-sequential RIU IDs {riu_ids}"
            )
        if critical == 0:
            raise AssertionError(f"{rec['task_id']}: no critical RIUs")

    # Pilot coverage checks.
    for domain in DOMAINS:
        diffs = {r["difficulty"] for r in rows if r["domain"] == domain}
        if not {"easy", "medium", "hard"}.issubset(diffs):
            raise AssertionError(f"{domain}: pilot lacks easy/medium/hard coverage")

    if not any(r["task_id"] == "SYN091" for r in rows):
        raise AssertionError("Pilot must include SYN091 extended-context task")
    if not any(r["task_id"] == "SYN100" for r in rows):
        raise AssertionError("Pilot must include SYN100 extended-context task")

    total_rius = sum(len(r["rius"]) for r in rows)
    critical_rius = sum(
        1 for r in rows for x in r["rius"] if x["criticality"] == "critical"
    )

    print("RIU pilot validation PASSED")
    print(f"  tasks: {len(rows)}")
    print(f"  domains: {dict(domain_counts)}")
    print(f"  RIUs: {total_rius}")
    print(f"  critical RIUs: {critical_rius}")
    print("  extended-context: SYN091, SYN100")

if __name__ == "__main__":
    main()
