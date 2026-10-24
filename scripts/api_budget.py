"""Crash-safe shared paid API budget. Unknown outcomes retain their full hold.

Amounts are integer nano-USD; cached input receives no discount. Reasoning tokens
are already included in output_tokens and are never added a second time.
"""
import contextlib
import fcntl
import hashlib
import json
import os
from pathlib import Path
from datetime import datetime, timezone
from research_approvals import ROOT, require_spending_approval

NANO=1_000_000_000
# USD per million tokens: short input/output, long input/output.
# Sol input uses 1.25x uncached price for ALL tokens to cover cache-write costs.
# Thus settlement remains a conservative usage estimate, not an invoice.
RATES={'gpt-6.1-sol':(2.5,10,5,15), 'gpt-5.4-2026-03-05':(2.5,15,5,22.5)}

class BudgetExceeded(RuntimeError): pass

class BudgetLedger:
    def __init__(self,config,manifest,purpose):
        approval=require_spending_approval(config,manifest,purpose)
        self.approval=approval
        self.cap=int(approval['maximum_usd']*NANO)
        if approval.get('authorization_id')!='prelim-four-v03-usd100-20261023' or self.cap!=100*NANO:
            raise RuntimeError('unexpected paid budget authorization')
        self.root=ROOT/'.local/paid_api_budget'/approval['authorization_id']
        self.root.mkdir(parents=True,exist_ok=True)
        self.path=self.root/'events.jsonl'
        self.purpose=purpose
        self.approval_hash=hashlib.sha256((ROOT/manifest['spending_approval_record']).read_bytes()).hexdigest()

    @contextlib.contextmanager
    def locked(self):
        with (self.root/'lock').open('a') as lock:
            fcntl.flock(lock,fcntl.LOCK_EX)
            yield

    def events(self):
        if not self.path.exists(): return []
        raw=self.path.read_text()
        if raw and not raw.endswith('\n'):raise RuntimeError('incomplete budget ledger; reconcile before spending')
        rows=[json.loads(line) for line in raw.splitlines()]
        if any(r['approval_sha256']!=self.approval_hash or r['cap_nano_usd']!=self.cap for r in rows):
            raise RuntimeError('budget authorization changed; spending blocked')
        return rows

    def append(self,row):
        row={**row,'approval_sha256':self.approval_hash,'cap_nano_usd':self.cap,
             'at_utc':datetime.now(timezone.utc).isoformat()}
        with self.path.open('a') as out:
            out.write(json.dumps(row,sort_keys=True)+'\n');out.flush();os.fsync(out.fileno())

    def state(self,rows):
        holds={};settled={}
        for r in rows:
            rid=r['request_id']
            if r['event']=='reserved':
                if rid in holds or rid in settled:raise RuntimeError('duplicate budget reservation')
                holds[rid]=r
            elif r['event']=='settled':
                if rid not in holds or rid in settled:raise RuntimeError('orphan budget settlement')
                if r['charged_nano_usd']>holds[rid]['reserved_nano_usd']:raise RuntimeError('usage exceeded conservative reservation')
                settled[rid]=r;del holds[rid]
            else:raise RuntimeError('unknown budget event')
        return holds,settled

    def summary(self):
        with self.locked():
            holds,settled=self.state(self.events())
            paid=sum(r['charged_nano_usd'] for r in settled.values())
            held=sum(r['reserved_nano_usd'] for r in holds.values())
            return {'currency':'USD','cap_usd':self.cap/NANO,'settled_usage_estimate_usd':paid/NANO,
                    'reserved_or_uncertain_usd':held/NANO,'remaining_uncommitted_usd':(self.cap-paid-held)/NANO,
                    'settled_requests':len(settled),'held_requests':len(holds)}

    def reserve(self,rid,model,prompt,system,max_output_tokens,extra_input=''):
        rates=RATES[model]
        # UTF-8 byte count bounds byte-level text tokenization. Include serialized
        # schema/instructions plus 4096 tokens for API framing. Always reserve
        # the long-context premium, even for these small requests.
        bound=len((prompt+system+extra_input).encode('utf-8'))+4096
        amount=bound*int(rates[2]*1000)+max_output_tokens*int(rates[3]*1000)
        with self.locked():
            holds,settled=self.state(self.events())
            if rid in holds or rid in settled:raise RuntimeError('request ID already budgeted')
            committed=sum(r['reserved_nano_usd'] for r in holds.values())+sum(r['charged_nano_usd'] for r in settled.values())
            if committed+amount>self.cap:
                raise BudgetExceeded(f'USD 100 cap: committed ${committed/NANO:.9f}; next request needs ${amount/NANO:.9f}; shortfall ${(committed+amount-self.cap)/NANO:.9f}')
            self.append({'event':'reserved','request_id':rid,'model':model,'purpose':self.purpose,
                         'input_token_bound':bound,'max_output_tokens':max_output_tokens,'reserved_nano_usd':amount})

    def settle(self,rid,usage):
        if not isinstance(usage,dict):raise RuntimeError('missing usage: retain full reservation')
        counts=[usage.get('input_tokens'),usage.get('output_tokens')]
        if any(type(v) is not int or v<0 for v in counts):raise RuntimeError('invalid usage: retain full reservation')
        with self.locked():
            holds,settled=self.state(self.events())
            if rid in settled:
                if settled[rid]['usage']!=usage:raise RuntimeError('conflicting budget settlement')
                return
            hold=holds[rid];inp,out=counts;rates=RATES[hold['model']]
            if inp>hold['input_token_bound'] or out>hold['max_output_tokens']:
                raise RuntimeError('usage exceeded token bounds; retain reservation and halt')
            offset=2 if inp>272000 else 0
            amount=inp*int(rates[offset]*1000)+out*int(rates[offset+1]*1000)
            self.append({'event':'settled','request_id':rid,'charged_nano_usd':amount,'usage':usage})
