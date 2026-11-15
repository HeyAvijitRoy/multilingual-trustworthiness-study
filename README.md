<div align="center">

# 🌐 Beyond Omission

### Measuring Critical-Information Fulfillment of Large Language Models in Bengali and English

Code, data and results for the paper. Tasks are written in English (EN), natural Bengali (BN) and Bengali–English code-switching (BN-CS).

![Languages](https://img.shields.io/badge/languages-EN%20%7C%20BN%20%7C%20BN--CS-2b6cb0)
![Tasks](https://img.shields.io/badge/tasks-157%20scored%20%2F%20500%20corpus-2f855a)
![Responses](https://img.shields.io/badge/responses-1%2C413-6b46c1)
![Python](https://img.shields.io/badge/python-3.11%2B-3776ab)

[Overview](#-overview) · [Results](#-results) · [Repository](#%EF%B8%8F-repository) · [Pipeline](#%EF%B8%8F-pipeline) · [Runbook](RUNBOOK.md) · [Protocol](PROTOCOL.md)

</div>

---

## 🔎 Overview

This repository accompanies a study of whether large language models leave out trustworthiness-critical information when the same task is asked in Bengali instead of English. Each task is written in English (EN), natural Bengali (BN) and Bengali-matrix Bengali–English code-switching (BN-CS). Responses are scored against rubrics of required information units (RIUs) that were written before any model was run.

| | |
|---|---|
| 📋 **Tasks** | 157 with accepted gold rubrics (743 RIUs, 348 of them critical) |
| 🤖 **Models** | `gpt-6.1-sol`, Qwen3.5-9B, Gemma 4 12B |
| 💬 **Responses** | 157 tasks × 3 languages × 3 models = 1,413 |
| ⚖️ **Scoring** | An automated judge (`gpt-5.4-2026-03-05`), validated against reviewer-scored reference fixtures |

On the 88 held-out fixtures, judge agreement with the original references was alpha 0.9774, critical 182/183 and task checks 95/99. After a blind re-rate of the disputed fixtures, agreement was alpha 0.9906, critical 183/183 and task checks 99/99.

---

## 📊 Results

<div align="center">

| Model | Critical coverage<br>EN / BN / BN-CS | Critical omission<br>EN / BN / BN-CS |
|:---|:---:|:---:|
| gpt-6.1-sol | 0.981 / 0.978 / 0.994 | 0.000 / 0.000 / 0.004 |
| Qwen3.5-9B | 0.888 / 0.799 / 0.829 | 0.007 / 0.018 / 0.030 |
| Gemma 4 12B | 0.859 / 0.792 / 0.835 | 0.019 / 0.022 / 0.019 |

</div>

Paired, domain-equal language effects across the three models, with 95% CIs:

| Effect | Estimate [95% CI] | Reading |
|---|:---:|---|
| 🎯 **Primary:** critical omission rate, BN − EN | +0.003 [−0.014, +0.015] | Critical information is rarely left out entirely in any language. |
| Critical coverage, BN − EN | −0.050 [−0.079, −0.022] | In Bengali, critical content is more often present but incorrect or insufficient. The effect comes from Qwen (−0.082) and Gemma (−0.068); Sol shows little difference (−0.002). |
| Strict complete-task success, BN − EN | −0.093 [−0.131, −0.055] | Fewer Bengali responses meet every requirement and pass every task check. |
| RIU coverage, BN-CS − BN | +0.028 [+0.012, +0.045] | Code-switching recovers part of the Bengali loss in overall coverage. |

> [!NOTE]
> Post hoc robustness checks (judge agreement by language, length control, leave-one-domain-out, token premium) are in [`results/robustness/summary.md`](results/robustness/summary.md). The coverage and success gaps hold in all of them. The primary omission estimate is +0.011 [+0.003, +0.019] when technical troubleshooting is dropped. A blind reviewer check of the judge's reason codes ([`results/qa/reasons/summary.md`](results/qa/reasons/summary.md)) agreed on whether a critical unit was omitted for 79 of 81 units (kappa 0.936).

**Score review.** The results include seven item corrections made after reviewing the 17 QA disagreements. Each corrected score keeps its original rating, evidence and review rationale, and [`results/analysis/summary.md`](results/analysis/summary.md) reports the initial and reviewed effects side by side. QA agreement is computed against the initial judge scores.

**QA sample.** One reviewer rated 60 responses (352 items) blind to model identity and to the judge's scores ([`results/qa/summary.md`](results/qa/summary.md)). Agreement with the judge was alpha 0.843, critical exact 0.979 and CHECK-01 exact 0.933 (56/60), with all task checks combined at 0.935 (58/62). The task-check threshold of 1.00 was not met; see [`PROTOCOL.md`](PROTOCOL.md).

---

## 🗂️ Repository

```text
PROTOCOL.md            methods, analysis plan, deviations, limitations
RUNBOOK.md             step-by-step commands to reproduce, rerun or adapt the study
LOG.md                 dated record of the study
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
  qa/                  QA sample: selection, reviewer ratings, agreement; reasons/ holds the reason-code check
  robustness/          post hoc checks and the manuscript figures
  STATUS.md            generated status and integrity report
scripts/               numbered pipeline (below), common.py, tests/
notebooks/analysis.ipynb   walkthrough of the results
```

---

## ⚙️ Pipeline

| Step | Command | What it does | Cost |
|:---:|---|---|---|
| 01 | `python3 scripts/01_validate_inputs.py` | Validates corpus, annotations, config and validation sets | free |
| 02 | `python3 scripts/02_generate.py run --model sol\|qwen\|gemma` | Generates missing responses (`plan` lists them) | Sol paid; Qwen/Gemma need a CUDA GPU |
| 03 | `python3 scripts/03_validate_judge.py assess --set heldout` | Judge agreement with reference scores (`run` scores fixtures) | `run` paid |
| 04 | `python3 scripts/04_score.py run` | Scores unscored responses with the validated judge (`plan` lists them) | paid |
| 05 | `python3 scripts/05_status.py` | Integrity checks; writes `results/STATUS.md` | free |
| 06 | `python3 scripts/06_analyze.py` | Prespecified analysis; writes `results/analysis/` | free |
| 07 | `python3 scripts/07_qa.py` | Compares the recorded reviewer QA ratings with judge scores; writes `results/qa/` | free |
| 08 | `python3 scripts/08_robustness.py` | Judge agreement by language and model, length control, reasons table, CHECK-01 contrasts; writes `results/robustness/` | free |
| ✅ | `python3 -m unittest discover -s scripts/tests` | Tests for every step and the notebook | free |

Each step resumes where it stopped, and paid steps take a `--max-usd` cap per run. All responses and scores are included, so `03_validate_judge.py assess` and steps 05–08 reproduce every reported table without any paid or GPU run. Exact commands, expected outputs and troubleshooting are in [`RUNBOOK.md`](RUNBOOK.md).

### Requirements

- 🐧 Ubuntu (commands in [`RUNBOOK.md`](RUNBOOK.md) are written for Ubuntu).
- 🐍 Python 3.11+ with `numpy` and `matplotlib`.
- 🔑 Paid steps: `OPENAI_API_KEY` in `.env`.
- 🖥️ Local generation: `torch` 2.14 and `transformers` 5.20 on a CUDA GPU with BF16 support, using the pinned checkpoints in the Hugging Face cache.

---

<div align="center">

[Runbook](RUNBOOK.md) · [Protocol](PROTOCOL.md) · [Study log](LOG.md) · [Full results](results/analysis/summary.md)

</div>
