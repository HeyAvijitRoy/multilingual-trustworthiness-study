# Active authorization update — 2026-10-23

The study lead approved v0.3, the dated GPT-5.4 judge, and **USD 100 total** for
all paid operations and retries. USD 200 references below describe the earlier
proposal and are superseded. Google limits are user-verified 5 RPM / 250,000
input TPM / 20 RPD, Free billing, no paid fallback. Use `FREEZE.json` explicitly
for actual calibration/generation/scoring; candidate manifests cannot generate.
`api_budget.py` enforces one durable shared reservation ledger under `.local/`.
Retain unknown-outcome holds until reconciled; never reset a ledger to gain funds.
A budget stop requires a progress/spending/needed-budget report, not new parameters.
Earlier readiness notes below are historical preparation instructions; current
approval and wire evidence are separate dated artifacts and final freeze pins.

# Revised four-model candidate runbook 0.3

Use the existing reference `.local/venv` for CPU-side orchestration/validation and
existing `.local/gpu-venv` only for local inference. No environment installation,
GPU benchmark, weight download or annotation work is repeated for this revision.
The defaults now select 0.3; 0.2 remains explicitly readable via its own config and
manifest. Never mix output directories or copy old records into the new namespace.

## Read-only checks now

```bash
.local/venv/bin/python scripts/validate_all.py
.local/venv/bin/python scripts/prelim_four.py check
.local/venv/bin/python scripts/prelim_four.py plan
.local/venv/bin/python scripts/prelim_four.py readiness
.local/venv/bin/python scripts/prelim_four.py run --provider google --dry-run
.local/venv/bin/python scripts/prelim_four_judge.py plan
.local/venv/bin/python scripts/prelim_four_judge.py gate
.local/venv/bin/python scripts/estimate_prelim_four_cost.py
.local/venv/bin/python scripts/estimate_prelim_four_cost.py --legacy-v02
```

Readiness and actual automated-judge gate exit 3 while blocking conditions remain.
Checks/dry-runs/estimates do not send inference requests. Authenticated metadata
may be refreshed through `check_cloud_access.py --env-file .env --out NEW_PATH`;
it uses only GET, saves public model fields and never exposes credential values.
A model list is not a free-tier/quota verification.

## Resolve project quota without changing the experiment

Use the same Google project's AI Studio Usage/Rate limits view. Record Free tier,
3.8 eligibility, RPM, input TPM and RPD with date/source. No key or private project
ID needs to enter Git. Save sanitized account evidence or explicit actual user
observations under ignored `.local/`. Copy the unverified quota candidate into a
new verified artifact only after obtaining real values; do not invent them.
Set status `verified-account-evidence`, billing_tier `free`, eligibility true,
positive integer limits, verified_by/verified_at and evidence path/SHA256. Keep
`day_timezone=America/Los_Angeles`, project alias `study-google-project` and shared
ledger directory `.local/google_project_quota`. Point MODELS to that artifact.
Existing null limits deliberately block Google requests. A zero/insufficient
quota is a compatibility blocker, not permission to lower output caps.

Limit values must reflect actual project access and allow headroom for other
traffic. The local ledger cannot see external clients. Do not rotate keys, projects
or accounts. Do not reset/delete the shared ledger when changing protocol versions,
restarting, reloading credentials or crossing a UTC date. A stale lock, torn ledger
or backwards clock must be investigated instead of automatically repaired.

## Synthetic validation, approval and final freeze

The user confirmed Gemini 3.8 as the model target, but numerical quota evidence,
new primary-judge/scientific approval and paid spending authorization are absent.
The USD 200 reference has never been approved. Read `REVIEW_PACKET.md` first.

With verified actual free-tier evidence, the authorized Google-only synthetic
probe can run without any paid fallback. Sol probes require explicit paid scope
`cloud_validation` pinned in the selected candidate manifest:

```bash
.local/venv/bin/python scripts/cloud_smoke_four.py --env-file .env --provider google --out-dir .local/cloud_validation/v03-google-new
.local/venv/bin/python scripts/cloud_smoke_four.py --env-file .env --provider openai --manifest PATH_TO_AUTHORIZED_CANDIDATE --out-dir .local/cloud_validation/v03-sol-new
```

Each probe runs synthetic EN/BN/BN-CS prompts, retaining the full 32,768 allowance.
Every Google attempt uses the shared quota ledger. Raw outputs remain ignored and
exclusive; no silent replay/retry on an interrupted diagnostic. Inspect language
understanding, actual wire settings, returned modelVersion/model, usage, safety,
truncation and errors. Create a sanitized wire-evidence summary and pin the exact
consistent observed returned IDs in MODELS. Do not infer them from Models.version.
Any needed scientific change requires review; no implicit substitute is allowed.

Obtain explicit approval of the full revised packet and **gpt-5.4-2026-03-05**
primary judge. Preserve actual study-lead, judge and spending approval records;
spending purposes are `cloud_validation`, `judge_calibration`, `generation`,
`study_scoring`, with USD cap/time/author/protocol. Judge and study-lead approval
may point to the same real record only if it explicitly covers both decisions.
No command fabricates acceptance. Approval checks bind structure and hashes; they
do not authenticate a human or implement provider invoice controls. Track actual
usage, reserve for retries and pause before exceeding the authorized cap.

Then create **new immutable 0.3 FREEZE.json**, final status
`frozen-before-model-generation`, distinct snapshot ID and cleared pre-freeze
decisions. Pin MODELS, protocol/scoring/analysis/JUDGE, quota artifact and actual
account evidence, cloud metadata/wire evidence, local runtime/dependency/artifact
and benchmark evidence, every adapter/runner/scorer/analysis/QA/plot source,
original calibration fixtures/plan/key/task snapshot and actual approval records.
Keep 0.2 and all candidate history. Require the final manifest before calibration;
require a passing new judge gate before any study generation.

## Actual calibration and generation after all gates

Global arguments precede subcommands; these final-manifest paths do not exist yet.
Load cloud credentials explicitly through `--env-file .env` without printing them.
Set both loopback endpoint environment variables to the intended server address
(e.g. `http://127.0.0.1:8765/v1`), using the same port sequentially for local A/B.

```bash
.local/venv/bin/python scripts/prelim_four_judge.py --manifest data/evaluation/amendments/prelim-157-four-model-0.3/FREEZE.json --env-file .env calibrate
.local/venv/bin/python scripts/prelim_four_judge.py --manifest data/evaluation/amendments/prelim-157-four-model-0.3/FREEZE.json gate
.local/venv/bin/python scripts/prelim_four.py --manifest data/evaluation/amendments/prelim-157-four-model-0.3/FREEZE.json --env-file .env readiness
.local/venv/bin/python scripts/prelim_four.py --manifest data/evaluation/amendments/prelim-157-four-model-0.3/FREEZE.json --env-file .env run --provider openai
.local/venv/bin/python scripts/prelim_four.py --manifest data/evaluation/amendments/prelim-157-four-model-0.3/FREEZE.json --env-file .env run --provider google --wait-for-quota
```

Google `--wait-for-quota` resumes automatically across minute/day windows in the
same process, with heartbeat sleeps <=60 seconds. Alternatively omit the flag:
exit **75** records the next permitted time in `quota_deferrals.jsonl`; relaunch
later with the same files/manifest to continue pending cells only. `--limit` is
supported for controlled runs but is not combined with `--wait-for-quota`.
Quota deferral is pending work, not a response or attempt. Failures/retries count
conservatively against project reservations. HTTP Retry-After/RetryInfo and day
quota details are preserved; a day quota waits until midnight Pacific including
DST. Do not delete failure rows or reserve a replacement under another identity.
A received successful payload without a response row blocks replay for explicit
reconciliation. The four-attempt cap persists across days/restarts.

For local A/B, reuse the validated servers and exact revision/settings in the
0.2 runbook, passing this **0.3 final manifest** and distinct raw logs under
`.local/prelim_157_four_v03/`. Use partition `local_a` with Qwen then `local_b`
with Gemma; cleanly stop one server before starting the other. Run the corresponding
`prelim_four.py ... run --provider local_a` / `local_b`. No CPU fallback or simultaneous
GPU loading. These are real experiment generations, not new benchmarks.

## Scoring, independent first pass, adjudication and results

```bash
.local/venv/bin/python scripts/prelim_four_judge.py --manifest data/evaluation/amendments/prelim-157-four-model-0.3/FREEZE.json --env-file .env score --provider all
.local/venv/bin/python scripts/prelim_four_judge.py --manifest data/evaluation/amendments/prelim-157-four-model-0.3/FREEZE.json qa --out-dir .local/prelim_157_four_v03/qa/new
```

Give `qa_packet.jsonl` to independent human raters. Automated labels/model identities
are withheld there; `qa_automated_ratings_private.jsonl` and private manifest stay
separate. Collect first-pass records with qa_id, reviewer_id, reviewed_at,
independent_before_unblinding=true, packet_sha256, response_sha256 and full ratings.
Only an actually independent first pass may claim that flag. Before adjudication:

```bash
.local/venv/bin/python scripts/audit_four_qa.py --manifest data/evaluation/amendments/prelim-157-four-model-0.3/FREEZE.json --packet-dir .local/prelim_157_four_v03/qa/new --human-first-pass .local/prelim_157_four_v03/qa/human-first-pass.jsonl --out .local/prelim_157_four_v03/qa/first-pass-audit.json
```

The audit validates the original scores and hashes, reports agreement by
model/language and review stratum, and escalates critical/safety disagreements.
It does not certify human authenticity, adjudicate disputes or confer gold status.
Keep resolved, reviewer/evidence-linked adjudications separate with explicit
supersession chains. Systematic errors require reviewing the affected class.

```bash
.local/venv/bin/python scripts/analyze_prelim_four.py --manifest data/evaluation/amendments/prelim-157-four-model-0.3/FREEZE.json --out-dir .local/prelim_157_four_v03/analysis/new
MPLCONFIGDIR=/tmp/study-matplotlib python3 scripts/plot_prelim_four.py .local/prelim_157_four_v03/analysis/new/prelim_four_results.json --out-dir .local/prelim_157_four_v03/analysis/new/figures
```

Use `--adjudications PATH` only with real resolved records and a new analysis
snapshot; raw AI and human first-pass labels never change. `--allow-missing`
permits documented unresolved API failures, not unattempted quota-deferred cells.
All reports remain provisional until actual required QA/adjudication and sign-off.

After the preliminary evaluation, continue P03–P14 as AI drafts while preserving
P01/P02. All 343 production tasks still need independent acceptance. No model
outcomes may change frozen prompts, RIUs, criticality or scoring anchors. The full
500-task/6,000-response experiment needs separate approved gold, protocol and budget.
