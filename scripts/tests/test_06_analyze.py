import unittest

from helpers import common, perfect_ratings, rating, step

analysis = step('06_analyze')
REC = {'task_id': 'T', 'rius': [
    {'id': 'RIU-01', 'criticality': 'critical', 'scoring_mode': 'binary', 'riu_type': 'action', 'description': 'a',
     'scoring_rule': {'0': 'x', '1': 'y', '0.5': None}, 'rationale': ''},
    {'id': 'RIU-02', 'criticality': 'critical', 'scoring_mode': 'ordinal', 'riu_type': 'action', 'description': 'b',
     'scoring_rule': {'0': 'x', '0.5': 'h', '1': 'y'}, 'rationale': ''},
    {'id': 'RIU-03', 'criticality': 'supporting', 'scoring_mode': 'binary', 'riu_type': 'action', 'description': 'c',
     'scoring_rule': {'0': 'x', '1': 'y', '0.5': None}, 'rationale': ''}],
    'task_checks': [{'id': 'CHECK-01', 'kind': 'unsupported_content', 'rule': 'r'}]}


class MetricsTest(unittest.TestCase):
    def test_perfect_response(self):
        m = analysis.response_metrics(REC, perfect_ratings(REC))
        self.assertEqual((m['riu_coverage'], m['critical_omission_rate'], m['strict_complete_task_success']), (1, 0, 1))

    def test_omission_versus_incorrect(self):
        m = analysis.response_metrics(REC, [rating('RIU-01', 0, 'omitted'), rating('RIU-02', 0, 'incorrect'),
                                            rating('RIU-03', 1), rating('CHECK-01', 1)])
        self.assertEqual(m['critical_omission_rate'], 0.5)
        self.assertEqual(m['critical_zero_rate'], 1.0)
        self.assertAlmostEqual(m['riu_coverage'], 1 / 3)

    def test_partial_credit_and_failed_check(self):
        m = analysis.response_metrics(REC, [rating('RIU-01', 1), rating('RIU-02', 0.5), rating('RIU-03', 1),
                                            rating('CHECK-01', 0)])
        self.assertEqual((m['critical_coverage'], m['critical_unmet_rate']), (0.75, 0.5))
        self.assertEqual((m['core_task_success'], m['unsupported_content_pass']), (0.0, 0.0))

    def test_non_answer_counts_as_omission(self):
        m = analysis.response_metrics(REC, [rating('RIU-01', 0, 'non_answer'), rating('RIU-02', 0, 'non_answer'),
                                            rating('RIU-03', 0, 'non_answer'), rating('CHECK-01', 1)])
        self.assertEqual((m['critical_omission_rate'], m['non_answer']), (1.0, 1.0))


class EffectTest(unittest.TestCase):
    def setUp(self):
        self.tasks = [{'task_id': f'{d}{i}', 'domain': d} for d in 'AB' for i in range(4)]
        self.rows = {}
        for t in self.tasks:
            for m, shift in (('x', 0.2), ('y', 0.0)):
                self.rows[m, t['task_id'], 'en'] = {'riu_coverage': 0.9}
                self.rows[m, t['task_id'], 'bn'] = {'riu_coverage': 0.9 - shift}

    def test_domain_equal_paired_effect(self):
        e = analysis.Stratum(self.tasks, 200).effect(self.rows, ['x', 'y'], 'riu_coverage', 'bn', 'en')
        self.assertAlmostEqual(e['by_model']['x'], -0.2)
        self.assertAlmostEqual(e['estimate'], -0.1)
        self.assertAlmostEqual(e['ci95'][0], -0.1)

    def test_missing_domain_makes_model_undefined(self):
        rows = {k: v for k, v in self.rows.items() if not (k[0] == 'y' and k[1].startswith('B'))}
        e = analysis.Stratum(self.tasks, 50).effect(rows, ['x', 'y'], 'riu_coverage', 'bn', 'en')
        self.assertIsNone(e['by_model']['y'])
        self.assertIsNone(e['estimate'])

    def test_bootstrap_is_deterministic(self):
        rows = dict(self.rows)
        rows['x', 'A0', 'bn'] = {'riu_coverage': 0.1}
        a = analysis.Stratum(self.tasks, 300).effect(rows, ['x', 'y'], 'riu_coverage', 'bn', 'en')
        b = analysis.Stratum(self.tasks, 300).effect(rows, ['x', 'y'], 'riu_coverage', 'bn', 'en')
        self.assertEqual(a['ci95'], b['ci95'])


class StudyAnalysisTest(unittest.TestCase):
    def test_primary_estimate_on_study_scores(self):
        report = analysis.analyze(replicates=200)
        self.assertEqual(report['models'], ['sol', 'qwen', 'gemma'])
        self.assertAlmostEqual(report['primary']['estimate'], 0.002575, 6)
        self.assertEqual(report['primary']['paired_tasks'], {'sol': 137, 'qwen': 137, 'gemma': 137})
        self.assertEqual(len(report['truncated_cells']), 2)


if __name__ == '__main__':
    unittest.main()
