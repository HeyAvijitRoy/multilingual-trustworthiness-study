# Raw generation operations — amendment 0.4

The [frozen prospective amendment](amendments/prelim-generation-0.4/AMENDMENT.md) controls active scope and settings. Raw collection is independent of judge calibration; production RIU/safety scoring is blocked. Do not run the older supervisor, which couples generation and scoring.

The detached controller uses `scripts/generation_controller_v04.py`. Its PID, events, logs and 15-second objective metadata snapshot are under `.local/prelim_157_four_v03/generation_only_v04/`. Study response files are `.local/prelim_157_four_v03/{openai,google,local_a,local_b}.jsonl`; exact attempted requests, received payloads and usage are retained in the corresponding `attempts/` and local server raw logs. They are ignored by Git. Each request contains exactly one task-language prompt. No scoring worker is launched.

Do not launch another controller while one is running or replace a running GPU server. The controller lock prevents duplicate controllers. The local pair runs sequentially on one GPU: first six Qwen responses, first six Gemma responses, then the remainder of Qwen and Gemma. Per-model order and frozen decoding settings are unchanged. Cloud workers run independently. Gemini waits for its quota reset without gating primary completion. A budget or technical pause is recorded for the affected worker; inspect it without discarding evidence or replaying uncertain requests.

Offline status commands, requiring no API calls:

```sh
.local/venv/bin/python scripts/generation_only_v04.py report
.local/venv/bin/python scripts/snapshot_generation_v04.py
```

The second command updates the manuscript's dated, public metadata checkpoint. A provider-success record is not a validated semantic-completion score. Report failed attempts separately from failed response records, quota-pending cells and retained truncated/empty responses. Gemini service-demand HTTP 503 errors consume conservative project request reservations even if the provider would not count them.

Only if the controller has stopped, investigate the recorded reason and all in-flight evidence first. A clean restart uses the same controller entry point and immutable manifest, reuses successful cells and retains all failures, holds, quotas and attempt limits. Do not delete locks, reset ledgers, retry ambiguous interruptions, change scientific parameters, or edit frozen execution sources to force a resume. Source changes after collection begins require a new versioned operational amendment and explicit provenance compatibility; preserve the old manifest and outputs.

The shared lifetime paid cap is USD 100, including all prior operations and conservative holds. Current generation enforces a USD 20 ceiling for prior paid commitments plus generation, protecting USD 80 for later validation and scoring. Gemini remains Free only at 5 RPM, 250,000 input TPM and 20 RPD. The full 500-task paid expansion is not launched and requires accepted annotations, resources and confirmation of sufficient budget.

R1's completed first-pass assessment, comparison and recommended adjudication are preserved privately. See [current adjudication status](remediation/CURRENT_GENERATION_AND_ADJUDICATION_STATUS.md). Do not substitute selected-case agreement for independent judge validation or claim the original 25/30 safety gate passed.

## Operational diagnosis — 2026-10-24 06:30 UTC

Inspection found the controller and all workers functioning; nothing was restarted or interrupted.

- **Gemma 4 12B at 6/471 is scheduled, not stalled.** The frozen local schedule is Qwen→6, Gemma→6, Qwen→471, Gemma→471, with the pair never co-loaded on the one A100-40GB. Gemma's warm-start completed at 04:26 UTC and its server was stopped cleanly; the logged `KeyboardInterrupt` is the controller's intended SIGINT. Gemma resumes automatically when Qwen reaches 471. Its six responses have a median latency of 53 s, and no errors, truncations or empty outputs.
- **Qwen3.5-9B** runs alone on the GPU: about 18.8 GB used of 40 GB, roughly 46% utilization, sequential batch-1 bf16 decoding, median latency about 60 s, about 60 responses per hour. Co-loading Gemma (about 24 GB of bf16 weights) would exceed 40 GB, so sequential execution is retained. The HTTP server is single-request by design, and request batching would change the frozen runtime.
- **Gemini HTTP 503s are transient provider overload, not quota exhaustion or request incompatibility.** All 10 bodies are `UNAVAILABLE: This model is currently experiencing high demand`; there were no 429s, and every affected cell later succeeded on a retry with the identical request. Each 503 still consumes one conservatively counted daily request. The 2026-10-23 Pacific day used 20/20: 3 smoke tests plus 17 study attempts (7 successes, 10 503s). The deferral to 07:00 UTC (Pacific midnight) is correct.
- **Starvation risk.** The frozen runner gives each cell a lifetime budget of four attempts and applies `--limit` *before* skipping exhausted cells. A cell that exhausts its attempts therefore blocks the controller's `--limit 1` loop for that partition, and the controller records the worker as paused. The cell itself remains a recorded `api_error` and is never replayed.

`scripts/generation_supervisor_v04.py` is unfrozen operational tooling and does not change scientific settings or record provenance:

```sh
.local/venv/bin/python scripts/generation_supervisor_v04.py status            # read-only
.local/venv/bin/python scripts/generation_supervisor_v04.py resume --provider google
```

`status` reports, per partition:
- unique, duplicate and missing cells;
- in-flight attempt ages;
- exhausted-attempt cells and HTTP error classes;
- last-success age, hourly throughput, median latency and ETA.

It also reports lock holders and their liveness, Gemini reservations per Pacific day, the ledger and GPU state.

`resume` refuses unless all of the following hold:
- the controller is gone or has recorded that worker as paused;
- no live or stale partition lock exists (locks are never removed);
- no attempt is in flight;
- the partition is incomplete.

It then calls the unchanged frozen `generation_only_v04.py run` **without** `--limit`, so exhausted cells are skipped rather than blocking, and it waits across quota deferrals. Local GPU phases are never resumed by the supervisor.

### Incident — 2026-10-24 07:19 UTC

The predicted starvation case occurred. Gemini SYN014/BN received four consecutive HTTP 503 "high demand" responses. Under the frozen four-attempt rule it is now a permanently recorded `api_error` cell, so it is missing, not replayed and not converted to an outcome. The controller then recorded its Gemini worker as paused. All resume preconditions held: no lock, no in-flight attempt, worker recorded as paused. `generation_supervisor_v04.py resume --provider google` was therefore started. It logged the cell as budget-exhausted and continued the remaining Gemini cells through the unchanged frozen entry point. The primary workers were unaffected.
