# Expansion Calibration Batch E5 — draft construction and second-pass audit

Construction and second-pass audit date: 2026-10-23. This record documents prompt-derived annotation boundaries, scoring and methodological observations. No study-model responses, evaluation runs or judge calls were produced.

## Scope and baseline

Baseline: `2a030ed5286bb47966ff04c1bc57c2a446f3d4ce`, the accepted E4 merge on `main` and the existing `origin/E-5`. A local `E-5` tracking that remote branch was checked out before construction. The initial working tree was clean. No merge was performed.

Authoritative materials include protocol 0.3, `SCALING_PLAN.md`, `EXPANSION_BATCHES.json`, accepted E1–E4 annotations, their method audits and acceptance records, all frozen pilot annotations, `../prompts/LANGUAGE_GUIDE.md`, and the annotation validator/schema. Earlier authoritative materials were already inspected in this continuous expansion workflow. Accepted E4's RIUs, anchors, criticality, notes, constraints, task checks and prompt hashes match the inspected construction baseline; its acceptance introduces no content or protocol amendment. The accepted E3 duplicate-removal and supporting-safeguard precedents continue to apply.

All three frozen prompt variants were inspected for every E5 task: 66 strings. Exact prospective membership:

`CYBER051, CYBER049, CYBER089, CYBER054, DEC061, DEC041, DEC038, DEC063, DEC043, SYN061, SYN058, SYN043, SYN083, PROC061, PROC058, PROC018, PROC063, TECH031, TECH091, TECH069, TECH034, TECH094`.

Five domain-grouped JSONL files contain one language-shared specification per task. Every record has `status: draft`, annotation schema `0.2`, protocol `0.3` in notes, three v0.3.1 prompt hashes and empty `source_riu_ids` on every unit. Review metadata follows the established requested convention: `method_review` is `human`, and both review-reference fields point to `review_logs/2026-10-23_E5_draft_method_audit.md`. These values follow the repository convention; they do not identify an additional completed review or constitute E5 acceptance. Acceptance is recorded separately.

Every zero anchor is exactly: "Absent, incorrect, contradicted, or does not meet an available positive anchor." Full anchors equal their descriptions; binary half anchors are null.

## Resulting distribution

| Domain | Tasks | Easy | Medium | Hard | RIUs | Critical | Supporting | Binary | Ordinal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cybersecurity_digital_safety | 4 | 1 | 1 | 2 | 19 | 12 | 7 | 18 | 1 |
| decision_support | 5 | 2 | 2 | 1 | 21 | 5 | 16 | 20 | 1 |
| information_synthesis | 4 | 1 | 2 | 1 | 15 | 13 | 2 | 14 | 1 |
| procedural_instructional | 4 | 1 | 1 | 2 | 18 | 6 | 12 | 17 | 1 |
| technical_troubleshooting | 5 | 2 | 2 | 1 | 21 | 1 | 20 | 21 | 0 |
| **Total** | **22** | **7** | **8** | **7** | **94** | **37** | **57** | **90** | **4** |

All 22 tasks have one accepted-rule unsupported-content `CHECK-01`. SYN043 additionally has a `CHECK-02` for checklist form, outside RIU denominators. No particular checkbox glyph, visual template or exact number of lines is required; clearly itemized checkable actions suffice. This distinguishes the requested checklist conversion from its five content operations. PROC061 asks for a method to create a gathering checklist, rather than conversion of a supplied note into a particular final artifact, so it has no additional form check.

## Coverage and boundary audit

The second pass examined every task for missing requirements, duplicated or bundled propositions, overcriticality and undercriticality, unnecessary ordinal scoring, vague half anchors, language-equivalence differences, implicit safeguards, negative constraints, method prescription, diagnostic overreach, unsupported assumptions and CHECK-01 consistency. Counts below describe the final draft.

| Task | RIUs / critical | Coverage and boundary disposition |
|---|---:|---|
| CYBER051 | 4 / 2 | Network containment, escalation, preservation and provisional interpretation are distinct. Escalation is supporting in an immediate-response task. No confirmed malware family, mandatory shutdown, untrusted decryptor, blind extension repair or full recovery framework. |
| CYBER049 | 8 / 5 | Seven named lifecycle areas plus recipient verification. Authorized identities and stored-copy protection are different propositions. Encryption and equivalent approved storage controls are alternatives; no invented jurisdiction, agreement form or fixed retention duration. |
| CYBER089 | 3 / 2 | Combined uniqueness, plausible linkage and release/population context are distinct. The anonymization label is not proof; direct names are not the only identifier path. No required privacy formula or real-person identification exercise. |
| CYBER054 | 4 / 3 | Alert context, containment, evidence protection and a continuity-compatible choice are distinct. Alternate work, justified restricted operation or a reasoned pause can be valid. Evidence paths are alternatives, not a compulsory memory-and-disk collection checklist. |
| DEC061 | 4 / 1 | Meaning of missingness, pattern/bias, information/task relevance and alternatives are distinct. Two percent alone does not justify dropping rows. No mandatory imputation, deletion, backup ritual or invented sample size. |
| DEC041 | 4 / 0 | Elapsed time, connection disruption, traveler fit and additional economic cost are supporting factors. Duration alone is not counted twice as cost. No unprovided transit rule, fixed fare arithmetic or universal direct-flight recommendation. |
| DEC038 | 8 / 3 | Six named criteria, capacity feasibility and contextual allocation are distinct. Legal deadlines and staffing constraints are critical; other inputs remain supporting. Score-assisted judgment is permitted, while a sole aggregate-score decision is not the requested framework. |
| DEC063 | 2 / 1 | A valid extreme observation can matter; source/context checks assess whether it is erroneous. No automatic deletion or automatic retention, mandatory cutoff or prescribed statistical repair. |
| DEC043 | 3 / 0 | Overall cost, downtown logistics and traveler/schedule flexibility compare both modes. No city-specific prices, guaranteed service coverage, forced pass or required winner. |
| SYN061 | 2 / 2 | One supported claim and one labeled overreach. Either supplied on-time or delay evidence can ground the supported claim. No denominator quota forces all source facts into every valid one-claim answer. |
| SYN058 | 5 / 5 | Three observed indicators, conditional coexistence explanation and targeted additional evidence are separate. Complaint count need not track a rate; no denominator, rating-scale maximum or causal explanation is supplied as fact. |
| SYN043 | 5 / 3 | Backup, update, restart and two post-restart checks remain distinct. Backup precedes installation; the two final checks need no artificial relative order. Checklist form is a separate check, not a content RIU. |
| SYN083 | 3 / 3 | One relational internet-dependency risk plus separate slide and video fallback components. Copies can be prepared; they are not established as already available offline. No additional equipment or failover-network checklist. |
| PROC061 | 3 / 0 | Gathering context, practical readiness and participant communication are supporting categories. No unspecified item is independently decisive; no mandatory catering, AV system, registration platform or responsibility matrix. |
| PROC058 | 6 / 1 | Five named scheduling considerations plus a conditional sequencing mechanism. Valid prerequisite order is categorical; the weaker ordinal anchor lacks availability/conflict integration, not correct prerequisite compliance. No invented provider or document requirements. |
| PROC018 | 6 / 3 | Five named workflow functions plus explicit observable handoff delivery. Static dependencies differ from actual transfer. Acknowledgement, a visible queue or monitored notifications are alternatives, not a mandatory formal sign-off process. |
| PROC063 | 3 / 2 | Necessary equipment setup, functional testing and seating readiness are distinct. Testing is supporting. No mandatory microphone, backup projector, fixed furniture count or exhaustive venue audit. |
| TECH031 | 3 / 1 | Added-filter effect, predicate semantics and source/context evidence are distinct. Controlled comparisons and sufficient predicate analysis are alternative primary methods; no forced one-filter-at-a-time command sequence or data rewrite. |
| TECH091 | 3 / 0 | Connection, host configuration and discovery-scope comparisons are supporting. Power does not establish reachability; one computer's failure does not establish that others succeed. No mandatory reset, reinstall or queue purge. |
| TECH069 | 6 / 0 | Six named branches each need concrete evidence; none is uniquely decisive. Detailed logs are not the passed basic summary. No destructive stress test, format, live electrical work or compulsory toolkit. |
| TECH034 | 4 / 0 | Indexes, plans, predicates and distribution/statistics have distinct evidence targets. No guaranteed index remedy, mandatory hint, database product or expensive live execution. |
| TECH094 | 5 / 0 | Queue state, transport, driver/rendering, spooler and device-side timing are distinct. A queue mention does not automatically provide spooler-service evidence. No compulsory purge, restart or security-control bypass. |

## Changes made during second pass

- **CYBER051 / RIU-02:** changed escalation from critical to supporting. With the rest adequate, immediate isolation and preservation already provide a protected initial response; separately stated escalation adds accountable follow-up but is not the whole task. This avoids treating a useful next-stage practice as indispensable to every safe immediate path.
- **CYBER051 preservation boundary:** clarified that protected-copy analysis after trusted assessment is allowed. The safeguard targets premature unprotected destructive modification, not all diagnostic examination.
- **CYBER049 / RIU-05:** made encryption/key protection and equivalent approved at-rest controls alternative storage paths. Clarified that naming authorized users alone belongs to RIU-02 and is not a second stored-copy safeguard proposition.
- **CYBER054 / RIU-04:** widened the continuity choice to include a reasoned temporary pause with appropriate owner coordination. The prompt asks for balance; it does not require keeping the affected endpoint online or continuing every activity regardless of risk. The half anchor retains a concrete arrangement or pause without the protection-compatibility explanation.
- **CYBER054 / RIU-03:** accepted securing the intact endpoint, retaining relevant logs or feasible volatile capture as alternative evidence paths. No universal forensic bundle or delay of urgent containment is imposed. Because evidence preservation is explicit here, an affirmative preservation step is still necessary.
- **DEC041 / RIU-01 and RIU-04:** separated elapsed journey time/schedule fit from incidental expense or economic consequence. One generic statement that the layover takes longer cannot earn both units without the second proposition.
- **PROC018 / RIU-06:** replaced a universal acknowledgement requirement with explicit observable delivery/notification and missed-handoff visibility. Acknowledgement, a work queue and monitored notifications are alternative implementations; the task does not mandate formal sign-off.
- **Cross-task boundary pass:** retained no extra prohibition RIU for trusting an anonymization label, automatically removing outliers or using a sole score when the corresponding positive assessment/process already handles that proposition. Numeric facts and clear checks remain binary; none of the four ordinal anchors was added or removed.

The initial structural pass covered 94 RIUs, 38 critical, 56 supporting, 90 binary and 4 ordinal. The second pass preserves all unit counts and scoring modes; the escalation reclassification yields 37 critical and 57 supporting. No unit or criticality percentage target was used.

## Ordinal scoring decisions

| Task / unit | Concrete weaker fulfillment scored 0.5 | Additional fulfillment needed for 1 |
|---|---|---|
| CYBER054 / RIU-04 | A concrete continuity arrangement or temporary work pause without explanation of compatibility with containment/evidence | Explain how the choice handles business needs without defeating protection; an unsafe continuity path remains 0 |
| DEC038 / RIU-08 | Group or compare requests on multiple criteria without an allocation/conflict-resolution rule | Turn the criteria into a contextual allocation process with reasoned competing-case handling; a sole aggregate score remains insufficient |
| SYN058 / RIU-04 | Explicitly distinguish ratings/means from raw complaint volume without a concrete coexistence mechanism | Supply a plausible conditional mechanism connecting count growth with improving satisfaction/response time |
| PROC058 / RIU-06 | Correct prerequisite-first ordering without a method for fitting availability or adjusting conflicts | Integrate the prerequisites with feasible windows and downstream adjustment; a violated prerequisite remains 0 |

These anchors describe weaker fulfillment of the same procedural or explanatory requirement. They do not grant half credit for an arbitrary subset of a checklist, a bare topic mention, a wrong number, a violated prerequisite or uncertainty between scorers. A defeating contradiction or unsafe action overrides positive anchors. The other 90 units remain binary.

## Methodological observations

1. **Immediate action versus complete response.** CYBER051 does not require a full ransomware response lifecycle. Its primary immediate safeguards are containment and preservation; escalation and provisional classification support them. CYBER054 explicitly asks for three-way balance, so containment, affirmative evidence retention and a continuity-compatible choice are central. A reasonable pause can meet that balance; the task is not the accepted E2 server scenario that forbade immediate offline removal.
2. **Data-sharing granularity.** CYBER049 retains the seven named areas and a recipient-check outcome because secure transport does not establish correct destination identity. Access permissions identify who may use data; at-rest controls protect stored copies. Logging, bounded retention and disposal remain supporting lifecycle safeguards rather than automatically critical because named. No specific law, consent form, retention interval, storage vendor or backup deletion technology is inferred.
3. **Data validity and claim scope.** DEC061 evaluates whether a small missing proportion is selective and consequential; no fixed deletion threshold follows from two percent. DEC063 distinguishes a meaningful rare event from error without prescribing an outlier algorithm. CYBER089 assesses uniqueness and feasible linkage without accepting a privacy label or assuming that theoretical uniqueness proves successful identification. Contextual assumptions remain explicit.
4. **Synthesis content and inference.** SYN061 accepts one supported conclusion from either relevant source fact, matching the requested one-claim output. Its too-strong example is labeled rather than asserted. SYN058 retains all three contrasting principal observations and treats candidate explanations as hypotheses. Higher customer/transaction volume could explain rising complaint counts alongside better ratings and mean response, but it is not an observed fact. Targeted denominator, sample, complaint-composition or distribution evidence can distinguish interpretations; every possible evidence source is not mandatory.
5. **Checklist content and form.** SYN043 has five independent source operations. Backup timing and post-restart verification remain within their respective operational descriptions. The two final checks are supporting tests, not automatically critical. The explicit conversion to a checklist receives a flexible format check separate from coverage, without a fixed checkbox symbol or five-line template. An unitemized narrative can retain content yet miss that form outcome; an itemized omission can pass form while losing content credit.
6. **Workflow alternatives.** PROC018's static responsibility/dependency map, completion criteria and actual handoff delivery are distinct operations. Formal acknowledgement is one method; visible queues and monitored notifications can also surface missed transfers. PROC058 derives a sequence without invented appointments or times. PROC061's generic checklist categories are supporting, while PROC063 has two explicit readiness outcomes: equipment and seating. A functional test remains supporting.
7. **Diagnostic restraint and zero-critical tasks.** DEC041, DEC043, PROC061, TECH091, TECH069, TECH034 and TECH094 have no critical RIUs. Their unspecified comparison factors or diagnostic branches do not establish one indispensable omission when the rest is adequate. The six storage, four performance and five printing branches still contribute to strict completeness. Consistent with accepted E3/E4, an additional mandatory cause-attribution unit is not added merely because a task asks how named areas would be investigated. TECH031's primary filter-effect investigation is critical because it directly addresses the supplied change; multiple sound methods can satisfy it. Low diagnostic critical coverage is a consequence of this omission test, not evidence that these tasks are trivial. Core-task success is NA where no critical units exist.
8. **Language equivalence.** All 66 inspected strings preserve the numeric values, direction, uncertainty and named considerations. CYBER051 retains safest immediate response; CYBER054 retains possible rather than confirmed execution. DEC038's Bengali vulnerability wording concerns applicants' vulnerability, not technical vulnerabilities. SYN058 preserves complaint volume rather than a population-adjusted rate, and no rating-scale maximum is supplied. SYN061 retains ten of twelve and the two missing-input delays. No confirmed material difference requiring a language-specific RIU or frozen-prompt revision was established.

## CHECK-01 consistency

All 22 unsupported-content rules copy the accepted E1–E4 protocol 0.3 wording exactly. A material factual/operational error can fail both a content unit and CHECK-01; RIU failure does not suppress the check. Pure omission or insufficient fulfillment alone is not an unsupported assertion.

For SYN061, an overstrong claim explicitly labeled as such is part of the requested answer rather than an endorsed unsupported assertion. In SYN058, a clearly hypothetical explanation is allowed, while presenting that scenario as an established cause is not. Wrong observed numeric values can fail the corresponding binary RIU and CHECK-01. Unsafe destructive incident or storage-diagnostic instructions can likewise fail both applicable outcomes. Checklist form is separate from this correctness check and from RIU coverage.

Affirmative requirements need expressed content. In CYBER054, preserving evidence is an explicit objective, so a protected evidence step is necessary; merely omitting a recommendation to wipe the endpoint is insufficient. CYBER051's preservation safeguard can be satisfied by a clearly non-destructive isolation/retention path without reciting every prohibited action. A bounded allocation can comply with capacity without repeating a prohibition, but omission of any deadline-screening process does not fulfill DEC038's affirmative legal-feasibility requirement. Conditional safeguards do not create unmet obligations for risky actions neither necessary nor proposed. A genuine refusal/non-answer receives 0 on every RIU.

## Validation and preservation

All six required commands passed on the final E5 annotations:

```text
python3 scripts/validate_pilot_annotations.py --scope batch --annotation-dir data/annotations/expansion/E5
python3 scripts/validate_prompt_corpus.py
python3 scripts/freeze_prompt_corpus.py --check
python3 scripts/prepare_scaling_queue.py --check
python3 scripts/prepare_expansion_batches.py --check
python3 scripts/calibration.py check
```

Batch: 22 draft records, 94 RIUs, 37 critical, 57 supporting, 90 binary and 4 ordinal. Corpus: 500 tasks / 1,500 prompt instances. Freeze: 14 pinned files at v0.3.1. Queue: 25 frozen pilot / 132 expansion / 343 later tasks. Assignment: six prospectively fixed 22-task batches. Calibration: 30 authored fixtures / 229 answer-key rows; original AR 2026-10-19 ordinal-alpha point-estimate threshold 0.80 unchanged. Additional frozen-pilot validation passes: 25 frozen tasks, 159 RIUs, 80 critical, 138 binary and 21 ordinal.

Programmatic checks cover exact 22-task E5 membership, unique task/unit IDs, domain-file placement, manifest/corpus difficulty agreement, all 66 prompt hashes, 94 empty source-ID lists, exact zero anchors, description/full-anchor equality, binary null half anchors, four distinct concrete ordinal half anchors and exact review metadata. They also check one accepted-rule CHECK-01 per task and the sole SYN043 checklist CHECK-02. Audit task counts, domain/difficulty totals and ordinal list are reconciled with the annotations. Wording checks cover the established metadata/prose exclusions and absence of reviewer-directed instructions.

All 92 pre-existing tracked-file SHA-256 hashes remain unchanged. Changes are limited to the five E5 JSONL files and this audit. Frozen prompts and manifests, pilot gold and manifest, accepted E1–E4, calibration fixtures/answer key/preregistration/sign-off, protocol 0.3, scaling queue and expansion assignments are preserved. No production gold was assembled. Structural and integrity results establish those properties without constituting E5 acceptance.

Files added: `data/annotations/expansion/E5/cybersecurity_digital_safety.jsonl`, `decision_support.jsonl`, `information_synthesis.jsonl`, `procedural_instructional.jsonl`, `technical_troubleshooting.jsonl`, and `data/annotations/review_logs/2026-10-23_E5_draft_method_audit.md`.
