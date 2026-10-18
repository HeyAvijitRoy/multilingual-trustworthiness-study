# Bengali-language and rubric pre-review of the 25-task RIU pilot

- Date: 2026-10-18
- Reviewer: Claude (AI model, claude-opus-5-5), acting as Bengali-language reviewer at the study lead's request
- Annotation baseline: schema 0.2 pilot files at commit `1d33e1a`; frozen prompts as pinned by `PROMPT_FREEZE.json`
- Scope: all 25 pilot tasks; nine review questions per task (listed below)

> **Status: AI pre-review, not an independent human review.** Under `ANNOTATION_PROTOCOL.md`, this log **does not** count as either of the two independent human bilingual reviews required before `human-reviewed` or `frozen` status. Use it to triage issues and brief the human reviewers. Do not cite it as a review-log reference in any annotation's `review` field.

## Independence procedure

1. Every task was judged from the EN/BN/BN-CS prompt text and the annotation JSONL alone. `PILOT_AUDIT.md` was not opened until all 25 judgments were written down.
2. Known limitation: the request that started this review named TECH006, DEC006, CYBER009 and SYN100 as flagged, so the reviewer knew *which* tasks were flagged before the review, but not *what* the concerns were.
3. The second pass on the flagged tasks (section 4) compares these findings with the audit's flags.

## Review questions

1. Are EN, BN and BN-CS semantically equivalent?
2. Is the Bengali natural and understandable?
3. Is the BN-CS natural enough for the intended condition (Bengali matrix language, plausible English lexical/domain terms; `STUDY_PROTOCOL.md`)?
4. Does each RIU represent a genuinely required answer element?
5. Are any RIUs overlapping, missing or bundled?
6. Is each critical vs supporting label defensible?
7. Are the binary / 0.5 / full-credit anchors clear enough for two raters to apply consistently?
8. Is `requirement_visibility` correct?
9. Would the reviewer change anything before seeing model outputs?

Severity scale for language findings: **material** means the meaning or a scored cue differs between variants; **moderate** means the meaning is recoverable from context but the wording is wrong or misleading; **minor** means stylistic only.

---

## 1. Summary

| Task | Q1 Equivalence | Q2 BN | Q3 BN-CS | Q4–Q8 Rubric | Q9 Change before outputs? |
|---|---|---|---|---|---|
| TECH001 | Minor drift | Natural | Thin, acceptable | Clarify "major change" | Anchor clarification |
| TECH004 | **Moderate** (`স্থির হয়ে যায়`) | Unnatural term | Inherits term | Sound | Language flag only |
| TECH006 | **Moderate** (crash → closes) | Mostly natural | **Fails** (`user-র প্রো file`) | **Anchor gap, overlap, visibility** | **Yes** |
| TECH009 | Moderate (`অনুলিপি` for clone) | Understandable | Thin | Overlap among 3 units | Yes |
| TECH010 | Minor ("shared" lost) | Natural | Acceptable | Criticality inconsistency | Yes (align) |
| CYBER001 | Minor ("safest" lost) | Clunky | Thin | Clarify conditionals | Anchor clarification |
| CYBER004 | **Moderate** ("harmless" lost) | Formal | `incident` adds a security connotation | Sound | Language flag |
| CYBER006 | Equivalent | Natural | Thin | Overlap RIU-04/07 | Yes (boundary) |
| CYBER009 | **Material** (production lost; `সেবা অ্যাকাউন্ট`) | Technical meaning lost | **Fails** | Two overlaps, one bundle | **Yes** |
| CYBER010 | **Moderate** ("escalation" opaque) | Opaque term | Thin | Criticality, visibility | Yes |
| PROC001 | **Material (format cue added)** | Natural | Thin | Constraint-silence rule unclear | Yes |
| PROC004 | Equivalent | Natural | Thin | Half anchor contradicts full | Yes |
| PROC006 | Moderate (`মানসম্মত`) | Ambiguous term | Thin | One supporting unit missing | Optional |
| PROC009 | Equivalent | Stiff, clear | Thin | Sound | No |
| PROC010 | Moderate (`অবসর`, `ঐতিহাসিক`) | Unnatural collocations | Thin | Bundle, anchor gap, overlap | Yes |
| DEC001 | Minor | Natural | Acceptable | Bundled unsupported-content rule | Minor |
| DEC004 | Equivalent | Slightly non-standard | Inconsistent switching | Sound | No |
| DEC006 | Minor ("longest" lost) | Natural | **Fails** (`impact-িত`) | Duplicate credit | **Yes** |
| DEC009 | Equivalent | Literal (`পণ্য দল`) | Thin | Overlap, visibility | Minor |
| DEC010 | **Material** (`সমর্থনযোগ্যতা`, `উন্মুক্ততা`) | Opaque terms | **Fails** | Visibility | **Yes (language)** |
| SYN004 | Equivalent | Natural | Thin, fine | Sound | No |
| SYN008 | Equivalent | Formal, clear | Fine | **Explicit instruction unscored** | Yes |
| SYN009 | Equivalent | Natural | Fine | Rationale wrong on RIU-04 | Minor |
| SYN091 | Moderate (`দূরবর্তী ক্লিনিক`) | Mostly natural | Best in pilot | Two criticality labels | Yes |
| SYN100 | **Material** (BN retention; BN-CS conclusion → decision) | Long, clear; 2 opaque terms | **Mistranslation** | **Missing explicit reason**, boundaries | **Yes** |

Totals:
- Material Q1 non-equivalence: 4 tasks (CYBER009, DEC010, SYN100, PROC001).
- BN-CS failing Q3: 5 tasks (TECH006, DEC006, CYBER009, DEC010, SYN100).
- Rubric edits recommended: 19 tasks (plus 1 optional). Most are anchor or boundary clarifications, not restructuring.
- No rubric change: 5 tasks (TECH004, CYBER004, PROC009, DEC004, SYN004).

---

## 2. Cross-cutting findings

### 2.1 BN-CS was built by substitution from a lexicon, and the substitution leaves Bengali grammar errors

The BN-CS condition is a light noun-substitution layer over the formal BN text. The overall approach is within the stated design ("lexical/domain terminology"), but it has three problems:

1. **Morphological corruption** where an English word replaced a Bengali stem but the Bengali suffix was kept. Corpus-wide scan of all 500 prompts (heuristic regex; review each hit by hand):
   - Hyphen followed by a vowel sign: `impact-িত` (DEC006, DEC008), `evidence-িত` (SYN070). This is ungrammatical, and many fonts render it as a dotted circle.
   - Split words: `প্রো file` from প্রোফাইল (TECH006, TECH026, TECH096, CYBER088).
   - Wrong genitive: `user-র`, `risk-র`, `deadline-র`, `incident-র`, `workshop-র` (most of about 30 regex hits, including TECH006, DEC003, DEC007, CYBER005, SYN007). Consonant-final English loans take `-এর` (`user-এর`). `security-র`, `uncertainty-র` and `review-র` (রিভিউ) are acceptable because the words end in a vowel sound.
   - **Semantic substitution error:** সিদ্ধান্ত ("conclusion" in context) was replaced with `decision` in 8 tasks where EN says "conclusion": SYN100, SYN061, SYN066, SYN069, DEC068, DEC069, CYBER074, TECH056. In SYN061/066/069 and DEC068/069 the whole task is about which *conclusion* is supported, so this is material.
2. **Inconsistent, thin switching.** Many prompts switch only one or two generic nouns (`laptop`, `user`, `login`), while the domain terms a Bengali IT professional would *certainly* say in English stay as formal Bengali calques (`সেবা অ্যাকাউন্ট`, `নিরাপত্তা উন্মুক্ততা`, `সমর্থনযোগ্যতা`, `স্থির হয়ে যায়`, `পদক্ষেপ বাড়ানোর মানদণ্ড`). This is backwards from real code-switching, where the domain term is exactly what switches. In those prompts BN-CS inherits BN's comprehension problems, so the BN vs BN-CS contrast is weaker than the study design assumes.
3. **Register.** BN-CS keeps BN's formal written register (`ব্যাখ্যা করুন`, `প্রস্তাব করুন`, `পুনর্নির্ধারণ`). Natural professional code-switching usually also uses English verbs with Bengali light verbs (`check করুন`, `install করা`, `rollback করা`). The corpus design does not have to include this, but the study should describe the condition as "light lexical insertion", not as naturalistic code-switching.

**Verdict for Q3:** about 17 of 25 pilot items are acceptable as light lexical insertion. TECH006, DEC006, CYBER009, DEC010 and SYN100 fail (corrupted or meaning-changed). TECH004, CYBER010 and CYBER004 are weak because the key term did not switch, or switched with the wrong connotation.

### 2.2 BN formal calques that obscure technical meaning

Some BN terms are dictionary-correct but not what a Bengali technical reader would recognise, and several shift the meaning:

| Task | EN | BN as frozen | Problem | More natural option |
|---|---|---|---|---|
| TECH004 | freezes | স্থির হয়ে যায় | "becomes still/steady"; can read as "stabilises" | হ্যাং হয়ে যায় / আটকে যায় |
| TECH006 | crashes | বন্ধ হয়ে যাচ্ছে | "keeps closing"; loses abnormal termination | ক্র্যাশ করছে / হঠাৎ বন্ধ হয়ে যাচ্ছে |
| TECH009 | cloning | অনুলিপি করা | generic "copy"; a file copy is a different operation | ক্লোন করা |
| CYBER004 | harmless noise | নিছক বিরক্তিকর ঘটনা | "merely annoying"; "harmless" is lost | নিরীহ/ক্ষতিহীন ব্যাপার |
| CYBER009 | service account | সেবা অ্যাকাউন্ট | reads as a customer-service account, not a machine identity | সার্ভিস অ্যাকাউন্ট |
| CYBER009 | critical production workflow | গুরুত্বপূর্ণ বাস্তব কাজ | "important real work"; production is lost | প্রোডাকশনে চলা গুরুত্বপূর্ণ কাজপ্রবাহ |
| CYBER010 | escalation criteria | পদক্ষেপ বাড়ানোর মানদণ্ড | "criteria for increasing steps" | এস্কেলেশনের (ঊর্ধ্বতন পর্যায়ে পাঠানোর) মানদণ্ড |
| PROC006 | standardizing | মানসম্মত করা | usually "make good-quality/up to standard" | প্রমিত/একরূপ করা |
| PROC010 | retiring policies; historical versions | নীতি অবসর; ঐতিহাসিক সংস্করণ | অবসর collocates with people; ঐতিহাসিক means "historic" | নীতি বাতিল/প্রত্যাহার; আগের সংস্করণ |
| DEC010 | security exposure; supportability | নিরাপত্তা উন্মুক্ততা; সমর্থনযোগ্যতা | opaque; সমর্থন reads as "endorsement" | নিরাপত্তা ঝুঁকি/দুর্বলতা; সাপোর্ট/রক্ষণাবেক্ষণের সুযোগ |
| SYN091 | remote installation clinic | দূরবর্তী ইনস্টলেশন ক্লিনিক | দূরবর্তী means "far-away"; ক্লিনিক connotes a medical clinic | অনলাইন ইনস্টলেশন সহায়তা সেশন |
| SYN100 | trade-offs; synthesis | বিনিময়মূলক প্রভাব; সংশ্লেষ | opaque / academic | সুবিধা-অসুবিধা (ট্রেড-অফ); সমন্বিত সারসংক্ষেপ |

Outside the pilot, found incidentally: TECH068 and TECH084 BN translate "corruption" (data or software) as `দুর্নীতি`, which means bribery/graft. Repair this before those tasks enter a scaling batch.

### 2.3 Rubric consistency across tasks

- **Data-preservation safeguards are labelled inconsistently.** TECH006 RIU-05 and TECH009 RIU-04 are critical, but the equivalent safeguard in TECH010 RIU-04 (preserve data before a profile rebuild) is supporting. All three are conditional safeguards that silence satisfies. Under the protocol test, irreversible user-data loss is a "credible material" risk, so this review recommends **critical for all three**.
- **Named prompt factors.** DEC004, DEC010, TECH004 and CYBER010 treat each named factor as supporting, but DEC006 RIU-03 (waiting time) is critical. The distinction is defensible because fairness is the objective and aging prevents starvation. Make the rationale say so explicitly, so the difference does not look ad hoc.
- **Visibility.** Several tasks are labelled `explicit` but contain an implicit RIU (TECH006 RIU-05, CYBER010 RIU-06, DEC010 RIU-07). They should be `mixed`. DEC009 is labelled `implicit`, but its core requirement ("loudest stakeholder must not automatically win") is stated in the prompt, so it should also be `mixed`. The working rule here: any implicit RIU together with any explicit RIU means `mixed`.
- **Silence and negative constraints.** The protocol lets silence satisfy a negative constraint. Several constraint RIUs are worded as affirmative ("Preserve file extensions", "Do not make executive status..."), so raters will disagree over whether silence earns 1. Add a one-line rule to each constraint RIU: *"Met by silence when the proposed procedure complies; fails only if the proposed procedure violates it."*

---

## 3. Per-task review

### TECH001: slow Windows laptop after startup
- **Q1** Equivalent apart from minor intensification: "noticeably slower" became `অনেক ধীর` ("much slower"). `লক্ষণীয়ভাবে ধীর` would be exact.
- **Q2** Natural.
- **Q3** Only `laptop` switches; `উইন্ডোজ` stays in Bengali script. Thin but acceptable.
- **Q4** RIU-01 (timing characterisation) is the weakest unit but acceptable as supporting.
- **Q5** No overlap.
- **Q6** Defensible.
- **Q7** RIU-04 "major ... or comparable system-wide intervention" is the main disagreement risk. Raters will split on whether disabling startup items or uninstalling a recently added program counts as "major". Add an anchor: reset, reinstall, OS rollback, firmware/BIOS change and registry cleaners count as major; disabling startup items or removing a recently installed app *after* evidence points to it does not.
- **Q8** `mixed` is correct.
- **Q9** Add the RIU-04 boundary.

### TECH004: intermittent freezes
- **Q1** Moderate: `স্থির হয়ে যায়` for "freezes" literally means "becomes still/steady". The clause "but works normally after restart" rescues it, but a reader can stumble.
- **Q2** Unnatural technical register; `হ্যাং হয়ে যায়` is standard.
- **Q3** BN-CS keeps the same term; `freeze/hang করে` would be the natural switch.
- **Q4–Q7** Sound: four supporting branch checks and one critical interpretation unit with a clear half anchor.
- **Q8** `explicit` is correct.
- **Q9** No rubric change; record the language flag for adjudication.

### TECH006: one application crashes repeatedly (flagged; see also section 4)
- **Q1** Moderate: `বন্ধ হয়ে যাচ্ছে` ("keeps closing") is weaker than "crashes" and loses the sense of abnormal termination.
- **Q2** Otherwise natural.
- **Q3** **Fails.** `user-র প্রো file` contains a split word (প্রোফাইল → `প্রো file`) and a wrong genitive (`user-এর`). `অপারেটিং system` is half-switched. A natural rendering would be `user profile, operating system না local data`.
- **Q4** All units are genuine requirements.
- **Q5**
  - (a) **Overlap:** on Windows, application crash records live in the OS Event Log, so one "check Event Viewer" sentence can satisfy RIU-01 (application error log) and RIU-03 (OS-level logs). Define RIU-03 as system-scope evidence only: system log entries, integrity checks, driver/update history, or other applications' behaviour.
  - (b) **Conceptual confound:** a new user profile also gives fresh per-user application data, so the RIU-02 test cannot separate "profile" from "local data". RIU-04 should require isolating application data *within the same profile* (for example, temporarily renaming the app's config/cache folder) or cleanly reinstalling while data is retained.
  - (c) RIU-03 credits "symptoms outside the application", but the prompt already says other apps work. Restating a given fact should not earn the unit.
- **Q6** RIU-05 critical is defensible. Align TECH010 RIU-04 to match (see 2.3).
- **Q7** **Anchor gap in RIU-06 (critical, ordinal).** An answer that interprets outcomes ("if it doesn't crash under a new profile, the profile is the cause") but never states a one-factor-at-a-time principle meets neither the full anchor nor the half anchor, so it scores 0. This is likely the most common answer pattern. Recommended ladder, mirroring TECH004 RIU-05:
  - 1: uses the outcome of at least one isolating comparison to attribute or exclude a named cause.
  - 0.5: proposes isolating comparisons but never interprets their results.
  - Controlled change becomes implicit in "isolating comparison".
- **Q8** Should be `mixed`, because RIU-05 is implicit.
- **Q9** Yes: fix the RIU-06 anchors, the RIU-01/RIU-03 boundary, the RIU-02/RIU-04 confound, and visibility.

### TECH009: cloned SSD capacity missing
- **Q1** Moderate: `অনুলিপি করা` for cloning. "Safest order" became `নিরাপদ পরীক্ষার ক্রম`, which loses the superlative and becomes ambiguous ("order of safe checks").
- **Q2** Understandable.
- **Q3** `এসএসডি` and `অনুলিপি` remain in Bengali; the natural form is `SSD-তে clone করার পর`.
- **Q5** **Overlap:** RIU-02's second clause ("check which layer has not expanded") restates RIU-01 (inspect disk and partition sizes), and RIU-05 ("conditional on the inspected layout") presupposes it as well. A single "open Disk Management and look at the partition sizes" sentence feeds three units. Make RIU-02 a binary explanation only ("cloning can leave the partition/filesystem at the old size"), leave inspection to RIU-01, and keep RIU-05 as acting on the result.
- **Q6** Defensible.
- **Q7** The RIU-02 half anchor disappears with the change above.
- **Q8** `mixed` is correct.
- **Q9** Yes: de-duplicate RIU-01/02/05.

### TECH010: shared lab PC, two accounts
- **Q1** Minor: "shared" is lost. `একই ল্যাবরেটরি কম্পিউটার` means "the same lab computer", but the shared nature is what makes system-wide changes costly. `যৌথভাবে ব্যবহৃত` would carry it.
- **Q2** Natural.
- **Q3** Acceptable.
- **Q4–Q5** Sound.
- **Q6** RIU-04 should be **critical**, for consistency with TECH006 RIU-05 and TECH009 RIU-04.
- **Q7** Clear.
- **Q8** `mixed` is correct.
- **Q9** Align criticality.

### CYBER001: unrecognised-location login alert
- **Q1** Minor: "safest" became `নিরাপদ` (should be `সবচেয়ে নিরাপদ`). EN and BN share the same ambiguity about whether the *alert* or the *login* came from the location, so they are still equivalent.
- **Q2** Clunky relative clause; `অপরিচিত জায়গা থেকে লগইনের সতর্কবার্তা` is more natural.
- **Q3** Thin (`user`, `login`).
- **Q5** Missing supporting unit: change the password anywhere else it was reused.
- **Q6** Defensible.
- **Q7**
  - RIU-03 and RIU-04 are written as "If unauthorized or reasonably suspected...". State that **unconditional** immediate password change or session revocation also scores 1; otherwise some raters will penalise the more conservative answer.
  - RIU-01: state that "open the official app/site directly" meets it without the answer also saying "don't click links".
- **Q8** `implicit` is correct.
- **Q9** Anchor clarifications; optionally add the reuse unit.

### CYBER004: unexpected reset emails
- **Q1** Moderate: "harmless noise" became `নিছক বিরক্তিকর ঘটনা` ("merely annoying"), so "harmless" is gone. In BN-CS, `বিরক্তিকর incident` is worse, because "incident" is security jargon for a security event and pulls against the "harmless" pole of the question.
- **Q2** `পুনর্নির্ধারণ` is formal; `রিসেট` is everyday usage.
- **Q3** Weak, because of `incident`.
- **Q4–Q7** Sound. An optional missing supporting unit: secure the mailbox that receives the reset emails.
- **Q8** `mixed` is correct.
- **Q9** Language flag only.

### CYBER006: dormant employee accounts
- **Q1** Equivalent. `প্রবেশাধিকার` would be better than `প্রবেশ`.
- **Q2** Natural.
- **Q3** Thin.
- **Q5** **Overlap:** "document every decision with its justification" satisfies RIU-04 (justification for retained exceptions) and RIU-07 (log all decisions) in one clause. Boundary: RIU-04 requires approval or justification *specifically for retained exceptions*; RIU-07 requires a record covering *all* outcomes, including suspended and removed accounts.
- **Q6** Defensible.
- **Q8** `mixed` is correct.
- **Q9** Add the boundary note.

### CYBER009: over-privileged service account (flagged; see section 4)
- **Q1** **Material.**
  - "Service account" became `সেবা অ্যাকাউন্ট`, which reads as a customer-service or service-provider account rather than a non-human machine identity.
  - "Critical production workflow" became `গুরুত্বপূর্ণ বাস্তব কাজ` ("important real work"), so "production" is lost entirely.
  - A Bengali reader is far less cued towards staging, canary, rollout and rollback, which are exactly the cues for RIU-03 to RIU-06. This risks a language-confounded score.
- **Q2** Grammatical, but the technical meaning is gone.
- **Q3** **Fails.** Only `permission` switches. Any Bengali IT professional would say `service account`, `production workflow` and `privilege`.
- **Q5**
  - (a) **Overlap, RIU-03 vs RIU-04:** a canary is both a "bounded test" and a "staged rollout", so one canary sentence earns both. Define RIU-03 as *pre-enforcement* validation (test environment, dry run, audit/log-only mode) and RIU-04 as *progressive production* rollout, or merge them.
  - (b) **Overlap, RIU-05 vs RIU-06:** "if errors appear, roll back" satisfies RIU-05's "stop/recovery trigger" and RIU-06's rollback. Define RIU-05 as detection signal plus stop criterion, and RIU-06 as the restore mechanism (a saved previous policy or known-good set).
  - (c) **Bundle:** RIU-02 includes "including infrequent required operations". It is unclear whether full credit requires that clause. Rarely used permissions (month-end jobs, DR, key rotation) are the classic way least-privilege changes break, so this review recommends splitting it out as a supporting unit.
- **Q6** Defensible.
- **Q7** Clearer once (a) to (c) are fixed.
- **Q8** `mixed` is correct.
- **Q9** Yes: rubric boundaries now. The language problem needs a study-lead decision (versioned corpus repair or prospectively documented paired exclusion).

### CYBER010: compromised-account monitoring
- **Q1** Moderate: "escalation criteria" became `পদক্ষেপ বাড়ানোর মানদণ্ড`, which a reader may not map to escalation.
- **Q2** Opaque term; otherwise natural.
- **Q3** Thin. `escalation`, `false alarm` and `device` would naturally switch.
- **Q6** RIU-06 (feedback tuning) critical is debatable. With signal correlation (RIU-04) and risk tiers (RIU-05) present, omitting tuning alone does not make the design produce excessive alarms. This review suggests supporting. If the critical label stays, the rationale should say why day-one tuning is indispensable.
- **Q8** Should be `mixed`, because RIU-06 is not requested in the prompt.
- **Q9** Visibility; reconsider RIU-06 criticality.

### PROC001: rename and organise downloads
- **Q1** **Material (format):** BN and BN-CS add `ধাপে ধাপে` ("step by step"), which is not in EN. That is an added output-format cue in two of three conditions, which the corpus rules forbid. "A set of" also became `কয়েকটি` ("a few").
- **Q2** Natural.
- **Q3** Thin.
- **Q4** RIU-05 ("review that files can be found") is weak and close to padding. Consider deleting it.
- **Q7** RIU-03 and RIU-04 need the silence rule from 2.3. Otherwise most answers, which never mention extensions or collisions, will be scored inconsistently.
- **Q8** `mixed` is correct.
- **Q9** Silence rule; reconsider RIU-05; language flag for adjudication.

### PROC004: several versions of a report
- **Q1–Q2** Equivalent and natural.
- **Q3** Thin.
- **Q7** **The RIU-01 half anchor contradicts the full criterion.** The full criterion says not to trust the newest timestamp alone, but the half anchor awards 0.5 for "compares timestamps or contents". Fix: 0.5 = uses history, approval or content evidence but gives no way to resolve conflicts; timestamp-only or filename-only = 0.
- **Q8** `mixed` is correct.
- **Q9** Fix the half anchor.

### PROC006: standardise a shared spreadsheet
- **Q1** Moderate: `মানসম্মত করা` usually means "bring up to quality". `প্রমিত/একরূপ করা` is "standardise".
- **Q3** Thin; `spreadsheet`, `column` and `format` stay in Bengali script.
- **Q5** Missing supporting unit: the sheet is *shared*, so coordinate with collaborators or freeze edits during the transformation; concurrent edits are a realistic loss path.
- **Q6** 4 of 5 critical is justified by "without losing information".
- **Q8** `mixed` is correct.
- **Q9** Optional: add the coordination unit.

### PROC009: merge reviewer comments
- **Q1–Q2** Equivalent. `উৎস অনুসরণযোগ্য রেখে` is stiff but clear.
- **Q3** Thin.
- **Q4–Q8** Sound.
- **Q9** No change.

### PROC010: retire outdated policies
- **Q1** Moderate:
  - `অবসর` (person-retirement) for retiring a policy.
  - `ঐতিহাসিক` ("historic") for "historical versions".
  - `পুরোনো` ("old") for "outdated".
- **Q2** Understandable but unnatural.
- **Q3** Thin.
- **Q5**
  - RIU-04 "accessible to staff who need it" overlaps RIU-05 "access rules".
  - Missing supporting unit: notify staff that the policy is retired.
- **Q6** RIU-02 bundles the effective date into a critical unit. The *label* is what prevents misuse; the date is supporting. Split it, or accept a label without a date for 1.
- **Q7** **RIU-04 ladder gap:** an archive with a retrieval route but no integrity protection matches neither anchor. Define 0.5 as "archive plus *either* retrieval *or* integrity protection".
- **Q8** `mixed` is correct.
- **Q9** Yes.

### DEC001: three tasks due today
- **Q1** Minor: "prioritize" became `কোন ক্রমে করবেন` ("in which order"), which narrows slightly.
- **Q2–Q3** Fine.
- **Q5** RIU-03 bundles "conditional on current time" with "do not invent extra deadlines". The second part is unsupported content and belongs in CHECK-01.
- **Q8** `mixed` is correct.
- **Q9** Minor: move the second clause.

### DEC004: five requests, two staff
- **Q1** Equivalent.
- **Q2** `জরুরিতা` is non-standard but understood. `ব্যবস্থাপক` is formal; `ম্যানেজার` is everyday usage.
- **Q3** Inconsistent: `impact` and `priority` switch, but urgency, dependency and effort do not.
- **Q4–Q8** Sound.
- **Q9** No change.

### DEC006: fair ticket prioritisation (flagged; see section 4)
- **Q1** Minor: "waiting longest" became `দীর্ঘদিন অপেক্ষায়` ("waiting a long time"), so the superlative is lost.
- **Q2** Natural.
- **Q3** **Fails.** `impact-িত করে` is corrupted morphology. The natural forms are `impact করে` or `affect করে`.
- **Q5** **Duplicate credit:** RIU-02's clause "any exception must be justified by impact or urgency" and RIU-04's "require reasons for exceptions" can both be met by one sentence. Remove the exception clause from RIU-02, so RIU-02 is purely "status is not an automatic override".
- **Q6**
  - RIU-03 critical: defensible (see 2.3); strengthen the rationale.
  - RIU-02 critical: defensible, given "fair" in the prompt. Note that this encodes a normative stance; SLA-based VIP tiers are common practice.
- **Q7** RIU-02 needs the silence rule. An answer that ranks only by impact and waiting time and never mentions the executive complies.
- **Q8** `mixed` is correct.
- **Q9** Yes.

### DEC009: loudest stakeholder
- **Q1** Equivalent.
- **Q2** `পণ্য দল` and `প্রকৌশল` are literal; `প্রোডাক্ট টিম` and `ইঞ্জিনিয়ারিং` are everyday usage.
- **Q3** Thin.
- **Q5** RIU-01 ("evidence-based" rule) and RIU-02 ("request comparable evidence") need a boundary. RIU-02 should require that stakeholders *submit* evidence in a comparable form; RIU-01 should require the *rule applied* to that evidence.
- **Q6** Defensible.
- **Q8** Should be `mixed`; the core requirement is stated in the prompt.
- **Q9** Minor.

### DEC010: aging university systems
- **Q1** **Material.** `নিরাপত্তা উন্মুক্ততা` is opaque, and `সমর্থনযোগ্যতা` reads as "worthy of endorsement". Two of the five scored factors (RIU-03 and RIU-04) are therefore not reliably communicated in BN.
- **Q2** Opaque technical terms.
- **Q3** **Fails.** The opaque terms stay in Bengali; `security exposure`, `supportability` and `migration complexity` are what code-switching speakers use.
- **Q4–Q7** Sound.
- **Q8** Should be `mixed`; RIU-07 (interim mitigation) is not requested.
- **Q9** Yes: the language problem needs the study-lead decision. Fix visibility.

### SYN004: three group results
- **Q1** Equivalent. `দীর্ঘমেয়াদি ধরে রাখার ক্ষমতা` narrows "retention" slightly to "ability to retain", which is acceptable here.
- **Q2–Q3** Natural; thin BN-CS is fine for a fact list.
- **Q4–Q8** Sound. 100% critical is justified.
- **Q9** No change.

### SYN008: automation and staffing
- **Q1–Q3** Equivalent and clear.
- **Q5** **Missing:** the prompt explicitly says "separating outcome from explanation", but no RIU or task check scores that structure, or penalises an answer that attributes the 18% to automation. Add a task check (format or unsupported content): *outcomes reported separately from interpretation; no causal attribution of the time reduction to automation*.
- **Q6** Defensible.
- **Q8** `explicit` is correct.
- **Q9** Yes: add the check.

### SYN009: survey evidence
- **Q1** Equivalent. `নামবিহীন` is understood; `বেনামি` is standard.
- **Q6** The RIU-04 rationale is wrong. Omitting the department concentration does not "suggest organisation-wide concentration". The real consequence is that the 4.2 mean hides a localised problem. Criticality is fine; fix the rationale text.
- **Q8** `mixed` is correct.
- **Q9** Rationale edit.

### SYN091: six-sentence workshop briefing
- **Q1** Moderate: `দূরবর্তী ইনস্টলেশন ক্লিনিক`. দূরবর্তী means far-away and ক্লিনিক suggests a medical clinic, so a BN reader may imagine a distant physical venue. This directly affects RIU-06. Minor points: "1–3 PM" became `দুপুর ১টা থেকে ৩টা` (3 PM is conventionally বিকেল), and `প্রস্থান ফরম` is a literal rendering of "exit form".
- **Q3** The best BN-CS in the pilot.
- **Q6** The prompt's own criterion is "requirements that affect whether someone can participate successfully".
  - RIU-10 (food away from equipment) does not affect participation.
  - RIU-11 (walk-in rule) does not apply to the registered attendees the briefing is written for.
  - This review recommends both be **supporting**. Ten critical units in a six-sentence format also makes complete-task success very hard to reach.
- **Q7** CHECK-02: specify that `।`, `?` and `!` are the sentence terminators in Bengali, and that semicolon-joined clauses count as one sentence in every language.
- **Q8** `explicit` is correct.
- **Q9** Yes: criticality and sentence-boundary note.

### SYN100: case-management synthesis (flagged; see section 4)
- **Q1** **Material.**
  - (a) EN "long-term retention" is ambiguous (staff, skill or performance retention). BN `দীর্ঘমেয়াদি দক্ষতা ধরে রাখা` commits to *skill* retention.
  - (b) BN-CS `কারণগত decision সীমিত করে` means "limits causal *decisions*". The substitution misread সিদ্ধান্ত, which means "conclusion" here. This error exists in BN-CS only.
  - (c) "Trade-offs" became `বিনিময়মূলক প্রভাব`, which is opaque.
- **Q2** Long but clear. `সংশ্লেষ` is academic.
- **Q3** Good switching density, but contains the error in (b).
- **Q5**
  - (a) **Gap:** the prompt's final sentence explicitly asks why "the short observation period *and* implementation differences" limit causal conclusions. RIU-14 anchors only implementation differences, and no unit covers the short observation period. Make RIU-14 full credit require both reasons, with 0.5 for one reason, or add a separate unit.
  - (b) **Boundary RIU-13/RIU-14:** citing "one department used a hybrid workflow" as the causal caveat gives RIU-14 its reason. Write down whether that also earns RIU-13, which as written requires both the two-department/week-3 fact and the hybrid/week-6 fact.
  - (c) **Boundary RIU-09/RIU-19:** "performance after the two temporary specialists leave is unknown" partly states RIU-09. Define that RIU-09 requires the six-week window and the not-normal-staffing status.
- **Q6** 12 of 19 critical.
  - RIU-18 (future satisfaction unknown) is the weakest critical label, because the observed drop is already reported.
  - RIU-05 (response-rate change) is debatable.
  - Neither label is clearly wrong, given "without dropping caveats"; flag both for human adjudication.
- **Q7** RIU-16 must accept staff, skill or performance retention readings in every language, because of Q1(a).
- **Q8** `explicit` is correct.
- **Q9** Yes: (a) and the boundaries now; the language problem needs the study-lead decision.

---

## 4. Second pass on the flagged tasks, against `PILOT_AUDIT.md`

| Task | Audit flag | This review independently found it | Additional findings in this review |
|---|---|---|---|
| TECH006 | BN-CS `প্রো file` | Yes | Wrong genitive `user-র`; BN "crash" weakened to "closes"; **RIU-06 anchor gap** (a common answer pattern scores 0 on a critical unit); app-log/OS-log overlap; profile/local-data confound; visibility should be `mixed` |
| DEC006 | BN-CS `impact-িত` | Yes | Same corruption in DEC008 and SYN070 (`evidence-িত`); duplicate credit for exception justification (RIU-02 vs RIU-04); silence rule needed |
| CYBER009 | "production" weakened in BN | Yes | `সেবা অ্যাকাউন্ট` is a second meaning loss; BN-CS fails to repair either term; canary double credit (RIU-03/04); rollback double credit (RIU-05/06); infrequent-operations bundle |
| SYN100 | BN skill-retention specificity | Yes | **BN-CS conclusion → decision mistranslation** (same error in 7 more tasks); **short-observation-period reason has no unit**; RIU-13/14 and RIU-09/19 boundaries |

All four audit flags are confirmed and none is overturned. Each flagged task also has rubric problems beyond the language flag. The concerns are confirmed and extended, not resolved.

## 5. Items requiring study-lead decision (not resolvable by rubric edits)

These need a versioned corpus repair or a prospectively documented paired exclusion, decided before any model run (`PILOT_AUDIT.md`, final paragraph):

1. CYBER009 BN/BN-CS (production, service account)
2. DEC010 BN/BN-CS (security exposure, supportability)
3. SYN100 BN-CS (conclusion → decision) and BN (retention scope)
4. TECH006 and DEC006 BN-CS morphological corruption
5. PROC001 BN/BN-CS added "step by step"
6. Moderate items to adjudicate: TECH004, TECH009, CYBER004, CYBER010, PROC006, PROC010, SYN091
7. Corpus-wide BN-CS generator defects (section 2.1) and BN `দুর্নীতি` (TECH068, TECH084), before scaling batches include them

## 6. Follow-up (same day): corpus v0.3

At the study lead's direction, the language findings in sections 2 and 5 were acted on through a versioned corpus repair: all 500 BN and BN-CS prompts were hand-rewritten and English was left unchanged. See `data/prompts/CORPUS_CHANGELOG.md` and `data/prompts/LANGUAGE_GUIDE.md`.

The rubric findings in sections 3 and 4 (anchors, overlaps, criticality, visibility) have **not** been applied; they need a separate annotation-protocol revision. Section 2.1 has already been corrected: `review-র` is correct, because রিভিউ ends in a vowel sound.
