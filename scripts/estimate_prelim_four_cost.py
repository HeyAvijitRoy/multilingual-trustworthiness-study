#!/usr/bin/env python3
"""Read-only scenario budget, not a tokenizer count, quote, or spending approval."""
from __future__ import annotations

import json
import math

import prelim_eval_157 as generation
import prelim_judge_157 as judge


def estimate():
    freeze, config, annotations, prompts = generation.verify_freeze()
    cells = generation.build_cells(freeze, annotations, prompts, "openai", config["request_order_seed"])
    system = config["system_prompt"]
    # Measured UTF-8 lengths, not model token counts. Provider tokenizers and
    # native message overhead have not been queried with this account's keys.
    prompt_bytes = [len((system + c["prompt_text"]).encode()) for c in cells]
    rubric_bytes = [len(judge.scoring_prompt(c["task_id"], c["prompt_text"], "", annotations[c["task_id"]]).encode())
                    for c in cells]
    fixture_contexts = judge.load_fixture_context(annotations, prompts)
    calibration_bytes = [len(judge.scoring_prompt(c["task_id"], c["prompt_text"], c["response_text"], c["rec"]).encode())
                         for c in fixture_contexts]
    scenarios = []
    # The envelope allows one input token per UTF-8 byte, 1024 message-overhead
    # tokens/call, full output caps and 4x response retokenization at the judge.
    # This is a conditional planning envelope, not a mathematically guaranteed
    # bound across undocumented tokenizer/provider changes or future prices.
    for name, divisor, overhead, output_tokens, judge_tokens, retokenization in [
        ("optimistic", 4, 64, 256, 512, 1),
        ("typical_planning", 2, 128, 2048, 2048, 1.5),
        ("conservative_envelope", 1, 1024, 32768, 8192, 4),
    ]:
        inputs = sum(math.ceil(n / divisor) + overhead for n in prompt_bytes)
        gen_out = 471 * output_tokens
        judge_inputs = [math.ceil(n / divisor) + overhead + math.ceil(output_tokens * retokenization)
                        for n in rubric_bytes] * 4
        judge_inputs.extend(math.ceil(n / divisor) + overhead for n in calibration_bytes)
        # Current OpenAI long-input premium is applied per request if needed.
        judge_cost = sum(n * (4 if n > 272_000 else 2) / 1e6 +
                         judge_tokens * (15 if n > 272_000 else 10) / 1e6 for n in judge_inputs)
        openai = (inputs * 10 + gen_out * 50) / 1e6
        google_intro = (inputs * 2 + gen_out * 10) / 1e6
        google_standard = (inputs * 4 + gen_out * 20) / 1e6
        scenarios.append({"scenario": name, "input_proxy_bytes_per_token": divisor,
                          "message_overhead_tokens_per_request": overhead,
                          "generation_billed_output_tokens_per_cell": output_tokens,
                          "judge_billed_output_tokens_per_cell": judge_tokens,
                          "generation_input_tokens_per_cloud_model_proxy": inputs,
                          "judge_response_retokenization_factor": retokenization,
                          "openai_generation_usd": round(openai, 2),
                          "google_generation_intro_usd": round(google_intro, 2),
                          "google_generation_after_intro_usd": round(google_standard, 2),
                          "judge_1884_plus_30_calibration_usd": round(judge_cost, 2),
                          "total_intro_one_attempt_usd": round(openai + google_intro + judge_cost, 2),
                          "total_after_intro_one_attempt_usd": round(openai + google_standard + judge_cost, 2),
                          "four_billed_attempts_envelope_intro_usd": round(4 * (openai + google_intro + judge_cost), 2)})
    return {"status": "scenario-estimate-only-no-paid-calls", "pricing_checked_date": "2026-10-23",
            "snapshot_sha256": generation.sha256_file(generation.FREEZE_PATH),
            "prompt_instances_per_cloud_model": 471, "judge_calls": 1914,
            "measured_prompt_and_system_utf8_bytes": sum(prompt_bytes),
            "largest_prompt_and_system_utf8_bytes": max(prompt_bytes),
            "measured_empty_response_scoring_prompt_utf8_bytes_per_panel_model": sum(rubric_bytes),
            "sources": ["https://developers.openai.com/api/docs/models/gpt-6-astra",
                        "https://developers.openai.com/api/docs/models/gpt-6.1-sol",
                        "https://developers.openai.com/api/docs/pricing",
                        "https://ai.google.dev/gemini-api/docs/pricing"],
            "assumptions": ["Standard text pricing, USD, no tools/cache discounts, no tax/regional premium",
                            "Google intro $2/$10 per million input/output through 2026-11-30; $4/$20 afterwards",
                            "OpenAI Astra $10/$50, Sol judge $2/$10 per million input/output",
                            "All output estimates include hidden reasoning, not just visible text",
                            "Exact cloud token counts, access, quotas and billed retry behavior unverified",
                            "No expected-output distribution measured on study prompts",
                            "Envelope conditional on stated token/overhead/price assumptions; not a hard invoice ceiling",
                            "Local machine compute/energy and human review costs excluded"],
            "scenarios": scenarios}


if __name__ == "__main__":
    print(json.dumps(estimate(), indent=2))
