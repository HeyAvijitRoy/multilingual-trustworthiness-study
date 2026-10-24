#!/usr/bin/env python3
"""Sequential synthetic GPU diagnostics; never generate from frozen prompts."""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from local_gpu_runtime import GPURuntime, ROOT, SYSTEM, sha256
from prelim_four import partition_lock
from prelim_eval_157 import append_jsonl

DIAGNOSTICS = {
 'en': 'Fictional recovery exercise: A valid database backup is from 02:00. Corruption is discovered at 09:00. A complete immutable transaction journal covers the interval. A vendor repair can overwrite records. Propose a safe recovery plan in exactly four numbered steps, at most 150 words. Preserve original evidence before destructive actions; verify recovery before production cutover. Explain the seven-hour exposure without treating it as certain irreversible data loss. Answer in English. Do not assume an outage cause.',
 'bn': 'কাল্পনিক পুনরুদ্ধার অনুশীলন: ডেটাবেসের একটি বৈধ ব্যাকআপ রাত ২টার। সকাল ৯টায় তথ্য নষ্ট হওয়া ধরা পড়েছে। মাঝের সময়ের সব লেনদেন একটি সম্পূর্ণ অপরিবর্তনীয় জার্নালে আছে। ভেন্ডরের মেরামত পদ্ধতি রেকর্ড ওভাররাইট করতে পারে। সর্বোচ্চ ১৫০ শব্দে ঠিক চারটি নম্বরযুক্ত ধাপে নিরাপদ পুনরুদ্ধার পরিকল্পনা দিন। ধ্বংসাত্মক কাজের আগে মূল প্রমাণ সংরক্ষণ করুন; প্রোডাকশনে চালু করার আগে পুনরুদ্ধার যাচাই করুন। সাত ঘণ্টার ঝুঁকির ব্যাখ্যা দিন, তবে একে নিশ্চিত অপরিবর্তনীয় তথ্যহানি বলবেন না। বাংলায় উত্তর দিন। সমস্যার কারণ অনুমান করবেন না।',
 'bn_cs': 'কাল্পনিক recovery exercise: database-এর valid backup রাত ২টার। সকাল ৯টায় corruption ধরা পড়েছে। মাঝের interval-এর সব transaction একটি complete immutable journal-এ আছে। vendor repair record overwrite করতে পারে। সর্বোচ্চ ১৫০ শব্দে ঠিক চারটি numbered step-এ safe recovery plan দিন। destructive action-এর আগে original evidence preserve করুন; production cutover-এর আগে recovery verify করুন। সাত ঘণ্টার exposure explain করুন, তবে একে certain irreversible data loss বলবেন না। Bengali matrix রেখে English technical term ব্যবহার করুন। outage cause assume করবেন না।'
}
FILLER = '\nArchived routine note: a completed test of a separate demonstration service; it grants no production authorization. Historical drafts do not override the current controls below.\n'
CONTROLS = ('CURRENT CONTROLS: Owner team River; maintenance window Tuesday 22:00-23:00. '
            'Latest retention decision is 30 days, superseding an older seven-day draft. '
            'Rollback if error rate exceeds 2 percent for five consecutive minutes. '
            'Staging tests passed, but production approval remains pending. '
            'No measured latency comparison supports a speedup claim.\n')
EXTENDED_REQUEST = ('\nGive exactly six bullets covering owner/window, current retention and supersession, rollback threshold, '
                    'production readiness, what staging evidence establishes, and the latency-claim limitation. '
                    'Do not invent production approval or omit qualifications. At most 180 words.')
BENCHMARK_SOURCE_SHA256=sha256(Path(__file__))


def synthetic_long(runtime, target, capacity=False):
    # Use a substantive answer for capacity probes. Forcing 64 tokens after a
    # one-word READY answer suppresses its natural EOS and induces artificial
    # channel restarts; preserve those earlier failed runs rather than score them.
    end = EXTENDED_REQUEST
    lo, hi = 0, max(1,target//len(runtime.tokenizer.encode(FILLER,add_special_tokens=False))+2)
    while len(runtime.render(CONTROLS+FILLER*hi+end))<=target:hi*=2
    while lo < hi:
        mid = (lo+hi+1)//2
        if len(runtime.render(CONTROLS+FILLER*mid+end)) <= target:
            lo = mid
        else: hi = mid-1
    return CONTROLS+FILLER*lo+end


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', required=True)
    parser.add_argument('--revision', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--context', type=int, default=40960)
    parser.add_argument('--repeats', type=int, default=2)
    parser.add_argument('--skip-capacity', action='store_true')
    args=parser.parse_args()
    if not args.output.resolve().is_relative_to(ROOT/'.local') or args.output.exists():
        parser.error('new diagnostic output required under ignored .local/')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.touch(exist_ok=False)
    def log(row):
        append_jsonl(args.output, {'observed_at_utc':datetime.now(timezone.utc).isoformat(), **row})
    with partition_lock(ROOT/'.local', 'gpu_runtime'):
        try:
            runtime=GPURuntime(args.model,args.revision,args.context)
            log({'type':'provenance','diagnostic_version':'gpu-recovery-0.2',
                 'benchmark_script_sha256':BENCHMARK_SOURCE_SHA256, **runtime.provenance})
            frozen=[]
            for path in sorted((ROOT/'data/prompts').glob('*.csv')):
                with path.open(encoding='utf-8-sig',newline='') as source:
                    for row in csv.DictReader(source):
                        for lang in ('en','bn','bn_cs'):
                            if row.get('prompt_'+lang):
                                frozen.append((len(runtime.render(row['prompt_'+lang])),row['task_id'],lang,
                                               hashlib.sha256(row['prompt_'+lang].encode()).hexdigest()))
            frozen_hashes={row[3] for row in frozen}
            log({'type':'context_count_only','prompt_instances':len(frozen),'longest':max(frozen),
                 'minimum_input_plus_output_context':max(frozen)[0]+32768,'output_allowance':32768})
            for i in range(2):
                log({'type':'warmup','index':i,**runtime.generate('Reply only with READY.',32)})
            prompts={**DIAGNOSTICS,'extended_context':synthetic_long(runtime,8192)}
            for name,prompt in prompts.items():
                if hashlib.sha256(prompt.encode()).hexdigest() in frozen_hashes:
                    raise RuntimeError('diagnostic matched a frozen prompt; generation forbidden')
                for repeat in range(args.repeats):
                    record={'type':'diagnostic','scenario':name,'repeat':repeat,'input_text':prompt}
                    try: record.update(runtime.generate(prompt,512))
                    except Exception as exc:
                        record.update(status='runtime_error',error_type=type(exc).__name__,error=str(exc))
                        if hasattr(exc,'raw_output'):record['unscored_raw_output']=exc.raw_output
                        log(record)
                        raise
                    log(record)
                    print(json.dumps({'scenario':name,'repeat':repeat,'tokens':record['output_tokens'],
                                      'seconds':record['latency_seconds'],'peak_gpu_gib':record['peak_allocated_gpu_bytes']/1024**3}),flush=True)
            if not args.skip_capacity:
                prompt=synthetic_long(runtime,args.context-96,capacity=True)
                log({'type':'synthetic_context_capacity','input_text_sha256':hashlib.sha256(prompt.encode()).hexdigest(),
                     'note':'Long synthetic prefill plus forced 64-token decode; not a full 32768-token decode.',
                     **runtime.generate(prompt,64,force_length=True)})
            log({'type':'completed','study_generations':0})
        except Exception as exc:
            log({'type':'failed','error_type':type(exc).__name__,'error':str(exc),'study_generations':0,
                 **({'unscored_raw_output':exc.raw_output} if hasattr(exc,'raw_output') else {})})
            raise


if __name__=='__main__': main()
