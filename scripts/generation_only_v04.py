#!/usr/bin/env python3
"""Authorized v0.4 raw generation only, delegating to unchanged v0.3 clients.

Process-local policy hooks replace only execution authorization, scope and
provenance. Frozen source/configuration files are never edited. No judge API.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
from collections import Counter

import prelim_four as four
import api_budget
from research_approvals import load_api_environment

ROOT=four.ROOT
BASE_CONFIG=four.CONFIG
BASE_MANIFEST=four.AMENDMENT/'FREEZE.json'
DIR=ROOT/'data/evaluation/amendments/prelim-generation-0.4'
MANIFEST=DIR/'FREEZE.json'
SCOPE=DIR/'SCOPE.json'
AMENDMENT_ID='prelim-generation-0.4-20261024'
PROTECTED_USD=80
_ORIGINAL_VERIFY=four.verify_candidate
_ORIGINAL_CELLS=four.cells_for
_ORIGINAL_PROVENANCE=four.provenance
_ORIGINAL_FROZEN=four.require_frozen
_OriginalBudget=api_budget.BudgetLedger


class GenerationBudget(_OriginalBudget):
    def reserve(self,rid,model,prompt,system,max_output_tokens,extra_input=''):
        if self.purpose!='generation' or model!='gpt-6.1-sol' or max_output_tokens!=32768:
            raise RuntimeError('generation-only budget cannot authorize judge/changed model/settings')
        rates=api_budget.RATES[model]
        bound=len((prompt+system+extra_input).encode())+4096
        amount=bound*int(rates[2]*1000)+max_output_tokens*int(rates[3]*1000)
        with self.locked():
            holds,settled=self.state(self.events())
            if rid in holds or rid in settled:raise RuntimeError('request already budgeted')
            committed=sum(r['reserved_nano_usd'] for r in holds.values())+sum(r['charged_nano_usd'] for r in settled.values())
            ceiling=self.cap-PROTECTED_USD*api_budget.NANO
            if committed+amount>ceiling:
                raise api_budget.BudgetExceeded(f'paid generation paused: ${committed/api_budget.NANO:.9f} committed; next maximum ${amount/api_budget.NANO:.9f}; ${PROTECTED_USD} protected for later evaluation; generation-phase ceiling ${ceiling/api_budget.NANO:.2f}')
            self.append({'event':'reserved','request_id':rid,'model':model,'purpose':'generation',
                'input_token_bound':bound,'max_output_tokens':max_output_tokens,'reserved_nano_usd':amount,
                'execution_amendment_id':AMENDMENT_ID,'protected_evaluation_usd':PROTECTED_USD})


def verify(config_path=BASE_CONFIG,manifest_path=MANIFEST):
    if Path(config_path).resolve()!=BASE_CONFIG or Path(manifest_path).resolve()!=MANIFEST:
        raise RuntimeError('only exact v0.4 execution manifest and unchanged base config allowed')
    config,base,freeze,annotations,prompts=_ORIGINAL_VERIFY(BASE_CONFIG,BASE_MANIFEST)
    manifest=four.read(MANIFEST)
    if (manifest.get('execution_amendment_id')!=AMENDMENT_ID or
        manifest.get('parent_freeze_sha256')!=four.digest(BASE_MANIFEST) or
        manifest.get('base_config_sha256')!=four.digest(BASE_CONFIG) or
        manifest.get('execution_mode')!='raw-generation-only' or
        manifest.get('scoring_authorized') is not False or
        manifest.get('protected_evaluation_usd')!=PROTECTED_USD):
        raise RuntimeError('generation-only amendment identity/authorization mismatch')
    scope=four.read(SCOPE)
    if scope['primary_partitions']!=['openai','local_a','local_b'] or scope['primary_responses']!=1413 or scope['exploratory_responses']!=60:
        raise RuntimeError('prospective panel/scope changed')
    selected=scope['gemini_task_ids']
    if len(selected)!=20 or len(set(selected))!=20 or not set(selected).issubset(annotations):raise RuntimeError('invalid matched Gemini sample')
    if any(scope['at_scope_change']['successful_responses'][p]!=0 for p in four.PARTITIONS):raise RuntimeError('unexpected scope change baseline')
    return config,manifest,freeze,annotations,prompts


def authorize(config,manifest,config_path=BASE_CONFIG,manifest_path=MANIFEST):
    verified,actual,*_=verify(config_path,manifest_path)
    if config!=verified or manifest!=actual:raise RuntimeError('configuration differs from approved execution record')
    _ORIGINAL_FROZEN(config,manifest,BASE_CONFIG,MANIFEST)
    _ORIGINAL_FROZEN(config,four.read(BASE_MANIFEST),BASE_CONFIG,BASE_MANIFEST)
    required={'scripts/generation_only_v04.py','scripts/generation_controller_v04.py',
              str(SCOPE.relative_to(ROOT)),str((DIR/'AUTHORIZATION.json').relative_to(ROOT)),str((DIR/'AMENDMENT.md').relative_to(ROOT))}
    if not required.issubset(manifest['artifact_sha256']):raise RuntimeError('generation amendment sources not frozen')
    auth=four.read(DIR/'AUTHORIZATION.json')
    if auth['status']!='approved-by-user' or auth['generation_authorized'] is not True or auth['scoring_authorized'] is not False:
        raise RuntimeError('raw generation authorization absent')
    # The original spending approval is deliberately reused byte-identically:
    # this retains all prior costs and in-flight commitments in the shared ledger.
    api_budget.require_spending_approval(config,manifest,'generation')


def cells(config,freeze,annotations,prompts,partition,language=None):
    result=_ORIGINAL_CELLS(config,freeze,annotations,prompts,partition,language)
    if partition=='google':
        ids=set(four.read(SCOPE)['gemini_task_ids']);result=[c for c in result if c['task_id'] in ids]
    return result


def provenance(config_path=BASE_CONFIG,manifest_path=MANIFEST):
    return {**_ORIGINAL_PROVENANCE(config_path,manifest_path),'execution_amendment_id':AMENDMENT_ID,
            'generation_entrypoint_sha256':four.digest(Path(__file__)), 'scope_sha256':four.digest(SCOPE)}


def install():
    # These hooks exist only in this explicitly authorized raw-generation process.
    # Independent scoring processes import unchanged original guards and reject
    # the new scope; this entry point has no scoring command or judge transport.
    four.verify_candidate=verify;four.require_execution_gates=authorize
    four.cells_for=cells;four.provenance=provenance
    api_budget.BudgetLedger=GenerationBudget


def report():
    config,manifest,freeze,annotations,prompts=verify();authorize(config,manifest)
    root=four.output_root(config);pins=provenance();models={}
    for p in four.PARTITIONS:
        selected=cells(config,freeze,annotations,prompts,p)
        done,errors=four.validated_records(root/(p+'.jsonl'),config,p,selected,pins)
        starts=four.historical.read_jsonl_records(root/'attempts'/(p+'.jsonl'))
        counts=Counter(r['language'] for r in done.values())
        usage=Counter();finishes=Counter();chars=[]
        for r in done.values():
            finishes[str(r.get('finish_status'))]+=1;chars.append(len(r['response_text']))
            for k,v in (r.get('usage') or {}).items():
                if type(v) is int:usage[k]+=v
        models[p]={'role':'exploratory' if p=='google' else 'primary','model_id':next(m['model_id'] for m in config['models'] if m['partition']==p),
                   'planned':len(selected),'success':len(done),'by_language':{l:counts[l] for l in ('en','bn','bn_cs')},
                   'failed_response_records':errors,'request_attempts':sum(r['status']=='started' for r in starts),
                   'in_flight_attempts':sum(r['status']=='started' for r in starts)-sum(r['status']!='started' for r in starts),
                   'finish_status_counts':dict(finishes),'truncated':sum(bool(r.get('truncated')) for r in done.values()),
                   'empty_visible_text':sum(not r['response_text'].strip() for r in done.values()),
                   'total_visible_characters':sum(chars),'numeric_usage_totals':dict(usage)}
    budget=_OriginalBudget(config,manifest,'generation').summary()
    return {'at_utc':four.historical.utc_now(),'execution_amendment_id':AMENDMENT_ID,'manifest_sha256':four.digest(MANIFEST),
            'primary_completed':sum(models[p]['success'] for p in ('openai','local_a','local_b')),'primary_planned':1413,
            'primary_complete':all(models[p]['success']==471 for p in ('openai','local_a','local_b')),
            'exploratory_completed':models['google']['success'],'exploratory_planned':60,'models':models,'budget':budget,
            'protected_for_later_evaluation_usd':PROTECTED_USD,
            'generation_remaining_usd':max(0,budget['remaining_uncommitted_usd']-PROTECTED_USD),
            'scoring_authorized':False,'scoring_blockers':['original safety-check calibration 25/30 versus 30/30','R1 adjudication pending','independent judge validation after exposure pending'],
            'interpretation':'exploratory objective generation metadata only; no RIU/safety scores, language effects, rankings or validated trustworthiness conclusions'}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--env-file',type=Path)
    sub=parser.add_subparsers(dest='command',required=True)
    sub.add_parser('readiness');sub.add_parser('report')
    p=sub.add_parser('run');p.add_argument('--provider',choices=four.PARTITIONS,required=True);p.add_argument('--limit',type=int)
    sub.add_parser('server')
    args,rest=parser.parse_known_args();load_api_environment(args.env_file);install()
    config,manifest,freeze,annotations,prompts=verify();authorize(config,manifest)
    if args.command=='readiness':print(json.dumps({'generation_ready':True,'scoring_ready':False,'scope':four.read(SCOPE)},indent=2));return 0
    if args.command=='report':print(json.dumps(report(),indent=2));return 0
    if args.command=='server':
        import local_gpu_server
        sys.argv=[str(ROOT/'scripts/local_gpu_server.py'),'--manifest',str(MANIFEST),*rest]
        local_gpu_server.main();return 0
    if rest:parser.error('unexpected arguments')
    if args.limit is not None and args.limit<=0:parser.error('limit must be positive')
    state=four.run_partition(config,manifest,freeze,annotations,prompts,args.provider,args.limit,
                             config_path=BASE_CONFIG,manifest_path=MANIFEST)
    return 75 if state else 0

if __name__=='__main__':
    try:raise SystemExit(main())
    except api_budget.BudgetExceeded as exc:raise SystemExit('BUDGET_PAUSE: '+str(exc))
    except (RuntimeError,ValueError) as exc:raise SystemExit(str(exc))
