# Study-lead review packet — four-model preliminary evaluation

**Decision requested; no approval is recorded.** GPU engineering and offline
validation are complete. Actual experiment: **0/1,884 responses and 0/1,884 scores**.
Actual automated-judge calibration: absent. Paid API expenditure: **$0**.

## Scientific proposal to approve

Approve the candidate in `MODELS.json`, `PROTOCOL.md`, `SCORING_PLAN.md`,
`JUDGE.json` and `ANALYSIS_PLAN.md`, together with the measured deployment evidence
in `GPU_MODEL_SELECTION.md` and `gpu/`:

- Panel: OpenAI `gpt-6-astra` (medium/standard), Google `gemini-4-argon`
  (medium), local A `Qwen/Qwen3.5-9B` revision
  `c202236235762e1c871ad0ccb60c8ee5ba337b9a`, local B
  `google/gemma-4-12B-it` revision `707f0a3b8a3c7ad586ed01e27eafbad8a27dd0f7`.
- Locals: BF16, no quantization/offload, native Transformers 5.20.2 / torch
  2.14.1+cu130, SDPA, 1,024-token chunked prefill, 40,960 context,
  native pinned chat templates and stops, greedy, seed 20261023, thinking off,
  expandable allocator segments. Exact full artifact hashes are in `MODELS.json`.
- Full output allowance stays 32,768 tokens for all models. Local timeout is
  proposed at 5,400 seconds; cloud timeout stays 900. Requests execute sequentially;
  one loaded local model at a time. Judge concurrency is 1, within the prior
  maximum 12. Four-attempt retry budgets persist across restarts.
- Exactly the same 157 accepted tasks / 471 prompt instances per model, unchanged
  v0.3.1 prompts, 743 RIUs / 348 critical and scoring anchors. One stateless
  response per cell, no tools or external grounding. Historical three-model
  configuration and all original scientific inputs remain unchanged.
- Judge remains `gpt-6.1-sol`, medium/standard, 8,192 output tokens. Actual 30-fixture /
  229-item calibration must meet ordinal alpha >=0.80, critical exact >=0.90,
  safety-check exact =1.00 before any study generation. Synthetic gate tests are
  not measured calibration. No threshold weakening or replacement judge is approved.
- Primary estimand remains paired Critical Omission Rate(BN) − Rate(EN), task means
  within domain, five equal domain weights, now four equal fixed-model weights.
  Keep 10,000 domain-stratified task-cluster bootstrap draws (seed 20261023),
  model intervals, code-switching contrasts, strata and missingness/truncation
  sensitivity. Independent human QA/adjudication precedes audited conclusions.

Both local models passed repeated synthetic generation and real server-adapter
checks. Qwen/Gemma measured short decode rates are 19.95/12.97 tokens/s, with
near-40k capacity peak allocated VRAM 19.67/23.73 GiB. Full 32,768-token decode
was not run; neither native 262k deployment nor human-validated Bengali quality
is claimed. The selection report records substantive Bengali/EN/BN-CS mistakes,
Gemma prefill OOMs and the resolved capacity-prompt failure. These observations
support keeping strict scoring and QA, not changing frozen gold.

Approve creation of a **new final immutable freeze** after authorized cloud
synthetic validation confirms the proposed wire settings and quota access.
Record actual approval evidence and pin all plans, code, dependencies, artifacts
and evidence. If validation requires a scientific setting change, return for
review. Model recommendation alone is not final experimental sign-off.

## Paid authorization proposed

**Proposed cap: USD 200**, covering only this preliminary protocol's synthetic
cloud validation, actual judge calibration, 942 cloud study generations and
1,884 study-scoring calls, including retries within the approved limit.
Local study generation contributes the other 942 cells. No 500-task study
expenditure, human-review fee or additional paid service is included.

The existing exact-byte/token-proxy scenarios estimate $24.64 optimistic,
$121.93 typical planning, $1,610.52 conservative one-attempt envelope and
$6,442.10 four-billed-attempt envelope at the checked introductory Google prices.
The two short synthetic validation calls are additional, usage-dependent costs.
These are not invoice guarantees; hidden reasoning, response length, retries,
taxes/regional prices and post-intro rates can increase cost. See
`COST_SCENARIOS.json` and its primary pricing sources. The proposed $200 cap may
not finish the experiment: monitor usage, reserve remaining-call/retry costs and
pause for additional authorization before exceeding it. Do not lower output caps,
change models or omit cells to make a budget fit. Approval-record checks enforce
scope/hash presence, not provider invoice accounting or an automatic monetary cap.

A different explicit cap is acceptable if authorized by the user. Never interpret
available API keys, successful model metadata, silence or this proposed amount
as permission to spend.

## Authorized sequence once approval arrives

1. Record actual user scientific and spending approvals with scope, cap and time.
2. Run approved small synthetic cloud wire validation; preserve raw response and
   usage, verify returned identities, actual account settings and quota evidence.
3. Create the approved immutable freeze, with complete content hashes and actual
   approval evidence. Preserve the candidate and all prior raw diagnostics.
4. Run actual judge calibration. A failing gate blocks experiment generation and
   requires diagnosis without changing frozen fixtures, keys or thresholds.
5. Once calibration, credentials/runtime and all validation conditions pass,
   generate 1,884 responses directly, score all valid responses and produce
   provisional results, tables, plots and blinded human QA packets. Resume safely
   and preserve every raw response, error and scoring record.
6. Obtain required independent human review/adjudication before audited claims.
   Then continue production drafts P03–P14 and the separately approved full study.

No new handover prompt is necessary once these approvals and factual gates are
satisfied. `RUNBOOK.md` gives the implemented commands and the precise boundaries.

## Evidence already complete

Full local validation: **90 tests passed**, corpus/freeze/annotation/queue and
calibration-fixture checks passed. Both model artifact sets match pinned upstream
hashes. GPU BF16 matrix execution and 55-package dependency check pass. Both real
GPU adapters pass routing, request reuse and diagnostic frozen-prompt refusal.
Separate scoring, source-linked adjudication ingestion, statistics and figure
export are implemented and tested on synthetic data. Actual judge gates remain
absent/false. `VALIDATION.md` records the checks and their limits.

Annotation status is unchanged: 157 accepted; P01/P02 preserve 50 AI drafts
(209 RIUs, 84 critical) awaiting independent review; all 343 remaining production
tasks need acceptance, including 293 not yet drafted. No human review or new gold
acceptance is claimed. Phase 5 drafting follows the preliminary evaluation and
must not use its outcomes to revise frozen prompts or gold.
