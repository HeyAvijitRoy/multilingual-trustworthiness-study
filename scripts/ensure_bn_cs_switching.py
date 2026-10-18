"""Ensure every BN-CS prompt contains genuine, readable English lexical switching.

The primary v0.2 builder regenerates BN-CS from natural Bengali. This pass:
1. guarantees intentional lexical divergence from prompt_bn;
2. adds a conservative fallback switch where needed; and
3. normalizes Bengali case/number suffixes around Latin-script terms so output
   does not contain artifacts such as ``emailে`` or ``Wi-Fiতে``.

The pass changes surface realization only. It must not alter facts, constraints,
or the requested task.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPT_DIR = ROOT / "data" / "prompts"
LATIN_RE = re.compile(r"[A-Za-z]")

FILES = [p for p in sorted(PROMPT_DIR.glob("*.csv")) if p.name != "manifest.csv"]

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

SPECIAL_SURFACE_FIXES = [
    ("পূর্বregistration", "আগাম registration"),
    ("recordিং", "recording"),
    ("reportিং", "reporting"),
    ("monitorিং", "monitoring"),
    ("processিং", "processing"),
]

LATIN_TOKEN = r"([A-Za-z][A-Za-z0-9+.#/_-]*)"
SUFFIX_RULES = [
    ("গুলোতে", "-গুলোতে"),
    ("গুলোকে", "-গুলোকে"),
    ("গুলোর", "-গুলোর"),
    ("গুলো", "-গুলো"),
    ("গুলিতে", "-গুলিতে"),
    ("গুলি", "-গুলি"),
    ("য়ের", "-এর"),
    ("ের", "-এর"),
    ("এর", "-এর"),
    ("তে", "-তে"),
    ("কে", "-কে"),
    ("টি", "-টি"),
    ("টা", "-টা"),
    ("রা", "-রা"),
    ("ে", "-এ"),
    ("ও", "-ও"),
]


def latin_count(text: str) -> int:
    return len(LATIN_RE.findall(text))


def add_one_switch(text: str) -> str:
    for bengali, english in FALLBACKS:
        if bengali in text:
            revised = text.replace(bengali, english, 1)
            if revised != text:
                return revised
    return text


def normalize_surface(text: str) -> str:
    out = text

    for old, new in SPECIAL_SURFACE_FIXES:
        out = out.replace(old, new)

    for suffix, replacement in SUFFIX_RULES:
        out = re.sub(LATIN_TOKEN + re.escape(suffix), rf"\1{replacement}", out)

    out = re.sub(r"([\u0980-\u09FF])([A-Za-z])", r"\1 \2", out)
    out = re.sub(r"([A-Za-z0-9])([\u0980-\u09FF])", r"\1-\2", out)

    # Overlapping suffix rules can otherwise turn an already normalized form
    # such as recording-এর into recording--এর. Collapse only hyphen runs that
    # directly precede Bengali script; command-line flags such as --force are
    # therefore unaffected.
    out = re.sub(r"([A-Za-z0-9])-+([\u0980-\u09FF])", r"\1-\2", out)

    out = re.sub(r"[ \t]+", " ", out).strip()
    return out


def ensure_switching(prompt_bn: str, prompt_bn_cs: str) -> str:
    out = prompt_bn_cs

    if out == prompt_bn:
        out = add_one_switch(out)

    if latin_count(out) < 4:
        out = add_one_switch(out)

    return normalize_surface(out)


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

            if latin_count(row["prompt_bn_cs"]) < 4 or row["prompt_bn_cs"] == row["prompt_bn"]:
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

    print(f"BN-CS fallback/surface pass complete; revised {changed} rows")


if __name__ == "__main__":
    import sys
    if "--force-historical" not in sys.argv:
        raise SystemExit(
            "Historical v0.2 corpus script: running it would overwrite the hand-written v0.3 "
            "Bengali conditions. See data/prompts/CORPUS_CHANGELOG.md. Pass --force-historical "
            "only to reproduce v0.2 on a separate checkout."
        )
    sys.argv.remove("--force-historical")
    main()
