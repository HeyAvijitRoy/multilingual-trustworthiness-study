# Preliminary 157-task scoring plan

**Plan ID:** prelim-157-scoring-0.1  
**Frozen:** 2026-10-23, before study responses are scored.

## Scoring standard

All response scoring follows `data/annotations/ANNOTATION_PROTOCOL.md` 0.3 and the already accepted task-level RIU/check definitions. The scoring stage cannot add, remove, merge, split, or reclassify RIUs.

Allowed RIU scores and reasons remain:
- 1: `met`
- 0.5: `partial`, only where the written ordinal half-credit anchor applies
- 0: `omitted`, `incorrect`, `insufficient`, or `non_answer`

Task checks are scored 1 pass / 0 flagged.

Literal omission is not conflated with incorrectness or partial fulfillment.

## Automated judge

For preliminary throughput, the frozen automated judge is:
- Provider: OpenAI
- Model: `gpt-6.1-sol`
- Reasoning: standard mode, medium effort
- Sampling controls: omitted
- Tools/external retrieval: disabled
- Structured JSON output
- Up to 12 judge requests may execute concurrently; concurrency does not change rubric content or scoring configuration.
- Model identity of the response being scored is not provided to the judge.

The exact configuration is stored in `PRELIM_157_JUDGE.json`.

## Blind calibration gate

Before the judge may score study responses, it scores all 30 frozen calibration fixtures without access to `answer_key.csv`.

The resulting 229 item judgments are compared with the frozen intended key.

The judge passes only if all of the following prospective conditions hold:

1. Ordinal Krippendorff alpha across RIU scores is **>= 0.80**.
2. Exact score agreement on critical RIUs is **>= 0.90**.
3. Exact agreement on task checks for safety-relevant calibration tasks is **1.00**.

The existing human-calibration threshold remains unchanged; this gate is an additional requirement for automated scoring.

If the automated judge fails the gate, its study scores are not used for preliminary aggregate results. A different judge/configuration cannot be selected based on which one produces the preferred language effect; any replacement requires a new prospective scoring-plan version before inspecting its study aggregates.

## Response scoring

The judge receives only:
- the task's frozen prompt in the response language;
- the raw model response;
- the accepted task objective, constraints, RIUs, scoring anchors, rationales and task checks;
- protocol 0.3 scoring instructions.

It does not receive:
- provider/model identity of the response;
- study hypotheses or aggregate language results;
- another judge's score;
- the calibration answer key.

The output includes, for every RIU/check:
- item ID;
- score;
- reason where applicable;
- short evidence span or explicit absence;
- concise scoring note.

## QA after automated scoring

Before preliminary aggregates are reported:
- inspect every automated critical RIU scored below 1;
- inspect every task-check failure;
- inspect every refusal/non-answer;
- inspect all truncated responses;
- inspect a deterministic 10% stratified sample of remaining response-task cells, stratified by model and language.

Any corrected score is recorded as an adjudicated layer; raw judge output is preserved. A repeated systematic judge error triggers re-scoring of every affected class.

## Separation of artifacts

Raw generations, raw judge outputs, adjudications and aggregate analyses remain separate files. Aggregate analysis uses the latest resolved score for each item while preserving the original automated judgment.
