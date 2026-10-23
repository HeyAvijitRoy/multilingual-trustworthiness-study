# Expansion Calibration Batch E1 — draft construction and second-pass audit

Date: 2026-10-22. E1 construction and second-pass methodological audit were completed before this record. No model response generation or evaluation/judge calls were performed.

## Scope and authority

Base: `f9fdbe354a0febbc7188b4a1b448d7d4d1dccc35` (current `origin/main`, including PR #9 calibration sign-off). Local `main` was older; `expansion-E1` was created from this newer main commit without changing local `main` or merging anything.

Sources read before construction: `ANNOTATION_PROTOCOL.md` (0.3), `SCALING_PLAN.md`, `EXPANSION_BATCHES.json`, `PILOT_AUDIT.md`, all 25 frozen pilot records, `review_logs/2026-10-22_calibration_adjudication.md`, `../calibration/2026-10-22_CALIBRATION_SIGNOFF.md`, `../prompts/LANGUAGE_GUIDE.md`, and the annotation schema/validator. All three frozen prompt variants were inspected for every E1 task (66 prompt strings).

The exact E1 membership is unchanged:

`CYBER061, CYBER011, CYBER098, CYBER063, CYBER014, DEC051, DEC078, DEC029, DEC054, SYN041, SYN081, SYN069, SYN054, PROC021, PROC031, PROC089, PROC023, PROC034, TECH081, TECH058, TECH018, TECH083`.

Only E1 is annotated. Five domain-grouped JSONL files are in `data/annotations/expansion/E1/`. Every record is `draft`, uses annotation schema `0.2` with protocol `0.3`, and has empty `source_riu_ids`. The queue and batch manifests continue to describe the prospective work allocation; draft creation is not production-gold inclusion.

## Resulting distribution

| Domain | Tasks | Easy | Medium | Hard | RIUs | Critical | Supporting | Binary | Ordinal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cybersecurity_digital_safety | 5 | 2 | 2 | 1 | 16 | 8 | 8 | 15 | 1 |
| decision_support | 4 | 1 | 1 | 2 | 25 | 3 | 22 | 23 | 2 |
| information_synthesis | 4 | 2 | 1 | 1 | 16 | 13 | 3 | 15 | 1 |
| procedural_instructional | 5 | 2 | 2 | 1 | 22 | 14 | 8 | 21 | 1 |
| technical_troubleshooting | 4 | 1 | 1 | 2 | 19 | 5 | 14 | 17 | 2 |
| **Total** | **22** | **8** | **7** | **7** | **98** | **43** | **55** | **91** | **7** |

There are 22 `CHECK-01` rules, outside RIU denominators. No E1 prompt specifies a separate sentence-count or rigid visual format; no additional format check was invented. Source-attribution and owner/action requirements are content, not added presentation penalties.

## Second-pass coverage and boundary audit

Every row below was checked for missing requirements, duplicate/bundled propositions, omission-based criticality, rationale adequacy, ordinal justification and half-anchor specificity, language dependence, prescribed answer methods, silence handling and task-check orthogonality.

| Task | RIUs / critical | Coverage and boundary disposition |
|---|---:|---|
| CYBER061 | 3 / 2 | Risk mechanism, least-privilege routine use and deliberate exceptional elevation are distinct. No mandatory provider role or security product. |
| CYBER011 | 3 / 2 | Message evidence, obtaining independent confirmation and avoiding an unsafe message-controlled interaction are separate. Safe link-detail inspection is accepted; no post-compromise checklist. |
| CYBER098 | 4 / 1 | Retains all four requested phases. Risk assessment accepts qualitative or quantitative methods. Redesign half credit requires a concrete lower-friction proposal; an explicitly unsafe redesign remains 0. |
| CYBER063 | 4 / 1 | Immediate public-access containment is critical. Intended sharing, available exposure evidence and accountable notification are supporting follow-up. Do not infer actual compromise or require unavailable logs. |
| CYBER014 | 2 / 2 | Independent confirmation and withholding an unverified irreversible purchase/transfer are separately necessary. No required phone product, purchase amount or recipient is invented. |
| DEC051 | 4 / 1 | Distinguishes issue impact, delay consequences, credibility of improvement and their decision link. A conditional information-to-choice explanation suffices; no unconditional launch decision. |
| DEC078 | 9 / 1 | Consistent core facts are distinct from four audiences' detail and action adaptations. Detail and action are independently omittable. No unstated change facts or required channel. |
| DEC029 | 6 / 0 | Exactly the six named comparison dimensions, addressing both alternatives. Predictability is not synonymous with cheapness. No forced winner or extra selection formula. |
| DEC054 | 6 / 1 | Limitation evidence, each of three option appraisals, selection process and conditional reconsideration are distinct. No compulsory redesign or numerical weighting. |
| SYN041 | 4 / 4 | Three owner-action relations and one shared Thursday deadline. Equivalent names/transliterations accepted; no threefold deadline duplication or invented hour. |
| SYN081 | 3 / 3 | Dependency risk, available backup/location and retrieval delay retained. The 15-minute delay receives binary scoring, not generic numeric partial credit. No new preventive action is required. |
| SYN069 | 5 / 2 | Observation supplies the narrower conclusion; the causal-interpretation rule supplies its limitation. Three concurrent changes remain separate facts. No duplicated generic noncausality unit. |
| SYN054 | 4 / 4 | Three attributed reports and one negative no-adjudication constraint. A faithful unresolved summary can satisfy the constraint without an explicit disclaimer. |
| PROC021 | 3 / 2 | Retrievable source identity, note-to-source mapping and course-level organization have different functions. Stable links or reference handles are valid. |
| PROC031 | 4 / 2 | Needs, current stock, shopping-list recording and ongoing updates are distinct. Meal plans, shared apps and category ordering are optional methods. |
| PROC089 | 8 / 5 | All six named areas retained. Current-content transfer validation, historical retention and transition recovery address different loss paths. Cutover half credit is a defined switch lacking edit coordination. |
| PROC023 | 3 / 2 | Capturing source identity during use and mapping draft claims to sources are separate. Passage locators support precision but no citation style or reference-manager product is imposed. |
| PROC034 | 4 / 3 | Stock knowledge, pre-depletion trigger and a purchasing action form the central replenishment cycle; updates sustain it. No fixed quantity, interval or inventory application. |
| TECH081 | 4 / 2 | Actual format, reader compatibility and completeness/corruption are different checks. Original preservation applies only to proposed modifications; read-only or separate-copy paths comply. |
| TECH058 | 6 / 1 | Five requested evidence branches plus result-to-cause interpretation. A branch list is not full diagnostic reasoning. No required failover or production change. |
| TECH018 | 6 / 1 | Five requested evidence branches plus same-service departmental comparison/interpretation. Internal access does not prove cloud reachability. No security-control bypass required. |
| TECH083 | 3 / 1 | Missing-set inventory, like-for-like count scope and one further completion-evidence path. Alternatives replace an excessive integrity/log/timing checklist; scope evidence cannot be counted twice. |

### Changes made during the second pass

- TECH083: reduced the initial five-unit diagnostic checklist to three units. Transfer logs, access errors, file-integrity comparisons and source-change timing are accepted as alternative follow-up evidence, rather than requiring every check. This removes an answer-method prescription without dropping the shared objective.
- CYBER011: made the negative safeguard cover following the unverified message link as well as secret submission, while accepting controlled non-interactive inspection and independently verified channels.
- CYBER063: removed a bundled demand to both enumerate exposure scope and check audit evidence from one binary RIU; the evidence rule now targets available access/audit evidence only.
- CYBER098: removed an unnecessarily narrow reading that could force separately stated likelihood and impact components for every valid risk assessment; equivalent justified qualitative/quantitative assessments remain valid.
- All tasks: made refusal/non-answer treatment explicit (0 on every RIU), including negative constraints. Zero anchors do not automatically penalize silence on a compliant negative constraint. Contradiction precedence and wrong-number handling are explicit.

### Ordinal scoring decisions

| Task / unit | Weaker fulfillment awarded 0.5 | Additional fulfillment needed for 1 |
|---|---|---|
| CYBER098 / RIU-03 | Concrete lower-friction redesign without explanation of retained security protection | Connect the redesign to the relevant protection; explicitly defeating that protection scores 0 |
| DEC051 / RIU-04 | Relevant evidence on both launching and waiting, without explaining its effect on choice | Explain the trade-off guiding the choice |
| DEC054 / RIU-05 | Common-criteria comparison of all three options, without a selection process | Explain a rule or process reaching a choice |
| SYN069 / RIU-05 | Explicitly reject or qualify checklist-only causation, without explaining concurrent changes | Explain why concurrent changes prevent isolation of the checklist effect |
| PROC089 / RIU-07 | Define a cutover point without treatment of concurrent edits | Explain edit control/reconciliation at cutover |
| TECH058 / RIU-06 | Explicit regional comparison without result-to-hypothesis interpretation | Link a possible regional result to a cause or exclusion |
| TECH018 / RIU-06 | Same-service departmental comparison without interpretation | Link a possible departmental result to a cause or exclusion |

These seven anchors grade weaker fulfillment of the same reasoning/procedural requirement. They are not uncertainty allowances or partial credit for wrong facts. All other RIUs remain binary. These anchors remain part of the E1 draft specification.

## Methodological observations

1. **Bilingual wording strength/scope (DEC051, DEC078, PROC031, TECH058).** BN `অগুরুত্বপূর্ণ` may sound stronger than noncritical; `মাঠপর্যায়ের কর্মী` may evoke field staff more narrowly than frontline employees; the grocery wording can sound like a guarantee against omissions; regional degradation is phrased as poor performance in BN. Draft rules retain the shared meaning, create no language-specific RIUs and make no frozen-prompt repair. These wording differences are recorded here; the shared rubric does not introduce language-specific RIUs.
2. **Criticality extremes.** DEC029 has no critical RIU because no one comparison dimension is established as individually decisive by the prompt. SYN041, SYN054 and SYN081 have all-critical units because each retained short-source claim or explicit constraint is treated as central. These are omission-consequence judgments, not distribution targets. The individual rationales include the treatment of SYN081 backup location as part of availability and its omission as a critical failure.
3. **Implicit safeguards and loss prevention.** CYBER011/CYBER014, PROC089 and TECH081 include justified task-knowledge safeguards rather than only literal prompt words. The draft distinguishes necessity, criticality and conditional applicability, especially PROC089's historical-record retention, current-content validation, controlled cutover and recovery path. A read-only or clearly recoverable path must not lose credit solely for omitting a backup warning. PROC034's three critical cycle stages also need omission-based review rather than automatic acceptance because they are named in a routine.
4. **Open-ended prompt scope.** DEC051 treats the proposed information-to-choice link as a critical gradable requirement because the prompt asks what information should guide a decision. Review DEC078's independent audience-detail/action granularity and acceptance of justified no-action cases, DEC054's conditional review trigger, and CYBER063's distinction between first containment and supporting assessment/notification. Do not require an invented concrete organizational scenario or an exhaustive incident-response process.
5. **Source/content boundaries.** The draft separates SYN041 owner-action relations and shared deadline, SYN054 attributed evidence and the negative no-winner constraint, and SYN069 observed association and causal reasoning. For PROC021/PROC023, determine whether source identifiers are retrievable without imposing a fixed bibliography field list; a mere list of sources must not substitute for linking notes or draft claims. Preserve the recorded language-shared alternatives.
6. **Diagnostic generality.** TECH081 uses minimum checks without requiring unnecessary conversion; TECH083 uses a three-unit alternative-evidence construction; TECH018/TECH058 retain central comparative interpretation without prescribing tools. Domain knowledge should not become a compulsory exhaustive checklist.

No confirmed material language mismatch requiring a frozen-corpus change was established by this pass. The wording observations above are recorded without changing the frozen corpus. No rule amendment is implied by this draft audit.

## CHECK-01 and silence audit

All 22 checks use one identical protocol 0.3 operational rule. They flag material unsupported/contradicted facts or unsafe operational assertions, including wrong numbers. The same span can fail an RIU and CHECK-01; an RIU error never suppresses the task check. Pure omission or insufficient RIU fulfillment alone does not fail CHECK-01. No generic correct-answer text or generated response is included.

Affirmative caveats/requirements need expressed content. Negative constraints need a complying proposed path, not gratuitous restatement. Conditional safeguards do not become unmet requirements merely because a risky action is neither necessary nor proposed. The explicit refusal/non-answer override prevents vacuous credit on every negative constraint.

## Validation

All required commands passed against the final draft:

```text
python3 scripts/validate_pilot_annotations.py --scope batch --annotation-dir data/annotations/expansion/E1
python3 scripts/validate_prompt_corpus.py
python3 scripts/freeze_prompt_corpus.py --check
python3 scripts/prepare_scaling_queue.py --check
python3 scripts/prepare_expansion_batches.py --check
python3 scripts/calibration.py check
```

Batch validation: 22 tasks, 98 RIUs, 43 critical, 91 binary and 7 ordinal; all 22 statuses draft. Corpus validation: 500 tasks / 1,500 prompt instances. Frozen corpus: 14 pinned files. Queue: 25 frozen pilot / 132 expansion / 343 later tasks. Expansion assignment: six batches of 22. Calibration: 30 authored fixtures / 229 key rows, original AR 2026-10-19 ordinal-alpha point-estimate threshold 0.80 unchanged.

Additional checks verify exact E1 membership and metadata, no pilot/E2–E6 records, all 66 prompt hashes, empty source IDs, pending review fields, identical CHECK-01 rules, and byte-for-byte preservation of all pre-existing tracked files and local calibration materials. The existing frozen pilot validator also passes. Structural/hash checks do not by themselves certify semantic completeness or criticality.

E1 remains a draft research artifact; promotion into final production gold is recorded separately when that release state is reached.
