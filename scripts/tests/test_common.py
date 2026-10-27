import json
import tempfile
import unittest
from pathlib import Path

from helpers import common, perfect_ratings, rating


class AgreementTest(unittest.TestCase):
    def test_perfect_agreement_is_one(self):
        self.assertEqual(common.krippendorff_alpha([(0, 0), (1, 1), (0.5, 0.5), (1, 1)]), 1.0)

    def test_no_variation_is_undefined(self):
        self.assertIsNone(common.krippendorff_alpha([(1, 1), (1, 1)]))

    def test_disagreement_lowers_alpha(self):
        self.assertLess(common.krippendorff_alpha([(0, 1), (1, 0), (0, 0), (1, 1)]), 0.5)


class RatingValidationTest(unittest.TestCase):
    def setUp(self):
        self.rec = next(iter(common.load_annotations('gold').values()))

    def test_perfect_ratings_pass(self):
        common.validate_ratings(self.rec, perfect_ratings(self.rec))

    def test_missing_item_rejected(self):
        with self.assertRaises(ValueError):
            common.validate_ratings(self.rec, perfect_ratings(self.rec)[1:])

    def test_reason_must_match_score(self):
        bad = perfect_ratings(self.rec)
        bad[0] = rating(bad[0]['item_id'], 1, 'omitted')
        with self.assertRaises(ValueError):
            common.validate_ratings(self.rec, bad)

    def test_half_credit_rejected_on_binary(self):
        binary = next(r for r in self.rec['rius'] if r['scoring_mode'] == 'binary')
        bad = [rating(binary['id'], 0.5, 'partial') if r['item_id'] == binary['id'] else r for r in perfect_ratings(self.rec)]
        with self.assertRaises(ValueError):
            common.validate_ratings(self.rec, bad)

    def test_boolean_score_rejected(self):
        bad = perfect_ratings(self.rec)
        bad[0]['score'] = True
        with self.assertRaises(ValueError):
            common.validate_ratings(self.rec, bad)


class JudgePromptTest(unittest.TestCase):
    def test_requirement_form(self):
        self.assertEqual(common.requirement_form({'riu_type': 'constraint', 'description': 'Do not delete the backup.'}),
                         'negative_or_conditional')
        self.assertEqual(common.requirement_form({'riu_type': 'constraint', 'description': 'Keep a backup.'}), 'affirmative')
        self.assertEqual(common.requirement_form({'riu_type': 'action', 'description': 'Do not reboot.'}), 'affirmative')

    def test_prompt_contains_rubric_but_no_model_identity(self):
        rec = next(iter(common.load_annotations('gold').values()))
        prompt = common.scoring_prompt(rec['task_id'], 'PROMPT', 'RESPONSE', rec)
        payload = json.loads(prompt.split('TASK_AND_RUBRIC_JSON:\n')[1])
        self.assertEqual([i['item_id'] for i in payload['items']],
                         [r['id'] for r in rec['rius']] + [c['id'] for c in rec['task_checks']])
        self.assertNotIn('model', payload)


class FilesTest(unittest.TestCase):
    def test_unterminated_record_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / 'x.jsonl'
            path.write_text('{"a": 1}\n{"a": 2}')
            with self.assertRaises(RuntimeError):
                common.read_jsonl(path)

    def test_append_then_read(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / 'x.jsonl'
            common.append_jsonl(path, {'text': 'বাংলা line'})
            self.assertEqual(common.read_jsonl(path), [{'text': 'বাংলা line'}])

    def test_cost(self):
        self.assertEqual(common.cost_usd('gpt-5.4-2026-03-05', {'input_tokens': 1_000_000, 'output_tokens': 0}), 2.5)
        self.assertEqual(common.cost_usd('Qwen/Qwen3.5-9B', {'input_tokens': 10, 'output_tokens': 10}), 0.0)


if __name__ == '__main__':
    unittest.main()
