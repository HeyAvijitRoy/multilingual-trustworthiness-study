"""Read-only RIU validation. Standard library only; never generates responses."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
from validate_prompt_corpus import load_rows

ROOT = Path(__file__).resolve().parents[1]
ANN = ROOT / 'data' / 'annotations'
FILES = ['pilot_technical.jsonl', 'pilot_cybersecurity.jsonl', 'pilot_procedural.jsonl',
         'pilot_decision_support.jsonl', 'pilot_information_synthesis.jsonl']
DOMAINS = ['technical_troubleshooting', 'cybersecurity_digital_safety',
           'procedural_instructional', 'decision_support', 'information_synthesis']
PILOT_IDS = {p + n for p in ['TECH', 'CYBER', 'PROC', 'DEC']
             for n in ['001', '004', '006', '009', '010']} | {'SYN004', 'SYN008', 'SYN009', 'SYN091', 'SYN100'}
TYPES = {'fact', 'action', 'evidence', 'constraint', 'warning', 'qualification', 'comparison', 'uncertainty'}
REQUIRED = {'task_id', 'domain', 'difficulty', 'task_objective', 'expected_output_type',
            'safety_relevance', 'requirement_visibility', 'constraints', 'rius', 'notes',
            'status', 'schema_version', 'prompt_sha256', 'review', 'task_checks'}
UNIT_KEYS = {'id', 'source_riu_ids', 'riu_type', 'criticality', 'description',
             'scoring_mode', 'scoring_rule', 'rationale'}
STATUSES = {'draft', 'method-audited', 'human-reviewed', 'frozen'}


def require(condition, context, message):
    if not condition:
        raise ValueError(f'{context}: {message}')


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def exact_keys(value, expected, context):
    require(isinstance(value, dict), context, 'expected an object')
    require(set(value) == expected, context,
            f'field mismatch: missing {sorted(expected-set(value))}, extra {sorted(set(value)-expected)}')


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'duplicate JSON key {key}')
        result[key] = value
    return result


def read_jsonl(path):
    rows = []
    for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        require(bool(line.strip()), f'{path.name}:{number}', 'blank record')
        try:
            rows.append(json.loads(line, object_pairs_hook=no_duplicate_keys))
        except ValueError as exc:
            raise ValueError(f'{path.name}:{number}: {exc}') from exc
    return rows


CORPUS_VERSION = '0.3.1'
SUPERSEDED_BASELINE = 'dfbd25fe150baeec59065ab644737955c38eb94f'


def validate_freeze(root=ROOT, manifest=None):
    manifest = manifest or json.loads((root/'data/annotations/PROMPT_FREEZE.json').read_text(encoding='utf-8'))
    exact_keys(manifest, {'corpus_version', 'supersedes', 'algorithm', 'files'}, 'freeze')
    require(manifest['corpus_version'] == CORPUS_VERSION, 'freeze', 'unexpected corpus version')
    require(manifest['supersedes'] == {'corpus_version': '0.3', 'baseline_commit': SUPERSEDED_BASELINE}, 'freeze', 'unexpected superseded baseline')
    require(manifest['algorithm'] == 'sha256', 'freeze', 'unexpected hash algorithm')
    actual = {f.relative_to(root).as_posix(): hashlib.sha256(f.read_bytes()).hexdigest()
              for f in (root/'data/prompts').rglob('*') if f.is_file()}
    require(actual == manifest['files'], 'freeze', 'prompt file set or bytes changed')


def validate_record(rec, prompts):
    context = rec.get('task_id', 'UNKNOWN') if isinstance(rec, dict) else 'UNKNOWN'
    exact_keys(rec, REQUIRED, context)
    for field in REQUIRED - {'constraints', 'rius', 'prompt_sha256', 'review', 'task_checks'}:
        require(nonempty(rec[field]), context, f'{field} must be nonempty text')
    require(context in prompts, context, 'unknown task ID')
    prompt = prompts[context]
    for field in ['domain', 'difficulty']:
        require(rec[field] == prompt[field], context, f'{field} differs from frozen prompt')
    require(rec['schema_version'] == '0.2', context, 'unsupported schema version')
    require(rec['status'] in STATUSES, context, 'invalid review status')
    require(rec['safety_relevance'] in {'none', 'low', 'moderate', 'high'}, context, 'invalid safety relevance')
    require(rec['requirement_visibility'] in {'explicit', 'implicit', 'mixed'}, context, 'invalid visibility')
    exact_keys(rec['prompt_sha256'], {'en', 'bn', 'bn_cs'}, context)
    for lang in ['en', 'bn', 'bn_cs']:
        expected = hashlib.sha256(prompt['prompt_'+lang].encode('utf-8')).hexdigest()
        require(rec['prompt_sha256'][lang] == expected, context, f'{lang} prompt hash mismatch')
    exact_keys(rec['review'], {'method_review', 'independent_human_review', 'language_equivalence_review'}, context)
    review = rec['review']
    require(review['method_review'] in {'pending', 'agent-internal', 'human'}, context, 'invalid method reviewer')
    for field in ['independent_human_review', 'language_equivalence_review']:
        require(nonempty(review[field]), context, f'{field} requires pending or a review-log reference')
    if rec['status'] != 'draft':
        require(review['method_review'] != 'pending', context, 'review status exceeds evidence')
    if rec['status'] in {'human-reviewed', 'frozen'}:
        require(all(review[x] != 'pending' for x in ['independent_human_review', 'language_equivalence_review']), context, 'human/bilingual review evidence missing')
    require(isinstance(rec['constraints'], list) and all(nonempty(x) for x in rec['constraints']), context, 'invalid constraints')
    require(isinstance(rec['rius'], list) and len(rec['rius']) > 0, context, 'RIUs must be a nonempty list')
    descriptions = set()
    for number, unit in enumerate(rec['rius'], 1):
        loc = f'{context}/RIU-{number:02d}'
        exact_keys(unit, UNIT_KEYS, loc)
        require(unit['id'] == f'RIU-{number:02d}', loc, 'non-sequential or duplicate ID')
        require(unit['riu_type'] in TYPES, loc, 'invalid type')
        require(unit['criticality'] in {'critical', 'supporting'}, loc, 'invalid criticality')
        for field in ['description', 'rationale']:
            require(nonempty(unit[field]), loc, f'{field} must be nonempty text')
        normalized = ' '.join(unit['description'].casefold().split())
        require(normalized not in descriptions, loc, 'duplicate description')
        descriptions.add(normalized)
        sources = unit['source_riu_ids']
        require(isinstance(sources, list) and all(isinstance(x, str) and re.fullmatch(r'RIU-\d{2}', x) for x in sources), loc, 'invalid source RIU IDs')
        require(len(set(sources)) == len(sources), loc, 'duplicate source RIU IDs')
        require(unit['scoring_mode'] in {'binary', 'ordinal'}, loc, 'invalid scoring mode')
        exact_keys(unit['scoring_rule'], {'0', '0.5', '1'}, loc)
        rule = unit['scoring_rule']
        require(nonempty(rule['0']) and nonempty(rule['1']), loc, 'empty scoring anchors')
        require(rule['1'] == unit['description'], loc, 'description/full-credit anchor mismatch')
        if unit['scoring_mode'] == 'binary':
            require(rule['0.5'] is None, loc, 'binary unit cannot award half credit')
        else:
            require(nonempty(rule['0.5']) and rule['0.5'] not in {rule['0'], rule['1']}, loc, 'ordinal unit needs distinct partial anchor')
    expected_constraints = [u['description'] for u in rec['rius'] if u['riu_type'] == 'constraint']
    require(rec['constraints'] == expected_constraints, context, 'constraints drift from scored units')
    require(isinstance(rec['task_checks'], list) and len(rec['task_checks']) > 0, context, 'missing task checks')
    kinds = []
    for number, check in enumerate(rec['task_checks'], 1):
        exact_keys(check, {'id', 'kind', 'rule'}, context)
        require(check['id'] == f'CHECK-{number:02d}', context, 'non-sequential task check')
        require(check['kind'] in {'unsupported_content', 'format'}, context, 'invalid task check kind')
        require(nonempty(check['rule']), context, 'empty task check rule')
        kinds.append(check['kind'])
    require(kinds.count('unsupported_content') == 1 and len(kinds) == len(set(kinds)), context, 'duplicate or missing task check')
    if context == 'SYN091':
        require('format' in kinds, context, 'six-sentence format check missing')


def validate_records(records, prompts, scope='pilot'):
    for record in records:
        validate_record(record, prompts)
    ids = [r['task_id'] for r in records]
    require(len(ids) == len(set(ids)), scope, 'duplicate task IDs')
    if scope in {'pilot', 'full'}:
        expected = PILOT_IDS if scope == 'pilot' else set(prompts)
        require(set(ids) == expected, scope, 'task coverage mismatch')
    if scope == 'pilot':
        require(Counter(r['domain'] for r in records) == Counter(dict.fromkeys(DOMAINS, 5)), scope, 'domain coverage mismatch')
        for domain in DOMAINS:
            require({r['difficulty'] for r in records if r['domain'] == domain} == {'easy','medium','hard'}, domain, 'difficulty coverage mismatch')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scope', choices=['pilot', 'batch', 'full'], default='pilot')
    parser.add_argument('--annotation-dir', type=Path, default=ANN)
    args = parser.parse_args()
    validate_freeze()
    prompts = {r['task_id']:r for r in load_rows()}
    records = []
    paths = [args.annotation_dir/f for f in FILES] if args.scope == 'pilot' else sorted(args.annotation_dir.glob('*.jsonl'))
    require(bool(paths), args.scope, 'no annotation files')
    for index, path in enumerate(paths):
        file_rows = read_jsonl(path)
        if args.scope == 'pilot':
            require(len(file_rows) == 5, path.name, 'expected five tasks')
        for row in file_rows:
            validate_record(row, prompts)
            if args.scope == 'pilot':
                require(row['domain'] == DOMAINS[index], path.name, 'wrong domain file')
        records.extend(file_rows)
    require(bool(records), args.scope, 'no annotation records')
    validate_records(records, prompts, args.scope)
    units = [u for r in records for u in r['rius']]
    critical = sum(u['criticality'] == 'critical' for u in units)
    print(f'RIU {args.scope} validation PASSED: {len(records)} tasks; {len(units)} RIUs; {critical} critical ({critical/len(units):.1%})')
    print('Scoring modes:', dict(Counter(u['scoring_mode'] for u in units)))
    print('Review statuses:', dict(Counter(r['status'] for r in records)))
    print('Frozen prompt bytes verified. Structural PASS does not certify semantic or human review.')

if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as exc:
        raise SystemExit(f'Validation FAILED: {exc}')
