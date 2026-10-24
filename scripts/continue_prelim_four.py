#!/usr/bin/env python3
"""Operational supervisor for the approved preliminary study; no scientific edits.

All generation/scoring uses frozen CLIs, one pending cell per invocation. Thread
locks keep scoring from reading a partition during an in-flight generation.
On failure, stop new requests, allow existing requests to finish, and preserve
all receipts/holds. Free Google waits across Pacific quota days. No paid fallback.
"""
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import threading
import time
import urllib.request
import urllib.error

import prelim_four as four
from prelim_four_judge import ScoringContext
from report_prelim_four_progress import report

PYTHON=four.ROOT/'.local/venv/bin/python'
GPU_PYTHON=four.ROOT/'.local/gpu-venv/bin/python'
MANIFEST=four.AMENDMENT/'FREEZE.json'


class Supervisor:
    def __init__(self):
        os.environ.setdefault('PRELIM_LOCAL_A_BASE_URL','http://127.0.0.1:8765/v1')
        os.environ.setdefault('PRELIM_LOCAL_B_BASE_URL','http://127.0.0.1:8765/v1')
        self.ctx=ScoringContext(four.CONFIG,MANIFEST)
        self.ctx.frozen()
        four.require_execution_gates(self.ctx.config,self.ctx.manifest,four.CONFIG,MANIFEST)
        self.root=self.ctx.root/'supervisor';self.root.mkdir(parents=True,exist_ok=True)
        self.stop=threading.Event();self.locks={p:threading.Lock() for p in four.PARTITIONS}
        self.errors=[];self.error_lock=threading.Lock()
        self.env=dict(os.environ);self.env['PYTORCH_ALLOC_CONF']='expandable_segments:True'
        # The operational launch is separately hash-bound; the scientific freeze
        # remains immutable. CLI implementations independently enforce its pins.
        four.historical.append_jsonl(self.root/'events.jsonl',{
            'event':'launch','at_utc':four.historical.utc_now(),'pid':os.getpid(),
            'freeze_sha256':four.digest(MANIFEST),'supervisor_sha256':four.digest(Path(__file__)),
            'report_script_sha256':four.digest(Path(__file__).with_name('report_prelim_four_progress.py'))})

    def fail(self,label):
        with self.error_lock:self.errors.append(label)
        self.stop.set()
        four.historical.append_jsonl(self.root/'events.jsonl',{'event':'pause','reason':label,'at_utc':four.historical.utc_now()})

    def command(self,script,args,label,allowed=(0,)):
        cmd=[str(PYTHON),str(four.ROOT/'scripts'/script),'--manifest',str(MANIFEST),'--env-file',str(four.ROOT/'.env'),*args]
        with (self.root/(label+'.log')).open('a') as log:
            result=subprocess.run(cmd,cwd=four.ROOT,env=self.env,stdout=log,stderr=subprocess.STDOUT)
        if result.returncode not in allowed:raise RuntimeError(label+' failed; inspect preserved '+label+'.log')
        return result.returncode

    def successes(self,p):
        return sum(r.get('status')=='success' for r in four.historical.read_jsonl_records(self.ctx.root/(p+'.jsonl')))

    def generate(self,p):
        while not self.stop.is_set():
            with self.locks[p]:
                before=self.successes(p)
                if before==471:return
                code=self.command('prelim_four.py',['run','--provider',p,'--limit','1'],'generate_'+p,allowed=(0,75))
                if code==0 and self.successes(p)!=before+1:
                    raise RuntimeError(p+' produced no new success; generation paused for failure reconciliation')
            if code==75:
                deferred=four.historical.read_jsonl_records(self.ctx.root/'quota_deferrals.jsonl')[-1]
                target=deferred['retry_at_epoch']
                while not self.stop.is_set() and time.time()<target:
                    self.stop.wait(min(60,target-time.time()))

    def guarded(self,label,func):
        try:func()
        except Exception as exc:self.fail(label+': '+str(exc))

    def locals(self):
        for p in ('local_a','local_b'):
            if self.stop.is_set():return
            if self.successes(p)==471:continue
            model=next(m for m in self.ctx.config['models'] if m['partition']==p)
            # Do not attach to or replace an unknown server using the study port.
            try:
                with urllib.request.urlopen('http://127.0.0.1:8765/v1/models',timeout=2):
                    raise RuntimeError('local study port already occupied; inspect before launching')
            except urllib.error.URLError:pass
            cmd=[str(GPU_PYTHON),str(four.ROOT/'scripts/local_gpu_server.py'),
                 '--model',model['model_id'],'--revision',model['weights_revision'],
                 '--partition',p,'--context',str(model['context_tokens']),
                 '--manifest',str(MANIFEST),'--env-file',str(four.ROOT/'.env'),
                 '--raw-log',str(self.ctx.root/'local_server'/('raw_'+p+'.jsonl'))]
            with (self.root/('server_'+p+'.log')).open('a') as log:
                server=subprocess.Popen(cmd,cwd=four.ROOT,env=self.env,stdout=log,stderr=subprocess.STDOUT)
                try:
                    deadline=time.monotonic()+1800
                    while not self.stop.is_set():
                        if server.poll() is not None:raise RuntimeError(p+' server exited before ready')
                        try:
                            with urllib.request.urlopen('http://127.0.0.1:8765/v1/models',timeout=2) as response:
                                metadata=json.load(response)
                            if (metadata.get('diagnostic_only') or metadata['data'][0]['id']!=model['model_id']
                                    or metadata['data'][0]['revision']!=model['weights_revision']):
                                raise RuntimeError('unexpected local runtime identity/mode')
                            break
                        except urllib.error.URLError:
                            if time.monotonic()>deadline:raise RuntimeError(p+' server startup deadline exceeded')
                            self.stop.wait(5)
                    if not self.stop.is_set():self.generate(p)
                finally:
                    if server.poll() is None:
                        # At this boundary no local request remains in flight.
                        # SIGINT unwinds the server's context-managed GPU lock.
                        server.send_signal(signal.SIGINT)
                        try:server.wait(timeout=60)
                        except subprocess.TimeoutExpired:raise RuntimeError('local server did not shut down; inspect before further GPU use')

    def snapshot(self,status):
        data={**report(),'supervisor_status':status,'supervisor_errors':list(self.errors)}
        tmp=self.root/'progress.tmp';tmp.write_text(json.dumps(data,indent=2)+'\n');tmp.replace(self.root/'progress.json')

    def run(self):
        with four.partition_lock(self.root,'supervisor'):
            workers=[threading.Thread(target=self.guarded,args=(p,lambda p=p:self.generate(p)),name=p)
                     for p in ('openai','google')]
            workers.append(threading.Thread(target=self.guarded,args=('locals',self.locals),name='locals'))
            for thread in workers:thread.start()
            try:
                while not self.stop.is_set():
                    scored=False
                    for p in four.PARTITIONS:
                        if self.stop.is_set():break
                        with self.locks[p]:
                            generated=self.successes(p)
                            existing=len(four.historical.read_jsonl_records(self.ctx.root/'scores'/(p+'.jsonl')))
                            if generated>existing:
                                self.command('prelim_four_judge.py',['score','--provider',p,'--limit','1'],'score_'+p)
                                scored=True
                    self.snapshot('running')
                    if not any(t.is_alive() for t in workers) and not scored:break
                    if not scored:self.stop.wait(30)
            except Exception as exc:self.fail('scoring/supervision: '+str(exc))
            finally:
                # Never abandon an in-flight response merely because a different
                # worker hit the cap. Reservations already cover active requests.
                if self.errors:self.stop.set()
                for thread in workers:
                    while thread.is_alive():thread.join(timeout=30)
            if self.errors:
                self.snapshot('paused-requires-reconciliation');return 3
            if sum(self.successes(p) for p in four.PARTITIONS)!=1884:
                self.fail('incomplete generation panel');self.snapshot('paused-incomplete');return 3
            self.command('prelim_four_judge.py',['qa','--out-dir',str(self.ctx.root/'qa/first_pass')],'prepare_qa')
            self.snapshot('awaiting-independent-human-QA')
            return 0

if __name__=='__main__':
    from research_approvals import load_api_environment
    load_api_environment(four.ROOT/'.env')
    try:raise SystemExit(Supervisor().run())
    except (RuntimeError,ValueError) as exc:raise SystemExit(str(exc))
