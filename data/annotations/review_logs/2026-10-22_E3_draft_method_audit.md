# Expansion Calibration Batch E3 — draft construction and second-pass audit

Construction and second-pass audit date: 2026-10-23. The filename retains the requested 2026-10-22 batch reference. This record describes annotation construction and methodological decisions; no study-model responses, evaluation runs or judge calls were produced.

## Scope and baseline

Baseline: accepted E1 and E2 on `main` (`9c0a73c486dca93cd5f4752461c9391f513f9be1`). E3 was constructed from that accepted baseline.

Sources read before construction: `ANNOTATION_PROTOCOL.md` (0.3), `SCALING_PLAN.md`, `EXPANSION_BATCHES.json`, all 22 E1 and 22 E2 annotations, both batches' draft-method audits and acceptance records, all 25 frozen pilot annotation records, `../prompts/LANGUAGE_GUIDE.md`, and `scripts/validate_pilot_annotations.py`. The accepted E1/E2 RIUs, constraints, checks and prompt hashes match the previously inspected construction baseline. All three frozen prompt variants were inspected for each E3 task: 66 prompt strings.

Exact E3 membership:

`CYBER021, CYBER071, CYBER038, CYBER023, CYBER074, DEC011, DEC089, DEC098, DEC014, SYN051, SYN049, SYN089, SYN063, PROC091, PROC041, PROC078, PROC094, PROC043, TECH071, TECH049, TECH029, TECH074`.

Five domain-grouped JSONL files contain one language-shared specification per task. All 22 records have `status: draft`, annotation schema `0.2`, protocol `0.3` recorded in notes, three v0.3.1 prompt hashes and empty `source_riu_ids` on every new unit. Review metadata follows the requested convention: `method_review` is `human`, and both review-reference fields point to `review_logs/2026-10-22_E3_draft_method_audit.md`. These metadata values follow the specified repository convention; they do not constitute an E3 acceptance decision or identify an additional completed review. Batch acceptance is a separate record and state.

Every zero anchor is exactly: "Absent, incorrect, contradicted, or does not meet an available positive anchor." Every full-credit anchor equals its unit description. Binary units have a null half-credit anchor.

## Resulting distribution

| Domain | Tasks | Easy | Medium | Hard | RIUs | Critical | Supporting | Binary | Ordinal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cybersecurity_digital_safety | 5 | 2 | 2 | 1 | 20 | 11 | 9 | 20 | 0 |
| decision_support | 4 | 1 | 1 | 2 | 19 | 10 | 9 | 17 | 2 |
| information_synthesis | 4 | 1 | 1 | 2 | 18 | 13 | 5 | 17 | 1 |
| procedural_instructional | 5 | 2 | 2 | 1 | 20 | 10 | 10 | 20 | 0 |
| technical_troubleshooting | 4 | 1 | 1 | 2 | 21 | 2 | 19 | 19 | 2 |
| **Total** | **22** | **7** | **7** | **8** | **98** | **46** | **52** | **93** | **5** |

Each task has exactly one `CHECK-01`, separate from RIU denominators. Its wording is identical to the accepted E1/E2 protocol 0.3 rule. No E3 prompt establishes a rigid sentence count or visual format, so no extra format check is added.

## Coverage and boundary audit

The second pass examined all 22 records for missing requirements, duplicate RIUs, bundled independent propositions, overcriticality and undercriticality, unjustified ordinal scoring, vague half anchors, language-equivalence differences, implicit safeguards, negative constraints, prescribed answer methods, diagnostic overreach, unsupported assumptions and CHECK-01 consistency. Counts below describe the final draft.

| Task | RIUs / critical | Coverage and boundary disposition |
|---|---:|---|
| CYBER021 | 3 / 2 | Non-connection, accountable handling and risk explanation are distinct. An ordinary device is not a safe ownership-identification tool; authorized isolated analysis is optional. Appearance does not establish safety or infection. |
| CYBER071 | 4 / 1 | Review security exposure, maintenance/support, functional fit and replacement consequences. Years without updates do not alone establish abandonment or vulnerability. No forced replacement, tool or rewrite. |
| CYBER038 | 6 / 4 | Dependency mapping, user/server boundaries, sensitive-system access, administrative access, enforced inter-zone policy and operational validation are distinct. Rollout validation remains supporting: it reduces operational-disruption risk but its omission alone does not defeat an otherwise complete segmentation strategy. No compulsory segmentation product or extended hardening framework. |
| CYBER023 | 3 / 2 | Withhold unverified installation, verify legitimacy and address recurrence through a trusted path. Settings review, an approved security check and IT escalation are alternatives. No mandatory reset or inferred confirmed compromise. |
| CYBER074 | 4 / 2 | Advisory/version applicability, reachable vulnerable functionality, impact/modifying controls and exploitation uncertainty have separate roles. High severity alone does not establish compromise or rule out exposure. No exploit execution or forced package removal. |
| DEC011 | 5 / 3 | Early closure, wait allowance, geographic efficiency, overall deadline and reasoned order are distinct. Current time and durations are unknown. Alternative orders are accepted when they respect feasibility; near-home and long-wait errands have no universally fixed position. |
| DEC089 | 3 / 2 | Burden evidence, concrete simplification and preserved accountable trace are distinct. Reuse, reduced duplication, integrated capture and automation are alternatives, not a mandatory process toolkit. No invented approval hierarchy or record-field quota. |
| DEC098 | 6 / 2 | Likelihood, impact and mitigation value are inputs; uncertainty treatment, robustness comparison and action choice are different operations. No mandatory expected-value formula or precise invented estimates. |
| DEC014 | 5 / 3 | Availability and duration evidence are separate; booking feasibility, compact placement of four interviews and transition allowance are separate outcomes. Joint attendance uses shared windows; split attendance depends on established participation requirements. No invented duration or zero-buffer optimum. |
| SYN051 | 4 / 4 | Common Tuesday is scored once, each note-time attribution separately, and the unresolved actual time/need for confirmation is scored once. A separate no-guessing RIU is not retained because it duplicates the same unresolved-time proposition. |
| SYN049 | 6 / 2 | Complaint magnitude, response-delay focus, staffing context, routing timing, reversible option and actionable investigation are distinct. Source facts are not automatically critical. Reversion is an available option, not a compulsory action or a proven causal remedy. |
| SYN089 | 6 / 5 | Dependency, launch/maintenance coincidence, no cached fallback, traffic forecast, conditional vendor warning and risk propagation are distinct. Highest expected traffic is supporting context. Possible intermittent outages are not guaranteed continuous failure. |
| SYN063 | 2 / 2 | One justified waiting-time observation and one explicitly labeled unjustified extension. Other outcomes and unsupported generalization of waiting-time gains are both valid broader-claim examples. Six minutes and 20 percent are equivalent changes, not extra required facts. |
| PROC091 | 3 / 2 | Feasible alternative, rain activation and participant communication are distinct. Indoor/covered relocation, rescheduling or cancellation can be valid. No mandatory weather service or comprehensive severe-weather framework. |
| PROC041 | 3 / 0 | Trip context, outward/return logistics and applicable essentials are supporting checklist categories. No unspecified item is individually decisive when the rest is adequate. Domestic day-trip scope does not create international or overnight requirements. |
| PROC078 | 6 / 2 | All six named phases are retained. Actuals collection, variance interpretation and forecast outturn are different operations. Existing-spend authorization checks or approval of corrective action are valid approval paths. No invented budget threshold or automatic freeze. |
| PROC094 | 5 / 3 | Scope triage, accountable ownership, dependencies, communication and tomorrow's feasibility are distinct. Original scope may remain if reassessed capacity supports it; deferral, temporary help or explicit renegotiation are valid alternatives. |
| PROC043 | 3 / 3 | Retrieval structure, point-of-use availability and exposure control have different functions. Indexed but inaccessible storage fails availability; convenient public sharing fails exposure control. Paper, digital or mixed organization can comply. |
| TECH071 | 4 / 0 | OS notification permission, app/account settings, suppression modes and connectivity/background delivery are separate supporting checks. Arriving messages do not prove every alert-delivery stage works. No compulsory reset or complete causal diagnosis. |
| TECH049 | 6 / 1 | Five explicit comparison branches plus diagnostic interpretation. Matching code or a mutable tag does not establish image equivalence. Cache evidence can use isolated clean builds or key comparison; no global purge or secret-value disclosure. |
| TECH029 | 6 / 1 | Five explicit cause branches plus controlled or failure-correlated interpretation. Compatibility, drift, credentials, throttling and upstream changes are not synonymous. No forced rollback, blanket credential rotation or cause inferred from upgrade timing alone. |
| TECH074 | 5 / 0 | Five named factors each need a concrete investigation. All are supporting because none is established as the decisive cause. Travel/non-travel comparisons and battery-use evidence are valid paths; no compulsory service disabling or battery-repair sequence. |

## Changes made during second pass

- **DEC014:** split the initial availability-plus-duration evidence unit. Both inputs can be supplied independently, so the final record has a separate binary supporting unit for planned duration. Clarified that split attendance is conditional on the required interview participation; partially overlapping calendars do not by themselves authorize waiving a panel member. A concrete schedule is not required without available windows and durations.
- **SYN051:** removed the separate no-guessing constraint after the final boundary pass because it duplicated the unresolved-time/confirmation proposition already scored in RIU-04. The prompt asks what is known, what conflicts and what must be confirmed; selecting an unsupported time remains assessable under CHECK-01 without a duplicate RIU.
- **SYN049 / RIU-01:** changed the exact complaint increase to supporting. An otherwise adequate plan can address delayed responses and investigate routing without separately stating the 30-percent magnitude. An incorrect asserted percentage still fails its binary unit and can trigger CHECK-01.
- **SYN049 / RIU-05:** changed the temporary-reversion capability to supporting. Losing an available option reduces completeness, but a sound investigation can validly retain current routing. Reversion is not the only permissible next step. The response-delay focus and evidence-to-action process remain critical.
- **SYN063 / RIU-02:** broadened the valid unsupported-claim examples to include generalization of waiting-time gains to untested populations, settings or periods. Restricting examples to entirely different outcomes would exclude a valid answer path. The example must remain explicitly labeled unjustified.
- **PROC078 / RIU-04:** accepted checking existing spending authorization as well as approval of corrective changes. The prompt names approvals without specifying a single point in the financial workflow. No fixed approval system is introduced.
- **PROC094:** made explicit that reassessment may preserve the original scope when available capacity supports it. The procedure assesses scope; it does not force a reduction regardless of evidence.

The initial construction evolved through the documented second-pass boundary and criticality revisions. The final E3 draft contains 98 RIUs: 46 critical, 52 supporting, 93 binary and 5 ordinal. The final pass removes one duplicate SYN051 binary RIU and reclassifies CYBER038 rollout validation from critical to supporting. No ordinal unit was added or removed.

## Ordinal scoring decisions

| Task / unit | Concrete weaker fulfillment scored 0.5 | Additional fulfillment needed for 1 |
|---|---|---|
| DEC011 / RIU-05 | An explicit order covering all three errands without a reason tied to timing, waiting or location | Explain why that sequence is sensible under the relevant constraints |
| DEC098 / RIU-06 | A call to compare all three risks on likelihood, impact and mitigation cost without a prioritization/response rule | Explain how those inputs guide an uncertainty-aware action choice |
| SYN049 / RIU-06 | A concrete investigation of response delays or routing without an evidence-to-next-action link or assessment of a temporary reversion | Connect investigation to an explicit decision/action or a monitored reversible trial |
| TECH049 / RIU-06 | A controlled local/CI or changed-input comparison without interpreting a possible result | Explain how a possible result supports or weakens a named failure cause |
| TECH029 / RIU-06 | A controlled comparison or failure-correlated investigation without a possible result and diagnostic implication | Link a possible result to support or weakening of a named cause relative to alternatives |

Each half anchor specifies a real but weaker sequence explanation, decision process or diagnostic contribution. None grants half credit for a wrong number, deadline, comparator, availability condition, bare topic mention or an arbitrary fraction of a checklist. Explicit atomic actions and constraints remain binary. A defeating contradiction or unsafe action overrides a full or half anchor.

## Methodological observations

1. **Information-synthesis criticality.** SYN049's magnitude, unchanged staffing, routing timing and available reversible option remain supporting. Their omission reduces source coverage without independently defeating an otherwise adequate delay-focused investigation/action plan. In SYN089, the expected traffic maximum adds demand context, while API dependence, maintenance timing, lack of cached fallback and the conditional outage warning define the central risk. SYN051's four retained units are critical because they establish the agreed day, both attributed conflicting times and the unresolved confirmation need without double-scoring a separate no-guessing constraint. These decisions apply the omission-consequence test rather than matching a domain percentage.
2. **Zero-critical tasks.** PROC041, TECH071 and TECH074 have no critical RIUs. They ask for broad preparation or initial evidence gathering without establishing one indispensable category or cause. Each retained category is useful for completeness, but omitting one alone does not defeat an otherwise adequate response or establish a material hazard. Core-task success is therefore NA under the existing protocol; completeness remains assessable. No critical label is added simply to avoid NA.
3. **Language equivalence.** Facts, numbers, deadlines, comparators and named branches align across the 66 inspected strings. CYBER074's BN `প্রকৃত ঝুঁকি কতটা` foregrounds degree of practical risk, while EN/BN-CS use exposure; the shared specification covers applicability, exploitation conditions and contextual consequence without requiring a numeric risk score. DEC089's BN `কাগজপত্র` does not make paper forms compulsory. DEC014's two-interviewer wording leaves the per-interview participation rule unspecified; the same conditional interpretation is used across languages. PROC091's Bengali outdoor-arrangement wording remains an activity contingency, not a data-backup requirement. No confirmed material mismatch requiring a frozen-corpus change was established.
4. **Security scope and safeguards.** Unknown USB handling does not require malware analysis by the finder. Repeated extension prompts do not justify automatically diagnosing infection or prescribing a system reset. Dependency age is a review signal, not proof of abandonment or compromise. Segmentation requires enforceable boundaries; operational validation is retained as a supporting rollout safeguard rather than a critical unit. A read-only or appropriately controlled diagnostic path does not acquire unrelated backup, credential-rotation or production-change requirements.
5. **Diagnostic generality.** TECH049 and TECH029 retain each explicitly named branch and one distinct interpretation unit. Each branch admits alternative task-relevant evidence sources rather than requiring every example. TECH071 and TECH074 ask for initial checks/investigation of factors, so no extra compulsory cause-attribution unit is added. A scanner, shell command, specific OS settings path, cache purge or production rollback is never required by annotator preference. One evidence span can satisfy separate units only when it supplies their distinct propositions.
6. **Workflow versus optional practice.** Budget review keeps the six explicit phases and distinguishes current variance from future outturn. The staffing contingency distinguishes scope, ownership and deadline feasibility. Travel-document organization distinguishes finding a document, reaching it when needed and limiting disclosure. Extra checklists, software products, mandatory duplicate documents, fixed buffers, numerical weights and universal approval thresholds are not promoted to requirements.
7. **Unsupported assumptions.** No available start time or travel duration is invented for DEC011. DEC014 supplies no interview duration or complete calendar. Unchanged staffing does not establish unchanged workload or adequate capacity in SYN049. A recent routing launch or software upgrade is a hypothesis-generating temporal fact, not an isolated causal demonstration. SYN089's expected traffic and possible outages retain their uncertainty. SYN063's deliberately unsupported example is identified as such rather than endorsed.

## CHECK-01 consistency

All 22 `CHECK-01` rules copy the accepted E1/E2 operational wording exactly. A materially false or unsafe assertion can fail both its content RIU and CHECK-01. Omission or insufficient fulfillment alone does not fail the task check. Wrong numbers, directions, deadlines or operational claims receive no special overlap exemption.

The distinction is consequential for SYN049: omitting the supporting percentage loses its RIU credit, while asserting a materially incorrect percentage can also flag CHECK-01. In SYN063, a broader claim clearly labeled unjustified is part of the requested contrast and is not itself an endorsed unsupported assertion. Selecting an unconfirmed meeting time, presenting a possible outage as certain or recommending an unsafe untrusted-USB interaction can trigger both outcomes when the relevant assertion is present.

Negative constraints can be met through a complying proposed path without reciting a prohibition. Handing an unconnected drive to the responsible custodian, withholding installation during verification, preserving an unresolved source-attributed meeting conflict, qualifying uncertain risk estimates and using private document storage are examples. Affirmative requirements still need expressed content: silence does not identify the meeting-time confirmation need or supply an enforced segmentation policy. Conditional safeguards apply to proposed risky actions, and a genuine refusal/non-answer receives 0 on every RIU, including negative constraints.

## Validation and preservation

All six required commands passed on the final E3 annotations:

```text
python3 scripts/validate_pilot_annotations.py --scope batch --annotation-dir data/annotations/expansion/E3
python3 scripts/validate_prompt_corpus.py
python3 scripts/freeze_prompt_corpus.py --check
python3 scripts/prepare_scaling_queue.py --check
python3 scripts/prepare_expansion_batches.py --check
python3 scripts/calibration.py check
```

Final batch validation: 22 draft tasks, 98 RIUs, 46 critical, 52 supporting, 93 binary and 5 ordinal. Corpus validation: 500 tasks and 1,500 prompt instances. Prompt freeze: 14 files matching v0.3.1. Queue: 25 frozen-pilot, 132 expansion and 343 later tasks. Assignment: six prospective batches of 22. Calibration: 30 authored fixtures and 229 answer-key rows; the original AR 2026-10-19 ordinal-alpha point-estimate threshold of 0.80 is unchanged. Additional frozen-pilot validation passes: 25 frozen tasks, 159 RIUs, 80 critical, 138 binary and 21 ordinal.

Programmatic integrity checks cover exact 22-task E3 membership, no duplicate task/unit IDs, domain-file placement, manifest/corpus difficulty metadata, all 66 prompt hashes, all 98 empty source-ID lists, exact zero anchors, description/full-anchor equality, binary null half anchors, distinct concrete ordinal half anchors, exact review metadata and one E1/E2-identical unsupported-content CHECK-01 per task. Prose checks cover the specified metadata/wording exclusions and absence of reviewer-directed instructions. The audit's task counts, domain/difficulty table and ordinal-unit list are reconciled with the JSONL records.

The starting SHA-256 inventory of all 78 pre-existing tracked files is unchanged. Changes are confined to the five E3 JSONL files and this audit. Frozen prompts and their manifest, pilot gold and its manifest, accepted E1/E2, calibration fixtures and answer key, agreement preregistration and sign-off, protocol 0.3, scaling queue and expansion assignments are preserved. No production gold was assembled. Structural and hash checks establish these integrity properties; they do not constitute a separate E3 acceptance decision.

Files added: `data/annotations/expansion/E3/cybersecurity_digital_safety.jsonl`, `decision_support.jsonl`, `information_synthesis.jsonl`, `procedural_instructional.jsonl`, `technical_troubleshooting.jsonl`, and `data/annotations/review_logs/2026-10-22_E3_draft_method_audit.md`.
