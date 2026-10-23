# Four-model candidate runbook

Status: preparation only. `FREEZE_CANDIDATE.json` cannot launch a study. The
historical three-model commands and data remain separate. Commands below run
from the repository root; `.local/venv` is isolated Python 3.11.17. The CPU
diagnostic environment is separately pinned Python 3.12.3.

## Read-only checks now

```bash
.local/venv/bin/python scripts/validate_all.py
.local/venv/bin/python scripts/prelim_eval_157.py check
.local/venv/bin/python scripts/prelim_eval_157.py plan
.local/venv/bin/python scripts/prelim_judge_157.py gate
.local/venv/bin/python scripts/prelim_four.py check
.local/venv/bin/python scripts/prelim_four.py plan
.local/venv/bin/python scripts/prelim_four.py readiness
.local/venv/bin/python scripts/prelim_four.py run --provider local_a --dry-run
.local/venv/bin/python scripts/estimate_prelim_four_cost.py
```

Historical judge `gate` exits 3 until independently calibrated; four-model
`readiness` exits 3 while decisions/approval/pins remain pending. These are
expected blocking statuses, not passed scientific gates. `check` reports
structural/frozen-input integrity separately from generation readiness.
Dry-run sends no request and writes no response record.

## Finish local feasibility and the amendment

Use `HARDWARE_AND_CANDIDATES.md` for observed hardware, diagnostic commands and
candidate pins. An outside-sandbox recheck confirmed a usable NVIDIA A100 SXM4
with 40 GiB VRAM; see `GPU_ACCESS_RECHECK.md`. The original sandbox hid NVIDIA
device nodes. The existing inference venv is CPU-only PyTorch; GPU diagnostics
require a CUDA-enabled runtime executed with GPU access. Prior CPU decode rates
describe that measured configuration only. A 4k synthetic-input probe
does not verify full 32,768-token output or peak memory at the proposed context.
Do not promote candidate-model cache metadata to study selection automatically.

Before a final freeze, resolve all candidate-manifest decisions. Verify the
selected runtime and adapter with synthetic EN/BN/BN-CS prompts, exact stop
tokens, thinking-off behavior, context budget, precision, template and weight
hashes. The implemented local adapter targets a loopback compatible server;
the measured Transformers diagnostic path is not yet an integrated study server.
Evaluate latency on the selected GPU runtime before deciding whether a local-timeout
amendment is necessary; CPU-only projections cannot decide that question.

Pin the chosen two checkpoints/settings in `MODELS.json`, finish all scientific
plans, obtain actual study-lead approval in a review record, then create a
**new immutable `FREEZE.json`**, preserving this candidate history in Git.
The final manifest must pin `MODELS.json`, protocol, scoring/analysis plans,
availability and feasibility evidence, adapter smoke/context evidence, and
approval record. It must clear pending decisions and identify its own snapshot.
Pin both the new runner and reused historical adapter source files as well;
their hashes and the executing Python version are recorded with every response.
There is no command that fabricates sign-off or turns a candidate into gold.

Verify cloud IDs using intended-account metadata and a separately authorized
small synthetic smoke call, record returned version/quotas/output limits and
actual wire compatibility. The runners use standard-library HTTP, not provider
SDKs; installed SDK support alone would not prove callable access. Never print
or commit API key values. Both required cloud key variables are currently absent.

## Budget review

`COST_SCENARIOS.json` is reproducible from exact frozen prompt/rubric UTF-8 lengths
and stated token proxies, **not exact cloud tokenizer counts**. At checked
2026-10-23 standard prices, generation plus 1,884 judge calls and 30 calibration
calls is approximately $24.64 optimistic, $121.93 typical planning, and $1,610.52
under the conservative one-attempt envelope. Four fully billed attempts give
an envelope of $6,442.10 at introductory Google prices. These are conditional
scenarios, excluding taxes, regional premiums, local compute and human review.
The Google introductory pricing expires after 2026-11-30; post-intro estimates
are also recorded. Hidden thinking counts toward billed output. Recheck rates
and actual token counts before requesting an approved spending cap.

Sources: [OpenAI Astra](https://developers.openai.com/api/docs/models/gpt-6-astra),
[OpenAI Sol judge](https://developers.openai.com/api/docs/models/gpt-6.1-sol),
[OpenAI pricing](https://developers.openai.com/api/docs/pricing),
[Google pricing](https://ai.google.dev/gemini-api/docs/pricing), and
[reasoning billing](https://developers.openai.com/api/docs/guides/reasoning).
No material paid generation or judge request has been made. Obtain explicit
budget approval before either, independently of scientific protocol approval.

## Partition commands after the approved final freeze exists

These are real implemented generation entry points. They currently refuse the
candidate or a missing final manifest. Set cloud credentials securely in the
execution environment; configure a validated pinned local server and its
loopback `PRELIM_LOCAL_A_BASE_URL`/`PRELIM_LOCAL_B_BASE_URL` only after selecting
that runtime. The following path is reserved for the future approved artifact:

```bash
.local/venv/bin/python scripts/prelim_four.py --manifest data/evaluation/amendments/prelim-157-four-model-0.2/FREEZE.json readiness
.local/venv/bin/python scripts/prelim_four.py --manifest data/evaluation/amendments/prelim-157-four-model-0.2/FREEZE.json run --provider openai
.local/venv/bin/python scripts/prelim_four.py --manifest data/evaluation/amendments/prelim-157-four-model-0.2/FREEZE.json run --provider google
.local/venv/bin/python scripts/prelim_four.py --manifest data/evaluation/amendments/prelim-157-four-model-0.2/FREEZE.json run --provider local_a
.local/venv/bin/python scripts/prelim_four.py --manifest data/evaluation/amendments/prelim-157-four-model-0.2/FREEZE.json run --provider local_b
.local/venv/bin/python scripts/prelim_four.py --manifest data/evaluation/amendments/prelim-157-four-model-0.2/FREEZE.json plan
```

Run local partitions sequentially; the shared local-runtime lock prevents
concurrent local execution. Successful cells are not regenerated. Failure records
and attempt events remain append-only. Conflicting provenance/duplicate successes
or a torn JSONL tail block resume. After interruption, inspect the lock and raw
records before removing a stale lock; do not delete/repair raw evidence silently.
Unmatched request-start events and success events without a response row block
replay even after a lock is removed. Exact received responses are preserved in
the success events for explicit reconciliation; ambiguous calls need investigation.

Amended response files are `.local/prelim_157_four_v02/{partition}.jsonl` and
attempt logs are in its `attempts/` subdirectory. Historical output paths never
receive amended records. Raw output directories are ignored by Git.

## Scoring and analysis boundary

Separate amended scoring/calibration and analysis entry points remain to be
implemented and validated against the eventual approved manifest. Do not use
the historical three-model judge/analysis commands on amended response files.
Keep the frozen judge thresholds and all human QA/adjudication requirements.
Do not report automated scores as reviewed or compute findings without actual
auditable observations. The 500-task evaluation stays blocked on approved gold
and a separate final protocol/preregistration.
