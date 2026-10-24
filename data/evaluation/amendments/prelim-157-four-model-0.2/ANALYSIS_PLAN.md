# Four-model analysis amendment candidate, 0.2

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
