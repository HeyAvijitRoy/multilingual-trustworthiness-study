import unittest

from helpers import TempResults, step

judge = step('03_validate_judge')


class AssessTest(unittest.TestCase):
    def test_recorded_results_reproduce(self):
        with TempResults(judge):
            final = judge.assess('heldout')
            before = judge.assess('heldout', before_rerate=True)
            original = judge.assess('calibration', 'scoring-0.3')
        self.assertEqual((final['fixtures'], final['riu_items'], final['critical_riu_items'], final['safety_check_items']),
                         (88, 352, 183, 99))
        self.assertTrue(final['passes'])
        self.assertAlmostEqual(final['ordinal_alpha'], 0.9906, 4)
        self.assertEqual((final['critical_exact'], final['safety_exact']), (1.0, 1.0))
        self.assertFalse(before['passes'])
        self.assertEqual(round(before['safety_exact'] * 99), 95)
        self.assertEqual(round(original['safety_exact'] * 30), 25)
        self.assertAlmostEqual(original['ordinal_alpha'], 0.9605, 4)


if __name__ == '__main__':
    unittest.main()
