"""No-network generation/scoring separation, scope and protected-budget checks."""
import json
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import Mock,patch
import api_budget
import generation_only_v04 as g
import generation_controller_v04 as controller
from prelim_four_judge import ScoringContext

class GenerationTests(unittest.TestCase):
    def test_exact_scope_and_unchanged_config(self):
        c,m,f,a,p=g.verify();g.authorize(c,m)
        sizes={k:len(g.cells(c,f,a,p,k)) for k in g.four.PARTITIONS}
        self.assertEqual(sizes,{'openai':471,'google':60,'local_a':471,'local_b':471})
        selected=g.cells(c,f,a,p,'google');self.assertEqual(len({x['task_id'] for x in selected}),20)
        self.assertEqual({l:sum(x['language']==l for x in selected) for l in ('en','bn','bn_cs')},{'en':20,'bn':20,'bn_cs':20})
        original=g._ORIGINAL_CELLS(c,f,a,p,'google');self.assertEqual(selected,[x for x in original if x['task_id'] in set(g.four.read(g.SCOPE)['gemini_task_ids'])])
        self.assertEqual(g.four.digest(g.BASE_CONFIG),m['base_config_sha256'])
    def test_generation_allowed_while_original_scoring_gate_remains_failed(self):
        c,m,*_=g.verify();g.authorize(c,m)
        old=ScoringContext(g.BASE_CONFIG,g.BASE_MANIFEST);self.assertFalse(old.gate()['gate_pass']);old.frozen()
        with self.assertRaisesRegex(RuntimeError,'dimensions'):ScoringContext(g.BASE_CONFIG,g.MANIFEST)
    def test_no_scoring_cli(self):
        with patch('sys.argv',['generation_only_v04.py','score']),self.assertRaises(SystemExit):g.main()
    def test_budget_reserves_include_prior_costs_and_protect_80(self):
        approval={'maximum_usd':100,'authorization_id':'prelim-four-v03-usd100-20261023'}
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'approval.json').write_text('SYNTHETIC AUTHORIZATION')
            with patch.object(api_budget,'ROOT',root),patch.object(api_budget,'require_spending_approval',return_value=approval):
                l=g.GenerationBudget({}, {'spending_approval_record':'approval.json'},'generation')
                with l.locked():
                    l.append({'event':'reserved','request_id':'prior','model':'gpt-6.1-sol','purpose':'generation','reserved_nano_usd':19500000000})
                    l.append({'event':'settled','request_id':'prior','charged_nano_usd':19500000000,'usage':{'input_tokens':1,'output_tokens':1}})
                before=l.path.read_bytes()
                with self.assertRaisesRegex(api_budget.BudgetExceeded,'protected'):l.reserve('next','gpt-6.1-sol','','',32768)
                self.assertEqual(before,l.path.read_bytes());self.assertEqual(l.summary()['remaining_uncommitted_usd'],80.5)
    def test_budget_rejects_judge_or_changed_output_allowance(self):
        l=g.GenerationBudget.__new__(g.GenerationBudget);l.purpose='generation'
        for model,cap in [('gpt-5.4-2026-03-05',8192),('gpt-6.1-sol',1024)]:
            with self.assertRaises(RuntimeError):l.reserve('test',model,'','',cap)
    def test_local_phases_preserve_single_gpu_and_primary_priority(self):
        c=controller.Controller.__new__(controller.Controller);c.local_phase=Mock();c.locals()
        self.assertEqual([call.args for call in c.local_phase.call_args_list],[('local_a',6),('local_b',6),('local_a',471),('local_b',471)])
    def test_worker_failure_does_not_stop_independent_free_local_collection(self):
        c=controller.Controller.__new__(controller.Controller);c.stop=threading.Event();c.states={};c.state_lock=threading.Lock();c.event=Mock()
        c.guarded('openai',Mock(side_effect=RuntimeError('protected budget pause')))
        self.assertFalse(c.stop.is_set());self.assertEqual(c.states['openai']['state'],'paused')

if __name__=='__main__':unittest.main()
