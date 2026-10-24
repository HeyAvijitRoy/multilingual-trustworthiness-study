"""Offline checks for the generation supervisor's refusal rules and accounting."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import generation_supervisor_v04 as s


def state(worker='paused',alive=True,lock=None,in_flight=(),remaining=5):
    return {'controller':{'alive':alive,'workers':{'google':{'state':worker}}},
            'locks':{'google.lock':lock,'openai.lock':None},
            'partitions':{'google':{'remaining':remaining,'in_flight':list(in_flight)},'openai':{'remaining':remaining,'in_flight':[]}}}


class SupervisorTests(unittest.TestCase):
    def test_refuses_while_controller_worker_active(self):
        for w in ('collecting','quota_wait'):self.assertIn('not recorded as paused',s.resumable('google',state(w)))
    def test_allows_only_recorded_pause_or_dead_controller(self):
        self.assertIsNone(s.resumable('google',state('paused')))
        self.assertIsNone(s.resumable('google',state('collecting',alive=False)))
    def test_never_bypasses_locks_or_in_flight_or_completion(self):
        self.assertIn('live process',s.resumable('google',state(lock={'holder_alive':True})))
        self.assertIn('never removed',s.resumable('google',state(lock={'holder_alive':False})))
        self.assertIn('in-flight',s.resumable('google',state(in_flight=[{'task_id':'X'}])))
        self.assertIn('complete',s.resumable('google',state(remaining=0)))
    def test_local_gpu_phases_not_resumable(self):
        self.assertIn('cloud',s.resumable('local_b',state()))
    def test_partition_accounting_detects_exhausted_and_in_flight(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d);(out/'attempts').mkdir()
            ok={'task_id':'A','language':'en','status':'success','generated_at_utc':'2026-10-24T00:00:00Z','latency_seconds':3,'response_text':'x'}
            (out/'google.jsonl').write_text(json.dumps(ok)+'\n'+json.dumps({**ok,'task_id':'B','status':'api_error'})+'\n')
            events=[]
            for n in range(1,5):
                events+=[{'attempt_id':f'b{n}','task_id':'B','language':'en','attempt':n,'status':'started','started_at_utc':'2026-10-24T00:00:00Z'},
                         {'attempt_id':f'b{n}','task_id':'B','language':'en','attempt':n,'status':'http_error','http_status':503}]
            events.append({'attempt_id':'c1','task_id':'C','language':'bn','attempt':1,'status':'started','started_at_utc':'2026-10-24T00:00:00Z'})
            (out/'attempts'/'google.jsonl').write_text(''.join(json.dumps(e)+'\n' for e in events))
            with patch.object(s,'OUT',out):r=s.partition_status('google',s.epoch('2026-10-24T00:10:00Z'))
        self.assertEqual((r['unique_cells'],r['failed_response_records'],r['duplicates']),(1,1,0))
        self.assertEqual(r['attempt_budget_exhausted_cells'],[['B','en']])
        self.assertEqual(r['http_error_status_counts'],{'503':4})
        self.assertEqual([(x['task_id'],x['age_seconds']) for x in r['in_flight']],[('C',600)])

if __name__=='__main__':unittest.main()
