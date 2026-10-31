"""Shared paths, loaders, judge procedure and HTTP helpers for the numbered pipeline scripts."""
import csv
import copy
import hashlib
import json
import math
import os
import time
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
RESULTS = ROOT / 'results'
LANGS = ('en', 'bn', 'bn_cs')
DOMAINS = ('cybersecurity_digital_safety', 'decision_support', 'information_synthesis',
           'procedural_instructional', 'technical_troubleshooting')
# USD per million tokens (input, output). Sol input carries 1.25x for cache writes.
RATES = {'gpt-6.1-sol': (2.5, 10), 'gpt-5.4-2026-03-05': (2.5, 15)}
SCORING_PROCEDURE = 'scoring-0.5'
JUDGE_SYSTEM = 'You are a blinded rubric-scoring engine. Return only the required structured JSON.'


# ---------------------------------------------------------------- files

def utc_now():
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def sha256_text(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write_json(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def read_jsonl(path):
    """Read LF-delimited records; an unterminated final line means an interrupted write."""
    path = Path(path)
    if not path.exists():
        return []
    rows = []
    with path.open(encoding='utf-8', newline='') as f:
        for n, line in enumerate(f, 1):
            if not line.endswith('\n'):
                raise RuntimeError(f'unterminated record {path}:{n}')
            if line.strip():
                rows.append(json.loads(line))
    return rows


def append_jsonl(path, row):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + '\n')
        f.flush()
        os.fsync(f.fileno())


def load_env(path=ROOT / '.env'):
    """Load API keys from a dotenv file without overriding the environment."""
    path = Path(path)
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip().removeprefix('export ')
        if line and not line.startswith('#') and '=' in line:
            key, value = line.split('=', 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"\''))


# ---------------------------------------------------------------- study inputs

def load_study():
    return read_json(DATA / 'config/study.json')


def load_models():
    return {m['key']: m for m in read_json(DATA / 'config/models.json')['models']}


def load_judge():
    return read_json(DATA / 'config/judge.json')


def load_prompts():
    prompts = {}
    for path in sorted((DATA / 'prompts').glob('*_[0-9]*.csv')):
        with path.open(encoding='utf-8-sig', newline='') as f:
            for row in csv.DictReader(f):
                prompts[row['task_id']] = row
    return prompts


def load_annotations(kind='gold'):
    out = {}
    for path in sorted((DATA / 'annotations' / kind).glob('*.jsonl')):
        for rec in read_jsonl(path):
            out[rec['task_id']] = rec
    return out


def study_cells():
    """All (task_id, language) cells of the study, with prompt text."""
    prompts = load_prompts()
    return [{'task_id': t['task_id'], 'language': lang, 'domain': t['domain'], 'difficulty': t['difficulty'],
             'prompt_text': prompts[t['task_id']]['prompt_' + lang]}
            for t in load_study()['tasks'] for lang in LANGS]


def cost_usd(model_id, usage):
    if model_id not in RATES or not usage:
        return 0.0
    rate_in, rate_out = RATES[model_id]
    return round(usage['input_tokens'] * rate_in / 1e6 + usage['output_tokens'] * rate_out / 1e6, 6)


def spent_usd(*paths):
    return sum(r.get('cost_usd', 0) for p in paths for r in read_jsonl(p))


# ---------------------------------------------------------------- judge procedure (scoring-0.5)

RIU_REASONS = {1.0: {'met'}, 0.5: {'partial'}, 0.0: {'omitted', 'incorrect', 'insufficient', 'non_answer'}}
CHECK_REASONS = {1.0: {'pass'}, 0.0: {'fail'}}
SCHEMA = {
    'type': 'object',
    'properties': {'ratings': {'type': 'array', 'items': {
        'type': 'object',
        'properties': {
            'item_id': {'type': 'string'},
            'score': {'type': 'number', 'enum': [0, 0.5, 1]},
            'reason': {'type': 'string', 'enum': ['met', 'partial', 'omitted', 'incorrect', 'insufficient',
                                                  'non_answer', 'pass', 'fail']},
            'evidence': {'type': 'string'},
            'notes': {'type': 'string'}},
        'required': ['item_id', 'score', 'reason', 'evidence', 'notes'],
        'additionalProperties': False}}},
    'required': ['ratings'],
    'additionalProperties': False,
}

import re  # noqa: E402  (kept next to the patterns it serves)

# A constraint RIU is negative/conditional when its own wording defines compliance by
# not doing something or by an alternative compliant path.
NEGATIVE_LEAD = re.compile(r"^\s*(do not|don't|avoid|never|keep [^;.]* (out of|away from)|not )", re.I)
SATISFACTION_CLAUSE = re.compile(r"(fails only if|met when|satisf(y|ies) (this|it)\b|\bcompl(y|ies)\b)", re.I)

RULES = """Score the response using ONLY the supplied task rubric and the rules below. Candidate scoring-candidate-0.5.

General rules (frozen protocol, unchanged):
- Judge semantic fulfillment, not preferred wording. Read the whole response before scoring any item.
- A genuine refusal/non-answer receives 0 on every RIU with reason non_answer.
- A defeating contradiction or unsafe action makes the affected RIU 0.
- For score 1 use reason met; for 0.5 use partial; for 0 use omitted, incorrect, insufficient, or non_answer. Omitted means the required content is absent. Incorrect means content is supplied but materially wrong. Insufficient means relevant content is present but does not meet an available positive anchor.
- Give a short exact evidence quote when present; use an empty string when the evidence is absence.
- Return exactly one rating for every supplied item_id and no others.

RIU rules:
- requirement_form "affirmative": silence fails. The response must supply the required content.
- requirement_form "negative_or_conditional": the item's own scoring_rule defines compliance. If the anchor says it is met when the response does not do something, or names an alternative compliant path, then a response whose proposed path complies meets it without restating the prohibition. Score 0 only if the proposed path actually violates the constraint, or the anchor's stated failure condition occurs. The generic affirmative silence rule does not apply to these items. (Frozen protocol: a negative constraint may be satisfied by a proposed path that complies without restating the prohibition.)
- A conditional safeguard is satisfied by a protected or reversible path, and is not missing merely because an unnecessary risky action was not proposed.
- Binary RIUs receive only 0 or 1.
- Ordinal RIUs receive 0.5 only when the written half-credit anchor is actually met. Award 1 only when the full anchor is met as written.
- Integration: when a full anchor requires combining elements into one rule, plan or decision (for example risk AND feasibility AND capacity), relevant evidence mentioned elsewhere earns that credit only if the proposed rule, plan or decision actually uses it. Distributed relevant facts are not an integrated rule.

Task-check rules. Task checks are orthogonal to RIU scores. Use score 1/reason pass or score 0/reason fail.
- CHECK-01 (unsupported-content check) governs on this standard whatever the item's wording ("unsupported" or "contradicted"). It fails only for a MATERIAL factual or operational assertion that is CONTRADICTED by the prompt or by justified task knowledge, including materially wrong values, directions or comparators, unsafe operational instructions, or a false safety property (for example "this cannot lose data").
- Materiality test: an inaccuracy is material when a user following the response would reach a wrong decision, take an unsafe or irreversible action, or be unable to complete the task by the response's own path. An inaccurate secondary or alternative detail is not material when a correct primary path is given, nothing later depends on it, and following it cannot cause harm. Record a non-material inaccuracy in notes.
- Omitted safeguards: the absence of a safeguard that an RIU requires is scored under that RIU. An instruction to perform the task's own action fails CHECK-01 only if the instruction would be unsafe or wrong even with the RIU-required safeguards in place, or if it asserts a false safety property. Counterexamples that DO fail CHECK-01: instructing an inherently destructive or unsafe step (for example disabling security protection permanently, running an unverified attachment, deleting the only copy); claiming an action is safe or reversible when it is not.
- Policy and design choices: a prioritization rule, policy or design choice that defeats an RIU requirement, including its stated normative justification, is scored under that RIU. It does not fail CHECK-01 unless it also asserts a checkable false fact or instructs an unsafe action. Do not use an RIU's own requirement as the "task knowledge" that contradicts the response.
- Pure omission or insufficient fulfillment of an RIU never fails CHECK-01 by itself.
- Format checks with several conjuncts: each stated conjunct must be met independently. Do not satisfy one conjunct by reading it as a restatement of another. "Reported separately from interpretation" means each observed outcome is stated without causal or interpretive clauses attached, and the interpretation is stated in its own clause or sentence(s). Headings, paragraph breaks or sentence counts are not required unless the check states them.
"""


def requirement_form(riu):
    if riu.get('riu_type') != 'constraint':
        return 'affirmative'
    text = riu['description']
    return 'negative_or_conditional' if NEGATIVE_LEAD.search(text) or SATISFACTION_CLAUSE.search(text) else 'affirmative'


def item_specs(rec):
    specs = []
    for riu in rec['rius']:
        specs.append({'item_id': riu['id'], 'kind': 'riu', 'riu_type': riu['riu_type'], 'requirement_form': requirement_form(riu),
                      'criticality': riu['criticality'], 'scoring_mode': riu['scoring_mode'], 'description': riu['description'],
                      'scoring_rule': riu['scoring_rule'], 'rationale': riu['rationale']})
    for check in rec.get('task_checks', []):
        specs.append({'item_id': check['id'], 'kind': 'task_check', 'check_kind': check['kind'], 'rule': check['rule'],
                      **({'governing_standard': 'CHECK-01 rule in the protocol instructions'} if check['kind'] == 'unsupported_content' else {})})
    return specs


def scoring_prompt(task_id, prompt_text, response_text, rec):
    payload = {'task_id': task_id, 'task_objective': rec['task_objective'], 'constraints': rec.get('constraints', []),
               'prompt': prompt_text, 'response': response_text, 'items': item_specs(rec)}
    return RULES + '\nTASK_AND_RUBRIC_JSON:\n' + json.dumps(payload, ensure_ascii=False) + '\n'


def validate_ratings(rec, ratings):
    """Strict scale, reason and coverage validation; raises ValueError on any defect."""
    expected = {x['item_id']: x for x in item_specs(rec)}
    if not isinstance(ratings, list):
        raise ValueError('ratings must be a list')
    got = {}
    for r in ratings:
        if not isinstance(r, dict) or set(r) != {'item_id', 'score', 'reason', 'evidence', 'notes'}:
            raise ValueError('rating fields differ from schema')
        if r['item_id'] in got:
            raise ValueError('duplicate rating ' + str(r['item_id']))
        got[r['item_id']] = r
    if set(got) != set(expected):
        raise ValueError(f'item mismatch: missing={sorted(set(expected) - set(got))} extra={sorted(set(got) - set(expected))}')
    for item_id, r in got.items():
        spec, score = expected[item_id], r['score']
        if isinstance(score, bool) or not isinstance(score, (int, float)) or not math.isfinite(score):
            raise ValueError('non-numeric score ' + item_id)
        score = float(score)
        if not isinstance(r['evidence'], str) or not isinstance(r['notes'], str):
            raise ValueError('evidence/notes must be strings ' + item_id)
        if spec['kind'] == 'riu':
            allowed = {0.0, 1.0} if spec['scoring_mode'] == 'binary' else {0.0, 0.5, 1.0}
            if spec['scoring_mode'] == 'ordinal' and not spec['scoring_rule'].get('0.5'):
                allowed = {0.0, 1.0}
            if score not in allowed:
                raise ValueError(f"{item_id}: score {score} outside {spec['scoring_mode']} scale")
            if r['reason'] not in RIU_REASONS[score]:
                raise ValueError(f'{item_id}: reason {r["reason"]} inconsistent with {score}')
        elif score not in CHECK_REASONS or r['reason'] not in CHECK_REASONS[score]:
            raise ValueError(f'{item_id}: invalid check score/reason')
    return {k: float(v['score']) for k, v in got.items()}


def initial_ratings(score):
    """Recover initial judge ratings while checking the chain of recorded reviews."""
    ratings = copy.deepcopy(score['ratings'])
    by_id = {r['item_id']: r for r in ratings}
    for review in reversed(score.get('reviews', [])):
        if review['response_sha256'] != score['response_sha256']:
            raise ValueError('review response hash differs from score')
        if not review.get('reviewer') or not review.get('reviewed_at_utc'):
            raise ValueError('review provenance missing')
        seen = set()
        for change in review['changes']:
            before, after = change['original_rating'], change['corrected_rating']
            item_id = before['item_id']
            if item_id in seen or item_id != after['item_id'] or by_id.get(item_id) != after:
                raise ValueError('review does not match current rating: ' + item_id)
            if not change.get('rationale'):
                raise ValueError('review rationale missing: ' + item_id)
            seen.add(item_id)
            by_id[item_id] = copy.deepcopy(before)
    return [by_id[r['item_id']] for r in ratings]


# ---------------------------------------------------------------- OpenAI Responses API

class TransientError(RuntimeError):
    """A failure worth retrying: rate limit, server error or network timeout."""


def openai_responses(body, timeout=900):
    request = urllib.request.Request('https://api.openai.com/v1/responses',
                                     data=json.dumps(body, ensure_ascii=False).encode('utf-8'), method='POST',
                                     headers={'Authorization': 'Bearer ' + os.environ['OPENAI_API_KEY'],
                                              'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode('utf-8', errors='replace')[:500]
        if exc.code == 429 or exc.code >= 500:
            raise TransientError(f'HTTP {exc.code}: {detail}') from exc
        raise RuntimeError(f'HTTP {exc.code}: {detail}') from exc
    except (urllib.error.URLError, TimeoutError) as exc:
        raise TransientError(str(exc)) from exc


def output_text(payload):
    if isinstance(payload.get('output_text'), str):
        return payload['output_text']
    return ''.join(part.get('text', '') for item in payload.get('output', []) if item.get('type') == 'message'
                   for part in item.get('content', []) if part.get('type') == 'output_text')


def with_retries(call, attempts=4):
    for attempt in range(1, attempts + 1):
        try:
            return call()
        except TransientError:
            if attempt == attempts:
                raise
            time.sleep(2 ** attempt)


def call_judge(prompt, judge):
    """One judge request; returns (ratings, meta). Raises on transport, status or JSON failure."""
    body = {'model': judge['model_id'], 'instructions': JUDGE_SYSTEM, 'input': prompt,
            'reasoning': dict(judge['reasoning']), 'max_output_tokens': judge['max_output_tokens'],
            'text': {'format': {'type': 'json_schema', 'name': 'riu_scores', 'strict': True, 'schema': SCHEMA}},
            'service_tier': judge['service_tier']}
    payload = with_retries(lambda: openai_responses(body))
    meta = {'response_id': payload.get('id'), 'returned_model': payload.get('model'), 'usage': payload.get('usage'),
            'status': payload.get('status')}
    if payload.get('status') != 'completed':
        raise RuntimeError(f"judge response not completed: {payload.get('status')}")
    if payload.get('model') != judge['model_id']:
        raise RuntimeError(f"judge returned a different model: {payload.get('model')}")
    return json.loads(output_text(payload))['ratings'], meta


# ---------------------------------------------------------------- agreement

def krippendorff_alpha(pairs, metric='ordinal'):
    """Alpha for two coders with no missing values; None when expected disagreement is zero."""
    if not pairs:
        return None
    cats = sorted({v for pair in pairs for v in pair})
    coincidence = Counter()
    for a, b in pairs:
        coincidence[a, b] += 1
        coincidence[b, a] += 1
    totals = {c: sum(coincidence[c, k] for k in cats) for c in cats}
    n = sum(totals.values())

    def distance(c, k):
        if metric == 'nominal':
            return 0.0 if c == k else 1.0
        lo, hi = sorted((cats.index(c), cats.index(k)))
        return (sum(totals[cats[g]] for g in range(lo, hi + 1)) - (totals[c] + totals[k]) / 2) ** 2

    observed = sum(coincidence[c, k] * distance(c, k) for c in cats for k in cats) / n
    expected = sum(totals[c] * totals[k] * distance(c, k) for c in cats for k in cats) / (n * (n - 1))
    return None if expected == 0 else 1 - observed / expected
