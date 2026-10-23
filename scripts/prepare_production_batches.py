"""Prepare/check outcome-independent production membership and draft review packets.

This does not generate annotations, accept gold, amend the historical queue, or
read model outcomes. Review sampling is fixed by this algorithm before drafting.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import math
import re
from pathlib import Path

from validate_pilot_annotations import read_jsonl, validate_freeze, validate_records
from validate_prompt_corpus import load_rows

ROOT = Path(__file__).resolve().parents[1]
ANN = ROOT / 'data/annotations'
TARGET = ANN / 'PRODUCTION_BATCHES_v0.1.json'
PACKETS = ANN / 'production_review'
BATCH_COUNT = 14
FIELDS = ('task_id', 'domain', 'subdomain', 'difficulty')
SAMPLE_SALT = 'production-review-v0.1-before-model-outcomes'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def encode(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


def build(root=ROOT):
    ann = root / 'data/annotations'
    queue_path = ann / 'SCALING_QUEUE.json'
    expansion_path = ann / 'EXPANSION_BATCHES.json'
    queue = json.loads(queue_path.read_text(encoding='utf-8'))
    expansion = json.loads(expansion_path.read_text(encoding='utf-8'))
    pilot = {r['task_id'] for r in queue['tasks'] if r['next_step'] == 'gold-frozen'}
    expanded = {r['task_id'] for b in expansion['batches'] for r in b['tasks']}
    if len(pilot) != 25 or len(expanded) != 132 or pilot & expanded:
        raise ValueError('historical 25 pilot / 132 expansion membership mismatch')
    tasks = [r for r in queue['tasks'] if r['task_id'] not in pilot | expanded]
    ids = [r['task_id'] for r in tasks]
    if len(ids) != 343 or len(set(ids)) != 343:
        raise ValueError('expected exactly 343 unique production task IDs')
    groups = defaultdict(list)
    for row in tasks:
        groups[(row['domain'], row['difficulty'])].append(row)
    batches = [[] for _ in range(BATCH_COUNT)]
    offset = 0
    for key in sorted(groups):
        group = sorted(groups[key], key=lambda r: (r['subdomain'], r['task_id']))
        for index, row in enumerate(group):
            batches[(offset + index) % BATCH_COUNT].append({f: row[f] for f in FIELDS})
        offset = (offset + len(group)) % BATCH_COUNT
    if sorted(map(len, batches)) != [24] * 7 + [25] * 7:
        raise ValueError('unexpected production batch sizes')
    return {
        'schema_version': '0.1',
        'version': 'production-draft-plan-0.1',
        'status': 'draft-preparation-only-pending-production-protocol-and-human-approval',
        'corpus_version': '0.3.1',
        'source_files_sha256': {
            'data/annotations/SCALING_QUEUE.json': digest(queue_path),
            'data/annotations/EXPANSION_BATCHES.json': digest(expansion_path),
        },
        'historical_queue_unchanged': True,
        'exclusion_counts': {'pilot': len(pilot), 'accepted_expansion': len(expanded)},
        'task_count': len(tasks), 'batch_count': BATCH_COUNT, 'maximum_batch_size': 25,
        'assignment_rule': ('Exclude the original 25 pilot and 132 prospectively assigned expansion tasks. '
                            'Group remaining tasks by domain/difficulty in lexical order; sort each '
                            'group by subdomain/task_id. Distribute round-robin to 14 batches using '
                            'a continuing rotating offset. No response or model outcome input.'),
        'review_sampling': {
            'mandatory': 'Every critical RIU, every identified ambiguity, and every task-level language-equivalence/coverage check.',
            'ordinary_strata': ['domain', 'difficulty', 'scoring_mode'],
            'ordinary_fraction_minimum': 0.2,
            'selection': 'Within each stratum of supporting RIUs select ceil(n/5), ranked by SHA-256(salt|batch_id|task_id|riu_id).',
            'salt': SAMPLE_SALT,
            'sampling_is_not_acceptance': True,
            'escalation': ('A systematic rule error requires review of every affected unit in the batch '
                           'and other drafted batches, including units outside the ordinary sample. '
                           'Log scope, rule, affected IDs, revisions and resolution; rerun validation '
                           'and regenerate packets before independent acceptance. No silent frozen edits.'),
        },
        'batches': [{
            'batch_id': f'P{i+1:02d}', 'task_count': len(batch),
            'domain_counts': dict(sorted(Counter(r['domain'] for r in batch).items())),
            'difficulty_counts': dict(sorted(Counter(r['difficulty'] for r in batch).items())),
            'tasks': batch,
        } for i, batch in enumerate(batches)],
    }


def ordinary_sample(records, batch_id):
    """Sample independently of ambiguity labels and unit content/outcomes."""
    strata = defaultdict(list)
    for record in records:
        for unit in record['rius']:
            if unit['criticality'] == 'supporting':
                key = (record['domain'], record['difficulty'], unit['scoring_mode'])
                strata[key].append((record['task_id'], unit['id']))
    selected = set()
    counts = []
    for key, units in sorted(strata.items()):
        ordered = sorted(units, key=lambda pair: hashlib.sha256(
            '|'.join((SAMPLE_SALT, batch_id, *pair)).encode()).hexdigest())
        take = math.ceil(len(units) / 5)
        selected.update(ordered[:take])
        counts.append({'stratum': dict(zip(('domain', 'difficulty', 'scoring_mode'), key)),
                       'ordinary_units': len(units), 'selected_units': take})
    return selected, counts


def packet(batch, records, prompts, ambiguity_data, revision="0.3"):
    batch_id = batch['batch_id']
    actual = {r['task_id'] for r in records}
    expected = {r['task_id'] for r in batch['tasks']}
    if actual != expected:
        raise ValueError(f'{batch_id}: missing/extra draft tasks: {sorted(expected-actual)} / {sorted(actual-expected)}')
    validate_records(records, prompts, 'batch')
    for record in records:
        if record['status'] != 'draft' or record['review'] != {
            'method_review': 'agent-internal', 'independent_human_review': 'pending',
            'language_equivalence_review': 'pending'}:
            raise ValueError(f'{record["task_id"]}: production preparation must remain an explicitly pending draft')
    if set(ambiguity_data) != actual:
        raise ValueError(f'{batch_id}: each task needs an explicit ambiguity/boundary checklist')
    sample, strata = ordinary_sample(records, batch_id)
    all_units = {(r['task_id'], u['id']) for r in records for u in r['rius']}
    ambiguities = set()
    for task_id, issues in ambiguity_data.items():
        if not isinstance(issues, list):
            raise ValueError(f'{task_id}: ambiguity list required')
        for issue in issues:
            if set(issue) != {'riu_ids', 'issue'} or not issue['issue'].strip():
                raise ValueError(f'{task_id}: malformed ambiguity/boundary issue')
            for unit_id in issue['riu_ids']:
                if (task_id, unit_id) not in all_units:
                    raise ValueError(f'{task_id}/{unit_id}: unknown ambiguity unit')
                ambiguities.add((task_id, unit_id))
    rows = []
    for record in sorted(records, key=lambda r: r['task_id']):
        task_id = record['task_id']
        for unit in record['rius']:
            pair = (task_id, unit['id'])
            reasons = []
            if unit['criticality'] == 'critical':
                reasons.append('all-critical')
            if pair in ambiguities:
                reasons.append('identified-ambiguity-or-boundary')
            if pair in sample:
                reasons.append('prespecified-ordinary-sample')
            rows.append({'task_id': task_id, 'riu_id': unit['id'], 'review_reasons': reasons,
                         'independent_review_status': 'pending', 'reviewer': None,
                         'decision': None, 'reviewed_at': None})
    manifest = {
        'version': 'production-review-packet-' + revision, 'batch_id': batch_id,
        'production_plan_sha256': digest(TARGET),
        'ambiguity_input_sha256': hashlib.sha256(encode(ambiguity_data).encode('utf-8')).hexdigest(),
        'status': 'pending-independent-human-and-language-review',
        'draft_sha256': {f'data/annotations/production/{batch_id}/{p.name}': digest(p)
                         for p in sorted((ANN / 'production' / batch_id).glob('*.jsonl'))},
        'task_count': len(records), 'riu_count': len(rows),
        'critical_count': sum(u['criticality'] == 'critical' for r in records for u in r['rius']),
        'ordinary_sample_count': len(sample), 'strata': strata,
        'mandatory_unit_review_count': sum(bool(r['review_reasons']) for r in rows),
        'human_reviewed_count': 0, 'approved_count': 0,
        'ambiguities_and_boundary_questions': ambiguity_data,
        'unit_checklist': rows,
        'escalation': build()['review_sampling']['escalation'],
    }
    lines = [f'# {batch_id} independent review packet', '',
             'Status: pending. AI-produced draft annotations; no human acceptance is claimed.', '',
             'Each task needs bilingual equivalence and full-prompt coverage review. Review all critical units, '
             'all ambiguity/boundary questions below, and every prespecified ordinary sample item. '
             'Additional ordinary units may be reviewed. Blank identity/decision fields are intentional.', '',
             f'{len(records)} tasks; {len(rows)} RIUs; {manifest["critical_count"]} critical; '
             f'{len(sample)} ordinary sample units; {manifest["mandatory_unit_review_count"]} mandatory unit reviews.', '',
             '## Reviewer procedure', '',
             '- [ ] Record validator identity, EN/BN competence, actual date and draft hashes in a new review log.',
             '- [ ] For every task compare EN, BN and BN-CS facts, quantities, constraints and requested output.',
             '- [ ] Check complete coverage, atomicity/overlap, omission-consequence rationale and alternative valid paths.',
             '- [ ] Review each marked critical/ambiguity/sample unit and its zero/full/half anchors.',
             '- [ ] Apply protocol 0.3 silence, conditional safeguard, contradiction and CHECK-01 rules.',
             '- [ ] Record disputes per task/RIU, proposed change, resolution and adjudicator; leave unresolved items pending.',
             '- [ ] Escalate systematic rule errors to every affected unit, including other batches; revalidate revisions.',
             '- [ ] Obtain explicit validator and study-lead acceptance before any status promotion or gold assembly.', '',
             'Ordinary sampling: ceil(n/5) per domain/difficulty/scoring-mode stratum of supporting RIUs, '
             'ranked by prespecified SHA-256. See the JSON packet for exact selections and counts.', '',
             '## Escalation', '', manifest['escalation'], '']
    by_task = {r['task_id']: r for r in records}
    for task_id in sorted(actual):
        record = by_task[task_id]
        lines += [f'## {task_id}', '', f'{record["domain"]}; {record["difficulty"]}.', '']
        for lang in ('en', 'bn', 'bn_cs'):
            lines += [f'### {lang}', '', prompts[task_id]['prompt_' + lang], '']
        lines += ['### Boundary and ambiguity questions', '']
        issues = ambiguity_data[task_id]
        lines += [f'- [ ] {", ".join(issue["riu_ids"]) or "Task-level"}: {issue["issue"]}' for issue in issues]
        if not issues:
            lines += ['- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.']
        lines += ['', '### RIU checklist', '']
        for unit in record['rius']:
            row = next(r for r in rows if r['task_id'] == task_id and r['riu_id'] == unit['id'])
            reasons = ', '.join(row['review_reasons']) or 'ordinary, outside prespecified sample'
            lines += [f'- [ ] **{unit["id"]}** ({unit["criticality"]}; {reasons}): {unit["description"]}',
                      f'  Rationale: {unit["rationale"]}',
                      f'  Anchors: 0 = {unit["scoring_rule"]["0"]}; 1 = description above.']
            if unit['scoring_mode'] == 'ordinal':
                lines += [f'  0.5 = {unit["scoring_rule"]["0.5"]}']
        lines += ['', 'Draft notes: ' + record['notes'], '', 'Task checks:', '']
        lines += [f'- [ ] {c["id"]}: {c["rule"]}' for c in record['task_checks']]
        lines += ['']
    return manifest, '\n'.join(lines)


def update(path, content, check):
    if check:
        if not path.is_file() or path.read_text(encoding='utf-8') != content:
            raise ValueError(f'missing/stale {path.relative_to(ROOT)}')
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.is_file() and path.read_text(encoding='utf-8') == content:
            return
        if path.exists():
            raise ValueError(f'refusing to overwrite different existing {path.relative_to(ROOT)}; '
                             'preserve review evidence and use a new version/revision')
        path.write_text(content, encoding='utf-8', newline='\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--packets', action='store_true', help='Prepare/check packets for complete drafted batches only.')
    parser.add_argument('--packet-revision', default='0.3', help='New version required if existing packet bytes differ.')
    args = parser.parse_args()
    if not re.fullmatch(r'[0-9]+\.[0-9]+', args.packet_revision):
        raise ValueError('packet revision must be a numeric major.minor version')
    validate_freeze()
    plan = build()
    update(TARGET, encode(plan), args.check)
    print('Production plan verified: 343 tasks, 14 batches (seven x 25, seven x 24), no historical mutation.')
    if args.packets:
        prompts = {r['task_id']: r for r in load_rows()}
        drafted = 0
        production = ANN / 'production'
        known_batches = {b['batch_id'] for b in plan['batches']}
        if production.exists() and any(p.name not in known_batches for p in production.iterdir()):
            raise ValueError('unexpected production path outside the prespecified batches')
        for batch in plan['batches']:
            directory = ANN / 'production' / batch['batch_id']
            if not directory.exists():
                continue
            records = []
            for path in sorted(directory.iterdir()):
                if path.suffix != '.jsonl' or not path.is_file():
                    raise ValueError(f'{directory}: annotation directories must contain only JSONL files')
                file_rows = read_jsonl(path)
                if any(r['domain'] != path.stem for r in file_rows):
                    raise ValueError(f'{path}: wrong domain placement')
                records.extend(file_rows)
            ambiguity_path = PACKETS / (batch['batch_id'] + '_ambiguities.json')
            ambiguity_data = json.loads(ambiguity_path.read_text(encoding='utf-8'))
            manifest, markdown = packet(batch, records, prompts, ambiguity_data, args.packet_revision)
            update(PACKETS / (batch['batch_id'] + '_packet_v' + args.packet_revision + '.json'), encode(manifest), args.check)
            update(PACKETS / (batch['batch_id'] + '_packet_v' + args.packet_revision + '.md'), markdown, args.check)
            drafted += len(records)
            print(f'{batch["batch_id"]}: {len(records)} machine-validated drafts, '
                  f'{manifest["riu_count"]} RIUs, {manifest["mandatory_unit_review_count"]} mandatory unit reviews; '
                  '0 human-reviewed / 0 approved.')
        print(f'Total: {drafted} drafted/validated, {343-drafted} not drafted; all 343 pending human approval.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as exc:
        raise SystemExit(f'Production preparation FAILED: {exc}')
