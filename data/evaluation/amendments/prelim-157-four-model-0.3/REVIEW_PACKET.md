# Revised preliminary panel and judge — decision packet 0.3

**Candidate, not approved/frozen.** User-requested targets are GPT-6.1 Sol and
Gemini 3.8 Flash (3.8 choice confirmed in this conversation). Local targets stay
Qwen3.5-9B and Gemma 4 12B, BF16 with their already validated exact settings.
Actual state: **0/1,884 study generations, 0/1,884 study scores, no new judge
calibration and $0 paid API expenditure**. All 0.2 and historical files remain
unchanged; new candidate/output namespace is 0.3. No GPU work was repeated.

## Concrete proposal

| Decision | Proposed setting / evidence | State |
| --- | --- | --- |
| OpenAI generator | gpt-6.1-sol; Responses; medium/standard; 32,768 output; omitted sampling | Requested; GET exact model ID HTTP 200; paid wire check pending |
| Google generator | gemini-3.8-flash; GenerateContent; medium; 32,768 output; no tools/grounding | Model choice confirmed; listed in authenticated catalog; public free-tier eligibility; actual billing/quota/wire unverified |
| Locals | Exact copied 0.2 MODELS entries, 40,960 context, BF16/no quantization/offload, same native runtime/templates/stops | Preserved; no model/inference-function changes or new GPU benchmark |
| Primary judge | **gpt-5.4-2026-03-05**, Responses, medium, 8,192 output, concurrency 1 | Proposed only; exact dated ID HTTP 200; distinct from every generator; approval/calibration pending |
| Primary estimand | Paired COR(BN) − COR(EN), five equal domain weights and four equal fixed-model weights | Unchanged principles; identities revised prospectively |
| Calibration | Original 30 fixtures / 229 keyed items; ordinal alpha >=0.80, critical exact >=0.90, safety checks exact =1.00 | Unchanged; actual new gate absent |
| Human QA | All mandatory critical/check/nonanswer/truncation flags + deterministic stratified 10% remaining sample | Unchanged coverage; first pass hides AI labels; disagreement audit/adjudication prepared, no real review completed |

Review `MODELS.json`, `JUDGE.json`, `PROTOCOL.md`, `SCORING_PLAN.md`,
`ANALYSIS_PLAN.md`, `CLOUD_MODEL_ASSESSMENT.md`, `COST_SCENARIOS.json` and
`RUNBOOK.md`. Source/evidence hashes are recorded separately for concrete review;
they are not an approved final freeze. No prompt, accepted annotation, RIU,
criticality, scoring anchor, output allowance or primary statistic changed.

The judge removes literal Sol self-scoring, but it remains an OpenAI model;
common-provider/style errors are possible. Blinding and passing fixture agreement
are not proof of full independence or Bengali technical validity. The proposal
therefore retains independent human QA, first-pass agreement checks and explicit
critical/safety dispute escalation. A different judge requires new prospective
review/calibration, not an outcome-dependent switch. Exact returned IDs must match
frozen allowlists; missing/new identities stop execution and preserve raw evidence.

## Actual Google quota verification still needed

The confirmed model target is not a numerical quota observation. Supported
programmatic model metadata returned no project billing/RPM/TPM/RPD, and no
OAuth/ADC/gcloud/authenticated browser interface is available here. The candidate
quota artifact is explicitly unverified with null limits. It prevents requests.

In Google AI Studio Usage/Rate limits for the project tied to the configured key,
confirm Free tier, 3.8 eligibility, RPM, input TPM and RPD, with a date/source.
No API key, private project ID or email needs to be committed. Provide sanitized
account evidence or explicit actual user observations; do not claim independent
browser verification if it was a user report. Set operational headroom for other
project use. The ledger applies per project/model across restarts and protocol
versions, with Pacific-day reset and durable 429 cooldowns. No key/account/project
rotation, quota deletion or paid fallback is permitted.

Published generic limits are not substituted. Hypothetical 474 successful requests
(471 study + 3 probes) need 24 days at 20 RPD, 10 at 50, 5 at 100, or 1 at 500,
before retries. Reasonable execution duration cannot be certified without actual
limits and stable access. If quota is zero/insufficient or the full output setting
is rejected, report the incompatibility instead of changing tasks/limits/models.

## Paid spending decision still required

The former **USD 200** proposal remains a reference, not authorization. Revised
one-attempt planning with actual-free-tier Google:

| Component | Typical planning USD |
| --- | ---: |
| 471 Sol generations | 9.96 |
| Up to 471 Gemini generations, conditional actual free tier | 0.00 |
| 942 local generations | No paid API fee; local resource cost unvalued |
| 30 new GPT-5.4 calibration calls | 1.22 |
| Up to 1,884 GPT-5.4 scoring calls | 86.26 |
| Three Sol synthetic language probes | 0.01 |
| Three Gemini probes, conditional free tier | 0.00 |
| **Total paid API planning** | **97.45** |

Optimistic one-attempt scenario: $24.38; conservative full-output/proxy envelope:
$1,041.32. Four-billed-attempt envelopes: $97.54 / $389.80 / $4,165.28 for optimistic /
typical / conservative scenarios. These include hidden reasoning in billed output;
they are not invoice guarantees. Token-proxy assumptions, long-input premiums,
current rates, hypothetical unauthorized paid-Google prices, exact call counts and
quota-day examples are in the reproducible cost JSON. No paid Google fallback,
500-task study, tax/regional premium or human-review expenditure is authorized.
At 2,048 hypothetical output tokens, prior measured local rates project 13.43 +
20.65 hours of decode only, excluding prefill/startup/retries and slowdown. No local
hourly price is assumed and no new measurement was made.

Authorize an explicit USD cap and scopes `cloud_validation`, `judge_calibration`,
`generation` and `study_scoring` before paid calls. If using a $200 cap, monitor
actual usage and reserve for retries; pause before exceeding it rather than
lowering output limits or silently omitting cells. Approval-record validation
checks scope and hashes, not human identity or provider invoice enforcement.

## Sequence after the unresolved decisions

1. Obtain actual project free-tier/quota evidence and set the verified operational
   artifact. Google-only synthetic probes may then use the authorized free tier.
2. Obtain explicit primary-judge, scientific/final-freeze and paid-budget approval.
   Run approved small Sol probes; inspect all three language conditions and wire
   metadata. Pin exact returned IDs and sanitized wire evidence before freeze.
3. Create a **new immutable 0.3 final freeze** with actual approval records, complete
   scientific/code/dependency/weight/evidence hashes and the unchanged original
   calibration fixtures/plan/key/task snapshot. No final freeze currently exists.
4. Run actual new primary-judge calibration. A failure blocks generation; never
   weaken thresholds or modify fixtures/keys to pass.
5. Once all real gates pass, proceed directly into the 1,884-cell experiment,
   respecting Google quotas across days and preserving all raw results/failures.
   Score eligible responses; create independent human packets, agreement audit,
   resolved adjudications and reproducible provisional analyses/plots.
6. Obtain actual required independent human review before audited claims. Then
   continue P03–P14 and later the separately approved 500-task/6,000-response study.

No new handover prompt is needed after actual approvals and factual gates pass.
This packet records preparation, not fabricated approval or experimental results.
Annotation state stays 157 accepted; 50 P01/P02 AI drafts awaiting review; all
343 production tasks need acceptance, including 293 not yet drafted.
