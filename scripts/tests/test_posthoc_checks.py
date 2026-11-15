"""Tests for the post hoc checks: reason-code packet blinding (step 09) and thinking-trace handling (step 10)."""
import importlib.util
import json
import random
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ReasonCheckTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rc = load('reason_check', '09_reason_check.py')
        cls.rows = cls.rc.draw(cls.rc.candidates(), random.Random(cls.rc.SEED))

    def test_one_item_per_response_and_quota(self):
        keys = [(r['model'], r['task_id'], r['language']) for r in self.rows]
        self.assertEqual(len(keys), len(set(keys)))
        for r in self.rows:
            self.assertEqual(r['unit']['criticality'], 'critical')
            self.assertIn(r['judge_reason'], self.rc.QUOTA)

    def test_packet_is_blind(self):
        items = [self.rc.packet_item(i + 1, r) for i, r in enumerate(self.rows)]
        page = self.rc.render_packet(items)
        payload = json.dumps(items)
        for leak in ('judge_score', 'judge_reason', '"model"', 'qwen', 'gemma'):
            self.assertNotIn(leak, payload)
        self.assertIn('Download ratings CSV', page)

    def test_kappa(self):
        self.assertEqual(self.rc.kappa(['a', 'b', 'a', 'b'], ['a', 'b', 'a', 'b']), 1.0)
        self.assertAlmostEqual(self.rc.kappa(['a', 'a', 'b', 'b'], ['a', 'b', 'a', 'b']), 0.0)


class ThinkingSubsetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.th = load('thinking_subset', '10_thinking_subset.py')

    def test_split_thinking(self):
        special = ['<|im_end|>', '<eos>']
        self.assertEqual(self.th.split_thinking('<think>\nplan\n</think>\n\nAnswer.<|im_end|>', special), ('plan', 'Answer.', True))
        self.assertEqual(self.th.split_thinking('<|channel>thought\nplan<channel|>Answer<eos>', special), ('plan', 'Answer', True))
        self.assertEqual(self.th.split_thinking('<think>runs out', special), ('runs out', '', False))
        self.assertEqual(self.th.split_thinking('Direct answer<eos>', special), ('', 'Direct answer', True))

    def test_subset_is_seeded_and_stratified(self):
        tasks = self.th.subset_tasks()
        self.assertEqual(tasks, self.th.subset_tasks())
        self.assertEqual(len(tasks), 30)
        self.assertEqual(len(set(tasks)), 30)


if __name__ == '__main__':
    unittest.main()
