"""Ensure every BN-CS prompt contains genuine English lexical material.

The primary v0.2 builder regenerates BN-CS from natural Bengali. A small number
of generic prompts may contain none of the domain lexicon entries. This pass
adds only common English lexical items by replacing equivalent Bengali nouns,
process terms, or instruction verbs. It never changes factual content.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPT_DIR = ROOT / "data" / "prompts"
LATIN_RE = re.compile(r"[A-Za-z]")

FILES = [
    p
    for p in sorted(PROMPT_DIR.glob("*.csv"))
    if p.name != "manifest.csv"
]

# Ordered from more domain-neutral professional nouns to instruction-verb
# fallbacks. The verb forms are common in Bengali-English technical discourse
# and preserve the same requested action.
FALLBACKS = [
    ("সমস্যা", "issue"),
    ("পদ্ধতি", "process"),
    ("পরীক্ষা", "check"),
    ("ধাপ", "step"),
    ("কাজ", "task"),
    ("কারণ", "factor"),
    ("ফল", "result"),
    ("সময়", "time"),
    ("নথি", "document"),
    ("সেবা", "service"),
    ("ব্যাখ্যা করুন", "explain করুন"),
    ("বর্ণনা করুন", "describe করুন"),
    ("প্রস্তাব করুন", "propose করুন"),
    ("তৈরি করুন", "design করুন"),
    ("লিখুন", "write করুন"),
    ("সংক্ষেপ করুন", "summarize করুন"),
    ("বলুন", "explain করুন"),
]


def latin_count(text: str) -> int:
    return len(LATIN_RE.findall(text))


def ensure_switching(text: str) -> str:
    if latin_count(text) >= 4:
        return text

    out = text
    for bengali, english in FALLBACKS:
        if bengali in out:
            out = out.replace(bengali, english, 1)
            if latin_count(out) >= 4:
                break
    return out


def main() -> None:
    changed = 0
    unresolved: list[str] = []

    for path in FILES:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            fields = reader.fieldnames
            rows = list(reader)

        if not fields or "prompt_bn_cs" not in fields:
            continue

        for row in rows:
            revised = ensure_switching(row["prompt_bn_cs"])
            if revised != row["prompt_bn_cs"]:
                row["prompt_bn_cs"] = revised
                changed += 1
            if latin_count(row["prompt_bn_cs"]) < 4:
                unresolved.append(row.get("task_id", "UNKNOWN"))

        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    if unresolved:
        raise RuntimeError(f"Unable to create natural BN-CS switching for: {unresolved}")

    print(f"BN-CS fallback pass complete; revised {changed} rows")


if __name__ == "__main__":
    main()
