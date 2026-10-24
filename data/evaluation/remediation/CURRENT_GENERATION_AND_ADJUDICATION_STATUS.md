# Current execution and adjudication status — October 24, 2026

This prospective status note supersedes the execution hold wording in the historical October 23 workflow. It does not modify that workflow, any original calibration fixture, label, threshold, prediction or historical failed result.

[Amendment 0.4](../amendments/prelim-generation-0.4/AMENDMENT.md) authorizes independent raw generation: 1,413 primary responses from Sol, Qwen and Gemma, and 60 separate exploratory Gemini responses. **Production RIU and safety scoring remain blocked.** Original safety-check agreement is 25/30 against required 30/30. Raw generation does not resolve that failure.

R1's first-pass CSV remains byte-identical with SHA256 `8d78c24304c296fdaccf9137093d5dc61b4e48ec8e09aee587387335d7937fcc`. The completed second-stage return has now been preserved unchanged with SHA256 `384b95cf0a9942cdb3458988edd2af9375c197365d86552be33145d24bdb1a53`. All seven disputed judgments have recorded decisions: five selected safety checks and two RIUs. Every returned score supports its original reference; two safety decisions revise the preserved first pass. The ordinal RIU retains 0.5 with its binary field blank, as instructed. No reference labels or judge predictions have changed.

The returned form matches the original seven-case metadata and frozen scoring scales. All seven evidence fields are source-linked, comprising eight exact excerpts. Original packet/source hashes remain valid. Structural and quotation checks do not authenticate authorship or independence, or establish every substantive claim. This exposed, selected-case adjudication is diagnostic; it does not supply a new reliability estimate or change the original failed gate. The actual return, comments and comparison are separate private artifacts under `.local/review_staff/v03_calibration_R1/adjudication_returns/` in the return-hash directory.

[Post-adjudication next steps](v03_R1_adjudication/POST_ADJUDICATION_NEXT_STEPS.md) distinguish the received decisions from proposed rubric clarifications. No key correction is indicated by this return. A new prospective scoring-procedure version, independent reference construction and validation remain outstanding; suggested wording is not silently applied to frozen anchors or accepted gold.

Before any new paid judge validation, prospectively freeze the adjudicated measurement version, candidate judge, unexposed validation material, reference construction, language/domain coverage, denominators and acceptance rule. Retain the existing minimum ordinal alpha 0.80, critical-RIU exact agreement 0.90 and safety-check exact agreement 1.00. Do not choose candidates based on repeated testing of the original exposed fixtures. A post-review recalculation on those fixtures is diagnostic/regression evidence only and cannot erase the failed original gate. New validation fixtures and their accepted reference labels do not yet exist; this note is not a completed validation design or a scoring release.

After valid independent judge validation, document readiness for the new generation provenance/scope before production scoring. Required independent study-response QA remains separate and necessary before audited scientific conclusions. Current raw-generation executables have no scoring command; unchanged scoring executables retain their original gate.

The shared paid cap remains USD 100, including the prior USD 0.542045 and all in-progress holds/retries. Generation protects USD 80 for later evaluation. Gemini remains Free only at 5 RPM, 250,000 input TPM and 20 RPD, with no paid fallback. No full 500-task expansion is launched. Current objective counts and usage are reported in the [timestamped manuscript snapshot](../../../manuscript/acm_trust2027/GENERATION_STATUS.md).

## Update — October 24, 2026, 07:10 UTC

- **Generation:** GPT-6.1 Sol is complete at 471/471. Qwen3.5-9B is collecting at about 60 responses per hour. Gemma 4 12B is queued by the frozen single-GPU schedule and is not stalled. Gemini resumed after its Pacific-day quota reset. The diagnosis and guarded supervisor are recorded in [the operations note](../GENERATION_V04_OPERATIONS.md).
- **Scoring:** [Scoring candidate 0.5](../amendments/scoring-candidate-0.5/CANDIDATE_SPEC.md) is hash-pinned and not approved. It maps all seven disagreements to judge-instruction or implementation gaps, and no key correction is indicated.
- **Held-out set:** [Ninety held-out families](../amendments/scoring-candidate-0.5/HELDOUT_PREPARATION.md) are constructed as drafts. They have no reference labels, and no candidate or judge inference has been run.
- **Annotations:** All 343 remaining tasks have AI-drafted annotations pending independent review.
- **Unchanged:** the original failed gate, every frozen artifact, the blocked production scoring, and the reserved USD 80.

## Preserved second-stage packet and completed return

The complete local seven-dispute packet remains unchanged at `data/evaluation/reviews/v03_calibration_R1/adjudication/`, ignored by Git and access-restricted. It includes complete original task/fixture evidence and exact historical judge-input texts recovered read-only and matched to their recorded hashes. Blank templates remain blank; R1's completed CSV is a separate file. Safe tracked templates, aggregate return status and the prospective independent-scoring plan are in [v03_R1_adjudication](v03_R1_adjudication/README.md). No new paid judge calibration or production scoring was performed by the return check.
