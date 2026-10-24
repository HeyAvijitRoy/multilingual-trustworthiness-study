# Validation evidence — 2026-10-23 EDT / 2026-10-24 UTC

All checks below used the current working implementation before commit. No paid
API calls, study generations, real judge scores or human approvals were produced.

| Check | Observed result |
| --- | --- |
| `.local/venv/bin/python scripts/validate_all.py` | PASS; 90 unittest cases in 17.383s, plus all corpus/freeze/annotation/queue/calibration and whitespace checks |
| Original frozen scientific data versus `88818e5` (`git diff --diff-filter=M` over prompts, annotations, calibration, review and historical `PRELIM_157*`) | No modified original files; earlier new P01/P02 draft artifacts are additions, unchanged by this continuation |
| Historical `prelim_eval_157.py check` | PASS; same 157-task snapshot and original three models |
| Historical generation plan | 0/1,413 generated; all remaining |
| Four-model `check` | Historical integrity and candidate structure PASS; generation_ready=false |
| Four-model generation/scoring plan | 0/1,884 generated and scored; 471 per partition |
| Four-model local A `run --dry-run` | 471 planned cells; no request sent |
| Historical automated judge gate | Exit 3; calibration report absent |
| Four-model automated judge gate | Exit 3; gate_pass=false, report absent |
| Four-model readiness | Exit 3; actual approvals, final freeze and authorized cloud validation remain absent |
| New/modified inference, adapter, scoring, analysis, approval and plotting scripts | Python 3.11 compilation PASS; actual GPU paths also run under Python 3.12.3 |
| GPU environment | CUDA available, BF16 supported; 256x256 ones matmul gives 256 everywhere; uv checks all 55 packages compatible |
| Upstream artifact integrity | Both exact revisions' weight SHA256 and small-file Git blob hashes match; no basename inference |
| Final synthetic GPU suites | Two warmups + 8 ordinary repeats + near-40k capacity per model, completed; current runtime/benchmark source hashes match summaries |
| Real GPU server-adapter smoke | Both pass one synthetic generation, duplicate-request reuse, wrong-model and frozen-prompt refusal |
| Synthetic four-model analysis | 1,884 mock cells across four fixed models; paired known effect verified; provisional status retained |
| Calibration regression | Frozen 229 keyed items; synthetic oracle passes, safety disagreement/missing/duplicate fixtures rejected; not actual calibration |
| Resume/provenance regressions | Ambiguous calls, duplicate successes, stale source/mode/manifest, cross-cell outcomes and attempt-budget reset rejected |
| Adjudication regressions | Source response/raw-score and review-log hash checks, explicit revision chain; no reviewer authenticity certification |
| Figure smoke | Synthetic-only Matplotlib fixture exported PNG/PDF/SVG plus provenance; primary figure visually inspected, NA shown without invented estimate |

`gpu/BENCHMARK_SUMMARY.json` and `gpu/ADAPTER_SMOKE.json` contain only sanitized
numeric/provenance summaries, with ignored raw source paths and SHA256 links.
All earlier failures remain locally preserved and are indexed in
`gpu/FAILED_RUNS.json`. Weight files, keys and raw outputs are excluded from Git.
The existing user change to `.gitignore` (adding `.env`) is preserved and not
included in these commits. Neither reference nor prior CPU environment was altered.

Tests of agreement thresholds use synthetic key-derived labels solely as test
fixtures. They are not judge calibration statistics. The 1,884-cell report test
uses synthetic outcomes and a reduced bootstrap count for test runtime; actual
analysis retains the prespecified 10,000 replicates. The figure fixture is plainly
marked synthetic and remains ignored. There are no actual preliminary findings.
