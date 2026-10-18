# Methodological audit of the 25-task RIU pilot

Audit date: 2026-10-08 UTC. Baseline: `74604be07b2246e1d7f063088a35799721290e81`.
Reviewer provenance: one Codex agent, internal methodological review; no independent human reviewer and no evaluation model calls. Every pilot task was read against its frozen English prompt; the three-language source records were inspected, with detailed follow-up on the two extended contexts. This is not a substitute for independent bilingual semantic/naturalness review.

## Finding and disposition

**Internal revision gate: PASS. Production scaling/gold freeze gate: PENDING.** The original schema validator checked structure, not the substantive assertions its manifest implied. Revisions now distinguish those claims. No frozen prompt bytes changed and no model responses were generated or scored.

The original 130 units included 100 critical (76.9%). Broad criticality language encouraged equating explicit prompt factors with indispensable units. Bundling also inflated the difficulty of satisfying a unit and hid which facts were omitted. There is no justified target percentage: the revised distribution is an outcome of unit-level decisions, not a quota.

## Task-by-task decisions

Counts are RIUs / critical RIUs. Migration is encoded in each new unit's `source_riu_ids`; task IDs and frozen difficulty labels are unchanged.

| Task | Before | After | Findings and revision |
|---|---:|---:|---|
| CYBER001 | 5 / 4 | 7 / 4 | Split password reset/session revocation and MFA/recovery checks. MFA and recovery review support longer-term protection rather than each counting as immediate critical containment. |
| CYBER004 | 5 / 4 | 5 / 3 | Made the assessment/attempt-versus-access distinction central. Reduced the over-specified bundled incident-response checklist to one optional follow-up containment action. |
| CYBER006 | 5 / 4 | 7 / 3 | Split exception justification from compensating control, and recurrence from logging. Core selection, legitimate need and reversible access reduction remain critical. |
| CYBER009 | 5 / 5 | 7 / 4 | Removed inventory/required-privilege overlap by separating current grants from evidence-based target needs. Split rollout/monitoring and rollback/ownership. Monitor-to-stop logic gets an ordinal anchor. |
| CYBER010 | 5 / 4 | 6 / 3 | Split signal correlation from escalation. Recalibrated named signal inputs as supporting; promoted alert-quality feedback because low false-alarm performance is central. |
| DEC001 | 4 / 2 | 3 / 1 | Merged deadline recognition/time protection. Removed unjustified uninterrupted-block requirement. Accepted conditional plans or explicit infeasibility because current time is unknown. |
| DEC004 | 5 / 4 | 6 / 2 | Separated effort estimate from two-person capacity. Made selection/allocation the critical method rather than awarding four critical points for naming factors; removed mandatory numerical scoring. |
| DEC006 | 5 / 3 | 5 / 3 | Retained impact/status neutrality/aging as core fairness safeguards. Impact includes breadth and severity as one graded prioritization criterion, not unrelated fact counting. |
| DEC009 | 5 / 4 | 5 / 2 | Merged shared criteria and consistent application to remove duplicate scoring. Split governance from documentation; common-format evidence is useful but no specific form is mandatory. |
| DEC010 | 6 / 5 | 7 / 1 | Kept five independent requested factors as supporting and promoted the feasible phased decision rule. Split interim mitigation from the roadmap. |
| PROC001 | 4 / 2 | 6 / 2 | Allowed stable tags as an equivalent organization path. Split extensions/collisions and final review/future practice; avoided requiring a particular folder hierarchy. |
| PROC004 | 5 / 4 | 5 / 2 | Merged evidence gathering and conditional owner confirmation into authoritative-version selection. Split naming convention from approval; newest timestamp alone cannot establish authority. |
| PROC006 | 5 / 5 | 5 / 4 | Separated name mapping from type/format conversion. Merged the redundant preservation examples into the conversion requirement; lossless reconciliation remains distinct. |
| PROC009 | 5 / 4 | 5 / 4 | Defined traceability as a retrievable source/location record rather than mandatory duplicate original files. Kept disagreement, adjudication and clean deliverable distinct; promoted the clean deliverable. |
| PROC010 | 5 / 3 | 6 / 2 | Split authorization from status metadata, and retention rules from recurrence. Combined replacement-link and active-discovery updating rather than scoring the same pointer twice. |
| SYN004 | 4 / 4 | 4 / 4 | Retained all four units and criticality: each is a distinct outcome or the key evidence limitation. A 100% critical task is permitted when justified. |
| SYN008 | 4 / 3 | 4 / 2 | Kept four distinct facts/caveat; staffing magnitude is supporting context while the causal limitation remains critical. No numeric partial credit. |
| SYN009 | 5 / 4 | 5 / 3 | Recalibrated response rate as context; sample composition and department concentration directly qualify interpretation. Kept mean satisfaction with its scale as one relational fact. |
| SYN091 | 9 / 7 | 14 / 10 | Split schedule/location/check-in, laptop/software, loaner count/eligibility, food rules and two certificate conditions. Fixed recording silence being wrongly accepted as an affirmative unknown. Moved sentence count and unsupported assertions to separate checks. |
| SYN100 | 10 / 7 | 19 / 12 | Split case volume/time gain, satisfaction/response rates, all implementation facts, two cost components and four distinct unknowns. Removed vague enough-details and and/or anchors. Values and directions within one before/after comparison remain one fact. |
| TECH001 | 4 / 3 | 4 / 2 | Removed overlap between symptom characterization and the major-change prohibition; resource metrics and attributed process load remain one diagnostic observation. Secondary examples are alternatives. |
| TECH004 | 5 / 4 | 5 / 1 | Kept four independent hypothesis checks without expanding each example into a unit. Recalibrated these as supporting and made actual differential interpretation critical. |
| TECH006 | 5 / 4 | 6 / 2 | Separated local-data testing from preservation. Promoted controlled result interpretation; individual hypothesis branches support completeness. Removed any mandatory reinstall path. |
| TECH009 | 5 / 4 | 5 / 3 | Separated locating capacity, explaining unexpanded size, and optional layout obstacles. Removed alignment as a standalone missing-capacity explanation; retained recovery before modification. |
| TECH010 | 5 / 3 | 4 / 3 | Merged overlapping comparison routes from old units 1/3 into the same-operation account control. A third clean profile is not mandatory. Data protection remains conditional. |

## Rubric revision 2 (2026-10-18)

The findings in `review_logs/2026-10-18_AI_bengali_prereview.md` (sections 3–4) were applied to 20 records before any model run; no responses exist, so nothing needs rescoring.

- **Anchor gaps closed:** TECH006 RIU-06 (interpretation without an explicit one-factor principle now earns credit); PROC004 RIU-01 (timestamp-only selection scores 0); PROC010 archive ladder.
- **Duplicate credit removed or bounded:** TECH006 app/OS logs; TECH009 inspection vs. explanation (RIU-02 now binary); CYBER006 exceptions vs. decision log; CYBER009 validation vs. rollout and stop signal vs. rollback; DEC006 exception reasons; DEC009 rule vs. evidence; SYN100 RIU-09/19 and RIU-13/14 boundaries.
- **Coverage:** SYN100 RIU-14 now requires both stated reasons (short observation period and implementation differences); SYN008 gains a format check for outcome/explanation separation; units added for CYBER001 credential reuse, CYBER009 infrequent operations, PROC006 shared-sheet coordination, PROC010 effective date and staff notification; PROC001 RIU-05 removed as padding.
- **Criticality:** TECH010 RIU-04 → critical (consistent data-preservation safeguards); CYBER010 RIU-06, SYN091 RIU-10/11 → supporting.
- **Visibility:** TECH006, CYBER010, DEC010 explicit → mixed; DEC009 implicit → mixed.
- **Clarifications:** silence rules (PROC001, DEC006), conditional wording (CYBER001), "major change" boundary (TECH001), Bengali sentence segmentation (SYN091), retention reading (SYN100).

Result: **159 RIUs, 80 critical (50.3%), 79 supporting; 138 binary and 21 ordinal.** An AI validation agreed with all 25 revised records and listed five judgment calls for human reviewers (`review_logs/2026-10-18_AI_pilot_validation.md`). Human review fields remain `pending` and statuses remain `method-audited`. The table below records revision 1.

## Distribution after revision

| Domain | Old critical / total | New critical / total | New ordinal units |
|---|---:|---:|---:|
| cybersecurity_digital_safety | 21 / 25 | 17 / 32 | 4 |
| decision_support | 18 / 25 | 9 / 26 | 6 |
| information_synthesis | 25 / 32 | 31 / 46 | 3 |
| procedural_instructional | 18 / 24 | 14 / 27 | 5 |
| technical_troubleshooting | 18 / 24 | 11 / 24 | 4 |

Total: **155 RIUs, 82 critical (52.9%), 73 supporting; 133 binary and 22 ordinal**. SYN091 has 14 content units plus separate task checks; SYN100 has 19 units. More extended-context units are justified by independently omittable claims, not a requirement to match task lengths. Ordinary tasks range from 3 to 7 units.

## Scoring and atomicity decisions

- Binary remains adequate for accurate numeric facts, clear constraints and discrete actions. An incorrect value must not earn half credit just because its direction is correct.
- Anchored partial credit is defensible for a limited set of reasoning/procedural requirements, subject to human calibration. Generic “partly correct” is prohibited. Binary sensitivity analysis remains mandatory.
- Before/after values are attributes of a single comparison, not independent atoms. Splitting 3.1%, 2.6%, and decrease into three points would reward fragments lacking the intended relation.
- Evidence and inference are distinct only when anchors distinguish them. TECH004 checks name concrete evidence; its critical comparison requires a result-to-hypothesis interpretation. CYBER009 current grants and required target permissions are likewise distinct.
- “Any one example” versus “all parts required” is now explicit. There is no “enough implementation details” threshold in SYN100. TECH001 secondary checks remain alternatives, not a checklist of all possible evidence.
- Conditional negative constraints accept a compliant safe path. Affirmative caveats require actual expression. SYN091 unknown recording status is no longer credited merely because no recording promise appears; an unsupported recording promise separately fails the task-level check.
- No unit-count minimum, critical-unit minimum, or domain criticality quota remains. Supporting units still count toward coverage and strict complete-task success.

## Coverage exclusions and boundaries

SYN091 omits beverages, available table outlets, the Monday email, and registered/capacity counts from required content because they do not change the stated participation conditions once equipment, installation assistance, conditional admission and food restrictions are retained. Loaner count, no lunch and check-in are supporting logistical context. The food exclusion zone is a critical explicit conduct restriction. The six-sentence constraint is scored once as format, without reducing content denominators.

SYN100 retains every outcome, implementation caveat and stated unknown. Relational facts retain their timing/comparators. Staff scheduling conflicts explain why training was missed but are not a separate performance-relevant unit; incomplete training uptake is retained. No additional outside causal or financial facts are required.

The pilot is purposive, not representative: technical tasks are all operating-system items; cybersecurity tasks all account-security; procedural tasks all documents/admin; decision tasks all prioritization. Synthesis spans ordinary and extended contexts but does not establish reliability for every subdomain. A 25-task internal PASS cannot support a claim that the annotation method is validated across all 500 tasks.

## Frozen-language concerns requiring independent review

| Task | Frozen evidence | Concern and handling |
|---|---|---|
| TECH006 | BN-CS `প্রো file` | Mechanical split of “profile”; inspect comprehensibility and whether lexical corruption changes difficulty. Preserve bytes; pending bilingual review. |
| DEC006 | BN-CS `impact-িত` | Mechanical replacement inside a Bengali word; naturalness concern not caught by script-boundary checks. Preserve bytes; pending bilingual review. |
| CYBER009 | EN “critical production workflow”; BN `গুরুত্বপূর্ণ বাস্তব কাজ` | Potential weakening of production/operational semantics. Do not add language-specific scoring requirements; bilingual adjudication needed. |
| SYN100 | EN “long-term retention”; BN `দীর্ঘমেয়াদি দক্ষতা ধরে রাখা` | Bengali makes skill retention more specific than the English phrase. Score the shared lack-of-retention-evidence concept and adjudicate equivalence before evaluation. |

**Update, corpus v0.3 (2026-10-18).** The study lead chose the versioned-corpus-repair route for these flags. All four are addressed in the v0.3 Bengali and BN-CS text, as is every other language issue in the AI pre-review (`review_logs/2026-10-18_AI_bengali_prereview.md`). The resolutions are listed in [CORPUS_CHANGELOG.md](../prompts/CORPUS_CHANGELOG.md). English prompts and RIU text are unchanged. The v0.3 text was approved and frozen by the study lead on 2026-10-18 without a recorded independent human linguistic review (an AI pre-review and AI validation are logged in `data/annotations/review_logs/`), and the prompt corpus is frozen at v0.3. These corpus-level flags are therefore closed; RIU gold review below is a separate, still-open gate.

These are review flags, not adjudicated exclusion decisions. Check all three variants for every task before freeze. If a material mismatch is confirmed, the study lead must choose a separately versioned corpus repair or a prospectively documented paired-task exclusion. Do not silently edit frozen prompts, tailor RIUs per language, or select exclusions after model results.

## Validation evidence and limits

Local corpus validation, pilot validation, negative validator tests, deterministic 500-task queue verification and patch checks are required. Prompt hashes are additionally compared against the baseline git blobs during this audit. CI is read-only; the old self-mutating corpus-cleanup workflow is retired.

Automated checks cover field/type/enum integrity, duplicate JSON keys and task IDs, exact pilot membership, corpus domain/difficulty joins, all three prompt hashes, binary/ordinal anchors, description-rule consistency, task checks, status gates and unchanged corpus bytes. Semantic overlap, factual adequacy, valid criticality and genuine human sign-off cannot be proved by these checks. No inter-rater agreement or model performance is reported. See `ANNOTATION_PROTOCOL.md` for the next validation stage.
