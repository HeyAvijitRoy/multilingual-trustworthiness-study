"""No-network financial safety regressions; temporary synthetic authorizations."""
import json
import multiprocessing
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import api_budget as budget

APPROVAL={'maximum_usd':100,'authorization_id':'prelim-four-v03-usd100-20261023'}

def concurrent(root,rid,queue):
    with patch.object(budget,'ROOT',Path(root)),patch.object(budget,'require_spending_approval',return_value=APPROVAL):
        ledger=budget.BudgetLedger({}, {'spending_approval_record':'approval.json'},'scoring')
        try:ledger.reserve(rid,'gpt-6.1-sol','', '',32768);queue.put('ok')
        except budget.BudgetExceeded:queue.put('denied')

class BudgetTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);(self.root/'approval.json').write_text('SYNTHETIC ONLY')
        p=patch.object(budget,'ROOT',self.root);p.start();self.addCleanup(p.stop)
        p=patch.object(budget,'require_spending_approval',return_value=APPROVAL);p.start();self.addCleanup(p.stop)
    def ledger(self):return budget.BudgetLedger({}, {'spending_approval_record':'approval.json'},'scoring')
    def test_settlement_reasoning_cached_input_and_idempotence(self):
        l=self.ledger();l.reserve('one','gpt-5.4-2026-03-05','বাংলা','system',8192)
        usage={'input_tokens':100,'output_tokens':200,'input_tokens_details':{'cached_tokens':90},'output_tokens_details':{'reasoning_tokens':150}}
        l.settle('one',usage);l.settle('one',usage)
        self.assertEqual(l.summary()['settled_usage_estimate_usd'],.00325)
        with self.assertRaises(RuntimeError):l.settle('one',{'input_tokens':100,'output_tokens':201})
    def test_unknown_outcome_retains_hold_across_restart_and_denial(self):
        l=self.ledger()
        for i in range(195):l.reserve(str(i),'gpt-6.1-sol','','',32768)
        before=l.path.read_bytes()
        with self.assertRaises(budget.BudgetExceeded):self.ledger().reserve('last','gpt-6.1-sol','','',32768)
        self.assertEqual(l.path.read_bytes(),before)
        self.assertLessEqual(l.summary()['reserved_or_uncertain_usd'],100)
    def test_invalid_usage_and_torn_ledger_block_without_releasing(self):
        l=self.ledger();l.reserve('one','gpt-6.1-sol','','',32768)
        for usage in (None,{'input_tokens':True,'output_tokens':1},{'input_tokens':999999,'output_tokens':1},{'input_tokens':1,'output_tokens':32769}):
            with self.assertRaises(RuntimeError):l.settle('one',usage)
        self.assertEqual(l.summary()['held_requests'],1)
        with l.path.open('a') as f:f.write('{')
        with self.assertRaises(RuntimeError):l.reserve('two','gpt-6.1-sol','','',32768)
    def test_concurrent_processes_share_cap(self):
        l=self.ledger()
        for i in range(194):l.reserve(str(i),'gpt-6.1-sol','','',32768)
        ctx=multiprocessing.get_context('fork');q=ctx.Queue()
        jobs=[ctx.Process(target=concurrent,args=(str(self.root),str(i),q)) for i in range(194,198)]
        for p in jobs:p.start()
        for p in jobs:p.join(10);self.assertEqual(p.exitcode,0)
        results=[q.get(timeout=2) for p in jobs]
        self.assertEqual(results.count('ok'),1);self.assertEqual(results.count('denied'),3)
        self.assertLessEqual(l.summary()['reserved_or_uncertain_usd'],100)
    def test_changed_approval_does_not_reset_ledger(self):
        l=self.ledger();l.reserve('one','gpt-6.1-sol','','',32768)
        (self.root/'approval.json').write_text('CHANGED')
        with self.assertRaises(RuntimeError):self.ledger().summary()

if __name__=='__main__':unittest.main()

class EntryPointBudgetTests(unittest.TestCase):
    def test_generation_denial_sends_no_request_and_creates_no_attempt(self):
        import os
        import prelim_four as four
        cfg,manifest,freeze,anns,prompts=four.verify_candidate()
        with tempfile.TemporaryDirectory() as folder,patch.dict(os.environ,{'OPENAI_API_KEY':'synthetic'}), \
             patch.object(four,'require_frozen'),patch.object(four,'require_execution_gates'), \
             patch.object(four,'output_root',return_value=Path(folder)), \
             patch('api_budget.BudgetLedger') as ledger,patch.dict(four.historical.CALLERS,{'openai':unittest.mock.Mock()}) :
            ledger.return_value.reserve.side_effect=budget.BudgetExceeded('synthetic cap')
            with self.assertRaises(budget.BudgetExceeded):four.run_partition(cfg,manifest,freeze,anns,prompts,'openai',limit=1)
            four.historical.CALLERS['openai'].assert_not_called()
            self.assertFalse((Path(folder)/'attempts/openai.jsonl').exists())

    def test_judge_denial_sends_no_request_and_creates_no_attempt(self):
        import os
        from prelim_four_judge import ScoringContext
        with tempfile.TemporaryDirectory() as folder,patch.dict(os.environ,{'OPENAI_API_KEY':'synthetic'}), \
             patch('api_budget.BudgetLedger') as ledger,patch('prelim_judge_157.http_judge') as http:
            ctx=ScoringContext();ctx.root=Path(folder)
            ledger.return_value.reserve.side_effect=budget.BudgetExceeded('synthetic cap')
            with self.assertRaises(budget.BudgetExceeded):ctx.call('synthetic','calibration:test')
            http.assert_not_called();self.assertFalse((ctx.root/'judge_requests.jsonl').exists())
