# Prospective amendment 0.4: raw generation and revised evaluation scope

Authorized October 24, 2026, America/New_York, in two successive user messages.
This execution amendment preserves the approved v0.3 configuration registry,
frozen corpus/tasks, accepted annotations, historical protocols, all calibration
records and raw outputs byte-identically. It changes the active panel scope and
allows independent raw generation before judge calibration is resolved.

## Rationale and exact cutover

Judge readiness concerns the validity of later ratings; independent stateless
response collection does not require that judge to assign any labels. Collecting
raw responses now advances the experiment while preserving a strict scoring hold.
No prompts, model inference settings, RIUs, anchors, criticality or thresholds
change. SCOPE.json records the exact scope-change time and observed completion
counts. All four partitions had zero study responses when scope changed; completed
synthetic wire diagnostics and 30 judge calibration fixtures remain separate.

## Prospective panel and sample

The primary panel is GPT-6.1 Sol, Qwen3.5-9B and Gemma 4 12B, with 157 accepted
tasks × three language conditions × three models = **1,413 responses**. Gemini
3.8 Flash is an exploratory comparison on **20 matched tasks × three languages
= 60 responses**. There are 1,473 active raw-generation cells overall. Gemini
collection or quota deferral never gates primary completion or its eventual
validated analysis. Original 1,884-response plans are preserved as historical
plans, not silently relabelled as completed experiments.

Before any study response, choose four tasks per domain from the accepted 157,
one easy, two medium and one hard, using sorted candidate IDs and Python's
Random(20261024) in sorted domain/difficulty order. Freeze the 20 selected IDs in
SCOPE.json. All three language variants are included, using the identical task
responses from the primary panel for matched exploratory comparisons. Selection
uses task metadata only, not judge labels or generated text. It is not a random
population sample or a new held-out scoring-validation set.

The later full benchmark target is 500 × three languages × three primary models
= 4,500 responses. It requires accepted annotations for all tasks, resources and
confirmation of sufficient paid budget; it is not launched by this amendment.

## Generation controls and preservation

Use the original MODELS.json byte-for-byte as a configuration registry. The new
manifest references it rather than changing the four stored model definitions.
The execution scope defines their primary/exploratory roles. Every request has one
task and one language, the original system instruction and original full output
allowance, with no cross-task context, tools, bundling or feedback from ratings.
Per-model fixed seeded task order, retries, return-ID checks, templates, native
BF16 local settings, context and timeout settings remain unchanged.

New process-local entry points enforce this explicit authorization while
reusing the pinned original request and local GPU implementations. Original
source files are not modified. Rows retain the base protocol identifier and add
the execution amendment ID, scope hash and new manifest provenance. The old
output namespace contains no earlier study responses; its calibration and smoke
subdirectories remain separate and unchanged. Every success, valid truncation,
empty response, failure, retry, token usage record and raw provider payload is
preserved. Ambiguous interrupted calls block replay.

The local models share one GPU and are never loaded together. Collect six initial
responses from Qwen, then six from Gemma, then finish Qwen and Gemma sequentially.
This fixed scheduling affects no within-model task order or independent prompt.
Sol and Gemini run independently alongside GPU collection. A paid-generation
budget pause need not stop free/local collection. Technical failures pause their
affected worker and preserve its evidence.

## Scoring restrictions and continued review

Raw generation authorization does **not** authorize production RIU/safety scoring,
recalibration on exposed fixtures, label changes or claims that calibration passed.
The existing judge safety gate remains 25/30 against 30/30. R1's first-pass form
is preserved; comparison and recommended adjudication are private and adjudication
is pending. Continue evidence-based adjudication and plan independent validation
using unexposed material; do not repeatedly tune against the same 30 fixtures.
Future production scoring requires a separately documented readiness decision and
validated integration with this execution scope. The raw-generation entry point
has no judge/scoring command. Independent study-response QA remains required.

## Budget and quotas

The shared lifetime paid cap stays USD 100, including the previously accounted
USD 0.542045 and all retries/in-progress estimated charges. Reuse the original
approval and ledger identity without resetting it. Protect **USD 80** of remaining
capacity for later validation and scoring: generation reservations plus all prior
paid commitments cannot exceed USD 20. This initially permits USD 19.457955 in
new paid generation. The former planning estimate scales to about USD 64.70 for
1,413 primary scores and USD 2.75 for 60 exploratory scores, before new calibration
and retries; the protected amount provides headroom, not guaranteed completion.
Pause paid generation before violating this reservation. Never reduce scientific
parameters to fit a budget. Unknown outcomes retain their full maximum-cost holds.

Gemini remains on the verified Free tier at 5 RPM, 250,000 input TPM and 20 RPD,
using the same shared project ledger, Pacific reset and provider cooldowns. No
paid fallback or account/key rotation. Sixty study requests plus existing probes
span at least four quota days in the existing ledger; actual scheduling depends
on external usage and cooldowns. This does not delay primary collection.

## Analysis and reporting

Primary planned Critical Omission Rate(BN) − Critical Omission Rate(EN), paired
tasks, equal five-domain weighting and task-clustered bootstrap choices remain.
The prospective pooled primary estimate gives the **three primary models** equal
weight; Gemini does not enter it. Report the 20-task Gemini comparisons separately
as exploratory, with matched denominators and selection limitations. No scores,
effect estimates, rankings or trustworthiness findings exist from raw collection
alone. Until scoring is validated, summarize only objective metadata: cell counts
by model/language, completion/finish status, truncation flags, visible character
counts, token usage, latencies, failures, missing/pending cells and collection dates.
Metadata differences do not establish response quality, omission rates or safety.
The ACM TRUST manuscript must report only actually completed evidence at its
submission cutoff; do not represent planned or unscored responses as validated
trustworthiness results. Preserve collection timing and alias-drift limitations.
