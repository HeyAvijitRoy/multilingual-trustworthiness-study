"""Project/model quota accounting across protocols, processes and Pacific days.

Every attempted request consumes a durable reservation, including failures and
ambiguous interruptions. No keys, prompts or private project identifiers are
stored. Limits require actual account evidence; published limits are not defaults.
"""
from datetime import datetime, time as day_time, timedelta, timezone
import hashlib
import json
from pathlib import Path
import re
import time
from zoneinfo import ZoneInfo

import prelim_eval_157 as records

ROOT=Path(__file__).resolve().parents[1]
PACIFIC=ZoneInfo('America/Los_Angeles')


class QuotaDeferred(RuntimeError):
    def __init__(self,reason,retry_at):
        self.reason,self.retry_at=reason,retry_at
        self.retry_at_utc=datetime.fromtimestamp(retry_at,timezone.utc).isoformat()
        super().__init__(reason+'; resume at or after '+self.retry_at_utc)


def next_day(epoch):
    local=datetime.fromtimestamp(epoch,PACIFIC)
    return datetime.combine(local.date()+timedelta(days=1),day_time.min,tzinfo=PACIFIC).timestamp()


def validate_settings(settings):
    if (settings.get('status')!='verified-account-evidence' or settings.get('billing_tier')!='free'
            or settings.get('free_tier_eligible') is not True
            or not settings.get('verified_at') or not settings.get('verified_by')):
        raise RuntimeError('actual project free-tier eligibility and quotas are unverified')
    if settings.get('model_id')!='gemini-3.8-flash':raise RuntimeError('quota model differs from selected panel')
    if settings.get('day_timezone')!='America/Los_Angeles':raise RuntimeError('Pacific daily quota reset required')
    for field in ('rpm','input_tpm','rpd'):
        if type(settings.get(field)) is not int or settings[field]<=0:
            raise RuntimeError('positive account-specific quota required: '+field)
    if not re.fullmatch('[a-z0-9_-]+',settings.get('project_alias','')):
        raise RuntimeError('stable non-secret project alias required')
    evidence=(ROOT/(settings.get('evidence_path') or '')).resolve()
    if (not evidence.is_relative_to(ROOT) or not evidence.is_file()
            or hashlib.sha256(evidence.read_bytes()).hexdigest()!=settings.get('evidence_sha256')):
        raise RuntimeError('dated account quota evidence missing or changed')
    directory=(ROOT/settings['ledger_directory']).resolve()
    if not directory.is_relative_to(ROOT/'.local') or directory==ROOT/'.local':
        raise RuntimeError('shared ignored project quota directory required')


class QuotaLedger:
    def __init__(self,path,*,clock=time.time):
        self.settings_path=Path(path)
        self.settings=json.loads(self.settings_path.read_text())
        validate_settings(self.settings)
        self.root=(ROOT/self.settings['ledger_directory']).resolve()
        self.path=self.root/'requests.jsonl';self.clock=clock
        self.pin=hashlib.sha256(self.settings_path.read_bytes()).hexdigest()

    def own(self,rows):
        return [r for r in rows if r.get('project_alias')==self.settings['project_alias']
                and r.get('model_id')==self.settings['model_id']]

    def event(self,kind,epoch,**fields):
        return {'type':kind,'project_alias':self.settings['project_alias'],'model_id':self.settings['model_id'],
                'epoch':epoch,'at_utc':datetime.fromtimestamp(epoch,timezone.utc).isoformat(),
                'quota_settings_sha256':self.pin,**fields}

    def reserve(self,request_id,input_tokens,protocol_id,prompt_sha256):
        from prelim_four import partition_lock
        if type(input_tokens) is not int or input_tokens<=0:raise ValueError('positive input reservation required')
        with partition_lock(self.root,self.settings['project_alias']):
            now=self.clock();rows=self.own(records.read_jsonl_records(self.path))
            if any(r['epoch']>now+.01 for r in rows):raise RuntimeError('quota clock moved backwards; investigate before resume')
            attempts=[r for r in rows if r['type']=='reserved']
            if any(r['request_id']==request_id for r in attempts):raise RuntimeError('request already accounted; do not replay')
            cool=max((r['retry_at'] for r in rows if r['type']=='cooldown'),default=0)
            if cool>now:raise QuotaDeferred('provider rate-limit cooldown',cool)
            day=datetime.fromtimestamp(now,PACIFIC).date().isoformat()
            if sum(r['pacific_day']==day for r in attempts)>=self.settings['rpd']:
                raise QuotaDeferred('project daily request budget exhausted',next_day(now))
            window=[r for r in attempts if r['epoch']>now-60]
            if len(window)>=self.settings['rpm']:
                raise QuotaDeferred('project rolling RPM budget exhausted',min(r['epoch'] for r in window)+60.01)
            if input_tokens>self.settings['input_tpm']:
                raise RuntimeError('conservative input reservation exceeds account TPM; verify exact tokens, do not truncate prompt')
            actual={r['request_id']:r['input_tokens'] for r in rows if r['type']=='usage'}
            if sum(max(r['input_token_reservation'],actual.get(r['request_id'],0)) for r in window)+input_tokens>self.settings['input_tpm']:
                raise QuotaDeferred('project rolling input TPM budget exhausted',min(r['epoch'] for r in window)+60.01)
            row=self.event('reserved',now,request_id=request_id,input_token_reservation=input_tokens,
                           pacific_day=day,protocol_id=protocol_id,prompt_sha256=prompt_sha256)
            records.append_jsonl(self.path,row)
            return row

    def finish(self,request_id,*,usage=None,error_status=None,error_payload=None,backoff_seconds=2):
        from prelim_four import partition_lock
        with partition_lock(self.root,self.settings['project_alias']):
            now=self.clock();rows=self.own(records.read_jsonl_records(self.path))
            if not any(r.get('request_id')==request_id and r['type']=='reserved' for r in rows):
                raise RuntimeError('quota outcome has no request reservation')
            if usage is not None:
                count=usage.get('promptTokenCount')
                if type(count) is int and count>=0:
                    records.append_jsonl(self.path,self.event('usage',now,request_id=request_id,input_tokens=count))
            if error_status==429:
                payload=error_payload or {};error=payload.get('error',{})
                details=error.get('details',[]) if isinstance(error,dict) else []
                retry=max(float(payload.get('_retry_after_seconds') or 0),backoff_seconds)
                for detail in details:
                    delay=detail.get('retryDelay','')
                    if re.fullmatch(r'\d+(\.\d+)?s',delay):retry=max(retry,float(delay[:-1]))
                # Preserve a day-level denial as a day-level cooldown, even if
                # Google doesn't provide RetryInfo. Never retry through a quota.
                daily=any('perday' in json.dumps(d).lower().replace('_','') for d in details)
                until=max(now+retry,next_day(now) if daily else 0)
                records.append_jsonl(self.path,self.event('cooldown',now,request_id=request_id,retry_at=until,
                                                          reason='provider_429_daily' if daily else 'provider_429'))


def input_reservation(prompt,system):
    # Conservative byte proxy plus envelope overhead, not a model-token count.
    # Actual provider prompt usage may only increase the rolling reservation.
    return len((system+prompt).encode('utf-8'))+1024
