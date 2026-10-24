"""Versioned cloud wire adapters; historical cloud clients retain their defaults."""
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import json
import os
import urllib.error
import urllib.request

import prelim_eval_157 as historical


def http_json(url,headers,body,timeout):
    request=urllib.request.Request(url,data=json.dumps(body,ensure_ascii=False).encode(),headers=headers,method='POST')
    try:
        with urllib.request.urlopen(request,timeout=timeout) as response:
            raw=response.read().decode('utf-8',errors='replace');status=response.status
    except urllib.error.HTTPError as exc:
        raw=exc.read().decode('utf-8',errors='replace')
        try:payload=json.loads(raw)
        except json.JSONDecodeError:payload={'error_text':raw}
        retry=exc.headers.get('Retry-After') if exc.headers else None
        if retry:
            try:delay=max(0,float(retry))
            except ValueError:
                try:delay=max(0,(parsedate_to_datetime(retry)-datetime.now(timezone.utc)).total_seconds())
                except (TypeError,ValueError):delay=0
            payload['_retry_after_seconds']=delay
        raise historical.ProviderHTTPError(exc.code,payload) from exc
    try:return json.loads(raw),status
    except json.JSONDecodeError as exc:
        raise historical.ProviderHTTPError(status,{'unparsed_raw_response':raw}) from exc


def call_google(model,prompt,system,timeout,max_tokens):
    reasoning=model['reasoning']
    if set(reasoning)=={'thinking_level'}:thinking={'thinkingLevel':reasoning['thinking_level']}
    elif set(reasoning)=={'thinking_budget'}:thinking={'thinkingBudget':reasoning['thinking_budget']}
    else:raise RuntimeError('exactly one supported Gemini thinking control required')
    body={'systemInstruction':{'parts':[{'text':system}]},
          'contents':[{'role':'user','parts':[{'text':prompt}]}],
          'generationConfig':{'maxOutputTokens':max_tokens,'thinkingConfig':thinking}}
    payload,status=http_json('https://generativelanguage.googleapis.com/v1beta/models/'+model['model_id']+':generateContent',
                             {'x-goog-api-key':os.environ[model['env_key']],'Content-Type':'application/json'},body,timeout)
    def invalid(message):
        raise historical.ProviderHTTPError(status,{'validation_error':message,'provider_raw_response':payload})
    if not isinstance(payload,dict):invalid('response must be a JSON object')
    candidates=payload.get('candidates',[])
    if not isinstance(candidates,list):invalid('candidate list is malformed')
    if payload.get('error') or len(candidates)>1:invalid('failed or multi-candidate response')
    first=candidates[0] if candidates else {}
    if not isinstance(first,dict):invalid('candidate is malformed')
    feedback=payload.get('promptFeedback') or {}
    if not isinstance(feedback,dict):invalid('prompt feedback is malformed')
    blocked=feedback.get('blockReason')
    finish=first.get('finishReason') or ('SAFETY' if blocked else None)
    if not isinstance(finish,str) or finish not in {'STOP','MAX_TOKENS','SAFETY','RECITATION','LANGUAGE','OTHER','BLOCKLIST','PROHIBITED_CONTENT','SPII'}:
        invalid('missing/unsupported finish reason; no continuation or tool-call recovery permitted')
    content=first.get('content') or {}
    if not isinstance(content,dict):invalid('content is malformed')
    parts=content.get('parts') or []
    if not isinstance(parts,list) or any(not isinstance(p,dict) for p in parts):invalid('content parts are malformed')
    if any('text' in p and not isinstance(p['text'],str) for p in parts):invalid('text part is malformed')
    if payload.get('usageMetadata') is not None and not isinstance(payload['usageMetadata'],dict):invalid('usage metadata is malformed')
    visible=''.join(p['text'] for p in parts if isinstance(p.get('text'),str) and not p.get('thought',False))
    return {'http_status':status,'provider_raw_response':payload,'response_text':visible,
            'provider_response_id':payload.get('responseId'),'returned_model':payload.get('modelVersion'),
            'finish_status':finish,'usage':payload.get('usageMetadata'),
            'provider_raw_meta':{'finish_message':first.get('finishMessage'),'prompt_feedback':payload.get('promptFeedback'),
                                 'safety_ratings':first.get('safetyRatings'),'continuation_available':False}}


def validate_identity(model,result):
    allowed=model.get('allowed_returned_model_ids')
    if not allowed or result.get('returned_model') not in allowed:
        raise historical.ProviderHTTPError(result.get('http_status',200),
             {'validation_error':'returned model/version is missing or differs from frozen allowlist',
              'provider_raw_response':result.get('provider_raw_response',result)})
