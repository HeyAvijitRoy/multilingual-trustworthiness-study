#!/usr/bin/env python3
"""Read-only operational report; never sends model requests or edits the freeze."""
import json
from collections import Counter
from pathlib import Path
import prelim_four as four
from api_budget import BudgetLedger,NANO
from prelim_four_judge import ScoringContext


def report():
    ctx=ScoringContext(four.CONFIG,four.AMENDMENT/'FREEZE.json')
    ctx.frozen()
    ledger=BudgetLedger(ctx.config,ctx.manifest,'scoring')
    with ledger.locked():
        holds,settled=ledger.state(ledger.events())
        # Keep the snapshot internally consistent while another worker settles.
        paid=sum(r['charged_nano_usd'] for r in settled.values())
        reserved=sum(r['reserved_nano_usd'] for r in holds.values())
        usage={'currency':'USD','cap_usd':ledger.cap/NANO,'conservative_settled_estimate_usd':paid/NANO,
               'in_progress_or_uncertain_reservations_usd':reserved/NANO,
               'remaining_uncommitted_usd':(ledger.cap-paid-reserved)/NANO,
               'settled_requests':len(settled),'held_requests':len(holds),
               'input_tokens':sum(r['usage']['input_tokens'] for r in settled.values()),
               'output_tokens_including_reasoning':sum(r['usage']['output_tokens'] for r in settled.values())}
    def rows(path):return four.historical.read_jsonl_records(path)
    cal=rows(ctx.cal_records)
    generations={p:dict(Counter(r['status'] for r in rows(ctx.root/(p+'.jsonl')))) for p in four.PARTITIONS}
    scores={p:len(rows(ctx.root/'scores'/(p+'.jsonl'))) for p in four.PARTITIONS}
    quota=rows(four.ROOT/'.local/google_project_quota/requests.jsonl')
    google=Counter(r.get('pacific_day') for r in quota if r.get('type')=='reserved')
    return {'at_utc':four.historical.utc_now(),'protocol_id':ctx.config['protocol_id'],
            'freeze_sha256':four.digest(ctx.manifest_path),'budget':usage,
            'calibration_completed_fixtures':len(cal),'calibration_planned_fixtures':30,
            'calibration_gate':ctx.gate() if ctx.cal_report.exists() else {'gate_pass':False,'reason':'actual calibration incomplete'},
            'raw_generation_records_by_status':generations,'scoring_records':scores,
            'google_request_reservations_by_pacific_day':dict(google),
            'independent_human_QA':'pending; no audited scientific conclusions authorized before completion'}

if __name__=='__main__':print(json.dumps(report(),indent=2))
