import unittest
from unittest import mock

from helpers import TempResults, common, step

gen = step('02_generate')


class OrderTest(unittest.TestCase):
    def test_order_reproduces_recorded_generation_order(self):
        for key in ('sol', 'qwen', 'gemma'):
            model = common.load_models()[key]
            recorded = sorted(common.read_jsonl(common.RESULTS / f'responses/{key}.jsonl'), key=lambda r: r['generated_at_utc'])
            self.assertEqual([(c['task_id'], c['language']) for c in gen.ordered_cells(model)],
                             [(r['task_id'], r['language']) for r in recorded])


class OpenAIClientTest(unittest.TestCase):
    def setUp(self):
        self.client = gen.OpenAIModel(common.load_models()['sol'], common.load_study())

    def payload(self, status='completed', reason=None):
        return {'status': status, 'model': 'gpt-6.1-sol', 'incomplete_details': {'reason': reason} if reason else None,
                'output': [{'type': 'message', 'content': [{'type': 'output_text', 'text': 'answer'}]}],
                'usage': {'input_tokens': 10, 'output_tokens': 5}}

    def test_request_uses_study_settings(self):
        with mock.patch.object(gen, 'openai_responses', return_value=self.payload()) as call:
            out = self.client.generate('hello')
        body = call.call_args[0][0]
        self.assertEqual((body['instructions'], body['max_output_tokens']), ("Answer the user's request directly.", 32768))
        self.assertEqual((out['response_text'], out['truncated']), ('answer', False))

    def test_truncation_flag(self):
        with mock.patch.object(gen, 'openai_responses', return_value=self.payload('incomplete', 'max_output_tokens')):
            self.assertTrue(self.client.generate('hello')['truncated'])

    def test_substituted_model_rejected(self):
        with mock.patch.object(gen, 'openai_responses', return_value={**self.payload(), 'model': 'other'}):
            with self.assertRaises(RuntimeError):
                self.client.generate('hello')


class FakeClient:
    def __init__(self, *args, fail_on=()):
        self.fail_on = fail_on

    def generate(self, prompt):
        if prompt in self.fail_on:
            raise RuntimeError('boom')
        return {'response_text': 'r:' + prompt[:10], 'returned_model': 'gpt-6.1-sol', 'finish_status': 'completed',
                'truncated': False, 'usage': {'input_tokens': 1, 'output_tokens': 1}}


class RunTest(unittest.TestCase):
    def test_run_resumes_and_logs_failures(self):
        model = common.load_models()['sol']
        cells = gen.ordered_cells(model)
        with TempResults(gen, copy=()) as tmp, mock.patch.object(gen, 'load_env'), \
                mock.patch.dict('os.environ', {'OPENAI_API_KEY': 'x'}), \
                mock.patch.object(gen, 'OpenAIModel', lambda *a: FakeClient(fail_on={cells[1]['prompt_text']})):
            self.assertEqual(gen.run(model, limit=3), 3)
            self.assertEqual(len(common.read_jsonl(tmp / 'responses/sol.errors.jsonl')), 1)
            self.assertEqual(len(gen.pending(model)), len(cells) - 3)
            gen.run(model, limit=2)
            done = common.read_jsonl(tmp / 'responses/sol.jsonl')
            self.assertEqual(len(done), 5)
            self.assertEqual(len({(r['task_id'], r['language']) for r in done}), 5)


if __name__ == '__main__':
    unittest.main()
