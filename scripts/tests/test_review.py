import copy
import unittest

from helpers import common, rating


class ReviewTest(unittest.TestCase):
    def score(self):
        before, after = rating('RIU-01', 0, 'insufficient'), rating('RIU-01', 1)
        return {'response_sha256': 'abc', 'ratings': [after], 'reviews': [
            {'reviewer': 'Codex', 'reviewed_at_utc': '2026-10-31T12:00:00Z', 'response_sha256': 'abc',
             'changes': [{'original_rating': before, 'corrected_rating': copy.deepcopy(after), 'rationale': 'Evidence meets anchor.'}]}]}

    def test_initial_ratings_recovered_without_mutating_corrected_scores(self):
        score = self.score()
        self.assertEqual(common.initial_ratings(score)[0]['score'], 0)
        self.assertEqual(score['ratings'][0]['score'], 1)

    def test_review_on_different_response_rejected(self):
        score = self.score()
        score['reviews'][0]['response_sha256'] = 'different'
        with self.assertRaises(ValueError):
            common.initial_ratings(score)

    def test_unrecorded_rating_change_rejected(self):
        score = self.score()
        score['ratings'][0]['score'] = .5
        with self.assertRaises(ValueError):
            common.initial_ratings(score)

    def test_duplicate_item_in_one_review_rejected(self):
        score = self.score()
        score['reviews'][0]['changes'] *= 2
        with self.assertRaises(ValueError):
            common.initial_ratings(score)


if __name__ == '__main__':
    unittest.main()
