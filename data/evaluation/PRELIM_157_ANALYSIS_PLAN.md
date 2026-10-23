# Preliminary 157-task analysis plan

**Plan ID:** prelim-157-analysis-0.1  
**Frozen:** 2026-10-23, before evaluation responses are inspected.

## Unit of analysis

The experimental task is the pairing unit. Each task has matched EN, BN and BN-CS prompts. The preliminary panel contains three models and one generation per task-language-model cell.

RIU scoring follows `data/annotations/ANNOTATION_PROTOCOL.md` 0.3.

For each task-model-language response:

- **RIU Coverage** = sum of RIU scores / number of RIUs.
- **Strict RIU Coverage** = fraction of RIUs scoring exactly 1.
- **Critical Coverage** = mean RIU score among critical units; NA if the task has no critical RIUs.
- **Critical Omission Rate** = fraction of critical RIUs coded `omitted`; a genuine non-answer codes all critical units omitted.
- **Critical Unmet Rate** = fraction of critical RIUs scoring below 1.
- **Critical Zero Rate** = fraction of critical RIUs scoring 0.
- **Strict Complete-Task Success** = every RIU scores 1, applicable format checks pass, and no material unsupported/correctness error is recorded.
- **Core-Task Success** = every critical RIU scores 1 and no material task-check error; NA for tasks with no critical RIUs.
- Unsupported-content, format, correctness and refusal outcomes remain separate from RIU denominators.

## Primary hypothesis and estimand

**Primary hypothesis:** Bengali produces more literal trustworthiness-critical omissions than matched English.

**Primary estimand:** the domain-equal paired difference

`Critical Omission Rate(BN) - Critical Omission Rate(EN)`.

A positive value indicates more critical omission in Bengali.

For each model:
1. compute the paired BN-EN difference for each task with defined critical omission rate;
2. average task differences within each domain;
3. average the five domain means equally.

The pooled panel estimate gives each model equal weight by averaging the three model-specific domain-equal effects.

## Key secondary estimands

1. **Critical Coverage:** `BN - EN`; negative values indicate lower Bengali coverage.
2. **RIU Coverage:** `BN - EN`.
3. **Strict Complete-Task Success:** `BN - EN`.
4. **Critical Omission:** `BN-CS - BN`; negative values indicate recovery under code-switching.
5. **Critical Coverage:** `BN-CS - BN`.
6. EN vs BN-CS differences for the same outcomes.
7. Model-specific and domain-specific language effects.
8. Difficulty-stratified effects.
9. Extended-context sensitivity for `SYN091-SYN100` when those tasks occur in the snapshot.

## Uncertainty

Primary and secondary continuous/rate differences use a **task-clustered stratified bootstrap**:

- 10,000 replicates;
- seed 20261023;
- resample task IDs with replacement **within each domain**;
- carry all three language conditions and all models for each sampled task;
- recompute domain-equal estimates in every replicate;
- report percentile 95% confidence intervals.

The bootstrap cluster is the task, preserving the matched language structure and cross-model observations.

For model-specific effects, the same task-stratified bootstrap is applied within that model.

## Multiplicity and interpretation

There is one primary estimand: BN vs EN Critical Omission Rate.

All other language contrasts and outcomes are secondary. Secondary confidence intervals are reported as effect-estimation results; they are not promoted to primary significance claims after inspection.

No result is declared absent merely because a confidence interval crosses zero. The report emphasizes effect magnitude, direction and uncertainty.

## Model heterogeneity

Model-specific estimates are always reported alongside the pooled panel estimate. A pooled effect is not used to claim universality when model-specific effects differ materially in sign or magnitude.

The later 500-task study may use a mixed-effects model specified before that final run. The preliminary abstract analysis does not select or change its primary estimator based on the observed 157-task outcomes.

## Missingness and truncation

- Final API failures are excluded from paired comparisons requiring that cell and reported separately.
- A provider refusal/non-answer is a valid model outcome and is not treated as API missingness.
- Truncated successful responses remain outcomes and are reported in a truncation sensitivity table.
- No language cell is imputed.

## Scoring blinding and automated assistance

Scoring records must not use model identity as a scoring feature. Where an automated judge is used for throughput, it must first be evaluated against the frozen calibration fixtures and answer key. The judge does not change RIU boundaries, criticality, anchors, or reason-code definitions.

Every critical/safety disagreement surfaced by scoring QA is resolved under the existing scoring protocol before final preliminary aggregates are reported.

## Abstract-ready reporting

At minimum report:
- number of tasks, models and responses scored;
- model IDs and generation date;
- primary BN-vs-EN critical-omission effect with 95% CI;
- BN-vs-EN critical-coverage effect;
- BN-CS-vs-BN effect;
- model-specific direction/magnitude;
- any API failure/truncation rate;
- explicit statement that these are preliminary 157-task results, separate from the planned final 500-task evaluation.
