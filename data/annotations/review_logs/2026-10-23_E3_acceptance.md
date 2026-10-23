# Expansion Calibration Batch E3 — acceptance record

Date: 2026-10-23
Study lead: AR
Protocol: 0.3
Prompt corpus: v0.3.1
Batch: E3

## Scope

This record covers the 22 tasks assigned prospectively to Expansion Calibration Batch E3 in `EXPANSION_BATCHES.json`.

Final E3 composition:
- 98 RIUs
- 46 critical
- 52 supporting
- 93 binary
- 5 ordinal

The batch spans all five study domains and all three difficulty levels. All three frozen prompt variants were considered for each task.

## Disposition

The E3 annotation set and methodological audit were checked and accepted on 2026-10-23.

Final boundary refinements before acceptance:
- SYN051: removed a duplicate no-guessing RIU because the unresolved-time/confirmation requirement already captured the same proposition.
- CYBER038: reclassified rollout validation from critical to supporting under the omission-consequence test.

The accepted batch preserves:
- protocol 0.3 scoring behavior
- standardized zero anchors
- CHECK-01 orthogonality
- binary/ordinal distinctions and concrete half-credit anchors
- EN/BN/BN-CS semantic alignment
- alternative valid answer paths
- frozen prompt and pilot-gold integrity

No prompt, pilot-gold, calibration, queue, or protocol amendment was required.

## Decision

**E3 ACCEPTED.**

The 22 E3 records are accepted expansion-calibration annotations. Final production-gold assembly remains a separate release step.
