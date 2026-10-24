#!/usr/bin/env python3
"""Read-only scenario budget, not a tokenizer count, quote, or spending approval."""
from __future__ import annotations

import argparse
import json
import math

import prelim_eval_157 as generation
import prelim_judge_157 as judge


def estimate_v02():
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


def estimate():
    import prelim_four as four
    from cloud_smoke_four import PROMPTS
    cfg,manifest,freeze,annotations,prompts=four.verify_candidate()
    cells=four.cells_for(cfg,freeze,annotations,prompts,'openai')
    prompt_bytes=[len((cfg['system_prompt']+c['prompt_text']).encode()) for c in cells]
    rubric_bytes=[len(judge.scoring_prompt(c['task_id'],c['prompt_text'],'',annotations[c['task_id']]).encode()) for c in cells]
    fixtures=judge.load_fixture_context(annotations,prompts)
    fixture_bytes=[len(judge.scoring_prompt(c['task_id'],c['prompt_text'],c['response_text'],c['rec']).encode()) for c in fixtures]
    smoke_bytes=[len((cfg['system_prompt']+p).encode()) for p in PROMPTS.values()]
    results=[]
    for name,divisor,overhead,output,judge_output,retokenization in [
        ('optimistic',4,64,256,512,1),('typical_planning',2,128,2048,2048,1.5),
        ('conservative_envelope',1,1024,32768,8192,4)]:
        inputs=sum(math.ceil(n/divisor)+overhead for n in prompt_bytes)
        sol=(inputs*2+471*output*10)/1e6
        def judge_cost(sizes):
            total=0
            for n in sizes:
                large=n>272000
                total+=(n*2.5*(2 if large else 1)+judge_output*15*(1.5 if large else 1))/1e6
            return total
        score_inputs=[math.ceil(n/divisor)+overhead+math.ceil(output*retokenization) for n in rubric_bytes]*4
        calibration=judge_cost([math.ceil(n/divisor)+overhead for n in fixture_bytes])
        scoring=judge_cost(score_inputs)
        # Each of three Sol probes retains the study cap but requests a short
        # sentence. Planning counts at least 256 billed tokens; conservative
        # allows all 32768, including reasoning. Gemini is conditionally free.
        smoke_output=32768 if name=='conservative_envelope' else 256
        smoke=(sum(math.ceil(n/divisor)+overhead for n in smoke_bytes)*2+len(smoke_bytes)*smoke_output*10)/1e6
        total=sol+calibration+scoring+smoke
        paid_google_fallback_not_authorized=(inputs*.75+471*output*3.75)/1e6
        results.append({'scenario':name,'input_proxy_bytes_per_token':divisor,'overhead_tokens_per_call':overhead,
            'generation_billed_output_tokens_per_cell':output,'judge_billed_output_tokens_per_call':judge_output,
            'judge_response_retokenization_factor':retokenization,'generation_input_tokens_proxy':inputs,
            'openai_generation_usd':round(sol,2),'google_generation_usd_if_actual_free_tier':0,
            'judge_calibration_30_usd':round(calibration,2),'judge_scoring_1884_usd':round(scoring,2),
            'openai_three_synthetic_smokes_usd':round(smoke,2),'google_three_smokes_usd_if_free_tier':0,
            'total_paid_one_attempt_usd_if_google_free':round(total,2),
            'four_billed_attempts_envelope_usd_if_google_free':round(total*4,2),
            'hypothetical_paid_google_generation_usd_not_authorized':round(paid_google_fallback_not_authorized,2)})
    prior_gpu=four.read(four.ROOT/'data/evaluation/amendments/prelim-157-four-model-0.2/gpu/BENCHMARK_SUMMARY.json')
    return {'status':'planning-only-not-spending-authorization','protocol_id':cfg['protocol_id'],
        'pricing_checked_date':'2026-10-23','openai_model':'gpt-6.1-sol','google_model':'gemini-3.8-flash',
        'primary_judge':'gpt-5.4-2026-03-05','openai_generation_calls':471,'google_generation_calls':471,
        'local_generation_calls':942,'calibration_calls':30,'scoring_calls':1884,'synthetic_cloud_calls':{'openai':3,'google':3},
        'prior_200_usd_cap':'reference only; no authorization recorded',
        'actual_paid_calls':0,'actual_paid_api_expenditure_usd':0,
        'standard_prices_per_million_tokens':{'gpt-6.1-sol':{'input':2,'output':10},
              'gpt-5.4-2026-03-05':{'input':2.5,'output':15,'long_input_threshold':272000,'long_input_multiplier':2,'long_output_multiplier':1.5},
              'gemini-3.8-flash':{'free_input':0,'free_output':0,'conditional_on_actual_project_free_tier':True,
                'paid_input_through_2026_12_31':.75,'paid_output_through_2026_12_31':3.75,'paid_fallback_authorized':False}},
        'measured_prompt_system_utf8_bytes':sum(prompt_bytes),'largest_prompt_system_utf8_bytes':max(prompt_bytes),
        'snapshot_sha256':four.digest(generation.FREEZE_PATH),
        'quota_days_examples_not_account_limits':[{'hypothetical_rpd':r,'minimum_days_471_plus_3_smokes':math.ceil(474/r),
                       'four_attempt_envelope_days':math.ceil(1896/r)} for r in (20,50,100,250,500)],
        'local_compute':{'paid_api_usd':0,'hourly_hardware_energy_rate_usd':None,
            'projected_decode_hours_at_2048_tokens_per_response':{
                m['provenance']['model_id']:m['decode_only_projection_hours_for_471_responses']['2048'] for m in prior_gpu['models']},
            'note':'Measured rates, projected resource use. Excludes prefill, startup, I/O, retries and long-context slowdown; local cost not valued.'},
        'assumptions':['UTF-8/token proxies are planning assumptions, not cloud-tokenizer measurements.',
            'All billed output includes hidden reasoning; judge retokenization is a conservative visible-response proxy.',
            'Google zero cost depends on actual project free-tier eligibility; unknown limits never become assumed quotas.',
            'Free tier may require multiple days; other project traffic and failed attempts consume headroom.',
            'Four-attempt envelopes assume every attempt is billed; no lowering output limits to meet budget.',
            'Taxes, regional pricing, independent human review and local compute fees excluded.',
            'No costs here authorize execution or guarantee an invoice ceiling.'],
        'sources':['https://developers.openai.com/api/docs/models/gpt-6.1-sol',
             'https://developers.openai.com/api/docs/models/gpt-5.4','https://developers.openai.com/api/docs/pricing',
             'https://ai.google.dev/gemini-api/docs/pricing','https://ai.google.dev/gemini-api/docs/rate-limits'],
        'scenarios':results}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--legacy-v02',action='store_true')
    args=parser.parse_args();print(json.dumps(estimate_v02() if args.legacy_v02 else estimate(),indent=2))
