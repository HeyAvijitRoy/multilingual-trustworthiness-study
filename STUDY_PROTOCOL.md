# Study Protocol

## Working Aim

Measure whether semantically equivalent prompts produce systematically different trustworthiness outcomes across English, Bengali, and Bengali-English code-switched conditions.

## Primary Research Questions

1. Does response completeness differ across the three language conditions?
2. Are trustworthiness-critical information units omitted more often in Bengali than in English?
3. Does Bengali-English code-switching recover information that is omitted in natural Bengali responses?
4. Do language-conditioned differences vary by task domain and difficulty?
5. Are observed differences consistent across model families?
6. Are language-conditioned failures stable across repeated generations?
7. When omissions occur, do they materially affect correctness, safety, or actionability?

## Experimental Unit

Each benchmark item is one canonical task represented by three matched prompt variants:

- `en`: English
- `bn`: natural Bengali
- `bn_en`: natural Bengali-English code-switching

All three variants must preserve:

- task objective
- factual context
- constraints
- required output elements
- difficulty
- safety relevance
- required information units

## Corpus Size

Target: **500 frozen evaluation tasks**.

Initial allocation:

| Domain | Tasks |
|---|---:|
| Technical troubleshooting | 100 |
| Cybersecurity and digital safety | 100 |
| Procedural and instructional | 100 |
| Decision-support and constraint-heavy | 100 |
| Information synthesis and long-context | 100 |
| **Total** | **500** |

## Difficulty Distribution

Across the full evaluation set:

- Easy: 125 tasks
- Medium: 250 tasks
- Hard: 125 tasks

Each domain should approximately preserve the same 25% / 50% / 25% distribution.

## Prompt Construction Principles

### English

The English prompt is the canonical semantic specification.

### Bengali

The Bengali version should be natural contemporary Bengali. It must not be a rigid word-for-word translation when such translation would be unnatural or alter pragmatic meaning.

Technical terms may remain in English where that is normal usage, but the condition should remain predominantly Bengali.

### Bengali-English Code-Switching

The code-switched condition should represent plausible Bengali technical discourse. English words should appear where Bengali speakers commonly retain domain terminology, interface labels, commands, software names, or technical concepts.

Code-switching must not introduce additional hints, detail, or simplification.

## Required Information Units

Each task will define atomic expected answer elements. Every unit will include:

- identifier
- description
- criticality
- rationale
- scoring rule

Criticality levels:

- `critical`: omission can materially affect correctness, safety, task completion, or decision quality
- `supporting`: useful but not necessary for successful completion

## Outcome Measures

Primary measures:

- required-information-unit coverage
- critical omission rate
- complete-task success
- instruction adherence
- factual/correctness error rate
- actionability

Secondary measures:

- refusal or non-answer rate
- unsupported-content rate
- verbosity/compression differences
- consistency across repeated runs

## Evaluation Design

The study should favor structured scoring over unconstrained holistic LLM judging.

Where possible:

1. score required information units deterministically or with explicit rules;
2. use blinded human review for ambiguous cases;
3. use model-based judging only as a supplemental measure with validation against human labels.

## Statistical Plan

Because language variants are paired within the same task, analysis should preserve that pairing.

Candidate analyses include:

- McNemar tests for paired binary outcomes
- Wilcoxon signed-rank tests for paired ordinal/non-normal measures
- mixed-effects logistic or ordinal regression
- interaction analysis for language × difficulty, language × domain, and language × model

A representative model for a binary critical-omission outcome is:

```text
CriticalOmission ~ Language + Model + Difficulty + Domain
                 + Language:Difficulty
                 + Language:Domain
                 + (1 | TaskID)
```

Final statistical choices will be determined after inspecting outcome distributions and model assumptions.

## Leakage and Freeze Policy

The final evaluation set must be frozen before full model evaluation.

Development items used to debug scoring logic, prompt construction, or experiment code should not be included in the final inferential test set unless explicitly designated before evaluation and handled appropriately.

## Reproducibility

Every generation record should preserve at minimum:

- task ID
- language condition
- model/provider
- model version where available
- generation timestamp
- generation parameters
- prompt text or prompt hash
- run index
- raw output

Analysis code should operate on immutable raw outputs and write derived results separately.
