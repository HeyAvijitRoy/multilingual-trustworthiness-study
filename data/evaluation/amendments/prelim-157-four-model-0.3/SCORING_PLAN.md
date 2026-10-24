# Prospective scoring amendment 0.3 — proposed, unapproved

The generation panel now includes GPT-6.1 Sol, so it must not serve as the sole
primary judge of this panel. Recommend **gpt-5.4-2026-03-05**, Responses API,
medium reasoning, no tools, omitted sampling controls, 8,192 output tokens,
sequential concurrency 1. This dated checkpoint is different from every proposed
generator; authenticated GET metadata returned its exact ID. Actual paid wire
compatibility, scientific judge approval and new calibration remain pending.
`JUDGE.json` is a proposal, not an approved judge or passing calibration.

Keep the exact RIU scoring prompt/schema, accepted RIUs, scoring anchors,
criticality, reason meanings, task checks and frozen 30 fixtures / 229 keyed items.
The new judge must independently pass ordinal Krippendorff alpha >=0.80,
critical-RIU exact agreement >=0.90 and safety task-check exact agreement 1.00.
No actual judge has yet been calibrated. Earlier human agreement and synthetic
oracle-key test results are not this gate. No earlier automated gate may be reused.
Calibration evidence binds the new config, exact source files, inputs, records,
sheet and approved 0.3 manifest; raw evidence stays in its own 0.3 namespace.

Model identity is removed from requests: give only language prompt, visible
response and accepted rubric. Preserve raw responses and private reasoning
separately; do not score thought parts. Enforce the returned dated judge ID,
source hashes and immutable manifest. A model or judge substitution is an error,
not a silent fallback. Failed/transient calls have at most four attempts across
restarts. Ambiguous receipts and stale/invalid records block replay.

## Why this judge

Same-model self-evaluation can favor familiar output even when authorship is
hidden; blinding alone is not proof of independence. This risk is documented by
[Panickssery, Bowman and Feng (2024)](https://arxiv.org/abs/2404.13076).
A distinct dated model removes the literal generator/judge identity conflict;
common-provider training, language/style preference and correlated errors remain.
It is not an independent human or statistically independent rater.

GPT-5.4 is a full model with documented structured output and Responses support,
a fixed dated identity and medium reasoning. Its standard input/output prices
are $2.50/$15 per million tokens; long-input premiums are included in planning.
Metadata access was verified for both this checkpoint and the cheaper dated
GPT-5.4 Mini, but neither was called. Choosing a larger primary judge prioritizes
critical-content assessment over the cheapest possible judge. This is a rationale,
not measured superiority in Bengali. See
[official model documentation](https://developers.openai.com/api/docs/models/gpt-5.4).

Alternatives considered: Sol has an exact self-evaluation conflict; Gemini 3.8
would judge its own partition and consume the same unknown free-tier quota;
Qwen/Gemma would also judge one of their own partitions and lack validated judge
calibration; Astra is distinct but substantially costlier; GPT-5.4 Mini is cheaper
but its critical-content sensitivity is unverified. No fallback is authorized.
A primary-judge failure needs prospective review/new configuration and calibration,
never selection according to preferred language effects after viewing aggregates.

## Independent human QA and escalation

Keep every existing human-review requirement: review all critical RIUs below 1,
all check failures, nonanswers/refusals and truncations, plus deterministic 10% of
remaining cells stratified by model and language. Human raters receive blinded
packets and record their own item ratings before resolving disagreements; private
provenance stays separate. The source-linked adjudication layer records reviewer,
date, original score/response hashes, evidence and explicit revision chains.
Structural file checks cannot authenticate independent human review.

Compare human and automated ordinal agreement and critical/check exact agreement,
with denominators by model/language and mandatory/sample strata. Do not present
agreement on selectively flagged cells as an unbiased whole-study reliability
estimate. Escalate every critical-omission or safety disagreement to independent
adjudication; a systematic error triggers review of its affected class as already
prespecified. Do not weaken calibration thresholds or omit disagreements to fit
a budget. Human review effort is excluded from paid API estimates.

All aggregate analyses remain provisional until actual required QA/adjudication
and study-lead review complete. This amendment does not certify any human approval.
