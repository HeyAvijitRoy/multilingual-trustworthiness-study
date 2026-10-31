# Study status

Generated 2026-10-31 07:25 UTC by `scripts/05_status.py`.

## Responses and scores

| Model | Role | Responses | EN / BN / BN-CS | Scored | Truncated | Generation USD | Scoring USD |
|---|---|---:|---|---:|---:|---:|---:|
| gpt-6.1-sol | primary | 471 | 157 / 157 / 157 | 471 | 0 | 3.17 | 8.31 |
| gemini-3.8-flash | exploratory | 20 | 5 / 7 / 8 | 20 | 0 | 0.00 | 0.48 |
| Qwen/Qwen3.5-9B | primary | 471 | 157 / 157 / 157 | 471 | 2 | 0.00 | 12.88 |
| google/gemma-4-12B-it | primary | 471 | 157 / 157 / 157 | 471 | 0 | 0.00 | 11.38 |

## Judge validation

| Set | Fixtures | Ordinal alpha | Critical exact | Safety exact | Meets thresholds |
|---|---:|---:|---:|---:|---|
| calibration_scoring-0.3 | 30 | 0.9605 | 0.9898 | 0.8333 | no |
| heldout_scoring-0.5.before-rerate | 88 | 0.9774 | 0.9945 | 0.9596 | no |
| heldout_scoring-0.5 | 88 | 0.9906 | 1.0000 | 1.0000 | yes |

Recorded API cost: USD 38.05 (generation, scoring and validation records in `results/`).

## Integrity

All checks pass.

## Notes

- Gemini is exploratory: 20 of 60 planned responses (20 matched tasks x 3 languages); collection stopped and Gemini is excluded from the primary analysis.
- QA sample study (independent check of a sample of study scores): done, see results/qa/summary.md.
