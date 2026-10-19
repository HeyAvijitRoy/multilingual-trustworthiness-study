# Scoring calibration: fixtures and two-rater agreement

This stage tests whether two raters, working independently with the frozen pilot gold (`pilot-gold-0.2`), score the same response the same way. It follows the "Calibration and freeze gate" section of `../annotations/ANNOTATION_PROTOCOL.md`. Fixtures are scoring test material, not model outputs. No model is called at any step.

## Current status

AR authored the 30 fixtures and their answer key. Review of the fixtures and intended scores is pending.

On 2026-10-19, before calibration ratings, F26's omission targets were corrected from `RIU-01;RIU-03` to `RIU-01;RIU-05` to match the existing response and intended scores. RIU-03 remains full credit under its extension-preservation anchor. This corrects target metadata; the response text, numeric scores and frozen gold are unchanged.

## Order of work

1. **Study lead records the agreement threshold** in `AGREEMENT_PREREG.json`, before anyone rates. The fields to fill are `set_by`, `set_date`, `minimum`, `decision_statistic` (`point_estimate` or `ci_lower_95`), and optionally a different `primary_coefficient`. The analysis refuses to give a pass/fail verdict if the threshold is dated after the first rating.
2. **Authors write the 30 fixtures** listed in `fixture_plan.csv` into `fixtures.csv`.
3. **Authors write the answer key** (`answer_key.csv`): the score each fixture was written to produce, for at least its target items. Keep it away from the raters until both sheets are returned, and commit it only after that.
4. **Build blind sheets:** `python3 scripts/calibration.py sheets --rater R2 --rater R3`. Each rater gets their own `sheets/<ID>_packet.md` (prompt, response, anchors, in a rater-specific order) and `sheets/<ID>_sheet.csv`. Send each pair privately.
5. **Raters score independently,** filling `rating_date`, `score`, `reason` and `evidence` for every row. They must not discuss the fixtures until both sheets are returned.
6. **Analyse:** `python3 scripts/calibration.py agreement sheets/R2_sheet.csv sheets/R3_sheet.csv --out reports/<date>_agreement.md`.
7. **Adjudicate** every critical-unit, safety or semantic-equivalence disagreement, and log the outcome in `../annotations/review_logs/`. If an anchor proves ambiguous, the fix is a new gold version, not an edit to `pilot-gold-0.2`.

Run `python3 scripts/calibration.py check` at any point to see progress and validate the files.

## Writing fixtures

Write each response as a plausible answer to the task prompt, **in the fixture's language** (`en`, `bn` or `bn_cs`, the same register as the frozen prompt). Record the author's ID in `author_id`. A fixture's author should not rate it, because the author knows the intended scores; the sheet builder warns if they overlap.

Each fixture is scored on **every** unit and task check for its task, not only the target items. Apart from the target, write the rest of the answer the way a typical decent response would, so the fixture also exercises ordinary units.

| `phenomenon` | What the response must show at `target_items` |
|---|---|
| `full_credit` | Meets every unit, using paraphrase, different order or different but valid methods rather than the anchor wording. |
| `omission` | Leaves the target units out entirely, with no contradicting text. |
| `partial_reasoning` | Meets the target's 0.5 anchor exactly, not the 1 anchor. |
| `incorrect_number` | States a wrong value, direction or comparator for the target fact (it must score 0, not 0.5). |
| `contradiction` | States the correct content and also contradicts it, or proposes an unsafe action that defeats the unit (rule 1 of the scoring order). |
| `conditional_safeguard` | Tests the silence rule: either takes a protected or clearly non-destructive path without reciting the safeguard (should score 1), or proposes the risky action without protection (should score 0). Record which one in the key. |
| `format_failure` | Breaks the task's format check (`CHECK-02`), for example seven sentences instead of six, while the content units remain scorable. |

## Files

| File | Who writes it | Contents |
|---|---|---|
| `fixture_plan.csv` | Fixed in advance | 30 slots: 10 per language, 6 per domain, every phenomenon in every language. Change it only before authoring starts, and record why. |
| `fixtures.csv` | Fixture authors | `fixture_id, author_id, authored_date, response_text` |
| `answer_key.csv` | Fixture authors | `fixture_id, item_id, intended_score, intended_reason, author_id, note` |
| `AGREEMENT_PREREG.json` | Study lead | Threshold, coefficient and disagreement policy |
| `sheets/` | Generated | Blind per-rater packets and score sheets |
| `reports/` | Generated | Agreement reports |

## What the analysis reports

- **Per slice:** exact agreement, Cohen's κ, Krippendorff's α (ordinal) with a 95% bootstrap interval that resamples whole fixtures, and strict-binary κ (`score == 1`). Slices are all units, and units by language, domain, scoring mode and criticality.
- **Confusion matrices:** binary and ordinal units.
- **Other agreement:** reason codes and task checks.
- **Answer-key comparison:** each rater against the answer key. Items where both raters agree with each other but not with the key point to an anchor problem, not a rater problem.
- **Disagreement list:** every disagreement, with critical units marked as blocking.
- **Threshold verdict:** the result against the recorded threshold.

Undefined coefficients (for example, every rater gives every unit the same score) are reported as NA, not as perfect agreement. With about 24 ordinal unit pairs, the ordinal slice is small and its interval will be wide. Report that interval; do not hide it.
