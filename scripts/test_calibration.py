"""Tests for calibration fixtures and agreement; synthetic placeholders only, never real fixtures."""
import contextlib
import csv
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from calibration import (CAL, FIXTURE_FIELDS, SHEET_FIELDS, agreement, check, cohen_kappa,
                         krippendorff_alpha, sheets)


class StatisticTests(unittest.TestCase):
    def test_hand_computed_values(self):
        pairs = [(0, 0), (1, 1), (0, 1), (1, 0)]
        self.assertAlmostEqual(krippendorff_alpha(pairs), 0.125)
        self.assertAlmostEqual(cohen_kappa(pairs), 0.0)
        self.assertEqual(krippendorff_alpha([(0, 0), (1, 1)]), 1.0)

    def test_constant_labels_are_undefined_not_perfect(self):
        self.assertIsNone(krippendorff_alpha([(1, 1)] * 5))
        self.assertIsNone(cohen_kappa([(1, 1)] * 5))

    def test_ordinal_metric_penalizes_near_misses_less(self):
        pairs = [(0, 0)] * 4 + [(1, 1)] * 4 + [(0.5, 0.5)] * 4 + [(1, 0.5), (0, 0.5)]
        self.assertGreater(krippendorff_alpha(pairs, 'ordinal'), krippendorff_alpha(pairs, 'nominal'))


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.cal = Path(self.tmp.name)
        for name in ['fixture_plan.csv', 'answer_key.csv']: shutil.copy(CAL / name, self.cal / name)
        self.prereg({'set_by': 'Study lead', 'set_date': '2026-10-20', 'minimum': 0.667,
                     'decision_statistic': 'point_estimate'})
        self.write_fixtures('H1')

    def tearDown(self):
        self.tmp.cleanup()

    def prereg(self, values):
        base = json.loads((CAL / 'AGREEMENT_PREREG.json').read_text(encoding='utf-8'))
        (self.cal / 'AGREEMENT_PREREG.json').write_text(json.dumps({**base, **values}), encoding='utf-8')

    def write_fixtures(self, author):
        with open(CAL / 'fixture_plan.csv', encoding='utf-8') as f:
            ids = [row['fixture_id'] for row in csv.DictReader(f)]
        with open(self.cal / 'fixtures.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, FIXTURE_FIELDS); writer.writeheader()
            writer.writerows({'fixture_id': i, 'author_id': author, 'authored_date': '2026-10-21',
                              'response_text': 'placeholder\nsecond line'} for i in ids)

    def fill(self, rater, flip=None):
        path = self.cal / 'sheets' / f'{rater}_sheet.csv'
        with open(path, encoding='utf-8', newline='') as f: rows = list(csv.DictReader(f))
        reasons = {'0': 'omitted', '0.5': 'partial', '1': 'met'}
        for row in rows:
            levels = ['0', '0.5', '1'] if row['scoring_mode'] == 'ordinal' else ['0', '1']
            score = levels[sum(map(ord, row['fixture_id'] + row['item_id'])) % len(levels)]
            row.update(rating_date='2026-10-22', score=score,
                       reason='' if row['scoring_mode'] == 'check' else reasons[score])
            if flip and (row['fixture_id'], row['item_id']) == flip:
                row.update(score='0', reason='omitted') if score != '0' else row.update(score='1', reason='met')
        with open(path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, SHEET_FIELDS); writer.writeheader(); writer.writerows(rows)
        return path

    def run_quiet(self, fn, *args, **kwargs):
        out = io.StringIO()
        with contextlib.redirect_stdout(out): fn(*args, **kwargs)
        return out.getvalue()

    def test_blind_sheets_and_report(self):
        self.run_quiet(sheets, ['R2', 'R3'], cal=self.cal)
        packet = (self.cal / 'sheets' / 'R2_packet.md').read_text(encoding='utf-8')
        for hidden in ['phenomenon', 'partial_reasoning', 'conditional_safeguard', '(critical)', '(supporting)']:
            self.assertNotIn(hidden, packet)
        a, b = self.fill('R2'), self.fill('R3', flip=('F05', 'RIU-01'))
        report = self.run_quiet(agreement, a, b, cal=self.cal)
        self.assertIn('1 on critical units block', report)
        self.assertIn('| F05 | RIU-01 |', report)
        self.assertIn('MEETS', report)

    def test_threshold_set_after_rating_is_not_evaluated(self):
        self.prereg({'set_by': 'Study lead', 'set_date': '2026-10-23', 'minimum': 0.667,
                     'decision_statistic': 'point_estimate'})
        self.run_quiet(sheets, ['R2', 'R3'], cal=self.cal)
        report = self.run_quiet(agreement, self.fill('R2'), self.fill('R3'), cal=self.cal)
        self.assertIn('NOT EVALUATED', report)

    def test_rejections(self):
        self.write_fixtures('Claude')
        with self.assertRaisesRegex(ValueError, 'human-authored'): self.run_quiet(check, self.cal)
        self.write_fixtures('H1')
        self.run_quiet(sheets, ['R2', 'R3'], cal=self.cal)
        a = self.fill('R2')
        with self.assertRaisesRegex(ValueError, 'same rater'): self.run_quiet(agreement, a, a, cal=self.cal)
        unscored = self.cal / 'sheets' / 'R3_sheet.csv'
        with self.assertRaisesRegex(ValueError, 'date must be'): self.run_quiet(agreement, a, unscored, cal=self.cal)
        with self.assertRaisesRegex(ValueError, 'two distinct raters'): self.run_quiet(sheets, ['R2', 'R2'], cal=self.cal)


if __name__ == '__main__':
    unittest.main()
