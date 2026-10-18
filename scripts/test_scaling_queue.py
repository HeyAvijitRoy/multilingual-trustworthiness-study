"""Ensure scaling preparation covers the corpus without implying completed gold."""
from collections import Counter
import unittest
from prepare_scaling_queue import queue
from validate_pilot_annotations import PILOT_IDS
from validate_prompt_corpus import load_rows

class ScalingQueueTests(unittest.TestCase):
    def test_exact_coverage_and_metadata(self):
        result = queue()
        source = {r['task_id']:r for r in load_rows()}
        rows = result['tasks']
        self.assertEqual(len(rows), 500)
        self.assertEqual({r['task_id'] for r in rows}, set(source))
        self.assertEqual(Counter(r['annotation_status'] for r in rows),
                         Counter({'human-reviewed':25, 'not-annotated':475}))
        for row in rows:
            for field in ['domain', 'subdomain', 'difficulty']:
                self.assertEqual(row[field], source[row['task_id']][field])
        self.assertEqual(result, queue())

    def test_expansion_covers_missing_strata_once(self):
        rows = queue()['tasks']
        key = lambda r: (r['domain'], r['subdomain'], r['difficulty'])
        pilot = {key(r) for r in rows if r['task_id'] in PILOT_IDS}
        expected = {key(r) for r in rows} - pilot
        expansion = [r for r in rows if r['next_step'] == 'expansion-calibration']
        self.assertEqual({key(r) for r in expansion}, expected)
        self.assertEqual(len(expansion), len(expected))
        for selected in expansion:
            candidates = [r['task_id'] for r in rows if key(r) == key(selected)]
            self.assertEqual(selected['task_id'], min(candidates))

if __name__ == '__main__': unittest.main()
