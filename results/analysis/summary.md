# Results: preliminary 157-task study

Generated 2026-10-31 by `scripts/06_analyze.py` (10,000 bootstrap replicates, seed 20261023).

## Primary estimand

Critical omission rate, BN minus EN (positive = more critical omission in Bengali); paired by task, domain-equal, three primary models weighted equally.

| Model | Estimate | 95% CI | Paired tasks |
|---|---:|---|---:|
| gpt-6.1-sol | +0.000 | [+0.000, +0.000] | 137 |
| Qwen/Qwen3.5-9B | +0.007 | [-0.020, +0.027] | 137 |
| google/gemma-4-12B-it | +0.001 | [-0.028, +0.027] | 137 |
| **Panel** | **+0.003** | **[-0.014, +0.015]** | |

## Language means by model

| Model | Language | Critical omission | Critical coverage | RIU coverage | Strict complete-task | CHECK-01 pass |
|---|---|---:|---:|---:|---:|---:|
| gpt-6.1-sol | en | 0.000 | 0.981 | 0.982 | 0.917 | 1.000 |
| gpt-6.1-sol | bn | 0.000 | 0.978 | 0.979 | 0.917 | 1.000 |
| gpt-6.1-sol | bn_cs | 0.004 | 0.994 | 0.990 | 0.962 | 1.000 |
| Qwen/Qwen3.5-9B | en | 0.007 | 0.888 | 0.905 | 0.561 | 0.834 |
| Qwen/Qwen3.5-9B | bn | 0.018 | 0.799 | 0.802 | 0.414 | 0.796 |
| Qwen/Qwen3.5-9B | bn_cs | 0.030 | 0.829 | 0.843 | 0.446 | 0.732 |
| google/gemma-4-12B-it | en | 0.019 | 0.859 | 0.880 | 0.586 | 0.904 |
| google/gemma-4-12B-it | bn | 0.022 | 0.792 | 0.819 | 0.452 | 0.904 |
| google/gemma-4-12B-it | bn_cs | 0.019 | 0.835 | 0.854 | 0.484 | 0.873 |

## Secondary contrasts (panel and by model)

| Outcome | Contrast | Panel [95% CI] | gpt-6.1-sol | Qwen/Qwen3.5-9B | google/gemma-4-12B-it |
|---|---|---|---|---|---|
| critical omission rate | bn − en | +0.003 [-0.014, +0.015] | +0.000 | +0.007 | +0.001 |
| critical omission rate | bn_cs − bn | +0.005 [-0.005, +0.016] | +0.003 | +0.015 | -0.003 |
| critical omission rate | bn_cs − en | +0.008 [-0.002, +0.017] | +0.003 | +0.021 | -0.001 |
| critical coverage | bn − en | -0.050 [-0.079, -0.022] | -0.002 | -0.082 | -0.068 |
| critical coverage | bn_cs − bn | +0.026 [-0.001, +0.054] | +0.016 | +0.020 | +0.042 |
| critical coverage | bn_cs − en | -0.025 [-0.049, -0.000] | +0.014 | -0.062 | -0.025 |
| riu coverage | bn − en | -0.055 [-0.071, -0.039] | -0.003 | -0.102 | -0.059 |
| riu coverage | bn_cs − bn | +0.028 [+0.012, +0.045] | +0.011 | +0.040 | +0.034 |
| riu coverage | bn_cs − en | -0.026 [-0.040, -0.013] | +0.008 | -0.061 | -0.025 |
| strict complete task success | bn − en | -0.093 [-0.131, -0.055] | +0.000 | -0.146 | -0.132 |
| strict complete task success | bn_cs − bn | +0.036 [-0.007, +0.081] | +0.045 | +0.032 | +0.031 |
| strict complete task success | bn_cs − en | -0.057 [-0.098, -0.016] | +0.045 | -0.114 | -0.101 |

## Primary estimand by stratum

| Stratum | Panel [95% CI] | gpt-6.1-sol | Qwen/Qwen3.5-9B | google/gemma-4-12B-it |
|---|---|---|---|---|
| domain: cybersecurity_digital_safety | +0.015 [-0.006, +0.038] | +0.000 | +0.055 | -0.010 |
| domain: decision_support | +0.006 [+0.000, +0.020] | +0.000 | +0.000 | +0.019 |
| domain: information_synthesis | +0.002 [+0.000, +0.007] | +0.000 | +0.000 | +0.007 |
| domain: procedural_instructional | +0.019 [+0.000, +0.041] | +0.000 | +0.028 | +0.028 |
| domain: technical_troubleshooting | -0.029 [-0.108, +0.020] | +0.000 | -0.050 | -0.037 |
| difficulty: easy | +0.014 [+0.000, +0.032] | +0.000 | +0.033 | +0.010 |
| difficulty: medium | -0.015 [-0.066, +0.017] | +0.000 | -0.018 | -0.027 |
| difficulty: hard | +0.009 [-0.001, +0.020] | +0.000 | +0.004 | +0.022 |
| extended context only | +0.000 [+0.000, +0.000] | +0.000 | +0.000 | +0.000 |
| excluding extended context | +0.003 [-0.015, +0.015] | +0.000 | +0.007 | +0.001 |
| excluding truncated responses | +0.002 [-0.015, +0.015] | +0.000 | +0.006 | +0.001 |

## Exploratory: Gemini (20 tasks, descriptive only)

| Language | n | Critical omission | Critical coverage | RIU coverage |
|---|---:|---:|---:|---:|
| en | 5 | 0.000 | 1.000 | 0.914 |
| bn | 7 | 0.000 | 0.828 | 0.893 |
| bn_cs | 8 | 0.000 | 0.800 | 0.902 |

## Score review

7 item ratings were corrected after review of the 17 QA disagreements. These tables use corrected ratings; original ratings and review reasons remain in the score records. This targeted review is not a full revalidation of the judge. QA agreement in results/qa/ uses the initial judge ratings.

| Outcome / contrast | Initial [95% CI] | After review [95% CI] |
|---|---|---|
| critical_omission_rate:bn-en | +0.003 [-0.014, +0.015] | +0.003 [-0.014, +0.015] |
| critical_coverage:bn-en | -0.050 [-0.078, -0.021] | -0.050 [-0.079, -0.022] |
| strict_complete_task_success:bn-en | -0.093 [-0.131, -0.055] | -0.093 [-0.131, -0.055] |
| riu_coverage:bn_cs-bn | +0.027 [+0.011, +0.044] | +0.028 [+0.012, +0.045] |

Truncated responses retained in the primary analysis: qwen/PROC089/bn, qwen/TECH098/bn.
Scores originate from the automated judge, with recorded review corrections where present; the QA sample study is in results/qa/.
