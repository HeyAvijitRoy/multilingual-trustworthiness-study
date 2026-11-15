"""Check the robustness helpers on small synthetic inputs and the study counts they must reproduce."""
import unittest

from helpers import step

rb = step('08_robustness')


class HelperTest(unittest.TestCase):
    def test_ci_is_percentile_interval(self):
        lo, hi = rb.ci(list(range(1000)))
        self.assertEqual((lo, hi), (25, 974))

    def test_fixed_effect_recovers_language_shift_and_length_control(self):
        # BN lowers coverage by 0.1 in every task, independent of length.
        recs = {}
        for i, t in enumerate(['A', 'B', 'C', 'D']):
            base = 0.6 + 0.1 * i
            recs['m', t, 'en'] = {'crit_cov': base, 'words': 100 + 10 * i}
            recs['m', t, 'bn'] = {'crit_cov': base - 0.1, 'words': 80 + 10 * i}
        tasks = ['A', 'B', 'C', 'D']
        self.assertAlmostEqual(rb.fe_effect(tasks, recs, 'm', False), -0.1)
        self.assertAlmostEqual(rb.fe_effect(tasks, recs, 'm', True), -0.1, places=6)

    def test_fixed_effect_skips_tasks_without_critical_rius(self):
        recs = {('m', 'A', 'en'): {'crit_cov': None, 'words': 10}, ('m', 'A', 'bn'): {'crit_cov': None, 'words': 10},
                ('m', 'B', 'en'): {'crit_cov': 1.0, 'words': 10}, ('m', 'B', 'bn'): {'crit_cov': 0.5, 'words': 10}}
        self.assertAlmostEqual(rb.fe_effect(['A', 'B'], recs, 'm', False), -0.5)


class StudyCountTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.recs = rb.load_study_rows()
        cls.reasons = rb.reason_table(cls.recs)

    def test_every_cell_has_348_critical_judgments(self):
        for cell in self.reasons.values():
            self.assertEqual(cell['critical_judgments'], 348)

    def test_reason_counts_add_up_and_match_the_paper(self):
        for cell in self.reasons.values():
            parts = sum(cell[k] for k in ('partial', 'insufficient', 'incorrect', 'omitted', 'non_answer'))
            self.assertEqual(parts, cell['below_full'])
        q = self.reasons['qwen:bn']
        self.assertEqual((q['below_full'], q['omitted'], q['incorrect']), (67, 6, 19))
        self.assertEqual(self.reasons['qwen:en']['below_full'], 35)
        self.assertEqual(self.reasons['gemma:bn']['below_full'], 69)

    def test_token_premium_excludes_reasoning_and_bengali_costs_more_for_sol(self):
        p = rb.token_premium()
        self.assertGreater(p['sol|bn|input'], 1.5)
        self.assertGreater(p['qwen|bn|output_per_word'], 1.5)
        self.assertLess(p['gemma|bn|output'], 1.1)


if __name__ == '__main__':
    unittest.main()
