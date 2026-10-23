"""Historical evaluation regressions; synthetic outputs only, never paid calls."""
import contextlib
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import analyze_prelim_157 as analysis
import prelim_eval_157 as generation
import prelim_judge_157 as judge


class SerializationTests(unittest.TestCase):
    def test_unicode_separator_round_trip_resume_and_scoring(self):
        row = {"status": "success", "task_id": "X", "language": "bn", "requested_model": "M",
               "run_index": 1, "response_text": "বাংলা\u2028line\u0085next\u2029end"}
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "p.jsonl"
            generation.append_jsonl(path, row)
            self.assertEqual(generation.read_jsonl_records(path), [row])
            self.assertEqual(generation.load_latest_success_keys(path), {("X", "bn", "M", 1)})
            self.assertEqual(judge.scored_keys(path), {("X", "bn", "M", 1)})
            with patch.object(judge, "OUTPUT_DIR", Path(folder)):
                path.rename(Path(folder) / "openai.jsonl")
                self.assertEqual(judge.load_successful_generations("openai"), [row])

    def test_torn_record_is_preserved_and_blocks_resume_and_append(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "p.jsonl"
            path.write_bytes(b'{"status":')
            original = path.read_bytes()
            with self.assertRaisesRegex(RuntimeError, "unterminated"):
                generation.load_latest_success_keys(path)
            with self.assertRaisesRegex(RuntimeError, "unterminated"):
                generation.append_jsonl(path, {"status": "success"})
            self.assertEqual(path.read_bytes(), original)

    def test_failed_records_do_not_block_retry(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "p.jsonl"
            generation.append_jsonl(path, {"status": "api_error"})
            self.assertEqual(generation.load_latest_success_keys(path), set())

    def test_resume_rejects_foreign_and_conflicting_successes(self):
        row = {"status": "success", "task_id": "X", "language": "bn", "requested_model": "M",
               "run_index": 1, "response_text": "one", "prompt_sha256": "hash", "provider": "openai",
               "snapshot_id": "S"}
        freeze = {"snapshot_id": "S"}
        models = {"models": [{"provider": "openai", "model_id": "M"}]}
        anns = {"X": {"prompt_sha256": {"bn": "hash"}}}
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "p.jsonl"
            generation.append_jsonl(path, row)
            generation.validate_generation_records(path, freeze, models, anns, "openai")
            generation.append_jsonl(path, {**row, "response_text": "two"})
            with self.assertRaisesRegex(RuntimeError, "conflicting"):
                generation.validate_generation_records(path, freeze, models, anns, "openai")
            with self.assertRaisesRegex(RuntimeError, "outside frozen"):
                generation.validate_generation_records(path, {"snapshot_id": "T"}, models, anns, "openai")


class AdapterTests(unittest.TestCase):
    def test_openai_visible_text_once_and_raw_retained(self):
        payload = {"status": "completed", "output_text": "বাংলা", "id": "R", "model": "M"}
        with patch.dict(generation.os.environ, {"KEY": "fake"}), patch.object(generation, "http_json", return_value=(payload, 200)):
            result = generation.call_openai({"env_key": "KEY", "model_id": "M"}, "P", "S", 1, 10)
        self.assertEqual(result["response_text"], "বাংলা")
        self.assertEqual(result["provider_raw_response"], payload)

    def test_openai_failed_payload_is_not_success(self):
        with patch.dict(generation.os.environ, {"KEY": "fake"}), patch.object(generation, "http_json", return_value=({"status": "failed", "error": {"code": "failure"}}, 200)):
            with self.assertRaises(generation.ProviderHTTPError):
                generation.call_openai({"env_key": "KEY", "model_id": "M"}, "P", "S", 1, 10)

    def test_google_thought_text_excluded(self):
        payload = {"candidates": [{"content": {"parts": [{"text": "hidden", "thought": True}, {"text": "visible"}]}, "finishReason": "MAX_TOKENS"}]}
        with patch.dict(generation.os.environ, {"KEY": "fake"}), patch.object(generation, "http_json", return_value=(payload, 200)):
            result = generation.call_google({"env_key": "KEY", "model_id": "M"}, "P", "S", 1, 10)
        self.assertEqual(result["response_text"], "visible")
        self.assertTrue(generation.is_truncated(result))

    def test_truncation_uses_provider_reason(self):
        self.assertTrue(generation.is_truncated({"finish_status": "max_tokens"}))
        self.assertTrue(generation.is_truncated({"finish_status": "incomplete", "provider_raw_meta": {"incomplete_details": {"reason": "max_output_tokens"}}}))
        self.assertFalse(generation.is_truncated({"finish_status": "incomplete", "provider_raw_meta": {"incomplete_details": {"reason": "content_filter"}}}))


class ScoringTests(unittest.TestCase):
    def setUp(self):
        self.rec = {"task_id": "X", "rius": [{"id": "R1", "criticality": "critical", "scoring_mode": "binary", "description": "D", "scoring_rule": {}, "rationale": "R"}], "task_checks": []}
        self.rating = {"item_id": "R1", "score": 0, "reason": "non_answer", "evidence": "", "notes": ""}

    def test_duplicate_item_is_not_silently_collapsed(self):
        with self.assertRaisesRegex(RuntimeError, "duplicate"):
            judge.validate_ratings(self.rec, [self.rating, self.rating])
        with self.assertRaisesRegex(RuntimeError, "duplicate"):
            analysis.response_metrics(self.rec, {"ratings": [self.rating, self.rating]})

    def test_nonanswer_is_literal_omission_but_incorrect_is_not(self):
        metrics = analysis.response_metrics(self.rec, {"ratings": [self.rating]})
        self.assertEqual(metrics["critical_omission_rate"], 1)
        self.assertEqual(metrics["non_answer"], 1)
        self.rating["reason"] = "incorrect"
        metrics = analysis.response_metrics(self.rec, {"ratings": [self.rating]})
        self.assertEqual(metrics["critical_omission_rate"], 0)
        self.assertEqual(metrics["critical_unmet_rate"], 1)

    def test_recalibration_cannot_overwrite_existing_evidence(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "sheet.csv"
            path.write_text("existing evidence\n")
            with patch.object(judge, "CAL_SHEET", path):
                with self.assertRaisesRegex(RuntimeError, "already exist"):
                    judge.calibrate()
            self.assertEqual(path.read_text(), "existing evidence\n")

    def test_stale_scores_cannot_skip_new_judge_or_changed_response(self):
        source = {"task_id": "X", "language": "bn", "requested_model": "M", "run_index": 1,
                  "response_text": "বাংলা", "prompt_sha256": "P", "snapshot_id": "S"}
        row = {**source, "status": "success", "response_sha256": generation.sha256_bytes("বাংলা".encode()),
               "judge_config_sha256": generation.sha256_file(judge.JUDGE_PATH),
               "scoring_plan_sha256": generation.sha256_file(judge.SCORING_PLAN_PATH)}
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "scores.jsonl"
            generation.append_jsonl(path, row)
            judge.validate_score_records(path, [source])
            with self.assertRaisesRegex(RuntimeError, "stale/mismatched"):
                judge.validate_score_records(path, [{**source, "response_text": "changed"}])
            with self.assertRaisesRegex(RuntimeError, "no successful generation"):
                judge.validate_score_records(path, [])



class StatisticalTests(unittest.TestCase):
    def setUp(self):
        self.domains = {"T3": "B", "T1": "A", "T4": "B", "T2": "A"}
        self.rows = {}
        for i, task in enumerate(sorted(self.domains)):
            for model in ["M1", "M2"]:
                self.rows[(model, task, "bn")] = {"metric": i / 3}
                self.rows[(model, task, "en")] = {"metric": 0}

    def test_bootstrap_is_independent_of_input_record_order(self):
        with patch.object(analysis, "BOOTSTRAP_N", 200):
            a = analysis.bootstrap_ci(self.rows, self.domains, ["M1", "M2"], "metric", "bn", "en")
            b = analysis.bootstrap_ci(dict(reversed(list(self.rows.items()))), dict(reversed(list(self.domains.items()))), ["M1", "M2"], "metric", "bn", "en")
        self.assertEqual(a, b)
        self.assertEqual(a["by_model_ci95"]["M1"], a["ci95"])

    def test_missing_panel_model_does_not_become_smaller_panel(self):
        with patch.object(analysis, "BOOTSTRAP_N", 100):
            result = analysis.bootstrap_ci(self.rows, self.domains, ["M1", "M2", "MISSING"], "metric", "bn", "en")
        self.assertIsNone(result["estimate"])
        self.assertEqual(result["ci95"], [None, None])
        self.assertEqual(result["by_model_ci95"]["MISSING"], [None, None])
        self.assertEqual(result["by_model_bootstrap_replicates"]["M1"], 100)
        json.dumps(result, allow_nan=False)

    def test_domain_equal_weighting_and_pairwise_missingness(self):
        self.domains["T5"] = "A"
        self.rows[("M1", "T5", "bn")] = {"metric": 1}
        pooled, _ = analysis.effect(self.rows, self.domains, ["M1"], "metric", "bn", "en")
        self.assertAlmostEqual(pooled, 0.5)


class ReportingTests(unittest.TestCase):
    def test_paired_denominators_separate_missing_and_undefined(self):
        rows = {("M", "T1", "bn"): {"metric": 1}, ("M", "T1", "en"): {"metric": 0},
                ("M", "T2", "bn"): {"metric": None}, ("M", "T2", "en"): {"metric": None},
                ("M", "T3", "bn"): {"metric": 1}}
        result = analysis.paired_counts(rows, {"T1": "A", "T2": "A", "T3": "B"}, ["M", "ABSENT"], "metric", "bn", "en")
        self.assertEqual(result["M"]["paired_tasks"], 1)
        self.assertEqual(result["M"]["undefined_metric_tasks"], 1)
        self.assertEqual(result["M"]["missing_cell_tasks"], 1)
        self.assertEqual(result["M"]["by_domain"]["B"]["missing_cell_tasks"], 1)
        self.assertEqual(result["ABSENT"]["missing_cell_tasks"], 3)

    def test_strata_extended_and_truncation_keep_matched_pairs(self):
        annotations = {"T1": {"domain": "A", "difficulty": "easy"},
                       "T2": {"domain": "A", "difficulty": "hard"},
                       "SYN091": {"domain": "S", "difficulty": "hard"}}
        rows = {}
        for task, value in (("T1", 0.5), ("T2", 0.2), ("SYN091", 1)):
            rows[("M", task, "bn")] = {"metric": value}
            rows[("M", task, "en")] = {"metric": 0}
        with patch.object(analysis, "BOOTSTRAP_N", 25), patch.object(analysis, "EFFECT_SPECS", [("metric", "bn", "en")]):
            result = analysis.reporting_tables(rows, annotations, ["M"], {("M", "T1", "bn")})
        self.assertAlmostEqual(result["by_domain"]["A"]["metric:bn-en"]["estimate"], 0.35)
        self.assertAlmostEqual(result["by_difficulty"]["easy"]["metric:bn-en"]["estimate"], 0.5)
        ext = result["extended_context_sensitivity"]
        self.assertEqual(ext["extended_task_ids"], ["SYN091"])
        self.assertEqual(ext["extended_only"]["metric:bn-en"]["estimate"], 1)
        self.assertAlmostEqual(ext["excluding_extended"]["metric:bn-en"]["estimate"], 0.35)
        sensitivity = result["truncation_sensitivity"]["effects_excluding_truncated"]["metric:bn-en"]
        self.assertAlmostEqual(sensitivity["estimate"], 0.6)
        self.assertEqual(sensitivity["paired_counts"]["M"]["paired_tasks"], 2)
        self.assertEqual(len(rows), 6)  # raw/full primary data were not removed

    def test_empty_stratum_is_undefined_and_json_safe(self):
        with patch.object(analysis, "BOOTSTRAP_N", 5):
            result = analysis.bootstrap_ci({}, {}, ["M"], "metric", "bn", "en")
        self.assertIsNone(result["estimate"])
        self.assertEqual(result["ci95"], [None, None])
        json.dumps(result, allow_nan=False)

    def test_generation_status_distinguishes_failures_retries_and_nonanswers(self):
        freeze = {"snapshot_id": "S", "pilot_task_ids": ["T1", "T2", "T3"], "expansion_tasks": []}
        cfg = {"models": [{"provider": "openai", "model_id": "M"}]}
        base = {"snapshot_id": "S", "requested_model": "M", "provider": "openai", "run_index": 1,
                "language": "en", "task_id": "T1"}
        rows = [{**base, "status": "api_error"},
                {**base, "status": "success", "response_text": "", "generated_at_utc": "2026-10-23T12:00:00Z", "finish_status": "max_tokens"},
                {**base, "task_id": "T2", "status": "api_error"},
                {**base, "task_id": "T3", "status": "success", "response_text": "normal"}]
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "openai.jsonl"
            for row in rows:
                generation.append_jsonl(path, row)
            with patch.object(analysis, "OUTPUT_DIR", Path(folder)):
                report, truncated = analysis.generation_status(freeze, cfg, {("M", "T1", "en", 1): {}})
        en = report["by_model_language"]["M:en"]
        self.assertEqual(en["api_error_records"], 2)
        self.assertEqual(en["unresolved_api_failure_cells"], 1)
        self.assertEqual(en["successful_generations"], 2)  # empty nonanswer is a valid outcome
        self.assertEqual(en["generated_unscored_cells"], 1)
        self.assertEqual(en["truncation_rate_among_successes"], 0.5)
        self.assertEqual(report["by_model_language"]["M:bn"]["unattempted_cells"], 3)
        self.assertEqual(truncated, {("M", "T1", "en")})
        self.assertEqual(report["generation_date_range_utc"], ["2026-10-23T12:00:00Z"] * 2)

    def test_format_denominator_excludes_tasks_without_format_check(self):
        rec = {"task_id": "T", "rius": [{"id": "R", "criticality": "critical", "scoring_mode": "binary", "description": "D", "scoring_rule": {}, "rationale": "R"}], "task_checks": []}
        row = {"ratings": [{"item_id": "R", "score": 1, "reason": "met"}]}
        self.assertIsNone(analysis.response_metrics(rec, row)["format_adherence"])

    def test_main_writes_synthetic_report_and_rejects_unattempted_missingness(self):
        rec = {"task_id": "T1", "domain": "A", "difficulty": "easy", "task_objective": "D", "constraints": [],
               "prompt_sha256": {lang: "P" for lang in analysis.LANGS},
               "rius": [{"id": "R", "criticality": "critical", "scoring_mode": "binary", "description": "D", "scoring_rule": {}, "rationale": "R"}],
               "task_checks": [{"id": "C", "kind": "unsupported_content", "rule": "Rule"}]}
        freeze = {"snapshot_id": "S", "pilot_task_ids": ["T1"], "expansion_tasks": []}
        models = {"models": [{"provider": "openai", "model_id": "M"}]}
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            output, score_dir, analysis_dir = root / "raw", root / "raw" / "scores", root / "analysis"
            raw, scored = [], []
            for language in analysis.LANGS:
                source = {"snapshot_id": "S", "provider": "openai", "requested_model": "M", "run_index": 1,
                          "task_id": "T1", "language": language, "prompt_sha256": "P", "response_text": "synthetic answer",
                          "status": "success", "finish_status": "completed", "generated_at_utc": "2026-10-23T12:00:00Z"}
                ratings = [{"item_id": "R", "score": 1, "reason": "met"}, {"item_id": "C", "score": 1, "reason": "pass"}]
                score = {**source, "ratings": ratings, "response_sha256": generation.sha256_bytes(source["response_text"].encode()),
                         "judge_config_sha256": judge.sha256_file(judge.JUDGE_PATH),
                         "scoring_plan_sha256": judge.sha256_file(judge.SCORING_PLAN_PATH)}
                raw.append(source)
                scored.append(score)
                generation.append_jsonl(output / "openai.jsonl", source)
                generation.append_jsonl(score_dir / "openai.jsonl", score)
            with contextlib.ExitStack() as stack:
                stack.enter_context(patch.object(generation, "verify_freeze", return_value=(freeze, models, {"T1": rec}, {})))
                stack.enter_context(patch.object(judge, "gate", return_value=True))
                stack.enter_context(patch.object(judge, "OUTPUT_DIR", output))
                stack.enter_context(patch.object(analysis, "OUTPUT_DIR", output))
                stack.enter_context(patch.object(analysis, "SCORES_DIR", score_dir))
                stack.enter_context(patch.object(analysis, "ANALYSIS_DIR", analysis_dir))
                stack.enter_context(patch.object(analysis, "PROVIDERS", ["openai"]))
                stack.enter_context(patch.object(analysis, "BOOTSTRAP_N", 10))
                stack.enter_context(patch.object(analysis, "EFFECT_SPECS", [("critical_omission_rate", "bn", "en")]))
                stack.enter_context(patch("sys.argv", ["analyze_prelim_157.py"]))
                stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
                self.assertEqual(analysis.main(), 0)
                report = json.loads((analysis_dir / "prelim_157_results.json").read_text())
                summary = (analysis_dir / "prelim_157_summary.md").read_text()
                self.assertEqual(report["scored_cells"], 3)
                self.assertEqual(report["effects"]["critical_omission_rate:bn-en"]["paired_counts"]["M"]["paired_tasks"], 1)
                self.assertIn("Domain strata", summary)
                self.assertIn("Difficulty strata", summary)
                self.assertIn("Extended-context sensitivity", summary)
                self.assertIn("Truncation sensitivity", summary)
                self.assertIn("Missingness sensitivity", summary)
                self.assertEqual(report["missingness_sensitivity"]["complete_panel_task_count"], 1)
                self.assertIn("provisional", summary)
                # Removing the BN raw/score cells creates unattempted missingness,
                # which --allow-missing must not silently bless as API failure.
                (output / "openai.jsonl").unlink()
                (score_dir / "openai.jsonl").unlink()
                for source, score in zip(raw, scored):
                    if source["language"] != "bn":
                        generation.append_jsonl(output / "openai.jsonl", source)
                        generation.append_jsonl(score_dir / "openai.jsonl", score)
                with patch("sys.argv", ["analyze_prelim_157.py", "--allow-missing"]):
                    with self.assertRaisesRegex(RuntimeError, "unattempted"):
                        analysis.main()
                    failure = {**raw[1], "status": "api_error", "error": {"type": "synthetic"}}
                    generation.append_jsonl(output / "openai.jsonl", failure)
                    self.assertEqual(analysis.main(), 0)
                    missing_report = json.loads((analysis_dir / "prelim_157_results.json").read_text())
                    self.assertEqual(missing_report["missing_cells"], 1)
                    self.assertEqual(missing_report["generation_status"]["by_model_language"]["M:bn"]["unresolved_api_failure_cells"], 1)
                    self.assertIsNone(missing_report["effects"]["critical_omission_rate:bn-en"]["estimate"])


class QAPacketTests(unittest.TestCase):
    def fixture(self):
        annotations, prompts, sources, scores = {}, {}, [], []
        for number in range(1, 31):
            task = f"T{number:02d}"
            annotations[task] = {"task_id": task, "task_objective": "Objective", "constraints": [],
                                 "rius": [{"id": "R", "criticality": "critical", "scoring_mode": "binary", "description": "D", "scoring_rule": {}, "rationale": "R"}],
                                 "task_checks": [{"id": "C", "kind": "unsupported_content", "rule": "No unsupported assertion"}]}
            prompts[task] = {"prompt_bn": "বাংলা prompt"}
            source = {"task_id": task, "language": "bn", "provider": "openai", "requested_model": "PRIVATE_MODEL",
                      "run_index": 1, "status": "success", "response_text": "answer", "finish_status": "completed"}
            sources.append(source)
            ratings = [{"item_id": "R", "score": 1, "reason": "met"}, {"item_id": "C", "score": 1, "reason": "pass"}]
            if number == 1:
                ratings[0].update(score=0, reason="omitted")
            elif number == 2:
                ratings[1].update(score=0, reason="fail")
            elif number == 3:
                ratings[0].update(score=0, reason="non_answer")
            elif number == 4:
                source["finish_status"] = "max_tokens"
            scores.append({**source, "ratings": ratings})
        # A truncated generation without scores must still be inspected.
        sources.append({**sources[3], "task_id": "T_UNSCORED"})
        annotations["T_UNSCORED"], prompts["T_UNSCORED"] = annotations["T04"], prompts["T04"]
        return annotations, prompts, sources, scores

    def test_mandatory_flags_and_remaining_stratum_sample_are_deterministic(self):
        annotations, prompts, sources, scores = self.fixture()
        packet, manifest = judge.build_qa_records({"snapshot_id": "S"}, annotations, prompts, sources, scores)
        again = judge.build_qa_records({"snapshot_id": "S"}, annotations, prompts, list(reversed(sources)), list(reversed(scores)))
        self.assertEqual((packet, manifest), again)
        cells = {row["task_id"]: row for row in manifest["cells"]}
        self.assertTrue({"T01", "T02", "T03", "T04", "T_UNSCORED"} <= set(cells))
        self.assertIn("critical_riu_below_full_credit", cells["T01"]["selection_reasons"])
        self.assertIn("task_check_failure", cells["T02"]["selection_reasons"])
        self.assertIn("refusal_or_nonanswer", cells["T03"]["selection_reasons"])
        self.assertIn("truncated_response", cells["T04"]["selection_reasons"])
        self.assertFalse(cells["T_UNSCORED"]["has_automated_scores"])
        self.assertEqual(manifest["sample_by_model_language"]["PRIVATE_MODEL:bn"], {"remaining_scored_cells": 26, "sampled_cells": 3})
        self.assertEqual(len(packet), 8)
        self.assertEqual(manifest["human_reviews_completed"], 0)
        self.assertEqual({row["review_status"] for row in packet}, {"pending_human_review"})
        self.assertNotIn("PRIVATE_MODEL", json.dumps(packet))
        self.assertNotIn('"provider"', json.dumps(packet))
        self.assertEqual(cells["T01"]["generation_record_sha256"], judge.canonical_record_sha256(sources[0]))
        self.assertEqual(cells["T01"]["score_record_sha256"], judge.canonical_record_sha256(scores[0]))

    def test_unscored_nontruncated_generation_does_not_enter_sample(self):
        annotations, prompts, sources, scores = self.fixture()
        packet, manifest = judge.build_qa_records({"snapshot_id": "S"}, annotations, prompts, sources[:1], [])
        self.assertEqual(packet, [])
        self.assertEqual(manifest["cells"], [])

    def test_qa_cli_writes_blinded_packet_and_never_overwrites(self):
        annotations, prompts, sources, scores = self.fixture()
        source, score = sources[0], scores[0]
        annotations = {"T01": {**annotations["T01"], "prompt_sha256": {"bn": "P"}}}
        source.update(snapshot_id="S", prompt_sha256="P")
        score.update(snapshot_id="S", prompt_sha256="P", response_sha256=generation.sha256_bytes(source["response_text"].encode()),
                     judge_config_sha256=judge.sha256_file(judge.JUDGE_PATH), scoring_plan_sha256=judge.sha256_file(judge.SCORING_PLAN_PATH))
        freeze = {"snapshot_id": "S"}
        cfg = {"models": [{"provider": "openai", "model_id": "PRIVATE_MODEL"}]}
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            output, destination = root / "raw", root / "qa"
            generation.append_jsonl(output / "openai.jsonl", source)
            generation.append_jsonl(output / "scores" / "openai.jsonl", score)
            with patch.object(generation, "verify_freeze", return_value=(freeze, cfg, annotations, prompts)), patch.object(judge, "OUTPUT_DIR", output), patch.object(judge, "ROOT", root), contextlib.redirect_stdout(io.StringIO()):
                judge.qa("all", destination)
                manifest = json.loads((destination / "qa_manifest_private.json").read_text())
                self.assertEqual(manifest["packet_sha256"], generation.sha256_file(destination / "qa_packet.jsonl"))
                self.assertEqual(manifest["source_file_sha256"]["raw/openai.jsonl"], generation.sha256_file(output / "openai.jsonl"))
                self.assertNotIn("PRIVATE_MODEL", (destination / "qa_packet.md").read_text())
                original = (destination / "qa_packet.jsonl").read_bytes()
                with self.assertRaises(FileExistsError):
                    judge.qa("all", destination)
                self.assertEqual((destination / "qa_packet.jsonl").read_bytes(), original)

    def test_orphan_scored_cell_is_rejected(self):
        annotations, prompts, sources, scores = self.fixture()
        with self.assertRaisesRegex(RuntimeError, "no source generation"):
            judge.build_qa_records({"snapshot_id": "S"}, annotations, prompts, sources[1:], scores)


if __name__ == "__main__":
    unittest.main()
