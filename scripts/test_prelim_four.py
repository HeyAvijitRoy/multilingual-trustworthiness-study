"""Regression checks for amendment isolation and pre-generation scientific gates."""
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import prelim_four as four


class FourModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config, cls.manifest, cls.freeze, cls.annotations, cls.prompts = four.verify_candidate()

    def test_candidate_cannot_generate_any_provider(self):
        with patch.dict(four.historical.CALLERS, {"openai": lambda *args: self.fail("paid request")}):
            with self.assertRaisesRegex(RuntimeError, "study generation blocked"):
                four.run_partition(self.config, self.manifest, self.freeze,
                                   self.annotations, self.prompts, "openai", limit=1)

    def test_candidate_cells_keep_all_471_frozen_prompts_per_partition(self):
        for partition in four.PARTITIONS:
            cells = four.cells_for(self.config, self.freeze, self.annotations, self.prompts, partition)
            self.assertEqual(len(cells), 471)
            self.assertEqual(len({(c["task_id"], c["language"]) for c in cells}), 471)
            self.assertEqual(cells, four.cells_for(self.config, self.freeze, self.annotations,
                                                self.prompts, partition))
            for cell in cells:
                self.assertEqual(cell["prompt_text"], self.prompts[cell["task_id"]]["prompt_" + cell["language"]])
                self.assertEqual(cell["prompt_sha256"], hashlib.sha256(cell["prompt_text"].encode()).hexdigest())

    def test_no_foreign_or_duplicate_successes_on_resume(self):
        config = deepcopy(self.config)
        config["models"][0]["model_id"] = "test-model"
        cell = four.cells_for(config, self.freeze, self.annotations, self.prompts, "openai")[0]
        pins = four.provenance()
        row = {**cell, **pins, "protocol_id": config["protocol_id"], "requested_model": "test-model",
               "response_text": "বাংলা\u2028পাঠ", "status": "success",
               "response_sha256": hashlib.sha256("বাংলা\u2028পাঠ".encode()).hexdigest()}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "openai.jsonl"
            four.historical.append_jsonl(path, row)
            done, failures = four.validated_records(path, config, "openai", [cell], pins)
            self.assertEqual((len(done), failures), (1, 0))
            foreign = {**row, "amendment_manifest_sha256": "foreign"}
            four.historical.append_jsonl(path, foreign)
            with self.assertRaisesRegex(RuntimeError, "foreign/stale"):
                four.validated_records(path, config, "openai", [cell], pins)
            path.write_text(json.dumps(row) + "\n" + json.dumps(row) + "\n")
            with self.assertRaisesRegex(RuntimeError, "duplicate successful"):
                four.validated_records(path, config, "openai", [cell], pins)

    def test_response_bytes_cannot_change_after_hashing(self):
        cells = four.cells_for(self.config, self.freeze, self.annotations, self.prompts, "openai")
        row = {**cells[0], **four.provenance(), "protocol_id": self.config["protocol_id"],
               "requested_model": self.config["models"][0]["model_id"], "status": "success",
               "response_text": "altered", "response_sha256": "0" * 64}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "openai.jsonl"
            four.historical.append_jsonl(path, row)
            with self.assertRaisesRegex(RuntimeError, "response integrity"):
                four.validated_records(path, self.config, "openai", cells, four.provenance())

    def test_historical_output_directory_cannot_be_reused(self):
        for rel in ("data/outputs/prelim_157", ".local/prelim_157", ".local", "../elsewhere"):
            with self.subTest(rel=rel), self.assertRaisesRegex(RuntimeError, "output|namespace"):
                four.output_root({**self.config, "output_directory": rel})

    def test_partition_lock_prevents_competing_generation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with four.partition_lock(root, "local_runtime"):
                with self.assertRaisesRegex(RuntimeError, "locked"):
                    with four.partition_lock(root, "local_runtime"):
                        self.fail("competing process acquired the same lock")
            self.assertFalse((root / "local_runtime.lock").exists())

    def test_local_adapter_keeps_visible_text_and_rejects_reasoning(self):
        model = {"model_id": "pinned-local", "endpoint_env": "FOUR_TEST_ENDPOINT",
                 "engine": "openai-compatible-local-server", "decoding": {"temperature": 0}}
        payload = {"model": "pinned-local", "choices": [{"message": {"content": "উত্তর"}, "finish_reason": "stop"}]}
        with patch.dict(os.environ, {"FOUR_TEST_ENDPOINT": "http://127.0.0.1:8080/v1"}):
            with patch.object(four, "local_http_json", return_value=(payload, 200)) as http:
                result = four.local_chat(model, "মূল প্রম্পট", self.config["system_prompt"], 10, 100)
                self.assertEqual(result["response_text"], "উত্তর")
                request = http.call_args.args[2]
                self.assertEqual(request["messages"][1]["content"], "মূল প্রম্পট")
                payload["choices"][0]["message"]["reasoning_content"] = "private"
                with self.assertRaisesRegex(RuntimeError, "reasoning not disabled"):
                    four.local_chat(model, "p", "s", 10, 100)

    def test_local_adapter_refuses_external_endpoint_and_substitution(self):
        model = {"model_id": "pinned", "endpoint_env": "FOUR_TEST_ENDPOINT",
                 "engine": "openai-compatible-local-server", "decoding": {}}
        with patch.dict(os.environ, {"FOUR_TEST_ENDPOINT": "https://example.com/v1"}):
            with patch.object(four, "local_http_json") as http:
                with self.assertRaisesRegex(RuntimeError, "loopback"):
                    four.local_chat(model, "p", "s", 10, 100)
                http.assert_not_called()
        with patch.dict(os.environ, {"FOUR_TEST_ENDPOINT": "http://localhost:8080/v1"}):
            payload = {"model": "other", "choices": [{"message": {"content": "answer"}, "finish_reason": "stop"}]}
            with patch.object(four, "local_http_json", return_value=(payload, 200)):
                with self.assertRaisesRegex(RuntimeError, "different model"):
                    four.local_chat(model, "p", "s", 10, 100)

    def test_error_payload_redacts_credentials(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": "synthetic-secret-never-real"}):
            clean = four.redact_credentials({"error": "echo synthetic-secret-never-real"}, self.config)
            self.assertEqual(clean, {"error": "echo [REDACTED]"})

    def test_mocked_run_records_retry_then_resumes_without_regenerating(self):
        cell = four.cells_for(self.config, self.freeze, self.annotations, self.prompts, "openai")[0]
        result = {"response_text": "valid outcome", "finish_status": "completed",
                  "provider_raw_meta": {}, "returned_model": "gpt-6-astra"}
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"OPENAI_API_KEY": "test-only"}):
            root = Path(tmp)
            with patch.object(four, "require_frozen"), patch.object(four, 'require_execution_gates'), patch.object(four, "output_root", return_value=root), \
                 patch.object(four, "cells_for", return_value=[cell]), patch.object(four.time, "sleep"), \
                 patch.dict(four.historical.CALLERS, {"openai": unittest.mock.Mock(side_effect=[
                     four.historical.ProviderHTTPError(429, {"error": "retry"}), result])}):
                caller = four.historical.CALLERS["openai"]
                for _ in range(2):
                    four.run_partition(self.config, self.manifest, self.freeze,
                                       self.annotations, self.prompts, "openai")
                self.assertEqual(caller.call_count, 2)
            rows = four.historical.read_jsonl_records(root / "openai.jsonl")
            attempts = four.historical.read_jsonl_records(root / "attempts/openai.jsonl")
            self.assertEqual(len(rows), 1)
            self.assertEqual([r["status"] for r in attempts], ["started", "http_error", "started", "success"])
            self.assertEqual(rows[0]["status"], "success")

    def test_mocked_runtime_error_stays_missing(self):
        cell = four.cells_for(self.config, self.freeze, self.annotations, self.prompts, "openai")[0]
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"OPENAI_API_KEY": "test-only"}):
            root = Path(tmp)
            with patch.object(four, "require_frozen"), patch.object(four, 'require_execution_gates'), patch.object(four, "output_root", return_value=root), \
                 patch.object(four, "cells_for", return_value=[cell]), \
                 patch.dict(four.historical.CALLERS, {"openai": unittest.mock.Mock(side_effect=RuntimeError("unavailable"))}):
                four.run_partition(self.config, self.manifest, self.freeze,
                                   self.annotations, self.prompts, "openai")
            row = four.historical.read_jsonl_records(root / "openai.jsonl")[0]
            self.assertEqual(row["status"], "api_error")
            self.assertEqual(row["attempts"][0]["status"], "runtime_error")
            self.assertNotIn("response_text", row)

    def test_crash_after_success_event_never_regenerates_cell(self):
        cell = four.cells_for(self.config, self.freeze, self.annotations, self.prompts, "openai")[0]
        result = {"response_text": "received outcome", "finish_status": "completed", "provider_raw_meta": {}}
        real_append = four.historical.append_jsonl
        def interrupted(path, row):
            real_append(path, row)
            if row.get("status") == "success" and path.parent.name == "attempts":
                raise KeyboardInterrupt()
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"OPENAI_API_KEY": "test-only"}):
            root = Path(tmp)
            caller = unittest.mock.Mock(return_value=result)
            with patch.object(four, "require_frozen"), patch.object(four, 'require_execution_gates'), patch.object(four, "output_root", return_value=root), \
                 patch.object(four, "cells_for", return_value=[cell]), \
                 patch.dict(four.historical.CALLERS, {"openai": caller}):
                with patch.object(four.historical, "append_jsonl", side_effect=interrupted):
                    with self.assertRaises(KeyboardInterrupt):
                        four.run_partition(self.config, self.manifest, self.freeze,
                                           self.annotations, self.prompts, "openai")
                with self.assertRaisesRegex(RuntimeError, "successful attempt lacks"):
                    four.run_partition(self.config, self.manifest, self.freeze,
                                       self.annotations, self.prompts, "openai")
                self.assertEqual(caller.call_count, 1)
            event = four.historical.read_jsonl_records(root / "attempts/openai.jsonl")[-1]
            self.assertEqual(event["received_response"]["response_text"], "received outcome")

    def test_inflight_request_blocks_resume(self):
        cell = four.cells_for(self.config, self.freeze, self.annotations, self.prompts, "openai")[0]
        row = {**cell, **four.provenance(), "protocol_id": self.config["protocol_id"],
               "requested_model": self.config["models"][0]["model_id"], "status": "started", "attempt_id": "unique"}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "attempts.jsonl"
            four.historical.append_jsonl(path, row)
            with self.assertRaisesRegex(RuntimeError, "ambiguous outcome"):
                four.validate_attempt_history(path, self.config, "openai", [cell], four.provenance(), {})

    def test_readiness_checks_immutable_artifacts_not_only_labels(self):
        with patch.object(four, "readiness", return_value=[]):
            self.assertTrue(four.generation_readiness(self.config, self.manifest))

    def test_local_adapter_refuses_unknown_finish_and_redirect(self):
        model = {"model_id": "pinned", "endpoint_env": "FOUR_TEST_ENDPOINT",
                 "engine": "openai-compatible-local-server", "decoding": {}}
        payload = {"model": "pinned", "choices": [{"message": {"content": "answer"}, "finish_reason": "error"}]}
        with patch.dict(os.environ, {"FOUR_TEST_ENDPOINT": "http://localhost:8080/v1"}):
            with patch.object(four, "local_http_json", return_value=(payload, 200)):
                with self.assertRaisesRegex(RuntimeError, "unknown local finish reason"):
                    four.local_chat(model, "p", "s", 10, 100)
        with self.assertRaisesRegex(RuntimeError, "redirect refused"):
            four.RejectLocalRedirects().redirect_request(None, None, 307, "redirect", {}, "https://example.com")


if __name__ == "__main__":
    unittest.main()
