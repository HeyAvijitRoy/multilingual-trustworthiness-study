import unittest

from helpers import step

inputs = step('01_validate_inputs')

EN = 'Restart the router 2 times and wait 30 seconds.'
BN = 'রাউটারটি ২ বার রিস্টার্ট করুন এবং ৩০ সেকেন্ড অপেক্ষা করুন, তারপর আবার চেষ্টা করুন।'
CS = 'router-টি ২ বার restart করুন এবং ৩০ সেকেন্ড অপেক্ষা করুন, তারপর আবার চেষ্টা করুন।'


class LanguageChecksTest(unittest.TestCase):
    def test_clean_prompts_pass(self):
        self.assertEqual(inputs.check_language('T1', EN, BN, CS), [])

    def test_missing_number_is_caught(self):
        self.assertTrue(any('numbers' in e for e in inputs.check_language('T1', EN, BN.replace('৩০', ''), CS)))

    def test_latin_words_in_bengali_are_caught(self):
        self.assertTrue(any('Latin-script' in e for e in inputs.check_language('T1', EN, BN + ' router', CS)))

    def test_fused_script_boundary_is_caught(self):
        self.assertTrue(any('fused' in e for e in inputs.check_language('T1', EN, BN, CS.replace('router-টি', 'routerটি'))))


class RealInputsTest(unittest.TestCase):
    def test_study_inputs_are_valid(self):
        self.assertEqual(inputs.main(), 0)


if __name__ == '__main__':
    unittest.main()
