# Multilingual Trustworthiness Study

Empirical study of language-conditioned trustworthiness failures in large language models, with an initial focus on semantically matched English, Bengali, and Bengali-English code-switched prompts.

## Research Objective

This project investigates whether language choice systematically affects response completeness, critical-information retention, instruction adherence, correctness, and actionability in LLM outputs.

The dataset is an experimental instrument rather than the primary scientific contribution. The study is designed around controlled paired prompts and structured scoring of trustworthiness-relevant failures.

## Study Design

- **500 evaluation tasks / 1,500 prompt instances**
- **3 matched language conditions per task**
  - English
  - Natural Bengali
  - Bengali-English code-switching with Bengali as the matrix language
- **5 task domains, 100 tasks each**
- **Difficulty allocation per domain:** 25 easy / 50 medium / 25 hard
- Extended-context synthesis subset: `SYN091`–`SYN100`
- Structured required-information-unit scoring planned after prompt freeze
- Cross-model evaluation planned
- Repeated generations planned where stochastic robustness is evaluated

## Domains

1. Technical troubleshooting
2. Cybersecurity and digital safety
3. Procedural and instructional tasks
4. Decision support and constraint-heavy tasks
5. Information synthesis and extended-context tasks

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

## Corpus Status

**v0.2 candidate prompt corpus complete and validated.**

Current corpus QA verifies:

- 500 unique task IDs
- 100 tasks in each of the five domains
- 1,500 total prompt instances
- exact 25 / 50 / 25 easy-medium-hard allocation per domain
- complete EN / BN / BN-CS variants
- no exact duplicate prompts
- predominantly Bengali natural-Bengali condition
- distinct Bengali-matrix code-switched condition
- normalized Bengali-English script boundaries
- substantially expanded extended-context tasks for `SYN091`–`SYN100`

No model evaluation has been run on the v0.2 candidate corpus yet.

Reproducible corpus QA and revision scripts are under `scripts/`, including:

- `revise_corpus_v02.py`
- `ensure_bn_cs_switching.py`
- `rebalance_synthesis_difficulty.py`
- `validate_prompt_corpus.py`

## Research Integrity

Prompt variants must preserve the same semantic task, factual context, constraints, difficulty, and expected information requirements across language conditions. Bengali prompts should use natural contemporary Bengali rather than rigid literal translation. Code-switched prompts should reflect plausible Bengali-English professional or technical discourse rather than arbitrary insertion of English words or English prompts wrapped in Bengali instructions.

The prompt corpus will be frozen before full model evaluation. Annotation and scoring metadata will be stored separately from the immutable prompt text.
