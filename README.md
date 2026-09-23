# Multilingual Trustworthiness Study

Empirical study of language-conditioned trustworthiness failures in large language models, with an initial focus on semantically matched English, Bengali, and Bengali-English code-switched prompts.

## Research Objective

This project investigates whether language choice systematically affects response completeness, critical-information retention, instruction adherence, correctness, and actionability in LLM outputs.

The dataset is an experimental instrument rather than the primary scientific contribution. The study is designed around controlled paired prompts and structured scoring of trustworthiness-relevant failures.

## Initial Study Design

- **500 evaluation tasks**
- **3 matched language conditions per task**
  - English
  - Natural Bengali
  - Bengali-English code-switching
- **5 task domains**
- Difficulty stratification across easy, medium, and hard tasks
- Structured required-information units for every task
- Critical vs. non-critical omission labels
- Cross-model evaluation
- Repeated generations where stochastic robustness is evaluated

## Planned Domains

1. Technical troubleshooting
2. Cybersecurity and digital safety
3. Procedural and instructional tasks
4. Decision-support and constraint-heavy tasks
5. Information synthesis and long-context tasks

## Repository Structure

```text
multilingual-trustworthiness-study/
├── README.md
├── STUDY_PROTOCOL.md
├── data/
│   ├── prompts/
│   ├── annotations/
│   └── outputs/
├── experiments/
├── analysis/
├── paper/
└── scripts/
```

## Status

Study design and corpus construction in progress.

## Research Integrity

Prompt variants should preserve the same semantic task, constraints, difficulty, and expected information requirements across language conditions. Bengali prompts should be natural rather than literal translations. Code-switched prompts should reflect realistic technical usage rather than arbitrary insertion of English words.
