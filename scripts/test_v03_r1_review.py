"""Offline checks with synthetic returns; never supplies real R1 decisions."""
from copy import deepcopy
import csv
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import v03_r1_review as review
from prepare_v03_r1_packet import FORM_FIELDS,COMPARE_FIELDS

class ReturnTests(unittest.TestCase):
    def row(self):
        return dict(zip(FORM_FIELDS,['R1-SYNTHETIC','CHECK-01','R1','0','SYNTHETIC test rationale',
             'SYNTHETIC evidence','no','','SYNTHETIC ONLY','2026-10-23']))
    def test_blank_or_invented_decisions_rejected(self):
        for change in ({'assessment':''},{'assessment':'0.5'},{'rationale':''},{'evidence_quote':''},
                       {'rubric_ambiguity':'yes'},{'review_date':''},{'reviewer':'invented'}):
            row=self.row();row.update(change)
            with self.subTest(change=change),self.assertRaises(ValueError):review.validate_return([row],{('R1-SYNTHETIC','CHECK-01')})
    def test_unresolved_requires_recorded_ambiguity(self):
        row=self.row();row.update(assessment='unresolved',rubric_ambiguity='unsure',rubric_ambiguity_details='SYNTHETIC ambiguity')
        self.assertEqual(review.validate_return([row],{('R1-SYNTHETIC','CHECK-01')}),[row])
    def test_duplicate_or_missing_rows_rejected(self):
        row=self.row();expected={('R1-SYNTHETIC','CHECK-01'),('R1-OTHER','CHECK-01')}
        with self.assertRaises(ValueError):review.validate_return([row,row],expected)
    def test_comparison_preserves_bytes_and_leaves_adjudication_empty(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);private=root/'staff';private.mkdir()
            mapping={'cases':[{'review_id':'R1-SYNTHETIC','checks':[{'public_check_id':'CHECK-01','reference_label':'1','judge_prediction':'0'}]}]}
            (private/'mapping.json').write_text(json.dumps(mapping));source=root/'returned.csv'
            with source.open('w',newline='') as out:
                w=csv.DictWriter(out,fieldnames=FORM_FIELDS);w.writeheader();w.writerow(self.row())
            raw=source.read_bytes()
            with patch.object(review,'PRIVATE',private),patch.object(review.four,'ROOT',root),patch.object(review,'validate'):
                result=review.compare(source)
                dest=root/result['private_output'];self.assertEqual((dest/'R1_REVIEW_FORM_COMPLETED.csv').read_bytes(),raw)
                fields,rows=review.read_csv(dest/'comparison.csv');self.assertEqual(tuple(fields),COMPARE_FIELDS)
                self.assertEqual(rows[0]['first_pass_assessment'],'0');self.assertEqual(rows[0]['reference_label'],'1')
                for field in ('adjudication_recommendation','adjudicated_label','adjudication_rationale','adjudication_date','prospective_action'):self.assertEqual(rows[0][field],'')
                self.assertEqual(rows[0]['adjudication_status'],'pending')
                with self.assertRaises(ValueError):review.compare(source)
    @unittest.skipUnless((review.PRIVATE/"mapping.json").exists(),"local private evidence needed for source audit")
    def test_live_packet_completeness_and_blinding(self):
        result=review.validate();self.assertEqual(result['review_cases'],5);self.assertEqual(result['source_RIUs_included'],25)

if __name__=='__main__':unittest.main()

class PacketInventoryTests(unittest.TestCase):
    def packet(self,root):
        folder=root/'packet';folder.mkdir()
        for name in review.FILES:(folder/name).touch()
        return folder
    def test_ignored_untracked_return_is_excluded_without_changing_packet(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);folder=self.packet(root);(folder/'R1_REVIEW_FORM_COMPLETED.csv').write_text('SYNTHETIC RETURN ONLY')
            with patch.object(review.four,'ROOT',root),patch.object(review.subprocess,'run') as run:
                run.side_effect=[type('Result',(),{'returncode':0})(),type('Result',(),{'returncode':1})()]
                self.assertEqual(review.validate_packet_inventory(folder),1)
            self.assertEqual(len(review.FILES),4)
    def test_tracked_or_unignored_return_is_rejected(self):
        for statuses in ((0,0),(1,1)):
            with self.subTest(statuses=statuses),tempfile.TemporaryDirectory() as d:
                root=Path(d);folder=self.packet(root);(folder/'R1_REVIEW_FORM_COMPLETED.csv').touch()
                with patch.object(review.four,'ROOT',root),patch.object(review.subprocess,'run') as run:
                    run.side_effect=[type('Result',(),{'returncode':n})() for n in statuses]
                    with self.assertRaisesRegex(ValueError,'ignored and untracked'):review.validate_packet_inventory(folder)
    def test_unexpected_file_or_missing_original_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);folder=self.packet(root);(folder/'staff_mapping.json').touch()
            with self.assertRaisesRegex(ValueError,'unexpected file'):review.validate_packet_inventory(folder)
            (folder/'staff_mapping.json').unlink();(folder/review.FILES[0]).unlink()
            with self.assertRaisesRegex(ValueError,'incomplete'):review.validate_packet_inventory(folder)
