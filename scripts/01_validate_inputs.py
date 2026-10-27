#!/usr/bin/env python3
"""Step 01: validate the study inputs.

Checks the prompt corpus (500 tasks x EN/BN/BN-CS), the annotations (157 accepted
gold tasks, 343 drafts), the study configuration and both judge-validation sets.
No network access and no writes.

    python3 scripts/01_validate_inputs.py

Exits 1 and lists every problem found; prints a one-line summary when all checks pass.
"""
import csv
import re
import sys
from collections import Counter, defaultdict

from common import DATA, DOMAINS, LANGS, load_annotations, load_prompts, load_study, read_json, sha256_text

FIELDS = ['task_id', 'domain', 'subdomain', 'difficulty', 'prompt_en', 'prompt_bn', 'prompt_bn_cs']
PREFIX = {'technical_troubleshooting': 'TECH', 'cybersecurity_digital_safety': 'CYBER',
          'procedural_instructional': 'PROC', 'decision_support': 'DEC', 'information_synthesis': 'SYN'}
BENGALI = re.compile(r'[ঀ-৿]')
LATIN = re.compile(r'[A-Za-z]')
LATIN_BENGALI = re.compile(r'[A-Za-z0-9][ঀ-৿]')
BENGALI_LATIN = re.compile(r'[ঀ-৿][A-Za-z]')
VOWEL_SIGN_AFTER_HYPHEN = re.compile(r'-[া-্ৗ]')
NON_BENGALI_INDIC = re.compile(r'[ऀ-ॣ०-ॿ]')
NUMBER = re.compile(r'\d+(?:\.\d+)?')
BENGALI_DIGITS = str.maketrans('০১২৩৪৫৬৭৮৯', '0123456789')
CS_WORD = re.compile(r'[A-Za-z][A-Za-z-]*|[ঀ-৿]+')
CS_SUFFIX = re.compile(r'([A-Za-z][A-Za-z-]*)-(এর|র|এ|তে)(?![ঀ-৿])')
VOWEL_FINAL = re.compile(r'(?:[aiouyw]|ee|ie|ue|oo)$', re.I)
# Calques and malformed fragments removed in corpus v0.3; see data/prompts/README.md.
DEPRECATED_BN = {'কার্যকরী ফোল্ডার', 'ধারাবাহিক সমন্বয়', 'নির্মাণ সঞ্চয়', 'বাস্তব এপিআই', 'গ্রাহক ব্যর্থতা',
                 'পুনরাবৃত্তি-নিরাপত্তা', 'সেবা অ্যাকাউন্ট', 'নিরাপত্তা উন্মুক্ততা', 'সমর্থনযোগ্যতা', 'দুর্নীতি',
                 'স্থির হয়ে যায়', 'বিনিময়মূলক প্রভাব', 'স্টোরেজ বালতি', 'প্রান্তসুরক্ষা', 'রোগনির্ণয়', 'ছাঁকনি',
                 'দূরবর্তী ইনস্টলেশন ক্লিনিক'}
DEPRECATED_CS = {'recordিং', 'reportিং', 'monitorিং', 'processিং', 'পূর্বregistration', 'প্রো file'}
RIU_FIELDS = {'id', 'riu_type', 'criticality', 'description', 'scoring_mode', 'scoring_rule', 'rationale'}


def numbers(text):
    return Counter(n for n in NUMBER.findall(text.translate(BENGALI_DIGITS).replace(',', '')) if n != '00')


def check_language(task_id, en, bn, cs):
    errors = []
    bn_b, bn_l = len(BENGALI.findall(bn)), len(LATIN.findall(bn))
    cs_b, cs_l = len(BENGALI.findall(cs)), len(LATIN.findall(cs))
    if bn_b < 20 or bn_b / (bn_b + bn_l) < 0.55:
        errors.append('BN is not predominantly Bengali')
    if cs_b < 10 or cs_l < 4 or not 0.25 <= cs_b / (cs_b + cs_l) <= 0.985:
        errors.append('BN-CS must mix Bengali and English with Bengali as matrix')
    if bn == cs:
        errors.append('BN and BN-CS identical')
    if LATIN_BENGALI.search(cs) or BENGALI_LATIN.search(cs):
        errors.append('BN-CS has a fused script boundary')
    for phrase in DEPRECATED_BN:
        if re.search(r'(?<![ঀ-৿])' + re.escape(phrase), bn + '\n' + cs):
            errors.append('deprecated phrase ' + phrase)
    errors += ['malformed BN-CS fragment ' + f for f in DEPRECATED_CS if f in cs]
    for name, text in (('BN', bn), ('BN-CS', cs)):
        if NON_BENGALI_INDIC.search(text):
            errors.append(name + ' has non-Bengali Indic characters')
        if text.count('(') > en.count('('):
            errors.append(name + ' adds parentheticals absent from EN')
        if numbers(en) - numbers(text):
            errors.append(f'{name} misses EN numbers {sorted(numbers(en) - numbers(text))}')
    latin_words = [w for w in re.findall(r'[A-Za-z]+', bn) if not (len(w) == 1 and w.isupper())]
    if latin_words:
        errors.append(f'BN has Latin-script words {latin_words[:5]}')
    if VOWEL_SIGN_AFTER_HYPHEN.search(cs):
        errors.append('BN-CS vowel sign after hyphen')
    for m in CS_SUFFIX.finditer(cs):
        word, suffix = m.groups()
        if not word.isupper() and len(word) > 2 and (suffix in {'র', 'তে'}) != bool(VOWEL_FINAL.search(word)):
            errors.append('BN-CS suffix mismatch ' + m.group(0))
    words = CS_WORD.findall(cs)
    if sum(w[0].isascii() for w in words) / len(words) > 0.6:
        errors.append('BN-CS English word share above 0.6')
    return [f'{task_id}: {e}' for e in errors]


def check_corpus(prompts):
    errors = []
    for path in sorted((DATA / 'prompts').glob('*_[0-9]*.csv')):
        with path.open(encoding='utf-8-sig', newline='') as f:
            if csv.DictReader(f).fieldnames != FIELDS:
                errors.append(f'{path.name}: columns differ from {FIELDS}')
    rows = list(prompts.values())
    if len(rows) != 500:
        errors.append(f'corpus has {len(rows)} tasks, expected 500')
    for domain, prefix in PREFIX.items():
        ids = sorted(int(r['task_id'].removeprefix(prefix)) for r in rows if r['domain'] == domain)
        if ids != list(range(1, 101)):
            errors.append(f'{domain}: IDs are not {prefix}001-{prefix}100')
        if Counter(r['difficulty'] for r in rows if r['domain'] == domain) != Counter(easy=25, medium=50, hard=25):
            errors.append(f'{domain}: difficulty is not 25/50/25')
    for field in ('prompt_en', 'prompt_bn', 'prompt_bn_cs'):
        normalized = Counter(re.sub(r'\s+', ' ', r[field]).strip().casefold() for r in rows)
        if any(n > 1 for n in normalized.values()):
            errors.append(f'duplicate prompts in {field}')
    extended = {r['task_id'] for r in rows if r['subdomain'] == 'extended_context'}
    if extended != {f'SYN{i:03d}' for i in range(91, 101)}:
        errors.append('extended-context subset is not SYN091-SYN100')
    for r in rows:
        if any(not r[f].strip() for f in FIELDS):
            errors.append(r['task_id'] + ': empty field')
            continue
        errors += check_language(r['task_id'], r['prompt_en'], r['prompt_bn'], r['prompt_bn_cs'])
    return errors


def check_record(rec, prompts):
    tid, errors = rec['task_id'], []
    corpus = prompts.get(tid)
    if corpus is None:
        return [f'{tid}: not in corpus']
    if (rec['domain'], rec['difficulty']) != (corpus['domain'], corpus['difficulty']):
        errors.append(f'{tid}: domain/difficulty differ from corpus')
    for lang in LANGS:
        if rec['prompt_sha256'][lang] != sha256_text(corpus['prompt_' + lang]):
            errors.append(f'{tid}: {lang} prompt hash differs from corpus')
    ids = [r['id'] for r in rec['rius']]
    if len(ids) != len(set(ids)) or not ids:
        errors.append(f'{tid}: RIU ids missing or duplicated')
    for riu in rec['rius']:
        if not RIU_FIELDS <= set(riu):
            errors.append(f"{tid}/{riu.get('id')}: missing fields {sorted(RIU_FIELDS - set(riu))}")
            continue
        if riu['criticality'] not in {'critical', 'supporting'} or riu['scoring_mode'] not in {'binary', 'ordinal'}:
            errors.append(f"{tid}/{riu['id']}: bad criticality or scoring mode")
        if riu['scoring_mode'] == 'binary' and riu['scoring_rule'].get('0.5'):
            errors.append(f"{tid}/{riu['id']}: binary RIU has a half anchor")
    checks = [c['id'] for c in rec.get('task_checks', [])]
    if 'CHECK-01' not in checks:
        errors.append(f'{tid}: missing CHECK-01')
    return errors


def check_annotations(prompts, study):
    errors = []
    gold, drafts = load_annotations('gold'), load_annotations('drafts')
    study_ids = {t['task_id'] for t in study['tasks']}
    if set(gold) != study_ids or len(gold) != 157:
        errors.append(f'gold set ({len(gold)}) differs from study tasks ({len(study_ids)})')
    if set(gold) & set(drafts):
        errors.append('task both gold and draft')
    for kind, recs, status in (('gold', gold, 'accepted'), ('drafts', drafts, 'draft')):
        for rec in recs.values():
            if rec.get('status') != status:
                errors.append(f"{rec['task_id']}: status {rec.get('status')} in {kind}")
            errors += check_record(rec, prompts)
    for t in study['tasks']:
        if t['task_id'] in gold and (t['domain'], t['difficulty']) != (gold[t['task_id']]['domain'], gold[t['task_id']]['difficulty']):
            errors.append(f"{t['task_id']}: study config disagrees with annotation")
    return errors


def check_validation_sets():
    errors = []
    for name in ('heldout', 'calibration'):
        folder = DATA / 'validation' / name
        fixtures = read_json(folder / 'fixtures.json')
        with (folder / 'references.csv').open(encoding='utf-8') as f:
            refs = {(r['fixture_id'], r['item_id']): r['score'] for r in csv.DictReader(f)}
        items = {(fx['fixture_id'], i) for fx in fixtures
                 for i in [r['id'] for r in fx['rius']] + [c['id'] for c in fx.get('task_checks', [])]}
        if items != set(refs):
            errors.append(f'{name}: references do not cover exactly the fixture items')
        if any(s not in {'0', '0.5', '1'} for s in refs.values()):
            errors.append(f'{name}: reference score outside 0/0.5/1')
    return errors


def main():
    prompts, study = load_prompts(), load_study()
    errors = check_corpus(prompts) + check_annotations(prompts, study) + check_validation_sets()
    if errors:
        print('\n'.join(errors))
        print(f'{len(errors)} problem(s) found')
        return 1
    gold = load_annotations('gold')
    rius = [r for rec in gold.values() for r in rec['rius']]
    print(f"inputs valid: 500 tasks / 1,500 prompts; {len(gold)} gold tasks, {len(rius)} RIUs "
          f"({sum(r['criticality'] == 'critical' for r in rius)} critical); {len(load_annotations('drafts'))} drafts; "
          f"validation sets heldout + calibration")
    return 0


if __name__ == '__main__':
    sys.exit(main())
