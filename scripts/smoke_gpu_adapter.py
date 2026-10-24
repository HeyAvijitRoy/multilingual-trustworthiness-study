#!/usr/bin/env python3
"""Real synthetic adapter smoke: routing, idempotency, refusal and raw provenance.

Starts only its own diagnostic-only server and stops it with SIGINT so its GPU
lock is released. No frozen-prompt generation or cloud request is permitted.
"""
import argparse
import hashlib
import json
from pathlib import Path
import signal
import subprocess
import sys
import time
import urllib.error
import urllib.request

import prelim_four as four
import prelim_eval_157 as historical
from local_gpu_runtime import SYSTEM, canonical_request_id


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--model',required=True);p.add_argument('--revision',required=True)
    p.add_argument('--output',type=Path,required=True);p.add_argument('--port',type=int,default=8765)
    args=p.parse_args();destination=args.output.resolve()
    if not destination.is_relative_to(four.ROOT/'.local') or destination.exists():
        p.error('new ignored .local output directory required')
    destination.mkdir(parents=True)
    base=f'http://127.0.0.1:{args.port}/v1'
    with (destination/'console.log').open('x') as console:
        process=subprocess.Popen([sys.executable,str(four.ROOT/'scripts/local_gpu_server.py'),
            '--model',args.model,'--revision',args.revision,'--context','40960','--port',str(args.port),
            '--diagnostic-only','--raw-log',str(destination/'server.jsonl')],stdout=console,stderr=console)
        try:
            deadline=time.monotonic()+600
            while True:
                if process.poll() is not None:raise RuntimeError('diagnostic server exited; inspect console.log')
                try:
                    with urllib.request.urlopen(base+'/models',timeout=2) as handle:metadata=json.load(handle)
                    break
                except (urllib.error.URLError,TimeoutError):
                    if time.monotonic()>deadline:raise RuntimeError('diagnostic server startup timed out')
                    time.sleep(.5)
            prov=metadata['runtime_provenance']
            if metadata['data'][0]['id']!=args.model or not metadata['diagnostic_only']:
                raise RuntimeError('unexpected diagnostic server')
            model={'model_id':args.model,'weights_revision':args.revision,'context_tokens':40960,
                   'engine':'openai-compatible-local-server',
                   'engine_version':prov['engine_version'],'weights_sha256':{k:v for k,v in prov['artifact_sha256'].items() if k.endswith('.safetensors')},
                   'tokenizer_sha256':{k:v for k,v in prov['artifact_sha256'].items() if k in ('tokenizer.json','tokenizer_config.json')},
                   'decoding':{'temperature':0,'seed':20261023,'chat_template_kwargs':{'enable_thinking':False}},
                   'endpoint_env':'PRELIM_SMOKE_BASE_URL'}
            import os
            os.environ['PRELIM_SMOKE_BASE_URL']=base
            prompt='Fictional diagnostic: a staging test passed but production approval is pending. In one sentence, explain whether this permits production deployment. Do not invent approval.'
            a=four.local_chat(model,prompt,SYSTEM,900,128)
            b=four.local_chat(model,prompt,SYSTEM,900,128)
            if a['provider_raw_response']['id']!=b['provider_raw_response']['id']:
                raise RuntimeError('identical request generated twice')
            _,_,_,_,prompts=four.verify_candidate()
            frozen=next(iter(prompts.values()))['prompt_en']
            body={'model':args.model,'messages':[{'role':'system','content':SYSTEM},{'role':'user','content':frozen}],
                  'max_tokens':128,'temperature':0,'stream':False}
            body['request_id']=canonical_request_id(body)
            rejected={}
            for label,request in [('frozen_prompt',body),('wrong_model',{**body,'model':'DIAGNOSTIC_WRONG_MODEL'})]:
                try:four.local_http_json(base+'/chat/completions',{'Content-Type':'application/json'},request,30)
                except historical.ProviderHTTPError as exc:rejected[label]={'status':exc.status,'payload':exc.payload}
                else:raise RuntimeError('diagnostic server failed to reject '+label)
            result={'model_id':args.model,'revision':args.revision,'at_utc':historical.utc_now(),
                    'runtime_provenance':prov,'adapter_script_sha256':four.digest(Path(four.__file__)),
                    'smoke_script_sha256':four.digest(Path(__file__)),'synthetic_response':a,
                    'identical_request_reused':True,'rejections':rejected,'study_generations':0}
            (destination/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
            print(json.dumps({'model_id':args.model,'status':'passed','idempotency':True,'study_generations':0}),flush=True)
        finally:
            if process.poll() is None:
                process.send_signal(signal.SIGINT)
                try:process.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    process.kill();process.wait()
                    raise RuntimeError('forced server stop; inspect GPU lock before continuing')


if __name__=='__main__':main()
