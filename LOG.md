# Study log

What happened, by date. Methods are in `PROTOCOL.md`; current numbers are in `results/STATUS.md` and `results/analysis/summary.md`.

| Date | Event |
|---|---|
| 2026-09-23 | Study protocol drafted. 500-task prompt corpus created: five domains, three language conditions. |
| 2026-09-24 | Corpus v0.2: difficulty rebalanced to 25/50/25 per domain; extended-context subset SYN091–SYN100 expanded. |
| 2026-10-07 | RIU annotation schema and 25-task pilot rubrics created. |
| 2026-10-18 | Corpus v0.3: BN and BN-CS hand-rewritten for all 500 tasks after review found grammar, meaning and calque problems in v0.2. Validated by the independent reviewer. |
| 2026-10-18 | Corpus v0.3.1: SYN079 English deadline clarified. Corpus frozen. Single-reviewer protocol for rubric review adopted. Pilot rubric revision 2 applied. |
| 2026-10-19 | Pilot frozen as gold (`pilot-gold-0.2`). Scoring-agreement threshold pre-registered (ordinal alpha ≥ 0.80). 30 calibration fixtures written. |
| 2026-10-20 | Human scoring calibration round 1: alpha 0.959 (two independent raters). |
| 2026-10-22 | `CHECK-01` clarified as orthogonal to RIU scores (protocol 0.3). Targeted round 2 resolved the disputed items. Scoring calibration signed off. Expansion batches E1 and E2 accepted. |
| 2026-10-23 | Expansion batches E3–E6 accepted: 157 gold tasks, 743 RIUs, 348 critical. Task snapshot, analysis plan and model panel frozen. USD 100 budget set. |
| 2026-10-23 | Panel set to Sol, Gemini 3.8 Flash, Qwen3.5-9B and Gemma 4 12B; judge set to GPT-5.4. Local GPU (A100 40 GB) verified. Draft rubrics prepared for the remaining 343 tasks. |
| 2026-10-23 | Judge (procedure scoring-0.3) failed calibration on safety checks: 25/30 against 30/30 required; alpha 0.9605, critical 97/98. Scoring held. |
| 2026-10-24 | Generation started with Sol, Qwen and Gemma as the primary panel; Gemini moved to an exploratory 20-task sample. Sol finished 471/471. |
| 2026-10-24 | Independent adjudication of the 7 disputed calibration judgments: all 7 supported the references. The causes were traced to gaps in the judge instructions. Procedure scoring-0.5 written and pinned. |
| 2026-10-24 | 90-fixture held-out validation set built; references set blind to intent; frozen at 88 fixtures. |
| 2026-10-24 | Qwen and Gemma finished 471/471 each. All 1,413 primary responses collected and integrity-checked; 2 Qwen responses truncated at the output cap. |
| 2026-10-24 | Held-out validation of scoring-0.5: alpha 0.9774, critical 182/183, safety 95/99, below threshold. |
| 2026-10-24 | Blind re-rate of the 8 disputed held-out fixtures, mixed with 12 decoys: decoys 62/62 unchanged; 6 references revised, all toward the judge. With the final references: alpha 0.9906, critical 183/183, safety 99/99. Thresholds met. |
| 2026-10-25 | Scoring-0.5 released for production. All 1,433 responses scored (1,413 primary and 20 Gemini), with one transient error retried; scoring cost USD 33.05. |
| 2026-10-25 | Gemini collection stopped at 20 of 60 responses; Gemini kept as exploratory. |
| 2026-10-25 | Pre-registered analysis run. Primary estimand (critical omission rate, BN − EN): +0.003 [−0.014, +0.015]. Critical coverage BN − EN: −0.050 [−0.078, −0.021]. |
| 2026-10-25 | Repository consolidated: one protocol, one log, a numbered six-step pipeline with tests, and results stored in `results/`. |
| Pending | QA sample study of study scores. |
