# Expansion Calibration Batch E6 — draft construction and second-pass audit

Construction and second-pass audit date: 2026-10-23. This record documents prompt-derived unit boundaries, criticality, anchors and language-equivalence observations. No study-model responses, evaluation runs or judge calls were produced.

## Scope and baseline

Baseline: `487fc8fde78c62f653bb6b13236db76a612060e9`, the accepted E5 merge. Work began on the existing `E-6` branch tracking `origin/E-6`, with a clean working tree. No branch merge was performed.

Authoritative materials include protocol 0.3, `SCALING_PLAN.md`, `EXPANSION_BATCHES.json`, accepted E1–E5 annotations, their method audits and acceptance records, all frozen pilot annotations, `../prompts/LANGUAGE_GUIDE.md`, and the annotation validator/schema. Earlier authoritative materials were inspected in this continuous expansion workflow. Accepted E5 differs from its inspected construction commit only in status and review metadata; all task objectives, RIUs, criticality, anchors, notes, constraints, checks and prompt hashes are unchanged. Its acceptance introduces no content or protocol amendment. E1 remains the methodological baseline, including the later accepted duplicate-removal, supporting-safeguard and diagnostic-restraint precedents.

All three frozen prompt variants were inspected for each task: 66 strings. Exact prospective E6 membership:

`CYBER031, CYBER029, CYBER078, CYBER034, DEC081, DEC091, DEC018, DEC083, DEC094, SYN071, SYN038, SYN014, SYN023, PROC071, PROC098, PROC049, PROC074, TECH041, TECH021, TECH078, TECH043, TECH023`.

Five domain-grouped JSONL files contain one language-shared specification per task. All records have `status: draft`, schema `0.2`, protocol `0.3` in notes, three v0.3.1 prompt hashes and empty `source_riu_ids` on every unit. Review metadata follows the established requested convention: `method_review` is `human`; both review-reference fields point to `review_logs/2026-10-23_E6_draft_method_audit.md`. These labels follow the repository convention; they do not identify an additional completed review or constitute E6 acceptance. Acceptance is recorded separately.

Every zero anchor is exactly: "Absent, incorrect, contradicted, or does not meet an available positive anchor." Full anchors equal their descriptions. Binary half anchors are null.

## Resulting distribution

| Domain | Tasks | Easy | Medium | Hard | RIUs | Critical | Supporting | Binary | Ordinal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cybersecurity_digital_safety | 4 | 1 | 1 | 2 | 16 | 4 | 12 | 15 | 1 |
| decision_support | 5 | 2 | 2 | 1 | 19 | 10 | 9 | 17 | 2 |
| information_synthesis | 4 | 1 | 2 | 1 | 18 | 14 | 4 | 18 | 0 |
| procedural_instructional | 4 | 1 | 1 | 2 | 18 | 8 | 10 | 17 | 1 |
| technical_troubleshooting | 5 | 2 | 2 | 1 | 19 | 1 | 18 | 19 | 0 |
| **Total** | **22** | **7** | **8** | **7** | **90** | **37** | **53** | **86** | **4** |

Each task has the accepted protocol 0.3 unsupported-content `CHECK-01`. SYN023 additionally has a `CHECK-02` for a short chronological timeline or clearly ordered event sequence. Compact prose, bullets and tables are valid; no exact word count or particular layout is imposed. Event/day facts remain content RIUs, while their chronological presentation is a separate format outcome. No other task has an added format check.

## Coverage and boundary audit

The second pass examined every task for missing requirements, RIU duplication, overcriticality and undercriticality, unnecessary ordinal scoring, vague half anchors, language differences, implicit safeguards, negative constraints, diagnostic prescription and CHECK-01 consistency. Counts below describe the final draft.

| Task | RIUs / critical | Coverage and boundary disposition |
|---|---:|---|
| CYBER031 | 2 / 2 | Default-credential exposure and administrator-credential replacement are distinct. Wireless-password changes alone do not replace administrator credentials. No assumed internet exposure, firmware-upgrade requirement or hardening checklist. |
| CYBER029 | 4 / 1 | Alert details, trusted application comparison, independent corroboration and evidence-based disposition are distinct. Application legitimacy does not establish benign execution. No mandatory blanket isolation, process termination or full forensic acquisition. |
| CYBER078 | 6 / 0 | Six named evidence targets: provenance, package source, resolved versions, reference hashes, CI execution and output artifacts. No unsupported conclusion that every artifact is compromised, required attestation format or compulsory full incident lifecycle. |
| CYBER034 | 4 / 1 | Blocking-rule evidence, required communication scope, bounded restoration and verification are distinct. A rule correction or bounded rollback can substitute for a new exception. Narrow restoration already implements the no-broad-exception constraint. |
| DEC081 | 2 / 1 | Consequences of inconsistent interpretation inform whether shared guidance justifies documentation and maintenance. No automatic formalization of every practice or compulsory procedure template. |
| DEC091 | 4 / 1 | Forecast uncertainty, rain consequences, a practical choice and useful updates are distinct. An indoor fallback, suitable outdoor plan or conditional change rule can work. No invented forecast probability or universal cancellation rule. |
| DEC018 | 6 / 5 | Staffing, room capacity, all-60 coverage, deadline, fairness and assignment mechanism are distinct. Fairness is supporting; the feasibility limits and allocation mechanism are critical. One session, repeated sessions or staggered cohorts can work if constraints permit. |
| DEC083 | 3 / 1 | Purpose evidence, present effects and the keep/change/retire decision are distinct. Relevant dependencies inform current effects; a universal legal/contract/safety audit is not inferred. A provisional decision or safe trial can be valid. |
| DEC094 | 4 / 2 | Learning about the dependency, structuring milestones, bounding commitments and updating plans are distinct. A checkpoint gates dependent work; no independent workstream, fixed early date or invented numerical buffer is assumed. |
| SYN071 | 4 / 1 | One feasible interval plus separate Ana, Ben and room justifications. Any 30-minute interval starting 2:15–2:30 PM inclusive is valid. Correct timing is critical; omitted individual explanations reduce completeness without changing an otherwise correct interval. |
| SYN038 | 5 / 4 | Deadline, transfer-to-validation dependency, soft weekend preference, vendor-hours limit and rollback prerequisite are distinct. Vendor availability does not itself mandate vendor participation or prohibit weekend cutover. No new validation-before-cutover requirement. |
| SYN014 | 5 / 5 | Paired experience and start comparisons, A's higher salary request, B's stronger data skills and no overall winner. No invented salary amount, absent skill or hiring priority. Dimension-specific advantages do not select an overall winner. |
| SYN023 | 4 / 4 | Four principal event/day relations remain binary. The final Monday is the following week and marks analysis start. Chronological presentation is CHECK-02; no invented dates, durations or extra events. |
| PROC071 | 3 / 2 | Monthly source coverage, consistent organization and readable retrieval are distinct. Physical or digital paths are valid. An existing monthly set need not be collected again; no required spreadsheet, tax system or exact retention period. |
| PROC098 | 5 / 2 | Warning evidence, feasible fallback, activation rule, communication and recovery are distinct. A trigger links to a decision; numerical scoring and a separate decision-owner matrix are not compulsory. Recovery can replan downstream work rather than return to the same vendor. |
| PROC049 | 5 / 2 | Differing traveler inputs, feasible transport, actual lodging entry, communication and contingencies are distinct. Separate journeys and staggered pickup are valid. A room reservation alone does not establish access at each arrival time. |
| PROC074 | 5 / 2 | Inventory, need evidence, subscription disposition, timely authorized execution and future review are distinct. A keep/cancel decision does not itself execute it. Data/service continuity safeguards apply to access-removing cancellation; no blanket cancellation or exact savings target. |
| TECH041 | 3 / 0 | Interpreter selection, module presence and search visibility are distinct. External package and local module branches are both valid. No forced global install, administrator privileges, named environment manager or script rewrite. |
| TECH021 | 3 / 0 | Correct page/context, targeted refresh/cache check and browser/session comparison are distinct simple checks. No forced all-history deletion, server access, DNS changes or website edits. |
| TECH078 | 7 / 0 | A controlled Wi-Fi/cellular failure capture plus six named diagnostic areas. VPN need is conditional; corporate-only policy may be intentional. No disabling certificate validation, evading policy or exposing internal services. |
| TECH043 | 3 / 1 | Expected empty-input behavior, failing-path reasoning and small comparison cases are distinct. The correct result may be an empty result, neutral value or clear rejection. No invented algorithm, guaranteed indexing fault or required code patch. |
| TECH023 | 3 / 0 | Initial failure/change evidence, file access and safe format/integrity evidence are distinct candidate branches. Error detail or relevant change evidence can establish context. No automatic app reinstall, destructive repair or untrusted document upload. |

## Changes made during second pass

- **DEC083:** removed the initial standalone critical legal/contract/safety-dependency screening unit. The prompt supplies no particular binding obligation. Actually implicated dependencies belong in the current-effects assessment, without a compulsory expert compliance checklist. This changes four units/two critical to three units/one critical. Records and affected people are alternative sources for the forgotten purpose, rather than jointly mandatory research methods.
- **DEC018 / RIU-03, RIU-04 and RIU-06:** removed compulsory attendance-tracking mechanics and universal staggering. Full workforce coverage remains a categorical outcome. The assignment method can use one feasible session, repeated sessions or staggered cohorts. A staffing/space conflict must be identified rather than a late plan represented as deadline-compliant; any adjustment requiring authorization remains conditional. The half anchor now recognizes concrete sessions/cohorts/slots without a participant-assignment or conflict-resolution mechanism.
- **DEC094 / RIU-02:** replaced a universal early-validation-plus-independent-workstream prescription with a dependency-resolution checkpoint that conditions downstream milestones. Independent work is scheduled separately only where available. The half anchor names a concrete checkpoint lacking the downstream update rule. Evidence-producing learning and milestone gating retain different boundaries.
- **TECH041 / RIU-02:** accepted checking an expected local module's presence as well as external-package availability in the active interpreter. A package install is not required for a local-module failure. Module presence differs from whether the running interpreter can find it through its search path.
- **TECH023 / RIU-01:** made error details and relevant recent file/location changes alternative ways to establish initial failure context; both are not obligatory. This avoids turning a first-check request into an exhaustive evidence collection sequence.
- **PROC071 / RIU-01:** explicitly allowed identifying an already assembled month's receipts rather than requiring collection again. Month scope, sorting and readable retrieval remain distinct outcomes.
- **PROC098 / RIU-03:** removed a separate mandatory decision-owner specification from the activation anchor. A concrete point/trigger linked to a feasible continue/switch/escalate/replan decision is the central requirement; communication responsibility remains in its own unit. No additional role matrix is inferred.

The final draft has 90 RIUs rather than the first construction's 91, with 37 critical rather than 38. The four ordinal boundaries survive the second pass; no numerical fact, categorical constraint or discrete diagnostic check is made ordinal.

## Ordinal anchor audit

| Task / unit | Concrete 0.5 anchor | Full-credit distinction |
|---|---|---|
| CYBER029 / RIU-04 | Explicitly keeps the alert unresolved because legitimacy alone is insufficient, but gives no evidence-based rule for deciding false positive versus further compromise response; blanket suppression or dismissal scores 0. | Evidence determines a false-positive disposition or continued compromise investigation/response rather than merely preserving uncertainty. |
| DEC018 / RIU-06 | Proposes concrete sessions, cohorts or attendance slots but gives no method for assigning participants across shifts or resolving capacity/coverage conflicts; an explicitly infeasible schedule scores 0. | Provides a workable assignment/conflict-resolution mechanism rather than only a session structure. |
| DEC094 / RIU-02 | Places a concrete dependency-resolution checkpoint in the plan but gives no rule for how its result changes dependent milestones; an explicitly infeasible fixed sequence scores 0. | Makes dependent milestones conditional on the checkpoint's result. |
| PROC098 / RIU-03 | Identifies a concrete review time or warning threshold but does not specify the resulting continue, switch, escalate or replan decision. | Connects a decision point/trigger to feasible activation or continued-operation decisions. |

These are weaker fulfillments of the same disposition, allocation, milestone or activation requirement. They are not half credit for missing independent source facts, wrong times/numbers or vague topic mentions. Contradictions and unsafe actions defeating a unit override positive anchors. Full credit takes precedence whenever its anchor is met. In particular, naming a session or checkpoint is not sufficient for full procedural reasoning, while a wrong categorical constraint does not earn half credit merely because some surrounding prose is useful.

## Methodological observations

1. **Criticality follows omission consequences.** The router's administrator exposure and correction are both central. In CYBER034 the narrow restoration decision is critical; supporting discovery and testing steps are not all promoted because the domain is security-related. CYBER029's evidence-based disposition is critical because treating product legitimacy as exoneration would defeat the task. CYBER078 and four technical tasks have no uniquely indispensable individual evidence branch, despite their contribution to completeness. Zero-critical tasks are CYBER078, TECH041, TECH021, TECH078 and TECH023; core-task success is NA for these tasks. No domain proportion was used as a target.
2. **Feasibility differs from supporting considerations.** DEC018's staffing, room capacity, full population coverage and completion deadline are separate categorical feasibility outcomes. Its allocation mechanism converts constraints into assignments rather than earning duplicate credit for restating them. Fairness remains a supporting dimension under the same omission test used for earlier scheduling/allocation tasks. PROC049's transport and lodging-entry outcomes are critical; collecting all coordination inputs and describing communications/contingencies support the procedure without making one platform or group itinerary mandatory.
3. **Source comparisons retain their defining trade-offs.** SYN014 preserves both sides of the experience and availability contrasts as relational units; separating each candidate's number would fragment one comparison. Salary and data skills are different dimensions. Omitting either distorts the candidate trade-off, while endorsing an overall winner violates the explicit boundary. SYN023's four event/day relations constitute the requested short timeline, with ordering assessed separately. SYN071's correct interval remains feasible even if one individual availability explanation is omitted, so the three explanations are supporting.
4. **Extraction does not authorize invented scheduling rules.** SYN038 identifies weekday vendor support as a resource limit and weekend cutover as a preference. It does not establish that support must attend cutover. Validation after transfer and rollback copy before cutover are the supplied dependencies; validation before cutover may be sensible in some real migrations but is not a new source requirement here. The exact deadline is before expiry on December 31, without an invented year or clock cutoff.
5. **Alternative operational paths remain open.** CYBER034 permits a bounded correction or rollback instead of a mandatory exception. CYBER029 permits documented false-positive closure when evidence supports it and continued investigation when it does not. DEC091 can use a practical rain-tolerant option or a conditional change rule. DEC083 can retain a rule provisionally while obtaining evidence. PROC098 can change supplier, use an internal workaround or replan scope/time when feasible; none is guaranteed available. PROC074 can keep, reduce, consolidate or cancel subscriptions on need/value evidence.
6. **Diagnostic scope stays proportionate.** CYBER078's six named evidence targets and TECH078's six named cause areas remain independently assessable without a compulsory final cause attribution or full incident lifecycle. TECH078 includes one controlled failure comparison because Wi-Fi-versus-cellular behavior defines the task; this does not establish one specific fault. TECH041, TECH021 and TECH023 ask for first/simple checks, so global reinstalls, resets and invasive fixes are not required. TECH043 first establishes the behavior contract; an empty list is not necessarily invalid and its correct output cannot be invented.
7. **Language equivalence.** All 66 inspected strings preserve task objectives, factual values, uncertainty and constraints. CYBER031's Bengali plural change wording does not add a second password requirement. CYBER029 preserves a possible false positive, not an established benign event. DEC018 preserves 60 participants across shifts. DEC094's Bengali time-estimate wording is consistent with EN's milestones and commitments. SYN071 retains the afternoon windows and 30-minute duration; SYN014 retains five/two years and four weeks; SYN023 preserves the following Monday. BN-CS technical terms do not add products or tool requirements. No confirmed material difference requiring a language-specific RIU or frozen-prompt revision was established.

## Silence, safeguards and CHECK-01 consistency

All 22 unsupported-content checks copy accepted E1–E5 protocol 0.3 wording exactly. A material wrong assertion or unsafe instruction can fail both an RIU and CHECK-01; an RIU failure never suppresses the check. Pure omission or insufficient fulfillment alone is not a CHECK-01 failure.

Affirmative requirements need expressed content. A correct SYN071 interval does not itself express each requested availability explanation. Omitting a dependency-learning step loses its affirmative unit, even if the answer makes no unsupported claim. Conversely, a balanced SYN014 comparison satisfies the no-overall-winner constraint without saying "I will not choose." CYBER034's bounded positive restoration implements its negative scope constraint without a second warning RIU. CYBER029's positive evidence-based disposition likewise does not require a duplicate unit saying not to ignore compromise.

Conditional safeguards are satisfied by a protected action or a clearly reversible/non-destructive path. A diagnostic-only document procedure need not recite that it avoids overwriting the original; an unprotected destructive repair would be evaluated as an unsafe instruction. An access-removing subscription cancellation must account for needed data/service continuity, whereas a review or continued authorized subscription creates no unmet deletion safeguard. No action neither necessary nor proposed generates a missing conditional safeguard merely through silence. A genuine refusal/non-answer receives 0 on every RIU, including negative constraints.

Wrong meeting windows, experience amounts, start delays, event weekdays or dependency directions can fail their binary RIUs and CHECK-01. In SYN038, falsely asserting that weekend cutover is prohibited because vendor support is weekday-only adds an unsupported restriction. In TECH078, recommending disabled certificate validation or unauthorized policy bypass is an unsafe operational assertion. Correctly framed hypotheses about a suspect dependency, endpoint alert or file fault are not treated as confirmed facts. Timeline form is separate from both RIU coverage and material-error checks.

## Validation and preservation

All six required commands passed on the final E6 annotations:

```text
python3 scripts/validate_pilot_annotations.py --scope batch --annotation-dir data/annotations/expansion/E6
python3 scripts/validate_prompt_corpus.py
python3 scripts/freeze_prompt_corpus.py --check
python3 scripts/prepare_scaling_queue.py --check
python3 scripts/prepare_expansion_batches.py --check
python3 scripts/calibration.py check
```

Batch: 22 draft records, 90 RIUs, 37 critical, 53 supporting, 86 binary and 4 ordinal. Corpus: 500 tasks / 1,500 prompt instances. Freeze: 14 pinned files at v0.3.1. Queue: 25 frozen pilot / 132 expansion / 343 later tasks. Assignment: six prospectively fixed 22-task batches. Calibration: 30 authored fixtures / 229 answer-key rows; original AR 2026-10-19 ordinal-alpha point-estimate threshold 0.80 unchanged. Additional frozen-pilot validation passes: 25 frozen tasks, 159 RIUs, 80 critical, 138 binary and 21 ordinal.

Programmatic integrity checks cover exact 22-task membership, unique task/unit IDs, domain-file placement, manifest/corpus difficulty agreement, all 66 prompt hashes, 90 empty source-ID lists, exact zero anchors, description/full-anchor equality, binary null half anchors, four exact ordinal half anchors and the established review metadata. They also check identical accepted-rule CHECK-01 wording, the sole SYN023 timeline CHECK-02, task and domain/difficulty counts, the audit's ordinal list and prose exclusions.

All 99 pre-existing tracked-file SHA-256 hashes remain unchanged. Changes are limited to five E6 JSONL files and this audit. Frozen prompts/manifests, pilot gold/manifest, accepted E1–E5, calibration fixtures/answer key/preregistration/sign-off, protocol 0.3, scaling queue and expansion assignments are preserved. No production gold was assembled. Structural and integrity results establish those properties without constituting E6 acceptance.

Files added: `data/annotations/expansion/E6/cybersecurity_digital_safety.jsonl`, `decision_support.jsonl`, `information_synthesis.jsonl`, `procedural_instructional.jsonl`, `technical_troubleshooting.jsonl`, and `data/annotations/review_logs/2026-10-23_E6_draft_method_audit.md`.
