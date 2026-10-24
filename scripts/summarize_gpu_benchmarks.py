#!/usr/bin/env python3
"""Export small numeric summaries; raw synthetic text/token IDs stay ignored."""
import argparse
import json
from pathlib import Path
import statistics

from local_gpu_runtime import ROOT,sha256
from prelim_eval_157 import read_jsonl_records


METRICS=('input_tokens','output_tokens','latency_seconds','time_to_first_token_seconds',
         'effective_prefill_tokens_per_second','decode_tokens_per_second',
         'peak_allocated_gpu_bytes','peak_reserved_gpu_bytes','system_rss_high_water_bytes')


def numeric(row):
    result={k:row[k] for k in METRICS}
    samples=row.get('gpu_samples',[])
    result['gpu_utilization_mean_percent']=statistics.mean(s['utilization_percent'] for s in samples) if samples else None
    result['gpu_utilization_peak_percent']=max((s['utilization_percent'] for s in samples),default=None)
    result['nvidia_smi_peak_memory_used_mib']=max((s['memory_used_mib'] for s in samples),default=None)
    result.update({k:row[k] for k in ('finish_reason','truncated','ended_on_eos','max_new_tokens')})
    return result


def summarize(path):
    records=read_jsonl_records(path)
    if records[-1].get('type')!='completed':raise RuntimeError('incomplete/failed benchmark: '+str(path))
    provenance=records[0]
    if provenance['runtime_script_sha256']!=sha256(ROOT/'scripts/local_gpu_runtime.py'):
        raise RuntimeError('runtime differs from final benchmark')
    if provenance['benchmark_script_sha256']!=sha256(ROOT/'scripts/benchmark_gpu.py'):
        raise RuntimeError('benchmark source differs from final run')
    if sum(r['type']=='warmup' for r in records)!=2:raise RuntimeError('two warmups required')
    scenarios={}
    for name in ('en','bn','bn_cs','extended_context'):
        rows=[r for r in records if r['type']=='diagnostic' and r['scenario']==name]
        if len(rows)!=2 or any(r.get('status')=='runtime_error' for r in rows):raise RuntimeError('two successful repeats required')
        scenarios[name]={'repeats':[numeric(r) for r in rows],
                         'median_decode_tokens_per_second':statistics.median(r['decode_tokens_per_second'] for r in rows),
                         'median_latency_seconds':statistics.median(r['latency_seconds'] for r in rows),
                         'identical_token_ids_across_repeats':rows[0]['output_token_ids']==rows[1]['output_token_ids']}
    capacity=next(r for r in records if r['type']=='synthetic_context_capacity')
    short=[r for r in records if r['type']=='diagnostic' and r['scenario']!='extended_context']
    rate=statistics.median(r['decode_tokens_per_second'] for r in short)
    return {'source_local_path':path.relative_to(ROOT).as_posix(),'source_sha256':sha256(path),
            'provenance':provenance,'context_count_only':next(r for r in records if r['type']=='context_count_only'),
            'scenarios':scenarios,'capacity':numeric(capacity),
            'capacity_note':capacity['note'],'short_median_decode_tokens_per_second':rate,
            'decode_only_projection_hours_for_471_responses':{str(n):471*n/rate/3600 for n in (512,2048,32768)},
            'projection_caveat':'Not measured study runtime; excludes prefill, startup, I/O, retries and long-context decode slowdown.',
            'study_generations':0}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--qwen',type=Path,required=True);p.add_argument('--gemma',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    result={'diagnostic_only':True,'independent_human_evaluation':False,
            'models':[summarize(args.qwen.resolve()),summarize(args.gemma.resolve())]}
    with args.out.open('x',encoding='utf-8') as handle:json.dump(result,handle,indent=2,ensure_ascii=False,allow_nan=False);handle.write('\n')
    print(json.dumps({'models':2,'output':str(args.out),'study_generations':0}))


if __name__=='__main__':main()
