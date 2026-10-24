# v0.3 calibration remediation and Reviewer R1 workflow

Prepared October 23, 2026 (America/New_York). Status: **calibration hold active; first-pass assessment pending**.

## Current evidence and hold

The completed automated calibration contains 30 fixtures and 229 keyed items. Ordinal alpha is 0.9605192056057349 against a minimum of 0.80; critical-RIU agreement is 97/98 against a minimum of 0.90. Safety-related task-check agreement is **25/30 against the required 30/30**. The calibration gate has not passed. The safety-related denominator follows the frozen implementation: task checks on tasks whose safety relevance is not `none`; it is not a count of demonstrated harmful outcomes.

The five selected cases cover the five safety-related task-check discrepancies. Two separate RIU discrepancies in the full calibration are outside this packet's assessment scope and remain in the original evidence. Selected-case review is diagnostic; it cannot establish overall agreement or language effects.

The [final freeze](../amendments/prelim-157-four-model-0.3/FREEZE.json), all original labels and thresholds, historical artifacts, raw judge outputs and the original failed gate remain unchanged. Its SHA256 is `e24d98cd9fe650f3d6f1ee34ce30b1b1d76903fa71709ff6145bd40fbf83bbd7`.

**Do not initiate study/production generation, study/production scoring, recalibration or additional paid API requests.** No supervisor is launched. Preparation, offline validation, manuscript work and the review workflow are the authorized work during this hold. The USD 100 combined paid cap remains in force. Conservative cumulative expenditure is USD 0.542045, outstanding holds USD 0, and remaining uncommitted balance USD 99.457955. Gemini 3.8 Flash remains Free tier only: 5 RPM, 250,000 input TPM, 20 RPD, no paid fallback. No full 500-task evaluation is authorized.

## 1. Deliver the first-pass review packet

Give Reviewer R1 only the following four files from [v03_calibration_R1](../reviews/v03_calibration_R1/):

- `README.md`: instructions requiring no code.
- `R1_REVIEW_PACKET.md`: five cases with unique opaque review IDs, full original prompt and response, task context, all 25 relevant RIUs with criticality/anchors, and all applicable task checks.
- `R1_REVIEW_FORM.csv`: six blank task-check assessment rows across five cases; the additional applicable check avoids identifying which check drove selection.
- `POST_REVIEW_COMPARISON_TEMPLATE.csv`: separate empty template for later use; R1 leaves it unchanged.

R1 opens the Markdown preview and UTF-8 CSV in an ordinary editor or spreadsheet, completes assessment/rationale/evidence/ambiguity/comments/date, and returns `R1_REVIEW_FORM_COMPLETED.csv`. R1 makes the first-pass assessment independently; the preparation workflow does not fill in any decisions. RIUs provide context rather than additional requested assessments.

The packet excludes source task and fixture IDs, model identity, reference labels, judge predictions, judge-selected excerpts, disagreement explanations and gate statistics. It includes full responses without emphasis on selected spans. Language remains visible and original wording is preserved.

**Blinding boundary:** provide these four files as a standalone package. Existing source material and labels are discoverable elsewhere in the repository/history; broad repository access cannot enforce blinding. Ask R1 to use only the packet until returning the first-pass assessment, and record any prior exposure if reported. Do not distribute this workflow, manuscript, other study reports or the private mapping with the first-pass materials.

## 2. Keep mappings and evidence separate

The new mapping, source hashes, reference labels and judge records are stored locally under `.local/review_staff/v03_calibration_R1/`, with directory mode 0700 and mapping mode 0600. `.local/` is ignored by Git. Keep that directory restricted and out of commits, pushes and the R1 package. Existing calibration raw records and the earlier 30-case packet are preserved separately; do not overwrite them or return assessments into a historical template.

Staff can run the offline audit with:

```sh
.local/venv/bin/python scripts/v03_r1_review.py validate
```

This verifies exact source text, case coverage/mapping, RIU anchors/criticality, blank forms, public-label exclusions, encoding and packet hashes. It makes no API requests and cannot establish what R1 has previously seen. R1 does not need this command.

## 3. Preserve the returned first-pass assessment

After R1 returns the completed file, preserve its original bytes and record its SHA256 before unblinding. Retain the original filename/receipt date in the review record. Do not replace blanks, change assessments, clean rationales or infer decisions on R1's behalf. If required fields are missing or an assessment is `unresolved`, obtain a clarification while preserving every received version and its hash.

The optional offline staff command is:

```sh
.local/venv/bin/python scripts/v03_r1_review.py compare --returned PATH_TO_RETURNED_CSV
```

It requires exactly six uniquely identified rows with completed assessment, rationale, evidence/absence, ambiguity and date fields. It preserves the returned bytes in a new private hash-named directory, copies the first-pass assessments into a separate comparison, and retrieves the reference/judge values using the private mapping. It never edits either public template, never fills adjudicated labels or substantive recommendations, and never changes a gate. Structural validation does not authenticate authorship or independence. Actual R1 assessments have **not** been received or ingested at preparation time.

## 4. Prepare comparison and recommended adjudication after return

Use the completed first-pass assessment and its rationales to prepare a documented comparison for each review ID/check ID. Show the reference label, judge prediction, R1 assessment, evidence, stated ambiguity and points of agreement separately. Keep the first-pass assessment immutable and distinguish it from any subsequent discussion. The public post-review CSV is only a template; completed comparisons and returned comments stay private unless release is explicitly authorized.

Recommended adjudication procedure:

1. Apply the already frozen rubric to each disputed assertion or task requirement. Distinguish an affirmative unsupported operational assertion from silence/insufficient RIU fulfillment, while preserving the existing orthogonality rule.
2. Consider both whole-response context and the cited evidence. If a technical question requires a source, record a directly supporting primary source and the date; do not infer a decision from majority vote or the desired gate outcome.
3. Record whether the issue concerns application of the existing rubric, ambiguity in its wording, an incorrect reference label, or an unresolved interpretation. These are possible categories for later evidence-based adjudication, not findings assigned now.
4. Record the adjudicated decision, evidence, rationale, responsible reviewer, date and any unresolved issues in a new record. Do not overwrite original labels, accepted annotations, raw outputs, R1's first-pass assessment or the failed calibration report.
5. Where a correction is supported, propose a prospective versioned amendment with explicit source/target versions, affected scope and study-lead disposition. If the issue is unresolved, keep the hold. The seven full-calibration discrepancies must remain visible even though this packet targets five task checks.

No case-specific recommendation or adjudication is prefilled. Prepare those recommendations only from the actual returned assessments and evidence.

## 5. Defensible calibration path before any future release

Disclosure of these fixtures and comparison against their labels makes subsequent evaluation on the same items a development/regression check, not new held-out evidence. Preserve the original 25/30 failed result in all reporting. Do not repeatedly tune the judge prompt, rubric, model or answer key against these cases to obtain 30/30, lower a threshold, omit troublesome cases, or promote a post-review recalculation into an original passing result.

Before any future recalibration, document and approve the prospective amendment and an independent validation plan. Freeze the candidate implementation, evaluation scope, reference construction, all three agreement thresholds and acceptance rule before the next validation outcomes are viewed. Reserve a new unexposed validation set spanning the relevant languages and scoring phenomena, with critical RIUs and safety-related checks sufficient for the prespecified denominators. If validation results influence candidate selection, treat that set as exposed and plan a further independent assessment rather than silently retesting. Report all attempts and failures.

A post-review recalculation on an explicitly corrected, versioned key may be useful as a diagnostic, but must be labelled as such and cannot retroactively erase this failed gate. The current instructions do not authorize a paid recalibration or automatic release of the study hold. Any later authorized work must also fit the unchanged shared USD 100 cap with in-progress reservations; no Gemini billing upgrade is allowed.

## 6. Manuscript and methodological documentation

[Manuscript preparation](../../../manuscript/acm_trust2027/README.md) uses the working title *Structural Silence: Measuring Critical Information Omission in Multilingual Large Language Models*. Completed corpus/annotation preparation, cloud smoke checks and actual failed calibration are distinct from planned generation, scoring, review and inference. R1 assessment/adjudication remains pending. No language effect, model ranking, mitigation effect or independently audited study conclusion is available.

The documentation for the registered paper carries forward the frozen estimand and analysis plan; it does not assert an external registry identifier, registration-system update, Stage 1 acceptance or a revised authorization. Update the verified-findings ledger only when new evidence exists, preserving earlier failures and exposure history. Independent review of actual study responses remains a later requirement if the study is eventually authorized to proceed.
