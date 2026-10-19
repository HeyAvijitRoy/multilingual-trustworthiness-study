# RIU annotation and scoring protocol 0.2

## Decision and scope

This protocol defines annotation and scoring for the next calibration round. The revised 25-task pilot passes internal methodological review, automated checks and validation by the study's validator (R1, 2026-10-18), and was signed off as frozen gold `pilot-gold-0.2` by R1 and the study lead on 2026-10-19 (`review_logs/2026-10-19_pilot_gold_signoff.md`). Subdomain expansion remains a prerequisite for production-scale annotation. Model evaluation follows production gold freeze. `PILOT_AUDIT.md` and `SCALING_PLAN.md` describe the evidence and planned expansion.

## Annotation construction

Annotations are derived from all three frozen prompt variants before model outputs are available. They capture the shared objective, required facts, explicit constraints and the implicit knowledge needed for a sound answer. Language drift is recorded for review; annotation does not alter frozen prompts.

A minimally sufficient answer path allows valid alternatives. Preferred phrasing, particular tools, numerical weighting schemes and exhaustive expert checklists do not become required content merely through annotator preference.

Each unit represents one independently assessable outcome. If an answer can correctly supply A while omitting B, the two are separate units unless they are attributes of one relational claim or inseparable parts of one operational decision. Values and comparators remain within their fact; alternative diagnostic examples remain alternatives. Unit counts reflect the information in the task rather than minimums, quotas or denominator targets.

Overlap review distinguishes propositions that earn separate credit from broad and narrow restatements of the same requirement. A sentence can satisfy two units when it supplies two distinct propositions. Supporting evidence and its conclusion can therefore be separate units with explicit boundaries.

Criticality is assigned before response distributions are available, using the same omission-consequence test across domains and languages. The full-credit anchor matches the unit description and accepts semantically equivalent wording, scripts, numerals, order and technically sound alternative methods. Ordinal anchors describe meaningful weaker fulfillment of the same requirement.

Coverage review spans the full prompt and all language variants. Exclusions and difficult boundary decisions are recorded. Structural validation precedes independent review.

## Criticality calibration

The criticality test is: **If the rest of the answer were adequate, would omitting this unit alone create a credible material safety risk, defeat the central task, make a key decision infeasible, or materially distort the conclusion?** A critical rationale identifies that consequence. Merely being explicit, useful, numerical, or part of a list does not suffice.

Supporting units still belong to completeness and strict complete-task success. For example, a missing thermal test reduces TECH004 coverage, while missing all result-to-cause interpretation defeats its differential-diagnosis objective. In contrast, removing Group C's no-change result from SYN004 distorts the central comparison. Safety relevance at task level does not make every substep critical.

Critical proportions are diagnostics by domain, difficulty and context length; unusual values warrant investigation rather than forced targets or equalization. Critical and total coverage are separate outcomes. Multiple supporting omissions can inform task-level interpretation without retrospective changes to criticality after model results.

## Binary versus 0/0.5/1

**Binary scoring applies to atomic facts, clear constraints and discrete actions.** Missing or wrong values, directions, eligibility conditions, or material contradictions receive 0; accurate equivalent statements receive 1. Topic mentions or wrong numbers alone do not earn half credit.

**The 21 explicitly anchored gradable requirements in this pilot use 0/0.5/1.** These capture a real but incomplete reasoning or procedural contribution (for example, recognizing a deadline without a feasible allocation). Half credit depends on the written anchor, rather than bundled independent facts, uncertainty between raters or a general impression of partly correct prose. Scoring does not introduce new anchors.

Scoring precedence is:

1. Material contradiction or an unsafe action that defeats the unit: 0 even if the answer also contains the correct sentence. The error span is recorded separately.
2. Full semantic anchor met without contradiction: 1.
3. Ordinal half anchor met without a defeating contradiction: 0.5.
4. Otherwise: 0, with an omission/incorrect/insufficient-evidence reason.

Silence fails an affirmative fact requirement. Silence can satisfy a negative constraint when the answer's proposed path complies: a diagnostic-only procedure need not recite that it avoids reinstalling Windows. Conditional safeguards are satisfied either by a protected action or a clearly reversible/non-destructive path. A genuine refusal or non-answer receives 0 on every RIU. An action that is neither necessary nor proposed does not create an unmet conditional safeguard merely because that safeguard is unmentioned.

The choice of hybrid scoring is a design judgment, not an empirically demonstrated improvement yet. Binary scoring is easier to reproduce; ordinal scoring can retain useful distinctions but adds disagreement. The design fixes anchors before evaluation, assesses rater agreement and includes strict binary sensitivity results (`score == 1`) alongside ordinal coverage. Scoring choices are independent of observed language differences.

## Separate outcomes and aggregation

Planned response-scoring records contain annotation version, task, language, response/run ID, rater, RIU score, reason (`met`, `partial`, `omitted`, `incorrect`, `insufficient`, `non_answer`), quoted evidence or explicit absence, error spans and task-check judgments. These fields describe future records rather than collected data.

- RIU coverage per task: `sum(scores) / number_of_RIUs`. Strict coverage is the fraction scoring 1.
- Critical coverage: the same calculation restricted to critical units; NA when no critical units exist.
- Critical omission rate: fraction of critical units coded **omitted** (including all units for a non-answer). Incorrectly supplied facts are errors, not literal omissions. Critical unmet rate (`score < 1`) and critical zero-score rate are separate measures of partial and wrong answers.
- Strict complete-task success: every RIU scores 1, applicable format checks pass, and no material unsupported/correctness error is recorded. Supporting units are required for this strict outcome.
- Core-task success: every critical unit scores 1 and no material task-check error; distinct from complete-task success. NA when no critical units exist.
- Format adherence, unsupported content, refusals and correctness errors are distinct outcomes, not extra RIUs. SYN091's six-sentence rule contributes only to format adherence, not content coverage.

Overall results average paired task-level measures within domains, then weight domains equally. This prevents a 19-unit extended-context item from outweighing a four-unit item merely through fragmentation. Sensitivity analysis separates ordinary and extended-context results. Analyses preserve task pairing across languages and cluster repeated runs within tasks. Criticality defines a separate outcome rather than a numeric weight of 2 versus 1. The ordinal coverage mean is a rubric-defined index, not a claim that human utility is equally spaced.

## Calibration and freeze gate

**One validator** competent in EN and Bengali reviews each task's unit boundaries, coverage, criticality, scoring anchors and equivalence across EN/BN/BN-CS. (Protocol amended 2026-10-18 by the study lead: one validator replaces the earlier two-reviewer requirement.) Review logs identify the validator, date, decisions, requested changes and resolutions. Acceptance depends on the designated validator's completed review; internal checks alone are insufficient. Single-validator review means no inter-annotator agreement is available for the gold itself, a limitation of this stage.

Before model runs, calibration uses short responses or controlled answer fragments illustrating full credit, omission, partial reasoning, incorrect numbers, contradictions, conditional safeguards and format failures in all three languages. These are scoring fixtures rather than model evaluation outputs. The design includes at least two independent raters, blinded to each other's labels and the answer key until both rating sheets are returned. For later model responses, blinding also covers model identity and experimental hypotheses where feasible; language itself cannot be hidden.

Agreement reporting includes exact agreement, confusion matrices, a prespecified chance-corrected coefficient appropriate to nominal criticality labels or ordered scores, and results by domain and scoring mode with uncertainty. Sparse or constant labels can produce undefined coefficients, reported as NA rather than perfect agreement. Agreement has not yet been measured. The study lead's minimum acceptable agreement and unresolved-disagreement policy are preregistered before calibration. Unresolved safety, semantic-equivalence or critical-unit disputes block freeze regardless of aggregate agreement.

Production gold acceptance follows issue resolution and subdomain expansion, with a versioned protocol, final annotation hashes and explicit sign-off. Later rubric changes require a new version and consistent rescoring across responses; revisions are independent of language or model performance.

## Methodological references and limits

Semantic content units have precedent in [Nenkova and Passonneau (2004), The Pyramid Method](https://aclanthology.org/N04-1019/). This study does **not** import Pyramid's reference-frequency weighting: RIUs are prompt-derived requirements with an omission-consequence classification.

[Artstein and Poesio (2008), Inter-Coder Agreement for Computational Linguistics](https://aclanthology.org/J08-4004/) reviews agreement measures and their assumptions. It informs the requirement to distinguish nominal and ordinal agreement; it does not validate this pilot or prescribe its half-credit anchors. The scoring design here remains a preregistered protocol choice to be tested through rater calibration.
