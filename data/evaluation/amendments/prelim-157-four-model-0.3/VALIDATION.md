# Validation of cloud/judge revision 0.3

Executed 2026-10-23 EDT / 2026-10-24 UTC, from latest origin/main `b361477` on
branch `revise-cloud-free-tier-panel`. No study responses, actual new judge
calibration, paid inference calls or human approvals were produced.

| Check | Result |
| --- | --- |
| `scripts/validate_all.py`, reference Python 3.11.17 | PASS, **111 tests**, 17.642 seconds; corpus/freeze/pilot/queue/expansion/calibration-fixture and whitespace checks pass |
| New cloud revision regression file | 21 synthetic tests included in the full total |
| Model IDs/wire settings | Sol exact Responses model, medium/standard and full 32,768 allowance verified with mocked transport; 3.8 medium/full allowance and thought filtering tested |
| Actual account metadata | GET exact Sol/dates for judge candidates HTTP 200; Gemini model catalog HTTP 200 including 3.8; no inference |
| Actual Gemini billing/quotas | **Unverified**, intentionally null; runtime refuses execution, no public default quota inserted |
| Quota persistence | Project/model shared reservations survive instance/protocol restart; failures count; successful daily continuation does not replay completed cells |
| RPM/input TPM/RPD | Rolling requests/input reservations enforced; over-limit prompts not truncated; daily deferral creates no generation attempt/response |
| Rate-limit behavior | Retry-After and RetryInfo preserved; 429 daily cooldown survives restart; Pacific reset tested through DST's 25-hour day |
| Counter integrity | Duplicate request IDs, torn ledger, changed evidence and backwards clock blocked |
| Missingness | Deferred quota cells with retry budget remain pending, not final API missingness |
| Response parsing | Visible Bengali kept, thought parts excluded but raw retained; truncation/safety/empty malformed/continuation outcomes distinguished; missing/changed returned model rejected |
| Judge conflict | Sol self-judge rejected; dated primary identity mismatch blocks receipt/replay; all original calibration input hashes required before calibration |
| Frozen thresholds | Exact 30/229 fixture/key requirements and 0.80/0.90/1.00 thresholds unchanged; synthetic oracle test is not measured calibration |
| Human QA preparation | AI labels/model IDs withheld in independent first-pass packet; private labels/source hashes validated; disagreement audit/escalation tested on synthetic ratings only |
| Cost reproducibility | Revised JSON exactly reproduced; archived 0.2 estimator output preserved via `--legacy-v02`; free Google costs explicitly conditional |
| Fixed-panel statistics | Existing 1,884-cell synthetic test retains paired known-effect expectation and provisional status; actual analysis remains 10,000 bootstraps |
| Historical/0.2/local preservation | Zero diff to 0.2 data, prompts, annotations, calibration/reviews, historical `PRELIM_157*`, native GPU runtime and benchmark sources; local configs equal and inference-function ASTs unchanged |
| Compilation | New/modified metadata, adapters, quota, runner, judge, QA, costing, analysis and regression scripts pass Python compilation |
| Current structural check | Historical integrity/candidate structure PASS; generation_ready=false |
| Current plans | All four models 0/471 generated and scored, total 0/1,884 |
| Actual new automated-judge gate | Exit 3, gate_pass=false, absent report |
| Candidate readiness | Exit 3 for quota, approval, wire validation and final freeze blockers |
| Google dry-run | 471 planned cells, no request sent |

The tests use mocked transports, synthetic model outputs, artificial clocks and
clearly labelled fake quota/human fixtures. They do not establish real account
quotas, model quality, measured agreement or human acceptance. Early test-fixture
migration errors (missing new scoring document/mock credential) were corrected;
no final test failure remains. The original GPU evidence is reused without a new
GPU execution. Calibration remains a factual unmet gate, not a failed test to hide.

`OUTPUT_INVENTORY.json` records empty known local/historical study namespaces;
this does not inventory other machines. Raw model metadata contains only public
model fields in `CLOUD_ACCESS.json`. No key, private project/account identifier,
weight file, raw diagnostic response or synthetic test output is committed.
An unrelated untracked `.aws` path was observed and left untouched/uncommitted;
its contents were not inspected. Existing `.env` exclusion remains committed.
