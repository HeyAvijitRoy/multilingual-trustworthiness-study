#!/usr/bin/env python3
"""Single-model loopback adapter using the identical benchmarked CUDA runtime.

Diagnostic mode refuses every frozen study prompt. Study mode independently
requires an approved freeze and exact selected partition settings.
"""
import argparse
import hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from pathlib import Path
import time
import uuid

from local_gpu_runtime import GPURuntime, ROOT, SYSTEM, canonical_request_id
import prelim_four as four
import prelim_eval_157 as historical


def validate_request(body, model_id, diagnostic_only):
    if not isinstance(body,dict):raise ValueError('JSON object required')
    allowed={'model','messages','max_tokens','stream','temperature','seed','chat_template_kwargs','request_id'}
    if set(body)-allowed or body.get('model') != model_id or body.get('stream',False):
        raise ValueError('unsupported request settings or model routing')
    if body.get('temperature',0) != 0 or body.get('seed',20261023) != 20261023:
        raise ValueError('pinned greedy decoding and seed required')
    if body.get('chat_template_kwargs',{'enable_thinking':False}) != {'enable_thinking':False}:
        raise ValueError('thinking must remain disabled')
    messages=body.get('messages',[])
    if len(messages)!=2 or messages[0]!={'role':'system','content':SYSTEM} or messages[1].get('role')!='user':
        raise ValueError('exact stateless system/user request required')
    prompt=messages[1].get('content')
    if not isinstance(prompt,str): raise ValueError('text prompt required')
    allowance=body.get('max_tokens')
    if isinstance(allowance,bool) or not isinstance(allowance,int) or allowance<=0 or allowance>32768:
        raise ValueError('invalid output allowance')
    if not diagnostic_only and allowance!=32768:
        raise ValueError('study allowance may not be reduced')
    if body.get('request_id')!=canonical_request_id(body):
        raise ValueError('deterministic request identity required')
    return prompt,allowance


def validate_log_provenance(records,provenance):
    fields=('model_id','revision','artifact_sha256','runtime_script_sha256',
            'context_tokens','versions','diagnostic_only','protocol_id',
            'manifest_sha256','config_sha256','server_script_sha256')
    if records and not any(r.get('type')=='server_provenance' for r in records):
        raise RuntimeError('existing server log lacks runtime provenance')
    for row in records:
        if row.get('type')=='server_provenance' and any(row.get(k)!=provenance.get(k) for k in fields):
            raise RuntimeError('existing server log belongs to different runtime, mode or protocol provenance')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--model',required=True)
    p.add_argument('--revision',required=True)
    p.add_argument('--port',type=int,default=8765)
    p.add_argument('--context',type=int,default=40960)
    p.add_argument('--raw-log',type=Path,required=True)
    p.add_argument('--diagnostic-only',action='store_true')
    p.add_argument('--partition',choices=['local_a','local_b'])
    p.add_argument('--config',type=Path,default=four.CONFIG)
    p.add_argument('--manifest',type=Path,default=four.MANIFEST)
    p.add_argument('--env-file',type=Path)
    args=p.parse_args()
    from research_approvals import load_api_environment
    load_api_environment(args.env_file)
    if not args.raw_log.resolve().is_relative_to(ROOT/'.local'):
        p.error('append-only raw log under .local required')
    config,manifest,freeze,annotations,prompts=four.verify_candidate(args.config.resolve(),args.manifest.resolve())
    if not args.diagnostic_only:
        four.require_frozen(config,manifest,args.config.resolve(),args.manifest.resolve())
        four.require_execution_gates(config,manifest,args.config.resolve(),args.manifest.resolve())
        selected=next(m for m in config['models'] if m['partition']==args.partition)
        if (selected['model_id'],selected['weights_revision'],selected['context_tokens']) != (args.model,args.revision,args.context):
            p.error('server settings differ from selected frozen partition')
    frozen_hashes={hashlib.sha256(row['prompt_'+lang].encode()).hexdigest()
                   for row in prompts.values() for lang in ('en','bn','bn_cs')}
    with four.partition_lock(ROOT/'.local','gpu_runtime'):
        runtime=GPURuntime(args.model,args.revision,args.context)
        old=historical.read_jsonl_records(args.raw_log)
        log_provenance={**runtime.provenance,'diagnostic_only':args.diagnostic_only,
                        'protocol_id':config['protocol_id'],
                        'manifest_sha256':four.digest(args.manifest),
                        'config_sha256':four.digest(args.config),
                        'server_script_sha256':four.digest(Path(__file__))}
        validate_log_provenance(old,log_provenance)
        started_requests={r['request_id']:r for r in old if r.get('type')=='request_started'}
        received={r['request_id']:r['payload'] for r in old if r.get('type')=='response_received'}
        failed={r['request_id']:r['error'] for r in old if r.get('type')=='request_failed' and 'request_id' in r}
        historical.append_jsonl(args.raw_log,{'type':'server_provenance',**log_provenance,
                                           'at_utc':historical.utc_now()})
        class Handler(BaseHTTPRequestHandler):
            def log_message(self,*args): pass  # Never echo prompts/request bodies to console.
            def send(self,status,payload):
                encoded=json.dumps(payload,ensure_ascii=False).encode()
                self.send_response(status);self.send_header('Content-Type','application/json')
                self.send_header('Content-Length',str(len(encoded)));self.end_headers();self.wfile.write(encoded)
            def do_GET(self):
                if self.path!='/v1/models': return self.send(404,{'error':'unknown route'})
                self.send(200,{'data':[{'id':args.model,'revision':args.revision}],
                               'runtime_provenance':runtime.provenance,'diagnostic_only':args.diagnostic_only})
            def do_POST(self):
                if self.path!='/v1/chat/completions': return self.send(404,{'error':'unknown route'})
                rid='local-'+uuid.uuid4().hex
                started=time.perf_counter()
                try:
                    size=int(self.headers.get('Content-Length','0'))
                    if size<=0 or size>2*1024*1024: raise ValueError('invalid request size')
                    body=json.loads(self.rfile.read(size))
                    prompt,allowance=validate_request(body,args.model,args.diagnostic_only)
                    request_id=body['request_id']
                    if args.diagnostic_only and hashlib.sha256(prompt.encode()).hexdigest() in frozen_hashes:
                        raise ValueError('study prompt refused by diagnostic-only server')
                    if request_id in received: return self.send(200,received[request_id])
                    if request_id in failed: return self.send(500,failed[request_id])
                    if request_id in started_requests:
                        raise ValueError('ambiguous interrupted local generation; inspect raw log before replay')
                    started_requests[request_id]={'request':body}
                    historical.append_jsonl(args.raw_log,{'type':'request_started','id':rid,
                        'request_id':request_id,'request':body,'at_utc':historical.utc_now()})
                    output=runtime.generate(prompt,allowance)
                    payload={'id':rid,'model':args.model,'revision':args.revision,
                             'choices':[{'message':{'role':'assistant','content':output['response_text']},
                                         'finish_reason':output['finish_reason']}],
                             'usage':{'prompt_tokens':output['input_tokens'],'completion_tokens':output['output_tokens'],
                                      'total_tokens':output['input_tokens']+output['output_tokens']},
                             'timings':{k:v for k,v in output.items() if k not in {'response_text','response_raw_text','output_token_ids'}},
                             'raw_text':output['response_raw_text'],'output_token_ids':output['output_token_ids'],
                             'runtime_provenance':runtime.provenance}
                    historical.append_jsonl(args.raw_log,{'type':'response_received','id':rid,'payload':payload,
                                                       'request_id':request_id,'at_utc':historical.utc_now()})
                    received[request_id]=payload
                    self.send(200,payload)
                except Exception as exc:
                    payload={'error':{'type':type(exc).__name__,'message':str(exc)},'id':rid,
                             **({'unscored_raw_output':exc.raw_output} if hasattr(exc,'raw_output') else {})}
                    historical.append_jsonl(args.raw_log,{'type':'request_failed','id':rid,'error':payload,
                                                       **({'request_id':body['request_id']} if 'body' in locals() and isinstance(body,dict) and body.get('request_id') else {}),
                                                       'seconds':time.perf_counter()-started,'at_utc':historical.utc_now()})
                    if 'body' in locals() and isinstance(body,dict) and body.get('request_id'):
                        failed[body['request_id']]=payload
                    self.send(400 if isinstance(exc,ValueError) else 500,payload)
        print(json.dumps({'status':'ready','model':args.model,'diagnostic_only':args.diagnostic_only,'port':args.port}),flush=True)
        HTTPServer(('127.0.0.1',args.port),Handler).serve_forever()


if __name__=='__main__': main()
