# Four-model preliminary amendment candidate, 0.2

Prepared 2026-10-23. **Not frozen; no study generation authorized.**

This prospective candidate is separate from `prelim-157-0.1`. The historical
three-model protocol, models, task manifest, judge and analysis documents remain
byte-identical to commit `88818e5`. No generations or automated scores were found
in this checkout, including ignored study directories. This observation does not
establish that another machine has no outputs; inventory that machine before
claiming global prospectivity. Preserve any subsequently discovered raw records
and document their timing relative to the amendment.

The proposed panel has exactly four partitions: OpenAI `gpt-6-astra`, Google
`gemini-4-argon`, proposed local A `Qwen/Qwen3.5-9B`, and proposed local B
`google/gemma-4-12B-it`. Exact revisions and settings are in `MODELS.json`. Anthropic remains
part of the historical panel and implementation, and is absent from this new
panel only. The GPU recommendation is documented in `GPU_MODEL_SELECTION.md`; it remains
subject to study-lead approval before the final freeze.

Membership is the unchanged 25 pilot plus 132 accepted E1–E6 tasks pinned by
`PRELIM_157_FREEZE.json` (SHA-256
`15c383838a02459c78a92ccbc997dcb73bd9c1e147a785eadf15dad3c945f0b6`).
There are 471 matched prompt instances per model and 1,884 planned responses.
The later 500-task study would contain 6,000 responses and requires its own
approved gold, preregistration and freeze. The 343 remaining tasks cannot be
used as outcome-driven model-selection material.

Controls carried forward: one stateless independent generation per cell, unchanged
frozen prompt as the user message, system instruction `Answer the user's request
directly.`, no tools/retrieval/grounding, run index 1, medium cloud reasoning,
omitted cloud sampling controls and output allowance 32,768 tokens. Cloud timeout
remains 900s. The proposed local timeout is 5,400s, allowing the full output budget
at measured decode rates; this difference requires study-lead approval.
Ordering uses seed 20261023 with partition offsets OpenAI=1, Google=3,
local A=4, local B=5. Requests are currently sequential within each partition;
run local partitions sequentially to avoid memory contention. Concurrency only
affects throughput and must be recorded if subsequently changed.

Proposed local deployment: native Transformers 5.20.2 / torch 2.14.1+cu130,
BF16, no quantization or CPU offload, one sequence, SDPA, native 1,024-token
chunked prefill, configured context 40,960, greedy decoding, seed 20261023,
`enable_thinking=False`, native chat templates and stop IDs. Exact parameter,
artifact, template and dependency hashes are recorded in `MODELS.json` and `gpu/`.
No prompt truncation, translation, rewriting or system-role workaround is used.
The loopback server shares the benchmark runtime; synthetic adapter checks cover
real routing, exact request reuse and refusal of frozen prompts in diagnostic mode.
Unexpected generated reasoning markers fail visible extraction and remain raw,
unscored evidence rather than being stripped heuristically.

The longest rendered frozen prompt was counted across all 1,500 prompts without
study generation: Qwen 958 and Gemma 512 tokens. Full output allowance therefore
requires at least 33,726 / 33,280 context tokens. Both passed synthetic prefill
near 40,960 plus 64 decode tokens. This tests long-context cache/workspace capacity,
not a full 32,768-token autoregressive decode or native 262,144-token feasibility.
Native templates differ from each other and cloud serialization; these are
recorded deployment differences, not identical tokenization.

Reasoning tokens and visible output share provider-dependent allowances/billing;
medium settings and local nonthinking settings are not mechanically equivalent.
Report these deployment differences, quantization and size without asserting
capacity matching to cloud models. Never score hidden reasoning as visible text.

Retry only transient transport/timeouts/429/5xx, same model and settings, at most
four attempts per cell across resumes with bounded exponential backoff. Persist attempt events separately
from response records. A successful refusal, empty visible outcome, or truncated
answer is retained for scoring/QA; an unresolved API/runtime error is missing.
Never substitute a different model/checkpoint. Resume may retry failed cells,
preserving all prior failures; duplicate successes or stale provenance block it.
An interrupted process lock requires investigation before manual removal.
Request-start and outcome events are durable. An unmatched in-flight request or
a success event without its response row blocks replay; reconcile the preserved
payload/outcome explicitly before resume. Never obtain a second generation to
replace a response lost between receipt and serialization.

Amended outputs use `.local/prelim_157_four_v02/` and carry protocol, task snapshot,
config and manifest hashes, partition/model IDs, unchanged prompt/hash, UTC time,
attempts, latency, usage, finish/truncation status and response hash. They must not
be mixed with historical `data/outputs/prelim_157/`. Keep raw provider outputs,
raw judge records, adjudications and derived analyses separate and append-only.
Do not commit raw outputs or secrets. Budget approval is additionally required
before cloud generation or judge calls.

The candidate manifest deliberately has no fabricated final freeze or approvals;
local IDs are proposed, measured recommendations. `check` verifies structure and historical integrity;
`readiness` must fail until all scientific and implementation blockers resolve.
Creating a final immutable freeze is a separate reviewed milestone.
