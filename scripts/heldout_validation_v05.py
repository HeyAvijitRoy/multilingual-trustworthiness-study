#!/usr/bin/env python3
"""Construction checks, public manifest and blind reviewer packet for the
scoring-candidate-0.5 held-out validation set.

Offline only: no transport, no scoring, no reference labels. Fixture content and
the sealed construction intent stay in ignored `.local/heldout_validation_v05/`;
only hashes and aggregate counts are written to the repository.
"""
import argparse
from collections import Counter
import csv
import glob
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PRIVATE=ROOT/'.local/heldout_validation_v05'
FIXTURES=PRIVATE/'fixtures'
INTENT=PRIVATE/'sealed/construction_intent.jsonl'
PUBLIC=ROOT/'data/evaluation/amendments/scoring-candidate-0.5/HELDOUT_MANIFEST.json'
DOMAINS=('technical_troubleshooting','cybersecurity_digital_safety','procedural_instructional','decision_support','information_synthesis')
LANGUAGES=('en','bn','bn_cs')
PHENOTYPES=('acceptable','unacceptable','borderline')
TAGS={'negative_constraint_silent_compliance','negative_constraint_violation','conditional_safeguard_protected_path',
      'omitted_required_safeguard','nonmaterial_secondary_inaccuracy','material_primary_error','false_safety_property',
      'inherently_unsafe_instruction','policy_choice_defeats_riu','multi_conjunct_format_partial','multi_conjunct_format_met',
      'distributed_vs_integrated_rule','ordinal_half_credit','contradiction','nonanswer_refusal','partial_fulfillment','complete_fulfillment'}
RIU_TYPES={'fact','action','evidence','constraint','warning','qualification','comparison','uncertainty'}
OVERLAP_LIMIT=0.30


def read_jsonl(path):
    return [json.loads(line) for line in Path(path).read_text(encoding='utf-8').split('\n') if line.strip()]


def fixtures():
    return [r for f in sorted(glob.glob(str(FIXTURES/'*.jsonl'))) for r in read_jsonl(f)]


def bengali_share(text):
    letters=[ch for ch in text if ch.isalpha()]
    return sum('ঀ'<=ch<='৿' for ch in letters)/len(letters) if letters else 0.0


def grams(text,n=5):
    text=' '.join(text.lower().split());return {text[i:i+n] for i in range(max(0,len(text)-n+1))}


def corpus_prompts():
    field={'en':'prompt_en','bn':'prompt_bn','bn_cs':'prompt_bn_cs'};out={l:[] for l in LANGUAGES}
    for path in sorted(glob.glob(str(ROOT/'data/prompts/*_0*.csv'))):
        with open(path,encoding='utf-8') as handle:
            for row in csv.DictReader(handle):
                for l,f in field.items():out[l].append((row['task_id'],grams(row[f])))
    return out


def check_riu(fid,i,riu):
    errors=[]
    if riu.get('id')!=f'RIU-{i:02d}':errors.append(f'{fid}: RIU ids must be sequential')
    if riu.get('riu_type') not in RIU_TYPES or riu.get('criticality') not in ('critical','supporting'):errors.append(f'{fid}/{riu.get("id")}: type/criticality')
    rule=riu.get('scoring_rule',{})
    if set(rule)!={'0','0.5','1'} or rule.get('1')!=riu.get('description'):errors.append(f'{fid}/{riu.get("id")}: scoring_rule keys or full anchor')
    if riu.get('scoring_mode')=='binary' and rule.get('0.5') is not None:errors.append(f'{fid}/{riu.get("id")}: binary half anchor must be null')
    if riu.get('scoring_mode')=='ordinal' and not rule.get('0.5'):errors.append(f'{fid}/{riu.get("id")}: ordinal needs a written half anchor')
    if riu.get('scoring_mode') not in ('binary','ordinal') or not riu.get('rationale'):errors.append(f'{fid}/{riu.get("id")}: mode/rationale')
    return errors


def check(records=None,intent=None,corpus=None):
    records=fixtures() if records is None else records
    intent={r['fixture_id']:r for r in (read_jsonl(INTENT) if intent is None else intent)}
    corpus=corpus_prompts() if corpus is None else corpus
    errors=[];ids=Counter(r.get('fixture_id') for r in records);fams=Counter(r.get('family_id') for r in records)
    errors+=[f'duplicate fixture {k}' for k,v in ids.items() if v>1]+[f'duplicate family {k}' for k,v in fams.items() if v>1]
    strata=Counter();phen=Counter();tags=Counter();riu_n=crit=safety=ordinal=0;max_overlap=(0,None,None)
    for r in records:
        fid=r.get('fixture_id')
        if r.get('domain') not in DOMAINS or r.get('language') not in LANGUAGES:errors.append(f'{fid}: domain/language');continue
        strata[r['domain'],r['language']]+=1
        if r.get('safety_relevance') not in ('low','moderate','high'):errors.append(f'{fid}: safety_relevance must be low/moderate/high')
        for field in ('task_objective','prompt_text','response_text'):
            if not isinstance(r.get(field),str) or not r[field].strip():errors.append(f'{fid}: {field}')
        rius=r.get('rius',[])
        if len(rius)!=4:errors.append(f'{fid}: exactly four RIUs required')
        for i,riu in enumerate(rius,1):errors+=check_riu(fid,i,riu)
        riu_n+=len(rius);c=sum(u.get('criticality')=='critical' for u in rius);crit+=c;ordinal+=sum(u.get('scoring_mode')=='ordinal' for u in rius)
        if c<2:errors.append(f'{fid}: at least two critical RIUs')
        if r.get('constraints')!=[u['description'] for u in rius if u.get('riu_type')=='constraint']:errors.append(f'{fid}: constraints index must list constraint RIUs in order')
        checks=r.get('task_checks',[])
        if not checks or checks[0].get('id')!='CHECK-01' or checks[0].get('kind')!='unsupported_content':errors.append(f'{fid}: CHECK-01 unsupported_content required first')
        if [k.get('id') for k in checks]!=[f'CHECK-{i:02d}' for i in range(1,len(checks)+1)] or any(k.get('kind') not in ('unsupported_content','format') or not k.get('rule') for k in checks):errors.append(f'{fid}: task check ids/kinds')
        safety+=len(checks)
        bad=set(r.get('coverage_tags',[]))-TAGS
        if bad or not r.get('coverage_tags'):errors.append(f'{fid}: coverage tags {sorted(bad)}')
        tags.update(r.get('coverage_tags',[]))
        text=r.get('prompt_text','')+' '+r.get('response_text','');share=bengali_share(text)
        if r['language']=='en' and share>0.02:errors.append(f'{fid}: EN contains Bengali script')
        if r['language']=='bn' and share<0.55:errors.append(f'{fid}: BN Bengali share {share:.2f}<0.55')
        if r['language']=='bn_cs' and not 0.25<=share<=0.985:errors.append(f'{fid}: BN-CS Bengali share {share:.2f}')
        g=grams(r.get('prompt_text',''))
        for task,cg in corpus.get(r['language'],[]):
            j=len(g&cg)/len(g|cg) if g|cg else 0
            if j>max_overlap[0]:max_overlap=(j,fid,task)
            if j>OVERLAP_LIMIT:errors.append(f'{fid}: prompt overlaps study task {task} (Jaccard {j:.2f})')
        it=intent.get(fid)
        if not it:errors.append(f'{fid}: missing sealed construction intent');continue
        if it.get('phenotype') not in PHENOTYPES:errors.append(f'{fid}: phenotype');continue
        phen[r['domain'],r['language'],it['phenotype']]+=1
        items={u['id']:u for u in rius}|{k['id']:k for k in checks}
        scores=it.get('intended_scores',{})
        if set(scores)!=set(items):errors.append(f'{fid}: intended scores must cover every item')
        for k,v in scores.items():
            u=items.get(k,{})
            allowed={0,0.5,1} if u.get('scoring_mode')=='ordinal' else {0,1}
            if isinstance(v,bool) or v not in allowed:errors.append(f'{fid}/{k}: intended score outside scale')
    errors+=[f'extra sealed intent {k}' for k in set(intent)-set(ids)]
    complete=len(records)==90
    if complete:
        errors+=[f'stratum {d}/{l} has {strata[d,l]} fixtures' for d in DOMAINS for l in LANGUAGES if strata[d,l]!=6]
        errors+=[f'stratum {d}/{l} has {phen[d,l,p]} {p}' for d in DOMAINS for l in LANGUAGES for p in PHENOTYPES if phen[d,l,p]!=2]
        errors+=[] if riu_n>=300 and crit>=150 and safety>=90 and ordinal>0 else ['denominator floors not met']
    return {'fixtures':len(records),'complete_design':complete,'riu_items':riu_n,'critical_riu_items':crit,'ordinal_riu_items':ordinal,
            'safety_check_items':safety,'strata':{f'{d}/{l}':strata[d,l] for d in DOMAINS for l in LANGUAGES},
            'coverage_tags':dict(sorted(tags.items())),'max_prompt_overlap':{'jaccard':round(max_overlap[0],3),'fixture':max_overlap[1],'study_task':max_overlap[2]},
            'errors':errors}


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def manifest():
    result=check()
    if result['errors']:raise SystemExit('construction check failed; manifest not written')
    files=sorted(glob.glob(str(FIXTURES/'*.jsonl')))
    out={'set_id':'heldout-v05-construction-1','status':'construction-draft-no-references','candidate_pin_sha256':digest(PUBLIC.parent/'CANDIDATE_PIN.json'),
         'fixture_files_sha256':{Path(f).name:digest(f) for f in files},'sealed_intent_sha256':digest(INTENT),
         **{k:result[k] for k in ('fixtures','riu_items','critical_riu_items','ordinal_riu_items','safety_check_items','strata','coverage_tags','max_prompt_overlap')},
         'references_established':False,'reference_independence_record':None,'exposed_during_development':False,
         'exposure_log':[{'event':'constructed','by':'AI constructor (Claude) under study-lead direction','candidate_known_to_constructor':True,
                          'intent_visible_to':['constructor'],'fixtures_visible_to':['constructor'],'candidate_or_judge_inference':0}],
         'production_scoring_authorized':False}
    PUBLIC.write_text(json.dumps(out,indent=2)+'\n');return out


def packet():
    """Blind Stage-B reviewer packet: fixtures and rubric only, presentation order by hash, no intent."""
    records=sorted(fixtures(),key=lambda r:hashlib.sha256(('heldout-v05|'+r['fixture_id']).encode()).hexdigest())
    target=PRIVATE/'reference_packet';target.mkdir(parents=True,exist_ok=True)
    rows=[]
    for n,r in enumerate(records,1):
        for item in [*r['rius'],*r['task_checks']]:
            rows.append({'packet_order':n,'fixture_id':r['fixture_id'],'language':r['language'],'item_id':item['id'],
                         'scale':item.get('scoring_mode','check'),'reference_score':'','evidence':'','rationale':'','ambiguity':'','reviewer':'','review_date':''})
    form=target/'REFERENCE_FORM_BLANK.csv'
    with form.open('x' if not form.exists() else 'w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    blind=[{k:v for k,v in r.items() if k not in ('coverage_tags','construction')} for r in records]
    (target/'FIXTURES_BLIND.json').write_text(json.dumps(blind,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
    return {'fixtures':len(records),'items':len(rows),'packet_dir':str(target.relative_to(ROOT))}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('command',choices=('check','manifest','packet'))
    a=p.parse_args()
    result={'check':check,'manifest':manifest,'packet':packet}[a.command]()
    print(json.dumps(result,indent=2,ensure_ascii=False))
    return 1 if a.command=='check' and result['errors'] else 0


if __name__=='__main__':raise SystemExit(main())
