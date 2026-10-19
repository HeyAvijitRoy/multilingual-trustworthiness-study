"""Tests for deterministic expansion-calibration batches."""
from collections import Counter
import unittest
from prepare_expansion_batches import build


class ExpansionBatchTests(unittest.TestCase):
    def test_exact_balanced_coverage(self):
        result = build()
        self.assertEqual(result['batch_count'], 6)
        self.assertEqual(result['expected_batch_size'], 22)
        self.assertEqual([b['task_count'] for b in result['batches']], [22] * 6)

        tasks = [t for b in result['batches'] for t in b['tasks']]
        self.assertEqual(len(tasks), 132)
        self.assertEqual(len({t['task_id'] for t in tasks}), 132)
        self.assertEqual(Counter(t['difficulty'] for t in tasks),
                         Counter({'easy': 44, 'medium': 44, 'hard': 44}))
        self.assertEqual(Counter(t['domain'] for t in tasks),
                         Counter({'technical_troubleshooting': 27,
                                  'cybersecurity_digital_safety': 27,
                                  'procedural_instructional': 27,
                                  'decision_support': 27,
                                  'information_synthesis': 24}))

    def test_reproducible(self):
        self.assertEqual(build(), build())


if __name__ == '__main__':
    unittest.main()
