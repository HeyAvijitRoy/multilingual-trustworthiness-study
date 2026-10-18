# Language realization guide (corpus v0.3)

This guide governs how each canonical English task is realized in Bengali (`prompt_bn`) and Bengali-English code-switched Bengali (`prompt_bn_cs`). It replaces the v0.2 approach, which generated BN-CS by substituting words from a lexicon into the Bengali text. v0.3 BN and BN-CS are hand-written, task by task.

## The manipulated variable

The three conditions should differ in **language and code choice only**. The following stay fixed across EN, BN and BN-CS:

- task objective, facts, numbers, comparators, time windows and caveats
- explicit constraints and output requirements: sentence counts, "concise", "table", "step by step", "safest", "first"
- register: the polite second person (আপনি) with imperatives (`করুন`, `দিন`, `লিখুন`) in both Bengali conditions
- clause order, wherever Bengali grammar allows

Neither Bengali condition may add hints, examples, structure cues or emphasis that EN lacks, or drop any of these that EN has. Superlatives and quantifiers carry over exactly ("safest" → `সবচেয়ে নিরাপদ`; "longest" → `সবচেয়ে বেশি সময় ধরে`; "at least" → `অন্তত`).

## BN: natural contemporary Bengali

- Standard colloquial written Bengali (চলিত রীতি). Where Bangladeshi and West Bengal usage differ (পানি/জল), the corpus follows Bangladeshi standard usage throughout.
- Native vocabulary wherever an ordinary educated reader would use it: ব্যবহারকারী, অগ্রাধিকার, সময়সীমা, জরিপ, প্রতিবেদন, ঝুঁকি, প্রমাণ.
- **English words in Bengali phonetic spelling are welcome** wherever that is what Bengali speakers actually say: ওয়ার্নিং (not সতর্কবার্তা for a software warning), এরর, চেক, সেটিংস, আপডেট, ডিপ্লয়. The test is everyday professional speech, not purism. In BN these words are always written in Bengali script; Latin-script English belongs to BN-CS. That script difference is part of what separates the two Bengali conditions.
- **Established technical loanwords are written in Bengali script, not calqued.** Write ল্যাপটপ, সফটওয়্যার, পাসওয়ার্ড, ব্যাকআপ, পার্টিশন, সার্ভিস অ্যাকাউন্ট, ক্লোন, রিসেট, হ্যাং, ক্র্যাশ, স্প্রেডশিট, ড্যাশবোর্ড. Sanskritized coinages that a technical reader would not recognize are prohibited. Examples from v0.2:

  | Avoid (v0.2) | Use | Concept |
  |---|---|---|
  | সেবা অ্যাকাউন্ট | সার্ভিস অ্যাকাউন্ট | service account |
  | বাস্তব কাজ | প্রোডাকশন … কাজ | production |
  | স্থির হয়ে যায় | হ্যাং হয়ে যায় | freezes |
  | অনুলিপি করা (disk) | ক্লোন করা | clone |
  | নিরাপত্তা উন্মুক্ততা | নিরাপত্তা ঝুঁকির মাত্রা (এক্সপোজার) | security exposure |
  | সমর্থনযোগ্যতা | সাপোর্ট ও রক্ষণাবেক্ষণের সুযোগ | supportability |
  | সফটওয়্যার দুর্নীতি | সফটওয়্যার/ফাইল নষ্ট হওয়া (করাপশন) | corruption |
  | বিনিময়মূলক প্রভাব | সুবিধা-অসুবিধার ভারসাম্য (ট্রেড-অফ) | trade-offs |
  | দূরবর্তী ইনস্টলেশন ক্লিনিক | অনলাইন ইনস্টলেশন সহায়তা সেশন | remote clinic |

- Spelling conventions fixed by the study lead: হেল্‌থ চেক (হেল্‌থ written with hasanta + ZWNJ, not the conjunct হেলথ); ওয়ার্নিং.
- Acronyms appear in Bengali script when that is common (এসএসডি, ভিপিএন, এপিআই). Literal on-screen identifiers stay exactly as in EN: error codes, file names, paths, group labels such as "A".
- Numbers use Bengali digits (১২ শতাংশ, ২,৪০০, ৪.২). Clock times use Bengali time-of-day words (সকাল/দুপুর/বিকেল/সন্ধ্যা/রাত).
- The BN condition must remain predominantly Bengali script (validator: at least 55% of letters).

## BN-CS: Bengali-matrix professional code-switching

The target is how a Bengali-speaking IT or office professional actually writes in a chat or ticket: Bengali grammar, with English for the domain vocabulary.

- **Bengali stays the matrix language.** Postpositions, case endings, verb inflection, negation, question words, connectives and discourse markers remain Bengali. The prompt must never read as English with a Bengali wrapper.
- **What switches into English (Latin script):**
  - domain and technical nouns and noun phrases: `user profile`, `service account`, `production workflow`, `false alarm`, `escalation criteria`, `deadline`, `stakeholder`, `response rate`
  - professional verbs, as an English stem plus a Bengali light verb: `check করুন`, `install করা`, `restart করার পর`, `prioritize করবেন`, `rollback করা`, `explain করুন`
  - occasional English adjectives and adverbs that professionals use naturally: `critical`, `temporary`, `manually`
- **Switch consistently.** If a term switches once, it switches everywhere in that prompt. The key domain term of a task must switch, because that is what real code-switching does; leaving it as a Bengali calque defeats the condition.
- **Typical density:** roughly 25–45% of word tokens in English, and never more than about half; task-list-heavy technical prompts sit at the top of that range. Generic vocabulary stays Bengali even when domain terms switch (কারণ, প্রমাণ, পরিকল্পনা, স্বাভাবিকভাবে, সম্ভাব্য). The validator separately requires a Bengali share of letters between 0.25 and 0.985.
- **Morphology at the script boundary.** Bengali suffixes attach to an English word with a hyphen and follow the word's *pronunciation*:

  | Word ends in | Genitive | Locative | Examples |
  |---|---|---|---|
  | a consonant sound (includes silent final *e*) | `-এর` | `-এ` | `user-এর`, `file-এ`, `server-এ`, `software-এর` |
  | a vowel sound | `-র` | `-তে` | `policy-র`, `data-তে`, `Wi-Fi-তে`, `review-র`, `SSD-তে` |

  Plurals take `-গুলো` (things) or `-দের` (people): `file-গুলো`, `user-দের`. Never attach a Bengali vowel sign directly to a hyphen (`impact-িত`), and never split a Bengali word around an English fragment (`প্রো file`).
- **Numbers:** BN-CS uses the same Bengali digits as BN. This keeps numeral script from confounding the BN vs BN-CS contrast.
- **Same facts and order:** BN-CS is written in parallel with BN, sentence by sentence, so that only code choice differs.

## English

English is the canonical specification. Corpus v0.3 left all English prompts byte-identical to v0.2. Corpus v0.3.1 changes only SYN079, replacing an ambiguous deadline phrase with an explicit equivalent of the already validated Bengali and BN-CS wording. That versioned clarification is recorded in `CORPUS_CHANGELOG.md`.

## Review status

v0.3 realizations were drafted with AI assistance (Claude) under this guide, then validated by human validator R1 and approved and frozen by the study lead on 2026-10-18 (`data/annotations/review_logs/2026-10-18_R1_human_validation.md`). The corpus is frozen at v0.3.1; this guide governs any future versioned release.
