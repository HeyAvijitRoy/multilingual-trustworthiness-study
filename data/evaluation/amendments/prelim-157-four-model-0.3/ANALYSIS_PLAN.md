# Four-model analysis amendment candidate, 0.3

Not approved/frozen. Carry forward the exact task-level metrics, reasons and
criticality in historical `PRELIM_157_ANALYSIS_PLAN.md` and annotation protocol
0.3. Primary estimand remains Critical Omission Rate(BN) − Critical Omission
Rate(EN): paired task differences within domain, then five equal domain weights.
The amended panel average gives **four** fixed models equal weight. Never infer
panel membership from observed outputs or omit an entirely missing model.

Carry forward all three-language secondary contrasts, separate ordinal and
strict coverage, domain/difficulty and SYN091–SYN100 strata, and truncation
sensitivity. Use 10,000 task-clustered bootstrap replicates within domain, seed
20261023, carrying all language/model observations in each sampled cluster;
report model-specific and pooled estimates/CIs. Report undefined effects as NA,
explicit pair counts and all missingness, without imputation or relabeling an
API failure as refusal. Secondary intervals remain descriptive; no retrospective
primary outcomes or significance claims. Distinguish genuine omitted content
from incorrect, insufficient and partially met content.

Report implementation/precision/quantization/context differences and the limited
fixed panel. A local-vs-cloud difference cannot establish an architectural or
capacity-matched causal effect. Diagnostic generations are excluded entirely.
Historical panel results, if later discovered, remain separately identified;
their outputs cannot be silently pooled with newly generated cloud cells.

The existing historical analysis command is for 1,413 historical cells only.
`scripts/analyze_prelim_four.py` implements the amended fixed-panel analysis,
source validation and separate adjudication ingestion using the shared historical
metric/bootstrap functions. Independent human QA-completion evidence remains an
external requirement. `scripts/plot_prelim_four.py` exports standalone PNG/PDF/SVG
figures from a saved report, showing paired primary-effect intervals and separate
descriptive language means with defined-cell denominators. Figure provenance pins
the source report and plotting implementation/dependency versions.
Do not feed four-model records to the historical command by renaming files.
No actual amended study estimates have been computed; synthetic end-to-end test
estimates are not scientific results.


The fixed revised identities are Sol / Gemini 3.8 Flash / Qwen3.5-9B / Gemma 4
12B; they never change according to available scores. The primary judge is
prospectively proposed as dated GPT-5.4, not the Sol generator. No calibration
or study outcome exists for this version. Do not pool 0.2, historical or synthetic
outputs with 0.3. Free-tier execution may span days: report generation dates,
model-version metadata, quota deferrals and potential temporal/provider drift.
These operational differences do not change the estimand, bootstrap or missingness
definitions; a quota pause is pending work, not an omitted answer or API refusal.

Human-QA first-pass ratings are collected before unblinding AI labels. The separate
`audit_four_qa.py` reports paired human/AI agreement, denominators and critical/safety
escalations by model/language and review-selection stratum, using validated source
scores. Selected QA strata do not provide an unbiased overall agreement estimate.
Resolved adjudication remains separate from raw first-pass agreement and raw AI
scores. Report same-provider judge bias and the limited diagnostic/fixture evidence
as limitations; do not claim that a different model ID establishes independent
human evaluation or removes all correlated error.
