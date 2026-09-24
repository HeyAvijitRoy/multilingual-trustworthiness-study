"""Ensure every BN-CS prompt contains genuine English lexical material.

The primary v0.2 builder regenerates BN-CS from natural Bengali. A small number
of generic prompts may contain none of the domain lexicon entries. Some Bengali
prompts also already contain Latin-script labels such as A/B/C, which must not
be mistaken for meaningful code-switching.

This pass therefore requires BOTH:
1. Latin-script lexical material in BN-CS; and
2. intentional surface divergence from prompt_bn.

Fallback replacements preserve factual content and requested actions.
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

# Ordered from domain-neutral professional nouns to instruction-verb fallbacks.
# These forms are common in Bengali-English professional/technical discourse.
FALLBACKS = [
    ("সমস্যা", "issue"),
    ("পদ্ধতি", "process"),
    ("পরীক্ষা", "check"),
    ("ধাপ", "step"),
    ("কাজ", "task"),
    ("কারণ", "factor"),
    ("ফলাফল", "result"),
    ("ফল", "result"),
    ("সময়", "time"),
    ("সময়সূচি", "schedule"),
    ("নথি", "document"),
    ("সেবা", "service"),
    ("তথ্য", "data"),
    ("প্রমাণ", "evidence"),
    ("সারাংশ", "summary"),
    ("উত্তর", "response"),
    ("পরিস্থিতি", "scenario"),
    ("বিষয়", "point"),
    ("ব্যাখ্যা করুন", "explain করুন"),
    ("বর্ণনা করুন", "describe করুন"),
    ("প্রস্তাব করুন", "propose করুন"),
    ("তৈরি করুন", "design করুন"),
    ("তুলনা করুন", "compare করুন"),
    ("চিহ্নিত করুন", "identify করুন"),
    ("আলাদা করুন", "separate করুন"),
    ("নির্ধারণ করুন", "determine করুন"),
    ("উল্লেখ করুন", "mention করুন"),
    ("রূপ দিন", "convert করুন"),
    ("বের করুন", "extract করুন"),
    ("দেখান", "show করুন"),
    ("বেছে নিন", "choose করুন"),
    ("লিখুন", "write করুন"),
    ("সংক্ষেপ করুন", "summarize করুন"),
    ("বলুন", "explain করুন"),
]


def latin_count(text: str) -> int:
    return len(LATIN_RE.findall(text))


def add_one_switch(text: str) -> str:
    """Apply the first natural fallback replacement that changes the text."""
    for bengali, english in FALLBACKS:
        if bengali in text:
            revised = text.replace(bengali, english, 1)
            if revised != text:
                return revised
    return text


def ensure_switching(prompt_bn: str, prompt_bn_cs: str) -> str:
    out = prompt_bn_cs

    # A/B/C, model names, dates, or acronyms already present in prompt_bn do
    # not by themselves establish a distinct code-switched condition.
    if out == prompt_bn:
        out = add_one_switch(out)

    # If the distinct condition still lacks lexical English, add one fallback.
    if latin_count(out) < 4:
        out = add_one_switch(out)

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
            original = row["prompt_bn_cs"]
            revised = ensure_switching(row["prompt_bn"], original)
            if revised != original:
                row["prompt_bn_cs"] = revised
                changed += 1

            if (
                latin_count(row["prompt_bn_cs"]) < 4
                or row["prompt_bn_cs"] == row["prompt_bn"]
            ):
                unresolved.append(row.get("task_id", "UNKNOWN"))

        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    if unresolved:
        raise RuntimeError(
            "Unable to create a distinct natural BN-CS condition for: "
            f"{unresolved}"
        )

    print(f"BN-CS fallback pass complete; revised {changed} rows")


if __name__ == "__main__":
    main()
