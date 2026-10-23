# Expansion Calibration Batch E4 — draft construction and second-pass audit

Construction and second-pass audit date: 2026-10-23. This record describes prompt-derived annotation decisions. No study-model responses, evaluation runs or judge calls were produced.

## Scope and baseline

Baseline: `7a4c80615602b6ce0cfaf8d885f9597568b2490c`, the accepted E3 merge on `main` and the existing `origin/E-4`. A local `E-4` tracking that remote branch was checked out before construction. The working tree was clean; no merge was performed.

Authoritative sources: `ANNOTATION_PROTOCOL.md` (0.3), `SCALING_PLAN.md`, `EXPANSION_BATCHES.json`, accepted E1/E2/E3 annotations, their method audits and acceptance records, all 25 frozen pilot annotation records, `../prompts/LANGUAGE_GUIDE.md`, and `scripts/validate_pilot_annotations.py`. Previously inspected protocol, corpus, pilot, E1 and E2 materials remained byte-identical. The final E3 acceptance refinements were inspected before E4 construction: removal of SYN051's duplicate no-guessing RIU and supporting classification of CYBER038 rollout validation. These precedents inform E4 boundaries and criticality without modifying earlier batches.

All EN, BN and BN-CS prompts were inspected for every E4 task: 66 frozen prompt strings. Exact prospective membership:

`CYBER091, CYBER069, CYBER018, CYBER094, DEC071, DEC021, DEC058, DEC074, DEC023, SYN031, SYN018, SYN029, SYN074, PROC081, PROC029, PROC038, PROC083, TECH051, TECH011, TECH089, TECH054, TECH014`.

Five domain-grouped JSONL files contain one shared specification per task. All records have `status: draft`, schema `0.2`, protocol `0.3` recorded in notes, three v0.3.1 prompt hashes and empty `source_riu_ids` for every unit. Review metadata follows the established requested convention: `method_review` is `human`, and both review-reference fields point to `review_logs/2026-10-23_E4_draft_method_audit.md`. These values follow the repository convention; they do not identify an additional completed review or constitute batch acceptance. Acceptance remains a separate record and state.

Every zero anchor is exactly: "Absent, incorrect, contradicted, or does not meet an available positive anchor." Every full anchor equals its unit description. Binary half anchors are null.

## Resulting distribution

| Domain | Tasks | Easy | Medium | Hard | RIUs | Critical | Supporting | Binary | Ordinal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cybersecurity_digital_safety | 4 | 1 | 1 | 2 | 12 | 7 | 5 | 11 | 1 |
| decision_support | 5 | 2 | 2 | 1 | 20 | 3 | 17 | 17 | 3 |
| information_synthesis | 4 | 1 | 1 | 2 | 29 | 27 | 2 | 29 | 0 |
| procedural_instructional | 4 | 1 | 1 | 2 | 18 | 6 | 12 | 17 | 1 |
| technical_troubleshooting | 5 | 2 | 2 | 1 | 18 | 3 | 15 | 17 | 1 |
| **Total** | **22** | **7** | **7** | **8** | **97** | **46** | **51** | **91** | **6** |

All 22 tasks have one E1/E2/E3-identical protocol 0.3 unsupported-content `CHECK-01`, outside RIU denominators. No additional format check is introduced. SYN031 extracts requirements for a report; it does not require the extraction response to contain a chart or be delivered as a PDF. SYN029 ordering and PROC038 weekly staging are semantic temporal relationships, not prescribed visual layouts.

## Coverage and boundary audit

Every task underwent a second pass for missing requirements, duplication, bundled independent propositions, overcriticality and undercriticality, unnecessary ordinal scoring, vague half anchors, language equivalence, implicit safeguards, negative constraints, method prescription, diagnostic overreach, unsupported assumptions and CHECK-01 consistency. The following counts describe the final draft.

| Task | RIUs / critical | Coverage and boundary disposition |
|---|---:|---|
| CYBER091 | 2 / 1 | Protected replacement of the visible note and explanation of usable retrieval/recall are distinct. A protected manager or secure private record can suffice. Removing the visible note is part of replacement, not a second prohibition RIU. |
| CYBER069 | 4 / 3 | Identity context, credential-linked observed access, effective permissions and validity interval are distinct. Possible permission scope is not observed use. No permanent-key workflow or mandatory provider-specific log/policy checklist. |
| CYBER018 | 3 / 2 | Safe cross-recipient evidence, variant-aware correlation and evidence-based campaign scoping are separate. Infrastructure, lure, URL and timing evidence are alternatives; exact message identity is not required. No compulsory full incident-response plan. |
| CYBER094 | 3 / 1 | Workflow burden, actual bypass/security consequences and assessment of policy contribution are distinct. Feedback and comparative evidence can suffice without an experiment or mandatory policy redesign. Coexistence alone is not established causation. |
| DEC071 | 3 / 1 | Required responsiveness, justified channel choice and nonurgent context have different functions. Email, chat, a call or a conditional sequence can be justified; two-channel handling is optional. |
| DEC021 | 3 / 0 | Each tool contributes a distinct task-relevant feature or limitation for ten deadlines. No forced winner, feature quota, notification system or advanced spreadsheet workflow. |
| DEC058 | 6 / 1 | Change-impact evidence, four option appraisals and selection rule are separate. Seventy percent complete is not seventy percent reusable; partial restart is not a full-project restart. No compulsory numeric weighting or invented deadline. |
| DEC074 | 5 / 1 | Audience/impact context, three channel appraisals and conditional choice are distinct. Group, written and private channels may be combined without a universal sequence or invented decision details. |
| DEC023 | 3 / 0 | Convenience, control and recovery each compare local and cloud backup. No compulsory winner, product, price assumption or full backup architecture. Synchronization does not automatically establish recoverable version retention. |
| SYN031 | 5 / 5 | Strictly under five pages, one chart, data through June, PDF and Friday are independent report requirements. These are affirmative extracted statements, not silently satisfied constraints on the answer itself. |
| SYN018 | 9 / 9 | Eight defining strategy-attribute facts and the explicit no-selection constraint. Preserve 10 percent, two extra days, two weeks, shortest rollout, easiest rollback and temporary version differences. No new rollout totals or preferred strategy. |
| SYN029 | 9 / 7 | Four event-time relations, selected backup, reported absence, chronology, backup coverage and residual ambiguity are distinct. Exact failure/restore-start times are supporting context. A missing later state is not evidence establishing why a whole file is absent. |
| SYN074 | 6 / 6 | Three duration allocations, A-before-B, work window and single-person non-overlap. All valid placements are accepted; B need not immediately follow A and C can precede or separate them. No extra arithmetic-summary RIU. |
| PROC081 | 3 / 1 | Two-location recoverable copying is critical; verification and refresh are supporting. Original plus a genuine separate backup can meet the two-location minimum; a third total copy or two additional backups is not imposed. Two folders on one storage device do not supply independent storage protection. |
| PROC029 | 5 / 1 | Population, method and outcome evidence, comparability-based synthesis and scoped conclusions are distinct. The explicit conclusion-scope step is supporting; the critical method already excludes indiscriminate equivalence. Narrative, grouped and justified quantitative paths remain available. |
| PROC038 | 7 / 2 | Six named workflow functions plus feasible weekly allocation. Moving-day execution and week-by-week staging are critical; named supporting phases are not automatically critical. No fixed four-week arithmetic, mover or exhaustive property checklist. |
| PROC083 | 3 / 2 | A size-resolving method, usable recipient access and a delivery check are separate. Compression is valid only if it actually makes a usable attachment fit. Upload/link, other transfer media and suitable physical transfer remain alternatives. |
| TECH051 | 3 / 0 | Account/workspace, intended sharing rights and one location/client-view evidence path. Successful sign-in does not establish folder authorization. Search, direct link, web view and move/deletion evidence are alternatives. |
| TECH011 | 4 / 1 | Scope, local network, further internet-path evidence and logical basic-first sequencing. No fixed command or universal reset. Repeating a scope test alone does not earn the additional external-path unit. |
| TECH089 | 2 / 1 | Actual byte comparison and one additional reading-context comparison. Metadata/access and reader/environment investigations are alternatives rather than mandatory parallel branches. Equal names and sizes do not prove byte identity; equal bytes do not prove a software defect. |
| TECH054 | 4 / 0 | Four named concrete investigation branches. No uniquely decisive cause is supplied, so no critical cause branch or extra compulsory attribution unit. No production failover, universal deployment architecture or secret-value exposure. |
| TECH014 | 5 / 1 | Four named evidence branches plus isolating interpretation. Adapter driver/power evidence is distinct from broader OS state. Known-good swaps and event evidence are alternatives, without disrupting stable users or mandating resets. |

## Changes made during second pass

- **TECH089:** reduced the initial three-unit construction to two units. Byte identity remains the critical comparison. File metadata/access and processing-context comparisons become alternative follow-up paths in one supporting unit. Requiring both categories would impose a diagnostic checklist not named by the prompt. The byte comparison cannot be counted again as the additional evidence.
- **PROC083 / RIU-01:** broadened the transfer anchor so compression that actually makes a usable attachment fit is accepted alongside upload/link and other transfer media. The initial wording could be read as requiring departure from email even when the attachment limit can genuinely be resolved within email.
- **PROC083 / RIU-03:** replaced a compulsory completion-plus-recipient check with an appropriate completion or retrieval check. The verification outcome remains supporting; multiple interchangeable checks do not become jointly necessary.
- **PROC029 / RIU-05:** changed explicit conclusion scoping from critical to supporting. A sound comparability-based synthesis can remain valid without a separately stated conclusion-scope step. An actual unsupported universal inference remains assessable under CHECK-01; the critical method unit still requires comparability-based synthesis. This applies the accepted E3 omission-consequence precedent rather than treating every methodological safeguard as critical.
- **Cross-task duplication pass:** retained no separate prohibition against visible notes in CYBER091, exact-message assumptions in CYBER018 or direct equivalence in PROC029 when the positive requirement already addresses that proposition. SYN018's no-selection rule remains because the prompt expressly forbids a choice and none of the fact units represents that distinct instruction.
- **Cross-task scoring pass:** kept numeric facts, categorical checks, durations, comparators, work windows and explicit constraints binary. The six ordinal requirements retain explicit weaker reasoning/process contributions. No count target or critical proportion was used.

The initial draft passed structural validation with 98 RIUs, 47 critical, 51 supporting, 92 binary and 6 ordinal. Consolidating the TECH089 alternatives removes one supporting binary unit; reclassifying the PROC029 conclusion step yields the final 97 RIUs, 46 critical, 51 supporting, 91 binary and 6 ordinal. No ordinal unit was added or removed.

## Ordinal scoring decisions

| Task / unit | Concrete weaker fulfillment scored 0.5 | Additional fulfillment needed for 1 |
|---|---|---|
| CYBER094 / RIU-03 | Identify a specific burdensome process step and corresponding bypass without a method/reasoning for judging policy contribution | Explain how evidence supports or weakens policy contribution, allowing alternative explanations |
| DEC071 / RIU-02 | Name a channel for the urgent question without a reason connected to responsiveness or interaction | Explain its fit to the urgent response need under the stated or conditional availability context |
| DEC058 / RIU-06 | Call for comparing all four adaptation paths on common benefits/costs/risks without a selection process | Give a conditional rule or process that reaches a choice using the evidence and binding constraints |
| DEC074 / RIU-05 | Describe uses of the three channels without a situation-to-channel choice rule | Connect audience/impact needs to a channel or justified combination |
| PROC029 / RIU-04 | Group studies by relevant differences without explaining how findings are synthesized within/across groups | Explain a comparability-based method for combining or juxtaposing the findings |
| TECH014 / RIU-05 | Propose a controlled component comparison or dropout-correlated observation without a result/diagnostic implication | Link a possible result to support or weakening of a candidate cause relative to alternatives |

These weaker anchors retain a real part of the same explanation, assessment or procedure. They are not half credit for mentioning a topic, supplying an arbitrary subset of facts or making a wrong numeric claim. A material contradiction or unsafe action that defeats the unit overrides both positive anchors. A wrong 10-percent fraction, deadline, duration, order requirement or comparator has no available half anchor.

## Methodological observations

1. **Individual criticality in synthesis.** SYN031's five binding report requirements determine whether the report meets its request. SYN018's supplied facts define the rollout and rollback/version trade-offs; omitting a defining attribute or explicit no-choice condition distorts that short comparison. SYN074's six units each determine actual schedule feasibility. SYN029 has supporting exact failure and restore-start times because a correct backup-coverage and missing-file distinction can remain valid without those exact timed events. Its selected restore point, missing-file observation and inference boundaries are central. The high synthesis critical share follows these task-specific consequences, not an automatic source-fact rule.
2. **Zero-critical tasks.** DEC021, DEC023, TECH051 and TECH054 have no critical RIUs. They compare underspecified options or gather first evidence without identifying one indispensable tool attribute or cause. Each unit contributes to strict completeness, but omission of one alone does not defeat an otherwise adequate comparison/investigation. Core-task success is NA under the existing protocol. No label was added merely to avoid that outcome.
3. **Backup-timeline ambiguity.** SYN029 does not say when the file was created, whether an earlier version was in the midnight backup or exactly what restore recovered. A 12:15 change is outside the completed midnight backup's normal coverage. This can explain a missing later state, but the absence of the whole file could involve backup membership or restore behavior, or a file first created after the backup. The shared specification preserves this distinction without selecting an unsupported explanation. Restore began at 1 AM; completion at 1 AM is not established.
4. **Two-location interpretation.** PROC081 specifies two locations without saying two additional backups beyond the source. The minimum shared reading is recoverable copies across two distinct storage locations, one genuinely separate from the working location. An original and a separate backup can comply; cloud plus another backup can also comply. A mandatory third copy, offsite product or full 3-2-1 scheme would add an unstated requirement. Two folders on a single storage device do not protect against that device's loss. Verification and refresh remain supporting basic procedure steps.
5. **Language equivalence.** All 66 inspected strings preserve the numbers, comparators, deadlines and named areas. SYN031's `পাঁচ পৃষ্ঠার কম` retains the strict under-five limit, and `জুন পর্যন্ত` retains the data cutoff. SYN018's `দুই দিন বেশি` preserves extra rather than total days, and `সবচেয়ে সহজ` preserves the rollback superlative. The file-versus-later-state ambiguity in SYN029 and the count interpretation in PROC081 occur across all three languages, not in one language only. PROC038's week-by-week wording does not fix an exact number of weeks per month. No confirmed material mismatch requiring prompt revision was established.
6. **Diagnostic restraint.** TECH051's location/view alternatives and TECH089's reading-context alternatives replace exhaustive lists of hypotheses. TECH054 asks how four areas would be investigated, so it does not gain an additional cause-attribution RIU. TECH014 explicitly asks to isolate causes and therefore retains a distinct interpretation requirement. TECH011 explicitly asks for order, so sequencing is content. No vendor tool, command, blanket security bypass, cache reset or invasive repair is introduced as necessary.
7. **Security and decision scope.** Temporary-credential analysis separates observed events from possible permission scope and validity. Variable phishing messages require correlation and evidence-based expansion, not exact equality or a full response framework. Policy friction is evaluated without assuming causation or requiring redesign. Communication choices can be conditional or combined. Project completion percentage is context, not a forced sunk-cost decision. Pure comparison tasks need no winner.
8. **Workflow centrality and safeguards.** Backup verification, file-transfer verification, utility arrangements and moving final checks remain supporting rather than automatically critical. Protected password replacement, two-location copying, recipient access and feasible moving-day coordination address the central requested outcomes. Destructive or unsafe instructions can still fail CHECK-01; no unrelated backup ritual or warning recitation is required for read-only or protected paths.

## CHECK-01 consistency

All 22 rules use the exact accepted E1/E2/E3 operational wording. Material unsupported/contradicted factual or operational assertions, wrong values/directions/comparators and unsafe instructions are flagged independently of RIU scores. A shared error span can fail both outcomes. Pure omission or insufficient RIU fulfillment does not automatically flag CHECK-01.

In SYN031, merely failing to list the PDF requirement is an RIU omission; falsely claiming the requested deliverable is a spreadsheet can also be a task-check error. SYN018 selection violates its no-choice RIU, but a preference alone is not automatically an unsupported factual assertion; accompanying false factual claims are checked separately. SYN029 assertions that the entire file's absence is proved by timing, or that restore completed at 1 AM, can create task-check errors. These are scoring boundaries, not generated or scored study responses.

Affirmative requirements require expressed content. An extraction response that happens to be short does not silently satisfy the report's under-five requirement; it must state that requirement. SYN018's neutral comparison can comply with no-selection without reciting a prohibition. SYN074's disjoint allocations can satisfy single-person non-overlap silently. The positive protected-replacement and comparability requirements are not duplicated as negative RIUs. Conditional safeguards accept protected or non-destructive paths and do not become obligations for risky actions neither necessary nor proposed. A refusal/non-answer receives 0 on every RIU.

## Validation and preservation

All six required commands passed against the final E4 annotations:

```text
python3 scripts/validate_pilot_annotations.py --scope batch --annotation-dir data/annotations/expansion/E4
python3 scripts/validate_prompt_corpus.py
python3 scripts/freeze_prompt_corpus.py --check
python3 scripts/prepare_scaling_queue.py --check
python3 scripts/prepare_expansion_batches.py --check
python3 scripts/calibration.py check
```

Batch validation: 22 draft tasks, 97 RIUs, 46 critical, 51 supporting, 91 binary and 6 ordinal. Corpus: 500 tasks / 1,500 prompt instances. Freeze: 14 pinned files at v0.3.1. Queue: 25 frozen-pilot / 132 expansion / 343 later tasks. Assignment: six prospectively fixed batches of 22. Calibration: 30 authored fixtures / 229 answer-key rows; original AR 2026-10-19 ordinal-alpha point-estimate threshold 0.80 unchanged. Additional frozen-pilot validation passes: 25 frozen tasks, 159 RIUs, 80 critical, 138 binary and 21 ordinal.

Programmatic checks cover exact 22-task E4 membership, unique task/unit IDs, correct domain files and difficulty metadata, all 66 prompt hashes, all 97 empty source-ID lists, exact zero anchors, description/full-anchor equality, binary null half anchors, six distinct concrete ordinal half anchors, exact review convention and one accepted-rule CHECK-01 per task. The audit's counts, domain/difficulty table and ordinal list are reconciled with the JSONL files. Wording checks cover the specified metadata/prose exclusions and absence of reviewer-directed instructions.

All 85 pre-existing tracked-file SHA-256 hashes are unchanged. Changes are confined to the five E4 JSONL files and this audit. Frozen prompts and manifests, pilot gold and manifest, accepted E1/E2/E3, calibration fixtures/answer key/preregistration/sign-off, protocol 0.3, scaling queue and batch assignments are preserved. No production gold was assembled. Structural and integrity checks establish these properties without constituting E4 acceptance.

Files added: `data/annotations/expansion/E4/cybersecurity_digital_safety.jsonl`, `decision_support.jsonl`, `information_synthesis.jsonl`, `procedural_instructional.jsonl`, `technical_troubleshooting.jsonl`, and `data/annotations/review_logs/2026-10-23_E4_draft_method_audit.md`.
