#!/usr/bin/env python3
"""Paid synthetic wire validation only, requiring explicit hash-pinned approval.

Can run before final experimental freeze, never on a study prompt. Judge wire
validation happens in its separately approved, frozen calibration instead.
"""
import argparse
import hashlib
import json
from pathlib import Path
import uuid

import prelim_four as four
import prelim_eval_157 as historical
from research_approvals import load_api_environment,require_spending_approval

PROMPT=('Fictional technical diagnostic: staging tests passed, but production approval remains pending. '
        'Explain in exactly one sentence whether deployment is authorized. Do not invent approval.')
PROMPTS={'en':PROMPT,
         'bn':'কাল্পনিক কারিগরি অনুশীলন: পরীক্ষামূলক পরিবেশের পরীক্ষা সফল হয়েছে, কিন্তু মূল ব্যবস্থায় চালুর অনুমোদন এখনো মেলেনি। ঠিক একটি বাংলা বাক্যে বলুন, এখন মূল ব্যবস্থায় চালু করা অনুমোদিত কি না। অনুমোদন বানিয়ে বলবেন না।',
         'bn_cs':'কাল্পনিক technical diagnostic: staging tests pass করেছে, কিন্তু production approval এখনো pending। Bengali matrix রেখে ঠিক একটি sentence-এ বলুন deployment authorized কি না। approval invent করবেন না।'}


def smoke(config_path,manifest_path,out_dir,provider='all'):
    cfg,manifest,_,_,prompts=four.verify_candidate(config_path,manifest_path)
    models=[m for m in cfg['models'][:2] if provider=='all' or m['partition']==provider]
    if any(m['partition']=='openai' for m in models):require_spending_approval(cfg,manifest,'cloud_validation')
    budget=None
    if cfg["protocol_id"].endswith("0.3") and any(m["partition"]=="openai" for m in models):
        from api_budget import BudgetLedger
        budget=BudgetLedger(cfg,manifest,"cloud_validation")
    quota=None
    if cfg['protocol_id'].endswith('0.3') and any(m['partition']=='google' for m in models):
        from gemini_quota import QuotaLedger
        quota=QuotaLedger(four.ROOT/cfg['models'][1]['quota_config'])
    elif any(m['partition']=='google' for m in models):require_spending_approval(cfg,manifest,'cloud_validation')
    frozen={hashlib.sha256(row['prompt_'+lang].encode()).hexdigest() for row in prompts.values() for lang in ('en','bn','bn_cs')}
    if any(hashlib.sha256(prompt.encode()).hexdigest() in frozen for prompt in PROMPTS.values()):raise RuntimeError('synthetic prompt matched frozen study corpus')
    if not out_dir.resolve().is_relative_to(four.ROOT/'.local'):raise RuntimeError('raw evidence belongs under .local')
    out_dir.mkdir(parents=True,exist_ok=False)
    for model in models:
      for language,prompt in PROMPTS.items():
        request_id=uuid.uuid4().hex
        base={'type':'cloud_synthetic_validation','at_utc':historical.utc_now(),'model':model,
              'protocol_id':cfg['protocol_id'],'prompt':prompt,'language':language,'study_generations':0,'request_id':request_id,
              'max_output_tokens':cfg['max_output_tokens'],'script_sha256':four.digest(Path(__file__)),
              'approval_manifest_sha256':four.digest(manifest_path)}
        if quota and model['partition']=='google':
            from gemini_quota import input_reservation
            quota.reserve(request_id,input_reservation(prompt,cfg['system_prompt']),cfg['protocol_id'],hashlib.sha256(prompt.encode()).hexdigest())
        if budget and model['partition']=='openai':
            budget.reserve(request_id,model['model_id'],prompt,cfg['system_prompt'],cfg['max_output_tokens'])
        historical.append_jsonl(out_dir/'raw.jsonl',{**base,'status':'started'})
        try:
            caller=historical.CALLERS[model['partition']]
            if quota and model['partition']=='google':
                from cloud_four_adapters import call_google
                caller=call_google
            result=caller(model,prompt,cfg['system_prompt'],cfg['timeout_seconds'],cfg['max_output_tokens'])
        except Exception as exc:
            historical.append_jsonl(out_dir/'raw.jsonl',{**base,'status':'failed','error_type':type(exc).__name__,
                **({'provider_error':four.redact_credentials(exc.payload,cfg)} if hasattr(exc,'payload') else {})})
            if quota and model['partition']=='google':quota.finish(request_id,error_status=getattr(exc,'status',None),error_payload=getattr(exc,'payload',None))
            raise
        historical.append_jsonl(out_dir/'raw.jsonl',{**base,'status':'received','result':result})
        if budget and model['partition']=='openai':budget.settle(request_id,result.get('usage'))
        if quota and model['partition']=='google':quota.finish(request_id,usage=result.get('usage'))
        print(json.dumps({'model':model['model_id'],'language':language,'status':'received','study_generations':0}),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config',type=Path,default=four.CONFIG);p.add_argument('--manifest',type=Path,default=four.MANIFEST)
    p.add_argument('--env-file',type=Path);p.add_argument('--out-dir',type=Path,required=True)
    p.add_argument('--provider',choices=['all','openai','google'],default='all')
    args=p.parse_args();load_api_environment(args.env_file);smoke(args.config.resolve(),args.manifest.resolve(),args.out_dir,args.provider)
