"""Snapshot boundary and request-integrity checks with synthetic records only."""
from copy import deepcopy
import json
import unittest
import audit_generation_metadata_v04 as audit

class AuditTests(unittest.TestCase):
    def test_incomplete_last_write_excluded_without_losing_closed_unicode_record(self):
        raw=(json.dumps({'text':'পরীক্ষা'},ensure_ascii=False)+'\n').encode();tail=b'{"partial":'
        prefix,rows,excluded=audit.complete_prefix(raw+tail)
        self.assertEqual(prefix,raw);self.assertEqual(rows,[{'text':'পরীক্ষা'}]);self.assertEqual(excluded,len(tail))
    def test_unicode_line_separators_remain_inside_one_record(self):
        value={'text':'SYNTHETIC\u2028separator\u0085inside text'}
        data=(json.dumps(value,ensure_ascii=False)+'\n').encode()
        _,records,tail=audit.complete_prefix(data)
        self.assertEqual(records,[value]);self.assertEqual(tail,0)
    def test_corrupt_closed_record_rejected(self):
        with self.assertRaises(json.JSONDecodeError):audit.complete_prefix(b'{broken}\n')
    def test_prompt_or_parameter_tampering_rejected(self):
        cell={'prompt_text':'SYNTHETIC one task'};config={'system_prompt':'SYNTHETIC system','max_output_tokens':32768};model={'model_id':'SYNTHETIC'}
        row={'prompt_text':cell['prompt_text'],'system_prompt':config['system_prompt'],'request_parameters':{'model':model,'max_output_tokens':32768,'tools_enabled':False,'external_grounding':False}}
        audit.validate_request_record(row,cell,config,model)
        changed=deepcopy(row);changed['prompt_text']+=' plus bundled task'
        with self.assertRaises(ValueError):audit.validate_request_record(changed,cell,config,model)
        changed=deepcopy(row);changed['request_parameters']['max_output_tokens']=128
        with self.assertRaises(ValueError):audit.validate_request_record(changed,cell,config,model)
    def test_complete_triplets_require_all_three_distinct_languages(self):
        keys={('SYNTHETIC-A','en'),('SYNTHETIC-A','bn'),('SYNTHETIC-B','en'),('SYNTHETIC-B','bn'),('SYNTHETIC-B','bn_cs')}
        self.assertEqual(audit.triplets(keys),{'SYNTHETIC-B'})

    def test_order_allows_only_recorded_failure_gaps(self):
        exp=[('A','en'),('B','en'),('C','en'),('D','en')]
        self.assertTrue(audit.order_consistent([('A','en'),('B','en')],exp,[]))
        self.assertFalse(audit.order_consistent([('A','en'),('C','en')],exp,[]))
        self.assertTrue(audit.order_consistent([('A','en'),('C','en')],exp,[('B','en')]))
        self.assertTrue(audit.order_consistent([('A','en'),('B','en'),('C','en')],exp,[('B','en')]))  # retried in place
        self.assertFalse(audit.order_consistent([('A','en'),('D','en')],exp,[('B','en')]))
        self.assertFalse(audit.order_consistent([('B','en'),('A','en')],exp,[]))

if __name__=='__main__':unittest.main()
