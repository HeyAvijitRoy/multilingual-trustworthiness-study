# Post-E6 preparation status — 2026-10-23

**Validated preparation milestone; evaluation and production-gold gates remain
open. No study model responses or automated study scores were generated.**

## Baseline audit

The initial checkout was clean on `E-6` at `a36dc1f`. GitHub main and the existing
`origin/main` both resolved to `88818e5dec6bf55b4f6e58e985ffdc641b7512c0`, the merged
historical preliminary protocol. No open PRs were returned by the GitHub API.
Work continues on `post-e6-four-model-preparation` based on that checkpoint;
the user's branches and ignored calibration returns were preserved.

The frozen v0.3.1 corpus remains 500 tasks / 1,500 prompts, five domains of 100
with 25 easy / 50 medium / 25 hard per domain. The accepted preliminary snapshot
contains 25 frozen pilot plus 132 human-reviewed E1–E6 records: **157 tasks,
743 RIUs, 348 critical**. Accepted domains contain 32 tasks each except synthesis
(29); difficulty counts are 49 easy, 54 medium, 54 hard. The snapshot includes
SYN091 and SYN100 from the extended-context subset. The remaining production
membership is 343 tasks. Historical review logs record E1–E6 acceptance and no
unresolved accepted-set disputes. Their authenticity was not newly certified.

Historical manifest hashes verified:

| Artifact | SHA-256 |
| --- | --- |
| Task snapshot | `15c383838a02459c78a92ccbc997dcb73bd9c1e147a785eadf15dad3c945f0b6` |
| Three-model panel | `36a32a4b3c5bf089d7dd132dcd053b0e4cb0f17e7e7f44e838955d8fe16e7548` |
| Generation protocol | `4b69c23ae0b3fcf8599f7fb8975dab92de1dd7692d6272834960646bfed75a70` |
| Analysis plan | `1b59cc0d55753185c93677d451b4f196c722c24cba63903f7e9c201cd78f9fad` |

All original prompt, accepted annotation, calibration, review, queue and historical
evaluation files remain byte-identical to `88818e5`. Queue/expansion manifests
are historical selection records and still contain prospective status labels;
the accepted snapshot and review logs establish the current 157 count. They were
not silently rewritten to update those labels. Several older README/plan prose
sections are stale; this report supplies a dated status without changing freezes.

No historical generation, scoring or automated-judge calibration records were
found in this checkout, including ignored local study paths. Historical plan:
OpenAI 0/471, Anthropic 0/471, Google 0/471; all 1,413 cells remain missing.
Scoring is 0/1,413. The human scoring calibration sign-off records alpha 0.959
and resolved disputes; **the automated judge is uncalibrated**, with `gate`
exiting 3 because its report is absent. No new outcome metrics were computed.
Inventory scope does not establish execution status on another workstation.

## Validated implementation

Historical runners retain their original panel and settings. Confirmed fixes
cover physical-line JSONL parsing for Bengali Unicode separators, torn-tail
protection, generation/score provenance on resume, duplicate rating rejection,
failed HTTP-200 response handling, raw payload and attempt preservation,
explicit truncation metadata, and calibration-sheet/input hash binding.

Analysis keeps the fixed panel when a model is entirely missing and now reports
model CIs, paired denominators, domain/difficulty/extended-context strata,
missingness and truncation sensitivity, generation status/rates and source hashes.
The bootstrap helper canonicalizes input ordering; the original CLI already
supplied a fixed membership order. A new offline judge `qa` command creates
immutable blinded packets and a separate private provenance manifest for all
mandatory flags plus the frozen deterministic 10% sample. It confers no human
approval. Authentic human adjudication ingestion remains unimplemented; analyses
are explicitly provisional/unreviewed.

The separate [four-model candidate](data/evaluation/amendments/prelim-157-four-model-0.2/PROTOCOL.md)
and [runbook](data/evaluation/amendments/prelim-157-four-model-0.2/RUNBOOK.md)
preserve exactly `gpt-6-astra`, `gemini-4-argon` and two pending local slots, for
1,884 planned responses. The historical Anthropic configuration is intact.
`scripts/prelim_four.py` reuses frozen loaders/cloud adapters, isolates outputs
under ignored `.local/prelim_157_four_v02/`, checks code/artifact/response hashes,
locks partitions and reconciles durable request-start/outcome events before
resume. Ambiguous in-flight or received-but-unserialized responses block replay.
The local loopback adapter rejects redirects, unknown stop statuses, model
substitution and non-disabled reasoning. Its tests use synthetic fixtures;
it has not been validated with a selected inference server.

`FREEZE_CANDIDATE.json` is intentionally **not a freeze**: no invented local IDs,
approval or evidence pins. Structural checks pass; generation readiness fails.
No actual amended scoring/analysis entry points are claimed to exist.

## Hardware and candidate diagnostics

The observed agent runtime is a KVM Linux guest presenting AMD EPYC 7713,
32 logical CPUs, about 115.14 GiB RAM, no swap, and about 107.5 GiB initially
free disk. NVIDIA querying fails; GPU model/free VRAM cannot be established.
This does not inspect the user's separate physical workstation. Sanitized
inventories omit personal identifiers. Base Python is 3.12.3; an isolated reference
3.11.17 venv was installed for repository validation, plus a separate CPU inference
venv with torch 2.14.1+cpu / Transformers 5.8.0.

Six cached Qwen3.5/Gemma4 configurations were assessed; four checkpoints were
actually benchmarked sequentially on **synthetic non-study prompts**. Each run
completed three language probes and one approximately 4k-input retrieval probe.

| Diagnostic contender | Peak process RSS GiB | Median short-probe decode tokens/s |
| --- | ---: | ---: |
| Qwen3.5-2B, initial prompt version | 13.57 | 2.66 |
| Qwen3.5-4B, v0.2 | 25.84 | 1.43 |
| Gemma4-E2B, v0.2 | 29.11 | 1.45 |
| Gemma4-E4B, v0.2 | 44.80 | 1.11 |

These are diagnostic performance observations, not study scores. Initial Qwen2B
outputs hit the 128-token diagnostic cap. The other probes exposed weak Bengali
instruction following, vague verification steps or a read-only constraint
violation. AI inspection is not independent human capability validation. All
retrieved the synthetic lookup key; that does not establish 32,768-token decode
stability or the quality needed for this study. **No final local pair is selected.**

At 1,000 output tokens/cell, extrapolated serial partitions take roughly 49–118
hours before prefill, retries and contention; full-cap responses exceed the
historical 900-second timeout. Exact revisions, hashes, templates, licensing,
KV calculations, observed latencies and diagnostic-version differences are in
[the candidate report](data/evaluation/amendments/prelim-157-four-model-0.2/HARDWARE_AND_CANDIDATES.md).
No frozen study prompt was used for generation. Tokenizer-only context checks
covered all 1,500 prompts without modifying or truncating them.

## Production annotation

A new outcome-independent plan assigns the 343 remaining tasks to 14 batches,
each 24 or 25 tasks. Historical assignments/accepted data are unchanged.

| State | Tasks |
| --- | ---: |
| Historically accepted | 157 |
| New drafted and machine-validated | 50 |
| New human-reviewed / approved | 0 / 0 |
| Not yet drafted | 293 |
| Production tasks still pending independent approval | 343 |

P01/P02 contain 209 draft RIUs, 84 critical, 202 binary and 7 ordinal. Current
v0.3 packets require 173 critical/ambiguity/sample unit reviews, plus full-task
coverage/equivalence review for all 50 tasks. Each batch samples 18 supporting
units with a prospectively specified stratified SHA-256 rule (at least 20% per
stratum). The construction audit removed redundant diagnostic units and broadened
review of affected technical tasks. Earlier unaccepted packets are preserved;
no packet is silently overwritten. See the [review entry point](data/annotations/production_review/README.md).
Bulk production protocol approval, independent bilingual review, disputes and
study-lead sign-off are still required. No production gold was assembled.

## Checks and execution status

Reference interpreter: `.local/venv/bin/python` (3.11.17). Commands actually run:

| Command (with reference interpreter) | Outcome |
| --- | --- |
| `-m py_compile` on generation, judge, analysis, amendment, budget, hardware, diagnostics and production scripts | PASS |
| `scripts/validate_all.py` | PASS; 71 tests, corpus/pilot/calibration/queue/expansion/freeze checks |
| `scripts/prelim_eval_157.py check` | PASS; historical hashes intact |
| `scripts/prelim_eval_157.py plan` | 0 generated / 1,413 remaining |
| `scripts/prelim_judge_157.py plan --provider all` | 0 generated / scored |
| `scripts/prelim_judge_157.py gate` | Exit 3; unrun automated calibration, not a pass |
| `scripts/prelim_four.py check` | Structural integrity PASS, generation readiness false |
| `scripts/prelim_four.py readiness` | Exit 3; pending scientific/implementation evidence |
| `scripts/prelim_four.py plan` | 0 generated / 1,884 missing, 471 per partition |
| `scripts/prelim_four.py run --provider local_a --dry-run` | No requests; 471 planned prompts |
| `scripts/prepare_production_batches.py --check --packets` | PASS; 50 drafts, 293 undrafted |
| `scripts/validate_pilot_annotations.py --scope batch --annotation-dir data/annotations/production/P01` | PASS; 25 tasks, 100 RIUs |
| Same batch validator for `P02` | PASS; 25 tasks, 109 RIUs |
| `scripts/estimate_prelim_four_cost.py` | Reproduces committed scenario JSON exactly; no requests |
| `git diff --exit-code 88818e5` scoped to all original frozen data | PASS; no historical scientific-data edits |

No paid generation, judge calibration/scoring, study local generation, real-data
analysis, or human approval was performed. Those are not counted as passed tests.
Full analysis was exercised only with synthetic fixtures. Diagnostic inference
used the separate pinned 3.12 environment and remains outside study outputs.

## Costs, gates and next work

Both `OPENAI_API_KEY` and `GEMINI_API_KEY` are absent (presence checked without
printing values). Official documentation lists the exact requested cloud IDs
and sufficient output allowances; intended-account access, quotas and callable
wire settings remain unverified. No provider was substituted. The standard-library
HTTP clients do not require an SDK, but still need actual access verification.

Paid API spend by this work: **$0**. The [budget scenarios](data/evaluation/amendments/prelim-157-four-model-0.2/COST_SCENARIOS.json)
estimate generation plus 1,884 scores/30 calibration calls at $24.64 optimistic,
$121.93 typical planning and $1,610.52 conservative one-attempt envelope, or
$6,442.10 if four full attempts were billed, at the checked introductory Google
rates. These are conditional token-proxy scenarios, not invoice guarantees;
local compute, human review, taxes and regional premiums are excluded.

Remaining gates/work:

1. Choose an acceptable local deployment/runtime and two independently assessed
   checkpoints; resolve diagnostic quality, exact stops, full output/context
   behavior, adapter validation and CPU timeout differences.
2. Verify intended cloud-account access; complete and approve the four-model
   scientific plans and immutable final manifest before any study generation.
3. Implement and validate amended scoring/calibration/analysis isolation and
   an explicit human adjudication exchange before amended results are reported.
4. Obtain explicit paid-generation/judge budget approval before paid calls.
5. Review the 50 drafts, approve the production protocol, and draft/review the
   remaining 293. Only independently approved 500-task gold permits the separate
   final preregistered 6,000-response study.

Local commits: `99f71ef` (evaluation integrity/reporting), `f8cd255`
(production plan and review-pending drafts), and `5bf0f65` (isolated four-model
candidate and measured local feasibility). The final status-document commit
ID is reported in the task's final message and `git log`. No push, PR creation,
remote merge, history rewrite or Git identity change was performed.
