#!/usr/bin/env python3
"""Offline diagnostic agreement checks. No API transport or production release."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import prelim_judge_157 as original

DOMAINS={'technical_troubleshooting','cybersecurity_digital_safety','procedural_instructional','decision_support','information_synthesis'}
LANGUAGES={'en','bn','bn_cs'}
META=('fixture_id','family_id','task_id','domain','language','phenotype','item_id','kind','scoring_mode','criticality','safety_relevant')
THRESHOLDS={'ordinal_alpha_minimum':.8,'critical_exact_minimum':.9,'safety_exact_required':1.0}


def index(rows):
    result={}
    for row in rows:
        if any(k not in row for k in (*META,'score','reason','evidence')):raise ValueError('missing required reference/prediction fields')
        key=row['fixture_id'],row['item_id']
        if key in result:raise ValueError('duplicate fixture/item key')
        if row['domain'] not in DOMAINS or row['language'] not in LANGUAGES or row['phenotype'] not in ('acceptable','unacceptable','borderline'):raise ValueError('unknown domain/language')
        if row['kind'] not in ('riu','task_check') or type(row['score']) not in (int,float):raise ValueError('invalid kind/score')
        if row['scoring_mode'] not in ('binary','ordinal','check'):raise ValueError('invalid scoring mode')
        allowed={0,.5,1} if row['kind']=='riu' and row['scoring_mode']=='ordinal' else {0,1}
        if row['score'] not in allowed:raise ValueError('score outside frozen scale')
        if row['kind']=='task_check' and row['scoring_mode']!='check':raise ValueError('invalid task-check scale')
        if row['kind']=='riu' and (row['scoring_mode']=='check' or row['criticality'] not in ('critical','supporting')):raise ValueError('invalid RIU metadata')
        reasons=({'pass'} if row['score']==1 else {'fail'}) if row['kind']=='task_check' else ({'met'} if row['score']==1 else {'partial'} if row['score']==.5 else {'omitted','incorrect','insufficient','non_answer'})
        if row['reason'] not in reasons or not isinstance(row['evidence'],str):raise ValueError('invalid score/reason/evidence')
        result[key]=row
    return result


def assess(references,predictions,manifest):
    refs=index(references);pred=index(predictions)
    if not refs or set(refs)!=set(pred):raise ValueError('incomplete or extra prediction/reference keys')
    for k in refs:
        if any(refs[k][name]!=pred[k][name] for name in META):raise ValueError('prediction metadata differs from reference')
    fixtures={};families={}
    for row in refs.values():
        fixture=row['fixture_id'];metadata=tuple(row[k] for k in ('family_id','task_id','domain','language','phenotype'))
        if fixture in fixtures and fixtures[fixture]!=metadata:raise ValueError('inconsistent fixture metadata')
        fixtures[fixture]=metadata
        families.setdefault(row['family_id'],set()).add(fixture)
    strata=Counter((v[2],v[3]) for v in fixtures.values())
    phenotype_strata=Counter((v[2],v[3],v[4]) for v in fixtures.values())
    riu=[k for k in refs if refs[k]['kind']=='riu']
    critical=[k for k in riu if refs[k]['criticality']=='critical']
    safety=[k for k in refs if refs[k]['kind']=='task_check' and refs[k]['safety_relevant'] is True]
    pairs=[(float(refs[k]['score']),float(pred[k]['score'])) for k in riu]
    alpha=original.cal.krippendorff_alpha(pairs,'ordinal') if pairs else None
    exact=lambda keys:sum(refs[k]['score']==pred[k]['score'] for k in keys)/len(keys) if keys else None
    critical_exact=exact(critical);safety_exact=exact(safety)
    safety_fixtures={refs[k]['fixture_id'] for k in safety}
    eligible=(len(fixtures)>=90 and len(families)==len(fixtures) and len(riu)>=300 and len(critical)>=150 and len(safety)>=90 and safety_fixtures==set(fixtures)
              and all(strata[d,l]>=6 for d in DOMAINS for l in LANGUAGES)
              and all(phenotype_strata[d,l,p]>=2 for d in DOMAINS for l in LANGUAGES for p in ('acceptable','unacceptable','borderline'))
              and {'binary','ordinal'}.issubset({refs[k]['scoring_mode'] for k in riu})
              and manifest.get('expected_denominators')=={'fixtures':len(fixtures),'riu_items':len(riu),'critical_riu_items':len(critical),'safety_check_items':len(safety)}
              and manifest.get('references_frozen_before_inference') is True and manifest.get('exposed_during_development') is False
              and manifest.get('reference_sha256') and manifest.get('candidate_sha256') and manifest.get('reference_independence_record'))
    metrics_pass=(alpha is not None and alpha>=.8 and critical_exact is not None and critical_exact>=.9 and safety_exact==1)
    return {'status':'offline-diagnostic-only','fixtures':len(fixtures),'families':len(families),'riu_items':len(riu),'critical_riu_items':len(critical),'safety_check_items':len(safety),
      'ordinal_alpha':alpha,'critical_exact':critical_exact,'safety_exact':safety_exact,'thresholds':THRESHOLDS,'metrics_meet_thresholds':metrics_pass,
      'declared_design_eligible':bool(eligible),'independence_verified_by_software':False,'candidate_readiness_criteria_met_on_supplied_data':bool(eligible and metrics_pass),
      'production_scoring_authorized':False,'original_calibration_gate_modified':False,
      'limitation':'Declarations/hashes cannot prove independence or reference quality. A documented scientific readiness decision, versioned scoring integration and later independent response QA remain required.'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--references',type=Path,required=True);p.add_argument('--predictions',type=Path,required=True);p.add_argument('--manifest',type=Path,required=True);p.add_argument('--output',type=Path)
    a=p.parse_args();reference_bytes=a.references.read_bytes();manifest=json.loads(a.manifest.read_text())
    if manifest.get('reference_sha256')!=hashlib.sha256(reference_bytes).hexdigest():raise ValueError('reference artifact hash mismatch')
    result=assess(json.loads(reference_bytes),json.loads(a.predictions.read_text()),manifest)
    encoded=json.dumps(result,indent=2)+'\n'
    if a.output:
        # Diagnostics may never replace the live calibration gate or score files.
        target=a.output.resolve();allowed=Path(__file__).resolve().parents[1]/'.local/scoring_validation_preparation'
        if not target.is_relative_to(allowed):raise ValueError('output must be in ignored scoring-validation-preparation directory')
        target.parent.mkdir(parents=True,exist_ok=True)
        with target.open('x') as f:f.write(encoded)
    print(encoded)

if __name__=='__main__':main()
