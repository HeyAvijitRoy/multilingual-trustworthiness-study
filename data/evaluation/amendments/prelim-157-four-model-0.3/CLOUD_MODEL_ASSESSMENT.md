# Cloud access and selection — 2026-10-23 EDT / 2026-10-24 UTC

**Targets: GPT-6.1 Sol and Gemini 3.8 Flash.** The user explicitly confirmed
“3.8flash is fine.” Model choice is distinct from final protocol/judge approval,
account quota verification and paid spending authorization. No cloud inference
has run in this revision. The earlier Astra/Argon candidate remains unchanged in
`../prelim-157-four-model-0.2/`; no raw result is overwritten or pooled.

## Authenticated read-only evidence

`CLOUD_ACCESS.json` was produced by `scripts/check_cloud_access.py` using the
configured keys solely for GET model metadata. OpenAI GET returned HTTP 200 and
exact IDs for `gpt-6.1-sol`, `gpt-5.4-2026-03-05`, the dated GPT-5.4 Mini and Astra.
The Google model catalog returned HTTP 200 and includes the candidates below.
No private project ID, account ID, key or provider error body is published.

| Gemini candidate | Catalog evidence | Public free-tier text eligibility | Account quota / inference entitlement | Decision |
| --- | --- | --- | --- | --- |
| gemini-2.5-flash | Listed; metadata version 001; 1,048,576 input / 65,536 output | Listed as free | Unverified | Initial candidate assessed; legacy access restriction; token-budget thinking would replace medium-level control |
| gemini-2.5-pro | Listed; same input/output limits | Listed as free | Unverified | Reasoning-capable legacy option; account access restriction and different thinking control; not chosen |
| gemini-3.5-flash-lite | Listed; same input/output limits | Listed as free | Unverified | Current stable lower-cost/high-volume option; weaker general-purpose proxy than full Flash, no study quality claim |
| gemini-3.6-flash | Listed; same input/output limits | Listed as free | Unverified | Prior full-Flash option; no automatic fallback |
| gemini-3.8-flash | Listed; metadata version 3.0; same input/output limits | Listed as free | Unverified | Selected target, subject to project free-tier/quota and synthetic wire checks |
| gemini-3.1-pro-preview | Listed | Public free tier unavailable | Not tested | Excluded; paid/preview identity does not meet proposed free-tier policy |
| gemini-4-argon | Listed; 32,768 output in prior/current metadata | Public free tier unavailable | No paid call authorized | Preserved historical candidate, excluded from revised target panel |

These are three different facts: catalog presence, public price eligibility and
actual project eligibility/quota. None implies the other two. A successful GET is
not proof that GenerateContent will accept the request or charge zero.
The metadata `version` field is not assumed to equal response `modelVersion`;
exact returned-version allowlists remain empty until authorized synthetic probes.
The new runner stops on any missing or changed returned ID after freeze.

## Compatibility and rationale

The selected stable [Gemini 3.8 Flash model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash)
confirms medium thinking and 65,536 output support. Keep 32,768 for this experiment.
This preserves the existing medium-level Google setting. The
[GenerateContent thinking guide](https://ai.google.dev/gemini-api/docs/generate-content/thinking)
distinguishes Gemini 2.5's numeric thinkingBudget from Gemini 3's thinkingLevel;
they are not silently treated as equivalent. Sol's documented Responses and
medium support likewise fit the unchanged generation controls:
[official OpenAI model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol).

3.8 is chosen as the current full Flash target, supported by documented capability,
metadata fit and the user's confirmation. No outcome-based tournament, independent
Bengali validation or measured BN-CS superiority is claimed. Published general
multilingual capability is only a reason to test it; English/Bengali/BN-CS technical
instruction retention remains unmeasured here. Three clearly synthetic language
probes are prepared in `cloud_smoke_four.py`; they are outside study/calibration
and retain the full output allowance. Run only after actual free-tier verification
(and paid authorization for Sol probes). Failed/empty/truncated/safety outcomes and
thought-token usage remain auditable instead of being hidden by text cleanup.

[Lifecycle documentation](https://ai.google.dev/gemini-api/docs/deprecations)
currently gives no announced shutdown for stable 3.8 and restricts 2.5 access to
prior users while continuing service. This is not a promise of availability for
the experiment's duration. Do not use rolling `latest` or preview substitutes.
Cloud aliases expose no weight hash; matching version IDs cannot exclude invisible
provider backend changes. Multiple-day free-tier execution can confound dates and
provider versions. Retain per-cell UTC dates, all metadata and day-level diagnostics;
report this limitation without changing the frozen primary estimand.

## Actual quotas remain unresolved

No gcloud CLI, OAuth/ADC identity or authenticated browser is available in this
session. The key-only model catalog does not expose billing tier, RPM/input TPM/RPD.
No private-project quota was inferred from a generic table, another account, API
key presence, or Gemini app/Google AI subscription limits.

Required supported verification: open
[Google AI Studio rate limits](https://aistudio.google.com/usage?tab=rate-limit)
for the **same project used by the key**, confirm Free tier and 3.8 eligibility,
record RPM, input TPM and RPD with date and source. Private identifiers and keys
are not needed in the public artifact. Attach sanitized evidence or an explicit
user account observation, not fabricated browser verification. Set operational
headroom for other traffic from that project. `GEMINI_QUOTA_CANDIDATE.json` is
intentionally unverified with null limits, so Google execution is blocked.

Google's [rate-limit documentation](https://ai.google.dev/gemini-api/docs/rate-limits)
uses project-wide RPM/input TPM/RPD and midnight Pacific daily reset. The shared
ledger enforces those dimensions, survives restarts/version changes, reserves
failed attempts and respects provider cooldowns. Hypothetical schedules, **not
account limits**: 474 requests (471 study + 3 probes) need at least 24 days at
20 RPD, 10 at 50, 5 at 100 or 1 at 500, before retries/external usage. No completion
date is promised until actual quota is known. Never rotate keys/accounts/projects.

## Cost and billing condition

[Public pricing](https://ai.google.dev/gemini-api/docs/pricing) currently lists free
text input/output for 3.8 and paid prices $0.75/$3.75 per million through 2026-12-31,
then $1.50/$7.50. This revision authorizes no paid Google fallback or billing
upgrade. Free requests may be used for product improvement under Google's listed
policy; frozen public/synthetic task content remains the same.
Actual paid API expenditure remains $0. The revised separate judge proposal and
costs are in `SCORING_PLAN.md` and `COST_SCENARIOS.json`; the USD 200 reference is
not a spending approval.
