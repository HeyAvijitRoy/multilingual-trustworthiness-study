# Preparing annotation of all 500 tasks

The repository supports controlled scaling, with bulk annotation gated on expanded calibration. The revised pilot and scaling preparation are complete; the remaining 475 tasks are not annotated.

## Queue and selection

`SCALING_QUEUE.json` covers every frozen task exactly once with domain, subdomain, difficulty, annotation status and next step. It contains no fabricated gold or model responses.

- 25 existing pilot tasks: validated by R1 (2026-10-18); frozen as gold `pilot-gold-0.2` (2026-10-19, `review_logs/2026-10-19_pilot_gold_signoff.md`).
- 132 expansion-calibration tasks: the lowest task ID in each domain/subdomain/difficulty stratum absent from the original pilot, preassigned prospectively to six deterministic 22-task batches in `EXPANSION_BATCHES.json`.
- 343 remaining tasks: production annotation follows the calibration gate.

This broad deterministic expansion is intended to expose domain transfer issues before production annotation. It is a proposed work allocation; the 132 additional items have not been accepted. Any smaller stratified calibration design would have a prospectively documented selection and rationale, reflected in the queue before annotation. Selection is independent of model performance.

`scripts/prepare_scaling_queue.py` generates the queue and verifies its consistency with the frozen corpus. `scripts/prepare_expansion_batches.py` generates/checks the six balanced expansion-calibration batches from that queue. Batch membership is fixed before R2/R3 calibration outcomes are inspected.

## Planned stages and acceptance criteria

1. **Pilot validation and scoring calibration.** R1 validated the 25 revised tasks on 2026-10-18. Corpus v0.3 resolved the language flags, and the pilot gold was signed off and frozen on 2026-10-19. Agreement criteria precede calibration ratings. The fixture design and agreement tooling are documented in [`data/calibration/`](../calibration/README.md).
2. **Expansion calibration.** After the R2/R3 calibration gate is met and all blocking disagreements are adjudicated, process `EXPANSION_BATCHES.json` in order (`E1`–`E6`), 22 tasks per batch, with validator review of each batch. Rule changes are logged and trigger pilot revalidation/versioning as required.
3. **Production annotation.** The accepted production protocol is frozen before the remaining tasks are annotated in batches of up to 25. Planned review covers every critical unit and ambiguity, plus a prespecified stratified sample of at least 20% of ordinary units per batch. A systematic rule error in that sample triggers review of every affected unit. These are prospective QA choices, not established empirical thresholds.
4. **Final annotation set.** `data/annotations/full/` is reserved for one final annotation record per task, including accepted pilot and expansion records. New tasks have empty `source_riu_ids`. Queue files and scoring logs are stored separately.
5. **Coverage validation.** Batch validation follows each batch; full validation requires exactly the 500 corpus task IDs with matching metadata and hashes. Review covers missing or extra tasks, unit counts, critical proportions, scoring modes and unresolved disputes across domain, subdomain, difficulty and context length.
6. **Production gold sign-off.** Validator and study-lead approval, a gold version and file hashes precede evaluation preparation. Annotation and calibration do not involve generation or judge calls.

Review logs identify task, unit and version; initial boundary, criticality and anchor judgments; language-equivalence decisions; disagreements; final resolutions; adjudicators; and dates. Annotation `review` fields reference this evidence. Status labels alone do not establish approval.

## Validation support

The corpus, annotation, calibration, queue and expansion-batch validators cover structural integrity and frozen-file consistency. Batch and full annotation validation become applicable when `data/annotations/full/` exists. The pilot files remain the method-development history; historical corpus-revision scripts are excluded from the frozen-corpus workflow.
