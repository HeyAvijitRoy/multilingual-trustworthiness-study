# Approved pre-execution validation — 2026-10-23 local date

118 no-network regression tests passed in 24.657 seconds. Tests cover shared
cross-process budget reservations, cap refusal before generation/judge HTTP calls,
unknown outcomes/restarts, invalid usage, torn ledgers, authorization changes,
quota windows/Pacific reset/retries/resume, immutable prompts/panel/local settings,
exact identities, calibration gates, and synthetic scoring/analysis integrity.
`git diff --check` passed. Synthetic oracle fixtures are software tests and do not
constitute actual judge calibration or independent human QA.

Six actual cloud wire probes passed: three per cloud provider across EN/BN/BNCS.
All raw receipts remain ignored and hash-pinned through CLOUD_WIRE_VALIDATION.
At final freeze: zero study responses, zero study scores, no actual calibration
report yet; calibration runs only against this completed final freeze.

Original v0.2 candidate artifacts and the historical task snapshot are preserved.
No GPU benchmarking or annotation work was repeated. The explicit default paid
service tier is an operational spending control; all reasoning, sampling, prompts,
output allowances and scoring thresholds remain unchanged. Credentials, .local
raw data and the unrelated local .aws path are ignored; no credential contents
were printed or included in approval evidence.
