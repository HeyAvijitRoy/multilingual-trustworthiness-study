# Scoring calibration: fixtures and two-rater agreement

This stage tests whether two raters, working independently with the frozen pilot gold (`pilot-gold-0.2`), score the same response the same way. It follows the "Calibration and freeze gate" section of `../annotations/ANNOTATION_PROTOCOL.md`. Fixtures are scoring test material, not model outputs. No model is called at any step.

## Current status

Calibration is **signed off and complete as of 2026-10-22**.

Round 1: R2 and R3 independently scored all 229 items across the 30 fixtures. The preregistered agreement result is preserved unchanged: RIU exact agreement 192/196 (97.96%), Cohen's κ 0.917, ordinal Krippendorff's α 0.959 (95% fixture-bootstrap CI 0.901–1.000), and strict-binary κ 0.957. The preregistered α ≥ 0.80 point-estimate gate was met.

Round 1 exposed 10 score disagreements. Protocol 0.3 then clarified CHECK-01/RIU orthogonality without changing any frozen prompt, RIU boundary, criticality label, RIU scoring anchor, fixture response or `pilot-gold-0.2` record. Three inconsistent CHECK-01 answer-key entries (F04, F14, F24) were corrected.

R2 and R3 independently rerated only the 10 disputed items. All three formerly disputed critical RIUs and all six targeted CHECK-01 scores converged. The sole remaining supporting-unit score dispute, F26/PROC001/RIU-03, was adjudicated as 1/`met` under the frozen negative-constraint anchor. F17/DEC004/RIU-05's agreed score of 0 was adjudicated with reason `omitted`. No unresolved critical, safety or semantic-equivalence score dispute remains.

Final records:
- [Calibration adjudication](../annotations/review_logs/2026-10-22_calibration_adjudication.md)
- [Calibration sign-off](2026-10-22_CALIBRATION_SIGNOFF.md)

**Decision: PROCEED TO EXPANSION CALIBRATION.**

On 2026-10-19, before calibration ratings, F26's omission targets were corrected from `RIU-01;RIU-03` to `RIU-01;RIU-05` to match the existing response and intended scores. RIU-03 remains full credit under its extension-preservation anchor. This corrects target metadata; the response text, numeric scores and frozen gold are unchanged.

## Calibration design

The study lead's agreement threshold is preregistered in `AGREEMENT_PREREG.json` before rating begins. Its fields identify the study lead, date, minimum agreement, primary coefficient and decision statistic (`point_estimate` or `ci_lower_95`). Thresholds dated after the first rating are ineligible for a pass/fail verdict.

The fixture set follows the 30 slots in `fixture_plan.csv`. The answer key records intended scores for at least the target items. **Raters do not have access to the answer key until both rating sheets have been returned.** Fixture authors are excluded from rating their own fixtures because they know the intended scores.

Each rater receives a separate packet containing prompts, responses and anchors in a rater-specific order, together with a matching CSV sheet. Ratings are independent, with no discussion between raters before both sheets are returned. Every unit and task check receives a score, rating date, reason and evidence.

Agreement analysis compares the two completed sheets. Disagreements involving critical units, safety or semantic equivalence require adjudication, with resolutions recorded in `../annotations/review_logs/`. Anchor changes produce a new gold version; `pilot-gold-0.2` remains immutable.

`scripts/calibration.py` provides file validation, packet generation, returned-sheet intake, agreement analysis and an adjudication working sheet. Generated packets, returned sheets and reports live under `.local/calibration/` and are ignored by Git. See [`RETURN_WORKFLOW.md`](RETURN_WORKFLOW.md) for the exact handoff procedure.

## Fixture characteristics

Each response represents a plausible answer in its assigned language (`en`, `bn` or `bn_cs`) and the same register as the frozen prompt. The `author_id` field identifies its author. Target items carry the intended scoring phenomenon; the rest of the response exercises ordinary units as well. Scoring covers **every** unit and task check for the task.

| `phenomenon` | Intended response characteristics at `target_items` |
|---|---|
| `full_credit` | Meets every unit, using paraphrase, different order or different but valid methods rather than the anchor wording. |
| `omission` | Leaves the target units out entirely, with no contradicting text. |
| `partial_reasoning` | Meets the target's 0.5 anchor exactly, not the 1 anchor. |
| `incorrect_number` | States a wrong value, direction or comparator for the target fact (score 0 rather than 0.5). |
| `contradiction` | States the correct content and also contradicts it, or proposes an unsafe action that defeats the unit (rule 1 of the scoring order). |
| `conditional_safeguard` | Tests the silence rule: a protected or clearly non-destructive path without reciting the safeguard scores 1; a risky action without protection scores 0. The key identifies the intended case. |
| `format_failure` | Breaks the task's format check (`CHECK-02`), for example seven sentences instead of six, while the content units remain scorable. |

## Files

| File | Who writes it | Contents |
|---|---|---|
| `fixture_plan.csv` | Study lead | Prespecified 30-slot plan: 10 per language, 6 per domain, every phenomenon in every language; the F26 metadata correction is recorded above. |
| `fixtures.csv` | Fixture authors | `fixture_id, author_id, authored_date, response_text` |
| `answer_key.csv` | Fixture authors | `fixture_id, item_id, intended_score, intended_reason, author_id, note` |
| `AGREEMENT_PREREG.json` | Study lead | Threshold, coefficient and disagreement policy |
| `.local/calibration/sheets/` | Generated locally | Blind per-rater packets and blank score sheets |
| `.local/calibration/returned/` | Local intake | Completed R2/R3 sheets, preserved exactly as returned |
| `.local/calibration/reports/` | Generated locally | Agreement report and adjudication CSV |
| `CALIBRATION_SIGNOFF_TEMPLATE.md` | Study lead | Versioned template for the post-adjudication calibration decision |

## What the analysis reports

- **Per slice:** exact agreement, Cohen's κ, Krippendorff's α (ordinal) with a 95% bootstrap interval that resamples whole fixtures, and strict-binary κ (`score == 1`). Slices are all units, and units by language, domain, scoring mode and criticality.
- **Confusion matrices:** binary and ordinal units.
- **Other agreement:** reason codes and task checks.
- **Answer-key comparison:** each rater against the answer key. Items where both raters agree with each other but not with the key point to an anchor problem, not a rater problem.
- **Disagreement list:** every disagreement, with critical units marked as blocking.
- **Threshold verdict:** the result against the recorded threshold.

Undefined coefficients (for example, every rater gives every unit the same score) are reported as NA, not as perfect agreement. With about 24 ordinal unit pairs, the ordinal slice is small and its interval is expected to be wide. The report includes that uncertainty.
