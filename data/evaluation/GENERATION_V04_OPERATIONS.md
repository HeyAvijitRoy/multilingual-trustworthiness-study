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
