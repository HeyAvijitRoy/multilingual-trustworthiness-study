"""Validate the multilingual prompt corpus before any model evaluation.

The validator is deliberately strict about the design decisions that should not
change after freezing the corpus. It does not score answer quality; it checks
corpus construction and language-condition hygiene.

Run from repo root:
    python scripts/validate_prompt_corpus.py
"""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPT_DIR = ROOT / "data" / "prompts"

PROMPT_FILES = [
    "technical_troubleshooting_001_050.csv",
    "technical_troubleshooting_051_100.csv",
    "cybersecurity_digital_safety_001_050.csv",
    "cybersecurity_digital_safety_051_100.csv",
    "procedural_instructional_001_050.csv",
    "procedural_instructional_051_100.csv",
    "decision_support_001_050.csv",
    "decision_support_051_100.csv",
    "information_synthesis_001_050.csv",
    "information_synthesis_051_100.csv",
]

FIELDS = [
    "task_id",
    "domain",
    "subdomain",
    "difficulty",
    "prompt_en",
    "prompt_bn",
    "prompt_bn_cs",
]

DOMAIN_PREFIX = {
    "technical_troubleshooting": "TECH",
    "cybersecurity_digital_safety": "CYBER",
    "procedural_instructional": "PROC",
    "decision_support": "DEC",
    "information_synthesis": "SYN",
}

BENGALI_RE = re.compile(r"[\u0980-\u09FF]")
LATIN_RE = re.compile(r"[A-Za-z]")

DEPRECATED_BN_PHRASES = {
    "কার্যকরী ফোল্ডার",
    "ধারাবাহিক সমন্বয়",
    "নির্মাণ সঞ্চয়",
    "বাস্তব এপিআই",
    "গ্রাহক ব্যর্থতা",
    "পুনরাবৃত্তি-নিরাপত্তা",
}


def alpha_script_counts(text: str) -> tuple[int, int]:
    return len(BENGALI_RE.findall(text)), len(LATIN_RE.findall(text))


def load_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for filename in PROMPT_FILES:
        path = PROMPT_DIR / filename
        if not path.exists():
            raise AssertionError(f"Missing prompt file: {filename}")
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != FIELDS:
                raise AssertionError(
                    f"Schema mismatch in {filename}: {reader.fieldnames} != {FIELDS}"
                )
            file_rows = list(reader)
        if len(file_rows) != 50:
            raise AssertionError(f"{filename}: expected 50 rows, found {len(file_rows)}")
        rows.extend(file_rows)
    return rows


def validate_structure(rows: list[dict[str, str]]) -> None:
    if len(rows) != 500:
        raise AssertionError(f"Expected 500 rows, found {len(rows)}")

    ids = [row["task_id"] for row in rows]
    if len(ids) != len(set(ids)):
        duplicates = [item for item, count in Counter(ids).items() if count > 1]
        raise AssertionError(f"Duplicate task IDs: {duplicates}")

    for row in rows:
        for field in FIELDS:
            if not row[field].strip():
                raise AssertionError(f"{row['task_id']}: empty field {field}")
        if row["difficulty"] not in {"easy", "medium", "hard"}:
            raise AssertionError(f"{row['task_id']}: bad difficulty {row['difficulty']}")

    domain_counts = Counter(row["domain"] for row in rows)
    expected_domains = set(DOMAIN_PREFIX)
    if set(domain_counts) != expected_domains:
        raise AssertionError(f"Unexpected domains: {domain_counts}")
    for domain in expected_domains:
        if domain_counts[domain] != 100:
            raise AssertionError(f"{domain}: expected 100 rows, found {domain_counts[domain]}")

    for domain, prefix in DOMAIN_PREFIX.items():
        domain_ids = sorted(
            int(row["task_id"].removeprefix(prefix))
            for row in rows
            if row["domain"] == domain
        )
        if domain_ids != list(range(1, 101)):
            raise AssertionError(f"{domain}: ID range is not exactly {prefix}001-{prefix}100")


def validate_difficulty(rows: list[dict[str, str]]) -> None:
    by_domain: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        by_domain[row["domain"]][row["difficulty"]] += 1

    expected = Counter({"easy": 25, "medium": 50, "hard": 25})
    for domain, counts in by_domain.items():
        if counts != expected:
            raise AssertionError(f"{domain}: difficulty {counts}; expected {expected}")

    total = Counter(row["difficulty"] for row in rows)
    if total != Counter({"easy": 125, "medium": 250, "hard": 125}):
        raise AssertionError(f"Overall difficulty mismatch: {total}")


def validate_language_conditions(rows: list[dict[str, str]]) -> None:
    for row in rows:
        task_id = row["task_id"]
        bn = row["prompt_bn"]
        cs = row["prompt_bn_cs"]

        bn_bengali, bn_latin = alpha_script_counts(bn)
        cs_bengali, cs_latin = alpha_script_counts(cs)

        if bn_bengali < 20:
            raise AssertionError(f"{task_id}: Bengali prompt has too little Bengali script")
        if bn_bengali + bn_latin and bn_bengali / (bn_bengali + bn_latin) < 0.55:
            raise AssertionError(f"{task_id}: Bengali condition is not predominantly Bengali")

        if cs_bengali < 10 or cs_latin < 4:
            raise AssertionError(f"{task_id}: BN-CS must contain both Bengali and English material")
        if cs_bengali + cs_latin:
            bn_share = cs_bengali / (cs_bengali + cs_latin)
            if not 0.25 <= bn_share <= 0.90:
                raise AssertionError(
                    f"{task_id}: BN-CS Bengali script share {bn_share:.2f} outside 0.25-0.90"
                )

        if bn == cs:
            raise AssertionError(f"{task_id}: Bengali and BN-CS prompts are identical")

        for phrase in DEPRECATED_BN_PHRASES:
            if phrase in bn:
                raise AssertionError(f"{task_id}: deprecated technical Bengali phrase remains: {phrase}")


def validate_duplicates(rows: list[dict[str, str]]) -> None:
    for field in ("prompt_en", "prompt_bn", "prompt_bn_cs"):
        values = [re.sub(r"\s+", " ", row[field]).strip().casefold() for row in rows]
        dupes = [value for value, count in Counter(values).items() if count > 1]
        if dupes:
            raise AssertionError(f"Exact duplicates detected in {field}: {len(dupes)}")


def validate_extended_context(rows: list[dict[str, str]]) -> None:
    target_ids = {f"SYN{number:03d}" for number in range(91, 101)}
    found = {row["task_id"] for row in rows if row["subdomain"] == "extended_context"}
    if found != target_ids:
        raise AssertionError(
            f"extended_context IDs mismatch. Expected {sorted(target_ids)}, found {sorted(found)}"
        )

    for row in rows:
        if row["task_id"] not in target_ids:
            continue
        en_words = len(row["prompt_en"].split())
        bn_tokens = len(row["prompt_bn"].split())
        # v0.2 requires a large increase over the original short context items.
        if en_words < 180:
            raise AssertionError(f"{row['task_id']}: English extended context only {en_words} words")
        if bn_tokens < 120:
            raise AssertionError(f"{row['task_id']}: Bengali extended context only {bn_tokens} tokens")


def main() -> None:
    rows = load_rows()
    validate_structure(rows)
    validate_difficulty(rows)
    validate_language_conditions(rows)
    validate_duplicates(rows)
    validate_extended_context(rows)

    print("Prompt corpus validation PASSED")
    print("  tasks: 500")
    print("  prompt instances: 1,500")
    print("  domains: 5 x 100")
    print("  difficulty per domain: 25 easy / 50 medium / 25 hard")
    print("  language conditions: EN / BN / BN-CS")
    print("  extended-context tasks: SYN091-SYN100")


if __name__ == "__main__":
    main()
