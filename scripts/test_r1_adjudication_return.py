"""Synthetic return checks; never generates or changes real reviewer decisions."""
from copy import deepcopy
from datetime import date
from pathlib import Path
import tempfile
import unittest
import check_r1_adjudication_return as intake

class ReturnTests(unittest.TestCase):
    def sample(self):
        rows=[];expected={};cases={}
        for i in range(7):
            row=dict.fromkeys(intake.packet.FIELDS,'');row.update(adjudication_id=f'SYNTHETIC-{i}',review_id=f'SYNTHETIC-REVIEW-{i}',fixture_id=f'SYNTHETIC-FIXTURE-{i}',task_id=f'SYNTHETIC-TASK-{i}',language='en',item_id='SYNTHETIC-ITEM',item_kind='task_check' if i<5 else 'riu',scoring_mode='ordinal' if i==6 else 'check' if i<5 else 'binary',reviewer='R1')
            expected[row['adjudication_id']]=deepcopy(row)
            row.update(adjudication_decision='' if i==6 else 'Pass (1)',adjudicated_riu_score='0.5' if i==6 else '',interpretation='Reference interpretation supported',rationale='SYNTHETIC rationale',response_evidence='SYNTHETIC evidence',frozen_criterion='SYNTHETIC criterion',review_date='2026-10-24')
            cases[row['adjudication_id']]={'reference':{'intended_score':'0.5' if i==6 else '1'},'judge':{'score':'1' if i==6 else '0'},'r1_first_pass':{'assessment':'0'} if i<5 else None,'context':{'response_text':'SYNTHETIC evidence with additional text'}}
            rows.append(row)
        return rows,expected,cases
    def validate(self,rows,expected,cases):return intake.validate_rows(rows,expected,cases,date(2026,10,24))
    def test_complete_return_preserves_half_credit_and_input_fields(self):
        rows,e,c=self.sample();original=deepcopy(rows);out=self.validate(rows,e,c)
        self.assertEqual(rows,original);self.assertEqual(out[-1]['normalized_adjudication_score'],'0.5')
        self.assertEqual(out[-1]['as_returned']['adjudication_decision'],'');self.assertIsNone(out[-1]['first_pass_score'])
    def test_missing_duplicate_or_changed_identity_rejected(self):
        rows,e,c=self.sample()
        for bad in (rows[:-1],rows[:-1]+[rows[0]]):
            with self.assertRaises(ValueError):self.validate(bad,e,c)
        rows[0]['language']='bn'
        with self.assertRaises(ValueError):self.validate(rows,e,c)
    def test_missing_rationale_or_future_date_rejected(self):
        for field,value in [('rationale',''),('frozen_criterion',''),('review_date','2026-10-25')]:
            rows,e,c=self.sample();rows[0][field]=value
            with self.assertRaises(ValueError):self.validate(rows,e,c)
    def test_conflicting_half_credit_or_binary_scores_rejected(self):
        rows,e,c=self.sample();rows[-1]['adjudication_decision']='Fail (0)'
        with self.assertRaises(ValueError):self.validate(rows,e,c)
        rows,e,c=self.sample();rows[-2]['adjudicated_riu_score']='0.5'
        with self.assertRaises(ValueError):self.validate(rows,e,c)
    def test_interpretation_cannot_disagree_with_recorded_score(self):
        rows,e,c=self.sample();rows[0]['interpretation']='Judge interpretation supported'
        with self.assertRaises(ValueError):self.validate(rows,e,c)
    def test_unresolved_not_converted_to_a_score(self):
        rows,e,c=self.sample();rows[0].update(adjudication_decision='Unresolved',interpretation='Rubric ambiguity prevents resolution')
        out=self.validate(rows,e,c);self.assertIsNone(out[0]['normalized_adjudication_score']);self.assertIsNone(out[0]['reference_match'])
    def test_two_exact_excerpts_accepted_without_rewriting_field(self):
        value='SYNTHETIC evidence | additional text';r=intake.evidence_check(value,'SYNTHETIC evidence with additional text')
        self.assertEqual(len(r['spans']),2);self.assertEqual(r['spans'][1]['text'],'additional text')
        self.assertEqual(intake.evidence_check('describes absence','SYNTHETIC evidence')['status'],'description-or-quote-requires-manual-check')
    def test_preservation_idempotent_and_different_bytes_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'return.csv';intake.preserve(path,b'SYNTHETIC\r\n');intake.preserve(path,b'SYNTHETIC\r\n')
            self.assertEqual(path.read_bytes(),b'SYNTHETIC\r\n')
            with self.assertRaises(ValueError):intake.preserve(path,b'CHANGED\n')

class SnapshotReviewStatusTests(unittest.TestCase):
    def test_valid_return_hash_can_update_metadata_without_releasing_scoring(self):
        import hashlib,json
        from unittest.mock import patch
        import snapshot_generation_v04 as snapshot
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);source=root/'data/evaluation/reviews/v03_calibration_R1/adjudication/R1_ADJUDICATION_FORM_COMPLETED.csv';source.parent.mkdir(parents=True);source.write_bytes(b'SYNTHETIC RETURN')
            status=root/'data/evaluation/remediation/v03_R1_adjudication/RETURN_STATUS.json';status.parent.mkdir(parents=True)
            value={'status':'returned-validated-comparison-prepared','returned_form_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'production_scoring_authorized':False}
            status.write_text(json.dumps(value))
            with patch.object(snapshot.gen,'ROOT',root):
                self.assertEqual(snapshot.current_adjudication_status(),value)
                source.write_bytes(b'CHANGED')
                with self.assertRaises(RuntimeError):snapshot.current_adjudication_status()
                source.write_bytes(b'SYNTHETIC RETURN');value['production_scoring_authorized']=True;status.write_text(json.dumps(value))
                with self.assertRaises(RuntimeError):snapshot.current_adjudication_status()

if __name__=='__main__':unittest.main()
