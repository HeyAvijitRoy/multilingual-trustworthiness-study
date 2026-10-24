# Post-E6 preparation status — 2026-10-23

**Latest continuation: prospective cloud/judge amendment 0.3 is prepared and
validated; actual account quota, approvals, final freeze and calibration remain
blocking. Validated GPU work is preserved.** The
historical checkpoint sections below are retained as an audit trail, including
superseded credential/runtime observations. See the latest continuation section
at the end and the concrete
[0.3 review packet](data/evaluation/amendments/prelim-157-four-model-0.3/REVIEW_PACKET.md).


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
free disk. The initial sandbox query failed, but a subsequent outside-sandbox
recheck confirmed an **NVIDIA A100 SXM4, 40 GiB VRAM**, with 40,018 MiB free
at the first recheck and driver 580.178.04. CUDA initialization and a 1 MiB
allocation/free passed outside the sandbox. The earlier GPU-unavailable
conclusion was a sandbox-scope error and is retracted. See
[the GPU recheck](data/evaluation/amendments/prelim-157-four-model-0.2/GPU_ACCESS_RECHECK.md).
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

For the measured CPU runtime, at 1,000 output tokens/cell, extrapolated serial partitions take roughly 49–118
hours before prefill, retries and contention; full-cap responses exceed the
historical 900-second timeout. These CPU projections do not describe the A100;
GPU diagnostics remain unrun. The installed inference PyTorch is CPU-only and
must be replaced or isolated alongside a CUDA-enabled runtime before GPU model
testing. Exact revisions, hashes, templates, licensing,
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
| `scripts/validate_all.py` | PASS; 73 tests after the GPU-scope correction, corpus/pilot/calibration/queue/expansion/freeze checks |
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
   behavior, adapter validation and measured timeout behavior. Reassess local
   candidates with a CUDA-enabled runtime on the verified A100; the CPU-only
   throughput limitation is not a host GPU limitation.
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


## A100 continuation — 2026-10-23 EDT / 2026-10-24 UTC

The CUDA-enabled environment is working: isolated Python 3.12.3,
torch 2.14.1+cu130, Transformers 5.20.2, 55 compatible pinned packages. CUDA BF16
matrix execution and actual model generation pass. Reference Python 3.11.17 and
the prior CPU environment are preserved. No GPU-unavailable conclusion remains.

Recommend local A **Qwen/Qwen3.5-9B**, revision
`c202236235762e1c871ad0ccb60c8ee5ba337b9a`, and local B
**google/gemma-4-12B-it**, revision
`707f0a3b8a3c7ad586ed01e27eafbad8a27dd0f7`. Both are BF16, unquantized, fully GPU
resident, native template/thinking-off/greedy, configured context 40,960, SDPA,
1,024-token native chunked prefill and expandable allocator segments. Full
artifact integrity matches upstream exact revisions. Exact settings, limitations
and qualitative AI-only review are in the
[selection report](data/evaluation/amendments/prelim-157-four-model-0.2/GPU_MODEL_SELECTION.md).

| Final measured diagnostic | Qwen 9B | Gemma 12B |
| --- | ---: | ---: |
| Loaded parameters | 9,409,813,744 | 11,959,730,176 |
| Short median decode tokens/s | 19.95 | 12.97 |
| Longest rendered frozen input, count only | 958 | 512 |
| Input + full output context needed | 33,726 | 33,280 |
| Synthetic capacity input + output | 40,853 + 64 | 40,858 + 64 |
| Capacity peak allocated VRAM GiB | 19.67 | 23.73 |
| 471 x 2,048 output-token decode-only projection | 13.43 h | 20.65 h |

The projections exclude prefill, startup, I/O, retries and long-context slowdown.
Neither a full 32,768-token decode nor 262k deployment was measured. Each final
suite includes two warmups and two repeats of all four synthetic scenarios;
ordinary responses stopped naturally and repeated token IDs matched. Both
preserve six extended-context constraints, while Bengali/EN/BN-CS recovery probes
still show substantive content/instruction errors documented in the report.
This is not independent human Bengali validation or a study result.

Gemma's earlier unchunked capacity OOMs and the forced-after-READY channel failure
remain raw preserved evidence. Native chunked prefill resolved the memory issue;
a substantive final capacity prompt avoids forcing continuation after a one-word
answer. The production parser still refuses unexpected reasoning-channel output.
No prompt shortening, output-limit reduction, quantization or evidence deletion
was used. Both real local server-adapter smoke tests pass model routing, exact
request reuse, provenance and frozen-prompt refusal in diagnostic mode.

Four-model engineering now includes isolated calibration/scoring ledgers and raw
artifacts, provenance-bound resume, four-attempt budgets across restarts, a shared
sequential judge lock, blinded QA packets, source-linked resolved adjudication
layers, fixed-four-model statistics and standalone plots. Shared historical
functions retain their defaults; frozen historical scientific data is unchanged.
Reports remain provisional pending independent human QA. Synthetic full-panel
analysis tests do not count as actual results or calibration.

Full validation passes **90 tests** plus corpus, freeze, annotation, queue,
calibration-fixture and whitespace checks. New scripts compile. Both actual
judge gates exit 3 with absent reports, and candidate readiness exits 3 as
intended. Historical three-model plan is still 0/1,413; amended plan is
**0/1,884 generated and 0/1,884 scored**. No outcome analysis was computed from
actual study data. No paid call occurred; expenditure remains **$0**.

Both intended cloud credentials are available through the explicit local `.env`
loader; values were not printed or committed. Intended-account GET metadata
returned HTTP 200 for gpt-6-astra, gemini-4-argon and gpt-6.1-sol. Paid synthetic
wire settings and quota remain unverified. Google account metadata gives 32,768
output tokens, despite a larger advertised public-page limit. This matches the
unchanged study allowance and does not authorize paid execution.

The candidate now proposes the exact local pair and a 5,400-second local timeout
(cloud stays 900), sequential judge concurrency 1 and the unchanged scientific
metrics/calibration thresholds. Actual study-lead approval, paid authorization,
cloud synthetic validation and a new immutable final freeze are still required.
Then actual judge calibration must pass before any study generation. The
[review packet](data/evaluation/amendments/prelim-157-four-model-0.2/REVIEW_PACKET.md)
proposes a **USD 200 cap** for this preliminary workflow, against $121.93 typical
planning and much larger conservative scenarios; it is not approval or a promise
to finish within that cap. Scope/hash checks do not track invoices. Monitor usage
and stop before the authorized amount is exceeded. The 500-task study requires
its own later approval and budget. No final freeze or approval was fabricated.

Annotation state is preserved: 157 accepted, 50 P01/P02 AI drafts pending human
review (209 RIUs / 84 critical), 293 still undrafted and all 343 production tasks
still requiring acceptance. P03–P14 follow preliminary evaluation under the user's
continuation sequence. No new human acceptance or independent adjudication is
claimed. The full 6,000-response study remains gated on all 500 accepted gold tasks.

New commits: `815dbbf` (CUDA runtime and reproducible numeric GPU evidence),
`8938f33` (complete isolated pipeline, proposed panel and review packet). The
following status/review-hash commit is identifiable in `git log`. The user's
existing `.gitignore` `.env` addition is preserved unstaged. No push, merge,
identity change, co-author trailer, committed secret, raw output or model weight.


## Revised cloud panel and judge, 0.3 — 2026-10-23 EDT / 2026-10-24 UTC

Continued from verified latest origin/main `b361477` on new branch
`revise-cloud-free-tier-panel`. Historical three-model experiment, all frozen
scientific inputs, accepted annotations, P01/P02 drafts, complete 0.2 amendment
and GPU evidence remain unchanged. A new prospective scoring version is required
for judge replacement, so 0.3 preserves the Astra/Argon/Sol-judge candidate rather
than overwriting it. No new GPU benchmark, dependency install or local integration
run was performed; local configs and inference-function ASTs match the baseline.

Generation targets: **gpt-6.1-sol**, **gemini-3.8-flash**, **Qwen3.5-9B** and
**Gemma-4-12B-it**. The user confirmed the 3.8 target. Authenticated read-only GET
metadata returned exact Sol ID and dated judge-candidate IDs; the Google catalog
includes 3.8 and the assessed 2.5/3.x alternatives. Public Google pricing lists
3.8 free-tier text eligibility, and metadata gives 1,048,576 input / 65,536 output.
Actual Free-tier entitlement, RPM/input TPM/RPD and wire compatibility are **not
verified** by that GET. No gcloud, OAuth/ADC or authenticated browser is available
for quota retrieval here. Required AI Studio verification and source-specific
findings are in the new `CLOUD_MODEL_ASSESSMENT.md`. Null quota fields deliberately
block execution rather than substituting a public limit. No paid Google fallback.

Propose **gpt-5.4-2026-03-05** as primary RIU judge, medium, Responses API,
8,192 output, concurrency 1, with an exact returned-ID check. Its dated identity
is accessible in authenticated metadata and differs from every generator. This
removes literal Sol self-scoring but does not certify independent human judgment
or remove same-provider/style bias. Keep original 30 fixtures / 229 items and
thresholds 0.80 ordinal alpha / 0.90 critical exact / 1.00 safety exact, with a
new independently run calibration. No new judge approval or passing gate exists.

The runner now enforces returned cloud identities and records every Google
reservation in a shared project/model ledger across versions and restarts.
Minute request/input budgets, midnight Pacific/DST reset, Retry-After/RetryInfo,
day-quota pauses and conservative failure counting are implemented. Deferred
work creates no new attempt/response and cannot be presented as final missingness
while retry budget remains. CLI exit 75 exposes the next eligible time; optional
`--wait-for-quota` resumes across days without rotating credentials/projects.
Successful cells and ambiguous receipts remain protected against replay.

The 0.3 human-QA first pass withholds AI labels as well as model IDs. A separate
source/hash-validated agreement audit reports selected-stratum human/AI agreement
and critical/safety disagreement escalation; adjudication stays a separate
resolved layer. No synthetic rater is counted as a human. Statistical estimand,
bootstrap principles, mandatory QA coverage and accepted gold are unchanged.

| Revised planning scenario, conditional actual-free-tier Google | One attempt USD | Four billed attempts USD |
| --- | ---: | ---: |
| Optimistic | 24.38 | 97.54 |
| Typical planning | 97.45 | 389.80 |
| Conservative full-output/proxy envelope | 1,041.32 | 4,165.28 |

Typical components: Sol generation $9.96, new judge calibration $1.22, 1,884 judge
scores $86.26, three Sol synthetic probes $0.01, Google $0 only if the actual
project qualifies. Local compute/energy, independent human review, taxes and
regional premiums are excluded. Three free Google probes are included in quota
planning. Previous $200 remains a **reference, not authorization**. Actual paid
API expenditure remains **$0**. The old 0.2 cost report is intact and its estimator
output remains reproducible with `--legacy-v02`.

Full final validation: **111 tests pass**, plus all existing corpus/freeze,
annotation, queue, expansion, calibration-fixture and whitespace checks. Source
compilation passes. New tests cover quotas, day continuation, DST, 429 recovery,
raw/visible response parsing, exact identities, new judge conflict/calibration
pins, independent first-pass QA and agreement audits. Synthetic tests exercise the
complete four-model analysis without generating real outcomes. Actual judge gate
and readiness correctly exit 3. Structural integrity passes; each partition is
0/471 generated/scored, total **0/1,884**. Known historical/0.2/0.3 output namespaces
contain no model-response/score records; no other machine's inventory is claimed.

The complete proposed packet and operational commands are in
[data/evaluation/amendments/prelim-157-four-model-0.3/REVIEW_PACKET.md](data/evaluation/amendments/prelim-157-four-model-0.3/REVIEW_PACKET.md)
and its runbook. Before execution: obtain real project quota/eligibility evidence,
actual new judge and full scientific/final-freeze approval, and explicit paid cap;
complete authorized cloud synthetic validation and pin returned versions; create
an immutable 0.3 final freeze; pass the actual new judge calibration. No approval,
quota, calibration result or outcome is fabricated. Approval questions are pending.
Once all actual gates pass, continue directly into the preliminary evaluation
without another handover prompt, respecting daily quotas and spending scope.

Annotation counts remain 157 accepted, 50 P01/P02 AI drafts pending review,
293 undrafted and all 343 production tasks still needing acceptance. P03–P14
follow preliminary evaluation; the later full 500-task/6,000-response study needs
separate approved gold, protocol and budget. No new human acceptance is claimed.

Engineering commit: `ccbc553`. The following status/review-hash commit is reported
in `git log` and the task response. No push, history rewrite, Git identity change
or co-author trailer. The unrelated untracked `.aws` path is untouched; no secret,
private account identifier, model weight or raw response is included in commits.
