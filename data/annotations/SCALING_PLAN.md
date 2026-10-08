# Preparing annotation of all 500 tasks

The repository is ready to support controlled scaling, but bulk annotation is gated on independent calibration. The current task stops at the revised pilot and preparation; the remaining 475 tasks are not annotated.

## Queue and selection

`SCALING_QUEUE.json` covers every frozen task exactly once with domain, subdomain, difficulty, annotation status and next step. It contains no fabricated gold or model responses.

- 25 existing pilot tasks: independent bilingual review.
- 132 expansion-calibration tasks: the lowest task ID in each domain/subdomain/difficulty stratum absent from the original pilot.
- 343 remaining tasks: annotate after the calibration gate.

This intentionally broad deterministic expansion exposes domain transfer issues before repetitive production annotation. It is a proposed work allocation, not a claim that 132 additional items have been accepted. If the human team chooses a smaller stratified calibration design, document the selection and rationale prospectively and update the queue before annotation. Do not use model performance to choose items.

Regenerate only the queue with `python3 scripts/prepare_scaling_queue.py`; verify without writing with `--check`.

## Execution gates

1. Independently review/adjudicate the 25 revised tasks using protocol 0.2. Resolve the frozen-language flags. Preserve reviewer decisions and establish acceptable agreement criteria before collecting calibration ratings.
2. Annotate and independently review the expansion strata in small batches. Use human-authored scoring fixtures to test binary and ordinal anchors in all three languages. Log changes and recheck the pilot when a rule changes.
3. Freeze the accepted production annotation protocol. Annotate remaining tasks in reviewable batches of up to 25, with independent review of critical units and all ambiguities; double-review at least a prespecified stratified 20% of ordinary units per batch. If any sampled unit reveals a systematic rule error, expand review to every affected unit. These are prospective QA choices, not established empirical thresholds.
4. Maintain one final annotation record per task in `data/annotations/full/`, including copies of the accepted pilot/expansion records. Use empty `source_riu_ids` for new tasks. Never put queue JSONL or score logs in this annotation directory.
5. Run batch validation after each batch and full validation at completion. Full mode must find exactly the 500 corpus task IDs with matching metadata/hashes. Review missing/extra coverage, unit-count distributions, critical proportions, scoring modes and unresolved disputes by domain, subdomain, difficulty and context length.
6. Obtain documented independent bilingual and study-lead sign-off, assign a gold version and hash the accepted annotation files. Only then prepare evaluation runs. No generation or judge calls are part of these steps.

Review logs should identify task/unit/version, each reviewer's initial proposed boundary/criticality/anchor, language-equivalence decision, disagreement, final resolution, adjudicator and date. Record human review references in the annotation's `review` fields; changing a status string alone is not approval.

## Commands

```sh
python3 scripts/validate_prompt_corpus.py
python3 scripts/validate_pilot_annotations.py
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/prepare_scaling_queue.py --check
python3 scripts/validate_pilot_annotations.py --scope batch --annotation-dir data/annotations/full
python3 scripts/validate_pilot_annotations.py --scope full --annotation-dir data/annotations/full
```

The last two commands are for future batches; they intentionally fail before full annotations exist. Keep the pilot files as the method-development history. Do not invoke the historical corpus-revision scripts on the frozen corpus.
