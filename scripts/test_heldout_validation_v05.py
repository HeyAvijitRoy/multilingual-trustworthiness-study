"""Offline checks for the held-out construction checker, using synthetic fixtures only."""
import copy
import unittest
import heldout_validation_v05 as h

ZERO='Absent, incorrect, contradicted, or does not meet an available positive anchor.'


def riu(i,crit='critical',mode='binary',kind='action'):
    d=f'Synthetic requirement {i}.'
    return {'id':f'RIU-{i:02d}','riu_type':kind,'criticality':crit,'description':d,'scoring_mode':mode,
            'scoring_rule':{'0':ZERO,'0.5':'Half anchor.' if mode=='ordinal' else None,'1':d},'rationale':'r'}


def fixture(n,domain,language):
    text={'en':'Synthetic prompt about a printer.','bn':'এটি একটি কৃত্রিম প্রশ্ন, প্রিন্টার নিয়ে।','bn_cs':'এটা একটা synthetic প্রশ্ন, printer নিয়ে।'}[language]
    return {'fixture_id':f'X{n:03d}','family_id':f'XF{n:03d}','domain':domain,'language':language,'safety_relevance':'low',
            'task_objective':'o','constraints':[],'prompt_text':text,'response_text':text,
            'rius':[riu(1),riu(2),riu(3,'supporting','ordinal'),riu(4,'supporting')],
            'task_checks':[{'id':'CHECK-01','kind':'unsupported_content','rule':'r'}],'coverage_tags':['complete_fulfillment']}


def design():
    records,intent=[],[];n=0
    for d in h.DOMAINS:
        for l in h.LANGUAGES:
            for p in h.PHENOTYPES*2:
                n+=1;records.append(fixture(n,d,l))
                intent.append({'fixture_id':f'X{n:03d}','phenotype':p,'intended_scores':{'RIU-01':1,'RIU-02':0,'RIU-03':0.5,'RIU-04':1,'CHECK-01':1}})
    return records,intent


class HeldoutCheckerTests(unittest.TestCase):
    def test_complete_balanced_design_passes(self):
        r,i=design();result=h.check(r,i,{})
        self.assertEqual(result['errors'],[]);self.assertTrue(result['complete_design'])
        self.assertEqual((result['riu_items'],result['critical_riu_items'],result['safety_check_items']),(360,180,90))

    def test_rejects_imbalance_scale_and_rubric_defects(self):
        r,i=design()
        bad=copy.deepcopy(i);bad[0]['phenotype']='acceptable' if bad[0]['phenotype']!='acceptable' else 'borderline'
        self.assertTrue(any('stratum' in e for e in h.check(r,bad,{})['errors']))
        bad=copy.deepcopy(i);bad[0]['intended_scores']['RIU-01']=0.5
        self.assertTrue(any('outside scale' in e for e in h.check(r,bad,{})['errors']))
        for mutate,needle in ((lambda x:x['rius'][2]['scoring_rule'].update({'0.5':None}),'half anchor'),
                              (lambda x:x['rius'][0]['scoring_rule'].update({'0.5':'x'}),'binary half'),
                              (lambda x:x['rius'][1].update({'criticality':'supporting'}),'two critical'),
                              (lambda x:x.update({'safety_relevance':'none'}),'safety_relevance'),
                              (lambda x:x['task_checks'].clear(),'CHECK-01'),
                              (lambda x:x.update({'coverage_tags':['made_up']}),'coverage'),
                              (lambda x:x.update({'family_id':'XF002'}),'duplicate family')):
            rr=copy.deepcopy(r);mutate(rr[0])
            self.assertTrue(any(needle in e for e in h.check(rr,i,{})['errors']),needle)

    def test_language_script_bounds(self):
        r,i=design();rr=copy.deepcopy(r)
        bn=next(x for x in rr if x['language']=='bn');bn['prompt_text']=bn['response_text']='Mostly English text here.'
        self.assertTrue(any('BN Bengali share' in e for e in h.check(rr,i,{})['errors']))

    def test_overlap_with_study_prompts_rejected(self):
        r,i=design();corpus={'en':[('STUDY1',h.grams(r[0]['prompt_text']))]}
        self.assertTrue(any('overlaps study task STUDY1' in e for e in h.check(r,i,corpus)['errors']))

    def test_no_transport(self):
        source=open(h.__file__).read()
        for token in ('urllib','requests','openai','http.client'):self.assertNotIn(token,source)

if __name__=='__main__':unittest.main()
