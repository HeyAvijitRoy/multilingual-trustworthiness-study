# Prompt corpus (v0.3.1, frozen)

500 tasks, each written in three matched language conditions, for 1,500 prompts. The conditions differ in language and code choice only.

| Condition | Column | Description |
|---|---|---|
| EN | `prompt_en` | Canonical English specification |
| BN | `prompt_bn` | Natural contemporary Bengali |
| BN-CS | `prompt_bn_cs` | Bengali-English code-switching with Bengali as the matrix language |

## Files and columns

Ten CSV files, two per domain (`<domain>_001_050.csv`, `<domain>_051_100.csv`). `manifest.csv` lists them. Every file has exactly these columns:

| Column | Values |
|---|---|
| `task_id` | `TECH001`–`TECH100`, `CYBER001`–`CYBER100`, `PROC001`–`PROC100`, `DEC001`–`DEC100`, `SYN001`–`SYN100` |
| `domain` | `technical_troubleshooting`, `cybersecurity_digital_safety`, `procedural_instructional`, `decision_support`, `information_synthesis` |
| `subdomain` | Task family within the domain. `SYN091`–`SYN100` are `extended_context`. |
| `difficulty` | `easy` / `medium` / `hard`, exactly 25 / 50 / 25 per domain |
| `prompt_en`, `prompt_bn`, `prompt_bn_cs` | The three conditions |

Difficulty reflects task structure:
- **Easy:** one objective with little interaction between constraints.
- **Medium:** several factors, steps or evidence elements must be integrated.
- **Hard:** several interacting constraints, dependencies, uncertainties or trade-offs must be reconciled while keeping important caveats.

The extended-context subset (`SYN091`–`SYN100`) has much longer prompts with multiple facts, dependencies and caveats. It tests information retention under dense context.

Annotations are stored separately, in `data/annotations/`. Prompt text never carries scoring metadata.

## What stays fixed across conditions

- **Content:** task objective, facts, numbers, comparators, time windows and caveats.
- **Instructions:** explicit constraints and output requirements (sentence counts, "concise", "table", "step by step", "safest", "first").
- **Register:** polite second person (আপনি) with imperatives (`করুন`, `দিন`, `লিখুন`) in both Bengali conditions.
- **Clause order,** wherever Bengali grammar allows.

Neither Bengali condition adds hints, examples, glosses or emphasis that EN lacks, or drops any that EN has. Quantifiers and superlatives carry over exactly: "safest" → `সবচেয়ে নিরাপদ`, "at least" → `অন্তত`. Where the English is ambiguous, the Bengali keeps the ambiguity rather than resolving it.

## BN: natural contemporary Bengali

- **Variety:** standard colloquial written Bengali (চলিত রীতি), following Bangladeshi usage where varieties differ (পানি, not জল).
- **Native vocabulary** where an educated reader would use it: ব্যবহারকারী, অগ্রাধিকার, সময়সীমা, ঝুঁকি, প্রমাণ.
- **Technical loanwords** are written in Bengali script, not calqued: ল্যাপটপ, পাসওয়ার্ড, ব্যাকআপ, সার্ভিস অ্যাকাউন্ট, ক্লোন, ক্র্যাশ, ওয়ার্নিং, এরর.
  - Sanskritized coinages a technical reader would not recognize are not used.
  - Latin script appears only in single-letter labels copied from EN (Group A, Model X).
- **Acronyms** use Bengali script when common (এসএসডি, ভিপিএন). On-screen identifiers stay exactly as in EN: error codes, file names, paths.
- **Numbers** use Bengali digits. Clock times use Bengali time-of-day words (সকাল, দুপুর, বিকেল, সন্ধ্যা, রাত).
- **Spelling conventions:** হেল্‌থ চেক (hasanta + ZWNJ), ওয়ার্নিং.

Calques removed in v0.3, with the term now used:

| Avoid | Use | Concept |
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

## BN-CS: Bengali-matrix professional code-switching

This condition reflects how a Bengali-speaking IT or office professional writes in a chat or ticket: Bengali grammar, with English domain vocabulary.

- **Bengali stays the matrix language.** Postpositions, case endings, verb inflection, negation, question words and connectives remain Bengali.
- **What switches into Latin-script English:**
  - domain nouns: `service account`, `production workflow`, `false alarm`, `deadline`;
  - professional verbs, as an English stem plus a Bengali light verb: `check করুন`, `restart করার পর`, `prioritize করবেন`;
  - occasional adjectives such as `critical` or `temporary`.
- **Switching is consistent within a prompt.** The key domain term of a task always switches.
- **Density:** typically 25–45% of word tokens are English, never more than about half. Generic vocabulary stays Bengali.
- **Suffixes** attach with a hyphen and follow the English word's pronunciation:

  | Word ends in | Genitive | Locative | Examples |
  |---|---|---|---|
  | consonant sound (including silent final *e*) | `-এর` | `-এ` | `user-এর`, `file-এ`, `server-এ` |
  | vowel sound | `-র` | `-তে` | `policy-র`, `data-তে`, `SSD-তে` |

  Plurals take `-গুলো` (things) or `-দের` (people). A Bengali vowel sign never attaches to a hyphen, and a Bengali word is never split around an English fragment.
- **Numbers** use Bengali digits, as in BN, so numeral script does not confound the BN vs BN-CS contrast.
- **Construction:** BN and BN-CS were hand-written in parallel, sentence by sentence.

## Version history

| Version | Date | Change |
|---|---|---|
| v0.2 | 2026-09-24 | Initial 500-task design: difficulty rebalance, extended-context expansion. BN-CS was generated by lexicon substitution. |
| v0.3 | 2026-10-18 | BN and BN-CS hand-rewritten for all 500 tasks; English unchanged. |
| v0.3.1 | 2026-10-18 | SYN079 English clarified. Frozen evaluation corpus. |

**Why v0.3.** Lexicon substitution in v0.2 caused four kinds of problem:
- **Broken grammar:** malformed BN-CS such as `impact-িত` and `প্রো file`, about 30 wrong genitives, and a Devanagari letter in SYN021.
- **Changed meaning:** "conclusion" became `decision` in 8 synthesis tasks.
- **Misleading calques:** for example, "software corruption" rendered as *bribery*, and "storage bucket" as *pail*.
- **Thin code-switching:** BN-CS had a median English word share of only 8%.

v0.3 fixed these issues and added the automated guards described below. No model responses existed at the time of any change.

| BN-CS English word share | v0.2 | v0.3 |
|---|---:|---:|
| Median | 0.083 | 0.375 |
| Interquartile range | 0.048–0.120 | 0.320–0.429 |
| Maximum | 0.270 | 0.531 |

**Why v0.3.1.** In SYN079, "the deadline is the following Friday" could mean either of two Fridays. Under one reading the plan is feasible; under the other it is not. The English now says "Friday of the following week", matching the Bengali conditions, so the correct answer is the same in all three languages. No annotation changed.

## Automated checks

`python3 scripts/01_validate_inputs.py` checks:

- **Structure:** IDs, columns, domain counts, difficulty allocation, the extended-context subset and duplicates.
- **Bengali conditions:**
  - every EN number appears in BN and BN-CS;
  - no parentheticals absent from EN;
  - no Latin-script words in BN beyond single-letter labels;
  - no non-Bengali Indic characters;
  - none of the deprecated calques.
- **BN-CS:**
  - script-boundary hyphenation and pronunciation-matched suffixes;
  - Bengali-script share between 0.25 and 0.985;
  - English word share at most 0.6.
