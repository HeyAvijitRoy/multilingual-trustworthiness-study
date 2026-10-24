# Four-model continuation runbook

Candidate only; no study generation is authorized. Commands run from repository
root. Historical three-model files and raw-output paths remain separate.
`GPU_MODEL_SELECTION.md`, `MODELS.json` and `gpu/` contain the measured proposed
pair and exact settings. `REVIEW_PACKET.md` identifies approvals still required.

## Environments and synthetic GPU reproduction

Reference validation stays in `.local/venv` (Python 3.11.17). The earlier CPU
inference venv is preserved. CUDA inference uses `.local/gpu-venv` (Python 3.12.3),
torch 2.14.1+cu130, Transformers 5.20.2, with all resolved packages pinned in
`gpu/requirements-cu130.lock.txt`. `gpu/ENVIRONMENT.json` records BF16 matmul,
device and dependency checks. Use the GPU-enabled execution scope: this session's
sandbox hides NVIDIA devices, while outside-sandbox execution exposes the A100.
Never fall back to CPU based on a sandbox-only query.

For a fresh equivalent environment, create an isolated Python 3.12 venv, install
`torch==2.14.1+cu130` from `https://download.pytorch.org/whl/cu130`, then install
`gpu/requirements-cu130.lock.txt` and run `uv pip check --python PATH_TO_GPU_PYTHON` (the installed uv-managed
venv has no pip module). Versions are pinned, but this
is not a wheel-content-hash lock or guarantee that upstream wheels remain online.
Model weights must already be cached at the pinned revisions; runtime downloads
and remote code are disabled and complete upstream integrity is checked on load.

Run sequentially, with a **new** ignored output path each time:

```bash
PYTORCH_ALLOC_CONF=expandable_segments:True .local/gpu-venv/bin/python scripts/benchmark_gpu.py --model Qwen/Qwen3.5-9B --revision c202236235762e1c871ad0ccb60c8ee5ba337b9a --context 40960 --output .local/gpu_benchmarks/qwen-new.jsonl
PYTORCH_ALLOC_CONF=expandable_segments:True .local/gpu-venv/bin/python scripts/benchmark_gpu.py --model google/gemma-4-12B-it --revision 707f0a3b8a3c7ad586ed01e27eafbad8a27dd0f7 --context 40960 --output .local/gpu_benchmarks/gemma-new.jsonl
PYTORCH_ALLOC_CONF=expandable_segments:True .local/gpu-venv/bin/python scripts/smoke_gpu_adapter.py --model Qwen/Qwen3.5-9B --revision c202236235762e1c871ad0ccb60c8ee5ba337b9a --output .local/gpu_benchmarks/qwen-adapter-new
PYTORCH_ALLOC_CONF=expandable_segments:True .local/gpu-venv/bin/python scripts/smoke_gpu_adapter.py --model google/gemma-4-12B-it --revision 707f0a3b8a3c7ad586ed01e27eafbad8a27dd0f7 --output .local/gpu_benchmarks/gemma-adapter-new
.local/venv/bin/python scripts/summarize_gpu_benchmarks.py --qwen .local/gpu_benchmarks/qwen-new.jsonl --gemma .local/gpu_benchmarks/gemma-new.jsonl --out .local/gpu_benchmarks/summary-new.json
```

The final committed summary is from Qwen run03 and Gemma run04. Earlier failures
and exploratory observations remain preserved and separately identified. Ordinary
probes stop naturally; the capacity probe deliberately truncates at 64 tokens.
No full 32,768-token decode or native 262,144-token capacity is claimed.

## Read-only checks available now

```bash
.local/venv/bin/python scripts/validate_all.py
.local/venv/bin/python scripts/prelim_eval_157.py check
.local/venv/bin/python scripts/prelim_eval_157.py plan
.local/venv/bin/python scripts/prelim_judge_157.py gate
.local/venv/bin/python scripts/prelim_four.py check
.local/venv/bin/python scripts/prelim_four.py plan
.local/venv/bin/python scripts/prelim_four.py readiness
.local/venv/bin/python scripts/prelim_four.py run --provider local_a --dry-run
.local/venv/bin/python scripts/prelim_four_judge.py gate
.local/venv/bin/python scripts/prelim_four_judge.py plan
.local/venv/bin/python scripts/estimate_prelim_four_cost.py
```

Both actual automated judge gates and candidate readiness exit 3 while their
conditions are absent. These are expected blocking statuses, not passed gates.
Checks and dry-runs make no paid requests. Keys may be loaded explicitly through
`--env-file .env` on the amended CLIs; values are never echoed, shell-evaluated or
overwritten when already injected. The intended-account metadata preflight
returned HTTP 200 for both cloud IDs and the judge; paid wire settings, quota and
throughput are not verified. Google account metadata returned outputTokenLimit
32,768, whereas its public model page advertised 65,536. Use the actual 32,768
study allowance; do not assume the larger account limit.

## Approval, paid validation and freeze sequence

1. Obtain real study-lead approval of this exact proposed panel/runtime, local
   timeout, protocol, scoring and analysis. Preserve its evidence; do not invent
   approval, human review or an independently passing judge.
2. Obtain explicit paid authorization covering `cloud_validation`,
   `judge_calibration`, `generation` and `study_scoring`, with a USD maximum.
   `research_approvals.py` requires an approved record, author/time/protocol,
   purpose scope and matching manifest hash. These structural checks do not
   authenticate a person, track invoices or enforce a live monetary cap. Monitor
   actual provider usage against authorization, reserve for retries and pause
   before exceeding it. Account/provider spending controls remain separate.
3. With authorization pinned to a candidate manifest, run a small synthetic wire
   validation, inspect returned IDs/settings/usage and account quota evidence.
   This command refuses missing spending authorization and makes no judge call:

   ```bash
   .local/venv/bin/python scripts/cloud_smoke_four.py --env-file .env --manifest PATH_TO_AUTHORIZED_CANDIDATE --out-dir .local/cloud_validation/new
   ```

   Preserve raw output; publish only a sanitized evidence summary. Any necessary
   scientific change returns for approval. Do not use study prompts for this test.
4. Create a **new immutable `FREEZE.json`**, with final status
   `frozen-before-model-generation`, a distinct snapshot ID, cleared pre-freeze
   decisions, actual approval records, config/scientific-plan/code hashes and all
   availability/feasibility/context/smoke evidence. Pin the dependency lock,
   upstream registry, calibration inputs, shared historical code, GPU runtime,
   server, new judge/analysis/plotting and approval helpers. Preserve the candidate
   history. This is not authorized merely by choosing local models.
5. Run actual isolated judge calibration using that freeze and spending approval.
   A failing gate stops study generation; fixture/key/threshold changes are not
   permitted. A replacement judge requires a separate prospective amendment.
6. Confirm full validation and all credentials/endpoints, then execute the 1,884
   cells without another handover once the authorized gates actually pass.

## Budget evidence

`COST_SCENARIOS.json` uses exact UTF-8 prompt/rubric lengths and token proxies,
not exact cloud token counts. At checked 2026-10-23 prices, generation plus 1,884
judge calls and 30 calibration calls totals about $24.64 optimistic, **$121.93
planning**, or $1,610.52 under the conservative one-attempt envelope. Four billed
attempts give $6,442.10 under the stated introductory Google rates. These exclude
tax/regional premiums, local compute and human review. Recheck current prices and
usage before execution. Hidden thinking is billed output; a planning scenario is
not an invoice ceiling. Google introductory rates expire after 2026-11-30.
Sources and assumptions are recorded in that JSON and the cost-estimator script.
Actual paid calls in this continuation: **zero**.

## Commands after the approved freeze exists

Global arguments precede the subcommand. The reserved final manifest path below
does not exist yet. Never substitute the candidate for approved freeze evidence.

```bash
.local/venv/bin/python scripts/prelim_four_judge.py --manifest data/evaluation/amendments/prelim-157-four-model-0.2/FREEZE.json --env-file .env calibrate
.local/venv/bin/python scripts/prelim_four_judge.py --manifest data/evaluation/amendments/prelim-157-four-model-0.2/FREEZE.json gate
.local/venv/bin/python scripts/prelim_four.py --manifest data/evaluation/amendments/prelim-157-four-model-0.2/FREEZE.json --env-file .env readiness
.local/venv/bin/python scripts/prelim_four.py --manifest data/evaluation/amendments/prelim-157-four-model-0.2/FREEZE.json --env-file .env run --provider openai
.local/venv/bin/python scripts/prelim_four.py --manifest data/evaluation/amendments/prelim-157-four-model-0.2/FREEZE.json --env-file .env run --provider google
```

Before readiness and local generation, export both loopback endpoints:
`PRELIM_LOCAL_A_BASE_URL=http://127.0.0.1:8765/v1` and
`PRELIM_LOCAL_B_BASE_URL=http://127.0.0.1:8765/v1`. The same port is reused
**sequentially**. Start local A's server in another terminal, then its runner:

```bash
PYTORCH_ALLOC_CONF=expandable_segments:True .local/gpu-venv/bin/python scripts/local_gpu_server.py --model Qwen/Qwen3.5-9B --revision c202236235762e1c871ad0ccb60c8ee5ba337b9a --context 40960 --partition local_a --manifest data/evaluation/amendments/prelim-157-four-model-0.2/FREEZE.json --env-file .env --raw-log .local/prelim_157_four_v02/server-local-a.jsonl
.local/venv/bin/python scripts/prelim_four.py --manifest data/evaluation/amendments/prelim-157-four-model-0.2/FREEZE.json --env-file .env run --provider local_a
```

Stop that server cleanly before starting local B with Gemma's exact model/revision,
`--partition local_b` and a separate `server-local-b.jsonl`. Run provider `local_b`
with the same runner. No CPU fallback or simultaneous model loading is allowed.
Server raw logs cannot cross diagnostic/study mode, runtime or manifest hashes.
An identical completed local request returns the exact preserved response.
Successful cells never regenerate. Retry only transient 429/5xx/transport errors,
at most four attempts per cell across resumes. Ambiguous in-flight requests,
duplicate successes, stale provenance and torn JSONL tails block replay. Inspect
raw evidence and live process state before manually releasing a stale lock.

## Scoring, human review and reporting

```bash
.local/venv/bin/python scripts/prelim_four_judge.py --manifest data/evaluation/amendments/prelim-157-four-model-0.2/FREEZE.json --env-file .env score --provider all
.local/venv/bin/python scripts/prelim_four_judge.py --manifest data/evaluation/amendments/prelim-157-four-model-0.2/FREEZE.json qa --out-dir .local/prelim_157_four_v02/qa/new
.local/venv/bin/python scripts/analyze_prelim_four.py --manifest data/evaluation/amendments/prelim-157-four-model-0.2/FREEZE.json --out-dir .local/prelim_157_four_v02/analysis/new
MPLCONFIGDIR=/tmp/study-matplotlib python3 scripts/plot_prelim_four.py .local/prelim_157_four_v02/analysis/new/prelim_four_results.json --out-dir .local/prelim_157_four_v02/analysis/new/figures
```

Plots use the existing system Matplotlib; their provenance records its version
and NumPy version without changing the reference or inference environments.
`--allow-missing` permits only documented unresolved API failures. Independent
human QA reviews every critical RIU below 1, all check failures, nonanswers and
truncations, plus the deterministic stratified 10% sample. Keep private provenance
separate from the blinded packet. Source-linked resolved adjudications may be
passed with `--adjudications PATH` to a **new** analysis directory. The schema is
implemented by `apply_adjudications` and tested for source/review hash and revision
chain checks; it does not certify reviewer authenticity. Raw automated scores are
never replaced. Reports remain explicitly provisional pending independent QA.

After the preliminary evaluation and required review, continue draft batches
P03–P14, preserving P01/P02. All 343 remaining production tasks still require
independent review and formal acceptance. Only then prepare the 500-task gold
snapshot and separately approved 6,000-response evaluation/budget. Study outcomes
must never be used to rewrite frozen gold or prompt content.
