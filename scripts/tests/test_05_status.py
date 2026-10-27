import json
import unittest

from helpers import TempResults, common, step

status = step('05_status')


class StatusTest(unittest.TestCase):
    def test_study_results_pass_integrity(self):
        with TempResults(status) as tmp:
            self.assertEqual(status.main(), 0)
            report = json.loads((tmp / 'status.json').read_text())
            self.assertEqual(report['problems'], [])
            self.assertEqual([report['models'][k]['scored'] for k in ('sol', 'qwen', 'gemma')], [471, 471, 471])
            self.assertIn('pending', (tmp / 'STATUS.md').read_text())

    def test_tampered_response_is_detected(self):
        with TempResults(status) as tmp:
            path = tmp / 'responses/qwen.jsonl'
            rows = common.read_jsonl(path)
            rows[0]['response_text'] += ' edited'
            path.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
            self.assertEqual(status.main(), 1)
            problems = json.loads((tmp / 'status.json').read_text())['problems']
            self.assertTrue(any('response text changed' in p for p in problems))

    def test_missing_primary_cell_is_detected(self):
        with TempResults(status) as tmp:
            path = tmp / 'responses/gemma.jsonl'
            rows = common.read_jsonl(path)[1:]
            path.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
            self.assertEqual(status.main(), 1)


if __name__ == '__main__':
    unittest.main()
