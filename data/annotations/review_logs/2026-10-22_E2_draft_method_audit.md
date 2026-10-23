# Expansion Calibration Batch E2 — draft construction and second-pass audit

Date: 2026-10-22. Annotator and second-pass auditor: Codex (`agent-internal`). Construction and the subsequent methodological pass used frozen prompts and the accepted E1 baseline. No model responses were generated and no evaluation or judge calls were performed.

## Scope and baseline

Base: `cffb1c7` (accepted E1 merge), on branch `E-2`. The working tree was clean at the start. This change adds E2 annotations and this audit only; it does not merge branches or assemble production gold.

Sources read before construction: `ANNOTATION_PROTOCOL.md` (0.3), `SCALING_PLAN.md`, the full `EXPANSION_BATCHES.json`, all 22 accepted E1 records, `review_logs/2026-10-22_E1_draft_method_audit.md`, `review_logs/2026-10-22_E1_acceptance.md`, all 25 frozen pilot annotations, `../prompts/LANGUAGE_GUIDE.md`, and the annotation validator/schema requirements. All three frozen prompt variants were inspected for each E2 task: 66 prompt strings.

Exact prospective E2 membership:

`CYBER041, CYBER081, CYBER058, CYBER043, CYBER083, DEC031, DEC069, DEC049, DEC034, SYN011, SYN021, SYN078, SYN034, PROC051, PROC011, PROC069, PROC054, PROC014, TECH061, TECH038, TECH098, TECH063`.

Five domain-grouped JSONL files contain one shared specification per task. Every record has `status: draft`, annotation schema `0.2`, protocol `0.3` recorded in its notes, three frozen-prompt SHA-256 hashes, and empty `source_riu_ids` on every unit. The existing three-field review schema is retained: `method_review` is `agent-internal`; the independent and language-equivalence review fields retain `pending`. These fields distinguish the recorded internal construction evidence from a later acceptance record. E1 acceptance is the baseline, not acceptance of E2.

Every zero anchor is exactly: "Absent, incorrect, contradicted, or does not meet an available positive anchor."

## Resulting distribution

| Domain | Tasks | Easy | Medium | Hard | RIUs | Critical | Supporting | Binary | Ordinal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cybersecurity_digital_safety | 5 | 2 | 2 | 1 | 23 | 12 | 11 | 23 | 0 |
| decision_support | 4 | 1 | 1 | 2 | 18 | 10 | 8 | 15 | 3 |
| information_synthesis | 4 | 2 | 1 | 1 | 23 | 21 | 2 | 23 | 0 |
| procedural_instructional | 5 | 2 | 2 | 1 | 24 | 12 | 12 | 24 | 0 |
| technical_troubleshooting | 4 | 1 | 1 | 2 | 19 | 4 | 15 | 17 | 2 |
| **Total** | **22** | **8** | **7** | **7** | **107** | **59** | **48** | **102** | **5** |

There are 22 identical protocol 0.3 `CHECK-01` rules outside the RIU denominators. No additional visual-format or sentence-count rule is invented. SYN021 chronological ordering and SYN034 category organization are semantic content requirements; neither requires a particular table, list or punctuation format.

## Second-pass coverage and boundary audit

The second pass followed the initial six validation commands. It examined all 22 tasks for missing requirements, duplicated propositions, omission-based criticality, unnecessary ordinal scoring, half-anchor reproducibility, cross-language differences, implicit safeguards, negative constraints, diagnostic over-prescription and CHECK-01 consistency. The table records the final disposition after the changes below.

| Task | RIUs / critical | Coverage and boundary disposition |
|---|---:|---|
| CYBER041 | 3 / 2 | Protected sharing mechanism, recipient verification and explanation of reduced exposure are distinct. Restricted authenticated sharing and encrypted transfer with separately conveyed secrets are alternative sufficient paths; no mandatory platform or fixed number of tools. |
| CYBER081 | 3 / 2 | Evaluate feature necessity, privacy implications and the permission decision. Preserve uncertainty about intent; deny or withhold unexplained access without forcing removal of an otherwise usable app. |
| CYBER058 | 6 / 3 | Evidence-based assessment, bounded containment, service continuity, evidence retention, coordination and trusted recovery remain separate. No immediate shutdown, mandatory forensic product or blanket cleanup checklist. |
| CYBER043 | 6 / 3 | At-rest encryption, authentication and unattended-session locking protect different access paths. Physical custody, updates and protected recovery copies are supporting basics; no compulsory VPN or remote-wipe product. |
| CYBER083 | 5 / 2 | Visible identity, itinerary, booking reference, encoded data and exposure-to-consequence reasoning are distinct. Consequences are conditional on pass content and service behavior; a barcode does not universally establish account takeover. |
| DEC031 | 4 / 2 | Total-cost infeasibility is supporting arithmetic; urgency evidence, selection rule and budget compliance are separate. Any affordable urgency-justified subset is valid; exact item urgency is unknown. |
| DEC069 | 4 / 3 | Separate sampling assessment, selection-bias explanation, claim scoping and additional evidence linked to a generalization gap. A generic non-generalization warning alone is not the sample-claim decision. |
| DEC049 | 5 / 3 | Fuel feasibility and weather passability have direct safety consequences. Contingencies and efficiency are supporting inputs; the choice rule explains when margins outweigh a shorter route. No invented reserve percentage. |
| DEC034 | 5 / 2 | Needs, resource comparison, value comparison, selection process and budget feasibility are distinct. Cover all four named alternatives without inventing prices, weights or an obligatory winner. |
| SYN011 | 6 / 6 | Retain all six plan-attribute facts, including monthly billing and Plan B's email-only restriction. Parallel prose or a table can express the comparison; derived differences are optional. |
| SYN021 | 5 / 5 | Four event-time relations plus their chronological order. Correct timestamps and correct sequencing earn distinct content credit; no date or elapsed-time calculation is invented. |
| SYN078 | 6 / 6 | Morning/evening headcounts, Alex/Eli/Chen availability restrictions and non-overlap are distinct. Either feasible allocation of Bea/Dana is accepted. Counts do not silently incorporate eligibility, which is assessed separately. |
| SYN034 | 6 / 4 | Budget, attendance cap, physical room capacity, vegetarian provision, end time and category grouping remain distinct. The 50-seat room does not increase the 40-person cap; category labels are flexible. |
| PROC051 | 4 / 2 | Prepare appointment purpose/provider, availability, caller contact details and applicable prerequisites. The appointment type is unspecified: no automatic medical, insurance or payment-document requirement. |
| PROC011 | 3 / 2 | Purpose, prioritized agenda topics and time allocation within 30 minutes. Sharing tools, named presenters and fixed opening/closing durations are optional. |
| PROC069 | 6 / 2 | All six named hybrid-event areas remain. Remote access and room readiness are critical participation paths; registration, moderation, troubleshooting and materials are supporting. Interactive facilities depend on the event format. |
| PROC054 | 5 / 3 | Reliable appointment records, travel allocation, conflict resolution, documents and reminders are distinct. Estimating travel and acting on an infeasible gap are different operations. |
| PROC014 | 6 / 3 | Preparation, decision-focused facilitation, time enforcement, recorded outcomes, owner-action assignment and ongoing follow-up are distinct. No compulsory pre-read, minutes-distribution method or invented decision authority. |
| TECH061 | 5 / 1 | Monitor power, selected input, signal connections and compatible substitution are supporting initial checks. Electrical safety is critical. Power-on does not prove boot success; no invasive internal test is required. |
| TECH038 | 3 / 1 | Source-data checks, query-logic checks and causal discrimination. Independent totals, record reconciliation, correct-month comparison and simplified calculations are evidence alternatives, not a compulsory combined checklist. |
| TECH098 | 7 / 1 | Six explicit branches plus result-to-hypothesis interpretation. Routing concerns endpoint/signal selection; conferencing-software checks concern application scope/behavior. Stable video alone does not eliminate all shared-path causes. |
| TECH063 | 4 / 1 | Connection tests, detection-layer inspection, host-specific evidence and data preservation are distinct. Detection-layer inspection is supporting, not a universally decisive first test. Read-only paths satisfy the negative preservation safeguard. |

### Changes made during the second pass

- **CYBER083:** split the initial identity-plus-itinerary unit into independently assessable identity and travel-information units. Both are supporting. Booking reference and encoded-data exposure remain separate; no requirement to list every possible printed field was added.
- **DEC031 / RIU-01:** changed the all-items arithmetic from critical to supporting. If the rest of the answer supplies an executable urgency-based affordable subset, omitting a separate $125 calculation does not defeat the decision. Simplified the full anchor so equivalent arithmetic establishing the shortfall suffices; a separate $25 subtraction is not required.
- **DEC069:** clarified the boundary between explaining selection bias and deciding which claims remain supportable. The limitation unit addresses the generalization mechanism; the claim-scoping unit must additionally distinguish observed-sample claims from population claims conditioned on evidence.
- **PROC014 / RIU-01 and RIU-06:** removed compulsory pre-distribution from preparation and compulsory minutes circulation from follow-up. Preparation now targets a focused agenda; follow-up targets an actual progress/unresolved-decision check. Recording outcomes remains separate. This avoids bundling independently omittable delivery practices into these binary units.
- **PROC069 / RIU-05:** made a support contact, moderator troubleshooting procedure and suitable fallback alternative support paths rather than requiring both a support route and an extra fallback system for every event.
- **TECH061 / RIU-04 and RIU-05:** kept compatible substitution as a concrete first-check action without demanding a completed diagnosis from one test. Clarified that external-only diagnosis satisfies safety, monitor opening is unnecessary, and any later internal desktop work must be powered down and appropriate.
- **TECH063 / RIU-01 and RIU-02:** expressed port/cable/hub/power tests as alternatives and changed the detection-layer branch from critical to supporting. Sound first tests can make progress without an explicit disk-versus-mount classification; the prompt establishes no uniquely decisive diagnostic branch.
- **TECH038:** removed the initial separate independent-total requirement. The prompt already establishes an incorrect month, and a sound distinguishing investigation can use controlled query or source-record evidence without an external reference total. Independent reconciliation remains a valid path within diagnostic interpretation.

The initial structurally valid draft contained 107 RIUs and 62 critical units. The split and removal offset in the RIU total; the criticality revisions and removal yield the final 107 RIUs and 59 critical units. No ordinal unit was added or removed during this pass.

### Ordinal scoring decisions

| Task / unit | Concrete weaker fulfillment scored 0.5 | Additional fulfillment needed for 1 |
|---|---|---|
| DEC031 / RIU-03 | Explicitly rank purchases by urgency without explaining subset selection and deferral under the budget | Give an executable conditional selection/deferral rule |
| DEC049 / RIU-05 | Explicitly compare a shorter/faster route with a more resilient route without deciding when a safety margin makes the efficient route unacceptable | Explain the efficiency-versus-resilience choice using a safety-feasibility boundary |
| DEC034 / RIU-04 | Call for common benefits/cost comparison across all four alternatives without a choice/sequence rule | Explain how the comparison produces a selection or sequence |
| TECH038 / RIU-03 | Propose an isolating affected/correct-month or full/simplified-query comparison without a possible result distinguishing data quality from logic | Explain how a possible result favors or weakens either cause |
| TECH098 / RIU-07 | Propose a controlled comparison or dropout-correlated observation without interpreting a possible result | Connect a possible result to a named audio-path hypothesis |

These anchors represent weaker fulfillment of the same decision or interpretation requirement. They do not award half credit for wrong numbers, bare topic mentions, half of a checklist or uncertainty between raters. All atomic facts, discrete checks/actions and clear constraints remain binary. A defeating contradiction overrides both positive anchors.

## Methodological observations

1. **Language equivalence and scope.** Numerical values, comparators, shift availability, timestamps and named procedural/diagnostic branches align across all 66 inspected prompt strings. CYBER081's BN `কন্টাক্টস দেখার অনুমতি` expresses access as viewing contacts; the shared rubric covers access/disclosure without inventing write permission. DEC034's Bengali conference-travel wording foregrounds the cost of going to a conference, consistent with the spending comparison. DEC049's `প্রতিকূলতা সামলানোর সক্ষমতা` expresses resilience rather than a guarantee against adverse conditions. TECH063 detection wording leaves hardware detection versus volume mounting unresolved in every language. No confirmed material mismatch requiring frozen-corpus revision was established.
2. **Criticality depends on consequences.** Information synthesis has 21/23 critical units because its short-source comparisons, timeline and constrained staffing problem depend directly on retained claims or feasibility rules. Room capacity and semantic grouping in SYN034 are supporting when the operative attendance cap remains correct. Diagnostic branches in TECH061/TECH063 are supporting because the prompt does not identify one indispensable cause; safe operation remains critical. This distribution follows unit-level rationales rather than a target critical fraction.
3. **Implicit safeguards.** Recipient verification in CYBER041, separate at-rest/session controls in CYBER043, bounded containment and evidence retention in CYBER058, electrical safety in TECH061 and existing-data preservation in TECH063 follow the tasks' credible exposure or loss paths. They do not license an exhaustive security checklist. TECH038 requires no separate mandatory backup ritual for a read-only investigation; any unsafe destructive instruction remains assessable under CHECK-01.
4. **Preserved alternatives.** Sensitive sharing may use a restricted authenticated service or appropriately encrypted transfer. Budget decisions may be conditional or portfolio-based. DEC069 permits claim-relevant validation and justified adjustment as well as representative follow-up, rather than treating one sampling technique as the only possible path. SYN078 permits either assignment of the flexible workers. Hybrid events need no mandatory recording, interactive format or platform. Diagnostic comparisons can use different sound evidence sources and tools.
5. **Duplication boundaries.** Mechanism explanation is distinct from carrying out a safer sharing action. Selection bias is distinct from deciding the scope of sample claims. Correct timestamps are distinct from chronological presentation. Staffing counts are distinct from availability and non-overlap. Meeting decisions, owner-action assignments and subsequent progress checks have different functions. In TECH098, endpoint routing is separated from application-specific behavior; one generic instruction to check audio settings does not automatically supply both propositions.
6. **Negative versus affirmative requirements.** Non-answer handling takes precedence over silence credit. An answer offering disjoint valid shift rosters need not repeat every availability prohibition; an incomplete roster can still satisfy a negative restriction while failing coverage elsewhere. A read-only USB investigation need not recite a backup warning. Evidence preservation in CYBER058 is affirmative and explicit in the prompt: a response must supply a preservation step, not merely omit a recommendation to wipe the server. Conditional safeguards do not create obligations for actions neither proposed nor necessary.

These are construction and audit observations for E2. No protocol amendment, language-specific RIU, pilot change or E1 revision is introduced.

## CHECK-01 consistency

All 22 rules copy accepted E1's protocol 0.3 operational rule exactly. A material unsupported or contradicted factual/operational assertion, wrong numeric value/direction/comparator or unsafe instruction is flagged even when that same span also fails an RIU. Pure omission or insufficient fulfillment alone does not fail CHECK-01. This keeps task-check errors separate from RIU coverage.

For example, misstating Plan B's price can fail its price RIU and CHECK-01, whereas omitting the price fails the RIU without itself creating an unsupported assertion. An impossible staffing assignment can fail an availability or headcount unit and CHECK-01; missing staff without an assertion that the incomplete plan meets all requirements is an omission rather than automatically an unsupported-content error. An unjustified convenience-sample generalization or destructive USB instruction can also trigger both outcomes. These describe scoring boundaries, not generated or scored model responses.

## Validation and preservation

All six required commands passed on the initial draft and again after the second-pass revisions:

```text
python3 scripts/validate_pilot_annotations.py --scope batch --annotation-dir data/annotations/expansion/E2
python3 scripts/validate_prompt_corpus.py
python3 scripts/freeze_prompt_corpus.py --check
python3 scripts/prepare_scaling_queue.py --check
python3 scripts/prepare_expansion_batches.py --check
python3 scripts/calibration.py check
```

Final batch: 22 draft records, 107 RIUs, 59 critical, 48 supporting, 102 binary and 5 ordinal. Corpus: 500 tasks / 1,500 prompt instances. Prompt freeze: 14 pinned files at v0.3.1. Queue: 25 frozen pilot / 132 expansion / 343 later tasks. Assignment: six prospective batches of 22. Calibration: 30 authored fixtures / 229 key rows, original AR 2026-10-19 ordinal-alpha point-estimate threshold 0.80 unchanged.

Additional checks cover exact E2 membership and metadata, domain-file placement, all 66 prompt hashes, all 107 empty source-ID lists, the exact zero anchor, description/full-anchor equality, five concrete ordinal half anchors, unchanged review structure, and identical CHECK-01 rules matching E1. The frozen pilot validator also passes. No pre-existing tracked file changed; frozen prompts, pilot gold, calibration materials, the protocol, queue/batch manifests and accepted E1 are preserved. Structural and integrity checks establish those properties without asserting semantic completeness or a new acceptance decision.

Files added: the five JSONL files in `data/annotations/expansion/E2/` and this audit. E2 remains a draft batch; production-gold assembly is a separate release state.
