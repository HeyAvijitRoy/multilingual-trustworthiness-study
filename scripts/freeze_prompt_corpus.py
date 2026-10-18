"""Write or verify data/annotations/PROMPT_FREEZE.json for the current prompt corpus version.

The manifest pins the SHA-256 of every file under data/prompts/. Run it only when a versioned
corpus revision has been approved; annotation work must never silently re-pin prompts.

    python scripts/freeze_prompt_corpus.py          # write the manifest
    python scripts/freeze_prompt_corpus.py --check  # verify without writing
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "annotations" / "PROMPT_FREEZE.json"
CORPUS_VERSION = "0.3"
SUPERSEDES = {"corpus_version": "0.2", "baseline_commit": "74604be07b2246e1d7f063088a35799721290e81"}


def build(root: Path = ROOT) -> dict:
    # Sort on POSIX path strings: Path ordering is case-insensitive on Windows but not on Linux.
    paths = sorted((f for f in (root / "data" / "prompts").rglob("*") if f.is_file()),
                   key=lambda f: f.relative_to(root).as_posix())
    files = {f.relative_to(root).as_posix(): hashlib.sha256(f.read_bytes()).hexdigest() for f in paths}
    return {"corpus_version": CORPUS_VERSION, "supersedes": SUPERSEDES, "algorithm": "sha256", "files": files}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    manifest = build()
    text = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if json.loads(MANIFEST.read_text(encoding="utf-8")) != manifest:
            raise SystemExit("PROMPT_FREEZE.json is stale: prompt bytes or file set changed")
        print(f"PROMPT_FREEZE.json matches corpus v{CORPUS_VERSION} ({len(manifest['files'])} files)")
        return
    MANIFEST.write_text(text, encoding="utf-8", newline="\n")
    print(f"Wrote PROMPT_FREEZE.json for corpus v{CORPUS_VERSION} ({len(manifest['files'])} files)")


if __name__ == "__main__":
    main()
