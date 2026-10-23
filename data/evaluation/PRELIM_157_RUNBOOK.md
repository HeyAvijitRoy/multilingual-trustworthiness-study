# Preliminary 157-task evaluation runbook

This runbook executes the frozen preliminary evaluation defined by:

- `PRELIM_157_FREEZE.json`
- `PRELIM_157_MODELS.json`
- `PRELIM_157_PROTOCOL.md`
- `PRELIM_157_JUDGE.json`
- `PRELIM_157_SCORING_PLAN.md`
- `PRELIM_157_ANALYSIS_PLAN.md`

The preliminary evaluation contains 157 accepted tasks, 471 matched prompt instances per model and 1,413 planned responses across the three-model panel.

## 1. Local preflight

Use Python 3.11 where available.

```bash
python3 -m py_compile   scripts/prelim_eval_157.py   scripts/prelim_judge_157.py   scripts/analyze_prelim_157.py

python3 scripts/validate_all.py
python3 scripts/prelim_eval_157.py check
python3 scripts/prelim_eval_157.py plan
```

Do not proceed if the frozen-snapshot preflight fails.

## 2. Set API credentials locally

The runners read credentials only from environment variables:

```bash
export OPENAI_API_KEY='...'
export ANTHROPIC_API_KEY='...'
export GEMINI_API_KEY='...'
```

Do not place API keys in repository files or generated output records.

## 3. Calibrate the automated judge first

The judge gate is prospective and must pass before its study-response scores may be used.

```bash
python3 scripts/prelim_judge_157.py calibrate
python3 scripts/prelim_judge_157.py gate
```

Expected calibration input:
- 30 frozen fixtures
- 229 keyed scoring items

The frozen gate requires:
- ordinal Krippendorff alpha >= 0.80;
- critical-RIU exact agreement >= 0.90;
- safety-relevant task-check exact agreement = 1.00.

The local calibration artifacts are stored under `.local/prelim_157/`.

## 4. Generate the 1,413 study responses

Each provider runs up to eight requests concurrently.

For the simplest single-terminal execution:

```bash
python3 scripts/prelim_eval_157.py run --provider all
```

For faster wall-clock execution, run these in three separate terminals after the same preflight:

```bash
python3 scripts/prelim_eval_157.py run --provider openai
```

```bash
python3 scripts/prelim_eval_157.py run --provider anthropic
```

```bash
python3 scripts/prelim_eval_157.py run --provider google
```

Raw append-only outputs:

```text
data/outputs/prelim_157/openai.jsonl
data/outputs/prelim_157/anthropic.jsonl
data/outputs/prelim_157/google.jsonl
```

The runner is resume-safe: successful cells are not regenerated. A rerun attempts only cells without a successful record.

Check remaining cells at any time:

```bash
python3 scripts/prelim_eval_157.py plan
```

A complete generation run should show:
- OpenAI: 471 successful cells
- Anthropic: 471 successful cells
- Google: 471 successful cells

Any final API failures remain explicit missing cells and are not replaced by another model or changed prompt.

## 5. Score responses

The judge uses 12 concurrent requests and is blinded to the response provider/model identity.

```bash
python3 scripts/prelim_judge_157.py gate
python3 scripts/prelim_judge_157.py score --provider all
python3 scripts/prelim_judge_157.py plan --provider all
```

Score files:

```text
data/outputs/prelim_157/scores/openai.jsonl
data/outputs/prelim_157/scores/anthropic.jsonl
data/outputs/prelim_157/scores/google.jsonl
```

A complete scoring run should contain 471 scored cells per provider.

## 6. Run the frozen preliminary analysis

With all 1,413 cells scored:

```bash
python3 scripts/analyze_prelim_157.py
```

If final API failures remain and are being explicitly reported:

```bash
python3 scripts/analyze_prelim_157.py --allow-missing
```

Outputs:

```text
data/outputs/prelim_157/analysis/prelim_157_results.json
data/outputs/prelim_157/analysis/prelim_157_summary.md
```

The primary frozen estimand is:

```text
Critical Omission Rate(BN) - Critical Omission Rate(EN)
```

Positive values indicate more literal trustworthiness-critical omissions in Bengali.

## 7. Scoring QA before abstract figures are treated as final preliminary results

Follow `PRELIM_157_SCORING_PLAN.md`:

- inspect every critical RIU scored below 1;
- inspect every task-check failure;
- inspect every refusal/non-answer;
- inspect every truncated response;
- inspect the deterministic stratified sample specified by the scoring plan.

Preserve raw generation and raw judge records. Any score correction belongs in a separate adjudication layer rather than overwriting raw outputs.

## Reporting boundary

These results must be described as the **preliminary 157-task evaluation**. They do not replace the planned final 500-task production-gold evaluation.
