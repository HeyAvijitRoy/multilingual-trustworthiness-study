"""Explicit provenance-bound spending approval; no implicit approval from a key.

This validates an approval record's structure/hash, not a person's authenticity.
The agent must obtain real user authorization before creating an approved record.
"""
import hashlib
import json
import math
import os
from pathlib import Path
import shlex

ROOT=Path(__file__).resolve().parents[1]


def load_api_environment(path=None):
    """Optional explicit dotenv selection; no shell evaluation or secret output."""
    if path is None: return
    path=Path(path)
    for line in path.read_text(encoding='utf-8').splitlines():
        line=line.strip()
        if line.startswith('export '): line=line[7:]
        if not line or line.startswith('#') or '=' not in line: continue
        key,value=line.split('=',1)
        key=key.strip()
        if key not in {'OPENAI_API_KEY','GEMINI_API_KEY'}: continue
        parts=shlex.split(value,comments=True,posix=True)
        if len(parts)!=1: raise RuntimeError('invalid credential assignment for '+key)
        os.environ.setdefault(key,parts[0])


def require_spending_approval(config,manifest,purpose):
    relative=manifest.get('spending_approval_record')
    if not relative: raise RuntimeError('explicit user spending approval is not recorded')
    path=(ROOT/relative).resolve()
    pins=manifest.get('artifact_sha256',{})
    if not path.is_relative_to(ROOT) or not path.is_file():
        raise RuntimeError('spending approval evidence missing')
    if pins.get(path.relative_to(ROOT).as_posix()) != hashlib.sha256(path.read_bytes()).hexdigest():
        raise RuntimeError('spending approval is not bound to the immutable manifest')
    record=json.loads(path.read_text())
    if (record.get('status')!='approved' or not record.get('approved_by') or not record.get('approved_at')
            or purpose not in record.get('purposes',[]) or record.get('currency')!='USD'
            or isinstance(record.get('maximum_usd'),bool)
            or not isinstance(record.get('maximum_usd'),(int,float))
            or not math.isfinite(record['maximum_usd']) or record['maximum_usd']<=0
            or record.get('protocol_id')!=config['protocol_id']):
        raise RuntimeError('spending approval does not cover this action')
    return record
