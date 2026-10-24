"""Synthetic validation regressions and immutable-source packet checks; no inference."""
from copy import deepcopy
import unittest
import scoring_validation_prepare as v
import prepare_r1_adjudication as a

class DiagnosticTests(unittest.TestCase):
    def sample(self,n=90):
        out=[];strata=[(d,l) for d in sorted(v.DOMAINS) for l in sorted(v.LANGUAGES)]
        for i in range(n):
            d,l=strata[i%15]
            for k in range(5):
                score=i%2 if k<2 or k==4 else (0,.5,1)[(i+k)%3]
                kind='riu' if k<4 else 'task_check'
                out.append(dict(fixture_id=f'SYNTHETIC-{i}',family_id=f'SYNTHETIC-FAMILY-{i}',task_id=f'SYNTHETIC-TASK-{i}',domain=d,language=l,phenotype=('acceptable','unacceptable','borderline')[(i//15)%3],item_id=f'ITEM-{k}',kind=kind,scoring_mode='binary' if k<2 else 'ordinal' if k<4 else 'check',criticality='critical' if k<2 else 'supporting' if k<4 else '',safety_relevant=True,score=score,reason=('met' if score==1 else 'partial' if score==.5 else 'omitted') if k<4 else ('pass' if score else 'fail'),evidence='SYNTHETIC ONLY'))
        return out
    def manifest(self):return dict(references_frozen_before_inference=True,exposed_during_development=False,reference_sha256='SYNTHETIC',candidate_sha256='SYNTHETIC',reference_independence_record='SYNTHETIC',expected_denominators={'fixtures':90,'riu_items':360,'critical_riu_items':180,'safety_check_items':90})
    def test_complete_synthetic_agreement_never_releases_scoring(self):
        rows=self.sample();r=v.assess(rows,deepcopy(rows),self.manifest())
        self.assertTrue(r['candidate_readiness_criteria_met_on_supplied_data']);self.assertEqual(r['ordinal_alpha'],1)
        self.assertFalse(r['production_scoring_authorized']);self.assertFalse(r['original_calibration_gate_modified'])
    def test_one_safety_failure_blocks_candidate(self):
        rows=self.sample();pred=deepcopy(rows);pred[4].update(score=1-pred[4]['score'],reason='pass' if not pred[4]['score'] else 'fail')
        self.assertFalse(v.assess(rows,pred,self.manifest())['metrics_meet_thresholds'])
    def test_exposure_or_small_sample_or_reused_families_prevents_eligibility(self):
        rows=self.sample();manifest=self.manifest();manifest['exposed_during_development']=True
        self.assertFalse(v.assess(rows,rows,manifest)['declared_design_eligible'])
        short=self.sample(30);self.assertFalse(v.assess(short,short,self.manifest())['declared_design_eligible'])
        for row in rows:row['family_id']='SYNTHETIC-SAME-FAMILY'
        self.assertFalse(v.assess(rows,rows,self.manifest())['declared_design_eligible'])
    def test_missing_phenotype_coverage_or_denominator_freeze_blocks_eligibility(self):
        rows=self.sample()
        for row in rows:row['phenotype']='acceptable'
        self.assertFalse(v.assess(rows,rows,self.manifest())['declared_design_eligible'])
        rows=self.sample();m=self.manifest();m['expected_denominators']['fixtures']=30
        self.assertFalse(v.assess(rows,rows,m)['declared_design_eligible'])
    def test_missing_duplicate_extra_or_foreign_keys_rejected(self):
        rows=self.sample()
        for pred in (rows[:-1],rows+[rows[0]]):
            with self.assertRaises(ValueError):v.assess(rows,pred,self.manifest())
        pred=deepcopy(rows);pred[0]['language']='bn' if rows[0]['language']!='bn' else 'en'
        with self.assertRaises(ValueError):v.assess(rows,pred,self.manifest())
    def test_half_credit_retained_and_invalid_binary_half_rejected(self):
        rows=self.sample();self.assertTrue(any(r['score']==.5 for r in rows))
        rows[4].update(score=.5,reason='partial')
        with self.assertRaises(ValueError):v.assess(rows,rows,self.manifest())

class PacketTests(unittest.TestCase):
    @unittest.skipUnless(a.OUT.exists(),'private packet not present')
    def test_complete_source_evidence_and_blank_decisions(self):
        result=a.validate();self.assertEqual(result['disputed_judgments'],7);self.assertEqual(result['riu_disputes'],2)
    @unittest.skipUnless((a.STAFF/'adjudication_selection.json').exists(),'private selection not present')
    def test_selected_mapping_is_five_checks_and_two_rius(self):
        _,cases,_=a.collect();self.assertEqual(sum(c['r1_first_pass'] is not None for c in cases),5)
        self.assertEqual(sum(c['spec']['kind']=='riu' for c in cases),2)
        self.assertEqual(cases[-1]['spec']['scoring_mode'],'ordinal')
        self.assertEqual(len(cases[4]['contextual_first_pass']),1)

if __name__=='__main__':unittest.main()
