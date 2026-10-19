"""Build/check deterministic balanced batches for the 132 expansion-calibration tasks."""
import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / 'data' / 'annotations' / 'SCALING_QUEUE.json'
TARGET = ROOT / 'data' / 'annotations' / 'EXPANSION_BATCHES.json'
BATCH_COUNT = 6
EXPECTED_SIZE = 22


def build():
    queue = json.loads(QUEUE.read_text(encoding='utf-8'))
    tasks = sorted(
        (row for row in queue['tasks'] if row['next_step'] == 'expansion-calibration'),
        key=lambda r: (r['domain'], r['difficulty'], r['subdomain'], r['task_id']))
    if len(tasks) != 132:
        raise ValueError(f'expected 132 expansion tasks, found {len(tasks)}')

    groups = defaultdict(list)
    for row in tasks:
        groups[(row['domain'], row['difficulty'])].append(row)

    batches = [[] for _ in range(BATCH_COUNT)]
    offset = 0
    for key in sorted(groups):
        group = groups[key]
        for i, row in enumerate(group):
            batches[(offset + i) % BATCH_COUNT].append(row)
        offset = (offset + len(group)) % BATCH_COUNT

    if any(len(batch) != EXPECTED_SIZE for batch in batches):
        raise ValueError(f'expected six {EXPECTED_SIZE}-task batches, found {[len(b) for b in batches]}')

    seen = [row['task_id'] for batch in batches for row in batch]
    if len(seen) != len(set(seen)) or set(seen) != {row['task_id'] for row in tasks}:
        raise ValueError('batch assignment has duplicate or missing tasks')

    return {
        'schema_version': '0.1',
        'source_queue': 'data/annotations/SCALING_QUEUE.json',
        'source_gate': queue['gate'],
        'status': 'planned-not-annotated',
        'batch_count': BATCH_COUNT,
        'expected_batch_size': EXPECTED_SIZE,
        'assignment_rule': ('Select the 132 predeclared expansion-calibration tasks, sort within '
                            'domain/difficulty groups by domain, difficulty, subdomain and task_id, '
                            'then distribute each domain/difficulty group round-robin across six '
                            'batches with a rotating offset.'),
        'batches': [{
            'batch_id': f'E{i+1}',
            'task_count': len(batch),
            'domain_counts': dict(sorted(Counter(r['domain'] for r in batch).items())),
            'difficulty_counts': dict(sorted(Counter(r['difficulty'] for r in batch).items())),
            'tasks': [{k: r[k] for k in ['task_id', 'domain', 'subdomain', 'difficulty']}
                      for r in batch],
        } for i, batch in enumerate(batches)]
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    result = build()
    encoded = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.check:
        if not TARGET.exists() or TARGET.read_text(encoding='utf-8') != encoded:
            raise SystemExit('Expansion batches are missing or stale; run scripts/prepare_expansion_batches.py')
    else:
        TARGET.write_text(encoded, encoding='utf-8', newline='\n')
    print('Expansion batches verified:', result['batch_count'], 'batches x',
          result['expected_batch_size'], 'tasks')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as exc:
        raise SystemExit(f'Expansion batch preparation FAILED: {exc}')
