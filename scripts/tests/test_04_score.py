import unittest
from unittest import mock

from helpers import TempResults, common, perfect_ratings, step

score = step('04_score')
ANNOTATIONS = common.load_annotations('gold')
USAGE = {'input_tokens': 1000, 'output_tokens': 100}


def fake_judge(prompt, judge):
    task_id = prompt.split('"task_id": "')[1].split('"')[0]
    return perfect_ratings(ANNOTATIONS[task_id]), {'usage': USAGE}


class ScoreRunTest(unittest.TestCase):
    def run_score(self, judge_fn, **kw):
        with mock.patch.object(score, 'call_judge', judge_fn), mock.patch.object(score, 'load_env'), \
                mock.patch.dict('os.environ', {'OPENAI_API_KEY': 'x'}):
            return score.run(['sol'], **kw)

    def test_scores_pending_responses_and_resumes(self):
        with TempResults(score, copy=('responses',)) as tmp:
            self.assertEqual(self.run_score(fake_judge, limit=4), 4)
            self.assertEqual(self.run_score(fake_judge, limit=2), 2)
            rows = common.read_jsonl(tmp / 'scores/sol.jsonl')
            self.assertEqual(len({(r['task_id'], r['language']) for r in rows}), 6)
            self.assertTrue(all(r['procedure'] == 'scoring-0.5' and r['cost_usd'] > 0 for r in rows))

    def test_invalid_ratings_are_logged_not_saved(self):
        def bad_judge(prompt, judge):
            ratings, meta = fake_judge(prompt, judge)
            return ratings[1:], meta
        with TempResults(score, copy=('responses',)) as tmp:
            self.assertEqual(self.run_score(bad_judge, limit=2), 0)
            self.assertEqual(common.read_jsonl(tmp / 'scores/sol.jsonl'), [])
            self.assertGreater(len(common.read_jsonl(tmp / 'scores/sol.errors.jsonl')), 0)

    def test_spend_cap_stops_the_run(self):
        with TempResults(score, copy=('responses',)):
            with self.assertRaises(RuntimeError):
                self.run_score(fake_judge, max_usd=0.01)


if __name__ == '__main__':
    unittest.main()
