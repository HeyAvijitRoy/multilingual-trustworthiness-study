<div align="center">

# 📘 Runbook

### Commands to reproduce, rerun and adapt the multilingual trustworthiness study

[Setup](#1--setup) · [Reproduce](#2--reproduce-the-reported-results-free) · [Notebook](#3--notebook) · [Paid steps](#4--rerun-judge-validation-and-scoring-paid) · [Generation](#5--regenerate-responses) · [Adapt](#6--adapt-the-study) · [Troubleshooting](#7--troubleshooting)

</div>

---

## Overview

| Task | Sections | Cost | Hardware |
|---|---|---|---|
| Reproduce every reported table and figure from the stored responses and scores | 1, 2 | free | any CPU, under a minute |
| Browse the results interactively | 1, 3 | free | any CPU |
| Re-score fixtures or responses with the judge | 1, 4 | paid API | any CPU |
| Regenerate model responses | 1, 5 | Sol: paid API; Qwen/Gemma: free | CUDA GPU with BF16 for Qwen/Gemma |
| Add models, tasks or a judge | 1, 6 | depends | depends |

All commands are for Ubuntu (bash) and are run from the repository root. They were checked on Ubuntu 24.04 with Python 3.13; CI runs the tests on Python 3.11.

---

## 1 · Setup

**1.1 Create an environment** (Python 3.11 or later):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install numpy matplotlib
```

If the venv module is missing, install it first: `sudo apt install python3-venv`.

**1.2 Keep LF line endings.** Prompts, annotations, responses and scores are checked by SHA-256, and `.gitattributes` keeps `data/`, `results/` and `scripts/` on LF. Keep `core.autocrlf` off (`git config core.autocrlf false`) so that no tool converts them to CRLF.

**1.3 Check the inputs:**

```bash
python3 scripts/01_validate_inputs.py
```

Expected output:

```text
inputs valid: 500 tasks / 1,500 prompts; 157 gold tasks, 743 RIUs (348 critical); 343 drafts; validation sets heldout + calibration
```

**1.4 Run the tests** (about 10 seconds):

```bash
python3 -m unittest discover -s scripts/tests
```

Expected: `Ran 52 tests ... OK`.

---

## 2 · Reproduce the reported results (free)

All 1,433 responses and their scores are stored in `results/`, so these steps need no API key and no GPU. Run them in order.

| # | Command | Writes | Time |
|---|---|---|---|
| 2.1 | `python3 scripts/03_validate_judge.py assess --set calibration --procedure scoring-0.3` | `results/validation/calibration_scoring-0.3.result.json` | < 1 s |
| 2.2 | `python3 scripts/03_validate_judge.py assess --set heldout --before-rerate` | `results/validation/heldout_scoring-0.5.before-rerate.result.json` | < 1 s |
| 2.3 | `python3 scripts/03_validate_judge.py assess --set heldout` | `results/validation/heldout_scoring-0.5.result.json` | < 1 s |
| 2.4 | `python3 scripts/05_status.py` | `results/STATUS.md`, `results/status.json` | ~1 s |
| 2.5 | `python3 scripts/06_analyze.py` | `results/analysis/` (results, summary, two figures) | ~5 s |
| 2.6 | `python3 scripts/07_qa.py` | `results/qa/results.json`, `results/qa/summary.md` | ~2 s |
| 2.7 | `python3 scripts/08_robustness.py` | `results/robustness/` (results, summary, three manuscript figures) | ~25 s |

**What to expect.**
- 2.1 prints `"passes": false` (safety checks 25/30), 2.2 prints `"passes": false` (95/99) and 2.3 prints `"passes": true` (99/99). These are the three judge-validation results reported in the paper.
- 2.4 ends with `All checks pass.` in `results/STATUS.md` and exits with code 0.
- 2.5 prints the analysis summary. The primary estimate is `+0.003 [-0.014, +0.015]`.

**Check that nothing changed.** The scripts overwrite their outputs, so Git shows any difference from the committed results:

```bash
git diff --stat results/
git diff results/analysis/summary.md results/qa/summary.md results/robustness/summary.md
```

Only the `Generated` timestamps and, in `results.json` files, the last digit of a few floating-point values should differ. PNG figures can differ in bytes across `matplotlib` versions while showing the same values. To return to the committed outputs:

```bash
git checkout -- results/
```

**Change the number of bootstrap replicates** (the reported analysis uses 10,000):

```bash
python3 scripts/06_analyze.py --replicates 2000
```

---

## 3 · Notebook

`notebooks/analysis.ipynb` reads `results/` and re-runs steps 01, 03 (assess), 05 and 06 in order.

```bash
python -m pip install notebook
jupyter notebook notebooks/analysis.ipynb
```

Run the first code cell before the others; it locates the repository and imports the steps.

---

## 4 · Rerun judge validation and scoring (paid)

**4.1 API key.** Create `.env` in the repository root (it is ignored by Git):

```bash
echo 'OPENAI_API_KEY=your-key-here' > .env
```

A key already set in the environment takes precedence over `.env`.

**4.2 Judge validation on the held-out fixtures.** `run` scores only fixtures that have no stored score, so move the stored scores aside first:

```bash
mkdir -p .local/previous
mv results/validation/heldout_scoring-0.5.jsonl .local/previous/
python3 scripts/03_validate_judge.py run --set heldout --max-usd 5
python3 scripts/03_validate_judge.py assess --set heldout
```

**4.3 Study scoring.** `plan` lists unscored responses; `run` scores them and appends to `results/scores/<model>.jsonl`.

```bash
python3 scripts/04_score.py plan
mv results/scores/qwen.jsonl .local/previous/      # example: rescore one model
python3 scripts/04_score.py run --model qwen --max-usd 15
python3 scripts/05_status.py
python3 scripts/06_analyze.py
```

`--model` accepts `all`, `sol`, `gemini`, `qwen` or `gemma`; `--limit N` stops after N requests.

**Notes.**
- `--max-usd` caps the spend of one run (defaults: 5 for step 03, 40 for step 04). The run stops with `run spend reached $X` and resumes from that point on the next call.
- Failed requests are logged to `results/scores/<model>.errors.jsonl` and retried on the next run.
- For reference, the recorded cost of the study was USD 33.05 for scoring all 1,433 responses and USD 38.05 in total (`results/STATUS.md`).
- Rescoring removes the seven recorded review corrections for the affected responses, and the new judge outputs will not match the stored ones exactly.

---

## 5 · Regenerate responses

`plan` lists missing cells for a model, and `run` generates them in the study's seeded order, appending to `results/responses/<model>.jsonl`. Because every cell is already stored, move the file aside before regenerating:

```bash
python3 scripts/02_generate.py plan --model qwen
mv results/responses/qwen.jsonl .local/previous/
```

### 5.1 Sol (OpenAI Responses API, paid)

```bash
python3 scripts/02_generate.py run --model sol --max-usd 10
```

The script refuses a response whose returned model differs from `gpt-6.1-sol`. The recorded generation cost for all 471 Sol responses was USD 3.17.

### 5.2 Qwen and Gemma (local GPU)

**Requirements:** a CUDA GPU with BF16 support (the study used one A100 40 GB), `torch` 2.14 and `transformers` 5.20. The exact package versions are in `data/config/models.json` under `versions`.

```bash
python -m pip install "torch==2.14.*" "transformers==5.20.*" "accelerate==1.15.*" "huggingface-hub==2.3.*" "safetensors==0.8.*"
```

**Download the pinned checkpoints** into the default Hugging Face cache. The script reads `~/.cache/huggingface/hub` and never downloads, so do not redirect `HF_HOME` or `HF_HUB_CACHE`.

```bash
hf download Qwen/Qwen3.5-9B --revision c202236235762e1c871ad0ccb60c8ee5ba337b9a
hf download google/gemma-4-12B-it --revision 707f0a3b8a3c7ad586ed01e27eafbad8a27dd0f7
```

**Generate:**

```bash
python3 scripts/02_generate.py run --model qwen --verify-weights
python3 scripts/02_generate.py run --model gemma --verify-weights
```

Before loading, the script checks the tokenizer and chat template against the SHA-256 values in `data/config/models.json`; `--verify-weights` also checks every weight file (slower, recommended on the first run). Decoding is greedy with thinking disabled, so the same checkpoint, software versions and hardware should reproduce the stored text closely, although GPU kernels can still introduce small differences.

**After any regeneration**, score the new responses and refresh the outputs:

```bash
python3 scripts/04_score.py run --model qwen --max-usd 15
python3 scripts/05_status.py
python3 scripts/06_analyze.py
python3 scripts/08_robustness.py
```

---

## 6 · Adapt the study

The pipeline reads the panel, tasks and judge from `data/config/`. Some per-model tables also name the three primary models in code, as listed below.

### 6.1 Add a model

1. Add an entry to `data/config/models.json`.
   - **OpenAI model:** `key`, `model_id`, `role` (`primary` or `exploratory`), `provider: "openai"`, `api: "responses"`, `reasoning`, `service_tier`, `timeout_seconds`, `order_offset`.
   - **Local model:** `key`, `model_id`, `role`, `provider: "local"`, `revision`, `precision`, `quantization`, `context_tokens`, `enable_thinking`, `do_sample`, `seed`, `prefill_chunk_size`, `attention_backend`, `versions`, `tokenizer_sha256`, `chat_template_sha256`, `weights_sha256`, `order_offset`. Compute the hashes from the snapshot folder, for example `sha256sum ~/.cache/huggingface/hub/models--<org>--<name>/snapshots/<revision>/tokenizer.json`.
   - Use a new `order_offset` so the model gets its own seeded cell order.
2. Add the key to the `--model` choices in `scripts/02_generate.py` (`main`, the `choices=['sol', 'qwen', 'gemma']` argument).
3. For an OpenAI model, add its per-million-token prices to `RATES` in `scripts/common.py` so that spend caps and cost records work.
4. For per-model QA and robustness tables, add the key to the model tuples in `scripts/07_qa.py` (`by_model`) and `scripts/08_robustness.py` (`PRIMARY`, `NAMES` and the per-model loops).
5. Run steps 02, 04, 05 and 06. Step 06 includes every model whose `role` is `primary` and weights the primary models equally in the panel estimate.

### 6.2 Add tasks

1. The corpus in `data/prompts/` is frozen at v0.3.1. Its construction rules are in `data/prompts/README.md`.
2. Write a rubric for each new task following `data/annotations/README.md`, with `status: "accepted"` and `prompt_sha256` set to the hashes of the three prompt strings, and place it in `data/annotations/gold/<domain>.jsonl`. The 343 rubrics in `data/annotations/drafts/` are a starting point.
3. Add the task to the `tasks` list in `data/config/study.json`.
4. Run `python3 scripts/01_validate_inputs.py`, then steps 02 and 04–06 for the new cells.

### 6.3 Change the judge

1. Edit `data/config/judge.json` (model, reasoning effort, thresholds). If the scoring instructions change, give the procedure a new name in `SCORING_PROCEDURE` and `RULES` in `scripts/common.py`.
2. Validate before scoring any study response:

   ```bash
   python3 scripts/03_validate_judge.py run --set heldout --max-usd 5
   python3 scripts/03_validate_judge.py assess --set heldout
   ```

3. Score with step 04 only after `assess` reports `"passes": true`. The held-out references are described in `data/validation/README.md`.

---

## 7 · Troubleshooting

| Message | Cause | Fix |
|---|---|---|
| `OPENAI_API_KEY missing` | No key in the environment or `.env` | See 4.1 |
| `run spend reached $X` | The `--max-usd` cap was reached | Rerun the same command; it resumes |
| `CUDA BF16 required` | No CUDA GPU, or the GPU lacks BF16 | Use a BF16-capable GPU (Ampere or newer) |
| `<file> differs from the pinned checkpoint` | Wrong revision or a modified file in the cache | Re-download with the exact `--revision` from 5.2 |
| `model parameters must all be on the GPU` | Not enough GPU memory for the full model | Use a larger GPU; offloading is not allowed |
| `returned model ...` | The API served a different model than requested | Check the model ID and account access |
| `unterminated record <file>:<line>` | A run was interrupted while writing | Remove the incomplete last line of that file and rerun |
| `05_status.py` exits with code 1 | An integrity check failed (missing cell, duplicate, hash mismatch) | Read the problems listed in `results/STATUS.md` |
| Hash mismatches right after checkout | Line endings were converted to CRLF | See 1.2, then check out the files again |

---

<div align="center">

[README](README.md) · [Protocol](PROTOCOL.md) · [Study log](LOG.md)

</div>
