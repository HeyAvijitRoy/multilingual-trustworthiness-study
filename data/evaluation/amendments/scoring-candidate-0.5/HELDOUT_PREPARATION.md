# Held-out validation set for scoring candidate 0.5 — preparation record

Status: **reference frozen 2026-10-24 at 88 of 90 fixtures** (see [HELDOUT_MANIFEST.json](HELDOUT_MANIFEST.json); two fixtures unresolved and removed, no replacements written; stage-2 adjudication was not blind to intent). Originally construction drafts. Started 2026-10-24, after candidate 0.5 was hash-pinned at commit `5cee48a` ([CANDIDATE_PIN.json](CANDIDATE_PIN.json)). There are no reference labels, no accepted held-out set, and no candidate or judge inference. Production scoring remains blocked.

## Separation of stages

| Stage | Who | Produces | Access controls |
|---|---|---|---|
| A. Construction | AI constructor (Claude) under study-lead direction | 90 fixture families: prompt, synthetic response, rubric (RIUs, criticality, anchors, task checks), coverage tags; separately a sealed construction-intent file | Private, ignored `.local/heldout_validation_v05/`. Only hashes and aggregate counts are public. |
| B. Reference establishment | Independent human reviewer(s), EN/BN competent, not the constructor | Blind first-pass item scores with evidence. After unsealing intent: second-stage resolution of every reference/intent disagreement. Reference freeze manifest. | Reviewers receive fixtures and rubric **without** construction intent. Intent is revealed only after the first pass is returned and hash-recorded. |
| C. Validation exposure | Candidate operator | One inference pass per item, metrics via `scripts/scoring_validation_prepare.py` | Only after the reference freeze and a recorded spending/budget check. The candidate pin must be unchanged. |

A construction-intent label is a design target, not a reference. Fixtures whose human reference contradicts intent remain in the set with the human reference. Fixtures with a genuinely unresolved reference are removed **before** the reference freeze, the removal is logged, and they are replaced from a new family. Denominators are frozen at Stage B, never after Stage C.

### Independence limitation, disclosed in advance

The same AI agent drafted candidate 0.5 and is constructing these fixtures. The candidate was pinned first, and fixture coverage follows the pre-existing [scoring-validation plan](../../remediation/v03_R1_adjudication/SCORING_VALIDATION_PLAN.md). Even so, the constructor knows the candidate's rules, so fixtures may unintentionally favor or disfavor them. Mitigations:

1. Human references are blind to intent.
2. Coverage includes counterexamples where the clarified rules must not exempt unsafe content.
3. Any candidate change after construction begins marks this set as exposed for that new candidate.
4. The study lead may substitute or add human-constructed families before the Stage B freeze.

A validation pass on this set should be reported as "held out from candidate development; constructed by the candidate's author; references independent".

## Design (fixed before construction)

- **Strata.** 90 families: 5 domains × 3 languages (EN, BN, BN-CS) × 6. Each stratum holds 2 acceptable, 2 unacceptable and 2 borderline families, by construction intent. Every family is a distinct scenario; no translated variant of another fixture. Scenarios are new and are checked automatically for n-gram overlap against all 1,500 frozen study prompts.
- **Rubric.** Annotation schema 0.2 conventions. Each fixture has 4 RIUs, at least 2 of them critical, and at least one binary and one ordinal RIU across each stratum. Ordinal RIUs carry a concrete written half anchor. That gives at least 360 RIU judgments and at least 180 critical judgments, against the plan's floors of 300 and 150.
- **Safety checks.** The original gate's definition is kept: every task check of a fixture whose `safety_relevance` ≠ `none` is safety-related. All held-out fixtures have `safety_relevance` ≥ `low`, and each has CHECK-01 (unsupported content) as its designated primary check. Some also carry a format CHECK-02, which is frozen and counted too. That gives at least 90 safety-related checks.
- **Coverage tags.** Distributed across strata:
  - `negative_constraint_silent_compliance`, `negative_constraint_violation`;
  - `conditional_safeguard_protected_path`, `omitted_required_safeguard`;
  - `nonmaterial_secondary_inaccuracy`, `material_primary_error`, `false_safety_property`, `inherently_unsafe_instruction`;
  - `policy_choice_defeats_riu`;
  - `multi_conjunct_format_partial`, `multi_conjunct_format_met`;
  - `distributed_vs_integrated_rule`, `ordinal_half_credit`;
  - `contradiction`, `nonanswer_refusal`, `partial_fulfillment`.
- **Language.** Prompts and responses follow the [corpus language guide](../../../prompts/LANGUAGE_GUIDE.md): BN in Bengali script with Bengali digits; BN-CS Bengali-matrix with Latin-script domain terms. The checker applies the corpus script-share bounds.

## Reproducible checks

```sh
python3 scripts/heldout_validation_v05.py check     # schema, strata, denominators, scripts, overlap
python3 scripts/heldout_validation_v05.py manifest  # writes the public hash/aggregate manifest
python3 scripts/heldout_validation_v05.py packet    # blind Stage-B reviewer packet (no intent), private
```

The checker reads only the private construction files and the frozen prompt corpus. It has no transport, and it writes no labels.
