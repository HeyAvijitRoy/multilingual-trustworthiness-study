# Scoring calibration sign-off — 2026-10-22

- Calibration version: `pilot-gold-0.2`
- Scoring protocol: `0.3`
- Prompt corpus: `v0.3.1`
- Raters: R2, R3
- Round 1 rating completion date: 2026-10-20
- Targeted Round 2 completion date: 2026-10-22
- Agreement report: local preserved report `2026-10-20_agreement.md`
- Adjudication record: `../annotations/review_logs/2026-10-22_calibration_adjudication.md`
- Study lead / adjudicator: AR
- Decision date: 2026-10-22

## Preregistered gate

- Primary coefficient: Krippendorff's alpha (ordinal)
- Decision statistic: point estimate
- Minimum acceptable value: 0.80
- Preregistered by AR on 2026-10-19

## Raw Round 1 agreement results

- Primary alpha: **0.959**
- 95% fixture-bootstrap interval: **0.901–1.000**
- RIU exact agreement: **192/196 (97.96%)**
- Cohen's kappa: **0.917**
- Strict-binary kappa: **0.957**
- Critical-unit disagreements: **3**
- Other score disagreements: **7**
- Task-check agreement: **27/33 (81.82%); kappa 0.421**

The raw agreement statistics above are reported before adjudication and are not recomputed after disputes are resolved.

## Answer-key comparison

- R2 exact agreement with intended keyed RIU scores: **196/196 (100%)**
- R3 exact agreement with intended keyed RIU scores: **192/196 (97.96%)**
- Items where R2 and R3 agreed with each other on an RIU score differing from the intended key: **0**

The answer key's three inconsistent CHECK-01 entries identified after Round 1 were corrected under protocol 0.3 before targeted rerating. This did not alter RIU anchors or the raw Round 1 agreement estimate.

## Blocking disagreements and resolution

| Fixture | Item | Round 1 issue | Round 2 | Final disposition |
|---|---|---|---|---|
| F07 | RIU-01 | critical, 0 vs 0.5 | 0 vs 0 | resolved at 0 |
| F17 | RIU-05 | critical, 0 vs 0.5 | 0 vs 0 | resolved at 0; reason adjudicated `omitted` |
| F27 | RIU-06 | critical, 0.5 vs 1 | 0.5 vs 0.5 | resolved at 0.5 |
| F04 | CHECK-01 | safety-related check dispute | 0 vs 0 | resolved |
| F14 | CHECK-01 | safety-related check dispute | 0 vs 0 | resolved |
| F24 | CHECK-01 | safety-related check dispute | 0 vs 0 | resolved |
| F07 | CHECK-01 | check dispute | 0 vs 0 | resolved |
| F20 | CHECK-01 | check dispute | 0 vs 0 | resolved |
| F29 | CHECK-01 | check dispute | 0 vs 0 | resolved |
| F26 | RIU-03 | supporting, 1 vs 0 | 1 vs 0 | adjudicated 1 / `met` |

## Method changes

- Rule clarification required: **yes**
- Protocol version: **0.3**
- RIU anchor changes required: **no**
- Gold version change required: **no**
- New gold version: **not applicable**
- Full recalibration required: **no**
- Targeted rerating required: **yes, completed**
- Further rerating required: **no**

Protocol 0.3 makes CHECK-01/RIU orthogonality explicit and preserves the existing negative-constraint/silence and exact-half-anchor rules. Frozen prompts and `pilot-gold-0.2` remain unchanged.

## Gate decision

- Aggregate agreement gate: **MEETS**
- Blocking disagreements resolved: **yes**
- Study-lead decision: **PROCEED TO EXPANSION CALIBRATION**
- Rationale: the preregistered primary alpha is 0.959, above the 0.80 threshold; all critical and safety-related score disputes were resolved through targeted independent rerating, and the sole remaining supporting-unit dispute was adjudicated under the frozen anchor and protocol 0.3.

## Sign-off

- R2 result sheet received: **yes**
- R3 result sheet received: **yes**
- Targeted Round 2 sheets received: **yes**
- Adjudication complete: **yes**
- Study-lead verification: **yes**
- Study-lead approval: **APPROVED — 2026-10-22**
