"""Negative regression tests for the annotation gate; no models or model outputs."""
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from validate_pilot_annotations import (ANN, FILES, read_jsonl, validate_record,
    validate_records, validate_freeze, load_rows)

class AnnotationValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = [r for f in FILES for r in read_jsonl(ANN/f)]
        cls.prompts = {r['task_id']: r for r in load_rows()}

    def test_current_pilot(self):
        validate_records(self.records, self.prompts)
        validate_freeze()

    def test_invalid_records_rejected(self):
        mutations = {
            'missing field': lambda r: r.pop('rius'),
            'wrong type': lambda r: r.update(rius='text'),
            'empty text': lambda r: r.update(task_objective='  '),
            'unknown field': lambda r: r.update(typo=True),
            'unknown task': lambda r: r.update(task_id='TECH999'),
            'wrong domain': lambda r: r.update(domain='information_synthesis'),
            'wrong difficulty': lambda r: r.update(difficulty='hard'),
            'stale hash': lambda r: r['prompt_sha256'].update(bn='0'*64),
            'false review': lambda r: (r.update(status='frozen'), r['review'].update(independent_human_review='pending')),
            'duplicate ID': lambda r: r['rius'][1].update(id='RIU-01'),
            'missing anchor': lambda r: r['rius'][0]['scoring_rule'].pop('0'),
            'binary partial': lambda r: r['rius'][0]['scoring_rule'].update({'0.5':'vague'}),
            'ordinal missing partial': lambda r: r['rius'][1]['scoring_rule'].update({'0.5':None}),
            'empty rationale': lambda r: r['rius'][0].update(rationale=''),
            'bad criticality': lambda r: r['rius'][0].update(criticality='major'),
            'duplicate requirement': lambda r: r['rius'][1].update(description=r['rius'][0]['description']),
            'constraints drift': lambda r: r.update(constraints=[]),
            'missing checks': lambda r: r.update(task_checks=[]),
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name):
                row = copy.deepcopy(self.records[0]); mutate(row)
                with self.assertRaises(ValueError):
                    validate_record(row, self.prompts)

    def test_duplicate_and_missing_tasks(self):
        for rows in [self.records[:-1], self.records + [self.records[0]]]:
            with self.assertRaises(ValueError):
                validate_records(rows, self.prompts)

    def test_batch_and_full_are_distinct(self):
        validate_records(self.records[:1], self.prompts, 'batch')
        with self.assertRaises(ValueError):
            validate_records(self.records, self.prompts, 'full')

    def test_no_arbitrary_minimum_or_critical_quota(self):
        row = copy.deepcopy(self.records[0])
        row['rius'] = row['rius'][:1]
        row['constraints'] = []
        validate_record(row, self.prompts)

    def test_duplicate_json_key(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'bad.jsonl'
            path.write_text('{"task_id":"A","task_id":"B"}\n')
            with self.assertRaisesRegex(ValueError, 'duplicate JSON key'):
                read_jsonl(path)

    def test_frozen_bytes_and_file_set(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); folder = root/'data/prompts'; folder.mkdir(parents=True)
            path = folder/'example.csv'; path.write_bytes(b'frozen\n')
            manifest = {'corpus_version':'0.3', 'supersedes':{'corpus_version':'0.2', 'baseline_commit':'74604be07b2246e1d7f063088a35799721290e81'}, 'algorithm':'sha256',
                        'files':{'data/prompts/example.csv':hashlib.sha256(path.read_bytes()).hexdigest()}}
            validate_freeze(root, manifest)
            path.write_bytes(b'changed\n')
            with self.assertRaises(ValueError): validate_freeze(root, manifest)
            path.write_bytes(b'frozen\n'); (folder/'extra.csv').write_bytes(b'extra')
            with self.assertRaises(ValueError): validate_freeze(root, manifest)
            (folder/'extra.csv').unlink(); path.unlink()
            with self.assertRaises(ValueError): validate_freeze(root, manifest)

if __name__ == '__main__':
    unittest.main()
