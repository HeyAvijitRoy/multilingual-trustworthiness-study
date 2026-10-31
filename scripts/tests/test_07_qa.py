"""Ensure QA reports the intended check instead of pooling format checks into it."""
import unittest

from helpers import step

qa = step('07_qa')


class QACheckTest(unittest.TestCase):
    def test_format_agreement_does_not_inflate_check01(self):
        rows = [
            {'kind': 'task_check', 'item_id': 'CHECK-01', 'critical': False, 'qa': 0, 'judge': 1},
            {'kind': 'task_check', 'item_id': 'CHECK-02', 'critical': False, 'qa': 1, 'judge': 1},
        ]
        a = qa.agreement(rows)
        self.assertEqual((a['check01_items'], a['check01_exact']), (1, 0))
        self.assertEqual((a['format_check_items'], a['format_check_exact']), (1, 1))
        self.assertEqual((a['check_items'], a['check_exact']), (2, .5))

    def test_study_counts_and_report(self):
        rows = qa.load_rows()
        a = qa.agreement(rows)
        self.assertEqual(a['check01_items'], 60)
        self.assertAlmostEqual(a['check01_exact'], 56 / 60)
        self.assertEqual(a['check_items'], 62)
        self.assertAlmostEqual(a['check_exact'], 58 / 62)
        self.assertEqual((a['format_check_items'], a['format_check_exact']), (2, 1))

    def test_no_check01_is_undefined(self):
        a = qa.agreement([{'kind': 'task_check', 'item_id': 'CHECK-02',
                           'critical': False, 'qa': 1, 'judge': 1}])
        self.assertIsNone(a['check01_exact'])


if __name__ == '__main__':
    unittest.main()
