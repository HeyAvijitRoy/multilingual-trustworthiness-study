"""Synthetic-only quota, cloud identity and prospective-judge regressions."""
import ast
from copy import deepcopy
from datetime import datetime,timezone
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

import audit_four_qa as qa_audit
import analyze_prelim_four as analysis
import cloud_four_adapters as adapters
import estimate_prelim_four_cost as costs
import gemini_quota as quota
import prelim_eval_157 as historical
import prelim_four as four
from prelim_four_judge import ScoringContext


class QuotaTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);self.now=1800000000.
        self.patch=patch.object(quota,'ROOT',self.root);self.patch.start();self.addCleanup(self.patch.stop)
        evidence=self.root/'account-evidence.txt';evidence.write_text('SYNTHETIC TEST EVIDENCE, NOT ACCOUNT VERIFICATION')
        self.settings={'status':'verified-account-evidence','model_id':'gemini-3.8-flash','project_alias':'synthetic-project',
          'billing_tier':'free','free_tier_eligible':True,'rpm':2,'input_tpm':100,'rpd':10,
          'day_timezone':'America/Los_Angeles','verified_at':'synthetic','verified_by':'SYNTHETIC_TEST_FIXTURE',
          'evidence_path':evidence.name,'evidence_sha256':hashlib.sha256(evidence.read_bytes()).hexdigest(),
          'ledger_directory':'.local/shared-project-quota'}
        self.path=self.root/'quota.json';self.write()

    def write(self):self.path.write_text(json.dumps(self.settings))
    def ledger(self):return quota.QuotaLedger(self.path,clock=lambda:self.now)
    def reserve(self,ledger,rid,tokens=10,protocol='synthetic-v1'):return ledger.reserve(rid,tokens,protocol,'synthetic-prompt-hash')

    def test_unverified_or_paid_tier_and_tampered_evidence_are_blocked(self):
        for change in ({'status':'unverified'},{'billing_tier':'paid'},{'free_tier_eligible':False},{'rpm':0},{'input_tpm':True},{'evidence_sha256':'wrong'}):
            saved=deepcopy(self.settings);self.settings.update(change);self.write()
            with self.subTest(change=change),self.assertRaises(RuntimeError):self.ledger()
            self.settings=saved
        self.write();self.ledger()

    def test_rolling_rpm_persists_across_resume_and_protocols(self):
        self.reserve(self.ledger(),'one');self.reserve(self.ledger(),'two',protocol='synthetic-v2')
        with self.assertRaisesRegex(quota.QuotaDeferred,'RPM'):self.reserve(self.ledger(),'three')
        self.now+=60.02;self.reserve(self.ledger(),'three')
        with self.assertRaisesRegex(RuntimeError,'already accounted'):self.reserve(self.ledger(),'three')

    def test_input_tpm_reservations_include_failures_and_actual_usage(self):
        ledger=self.ledger();self.reserve(ledger,'one',60)
        ledger.finish('one',usage={'promptTokenCount':80})
        with self.assertRaisesRegex(quota.QuotaDeferred,'TPM'):self.reserve(self.ledger(),'two',30)
        with self.assertRaisesRegex(RuntimeError,'do not truncate'):self.reserve(self.ledger(),'too-big',101)

    def test_daily_budget_defers_without_new_request_and_resumes_next_day(self):
        self.settings['rpd']=1;self.write();self.reserve(self.ledger(),'one')
        ledger=self.ledger();before=ledger.path.read_bytes()
        with self.assertRaisesRegex(quota.QuotaDeferred,'daily') as caught:self.reserve(ledger,'two')
        self.assertEqual(before,ledger.path.read_bytes());self.now=caught.exception.retry_at+.01
        self.reserve(self.ledger(),'two')

    def test_pacific_reset_observes_dst_instead_of_utc_midnight(self):
        start=datetime(2026,11,1,7,30,tzinfo=timezone.utc).timestamp() # 00:30 PDT, DST ends later.
        expected=datetime(2026,11,2,8,0,tzinfo=timezone.utc).timestamp()
        self.assertEqual(quota.next_day(start),expected)

    def test_retryinfo_and_daily_429_cooldowns_survive_restart(self):
        ledger=self.ledger();self.reserve(ledger,'one')
        ledger.finish('one',error_status=429,error_payload={'_retry_after_seconds':70,'error':{'details':[{'retryDelay':'90s'}]}})
        with self.assertRaises(quota.QuotaDeferred) as caught:self.reserve(self.ledger(),'two')
        self.assertEqual(caught.exception.retry_at,self.now+90)
        self.now+=91;self.reserve(self.ledger(),'two')
        self.ledger().finish('two',error_status=429,error_payload={'error':{'details':[{'violations':[{'quotaId':'GenerateRequestsPerDayPerProjectPerModel-FreeTier'}]}]}})
        with self.assertRaises(quota.QuotaDeferred) as caught:self.reserve(self.ledger(),'three')
        self.assertEqual(caught.exception.retry_at,quota.next_day(self.now))

    def test_torn_counter_and_backwards_clock_block_execution(self):
        ledger=self.ledger();self.reserve(ledger,'one');self.now-=1
        with self.assertRaisesRegex(RuntimeError,'clock moved backwards'):self.reserve(self.ledger(),'two')
        self.now+=2
        with ledger.path.open('a') as handle:handle.write('{"torn":')
        with self.assertRaises(RuntimeError):self.reserve(self.ledger(),'two')

    def test_runner_quota_deferral_does_not_create_attempt_or_response(self):
        cfg,manifest,freeze,anns,prompts=four.verify_candidate();cfg=deepcopy(cfg)
        cfg['models'][1]['quota_config']=str(self.path)
        self.settings['rpd']=1;self.write();ledger=self.ledger();self.reserve(ledger,'already-used')
        cells=four.cells_for(cfg,freeze,anns,prompts,'google')[:1];out=self.root/'.local/study'
        with patch.object(four,'require_frozen'),patch.object(four,'require_execution_gates'), \
             patch.dict(os.environ,{'GEMINI_API_KEY':'synthetic'}), \
             patch.object(four,'output_root',return_value=out),patch.object(four,'cells_for',return_value=cells), \
             patch.object(quota,'QuotaLedger',return_value=ledger),patch.object(adapters,'call_google') as http:
            state=four.run_partition(cfg,manifest,freeze,anns,prompts,'google')
        self.assertEqual(state['state'],'quota_deferred');http.assert_not_called()
        self.assertFalse((out/'attempts/google.jsonl').exists());self.assertFalse((out/'google.jsonl').exists())

    def run_google(self,cfg,manifest,freeze,anns,prompts,cells,out,ledger,http):
        with patch.object(four,'require_frozen'),patch.object(four,'require_execution_gates'), \
             patch.dict(os.environ,{'GEMINI_API_KEY':'synthetic'}),patch.object(four.time,'sleep'), \
             patch.object(four,'output_root',return_value=out),patch.object(four,'cells_for',return_value=cells), \
             patch.object(quota,'QuotaLedger',return_value=ledger),patch.object(adapters,'call_google',http):
            return four.run_partition(cfg,manifest,freeze,anns,prompts,'google')

    def test_successful_daily_continuation_never_replays_completed_cells(self):
        self.settings.update(input_tpm=100000,rpd=1,rpm=10);self.write();ledger=self.ledger()
        cfg,manifest,freeze,anns,prompts=four.verify_candidate();cfg=deepcopy(cfg)
        cfg['models'][1].update(quota_config=str(self.path),allowed_returned_model_ids=['synthetic-version'])
        cells=four.cells_for(cfg,freeze,anns,prompts,'google')[:2];out=self.root/'.local/study'
        result={'response_text':'SYNTHETIC বাংলা','returned_model':'synthetic-version','finish_status':'STOP','usage':{'promptTokenCount':25}}
        http=unittest.mock.Mock(return_value=result)
        state=self.run_google(cfg,manifest,freeze,anns,prompts,cells,out,ledger,http)
        self.assertEqual(state['state'],'quota_deferred');self.assertEqual(http.call_count,1)
        self.now=state['retry_at_epoch']+.01
        self.assertIsNone(self.run_google(cfg,manifest,freeze,anns,prompts,cells,out,self.ledger(),http))
        self.assertIsNone(self.run_google(cfg,manifest,freeze,anns,prompts,cells,out,self.ledger(),http))
        self.assertEqual(http.call_count,2)
        self.assertEqual(len(historical.read_jsonl_records(out/'google.jsonl')),2)
        self.assertEqual(sum(r['type']=='reserved' for r in historical.read_jsonl_records(ledger.path)),2)

    def test_429_daily_pause_preserves_failure_and_resumes_same_cell(self):
        self.settings.update(input_tpm=100000,rpd=100,rpm=10);self.write();ledger=self.ledger()
        cfg,manifest,freeze,anns,prompts=four.verify_candidate();cfg=deepcopy(cfg)
        cfg['models'][1].update(quota_config=str(self.path),allowed_returned_model_ids=['synthetic-version'])
        cells=four.cells_for(cfg,freeze,anns,prompts,'google')[:1];out=self.root/'.local/study'
        error=historical.ProviderHTTPError(429,{'error':{'details':[{'quotaId':'GenerateRequestsPerDay'}]}})
        result={'response_text':'SYNTHETIC','returned_model':'synthetic-version','finish_status':'STOP'}
        http=unittest.mock.Mock(side_effect=[error,result])
        state=self.run_google(cfg,manifest,freeze,anns,prompts,cells,out,ledger,http)
        self.assertEqual(http.call_count,1);self.assertEqual(state['reason'],'provider rate-limit cooldown')
        self.now=state['retry_at_epoch']+.01
        self.run_google(cfg,manifest,freeze,anns,prompts,cells,out,self.ledger(),http)
        self.assertEqual(http.call_count,2)
        self.assertEqual([r['status'] for r in historical.read_jsonl_records(out/'google.jsonl')],['api_error','success'])
        starts=[r for r in historical.read_jsonl_records(out/'attempts/google.jsonl') if r['status']=='started']
        self.assertEqual([r['attempt'] for r in starts],[1,2])


class AdapterAndJudgeTests(unittest.TestCase):
    def model(self):return four.read(four.CONFIG)['models'][1]

    def payload(self,finish='STOP'):
        return {'modelVersion':'gemini-3.8-flash-stable-test','responseId':'synthetic',
                'candidates':[{'finishReason':finish,'content':{'parts':[{'thought':True,'text':'PRIVATE'}, {'text':'বাংলা visible'}]}}],
                'usageMetadata':{'promptTokenCount':25,'candidatesTokenCount':10,'thoughtsTokenCount':4,'totalTokenCount':39}}

    def test_sol_generation_uses_exact_model_and_existing_responses_controls(self):
        model=four.read(four.CONFIG)['models'][0]
        payload={'status':'completed','model':'gpt-6.1-sol','output_text':'SYNTHETIC','id':'test'}
        with patch.dict(os.environ,{'OPENAI_API_KEY':'synthetic'}),patch.object(historical,'http_json',return_value=(payload,200)) as http:
            result=historical.call_openai(model,'unchanged prompt','unchanged system',900,32768)
        body=http.call_args.args[2]
        self.assertEqual(body,{'model':'gpt-6.1-sol','instructions':'unchanged system','input':'unchanged prompt',
                               'reasoning':{'effort':'medium','mode':'standard'},'max_output_tokens':32768})
        self.assertEqual(result['provider_raw_response'],payload)

    def test_quota_deferred_cell_is_pending_until_scored_or_retry_budget_exhausted(self):
        ctx=ScoringContext();google=ctx.config['models'][1]['model_id'];key=(google,'T','bn',1)
        with tempfile.TemporaryDirectory() as folder:
            ctx.root=Path(folder)
            historical.append_jsonl(ctx.root/'quota_deferrals.jsonl',{'task_id':'T','language':'bn'})
            self.assertEqual(analysis.pending_quota_cells(ctx,set()),[key])
            self.assertEqual(analysis.pending_quota_cells(ctx,{key}),[])
            for attempt in range(4):
                historical.append_jsonl(ctx.root/'attempts/google.jsonl',{'task_id':'T','language':'bn','run_index':1,'status':'started'})
            self.assertEqual(analysis.pending_quota_cells(ctx,set()),[])

    def test_final_judge_freeze_requires_original_calibration_input_hashes(self):
        ctx=ScoringContext();ctx.manifest=deepcopy(ctx.manifest)
        ctx.manifest['artifact_sha256']={str(path.relative_to(four.ROOT)):four.digest(path) for path in
             (ctx.judge_path,Path('scripts/prelim_four_judge.py').resolve(),Path('scripts/prelim_judge_157.py').resolve())}
        with patch.object(four,'require_frozen'):
            with self.assertRaisesRegex(RuntimeError,'original calibration inputs'):ctx.frozen()
            ctx.manifest['artifact_sha256'].update(ctx.calibration_input_pins())
            ctx.frozen()

    def test_google_wire_preserves_medium_full_allowance_and_visible_extraction(self):
        with patch.dict(os.environ,{'GEMINI_API_KEY':'synthetic'}),patch.object(adapters,'http_json',return_value=(self.payload(),200)) as http:
            result=adapters.call_google(self.model(),'unchanged prompt','unchanged system',900,32768)
        body=http.call_args.args[2]
        self.assertEqual(body['contents'][0]['parts'][0]['text'],'unchanged prompt')
        self.assertEqual(body['generationConfig'],{'maxOutputTokens':32768,'thinkingConfig':{'thinkingLevel':'medium'}})
        self.assertEqual(result['response_text'],'বাংলা visible');self.assertIn('PRIVATE',json.dumps(result['provider_raw_response']))
        self.assertEqual(result['usage']['thoughtsTokenCount'],4)

    def test_truncation_safety_empty_and_malformed_payloads_remain_distinct(self):
        payloads=[(self.payload('MAX_TOKENS'),'MAX_TOKENS'),
                  ({'modelVersion':'test','candidates':[],'promptFeedback':{'blockReason':'SAFETY'}},'SAFETY')]
        with patch.dict(os.environ,{'GEMINI_API_KEY':'synthetic'}):
            for payload,finish in payloads:
                with patch.object(adapters,'http_json',return_value=(payload,200)):
                    self.assertEqual(adapters.call_google(self.model(),'p','s',900,32768)['finish_status'],finish)
            for payload in ({},{'error':{'message':'failed'}},self.payload('CONTINUATION'),[],
                            {'candidates':None},{'candidates':[None]},
                            {'candidates':[{'finishReason':'STOP','content':{'parts':[None]}}]}):
                with patch.object(adapters,'http_json',return_value=(payload,200)),self.assertRaises(historical.ProviderHTTPError) as caught:
                    adapters.call_google(self.model(),'p','s',900,32768)
                self.assertIn('provider_raw_response',caught.exception.payload)

    def test_version_allowlist_rejects_missing_and_changed_returned_model(self):
        model=self.model();model['allowed_returned_model_ids']=['exact-test-id']
        adapters.validate_identity(model,{'returned_model':'exact-test-id'})
        for actual in (None,'other-version'):
            with self.assertRaises(historical.ProviderHTTPError):adapters.validate_identity(model,{'returned_model':actual})

    def test_http_retry_after_is_preserved_without_real_network(self):
        error=urllib.error.HTTPError('https://example.invalid',429,'limited',{'Retry-After':'75'},io.BytesIO(b'{"error":{"code":429}}'))
        with patch.object(adapters.urllib.request,'urlopen',side_effect=error),self.assertRaises(historical.ProviderHTTPError) as caught:
            adapters.http_json('https://example.invalid',{}, {},900)
        self.assertEqual(caught.exception.payload['_retry_after_seconds'],75)

    def test_new_panel_and_prior_candidate_are_isolated_and_no_local_change(self):
        cfg,manifest,*_=four.verify_candidate();self.assertEqual(cfg['models'][0]['model_id'],'gpt-6.1-sol')
        self.assertEqual(cfg['models'][1]['model_id'],'gemini-3.8-flash')
        old=four.ROOT/'data/evaluation/amendments/prelim-157-four-model-0.2'
        prior,*_=four.verify_candidate(old/'MODELS.json',old/'FREEZE_CANDIDATE.json')
        self.assertEqual(cfg['models'][2:],prior['models'][2:]);self.assertNotEqual(four.output_root(cfg),four.output_root(prior))
        self.assertEqual(ScoringContext(old/'MODELS.json',old/'FREEZE_CANDIDATE.json').judge['model_id'],'gpt-6.1-sol')
        before=subprocess.check_output(['git','show','b361477:scripts/prelim_four.py'],text=True)
        def selected(source):
            return {n.name:ast.dump(n,include_attributes=False) for n in ast.parse(source).body
                    if isinstance(n,ast.FunctionDef) and n.name in ('local_chat','local_http_json','partition_lock')}
        self.assertEqual(selected(before),selected(Path(four.__file__).read_text()))

    def test_primary_judge_self_evaluation_and_returned_identity_are_blocked(self):
        original=four.read
        def wrong(path):
            value=original(path)
            if Path(path).name=='JUDGE.json':value['model_id']='gpt-6.1-sol'
            return value
        with patch.object(four,'read',side_effect=wrong),self.assertRaisesRegex(RuntimeError,'self-evaluation'):
            ScoringContext()
        with tempfile.TemporaryDirectory() as folder,patch.dict(os.environ,{'OPENAI_API_KEY':'synthetic'}):
            ctx=ScoringContext();ctx.root=Path(folder)
            with patch('prelim_judge_157.http_judge',return_value={'ratings':[],'_judge_meta':{'returned_model':'gpt-6.1-sol'}}) as http:
                with self.assertRaisesRegex(RuntimeError,'returned judge identity'):ctx.call('synthetic','test')
                with self.assertRaisesRegex(RuntimeError,'ambiguous/invalid'):ctx.call('synthetic','test')
                self.assertEqual(http.call_count,1)

    def test_revised_costs_keep_prior_scenarios_and_condition_free_google(self):
        prior=four.read(four.ROOT/'data/evaluation/amendments/prelim-157-four-model-0.2/COST_SCENARIOS.json')
        self.assertEqual(costs.estimate_v02(),prior)
        report=costs.estimate();self.assertEqual(report,four.read(four.AMENDMENT/'COST_SCENARIOS.json'))
        self.assertEqual(report['primary_judge'],'gpt-5.4-2026-03-05')
        self.assertEqual((report['openai_generation_calls'],report['local_generation_calls'],report['scoring_calls']),(471,942,1884))
        self.assertFalse(report['standard_prices_per_million_tokens']['gemini-3.8-flash']['paid_fallback_authorized'])
        for scenario in report['scenarios']:
            self.assertEqual(scenario['google_generation_usd_if_actual_free_tier'],0)
            self.assertAlmostEqual(scenario['total_paid_one_attempt_usd_if_google_free'],
                sum(scenario[k] for k in ('openai_generation_usd','judge_calibration_30_usd','judge_scoring_1884_usd','openai_three_synthetic_smokes_usd')),places=1)

    def test_qa_first_pass_hides_ai_labels_and_audits_critical_disagreement(self):
        ctx=ScoringContext();task,rec=next(iter(ctx.annotations.items()));model=ctx.config['models'][0]['model_id']
        critical=next(u['id'] for u in rec['rius'] if u['criticality']=='critical')
        ratings=[{'item_id':u['id'],'score':0 if u['id']==critical else 1,
                  'reason':'omitted' if u['id']==critical else 'met'} for u in rec['rius']]
        ratings.extend({'item_id':c['id'],'score':1,'reason':'pass'} for c in rec['task_checks'])
        source={'task_id':task,'language':'en','provider':'openai','requested_model':model,'run_index':1,
                'response_text':'SYNTHETIC TEST DATA','status':'success','finish_status':'completed'}
        score={**source,'ratings':ratings}
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);packet=root/'packet'
            with patch.object(ctx,'generations',return_value={(task,'en'):source}),patch.object(ctx,'scores',return_value={(task,'en'):score}):
                ctx.qa(['openai'],packet)
            row=historical.read_jsonl_records(packet/'qa_packet.jsonl')[0]
            self.assertNotIn('automated_ratings',row);self.assertNotIn('requested_model',row)
            manifest=four.read(packet/'qa_manifest_private.json');cell=manifest['cells'][0]
            human={'qa_id':row['qa_id'],'reviewer_id':'SYNTHETIC_TEST_FIXTURE','reviewed_at':'synthetic',
                   'independent_before_unblinding':True,'packet_sha256':manifest['packet_sha256'],
                   'response_sha256':cell['response_sha256'],'ratings':deepcopy(ratings)}
            rating=next(r for r in human['ratings'] if r['item_id']==critical);rating.update(score=1,reason='met')
            path=root/'human.jsonl';path.write_text(json.dumps(human)+'\n')
            with patch.object(ctx,'scores',return_value={(task,'en'):score}):audit=qa_audit.audit(ctx,packet,path)
            self.assertEqual(audit['reviewed_cells'],1);self.assertEqual(len(audit['critical_safety_disagreements']),1)
            self.assertFalse(audit['independent_human_authenticity_certified'])
            human['independent_before_unblinding']=False;path.write_text(json.dumps(human)+'\n')
            with self.assertRaisesRegex(RuntimeError,'first-pass human evidence'):qa_audit.audit(ctx,packet,path)


if __name__=='__main__':unittest.main()
