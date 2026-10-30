# Multilingual trustworthiness study

Do large language models drop trustworthiness-critical information when the same task is asked in Bengali instead of English? Each task is asked in English (EN), Bengali (BN) and Bengali-English code-switched Bengali (BN-CS). Responses are scored against rubrics of required information units (RIUs) written before any model was run.

## Preliminary study (157 tasks)

- **Tasks:** 157 with accepted gold rubrics (743 RIUs, 348 critical).
- **Responses:** 157 tasks × 3 languages × 3 models = 1,413.
- **Scoring:** an automated judge whose procedure was validated against independent reference scores (alpha 0.99; critical and safety-check agreement 100% on 88 held-out fixtures).

| Model | Critical coverage EN / BN / BN-CS | Critical omission EN / BN / BN-CS |
|---|---|---|
| gpt-6.1-sol | 0.981 / 0.978 / 0.994 | 0.000 / 0.000 / 0.004 |
| Qwen3.5-9B | 0.885 / 0.799 / 0.829 | 0.007 / 0.018 / 0.030 |
| Gemma 4 12B | 0.859 / 0.792 / 0.835 | 0.019 / 0.022 / 0.019 |

Paired, domain-equal language effects across the three models, with 95% CIs:

- **Primary (critical omission rate, BN − EN): +0.003 [−0.014, +0.015].** Critical information is rarely left out entirely, in any language.
- **Critical coverage, BN − EN: −0.050 [−0.078, −0.021].** In Bengali, critical content is more often present but wrong or insufficient. The effect comes from Qwen (−0.080) and Gemma (−0.068); Sol shows no gap (−0.002).
- **Strict complete-task success, BN − EN: −0.093 [−0.131, −0.055].**
- **RIU coverage, BN-CS − BN: +0.027 [+0.011, +0.044].** Code-switching recovers part of the Bengali loss.

Full tables and figures: `results/analysis/summary.md`. Status and integrity checks: `results/STATUS.md`. QA sample study: pending.

## Repository

```text
PROTOCOL.md            methods, analysis plan, deviations, limitations
LOG.md                 dated record of what happened
data/
  prompts/             500-task corpus, EN / BN / BN-CS (v0.3.1, frozen)
  annotations/         gold/ (157 accepted rubrics), drafts/ (343)
  config/              study, model and judge settings
  validation/          judge validation sets with reference scores
results/
  responses/           one JSONL per model
  scores/              judge ratings per response
  validation/          judge scores and agreement results on the validation sets
  analysis/            results.json, summary.md, figures
  STATUS.md            generated status and integrity report
scripts/               numbered pipeline (below), common.py, tests/
notebooks/analysis.ipynb   walkthrough of the results
```

## Running the pipeline

| Step | Command | What it does | Cost |
|---|---|---|---|
| 01 | `python3 scripts/01_validate_inputs.py` | Validates corpus, annotations, config and validation sets | free |
| 02 | `python3 scripts/02_generate.py run --model sol\|qwen\|gemma` | Generates missing responses (`plan` lists them) | Sol paid; Qwen/Gemma need a CUDA GPU |
| 03 | `python3 scripts/03_validate_judge.py assess --set heldout` | Judge agreement with reference scores (`run` scores fixtures) | `run` paid |
| 04 | `python3 scripts/04_score.py run` | Scores unscored responses with the validated judge (`plan` lists them) | paid |
| 05 | `python3 scripts/05_status.py` | Integrity checks; writes `results/STATUS.md` | free |
| 06 | `python3 scripts/06_analyze.py` | Pre-registered analysis; writes `results/analysis/` | free |
| tests | `python3 -m unittest discover -s scripts/tests` | Tests for every step and the notebook | free |

Each step resumes where it stopped. Paid steps take a `--max-usd` cap per run.

**Requirements:**
- Python 3.11+ with `numpy` and `matplotlib`.
- Paid steps: `OPENAI_API_KEY` in `.env`.
- Local generation: `torch` 2.14 and `transformers` 5.20 on a CUDA GPU with BF16 support, using the pinned checkpoints in the Hugging Face cache.
