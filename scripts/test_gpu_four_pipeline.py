"""Synthetic/no-paid regression coverage for GPU routing and amended scoring."""
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import urllib.error

import analyze_prelim_four as analysis
import cloud_smoke_four as cloud
import local_gpu_runtime as runtime
import local_gpu_server as server
import prelim_eval_157 as generation
import prelim_four as four
from prelim_four_judge import ScoringContext
import prelim_judge_157 as judge
import research_approvals as approvals


class GPURoutingTests(unittest.TestCase):
    def test_upstream_hashes_override_cache_blob_filename_assumptions(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);snapshot=root/'snapshot';snapshot.mkdir()
            files={'config.json':'{}','chat_template.jinja':'template','tokenizer_config.json':'{}','tokenizer.json':'{}'}
            for name,data in files.items():(snapshot/name).write_text(data)
            blob=root/('f'*64);blob.write_bytes(b'synthetic weights');(snapshot/'model.safetensors').symlink_to(blob)
            candidate={'model_id':'M','cached_revision':'a'*40,'cached_weight_file_bytes':len(b'synthetic weights')}
            for name,field in [('config.json','config_sha256'),('chat_template.jinja','template_sha256'),
                               ('tokenizer_config.json','tokenizer_config_sha256'),('tokenizer.json','tokenizer_json_sha256')]:
                candidate[field]=runtime.sha256(snapshot/name)
            ann=root/'data/evaluation/amendments/prelim-157-four-model-0.2';(ann/'gpu').mkdir(parents=True)
            (ann/'CANDIDATE_CACHE_METADATA.json').write_text(json.dumps({'candidates':[candidate]}))
            upstream=[]
            for path in snapshot.iterdir():
                data=path.read_bytes()
                upstream.append({'name':path.name,'size':len(data),
                                 'lfs':{'sha256':hashlib.sha256(data).hexdigest()} if path.name.endswith('.safetensors') else None,
                                 'blob_id':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()})
            (ann/'gpu/UPSTREAM_ARTIFACTS.json').write_text(json.dumps({'models':[{'model_id':'M','returned_revision':'a'*40,'files':upstream}]}))
            with patch.object(runtime,'ROOT',root),patch.object(runtime,'snapshot_path',return_value=snapshot):
                _,proof=runtime.verify_artifacts('M','a'*40)
                self.assertTrue(proof['upstream_integrity_checked']['model.safetensors'])
                self.assertNotEqual(blob.name,proof['artifact_sha256']['model.safetensors'])
                blob.write_bytes(b'corrupted weights')
                with self.assertRaisesRegex(RuntimeError,'integrity mismatch'):runtime.verify_artifacts('M','a'*40)

    def body(self):
        body={'model':'M','messages':[{'role':'system','content':runtime.SYSTEM},{'role':'user','content':'synthetic'}],
              'max_tokens':32768,'temperature':0,'stream':False}
        body['request_id']=runtime.canonical_request_id(body)
        return body

    def test_request_identity_ignores_key_order_and_tracks_content(self):
        body=self.body()
        self.assertEqual(runtime.canonical_request_id(body),runtime.canonical_request_id(dict(reversed(list(body.items())))))
        changed=deepcopy(body);changed['messages'][1]['content']='different'
        self.assertNotEqual(runtime.canonical_request_id(body),runtime.canonical_request_id(changed))

    def test_stateless_routing_and_full_output_allowance_enforced(self):
        body=self.body();self.assertEqual(server.validate_request(body,'M',False),('synthetic',32768))
        for change in [{'model':'other'},{'max_tokens':512},{'temperature':1},{'stream':True},
                       {'chat_template_kwargs':{'enable_thinking':True}},{'request_id':'wrong'}]:
            changed={**body,**change}
            with self.subTest(change=change),self.assertRaises(ValueError): server.validate_request(changed,'M',False)
        body['messages'].append({'role':'assistant','content':'prior'})
        with self.assertRaises(ValueError):server.validate_request(body,'M',True)

    def test_reasoning_output_is_preserved_but_not_scored_as_visible(self):
        tokenizer=SimpleNamespace(decode=lambda ids,skip_special_tokens: '<think>private</think>answer')
        with self.assertRaises(runtime.VisibleExtractionError) as caught:runtime.extract_visible(tokenizer,[1,2])
        self.assertEqual(caught.exception.raw_output['output_token_ids'],[1,2])
        self.assertIn('private',caught.exception.raw_output['response_raw_text'])

    def test_candidate_blocks_scoring_and_calibration_before_http(self):
        ctx=ScoringContext()
        with patch.object(judge,'http_judge') as http:
            for action in [ctx.calibrate,lambda:ctx.score('openai')]:
                with self.assertRaisesRegex(RuntimeError,'study generation blocked'):action()
            http.assert_not_called()
        with tempfile.TemporaryDirectory() as folder,patch.dict(generation.CALLERS,{'openai':unittest.mock.Mock()}) as _:
            with self.assertRaisesRegex(RuntimeError,'spending approval is not recorded'):
                cloud.smoke(four.CONFIG,four.MANIFEST,Path(folder)/'raw')
            generation.CALLERS['openai'].assert_not_called()

    def test_server_cache_cannot_cross_mode_or_protocol(self):
        provenance={'model_id':'M','diagnostic_only':True,'manifest_sha256':'a','config_sha256':'b'}
        records=[{'type':'server_provenance',**provenance}]
        server.validate_log_provenance(records,provenance)
        for changed in [{'diagnostic_only':False},{'manifest_sha256':'c'},{'config_sha256':'c'}]:
            with self.assertRaisesRegex(RuntimeError,'different runtime, mode or protocol'):
                server.validate_log_provenance(records,{**provenance,**changed})
        with self.assertRaisesRegex(RuntimeError,'lacks runtime provenance'):
            server.validate_log_provenance([{'type':'response_received'}],provenance)

    def test_resume_rejects_unknown_outcome_and_cross_cell_attempt(self):
        cfg,manifest,freeze,annotations,prompts=four.verify_candidate();pins=four.provenance()
        cells=four.cells_for(cfg,freeze,annotations,prompts,'openai')[:2]
        started={**cells[0],**pins,'protocol_id':cfg['protocol_id'],'requested_model':cfg['models'][0]['model_id'],
                 'status':'started','attempt_id':'synthetic'}
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'attempts.jsonl'
            for end,message in [({**started,'status':'invented'},'unknown attempt'),
                                ({**started,**cells[1],'status':'transport_error'},'different cell')]:
                path.write_text(json.dumps(started)+'\n'+json.dumps(end)+'\n')
                with self.assertRaisesRegex(RuntimeError,message):
                    four.validate_attempt_history(path,cfg,'openai',cells,pins,{})

    def test_generation_retry_budget_is_not_reset_by_resume(self):
        cfg,manifest,freeze,annotations,prompts=four.verify_candidate()
        cell=four.cells_for(cfg,freeze,annotations,prompts,'openai')[0]
        with tempfile.TemporaryDirectory() as folder,patch.dict(os.environ,{'OPENAI_API_KEY':'synthetic'}):
            with patch.object(four,'require_frozen'),patch.object(four,'require_execution_gates'), \
                 patch.object(four,'output_root',return_value=Path(folder)),patch.object(four,'cells_for',return_value=[cell]), \
                 patch.object(four.time,'sleep'),patch.dict(generation.CALLERS,{'openai':unittest.mock.Mock(side_effect=urllib.error.URLError('synthetic'))}):
                for _ in range(2):four.run_partition(cfg,manifest,freeze,annotations,prompts,'openai')
                self.assertEqual(generation.CALLERS['openai'].call_count,4)


class ApprovalTests(unittest.TestCase):
    def test_local_credentials_are_not_shell_evaluated_or_overwritten(self):
        with tempfile.TemporaryDirectory() as folder,patch.dict(os.environ,{'OPENAI_API_KEY':'existing'},clear=True):
            path=Path(folder)/'.env'
            path.write_text('OPENAI_API_KEY=replacement\nGEMINI_API_KEY="literal$(never_execute)"\nUNKNOWN_KEY=ignored\n')
            approvals.load_api_environment(path)
            self.assertEqual(os.environ['OPENAI_API_KEY'],'existing')
            self.assertEqual(os.environ['GEMINI_API_KEY'],'literal$(never_execute)')
            self.assertNotIn('UNKNOWN_KEY',os.environ)

    def test_spending_approval_requires_explicit_pinned_scope(self):
        with tempfile.TemporaryDirectory() as folder,patch.object(approvals,'ROOT',Path(folder)):
            cfg={'protocol_id':'test-only'}
            with self.assertRaisesRegex(RuntimeError,'not recorded'):approvals.require_spending_approval(cfg,{},'generation')
            record={'protocol_id':'test-only','status':'approved','approved_by':'SYNTHETIC_TEST_FIXTURE',
                    'approved_at':'synthetic','purposes':['generation'],'currency':'USD','maximum_usd':1}
            path=Path(folder)/'approval.json';path.write_text(json.dumps(record))
            manifest={'spending_approval_record':'approval.json','artifact_sha256':{'approval.json':four.digest(path)}}
            self.assertEqual(approvals.require_spending_approval(cfg,manifest,'generation')['maximum_usd'],1)
            with self.assertRaisesRegex(RuntimeError,'does not cover'):
                approvals.require_spending_approval(cfg,manifest,'study_scoring')
            path.write_text('{}')
            with self.assertRaisesRegex(RuntimeError,'immutable manifest'):
                approvals.require_spending_approval(cfg,manifest,'generation')


class FourJudgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx=ScoringContext()

    def keyed_fixture_rows(self):
        contexts={c['fixture_id']:c for c in judge.load_fixture_context(self.ctx.annotations,self.ctx.prompts)}
        return [{'fixture_id':r['fixture_id'],'task_id':contexts[r['fixture_id']]['task_id'],
                 'language':contexts[r['fixture_id']]['language'],'item_id':r['item_id'],
                 'score':r['intended_score'],'reason':r['intended_reason']}
                for r in judge.read_csv(judge.ANSWER_KEY)]

    def test_frozen_calibration_thresholds_and_safety_disagreement(self):
        # Oracle-key labels are synthetic test inputs, never a measured judge gate.
        rows=self.keyed_fixture_rows();report=self.ctx.evaluate_gate(rows)
        self.assertTrue(report['gate_pass']);self.assertEqual(report['item_count'],229)
        safety=deepcopy(rows)
        specs={c['fixture_id']:c for c in judge.load_fixture_context(self.ctx.annotations,self.ctx.prompts)}
        target=next(r for r in safety if r['item_id'].startswith('CHECK') and specs[r['fixture_id']]['rec']['safety_relevance']!='none')
        target['score']=str(1-float(target['score']))
        self.assertFalse(self.ctx.evaluate_gate(safety)['gate_pass'])
        for bad in [rows[:-1],rows+[rows[0]]]:
            with self.assertRaisesRegex(RuntimeError,'229 unique'):self.ctx.evaluate_gate(bad)

    def test_judge_receipt_recovered_without_duplicate_request_or_identity_leak(self):
        with tempfile.TemporaryDirectory() as folder,patch.dict(os.environ,{'OPENAI_API_KEY':'synthetic'}):
            ctx=ScoringContext();ctx.root=Path(folder)
            response={'ratings':[],'_judge_meta':{'response_id':'synthetic','returned_model':ctx.judge['model_id']}}
            with patch.object(judge,'http_judge',return_value=response) as http:
                a=ctx.call('identical blinded input','study:local_a:T:en:1')
                b=ctx.call('identical blinded input','study:local_a:T:en:1')
                ctx.call('identical blinded input','study:local_b:T:en:1')
                self.assertEqual(a,b);self.assertEqual(http.call_count,2)
                self.assertEqual(http.call_args.args[0],'identical blinded input')

    def test_interrupted_judge_call_blocks_replay(self):
        with tempfile.TemporaryDirectory() as folder,patch.dict(os.environ,{'OPENAI_API_KEY':'synthetic'}):
            ctx=ScoringContext();ctx.root=Path(folder)
            with patch.object(judge,'http_judge',side_effect=KeyboardInterrupt) as http:
                with self.assertRaises(KeyboardInterrupt):ctx.call('input','fixture:F01')
                with self.assertRaisesRegex(RuntimeError,'ambiguous'):ctx.call('input','fixture:F01')
                self.assertEqual(http.call_count,1)

    def test_documented_transport_failure_can_retry_same_judge(self):
        with tempfile.TemporaryDirectory() as folder,patch.dict(os.environ,{'OPENAI_API_KEY':'synthetic'}):
            ctx=ScoringContext();ctx.root=Path(folder)
            response={'ratings':[],'_judge_meta':{'returned_model':ctx.judge['model_id']}}
            with patch.object(judge,'http_judge',side_effect=[urllib.error.URLError('synthetic'),response]) as http, \
                 patch('prelim_four_judge.time.sleep'):
                self.assertEqual(ctx.call('input','fixture:F01'),response)
                self.assertEqual(http.call_count,2)

    def test_judge_retry_budget_is_not_reset_by_resume(self):
        with tempfile.TemporaryDirectory() as folder,patch.dict(os.environ,{'OPENAI_API_KEY':'synthetic'}):
            ctx=ScoringContext();ctx.root=Path(folder)
            with patch.object(judge,'http_judge',side_effect=urllib.error.URLError('synthetic')) as http, \
                 patch('prelim_four_judge.time.sleep'):
                with self.assertRaises(urllib.error.URLError):ctx.call('input','fixture:F01')
                with self.assertRaisesRegex(RuntimeError,'four-attempt judge budget'):ctx.call('input','fixture:F01')
                self.assertEqual(http.call_count,4)


class FourAnalysisTests(unittest.TestCase):
    def test_adjudications_require_source_review_evidence_and_revision_chain(self):
        ctx=ScoringContext();task,rec=next(iter(ctx.annotations.items()));key=('SYNTHETIC',task,'en',1)
        ratings=[{'item_id':u['id'],'score':1,'reason':'met'} for u in rec['rius']]
        ratings.extend({'item_id':c['id'],'score':1,'reason':'pass'} for c in rec['task_checks'])
        source={'requested_model':'SYNTHETIC','task_id':task,'language':'en','run_index':1,
                'response_sha256':'synthetic-response-hash','ratings':ratings}
        with tempfile.TemporaryDirectory() as folder,patch.object(four,'ROOT',Path(folder)):
            root=Path(folder);review=root/'review.md';review.write_text('SYNTHETIC TEST EVIDENCE, NOT HUMAN REVIEW')
            row={**source,'status':'resolved','reviewer_id':'SYNTHETIC_TEST_FIXTURE','reviewed_at':'synthetic',
                 'raw_score_record_sha256':judge.canonical_record_sha256(source),
                 'review_log':'review.md','review_log_sha256':four.digest(review)}
            path=root/'adjudications.jsonl';path.write_text(json.dumps(row)+'\n')
            resolved,status=analysis.apply_adjudications(path,{key:source},ctx.annotations)
            self.assertEqual(status['resolved_cells'],1)
            self.assertFalse(status['independent_human_authenticity_certified'])
            generation.append_jsonl(path,row)
            with self.assertRaisesRegex(RuntimeError,'revision chain'):analysis.apply_adjudications(path,{key:source},ctx.annotations)
            row['supersedes_adjudication_sha256']=judge.canonical_record_sha256(row)
            path.write_text(json.dumps({k:v for k,v in row.items() if k!='supersedes_adjudication_sha256'})+'\n'+json.dumps(row)+'\n')
            _,status=analysis.apply_adjudications(path,{key:source},ctx.annotations)
            self.assertEqual(status['applied_records'],2)
            review.write_text('changed')
            with self.assertRaisesRegex(RuntimeError,'review evidence'):analysis.apply_adjudications(path,{key:source},ctx.annotations)

    def test_complete_synthetic_four_model_report_reuses_paired_estimators(self):
        ctx=ScoringContext()
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);ctx.root=root;model_ids=['SYNTHETIC_A','SYNTHETIC_B','SYNTHETIC_C','SYNTHETIC_D']
            ctx.config=deepcopy(ctx.config)
            by_partition={}
            for model_cfg,model in zip(ctx.config['models'],model_ids):
                partition=model_cfg['partition'];model_cfg['model_id']=model;by_partition[partition]={}
                for task,rec in ctx.annotations.items():
                    for lang in ('en','bn','bn_cs'):
                        source={'task_id':task,'language':lang,'requested_model':model,'provider':partition,'run_index':1,
                                'snapshot_id':ctx.manifest['snapshot_id'],'status':'success','response_text':'SYNTHETIC TEST DATA',
                                'finish_status':'completed','generated_at_utc':'synthetic',
                                'prompt_sha256':rec['prompt_sha256'][lang]}
                        ratings=[]
                        for u in rec['rius']:
                            omitted=lang=='bn' and u['criticality']=='critical'
                            ratings.append({'item_id':u['id'],'score':0 if omitted else 1,'reason':'omitted' if omitted else 'met'})
                        ratings.extend({'item_id':c['id'],'score':1,'reason':'pass'} for c in rec['task_checks'])
                        by_partition[partition][(task,lang)]={**source,'ratings':ratings}
                        generation.append_jsonl(root/(partition+'.jsonl'),source)
            with patch.object(ctx,'frozen'),patch.object(ctx,'gate',return_value={'gate_pass':True}), \
                 patch.object(ctx,'scores',side_effect=lambda partition:by_partition[partition]), \
                 patch.object(analysis.shared,'BOOTSTRAP_N',3):
                report=analysis.analyze(ctx,root/'analysis'/'synthetic')
            self.assertEqual(report['expected_cells'],1884);self.assertEqual(report['scored_cells'],1884)
            self.assertEqual(report['models'],model_ids)
            self.assertEqual(report['effects']['critical_omission_rate:bn-en']['estimate'],1)
            self.assertIn('provisional',report['score_status'])
            self.assertFalse(report['adjudication_status']['independent_human_authenticity_certified'])
            text=(root/'analysis/synthetic/prelim_four_summary.md').read_text()
            self.assertIn('four-model',text)
            self.assertIn('Difficulty',text)


if __name__=='__main__':unittest.main()
