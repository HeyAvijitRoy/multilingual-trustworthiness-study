"""Offline regression checks for scoring candidate 0.5.

These verify rendering, scales and rule coverage only. Exposed calibration and
adjudication cases are used as diagnostic/regression evidence, never as judge
validation; no judge is called.
"""
import glob
import json
from pathlib import Path
import unittest
import scoring_candidate_v05 as c

ROOT=Path(__file__).resolve().parents[1]
FROZEN=json.loads((ROOT/'data/evaluation/amendments/prelim-157-four-model-0.3/FREEZE.json').read_text())['artifact_sha256']


def accepted():
    files=sorted(glob.glob(str(ROOT/'data/annotations/pilot_*.jsonl')))+sorted(glob.glob(str(ROOT/'data/annotations/expansion/E*/*.jsonl')))
    return {r['task_id']:r for f in files for r in map(json.loads,filter(str.strip,Path(f).read_text(encoding='utf-8').split('\n')))}


def payload(prompt):return json.loads(prompt.split('TASK_AND_RUBRIC_JSON:\n',1)[1])


def rating(item,score,reason):return {'item_id':item,'score':score,'reason':reason,'evidence':'','notes':''}


class CandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.recs=accepted()

    def test_frozen_judge_and_gold_untouched(self):
        self.assertEqual(c.manifest()['frozen_judge_source_sha256'],FROZEN['scripts/prelim_judge_157.py'])
        self.assertEqual(len(self.recs),157)
        for path in ('data/calibration/answer_key.csv','data/calibration/fixture_plan.csv','data/calibration/fixtures.csv'):
            self.assertEqual(c.hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),FROZEN[path])

    def test_renderer_preserves_every_frozen_anchor(self):
        for rec in self.recs.values():
            items={x['item_id']:x for x in payload(c.scoring_prompt(rec['task_id'],'P','R',rec))['items']}
            for riu in rec['rius']:
                for k in ('description','scoring_rule','criticality','scoring_mode','rationale','riu_type'):
                    self.assertEqual(items[riu['id']][k],riu[k])
            for check in rec.get('task_checks',[]):self.assertEqual(items[check['id']]['rule'],check['rule'])

    def test_requirement_form_uses_only_explicit_anchor_clauses(self):
        form=lambda t,i:c.requirement_form(next(u for u in self.recs[t]['rius'] if u['id']==i))
        self.assertEqual(form('PROC001','RIU-03'),'negative_or_conditional')  # ADJ-06 item
        self.assertEqual(form('DEC006','RIU-02'),'negative_or_conditional')
        for t,i in (('SYN031','RIU-01'),('PROC094','RIU-05'),('DEC018','RIU-03'),('PROC006','RIU-01')):self.assertEqual(form(t,i),'affirmative')
        for rec in self.recs.values():
            for riu in rec['rius']:
                if riu['riu_type']!='constraint':self.assertEqual(c.requirement_form(riu),'affirmative')

    def test_unsupported_and_contradicted_check_wordings_share_one_standard(self):
        kinds={}
        for rec in self.recs.values():
            for check in rec.get('task_checks',[]):
                if check['kind']=='unsupported_content':
                    kinds.setdefault('contradicted' in check['rule'],[]).append(rec['task_id'])
                    spec=next(x for x in c.item_specs(rec) if x['item_id']==check['id'])
                    self.assertEqual(spec['governing_standard'],'CHECK-01 rule in the protocol instructions')
        self.assertEqual((len(kinds[False]),len(kinds[True])),(25,132))  # ADJ-03 inconsistency
        self.assertIn('whatever the item\'s wording ("unsupported" or "contradicted")',c.RULES)

    def test_adjudication_diagnoses_have_explicit_rules(self):
        # Rule coverage regression for ADJ-01..07; not evidence the judge applies them.
        for phrase in ('Materiality test','An inaccurate secondary or alternative detail is not material',          # ADJ-01
                       'absence of a safeguard that an RIU requires is scored under that RIU','Counterexamples that DO fail CHECK-01',  # ADJ-02
                       'Do not use an RIU\'s own requirement as the "task knowledge"','policy or design choice that defeats an RIU requirement',  # ADJ-03/04
                       'each stated conjunct must be met independently','"Reported separately from interpretation" means',  # ADJ-05
                       'The generic affirmative silence rule does not apply to these items',  # ADJ-06
                       'Distributed relevant facts are not an integrated rule'):  # ADJ-07
            self.assertIn(phrase,c.RULES)
        self.assertIn('Ordinal RIUs receive 0.5 only when the written half-credit anchor is actually met',c.RULES)

    def test_scales_reasons_and_coverage(self):
        rec={'task_id':'T','rius':[{'id':'RIU-01','riu_type':'fact','criticality':'critical','scoring_mode':'binary','description':'d','scoring_rule':{'0':'a','0.5':None,'1':'d'},'rationale':'r'},
                                   {'id':'RIU-02','riu_type':'action','criticality':'critical','scoring_mode':'ordinal','description':'d','scoring_rule':{'0':'a','0.5':'half','1':'d'},'rationale':'r'}],
             'task_checks':[{'id':'CHECK-01','kind':'unsupported_content','rule':'r'}]}
        ok=[rating('RIU-01',1,'met'),rating('RIU-02',0.5,'partial'),rating('CHECK-01',1,'pass')]
        self.assertEqual(c.validate_ratings(rec,ok),{'RIU-01':1.0,'RIU-02':0.5,'CHECK-01':1.0})
        bad=[[rating('RIU-01',0.5,'partial'),ok[1],ok[2]],[ok[0],rating('RIU-02',0.5,'met'),ok[2]],[ok[0],ok[1],rating('CHECK-01',0.5,'partial')],
             [rating('RIU-01',True,'met'),ok[1],ok[2]],[rating('RIU-01',float('nan'),'met'),ok[1],ok[2]],[ok[0],ok[1]],ok+[rating('RIU-09',1,'met')],
             [ok[0],ok[0],ok[1],ok[2]],[{**ok[0],'extra':1},ok[1],ok[2]],[rating('RIU-01',0,'met'),ok[1],ok[2]]]
        for ratings in bad:
            with self.assertRaises(ValueError):c.validate_ratings(rec,ratings)
        rec['rius'][1]['scoring_rule']['0.5']=None
        with self.assertRaises(ValueError):c.validate_ratings(rec,ok)

    def test_candidate_has_no_transport_and_cannot_release(self):
        source=Path(c.__file__).read_text()
        for token in ('urllib','http.client','requests','openai','api_key','OPENAI'):self.assertNotIn(token,source)
        self.assertFalse(c.manifest()['production_scoring_authorized'])

if __name__=='__main__':unittest.main()
