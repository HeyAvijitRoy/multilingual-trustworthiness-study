#!/usr/bin/env python3
"""Compare independent first-pass human QA to AI scores, before adjudication.

Structural checks do not authenticate a human or certify independent review.
Selected/mandatory strata must not be presented as an unbiased population sample.
"""
import argparse
import json
from pathlib import Path

import prelim_eval_157 as records
import prelim_four as four
import prelim_judge_157 as judge
from prelim_four_judge import ScoringContext


def audit(ctx,packet_dir,human_file):
    manifest=four.read(packet_dir/'qa_manifest_private.json')
    packet=packet_dir/'qa_packet.jsonl';packet_hash=four.digest(packet)
    if manifest['packet_sha256']!=packet_hash or any(manifest.get(k)!=v for k,v in ctx.pins.items()):
        raise RuntimeError('stale/changed QA packet provenance')
    cells={r['qa_id']:r for r in manifest['cells']}
    automated={r['qa_id']:r['ratings'] for r in records.read_jsonl_records(packet_dir/'qa_automated_ratings_private.jsonl')}
    if manifest.get('private_automated_ratings_sha256')!=four.digest(packet_dir/'qa_automated_ratings_private.jsonl'):
        raise RuntimeError('private automated QA labels changed')
    reviewed=set();groups={};escalations=[];source_scores={}
    def group(name):return groups.setdefault(name,{'riu_pairs':[],'critical_exact':[],'safety_check_exact':[],'response_cells':0})
    for row in records.read_jsonl_records(human_file):
        qa_id=row['qa_id'];cell=cells.get(qa_id)
        if cell is None or qa_id in reviewed:raise RuntimeError('unknown/duplicate human QA cell')
        if (not row.get('reviewer_id') or not row.get('reviewed_at') or row.get('independent_before_unblinding') is not True
                or row.get('packet_sha256')!=packet_hash or row.get('response_sha256')!=cell['response_sha256']):
            raise RuntimeError('independent first-pass human evidence/provenance missing')
        reviewed.add(qa_id);rec=ctx.annotations[cell['task_id']]
        partition=cell['provider']
        if partition not in source_scores:source_scores[partition]=ctx.scores(partition)
        source=source_scores[partition].get((cell['task_id'],cell['language']))
        if (source is None or judge.canonical_record_sha256(source)!=cell['score_record_sha256']
                or source['ratings']!=automated[qa_id]):
            raise RuntimeError('QA automated labels differ from validated source score')
        judge.validate_ratings(rec,row['ratings']);judge.validate_ratings(rec,automated[qa_id])
        human={r['item_id']:r for r in row['ratings']};auto={r['item_id']:r for r in automated[qa_id]}
        keys=['overall',cell['requested_model']+':'+cell['language']]
        keys+=['selection:'+reason for reason in cell['selection_reasons']]
        for name in keys:group(name)['response_cells']+=1
        for spec in judge.item_specs(rec):
            item=spec['item_id'];h,a=human[item],auto[item];pair=(float(h['score']),float(a['score']))
            critical=spec['kind']=='riu' and spec['criticality']=='critical'
            safety=spec['kind']=='check' and rec.get('safety_relevance','none')!='none'
            for name in keys:
                out=group(name)
                if spec['kind']=='riu':out['riu_pairs'].append(pair)
                if critical:out['critical_exact'].append(pair[0]==pair[1])
                if safety:out['safety_check_exact'].append(pair[0]==pair[1])
            if (critical or safety) and (pair[0]!=pair[1] or h['reason']!=a['reason']):
                escalations.append({'qa_id':qa_id,'item_id':item,'critical_riu':critical,'safety_check':safety,
                                    'human_rating':h,'automated_rating':a,'status':'requires_independent_adjudication'})
    summary={}
    for name,values in groups.items():
        summary[name]={'response_cells':values['response_cells'],'riu_items':len(values['riu_pairs']),
            'krippendorff_alpha_ordinal':judge.cal.krippendorff_alpha(values['riu_pairs'],'ordinal'),
            **{metric:{'item_count':len(values[metric]),'agreement':sum(values[metric])/len(values[metric]) if values[metric] else None}
               for metric in ('critical_exact','safety_check_exact')}}
    return {**ctx.pins,'packet_sha256':packet_hash,'human_first_pass_file_sha256':four.digest(human_file),
            'reviewed_cells':len(reviewed),'selected_qa_cells':len(cells),'pending_cells':len(cells)-len(reviewed),
            'agreement_by_review_stratum':summary,'critical_safety_disagreements':escalations,
            'status':'provisional_QA_audit_not_human_acceptance','independent_human_authenticity_certified':False,
            'limitations':['Agreement reflects selected review strata, not an unbiased study-wide estimate.',
                           'First-pass agreement is separate from resolved adjudications; thresholds are unchanged.',
                           'Systematic disagreement requires review of the affected class under the scoring plan.']}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config',type=Path,default=four.CONFIG);p.add_argument('--manifest',type=Path,default=four.MANIFEST)
    p.add_argument('--packet-dir',type=Path,required=True);p.add_argument('--human-first-pass',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args();ctx=ScoringContext(args.config,args.manifest)
    if not args.out.resolve().is_relative_to(ctx.root/'qa'):p.error('QA audit belongs in the ignored amended qa directory')
    report=audit(ctx,args.packet_dir,args.human_first_pass)
    with args.out.open('x',encoding='utf-8') as handle:json.dump(report,handle,indent=2,allow_nan=False);handle.write('\n')
