#!/usr/bin/env python3
"""Offline packet audit and post-return comparison. Never rates or calls models."""
import argparse
import csv
from datetime import date
import hashlib
import io
import json
import os
from pathlib import Path
import re

import prelim_four as four
from prelim_four_judge import ScoringContext
import prelim_judge_157 as judge
from prepare_v03_r1_packet import PACKET,PRIVATE,FILES,FORM_FIELDS,COMPARE_FIELDS,write_private


def read_csv(path):
    with Path(path).open(encoding='utf-8-sig',newline='') as handle:
        reader=csv.DictReader(handle);rows=list(reader)
        return reader.fieldnames,rows


def validate():
    ctx=ScoringContext(four.CONFIG,four.AMENDMENT/'FREEZE.json');ctx.frozen()
    gate=ctx.gate()
    assert not gate['gate_pass'] and gate['safety_task_check_exact']==25/30
    mapping=four.read(PRIVATE/'mapping.json')
    assert mapping['source_freeze_sha256']==four.digest(ctx.manifest_path)
    assert mapping['source_key_sha256']==four.digest(judge.ANSWER_KEY)
    assert mapping['source_sheet_sha256']==four.digest(ctx.cal_sheet)
    assert (PRIVATE.stat().st_mode&0o777)==0o700
    assert ((PRIVATE/'mapping.json').stat().st_mode&0o777)==0o600
    assert set(p.name for p in PACKET.iterdir())==set(FILES)
    assert mapping['packet_sha256']=={n:four.digest(PACKET/n) for n in FILES}
    body=(PACKET/'R1_REVIEW_PACKET.md').read_text(encoding='utf-8')
    public_text='\n'.join((PACKET/n).read_text(encoding='utf-8') for n in FILES if n.endswith('.md'))
    contexts={c['fixture_id']:c for c in judge.load_fixture_context(ctx.annotations,ctx.prompts)}
    key={(r['fixture_id'],r['item_id']):r for r in judge.read_csv(judge.ANSWER_KEY)}
    scores={(r['fixture_id'],r['item_id']):r for r in judge.read_csv(ctx.cal_sheet)}
    expected=set()
    for c in contexts.values():
        for check in c['rec'].get('task_checks',[]):
            k=c['fixture_id'],check['id']
            if c['rec'].get('safety_relevance','none')!='none' and float(key[k]['intended_score'])!=float(scores[k]['score']):expected.add(k)
    actual=set();ids=set();form_keys=set();riu_count=0
    case_blocks=re.split(r'^## (R1-[0-9A-F]{8})\n',body,flags=re.M)
    assert len(case_blocks)==11
    block_by_id=dict(zip(case_blocks[1::2],case_blocks[2::2]))
    for case in mapping['cases']:
        rid=case['review_id'];assert re.fullmatch(r'R1-[0-9A-F]{8}',rid) and rid not in ids;ids.add(rid)
        c=contexts[case['fixture_id']];block=block_by_id[rid]
        for name in ('prompt_text','response_text'):
            value=c[name];assert value in block
            assert hashlib.sha256(value.encode()).hexdigest()==case['prompt_sha256' if name=='prompt_text' else 'response_sha256']
        assert c['rec']['task_objective'] in block
        for constraint in c['rec'].get('constraints',[]):assert constraint in block
        for spec in judge.item_specs(c['rec']):
            assert spec['item_id'] in block
            if spec['kind']=='riu':
                riu_count+=1
                assert spec['description'] in block and spec['rationale'] in block
                assert f'**Criticality:** {spec["criticality"]}.' in block
                assert f'**Scoring mode:** {spec["scoring_mode"]}.' in block
                for anchor in spec['scoring_rule'].values():
                    if anchor is not None:assert anchor in block
            else:
                assert spec['rule'] in block;form_keys.add((rid,spec['item_id']))
        for item in case['selected_item_ids']:actual.add((case['fixture_id'],item))
        for item in case['checks']:
            ident=case['fixture_id'],item['public_check_id']
            assert item['reference_label']==key[ident]['intended_score']
            assert item['judge_prediction']==scores[ident]['score']
        for secret in (case['fixture_id'],case['task_id']):assert not re.search(r'\b'+re.escape(secret)+r'\b',public_text)
    assert expected==actual and len(actual)==5 and len(ids)==5
    for token in ('gpt-5.4','gpt-6.1','gemini','Qwen','Gemma','frozen_intended_score','actual_judge_rating','disagreement','answer_key','0.9605','25/30','97/98'):
        assert token.casefold() not in public_text.casefold(),token
    fields,rows=read_csv(PACKET/'R1_REVIEW_FORM.csv');assert tuple(fields)==FORM_FIELDS
    assert len(rows)==6 and len({(r['review_id'],r['check_id']) for r in rows})==6
    assert {(r['review_id'],r['check_id']) for r in rows}==form_keys
    for r in rows:
        assert r['reviewer']=='R1'
        assert all(not r[k] for k in fields if k not in ('review_id','check_id','reviewer'))
    fields,rows=read_csv(PACKET/'POST_REVIEW_COMPARISON_TEMPLATE.csv');assert tuple(fields)==COMPARE_FIELDS
    assert {(r['review_id'],r['check_id']) for r in rows}==form_keys and len(rows)==6
    assert all(not r[k] for r in rows for k in fields if k not in ('review_id','check_id'))
    for n in FILES:
        text=(PACKET/n).read_text(encoding='utf-8');assert '\ufffd' not in text and '\x00' not in text
        assert b'\r' not in (PACKET/n).read_bytes(), 'public packet must retain pinned LF bytes through Git'
    assert (PACKET/'README.md').read_text().count('](R1_REVIEW_PACKET.md)')==1
    assert 'No code, terminal or model calls are needed' in (PACKET/'README.md').read_text()
    # Existing labels in repository history remain outside the packet. Technical
    # checks cannot establish what R1 has previously seen.
    return {'status':'PASS','review_cases':5,'applicable_check_rows':6,'source_RIUs_included':riu_count,
            'prompts_responses_constraints_and_rubric_anchors':'exact source text verified',
            'case_selection_and_private_mapping':'all five source task-check cases, one-to-one; no public mapping',
            'first_pass_and_adjudication_decisions':'all blank',
            'private_directory_permissions':'0700; mapping 0600; ignored by Git',
            'accessibility':'UTF-8, meaningful headings, case index links, spreadsheet CSV; no code required',
            'blinding_boundary':'standalone four-file packet only; no source IDs, judge identity/ratings, reference labels or selection details in its prose',
            'limitation':'full-repository/history access can reveal source material; distribute only these four files for first-pass assessment',
            'packet_sha256':{n:four.digest(PACKET/n) for n in FILES}}


def validate_return(rows,expected):
    if len(rows)!=len(expected) or {(r.get('review_id'),r.get('check_id')) for r in rows}!=expected:
        raise ValueError('returned form must contain exactly the six unique expected case/check rows')
    for r in rows:
        if set(r)!=set(FORM_FIELDS) or any(not isinstance(v,str) for v in r.values()):raise ValueError('malformed CSV row or changed fields')
        if r.get('reviewer')!='R1':raise ValueError('Reviewer R1 identifier required')
        if r.get('assessment') not in {'0','1','unresolved'}:raise ValueError('assessment must be 0, 1 or unresolved')
        if not r.get('rationale','').strip() or not r.get('evidence_quote','').strip():raise ValueError('rationale and evidence quote or description of absence required')
        if r.get('rubric_ambiguity') not in {'yes','no','unsure'}:raise ValueError('rubric ambiguity must be yes, no or unsure')
        if r['rubric_ambiguity']!='no' and not r.get('rubric_ambiguity_details','').strip():raise ValueError('describe rubric ambiguity')
        if r['assessment']=='unresolved' and r['rubric_ambiguity']=='no':raise ValueError('explain unresolved assessment as ambiguous/unsure')
        date.fromisoformat(r.get('review_date',''))
    return rows


def compare(returned):
    # A completed form is necessary; no labels are exposed into public files.
    validate();mapping=four.read(PRIVATE/'mapping.json')
    expected={(c['review_id'],i['public_check_id']) for c in mapping['cases'] for i in c['checks']}
    returned=Path(returned).resolve()
    if returned==PACKET/'R1_REVIEW_FORM.csv':raise ValueError('preserve original blank template; supply returned completed file')
    raw=returned.read_bytes();fields,rows=read_csv(returned)
    if tuple(fields)!=FORM_FIELDS:raise ValueError('returned CSV headers changed')
    validate_return(rows,expected)
    ident=hashlib.sha256(raw).hexdigest();dest=PRIVATE/'returns'/ident
    if dest.exists():raise ValueError('returned assessment already preserved; do not overwrite')
    dest.mkdir(parents=True,mode=0o700)
    os.chmod(dest.parent,0o700)
    fd=os.open(dest/'R1_REVIEW_FORM_COMPLETED.csv',os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
    with os.fdopen(fd,'wb') as out:out.write(raw)
    ratings={(r['review_id'],r['check_id']):r for r in rows};output=[]
    for c in mapping['cases']:
        for item in c['checks']:
            row=ratings[c['review_id'],item['public_check_id']];r1=row['assessment'];ref=str(int(float(item['reference_label'])));pred=str(int(float(item['judge_prediction'])))
            rowout={**dict.fromkeys(COMPARE_FIELDS,''),'review_id':c['review_id'],'check_id':item['public_check_id'],
                'returned_form_sha256':ident,'first_pass_assessment':r1,'first_pass_rationale':row['rationale'],
                'reference_label':ref,'judge_prediction':pred,'rubric_ambiguity':row['rubric_ambiguity'],
                'comparison':'unresolved' if r1=='unresolved' else f'R1/reference={r1==ref}; R1/judge={r1==pred}',
                'adjudication_status':'pending'}
            output.append(rowout)
    fd=os.open(dest/'comparison.csv',os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
    with os.fdopen(fd,'w',encoding='utf-8',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=COMPARE_FIELDS);writer.writeheader();writer.writerows(output)
    write_private(dest/'receipt.json',{'returned_form_sha256':ident,'review_id_count':len(mapping['cases']),'assessment_rows':len(rows),
        'status':'comparison-prepared-adjudication-pending','authentication':'structural validation only; does not establish authorship, independence or exposure history',
        'adjudication':'all adjudicated labels and recommendations remain blank; prepare documented recommendations from actual returned rationales before any decision'})
    return {'status':'comparison-prepared-adjudication-pending','private_output':str(dest.relative_to(four.ROOT))}


def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='command',required=True)
    sub.add_parser('validate');p=sub.add_parser('compare');p.add_argument('--returned',type=Path,required=True)
    args=parser.parse_args()
    print(json.dumps(validate() if args.command=='validate' else compare(args.returned),indent=2))

if __name__=='__main__':main()
