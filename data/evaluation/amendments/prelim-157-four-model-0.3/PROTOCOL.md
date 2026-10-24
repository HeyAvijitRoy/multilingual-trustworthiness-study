# Preliminary four-model amendment 0.3 — candidate, not frozen

Prepared prospectively from latest origin/main `b361477`, before any study outputs
in this checkout. This new version supersedes candidate 0.2 for proposed future
execution, preserving every 0.2 file, its Astra/Argon settings and diagnostic
records. Historical three-model protocol and all original scientific inputs stay
unchanged. A replacement judge requires a prospective scoring version under the
historical scoring plan; therefore 0.2 is archived instead of overwritten.

Proposed panel: OpenAI **gpt-6.1-sol**, Google **gemini-3.8-flash**, local A
**Qwen/Qwen3.5-9B**, local B **google/gemma-4-12B-it**. The user confirmed the 3.8
Flash target in this conversation; that is not final protocol/judge approval or
paid authorization. All exact model/local-artifact settings are in `MODELS.json`.
OpenAI generation remains Responses API, medium/standard reasoning. Google
GenerateContent uses medium thinking, with all sampling controls omitted.
No dynamic `latest` alias, paid Gemini fallback or automatic model rotation.

Use exactly the same accepted 157 tasks (25 pilot + 132 E1–E6), 743 RIUs / 348
critical, frozen prompt v0.3.1 and original task snapshot SHA256
`15c383838a02459c78a92ccbc997dcb73bd9c1e147a785eadf15dad3c945f0b6`.
There are 157 × 3 languages × 4 models = **1,884** independent responses, with
one run per cell. Keep system instruction `Answer the user's request directly.`,
32,768 output allowance for every model, no tools, retrieval or grounding,
unchanged prompts without rewriting/truncation and seed/order offsets 20261023
(OpenAI 1, Google 3, local A 4, local B 5). Cloud timeout remains 900 seconds;
previously proposed local timeout stays 5,400 seconds.

Local BF16, no-quantization/no-offload configurations, exact checkpoint/tokenizer
revisions, hashes, templates, stops, 40,960 context, greedy seed/thinking-off,
Transformers 5.20.2 / torch 2.14.1+cu130, SDPA/chunked prefill and A100 evidence are
copied unchanged from 0.2. Evidence links refer to that preserved directory;
no new GPU benchmarks or integration runs are needed for this cloud-only revision.
Prior source-level module hashes remain historical evidence; local inference
functions/runtime are unchanged, checked separately from new cloud/quota code.

## Account and quota requirements

`CLOUD_ACCESS.json` establishes authenticated model metadata/catalog access, not
free-tier entitlement, callable inference, quota or model quality. Public pricing
lists 3.8 Flash text generation as free-tier eligible; metadata lists 1,048,576
input and 65,536 output tokens. Preserve the experimental allowance 32,768.
The actual project billing tier, eligibility, RPM, input TPM and RPD must be
confirmed in AI Studio with dated evidence before Google generation. These
values are deliberately null in `GEMINI_QUOTA_CANDIDATE.json`; no public generic
quota is substituted. No OAuth/ADC/gcloud or authenticated browser is available
here to retrieve account quotas. See `CLOUD_MODEL_ASSESSMENT.md`.

Persist every Google request reservation (including synthetic probes, failures,
retries and ambiguous calls) in one shared project/model ledger outside the study
output directory. Rate limits apply per project, not key, with daily reset at
midnight America/Los_Angeles, including DST. Enforce rolling RPM/input TPM,
conservative UTF-8 input reservation, RPD and provider Retry-After/RetryInfo.
429 day-quota details pause to the next Pacific day; no tight retry loops.
Resume only pending cells after the allowed window. Never rotate accounts, keys
or projects to bypass limits. External project use also consumes quota and needs
operational headroom; local counters cannot see another client's traffic.

No quota pause is a fabricated response or new generation attempt. Successful
refusals/nonanswers and truncations are retained outcomes; unresolved API errors
are missing. Retry only transient failures, same identity/settings, at most four
attempts per cell across restarts. Ambiguous in-flight calls or a received response
without its final row block replay; reconcile raw evidence rather than regenerate.
Enforce the exact returned-version allowlist learned from authorized synthetic
validation and pinned before freeze; a new returned ID stops execution. Provider
stable aliases do not expose weight hashes, so undetectable backend changes remain
a limitation even when IDs match. Record metadata, dates, usage and every raw payload.

## Approval and output isolation

All 0.3 responses/scores/calibration/reviews/analysis use `.local/prelim_157_four_v03/`.
The 0.2 and historical namespaces cannot be reused or pooled. No 0.3 study records
were discovered; new outcomes cannot be generated until actual panel and primary
judge approval, paid budget authorization, full validation, a new immutable final
freeze and a passing new judge calibration all exist. Freeze code/settings/evidence
and actual approval records before calibration/generation. The proposed USD 200
reference is not authorization. Google must remain free-tier-only; do not upgrade
billing or use a paid fallback. Paid Sol/judge calls require explicit scope/cap.

The primary estimand and statistical principles remain unchanged, except the
prospectively revised fixed identities. Human QA and resolved adjudications are
mandatory before independently reviewed claims. Production P01/P02 are preserved;
P03–P14 follow preliminary evaluation under the continuation instructions. Full
500-task gold and 6,000 responses require separate acceptance, freeze and budget.
