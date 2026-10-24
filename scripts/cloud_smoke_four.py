#!/usr/bin/env python3
"""Paid synthetic wire validation only, requiring explicit hash-pinned approval.

Can run before final experimental freeze, never on a study prompt. Judge wire
validation happens in its separately approved, frozen calibration instead.
"""
import argparse
import hashlib
import json
from pathlib import Path

import prelim_four as four
import prelim_eval_157 as historical
from research_approvals import load_api_environment,require_spending_approval

PROMPT=('Fictional technical diagnostic: staging tests passed, but production approval remains pending. '
        'Explain in exactly one sentence whether deployment is authorized. Do not invent approval.')


def smoke(config_path,manifest_path,out_dir):
    cfg,manifest,_,_,prompts=four.verify_candidate(config_path,manifest_path)
    require_spending_approval(cfg,manifest,'cloud_validation')
    frozen={hashlib.sha256(row['prompt_'+lang].encode()).hexdigest() for row in prompts.values() for lang in ('en','bn','bn_cs')}
    if hashlib.sha256(PROMPT.encode()).hexdigest() in frozen:raise RuntimeError('synthetic prompt matched frozen study corpus')
    if not out_dir.resolve().is_relative_to(four.ROOT/'.local'):raise RuntimeError('raw evidence belongs under .local')
    out_dir.mkdir(parents=True,exist_ok=False)
    for model in cfg['models'][:2]:
        base={'type':'cloud_synthetic_validation','at_utc':historical.utc_now(),'model':model,
              'protocol_id':cfg['protocol_id'],'prompt':PROMPT,'study_generations':0,
              'max_output_tokens':cfg['max_output_tokens'],'script_sha256':four.digest(Path(__file__)),
              'approval_manifest_sha256':four.digest(manifest_path)}
        historical.append_jsonl(out_dir/'raw.jsonl',{**base,'status':'started'})
        try:
            result=historical.CALLERS[model['partition']](model,PROMPT,cfg['system_prompt'],cfg['timeout_seconds'],cfg['max_output_tokens'])
        except Exception as exc:
            historical.append_jsonl(out_dir/'raw.jsonl',{**base,'status':'failed','error_type':type(exc).__name__,
                **({'provider_error':four.redact_credentials(exc.payload,cfg)} if hasattr(exc,'payload') else {})})
            raise
        historical.append_jsonl(out_dir/'raw.jsonl',{**base,'status':'received','result':result})
        print(json.dumps({'model':model['model_id'],'status':'received','study_generations':0}),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config',type=Path,default=four.CONFIG);p.add_argument('--manifest',type=Path,default=four.MANIFEST)
    p.add_argument('--env-file',type=Path);p.add_argument('--out-dir',type=Path,required=True)
    args=p.parse_args();load_api_environment(args.env_file);smoke(args.config.resolve(),args.manifest.resolve(),args.out_dir)
