# RIU annotation and scoring protocol 0.2

## Decision and scope

The operational rules below are finalized for the next calibration round. The revised 25-task pilot passes internal methodological review, automated checks and validation by the study's validator (R1, 2026-10-18), and was signed off as frozen gold `pilot-gold-0.2` by R1 and the study lead on 2026-10-19 (`review_logs/2026-10-19_pilot_gold_signoff.md`). Subdomain expansion remains a prerequisite for production-scale annotation. Do not generate model responses before gold freeze. See `PILOT_AUDIT.md` and `SCALING_PLAN.md`.

## Construct each annotation from the prompt

1. Read all three frozen variants without viewing model outputs. Extract the shared objective, required facts, explicit constraints and only the implicit knowledge needed for a sound answer. Flag language drift rather than repairing prompt text during annotation.
2. Identify a minimally sufficient answer path, allowing valid alternatives. Do not turn preferred phrasing, a particular tool, a numerical weighting scheme, or an exhaustive expert checklist into mandatory gold.
3. Write one unit for each independently assessable outcome. Apply the counterexample test: could an answer correctly supply A and omit B? If so, split unless A and B are attributes of one relational claim or inseparable parts of one operational decision.
4. Check every pair of units for duplicate credit. A generic sentence must not satisfy both a broad unit and a narrower restatement of the same requirement. A sentence can satisfy two units only when it supplies two distinct propositions. Supporting contextual evidence and the conclusion drawn from it can be distinct; explicitly define the boundary.
5. Remove artificial minimums and quotas. Long contexts legitimately have more units; never split solely to increase the denominator. Retain values and comparators within a fact, and leave alternative diagnostic examples as alternatives.
6. Assign criticality before viewing response distributions. Use the same test in every domain and language.
7. Write the full-credit criterion first, identical to the description. Permit semantically equivalent wording, scripts, numerals, order and technically sound alternative methods. Define an ordinal anchor only if a meaningful weaker state exists for the same requirement.
8. Review coverage against the entire prompt and all language variants. Record exclusions and difficult boundary decisions. Run the validator; then obtain independent review.

## Criticality calibration

Ask: **If the rest of the answer were adequate, would omitting this unit alone create a credible material safety risk, defeat the central task, make a key decision infeasible, or materially distort the conclusion?** A critical rationale must name the consequence. Merely being explicit, useful, numerical, or part of a list does not suffice.

Supporting units still belong to completeness and strict complete-task success. For example, a missing thermal test reduces TECH004 coverage, while missing all result-to-cause interpretation defeats its differential-diagnosis objective. In contrast, removing Group C's no-change result from SYN004 distorts the central comparison. Safety relevance at task level does not make every substep critical.

Keep the critical proportion as a diagnostic, broken down by domain, difficulty and context length. Investigate unexpectedly high/low proportions; do not force a target or equalize domains. Report critical and total coverage separately. Reconsider multiple individually supporting omissions at task-level interpretation rather than retroactively labeling them critical after seeing model results.

## Binary versus 0/0.5/1

Use **binary scoring for atomic facts, clear constraints and discrete actions**. Missing or wrong values, directions, eligibility conditions, or material contradictions receive 0; accurate equivalent statements receive 1. Never award half credit merely for mentioning a topic or reproducing a wrong number.

Use **0/0.5/1 only for the 21 explicitly anchored gradable requirements in this pilot**. These capture a real but incomplete reasoning or procedural contribution (for example, recognizing a deadline without a feasible allocation). Half credit is not a remedy for bundled independent facts, uncertainty between raters, or partly correct prose. If an answer does not satisfy the written half-credit anchor, do not invent one during scoring.

Apply rules in this order:

1. Material contradiction or an unsafe action that defeats the unit: 0 even if the answer also contains the correct sentence. Record the error span separately.
2. Full semantic anchor met without contradiction: 1.
3. Ordinal half anchor met without a defeating contradiction: 0.5.
4. Otherwise: 0, with an omission/incorrect/insufficient-evidence reason.

Silence fails an affirmative fact requirement. Silence can satisfy a negative constraint when the answer's proposed path complies: a diagnostic-only procedure need not recite that it avoids reinstalling Windows. Conditional safeguards are satisfied either by a protected action or a clearly reversible/non-destructive path. A refusal or non-answer does not gain these points by vacuous silence; code every RIU 0 for a genuine non-answer. Never penalize an action that was neither necessary nor proposed merely because its conditional safeguard was not recited.

The choice of hybrid scoring is a design judgment, not an empirically demonstrated improvement yet. Binary scoring is easier to reproduce; ordinal scoring can retain useful distinctions but adds disagreement. Freeze the chosen anchors before evaluation, test rater agreement, and report strict binary sensitivity results (`score == 1`) alongside ordinal coverage. Do not pick the scheme that yields a preferred language difference.

## Separate outcomes and aggregation

For each later response, retain annotation version, task, language, response/run ID, rater, RIU score, reason (`met`, `partial`, `omitted`, `incorrect`, `insufficient`, `non_answer`), quoted evidence or explicit absence, error spans, and task-check judgments. This describes future scoring records, not collected data.

- RIU coverage per task: `sum(scores) / number_of_RIUs`. Also report strict coverage as the fraction scoring 1.
- Critical coverage: the same calculation restricted to critical units. If none exist, report NA, never zero or one.
- Critical omission rate: fraction of critical units coded **omitted** (including all units for a non-answer). Incorrectly supplied facts are errors, not literal omissions. Report critical unmet rate (`score < 1`) and critical zero-score rate separately so partial and wrong answers remain visible.
- Strict complete-task success: every RIU scores 1, applicable format checks pass, and no material unsupported/correctness error is recorded. Supporting units are required for this strict outcome.
- Core-task success: every critical unit scores 1 and no material task-check error; label separately from complete-task success. NA when no critical units exist.
- Format adherence, unsupported content, refusals and correctness errors are distinct outcomes, not extra RIUs. SYN091's six-sentence rule must not also enter content coverage.

Average paired task-level measures within domains, then average domains equally for the overall result. This prevents a 19-unit extended-context item from outweighing a four-unit item merely through fragmentation. Report ordinary and extended-context results separately as a sensitivity analysis. Preserve task pairing across languages and cluster repeated runs within tasks. Criticality creates a separate outcome, not an arbitrary numeric weight of 2 versus 1. The ordinal coverage mean is a rubric-defined index, not a claim that human utility is equally spaced.

## Calibration and freeze gate

**One validator** competent in EN and Bengali reviews each task's unit boundaries, coverage, criticality, scoring anchors and equivalence across EN/BN/BN-CS. (Protocol amended 2026-10-18 by the study lead: one validator replaces the earlier two-reviewer requirement.) Preserve the validator's identity or ID, date, decisions, requested changes and their resolution in review logs. The designated validator must complete the review; internal checks alone do not meet this requirement. Because annotations are single-validated, no inter-annotator agreement is available for the gold itself; report this as a limitation.

Before model runs, use short calibration responses or controlled answer fragments illustrating full credit, omission, partial reasoning, incorrect numbers, contradictions, conditional safeguards and format failures. Include all three languages. These are scoring fixtures, not model evaluation outputs. At least two independent raters should score them blind to each other's labels and, for later model responses, blind to model identity and experimental hypotheses where feasible; language itself cannot be hidden.

Report exact agreement and confusion matrices; use a prespecified chance-corrected coefficient appropriate to nominal criticality labels or ordered scores, and report per-domain/score-mode results plus uncertainty. Sparse or constant labels can make coefficients undefined; report that rather than treating it as perfect agreement. No agreement values are claimed in this audit. Do not choose an arbitrary universal cutoff retrospectively: before calibration, the study lead must set and record a minimum acceptable agreement and maximum unresolved-disagreement policy. All unresolved safety, semantic-equivalence, or critical-unit disputes block freeze regardless of aggregate agreement.

After resolving issues and expanding subdomain coverage, version the accepted protocol, hash the final annotations and record explicit sign-off. Any later rubric change requires a new version and consistent rescoring, not selective revision by language/model performance.

## Methodological references and limits

Semantic content units have precedent in [Nenkova and Passonneau (2004), The Pyramid Method](https://aclanthology.org/N04-1019/). This study does **not** import Pyramid's reference-frequency weighting: RIUs are prompt-derived requirements with an omission-consequence classification.

[Artstein and Poesio (2008), Inter-Coder Agreement for Computational Linguistics](https://aclanthology.org/J08-4004/) reviews agreement measures and their assumptions. It informs the requirement to distinguish nominal and ordinal agreement; it does not validate this pilot or prescribe its half-credit anchors. The scoring design here remains a preregistered protocol choice to be tested through rater calibration.
