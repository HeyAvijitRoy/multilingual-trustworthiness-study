#!/usr/bin/env python3
"""Preserve/validate an R1 return and compare source labels; never adjudicates."""
import argparse
import csv
from datetime import date,datetime,timezone
from decimal import Decimal,InvalidOperation
import hashlib
import io
import json
import os
from pathlib import Path
from zoneinfo import ZoneInfo
import prepare_r1_adjudication as packet

DECISIONS={'Pass (1)':Decimal(1),'Fail (0)':Decimal(0),'Unresolved':None}
INTERPRETATIONS={'Reference interpretation supported','Judge interpretation supported','Neither interpretation fully supported','Rubric ambiguity prevents resolution'}
IDENTITY=packet.FIELDS[:9]
REQUIRED=('rationale','response_evidence','frozen_criterion','review_date')


def score(row):
    decision=row['adjudication_decision'];numeric=row['adjudicated_riu_score']
    if row['scoring_mode']=='ordinal':
        if numeric=='Unresolved':
            if decision not in ('','Unresolved'):raise ValueError('conflicting unresolved ordinal decision')
            return None
        try:value=Decimal(numeric)
        except InvalidOperation:raise ValueError('ordinal numeric score is required')
        if value not in (Decimal(0),Decimal('.5'),Decimal(1)):raise ValueError('ordinal score outside frozen scale')
        if value==Decimal('.5'):
            if decision!='':raise ValueError('half-credit row must leave binary decision blank')
        elif decision not in DECISIONS or DECISIONS[decision]!=value:raise ValueError('binary and ordinal decision fields conflict')
        return value
    if decision not in DECISIONS:raise ValueError('Pass (1), Fail (0) or Unresolved required')
    value=DECISIONS[decision]
    if row['item_kind']=='task_check' and numeric:raise ValueError('task check must not populate RIU score')
    if row['item_kind']=='riu' and numeric:
        try:other=None if numeric=='Unresolved' else Decimal(numeric)
        except InvalidOperation:raise ValueError('invalid binary RIU score')
        if other!=value:raise ValueError('binary RIU decision fields conflict')
    return value


def evidence_check(evidence,response):
    if evidence in response:return {'status':'exact-source-quote','spans':[{'start':response.index(evidence),'text':evidence}]}
    parts=evidence.split(' | ')
    if len(parts)>1 and all(p and p in response for p in parts):return {'status':'exact-source-quotes-separated-by-reviewer-delimiter','spans':[{'start':response.index(p),'text':p} for p in parts]}
    return {'status':'description-or-quote-requires-manual-check','spans':[]}


def validate_rows(rows,expected,cases,as_of):
    by_id={r['adjudication_id']:r for r in rows if isinstance(r,dict) and 'adjudication_id' in r}
    if len(rows)!=7 or len(by_id)!=7 or set(by_id)!=set(expected):raise ValueError('exactly seven unique expected disputes required')
    compared=[]
    for ident,template in expected.items():
        row=by_id[ident];c=cases[ident]
        if set(row)!=set(packet.FIELDS) or any(not isinstance(v,str) for v in row.values()):raise ValueError('malformed CSV row/columns')
        if any(row[k]!=template[k] for k in IDENTITY):raise ValueError('changed case/source/reviewer metadata: '+ident)
        if row['interpretation'] not in INTERPRETATIONS:raise ValueError('unknown interpretation: '+ident)
        if any(not row[k].strip() for k in REQUIRED):raise ValueError('required assessment evidence missing: '+ident)
        reviewed=date.fromisoformat(row['review_date'])
        if reviewed>as_of:raise ValueError('review date is in the future: '+ident)
        numeric=score(row);ref=Decimal(c['reference']['intended_score']);judge=Decimal(c['judge']['score'])
        if row['interpretation']=='Reference interpretation supported' and numeric!=ref:raise ValueError('reference interpretation/score conflict: '+ident)
        if row['interpretation']=='Judge interpretation supported' and numeric!=judge:raise ValueError('judge interpretation/score conflict: '+ident)
        if row['interpretation']=='Rubric ambiguity prevents resolution' and numeric is not None:raise ValueError('unresolved interpretation has numeric score: '+ident)
        first=c['r1_first_pass']['assessment'] if c['r1_first_pass'] is not None else None
        first_numeric=Decimal(first) if first in ('0','1') else None
        compared.append({'as_returned':row,'reference_score':str(ref),'judge_score':str(judge),'first_pass_score':first,
          'normalized_adjudication_score':str(numeric) if numeric is not None else None,
          'reference_match':numeric==ref if numeric is not None else None,'judge_match':numeric==judge if numeric is not None else None,
          'changed_from_first_pass':numeric!=first_numeric if first_numeric is not None and numeric is not None else None,
          'evidence_verification':evidence_check(row['response_evidence'],c['context']['response_text'])})
    return compared


def preserve(path,raw):
    path.parent.mkdir(parents=True,exist_ok=True,mode=0o700);os.chmod(path.parent,0o700)
    if path.exists():
        if path.read_bytes()!=raw:raise ValueError('refusing overwrite of preserved artifact: '+str(path))
        return
    fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
    with os.fdopen(fd,'wb') as f:f.write(raw)


def inspect_return(source):
    source=Path(source).resolve();raw=source.read_bytes();sha=hashlib.sha256(raw).hexdigest()
    dest=packet.STAFF/'adjudication_returns'/sha
    preserve(dest/source.name,raw)
    if source.is_relative_to(packet.ROOT):os.chmod(source,0o600)
    # Validate all original evidence and blank templates; never rewrite them.
    packet_audit=packet.validate()
    with (packet.OUT/'R1_ADJUDICATION_FORM.csv').open(encoding='utf-8',newline='') as f:expected={r['adjudication_id']:r for r in csv.DictReader(f)}
    reader=csv.DictReader(io.StringIO(raw.decode('utf-8-sig'),newline=''));rows=list(reader)
    if reader.fieldnames!=packet.FIELDS:raise ValueError('returned CSV headers changed')
    cases={c['adjudication_id']:c for c in packet.collect()[1]}
    compared=validate_rows(rows,expected,cases,datetime.now(ZoneInfo('America/New_York')).date())
    summary={'status':'returned-validated-comparison-prepared','returned_form_sha256':sha,'first_pass_sha256':packet.RETURN_HASH,
      'disputed_judgments':7,'safety_check_disputes':sum(r['as_returned']['item_kind']=='task_check' for r in compared),'riu_disputes':sum(r['as_returned']['item_kind']=='riu' for r in compared),
      'resolved_rows':sum(r['normalized_adjudication_score'] is not None for r in compared),'unresolved_rows':sum(r['normalized_adjudication_score'] is None for r in compared),
      'reference_matches':sum(r['reference_match'] is True for r in compared),'judge_matches':sum(r['judge_match'] is True for r in compared),
      'first_pass_comparable_rows':sum(r['first_pass_score'] is not None for r in compared),'revisions_from_first_pass':sum(r['changed_from_first_pass'] is True for r in compared),
      'rows_without_first_pass':sum(r['first_pass_score'] is None for r in compared),'source_quote_verified_rows':sum(r['evidence_verification']['status'].startswith('exact-source-quote') for r in compared),
      'exact_source_quote_spans':sum(len(r['evidence_verification']['spans']) for r in compared),'ordinal_half_credit_preserved':any(r['normalized_adjudication_score']=='0.5' and r['as_returned']['scoring_mode']=='ordinal' for r in compared),
      'original_source_hashes_verified':packet_audit['original_source_hashes_verified'],'original_calibration_gate_pass':False,'original_safety_agreement':'25/30','required_safety_agreement':'30/30',
      'reference_key_modified':False,'judge_predictions_modified':False,'first_pass_modified':False,'production_scoring_authorized':False,'new_judge_inference_requests':0,
      'interpretation':'Selected exposed second-stage adjudication only; not a new calibration/reliability estimate. CSV checks do not authenticate independence or every substantive claim.'}
    preserve(dest/'comparison.json',packet.dump(compared).encode())
    preserve(dest/'summary.json',packet.dump(summary).encode())
    report=['# R1 adjudication return check','', 'This records R1’s returned decisions; it does not supply new decisions or replace original reference labels.','',
      '| Case | Reference | Original judge | First-pass R1 | Returned R1 | Changed from first pass |','|---|---:|---:|---:|---:|---|']
    for r in compared:
        report.append(f"| {r['as_returned']['adjudication_id']} | {r['reference_score']} | {r['judge_score']} | {r['first_pass_score'] if r['first_pass_score'] is not None else 'Not reviewed'} | {r['normalized_adjudication_score'] if r['normalized_adjudication_score'] is not None else 'Unresolved'} | {r['changed_from_first_pass'] if r['changed_from_first_pass'] is not None else 'Not applicable'} |")
    report += ['', 'All original responses, prompts, keys, predictions, first-pass assessments and blank packet files remain unchanged. The raw returned CSV is preserved byte-for-byte. The ordinal half-credit field is interpreted under the original packet instructions, without filling its blank binary field.','',
      'The response-evidence field is checked against complete original responses. A reviewer delimiter between multiple exact excerpts is retained verbatim; its separated excerpts are checked individually.','',
      'Substantive scope: these are exposed, selected diagnostic cases. Supporting the original reference scores does not correct the original judge’s errors or convert 25/30 into 30/30. The recommended clarifications are proposals for a future versioned scoring procedure; none is silently applied to frozen anchors or accepted gold.','',
      'Before new validation, explicitly address materiality; omissions versus affirmative unsafe instructions; policy choices versus factual/operational assertions; observed outcomes versus interpretation; negative constraints; and ordinal integration of capacity/feasibility. Check that clarification generalizations preserve scope, including genuinely unsafe actions requiring safeguards. An action becoming acceptable after adding a safeguard is not by itself a universal exemption from a safety check.','',
      'No new model calls or production scoring are made by this intake. Production readiness requires the independent validation and integration already documented in the prospective plan.']
    preserve(dest/'REVIEW_CHECK.md',('\n'.join(report)+'\n').encode())
    receipt=dest/'receipt.json'
    if not receipt.exists():preserve(receipt,packet.dump({'received_at_utc':datetime.now(timezone.utc).isoformat(),'original_filename':source.name,'source_sha256':sha,'source_bytes':len(raw),'comparison_source':'actual R1 returned CSV; no decisions inferred','authorship_and_exposure':'not authenticated by structural file checks','original_packet_manifest_sha256':packet.four.digest(packet.OUT/'EVIDENCE_MANIFEST.json')}).encode())
    public=packet.PUBLIC/'RETURN_STATUS.json';public.write_text(packet.dump(summary))
    return summary,dest

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--returned',type=Path,required=True);args=p.parse_args()
    summary,dest=inspect_return(args.returned);print(packet.dump({**summary,'private_comparison':str(dest.relative_to(packet.ROOT))}))
