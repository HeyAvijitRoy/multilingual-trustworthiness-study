#!/usr/bin/env python3
"""Offline evidence assembly and audit. Never decides a case or calls an API."""
import argparse
import ast
import csv
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import prelim_four as four
import prelim_judge_157 as judge
from prelim_four_judge import ScoringContext

ROOT=four.ROOT
OUT=ROOT/'data/evaluation/reviews/v03_calibration_R1/adjudication'
PUBLIC=ROOT/'data/evaluation/remediation/v03_R1_adjudication'
STAFF=ROOT/'.local/review_staff/v03_calibration_R1'
RETURN_HASH='8d78c24304c296fdaccf9137093d5dc61b4e48ec8e09aee587387335d7937fcc'
RETURN=STAFF/'returns'/RETURN_HASH/'R1_REVIEW_FORM_COMPLETED.csv'
def selection():
    return four.read(STAFF/'adjudication_selection.json')

def case_keys():
    return [(r['review_id'],r['fixture_id'],r['item_id']) for r in selection()]

FIELDS=['adjudication_id','review_id','fixture_id','task_id','language','item_id','item_kind','scoring_mode','reviewer','adjudication_decision','adjudicated_riu_score','interpretation','rationale','response_evidence','frozen_criterion','materiality','technical_correctness','ambiguity','recommended_prospective_clarification','additional_evidence_needed','reviewer_comments','review_date']
COMPARISON=['adjudication_id','review_id','item_id','original_reference','original_judge','r1_first_pass','adjudication_decision','adjudicated_riu_score','rationale','reference_comparison','judge_comparison','measurement_version','prospective_action','adjudication_date']


def digest_text(s):return hashlib.sha256(s.encode('utf-8')).hexdigest()
def dump(v):return json.dumps(v,ensure_ascii=False,indent=2)+'\n'
def fence(s):
    marker='`'*max(3,1+max([len(x) for x in re.findall(r'`+',s)] or [0]))
    return marker+'text\n'+s+'\n'+marker+'\n'
def write(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(text,encoding='utf-8');os.chmod(path,0o600)
def rows(path):return judge.read_csv(path)
def rules_literal():
    tree=ast.parse(Path(judge.__file__).read_text())
    fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='scoring_prompt')
    ret=next(n for n in fn.body if isinstance(n,ast.Return))
    return ret.value.values[0].value

def definitions(context,specs):
    out=['**Original task objective:**\n\n',fence(context['rec']['task_objective']),'\n**Original constraints:**\n\n']
    out += [fence(x) for x in context['rec'].get('constraints',[])]
    for item in specs:
        out += ['\n#### '+item['item_id']+'\n\n']
        if item['kind']=='riu':
            out += ['**Criticality:** '+item['criticality']+'. **Scoring mode:** '+item['scoring_mode']+'.\n\n','**Exact requirement:**\n\n',fence(item['description']),'\n**Criticality rationale:**\n\n',fence(item['rationale']),'\n**Frozen anchors:**\n\n']
            for score,anchor in item['scoring_rule'].items():
                if anchor is not None:out += ['**'+score+':**\n\n',fence(anchor)]
        else:out += ['**Exact check wording:**\n\n',fence(item['rule'])]
    return ''.join(out)

def sources():
    ctx=ScoringContext(four.CONFIG,four.AMENDMENT/'FREEZE.json');ctx.frozen()
    assert not ctx.gate()['gate_pass']
    assert four.digest(RETURN)==RETURN_HASH
    contexts={c['fixture_id']:c for c in judge.load_fixture_context(ctx.annotations,ctx.prompts)}
    key={(r['fixture_id'],r['item_id']):r for r in rows(judge.ANSWER_KEY)}
    scores={(r['fixture_id'],r['item_id']):r for r in rows(ctx.cal_sheet)}
    actual={k for k in key if float(key[k]['intended_score'])!=float(scores[k]['score'])}
    assert actual=={(f,i) for _,f,i in case_keys()}
    return ctx,contexts,key,scores

def collect():
    ctx,contexts,key,scores=sources()
    first={(r['review_id'],r['check_id']):r for r in rows(RETURN)}
    mapping=four.read(STAFF/'mapping.json');mapped={c['review_id']:c for c in mapping['cases']}
    records={r['fixture_id']:r for r in four.historical.read_jsonl_records(ctx.cal_records)}
    ledger=four.historical.read_jsonl_records(ctx.root/'judge_requests.jsonl')
    raw=four.historical.read_jsonl_records(ctx.root/'judge_raw/judge_raw.jsonl')
    fixture_rows={r['fixture_id']:r for r in rows(judge.FIXTURES)}
    history_files=[ROOT/'.local/calibration/completed/utf8_2026-10-22/normalized'/f'{r}_sheet.csv' for r in ('R2','R3')]+[ROOT/'.local/calibration/round2/completed/normalized'/f'{r}_sheet.csv' for r in ('R2','R3')]
    result=[]
    for n,(rid,fix,item) in enumerate(case_keys(),1):
        c=contexts[fix];specs=judge.item_specs(c['rec']);spec=next(s for s in specs if s['item_id']==item)
        if n<=5:assert mapped[rid]['fixture_id']==fix and mapped[rid]['task_id']==c['task_id'] and mapped[rid]['selected_item_ids']==[item]
        requests=[r for r in ledger if r['tag']=='calibration:'+fix and r['status']=='received'];assert len(requests)==1
        request=requests[0];provider=[r for r in raw if r['scoring_input_sha256']==request['scoring_input_sha256']];assert len(provider)==1
        response=provider[0]['payload'];assert response['id']==records[fix]['result']['_judge_meta']['response_id']
        original_instructions=response.get('instructions')
        history=[]
        for path in history_files:
            if not path.exists():continue
            for r in rows(path):
                if r.get('fixture_id')==fix and r.get('item_id')==item:history.append({'source':str(path.relative_to(ROOT)),'row':r})
        recovered_path=STAFF/'retrieved_judge_inputs'/(fix+'.prompt.txt')
        recovered=recovered_path.read_text() if recovered_path.exists() else None
        if recovered is not None:assert digest_text(recovered)==request['scoring_input_sha256']
        result.append({'recovered_judge_input':recovered,'adjudication_id':f'ADJ-{n:02}','review_id':rid,'fixture_id':fix,'item_id':item,'context':c,'spec':spec,'all_specs':specs,'reference':key[fix,item],'judge':scores[fix,item],
          'r1_first_pass':first.get((rid,item)),'contextual_first_pass':[{'assessment':v,'reference':key[fix,ch],'judge':scores[fix,ch]} for (review,ch),v in first.items() if review==rid and ch!=item],
          'historical_assessments':history,'fixture_provenance':{k:v for k,v in fixture_rows[fix].items() if k!='response_text'},
          'judge_provenance':records[fix],'judge_original_instructions':original_instructions,'scoring_input_sha256':request['scoring_input_sha256'],
          'judge_request_provenance':{k:v for k,v in request.items() if k!='result'},'question':selection()[n-1]['question'],
          'unavailable_evidence':['Fixture response generator model identifier: not applicable to this constructed fixture; no generation-model record exists.',*(['Complete historic judge input text is unavailable locally and has not been reconstructed.'] if recovered is None else [])]})
    return ctx,result,history_files

def build():
    if OUT.exists():raise RuntimeError('adjudication folder already exists; validate it, do not overwrite')
    ctx,cases,history_files=collect();OUT.mkdir(parents=True,mode=0o700);os.chmod(OUT,0o700)
    source_paths=[ctx.manifest_path,ctx.config_path,ctx.judge_path,ctx.plan_path,ctx.cal_sheet,ctx.cal_records,ctx.cal_report,judge.FIXTURE_PLAN,judge.FIXTURES,judge.ANSWER_KEY,Path(judge.__file__),ROOT/'data/annotations/ANNOTATION_PROTOCOL.md',ROOT/'data/calibration/README.md',ROOT/'data/annotations/review_logs/2026-10-22_calibration_adjudication.md',STAFF/'mapping.json',RETURN,ctx.root/'judge_requests.jsonl',ctx.root/'judge_raw/judge_raw.jsonl',*history_files]
    source_paths += list((STAFF/'retrieved_judge_inputs').glob('*'))
    source_paths += [four.historical.FREEZE_PATH]+[ROOT/x for x in ctx.freeze['annotation_file_pins']]+[ROOT/x for x in ctx.freeze['prompt_corpus_sha256']]
    manifests={str(p.relative_to(ROOT)):{'sha256':four.digest(p),'bytes':p.stat().st_size} for p in sorted(set(source_paths)) if p.is_file()}
    lines=['# Reviewer R1 — second-stage adjudication packet\n\nPrepared October 24, 2026 (America/New_York). Five selected safety-check disputes and two RIU disputes. All new decisions remain blank. Labels and prior assessments are deliberately exposed at this second stage.\n\n',
     '## Evidence origin and availability\n\nOriginal task prompts below are copied verbatim from the frozen corpus. Complete response texts are copied verbatim from fixtures.csv. The calibration README identifies these as constructed scoring test material, not sampled model outputs; author/date metadata are preserved without inventing a generator model. The automated judge is gpt-5.4-2026-03-05, not the response author. The exact original judge input texts were recovered through read-only retrieval of stored response input items and matched against their originally recorded SHA256 hashes. They are included verbatim and were not reconstructed. The retrieval receipt and raw returned input items are preserved separately. Original task prompts and fixture responses are complete.\n\n',
     '## Frozen common scoring instructions\n\nThe following is the literal text prefix of the pinned scoring function, separate from the exact recovered historic judge inputs below. Item-specific rules and complete annotation-protocol materiality criteria follow.\n\n',fence(rules_literal()),'\n## Case index\n\n']
    for c in cases:lines.append(f'- [{c["adjudication_id"]} / {c["review_id"]} / {c["fixture_id"]} / {c["item_id"]}](#{c["adjudication_id"].lower()})\n')
    form=[];comparison=[];case_manifest=[]
    for c in cases:
        context=c['context'];spec=c['spec'];aid=c['adjudication_id']
        lines += [f'\n## {aid}\n\n',f'**Review ID:** {c["review_id"]}. **Original fixture:** {c["fixture_id"]}. **Task:** {context["task_id"]}. **Language:** {context["language"]}. **Disputed item:** {c["item_id"]}.\n\n',
         '### Complete original evaluation task prompt — verbatim\n\n',fence(context['prompt_text']), '\n### Complete original calibration response — verbatim\n\n',fence(context['response_text']),
         '\n### Complete original judge evaluation input — retrieved verbatim, original hash verified\n\n',fence(c['recovered_judge_input']) if c['recovered_judge_input'] is not None else 'Exact original input unavailable; not reconstructed.\n',
         '\n### Original task context and complete applicable item definitions\n\n',definitions(context,c['all_specs']),
         '\n### Original reference assessment — verbatim stored fields\n\n',fence(dump(c['reference'])), '\n### Automated judge assessment and rationale — verbatim stored fields\n\n',fence(dump(c['judge'])),
         '\n### Original R1 first-pass assessment and comments\n\n',fence(dump(c['r1_first_pass'])) if c['r1_first_pass'] else 'No R1 first-pass assessment exists for this RIU. No assessment or comments are manufactured.\n',
         '\n### Contextual first-pass assessments — outside the selected dispute\n\n',fence(dump(c['contextual_first_pass'])) if c['contextual_first_pass'] else 'None for this case.\n',
         '\n### Available earlier assessment evidence — separate historical round\n\n',fence(dump(c['historical_assessments'])) if c['historical_assessments'] else 'No matching earlier assessment row was located in the preserved normalized round-one/round-two sheets.\n',
         '\n### Original provenance and returned judge instructions\n\n',fence(dump({'fixture_origin':c['fixture_provenance'],'judge_provenance':c['judge_provenance'],'judge_request_provenance':c['judge_request_provenance'],'original_returned_instructions':c['judge_original_instructions']})),
         '\n### Adjudication question — explanatory note prepared for this stage\n\n',c['question']+'\n\n',
         '### New adjudication decision fields — intentionally blank\n\nRecord your decision, interpretation, rationale, response evidence and frozen criterion in the CSV row for '+aid+'. Pass (1), Fail (0) and Unresolved are available. Preserve ordinal half credit using the separate RIU-score field, as explained in README.md. No outcome is preselected.\n\n']
        if aid=='ADJ-01':lines += ['### Supporting Microsoft documentation — explanatory notes, not new rubric requirements\n\n', (PUBLIC/'MICROSOFT_SUPPORTING_DOCUMENTATION.md').read_text()+'\n']
        lines += ['### Explicit unavailable evidence\n\n']+['- '+m+'\n' for m in c['unavailable_evidence']]
        row=dict.fromkeys(FIELDS,'');row.update(adjudication_id=aid,review_id=c['review_id'],fixture_id=c['fixture_id'],task_id=context['task_id'],language=context['language'],item_id=c['item_id'],item_kind=spec['kind'],scoring_mode=spec.get('scoring_mode','check'),reviewer='R1');form.append(row)
        r=dict.fromkeys(COMPARISON,'');r.update(adjudication_id=aid,review_id=c['review_id'],item_id=c['item_id']);comparison.append(r)
        evidence='evidence/'+aid+'.json';write(OUT/evidence,dump(c))
        case_manifest.append({'adjudication_id':aid,'review_id':c['review_id'],'fixture_id':c['fixture_id'],'task_id':context['task_id'],'language':context['language'],'item_id':c['item_id'],'item_kind':spec['kind'],'evidence_file':evidence,'evidence_sha256':four.digest(OUT/evidence),
          'prompt_utf8_sha256':digest_text(context['prompt_text']),'response_utf8_sha256':digest_text(context['response_text']),'prompt_characters':len(context['prompt_text']),'response_characters':len(context['response_text']),'r1_first_pass_available':c['r1_first_pass'] is not None,'historic_judge_input_sha256':c['scoring_input_sha256'],'missing_or_inapplicable_evidence':c['unavailable_evidence']})
    lines+=['\n## Appendix A — complete frozen annotation protocol\n\n',fence((ROOT/'data/annotations/ANNOTATION_PROTOCOL.md').read_text()),'\n## Appendix B — complete frozen automated scoring plan\n\n',fence(ctx.plan_path.read_text()),'\n## Appendix C — historical human adjudication record (distinct from current automated gate)\n\n',fence((ROOT/'data/annotations/review_logs/2026-10-22_calibration_adjudication.md').read_text())]
    write(OUT/'R1_ADJUDICATION_PACKET.md',''.join(lines))
    shutil.copyfile(RETURN,OUT/'evidence/R1_FIRST_PASS_ORIGINAL.csv');os.chmod(OUT/'evidence',0o700);os.chmod(OUT/'evidence/R1_FIRST_PASS_ORIGINAL.csv',0o600)
    archive=STAFF/'retrieved_judge_inputs'
    for path in archive.glob('*'):
        shutil.copyfile(path,OUT/'evidence'/path.name);os.chmod(OUT/'evidence'/path.name,0o600)
    write(OUT/'README.md',README)
    write(OUT/'SCORING_VALIDATION_PLAN.md',(PUBLIC/'SCORING_VALIDATION_PLAN.md').read_text())
    # CSVs are authored separately through the spreadsheet artifact runtime.
    write(OUT/'evidence/form_build_inputs.json',dump({'form_fields':FIELDS,'form_rows':form,'comparison_fields':COMPARISON,'comparison_rows':comparison,'public_form_rows':[{**dict.fromkeys(FIELDS,''),'adjudication_id':c['adjudication_id'],'reviewer':'R1'} for c in cases],'public_comparison_rows':[{**dict.fromkeys(COMPARISON,''),'adjudication_id':c['adjudication_id']} for c in cases]}))
    manifest={'prepared_at_utc':four.historical.utc_now(),'status':'prepared-no-adjudication-decisions','original_gate_pass':False,'original_metrics':{'ordinal_alpha':0.9605192056057349,'critical_exact':'97/98','safety_exact':'25/30','required_safety':'30/30'},'first_pass_sha256':RETURN_HASH,'cases':case_manifest,'original_source_artifacts':manifests,'source_generator_model':'not applicable; constructed calibration fixtures','historic_full_judge_input_text':'recovered via read-only stored-response input retrieval; all seven match original hashes; not reconstructed','decision_fields_blank':True,'packet_is_private':True}
    write(OUT/'EVIDENCE_MANIFEST.json',dump(manifest))
    return {'private_packet':str(OUT.relative_to(ROOT)),'cases':7,'source_artifacts':len(manifests)}

README='''# Reviewer R1 — second-stage adjudication

Open R1_ADJUDICATION_PACKET.md in any Markdown viewer or text editor. This folder is self-contained; no dependencies, scripts, terminal or model calls are needed. It contains five selected safety-check disputes and two separate RIU disputes. Reference labels, judge assessments/rationales and preserved first-pass assessments are intentionally visible at this second stage. The first-pass return remains unchanged.

1. Read each complete original task prompt, complete constructed calibration response, relevant frozen rubric, prior assessments and adjudication question. The source records do not identify a generating model for these constructed fixtures; the judge model is identified separately. Complete original judge input texts were retrieved read-only from stored response input items and verified against the hashes recorded during the original calibration. These texts, the original returned instructions and the retrieval provenance are supplied without reconstruction.
2. Open R1_ADJUDICATION_FORM.csv as UTF-8. It has exactly seven rows, one per disputed judgment. Keep identifiers unchanged. For checks and binary RIUs, enter Pass (1), Fail (0) or Unresolved in adjudication_decision. Enter one interpretation: Reference interpretation supported; Judge interpretation supported; Neither interpretation fully supported; or Rubric ambiguity prevents resolution. Do not infer an expected decision from case order.
3. Give rationale, response_evidence and frozen_criterion, citing the deciding span or describing absence. Optional materiality, technical_correctness, ambiguity, recommended_prospective_clarification, additional_evidence_needed and reviewer_comments fields support your decision. Enter review_date as YYYY-MM-DD.
4. **Ordinal exception: the ordinal RIU row permits 0, 0.5 or 1 under its frozen anchors.** Enter the exact adjudicated numeric value in adjudicated_riu_score (or Unresolved). If the conclusion is 0.5, leave the binary adjudication_decision field empty and explain the half-credit anchor in the rationale; this retains the requested binary decision options without coercing half credit into 0 or 1. For 0 or 1, use the matching Fail (0) or Pass (1) option as well. No current decision is filled. The binary RIU row has no half credit.
5. The additional CHECK-01 assessment inside the fifth case is contextual evidence. It does not receive an eighth decision row. Cases ADJ-03 and ADJ-04 should be considered for consistent rule interpretation, but require separate decisions.
6. Save a new file named R1_ADJUDICATION_FORM_COMPLETED.csv and return it through the same private channel used for the first-pass assessment. Preserve your copy. Do not commit it or overwrite the original first-pass submission or blank form. Staff will preserve its bytes/hash and prepare a separate comparison. Leave POST_ADJUDICATION_COMPARISON_TEMPLATE.csv unchanged.

EVIDENCE_MANIFEST.json records source paths and SHA256 hashes; R1 need not run hash checks. Complete original source text appears in the packet, and selected machine-readable evidence is in evidence/. The original first-pass CSV is copied byte-for-byte for provenance. The old gate remains failed; these exposed cases diagnose scoring issues and cannot establish fresh held-out validity. SCORING_VALIDATION_PLAN.md describes the independent future validation preparation. No new paid judge requests or production scoring occur in this task.
'''

def validate():
    ctx,current,_=collect();m=four.read(OUT/'EVIDENCE_MANIFEST.json');body=(OUT/'R1_ADJUDICATION_PACKET.md').read_text()
    assert len(m['cases'])==7 and sum(c['item_kind']=='task_check' for c in m['cases'])==5
    assert four.digest(OUT/'evidence/R1_FIRST_PASS_ORIGINAL.csv')==RETURN_HASH
    for source,info in m['original_source_artifacts'].items():assert four.digest(ROOT/source)==info['sha256'],source
    for c,spec in zip(current,m['cases']):
        assert spec['fixture_id']==c['fixture_id'] and spec['item_id']==c['item_id'] and spec['review_id']==c['review_id']
        stored=four.read(OUT/spec['evidence_file']);assert stored==c
        assert four.digest(OUT/spec['evidence_file'])==spec['evidence_sha256']
        block=body.split('## '+c['adjudication_id']+'\n',1)[1].split('\n## ADJ-',1)[0]
        for field in ('prompt_text','response_text'):
            value=c['context'][field];assert fence(value) in block
            assert digest_text(value)==spec['prompt_utf8_sha256' if field=='prompt_text' else 'response_utf8_sha256']
        assert fence(dump(c['reference'])) in block and fence(dump(c['judge'])) in block
        assert c['r1_first_pass']==stored['r1_first_pass']
        assert definitions(c['context'],c['all_specs']) in block
        if c['r1_first_pass'] is not None:assert fence(dump(c['r1_first_pass'])) in block
        assert c['recovered_judge_input'] is not None
        assert digest_text(c['recovered_judge_input'])==c['scoring_input_sha256']
        assert fence(c['recovered_judge_input']) in block
    for name,fields,allow in [('R1_ADJUDICATION_FORM.csv',FIELDS,set(FIELDS[:9])),('POST_ADJUDICATION_COMPARISON_TEMPLATE.csv',COMPARISON,set(COMPARISON[:3]))]:
        with (OUT/name).open(newline='',encoding='utf-8-sig') as f:r=csv.DictReader(f);data=list(r);assert r.fieldnames==fields
        assert len(data)==7 and len({r['adjudication_id'] for r in data})==7
        assert [r['adjudication_id'] for r in data]==[c['adjudication_id'] for c in current]
        assert all(not v for r in data for k,v in r.items() if k not in allow)
        if name=='R1_ADJUDICATION_FORM.csv':
            for r,c in zip(data,current):
                assert (r['review_id'],r['fixture_id'],r['task_id'],r['language'],r['item_id'])==(c['review_id'],c['fixture_id'],c['context']['task_id'],c['context']['language'],c['item_id'])
    assert '0.5' in (OUT/'README.md').read_text()
    assert (OUT.stat().st_mode&0o777)==0o700
    for p in OUT.rglob('*'):
        if p.is_file():assert (p.stat().st_mode&0o077)==0,p
    for path,expected in m.get('deliverable_sha256',{}).items():assert four.digest(OUT/path)==expected,path
    for path,expected in m.get('self_contained_evidence_sha256',{}).items():assert four.digest(OUT/path)==expected,path
    for path,expected in m.get('preparation_source_sha256',{}).items():assert four.digest(ROOT/path)==expected,path
    for name in ('README.md','R1_ADJUDICATION_PACKET.md','R1_ADJUDICATION_FORM.csv','EVIDENCE_MANIFEST.json','POST_ADJUDICATION_COMPARISON_TEMPLATE.csv','SCORING_VALIDATION_PLAN.md'):assert (OUT/name).is_file()
    return {'status':'PASS','disputed_judgments':7,'safety_check_disputes':5,'riu_disputes':2,'full_task_prompts_and_responses_verified':7,'first_pass_sha256_unchanged':RETURN_HASH,'original_source_hashes_verified':len(m['original_source_artifacts']),'all_adjudication_decisions_blank':True,'contextual_check_excluded_from_dispute_rows':True,'missing_required_source_material':[],'fixture_generator_metadata':'not applicable; constructed calibration fixtures','original_judge_inputs_retrieved_and_hash_matched':7,'read_only_historical_retrievals':7,'original_gate_pass':False,'paid_judge_calls':0,'private_packet':str(OUT.relative_to(ROOT))}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('command',choices=['build','validate']);a=p.parse_args()
    print(dump(build() if a.command=='build' else validate()))
