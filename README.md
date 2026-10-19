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

**Prompt corpus v0.3.1 is final: validated by R1 and frozen.** v0.3 hand-rewrote the Bengali and Bengali-English conditions for all 500 tasks with English unchanged from v0.2; v0.3.1 clarifies one English prompt (SYN079) to match its Bengali versions ([changelog](data/prompts/CORPUS_CHANGELOG.md), [language guide](data/prompts/LANGUAGE_GUIDE.md)).

Current corpus QA verifies:

- 500 unique task IDs
- 100 tasks in each of the five domains
- 1,500 total prompt instances
- exact 25 / 50 / 25 easy-medium-hard allocation per domain
- complete EN / BN / BN-CS variants
- no exact duplicate prompts
- predominantly Bengali natural-Bengali condition
- distinct Bengali-matrix code-switched condition
- normalized Bengali-English script boundaries and pronunciation-correct suffixes
- every English number preserved in both Bengali conditions
- no Latin-script words in the natural-Bengali condition beyond single-letter labels
- substantially expanded extended-context tasks for `SYN091`–`SYN100`

No model evaluation has been run on any corpus version yet. R1 validated the v0.3 Bengali and code-switched prompts, and the study lead approved and froze them on 2026-10-18 (`data/annotations/review_logs/2026-10-18_R1_human_validation.md`). v0.3.1 is the frozen evaluation corpus.

Corpus QA scripts are under `scripts/`:

- `validate_prompt_corpus.py`: structure, difficulty, language-condition and equivalence guards
- `freeze_prompt_corpus.py`: writes or verifies the v0.3 prompt freeze manifest

`revise_corpus_v02.py`, `ensure_bn_cs_switching.py` and `rebalance_synthesis_difficulty.py` are kept only as the v0.2 construction history. They refuse to run without `--force-historical`, because they would overwrite the hand-written v0.3 Bengali conditions.

## Research Integrity

The matched prompt design preserves the same semantic task, factual context, constraints, difficulty and expected information requirements across language conditions. Bengali prompts use natural contemporary Bengali. Code-switched prompts reflect plausible Bengali-English professional or technical discourse with Bengali as the matrix language.

The prompt corpus is frozen before full model evaluation. Annotation and scoring metadata are stored separately from the immutable prompt text.

## RIU annotation status

The 25-task pilot has been methodologically revised under schema 0.2 (rubric revision 2, 2026-10-18): 159 RIUs, 80 critical, with binary scoring for discrete requirements and explicit partial-credit anchors for 21 graded requirements. All 25 records were validated by the study's validator (R1) on 2026-10-18 and were signed off by R1 and the study lead on 2026-10-19 and are frozen as gold `pilot-gold-0.2` ([sign-off](data/annotations/review_logs/2026-10-19_pilot_gold_signoff.md)). [Pilot audit](data/annotations/PILOT_AUDIT.md) and [annotation protocol](data/annotations/ANNOTATION_PROTOCOL.md).

The prompt files are byte-pinned as corpus v0.3.1 in `data/annotations/PROMPT_FREEZE.json` (superseding v0.3 at commit `dfbd25f`, which superseded v0.2 at `74604be`); the English of all pilot tasks is unchanged, so the pilot RIU text still applies and only its prompt hashes were re-pinned. The corpus is frozen; any change requires a new versioned release. The [scaling plan](data/annotations/SCALING_PLAN.md) prepares all 500 tasks but gates production annotation and model runs on validation, expanded calibration and gold sign-off. All 25 pilot records are frozen gold; their hashes are pinned in `data/annotations/PILOT_GOLD_FREEZE.json`. Repository validation is run locally with the scripts described below; no GitHub Actions validation workflow is retained.

## Validation support

Validation tooling covers corpus structure, pilot annotations, frozen-file hashes and scaling-queue consistency, with regression tests under `scripts/`. Run validation locally with Python 3.10 or newer; Python 3.11 is the reference environment.
