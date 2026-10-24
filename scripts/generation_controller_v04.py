#!/usr/bin/env python3
"""Resume raw generation only; Gemini never gates primary completion. No scoring."""
import json
import os
from pathlib import Path
import signal
import subprocess
import threading
import time
import urllib.request
import urllib.error

import generation_only_v04 as gen
from research_approvals import load_api_environment

ROOT=gen.ROOT
PYTHON=ROOT/'.local/venv/bin/python'
GPU_PYTHON=ROOT/'.local/gpu-venv/bin/python'


class Controller:
    def __init__(self):
        self.config,self.manifest,*_=gen.verify();gen.authorize(self.config,self.manifest)
        self.root=gen.four.output_root(self.config)/'generation_only_v04';self.root.mkdir(parents=True,exist_ok=True)
        self.stop=threading.Event();self.states={};self.state_lock=threading.Lock()
        self.env=dict(os.environ);self.env.update(PRELIM_LOCAL_A_BASE_URL='http://127.0.0.1:8765/v1',PRELIM_LOCAL_B_BASE_URL='http://127.0.0.1:8765/v1',PYTORCH_ALLOC_CONF='expandable_segments:True')

    def event(self,**row):gen.four.historical.append_jsonl(self.root/'events.jsonl',{'at_utc':gen.four.historical.utc_now(),**row})
    def count(self,p):return sum(r.get('status')=='success' for r in gen.four.historical.read_jsonl_records(gen.four.output_root(self.config)/(p+'.jsonl')))
    def guarded(self,p,fn):
        try:fn()
        except Exception as exc:
            with self.state_lock:self.states[p]={'state':'paused','reason':str(exc)}
            self.event(event='worker_paused',worker=p,reason=str(exc))

    def generate(self,p,target):
        while not self.stop.is_set() and self.count(p)<target:
            before=self.count(p)
            command=[str(PYTHON),str(ROOT/'scripts/generation_only_v04.py'),'--env-file',str(ROOT/'.env'),'run','--provider',p,'--limit','1']
            with (self.root/(p+'.log')).open('a') as log:
                result=subprocess.run(command,cwd=ROOT,env=self.env,stdout=log,stderr=subprocess.STDOUT)
            if result.returncode==75:
                rows=gen.four.historical.read_jsonl_records(gen.four.output_root(self.config)/'quota_deferrals.jsonl');target_time=rows[-1]['retry_at_epoch']
                with self.state_lock:self.states[p]={'state':'quota_wait','retry_at_utc':rows[-1]['retry_at_utc']}
                while not self.stop.is_set() and time.time()<target_time:self.stop.wait(min(60,target_time-time.time()))
                continue
            if result.returncode!=0:raise RuntimeError(p+' paused; inspect '+p+'.log (includes budget/identity/transport details)')
            if self.count(p)!=before+1:raise RuntimeError(p+' did not yield a new completed response; inspect preserved failure records')
            with self.state_lock:self.states[p]={'state':'collecting','completed':before+1,'target':target}
        with self.state_lock:self.states[p]={'state':'complete' if self.count(p)>=target else 'stopped','completed':self.count(p),'target':target}

    def local_phase(self,p,target):
        if self.stop.is_set() or self.count(p)>=target:return
        model=next(m for m in self.config['models'] if m['partition']==p)
        try:
            with urllib.request.urlopen('http://127.0.0.1:8765/v1/models',timeout=2):raise RuntimeError('study GPU port already occupied; inspect before replacement')
        except urllib.error.URLError:pass
        command=[str(GPU_PYTHON),str(ROOT/'scripts/generation_only_v04.py'),'--env-file',str(ROOT/'.env'),'server',
                 '--model',model['model_id'],'--revision',model['weights_revision'],'--partition',p,'--context',str(model['context_tokens']),
                 '--raw-log',str(self.root/('server_raw_'+p+'.jsonl'))]
        with (self.root/('server_'+p+'.log')).open('a') as log:
            server=subprocess.Popen(command,cwd=ROOT,env=self.env,stdout=log,stderr=subprocess.STDOUT)
            try:
                deadline=time.monotonic()+1800
                while not self.stop.is_set():
                    if server.poll() is not None:raise RuntimeError(p+' GPU server exited before ready; inspect server log')
                    try:
                        with urllib.request.urlopen('http://127.0.0.1:8765/v1/models',timeout=2) as response:metadata=json.load(response)
                        if metadata.get('diagnostic_only') or metadata['data'][0]['id']!=model['model_id'] or metadata['data'][0]['revision']!=model['weights_revision']:raise RuntimeError('local server provenance/routing mismatch')
                        break
                    except urllib.error.URLError:
                        if time.monotonic()>deadline:raise RuntimeError('GPU server startup timed out')
                        self.stop.wait(3)
                if not self.stop.is_set():self.generate(p,target)
            finally:
                if server.poll() is None:
                    server.send_signal(signal.SIGINT)
                    try:server.wait(timeout=60)
                    except subprocess.TimeoutExpired:raise RuntimeError('GPU server did not stop cleanly; inspect before reuse')

    def locals(self):
        # Fixed prospective warm-start schedule, preserving each model's exact
        # internal task order and independent requests; never co-load the pair.
        for p,target in [('local_a',6),('local_b',6),('local_a',471),('local_b',471)]:self.local_phase(p,target)

    def run(self):
        with gen.four.partition_lock(self.root,'controller'):
            (self.root/'controller.pid').write_text(str(os.getpid())+'\n')
            self.event(event='controller_start',pid=os.getpid(),manifest_sha256=gen.four.digest(gen.MANIFEST))
            workers=[threading.Thread(target=self.guarded,args=('openai',lambda:self.generate('openai',471))),
                     threading.Thread(target=self.guarded,args=('google',lambda:self.generate('google',60))),
                     threading.Thread(target=self.guarded,args=('locals',self.locals))]
            for w in workers:w.start()
            primary_reported=False
            while any(w.is_alive() for w in workers):
                if (self.root/'STOP').exists():self.stop.set()
                try:
                    snapshot=gen.report()
                    with self.state_lock:snapshot['workers']=dict(self.states)
                    temp=self.root/'progress.tmp';temp.write_text(json.dumps(snapshot,indent=2)+'\n');temp.replace(self.root/'progress.json')
                    if snapshot['primary_complete'] and not primary_reported:
                        self.event(event='primary_generation_complete',responses=1413,gemini_not_a_gate=True);primary_reported=True
                except Exception as exc:self.event(event='snapshot_deferred',error_type=type(exc).__name__)
                self.stop.wait(15)
            for w in workers:w.join()
            snapshot=gen.report();snapshot['workers']=self.states
            (self.root/'progress.json').write_text(json.dumps(snapshot,indent=2)+'\n')
            self.event(event='controller_finished',primary_completed=snapshot['primary_completed'],exploratory_completed=snapshot['exploratory_completed'])

if __name__=='__main__':
    load_api_environment(ROOT/'.env');Controller().run()
