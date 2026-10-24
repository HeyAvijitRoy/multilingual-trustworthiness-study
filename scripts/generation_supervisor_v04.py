#!/usr/bin/env python3
"""Read-only status and guarded resumption for amendment 0.4 raw generation.

Not part of the frozen execution sources. It never edits frozen files, records,
ledgers or locks, and every response is still produced by the unchanged frozen
entry point `generation_only_v04.py run`. Resumption is allowed only for a worker
the running controller has already recorded as paused (or when the controller is
gone), and it calls `run` without `--limit`: the frozen runner applies `--limit`
before skipping cells whose four-attempt lifetime budget is exhausted, so the
controller's `--limit 1` loop cannot progress past such a cell.
"""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import subprocess
import time

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'.local/prelim_157_four_v03'
CTRL=OUT/'generation_only_v04'
PYTHON=ROOT/'.local/venv/bin/python'
ENTRY=ROOT/'scripts/generation_only_v04.py'
PRIMARY=('openai','local_a','local_b')
TARGET={'openai':471,'local_a':471,'local_b':471,'google':60}
LOCK={'openai':'openai.lock','google':'google.lock','local_a':'local_runtime.lock','local_b':'local_runtime.lock'}
RESUMABLE=('openai','google')


def rows(path):
    if not path.exists():return []
    # Physical lines only: Bengali text may contain Unicode line separators.
    return [json.loads(line) for line in path.read_text(encoding='utf-8').split('\n') if line.strip()]


def epoch(stamp):return datetime.fromisoformat(stamp.replace('Z','+00:00')).timestamp()


def alive(pid):
    try:os.kill(int(pid),0)
    except (OSError,ValueError,TypeError):return False
    return True


def lock_state(path):
    if not path.exists():return None
    try:holder=json.loads(path.read_text())
    except ValueError:return {'path':path.name,'unreadable':True}
    return {'path':path.name,'pid':holder.get('pid'),'holder_alive':alive(holder.get('pid')),'since':holder.get('started_at')}


def partition_status(p,now,window=3600):
    done=[r for r in rows(OUT/(p+'.jsonl')) if r.get('status')=='success']
    errors=sum(1 for r in rows(OUT/(p+'.jsonl')) if r.get('status')=='api_error')
    attempts=rows(OUT/'attempts'/(p+'.jsonl'))
    started={r['attempt_id']:r for r in attempts if r.get('status')=='started'}
    for r in attempts:
        if r.get('status')!='started':started.pop(r.get('attempt_id'),None)
    times=sorted(epoch(r['generated_at_utc']) for r in done)
    recent=[t for t in times if now-t<=window]
    latency=sorted(r['latency_seconds'] for r in done)
    unique={(r['task_id'],r['language']) for r in done}
    per_cell={}
    for r in attempts:
        if r.get('status')=='started':per_cell[r['task_id'],r['language']]=per_cell.get((r['task_id'],r['language']),0)+1
    exhausted=sorted(k for k,n in per_cell.items() if n>=4 and k not in unique)
    http=[r.get('http_status') for r in attempts if r.get('status')=='http_error']
    rate=len(recent)/(window/3600)
    remaining=TARGET[p]-len(unique)
    return {'success':len(done),'unique_cells':len(unique),'duplicates':len(done)-len(unique),'target':TARGET[p],'remaining':remaining,
            'failed_response_records':errors,'attempt_budget_exhausted_cells':[list(k) for k in exhausted],
            'http_error_status_counts':{str(s):http.count(s) for s in sorted(set(http),key=str)},
            'in_flight':[{'task_id':r['task_id'],'language':r['language'],'attempt':r['attempt'],
                          'age_seconds':round(now-epoch(r['started_at_utc']))} for r in started.values()],
            'last_success_utc':datetime.fromtimestamp(times[-1],timezone.utc).isoformat() if times else None,
            'seconds_since_last_success':round(now-times[-1]) if times else None,
            'responses_last_hour':len(recent),
            'median_latency_seconds':latency[len(latency)//2] if latency else None,
            'eta_hours_at_last_hour_rate':round(remaining/rate,2) if rate and remaining>0 else None,
            'empty_visible_text':sum(not r['response_text'].strip() for r in done),'truncated':sum(bool(r.get('truncated')) for r in done)}


def gpu():
    if not shutil.which('nvidia-smi'):return None
    try:
        out=subprocess.run(['nvidia-smi','--query-gpu=name,memory.used,memory.total,utilization.gpu','--format=csv,noheader,nounits'],
                           capture_output=True,text=True,timeout=20).stdout.strip()
        apps=subprocess.run(['nvidia-smi','--query-compute-apps=pid,used_memory','--format=csv,noheader,nounits'],
                            capture_output=True,text=True,timeout=20).stdout.strip()
    except (OSError,subprocess.SubprocessError):return None
    name,used,total,util=[x.strip() for x in out.split(',')]
    return {'name':name,'memory_used_mib':int(used),'memory_total_mib':int(total),'utilization_percent':int(util),
            'processes':[{'pid':int(a.split(',')[0]),'memory_mib':int(a.split(',')[1])} for a in apps.splitlines() if a.strip()]}


def status(now=None):
    now=time.time() if now is None else now
    progress=json.loads((CTRL/'progress.json').read_text()) if (CTRL/'progress.json').exists() else {}
    pid=(CTRL/'controller.pid').read_text().strip() if (CTRL/'controller.pid').exists() else None
    snapshot_age=round(now-epoch(progress['at_utc'])) if progress.get('at_utc') else None
    parts={p:partition_status(p,now) for p in (*PRIMARY,'google')}
    quota=[r for r in rows(ROOT/'.local/google_project_quota/requests.jsonl') if r.get('type')=='reserved']
    days={}
    for r in quota:days[r['pacific_day']]=days.get(r['pacific_day'],0)+1
    deferrals=rows(OUT/'quota_deferrals.jsonl')
    return {'at_utc':datetime.fromtimestamp(now,timezone.utc).isoformat(),
            'controller':{'pid':pid,'alive':alive(pid),'snapshot_age_seconds':snapshot_age,'workers':progress.get('workers',{})},
            'locks':{name:lock_state(OUT/name) for name in sorted(set(LOCK.values()))}|{'gpu_runtime.lock':lock_state(ROOT/'.local/gpu_runtime.lock'),'controller.lock':lock_state(CTRL/'controller.lock')},
            'partitions':parts,'primary_unique_cells':sum(parts[p]['unique_cells'] for p in PRIMARY),'primary_target':1413,
            'gemini_quota_reservations_by_pacific_day':days,'gemini_last_deferral':deferrals[-1].get('retry_at_utc') if deferrals else None,
            'budget':progress.get('budget'),'gpu':gpu(),
            'interpretation':'operational metadata only; success means a preserved provider response, not semantic correctness'}


def resumable(p,state):
    """Return a reason a resume is unsafe, or None. Local GPU phases stay with the controller."""
    if p not in RESUMABLE:return 'only cloud partitions can be resumed by the supervisor'
    ctrl=state['controller'];worker=ctrl['workers'].get(p,{})
    if state['partitions'][p]['remaining']<=0:return 'partition already complete'
    if ctrl['alive'] and worker.get('state')!='paused':return 'controller alive and worker not recorded as paused'
    lock=state['locks'][LOCK[p]]
    if lock and lock.get('holder_alive',True):return 'partition lock held by a live process'
    if lock:return 'stale partition lock present; investigate before removal (never removed automatically)'
    if state['partitions'][p]['in_flight']:return 'unreconciled in-flight attempt; investigate before replay'
    return None


def resume_cloud(p,log):
    """Run the frozen entry point without --limit, waiting across quota deferrals."""
    while True:
        with log.open('a') as handle:
            code=subprocess.run([str(PYTHON),str(ENTRY),'--env-file',str(ROOT/'.env'),'run','--provider',p],
                                cwd=ROOT,stdout=handle,stderr=subprocess.STDOUT).returncode
        if code!=75:return code
        retry=rows(OUT/'quota_deferrals.jsonl')[-1]['retry_at_epoch']
        while time.time()<retry:time.sleep(min(60,max(1,retry-time.time())))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    sub.add_parser('status')
    r=sub.add_parser('resume');r.add_argument('--provider',choices=RESUMABLE,required=True)
    a=parser.parse_args()
    state=status()
    if a.command=='status':print(json.dumps(state,indent=2,ensure_ascii=False));return 0
    reason=resumable(a.provider,state)
    if reason:raise SystemExit('resume refused: '+reason)
    log=CTRL/(a.provider+'.supervisor.log')
    with log.open('a') as handle:handle.write(json.dumps({'at_utc':state['at_utc'],'event':'supervisor_resume','provider':a.provider,'pid':os.getpid()})+'\n')
    return resume_cloud(a.provider,log)


if __name__=='__main__':raise SystemExit(main())
