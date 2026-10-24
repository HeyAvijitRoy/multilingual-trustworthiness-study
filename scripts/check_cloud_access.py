#!/usr/bin/env python3
"""Read-only public model metadata using configured accounts; never generate.

List/Get model access does not establish free-tier billing, quotas, wire
compatibility, model quality or authorization for paid inference.
"""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import urllib.error
import urllib.request

from research_approvals import load_api_environment

OPENAI_MODELS=('gpt-6.1-sol','gpt-5.4-2026-03-05','gpt-5.4-mini-2026-03-17','gpt-6-astra')


def get(url,headers):
    req=urllib.request.Request(url,headers=headers)
    try:
        with urllib.request.urlopen(req,timeout=60) as response:return response.status,json.load(response)
    except urllib.error.HTTPError as exc:
        # Provider error bodies can include account identifiers; do not publish.
        return exc.code,{}


def inspect():
    result={'observed_at_utc':datetime.now(timezone.utc).isoformat(),
            'method':'GET model metadata only; no generation or countTokens calls',
            'paid_inference_calls':0,'openai':[],'google':[],
            'account_billing_tier_verified':False,'account_quotas_verified':False}
    if os.environ.get('OPENAI_API_KEY'):
        for model in OPENAI_MODELS:
            status,data=get('https://api.openai.com/v1/models/'+model,
                            {'Authorization':'Bearer '+os.environ['OPENAI_API_KEY']})
            result['openai'].append({'requested_model':model,'http_status':status,'returned_id':data.get('id')})
    if os.environ.get('GEMINI_API_KEY'):
        token=None
        while True:
            url='https://generativelanguage.googleapis.com/v1beta/models?pageSize=1000'
            if token:
                from urllib.parse import quote
                url+='&pageToken='+quote(token,safe='')
            status,data=get(url,{'x-goog-api-key':os.environ['GEMINI_API_KEY']})
            result['google_list_http_status']=status
            for model in data.get('models',[]):
                name=model.get('name','')
                if name.startswith('models/gemini-') and 'generateContent' in model.get('supportedGenerationMethods',[]):
                    result['google'].append({k:model[k] for k in ('name','version','inputTokenLimit','outputTokenLimit','supportedGenerationMethods') if k in model})
            token=data.get('nextPageToken')
            if status!=200 or not token:break
    return result


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--env-file',type=Path)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    load_api_environment(args.env_file);report=inspect()
    with args.out.open('x',encoding='utf-8') as handle:json.dump(report,handle,indent=2);handle.write('\n')
    print(json.dumps(report,indent=2))
