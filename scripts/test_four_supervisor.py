"""Operational supervisor regressions; no network, GPU or credentials."""
import threading
import unittest
from types import SimpleNamespace
from unittest.mock import Mock,patch
from pathlib import Path
import tempfile
import continue_prelim_four as supervisor

class SupervisorTests(unittest.TestCase):
    def instance(self):
        s=supervisor.Supervisor.__new__(supervisor.Supervisor)
        s.stop=threading.Event();s.locks={'google':threading.Lock(),'openai':threading.Lock()}
        s.ctx=SimpleNamespace(root=Path('/synthetic/never-written'))
        return s
    def test_completed_partition_never_calls_paid_cli(self):
        s=self.instance();s.successes=Mock(return_value=471);s.command=Mock();s.generate('openai');s.command.assert_not_called()
    def test_one_pending_cell_at_a_time_and_no_parameter_changes(self):
        s=self.instance();s.successes=Mock(side_effect=[470,471,471]);s.command=Mock(return_value=0);s.generate('openai')
        self.assertEqual(s.command.call_args.args[1],['run','--provider','openai','--limit','1'])
        self.assertEqual(s.command.call_count,1)
    def test_no_progress_pauses_instead_of_replaying_forever(self):
        s=self.instance();s.successes=Mock(return_value=0);s.command=Mock(return_value=0)
        with self.assertRaisesRegex(RuntimeError,'failure reconciliation'):s.generate('openai')
        self.assertEqual(s.command.call_count,1)
    def test_quota_deferral_waits_without_extra_http_or_paid_fallback(self):
        s=self.instance();s.successes=Mock(return_value=0);s.command=Mock(return_value=75)
        def wait(seconds):self.assertLessEqual(seconds,60);s.stop.set()
        with patch.object(supervisor.four.historical,'read_jsonl_records',return_value=[{'retry_at_epoch':99999999999}]),patch.object(s.stop,'wait',side_effect=wait):s.generate('google')
        self.assertEqual(s.command.call_count,1)
    def test_worker_failure_stops_new_requests_and_preserves_reason(self):
        s=self.instance();s.error_lock=threading.Lock();s.errors=[]
        with tempfile.TemporaryDirectory() as d:
            s.root=Path(d);s.guarded('synthetic',Mock(side_effect=RuntimeError('cap denied')))
            self.assertTrue(s.stop.is_set());self.assertIn('cap denied',s.errors[0]);self.assertTrue((s.root/'events.jsonl').exists())

if __name__=='__main__':unittest.main()
