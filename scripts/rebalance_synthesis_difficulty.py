"""Rebalance information-synthesis difficulty after extended-context expansion.

SYN091-SYN093 were originally short extraction tasks labeled easy. After v0.2
expanded them into substantially longer multi-constraint contexts, keeping them
as easy would confound context density with the difficulty label.

To preserve the study's exact 25/50/25 per-domain allocation while improving
construct validity:
- SYN091-SYN093 -> medium
- SYN004-SYN006 -> easy

SYN004-SYN006 are short, explicit synthesis tasks with straightforward factual
coverage requirements and no multi-step dependency structure.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPT_DIR = ROOT / "data" / "prompts"
FILES = [
    PROMPT_DIR / "information_synthesis_001_050.csv",
    PROMPT_DIR / "information_synthesis_051_100.csv",
]

OVERRIDES = {
    "SYN004": "easy",
    "SYN005": "easy",
    "SYN006": "easy",
    "SYN091": "medium",
    "SYN092": "medium",
    "SYN093": "medium",
}


def main() -> None:
    seen: set[str] = set()

    for path in FILES:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            fields = reader.fieldnames
            rows = list(reader)

        if not fields:
            raise RuntimeError(f"Missing CSV header in {path}")

        for row in rows:
            task_id = row["task_id"]
            if task_id in OVERRIDES:
                row["difficulty"] = OVERRIDES[task_id]
                seen.add(task_id)

        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    missing = set(OVERRIDES) - seen
    if missing:
        raise RuntimeError(f"Difficulty override IDs not found: {sorted(missing)}")

    print("Synthesis difficulty rebalance applied:")
    print("  SYN004-SYN006 -> easy")
    print("  SYN091-SYN093 -> medium")


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
