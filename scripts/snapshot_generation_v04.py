#!/usr/bin/env python3
"""Export collection metadata and validated aggregate review status; no API calls."""
import hashlib
from datetime import datetime, timezone
import gemini_quota
import json
from pathlib import Path
import statistics
import generation_only_v04 as gen

D=gen.ROOT/'manuscript/acm_trust2027'


def current_adjudication_status():
    path=gen.ROOT/'data/evaluation/remediation/v03_R1_adjudication/RETURN_STATUS.json'
    source=gen.ROOT/'data/evaluation/reviews/v03_calibration_R1/adjudication/R1_ADJUDICATION_FORM_COMPLETED.csv'
    if not path.exists() or not source.exists():return None
    status=json.loads(path.read_text())
    if status.get('status')!='returned-validated-comparison-prepared' or status.get('returned_form_sha256')!=gen.four.digest(source):
        raise RuntimeError('adjudication return changed or is not validated; inspect before reporting current review state')
    if status.get('production_scoring_authorized') is not False:raise RuntimeError('review return cannot authorize production scoring')
    return status


def export():
    snapshot=gen.report()
    adjudication=current_adjudication_status()
    if adjudication:
        complete=adjudication['resolved_rows']==adjudication['disputed_judgments']==7 and adjudication['unresolved_rows']==0
        snapshot['r1_adjudication_return']={k:adjudication[k] for k in ('returned_form_sha256','resolved_rows','unresolved_rows','reference_matches','revisions_from_first_pass')}
        if complete:
            snapshot['scoring_blockers']=['original safety-check calibration 25/30 versus 30/30','prospective scoring procedure and independent judge validation pending','validated scoring integration and subsequent independent study-response QA pending']
            snapshot['review_status_note']='Current adjudication status comes from the separately validated return; frozen controller blocker text retains historical wording. No scoring gate has been changed.'
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
    config=gen.four.read(gen.BASE_CONFIG)
    google=next(m for m in config['models'] if m['partition']=='google')
    quota=gemini_quota.QuotaLedger(gen.ROOT/google['quota_config'])
    events=quota.own(gen.four.historical.read_jsonl_records(quota.path))
    now=quota.clock();day=datetime.fromtimestamp(now,gemini_quota.PACIFIC).date().isoformat()
    used=sum(r['type']=='reserved' and r['pacific_day']==day for r in events)
    snapshot['gemini_project_quota']={'pacific_day':day,'requests_reserved_today':used,'daily_limit':20,'remaining_daily_request_capacity':max(0,20-used),'next_daily_reset_utc':datetime.fromtimestamp(gemini_quota.next_day(now),timezone.utc).isoformat(),'includes_prior_probes_and_failed_attempts':True,'external_usage_beyond_this_shared_ledger_observable':False}
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
              '**Production RIU/safety scoring is blocked.** The original safety-check calibration remains 25/30 against 30/30. Independent judge validation after fixture exposure, versioned scoring integration and later independent study-response QA remain outstanding. No language effects, model rankings, omission rates or validated trustworthiness findings are reported.', '',
              'The JSON companion includes finish-status counts, truncation and empty-text flags, visible character counts, token usage, latency and source hashes. These characterize collection only. Raw outputs, detailed attempts and provider payloads remain preserved locally under `.local/prelim_157_four_v03/`; credentials and private R1 materials are excluded from this public summary.', '',
              'Staff can refresh this checkpoint without API requests using `python3 scripts/snapshot_generation_v04.py`. A final submission must retain its exact evidence cutoff and reconcile incomplete cells.']
    if adjudication:
        lines += ['',f"R1's second-stage return has {adjudication['resolved_rows']} resolved decisions and {adjudication['unresolved_rows']} unresolved decisions. All seven returned scores support the original references; two revise first-pass decisions. This exposed, selected-case adjudication is not a new calibration estimate or scoring release."]
    (D/'GENERATION_STATUS.md').write_text('\n'.join(lines)+'\n')
    claims=json.loads((D/'VERIFIED_FINDINGS.json').read_text())
    claims['as_of_local_date']='2026-10-24';claims['status']='raw-generation-active-production-scoring-blocked'
    claims['r1_review'].update(status='returned-preserved-compared-adjudication-pending',returned_assessment_rows=6,adjudication_completed=False)
    if adjudication:
        complete=adjudication['resolved_rows']==adjudication['disputed_judgments']==7 and adjudication['unresolved_rows']==0
        claims['r1_review'].update(status='second-stage-return-validated',first_pass_status='preserved-compared',second_stage_status='returned-validated',second_stage_status_source='validated returned CSV and source hash',adjudication_return_received=True,adjudication_completed=complete,new_adjudication_decisions=adjudication['resolved_rows'],adjudication_return_sha256=adjudication['returned_form_sha256'],reference_matches=adjudication['reference_matches'],first_pass_decision_revisions=adjudication['revisions_from_first_pass'])
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
