#!/usr/bin/env python3
"""Export objective, dated collection metadata; never read labels or call APIs."""
import hashlib
import json
from pathlib import Path
import statistics
import generation_only_v04 as gen

D=gen.ROOT/'manuscript/acm_trust2027'


def export():
    snapshot=gen.report()
    root=gen.four.output_root(gen.four.read(gen.BASE_CONFIG))
    for partition,model in snapshot['models'].items():
        rows=gen.four.historical.read_jsonl_records(root/(partition+'.jsonl'))
        values=[r['latency_seconds'] for r in rows if r['status']=='success']
        model['latency_seconds']={'minimum':min(values),'median':statistics.median(values),'maximum':max(values)} if values else None
        model['raw_response_file_sha256']=hashlib.sha256((root/(partition+'.jsonl')).read_bytes()).hexdigest() if (root/(partition+'.jsonl')).exists() else None
        attempts=gen.four.historical.read_jsonl_records(root/'attempts'/(partition+'.jsonl'))
        model['failed_attempts']=sum(r['status'] not in ('started','success') for r in attempts)
    progress=root/'generation_only_v04/progress.json'
    if progress.exists():
        current=json.loads(progress.read_text())
        snapshot['controller_workers_last_observed']=current.get('workers',{})
        snapshot['controller_workers_observed_at_utc']=current['at_utc']
    snapshot['raw_file_hash_note']='Non-atomic live-file hashes identify bytes read at export; files remain append-only and continue growing. Cell counts use validated complete records read earlier during this snapshot.'
    snapshot['manuscript_status']='partial collection metadata only; production scoring and independent study-response QA pending'
    (D/'GENERATION_SNAPSHOT.json').write_text(json.dumps(snapshot,indent=2)+'\n')
    lines=['# Exploratory generation metadata', '', 'Snapshot: '+snapshot['at_utc']+'. Raw collection continues after this checkpoint.', '',
           'Primary target: **1,413** responses (157 tasks × three languages × three models). Exploratory Gemini target: **60** responses (20 prospectively matched tasks × three languages). Each cell is an independent stateless request. Completion here means a preserved provider response; it does not establish semantic task completion.', '',
           '| Model | Role | EN | BN | BN-CS | Preserved / planned | Failed response records | Failed attempts |',
           '|---|---|---:|---:|---:|---:|---:|---:|']
    for model in snapshot['models'].values():
        c=model['by_language'];lines.append(f"| {model['model_id']} | {model['role']} | {c['en']} | {c['bn']} | {c['bn_cs']} | {model['success']} / {model['planned']} | {model['failed_response_records']} | {model['failed_attempts']} |")
    budget=snapshot['budget']
    lines += ['',f"Paid cap: USD {budget['cap_usd']:.2f}. Conservative usage-derived settled estimate: USD {budget['settled_usage_estimate_usd']:.9f}; outstanding maximum-cost holds: USD {budget['reserved_or_uncertain_usd']:.9f}; uncommitted: USD {budget['remaining_uncommitted_usd']:.9f}. The prior USD 0.542045 is included. USD 80 is protected for later validation and scoring. These are estimates, not invoices.",'',
              'Gemini remains Free tier only (5 RPM, 250,000 input TPM, 20 RPD); its multi-day schedule does not gate primary completion. The conditional 4,500-response full benchmark has not started.', '',
              '**Production RIU/safety scoring is blocked.** The original safety-check calibration remains 25/30 against 30/30. R1 adjudication, independent judge validation after fixture exposure and later independent study-response QA remain outstanding. No language effects, model rankings, omission rates or validated trustworthiness findings are reported.', '',
              'The JSON companion includes finish-status counts, truncation and empty-text flags, visible character counts, token usage, latency and source hashes. These characterize collection only. Raw outputs, detailed attempts and provider payloads remain preserved locally under `.local/prelim_157_four_v03/`; credentials and private R1 materials are excluded from this public summary.', '',
              'Staff can refresh this checkpoint without API requests using `python3 scripts/snapshot_generation_v04.py`. A final submission must retain its exact evidence cutoff and reconcile incomplete cells.']
    (D/'GENERATION_STATUS.md').write_text('\n'.join(lines)+'\n')
    claims=json.loads((D/'VERIFIED_FINDINGS.json').read_text())
    claims['as_of_local_date']='2026-10-24';claims['status']='raw-generation-active-production-scoring-blocked'
    claims['r1_review'].update(status='returned-preserved-compared-adjudication-pending',returned_assessment_rows=6,adjudication_completed=False)
    claims['r1_review'].pop('decisions_filled',None);claims['r1_review'].pop('blank_assessment_rows',None)
    claims['planned_study'].update(models=3,responses=1413,completed_generations=snapshot['primary_completed'],exploratory_model='gemini-3.8-flash',exploratory_tasks=20,exploratory_responses=60,completed_exploratory_generations=snapshot['exploratory_completed'],full_study_responses=4500,full_study_authorized=False,completed_scoring_records=0)
    claims['operational_limits'].update(conservative_accounted_usd=budget['settled_usage_estimate_usd'],outstanding_holds_usd=budget['reserved_or_uncertain_usd'],remaining_uncommitted_usd=budget['remaining_uncommitted_usd'],generation_phase_ceiling_usd=20,protected_evaluation_usd=80,budget_ledger_unchanged=False,additional_paid_API_calls_this_workflow=budget['settled_requests']+budget['held_requests']-33)
    claims['generation_snapshot_at_utc']=snapshot['at_utc']
    for source in [gen.MANIFEST,gen.SCOPE]:claims['source_sha256'][str(source.relative_to(gen.ROOT))]=gen.four.digest(source)
    (D/'VERIFIED_FINDINGS.json').write_text(json.dumps(claims,indent=2)+'\n')
    return snapshot

if __name__=='__main__':
    result=export()
    print(json.dumps({k:result[k] for k in ('at_utc','primary_completed','exploratory_completed','budget')},indent=2))
