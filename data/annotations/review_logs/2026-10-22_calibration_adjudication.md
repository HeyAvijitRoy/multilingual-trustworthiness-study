# Calibration adjudication — 2026-10-22

## Scope

This record closes the human scoring-calibration disputes identified in Calibration Round 1 and the targeted Round 2 rerating under annotation protocol 0.3.

Round 1 remains the original preregistered agreement estimate. Round 2 was a targeted rule-clarification/dispute-resolution step and does not replace or recompute the original overall agreement coefficient.

## Round 1 agreement

- Raters: R2, R3
- Completed rating date: 2026-10-20
- RIU exact agreement: 192/196 (97.96%)
- Cohen's kappa: 0.917
- Krippendorff's alpha (ordinal): 0.959
- 95% fixture-bootstrap CI: 0.901–1.000
- Strict-binary kappa: 0.957
- Task-check exact agreement: 27/33 (81.82%)
- Task-check Cohen's kappa: 0.421
- Preregistered gate: alpha point estimate >= 0.80
- Gate result: MEETS

Round 1 produced 10 score disagreements, including three critical-unit disagreements and safety-related CHECK-01 disagreements.

## Protocol clarification

On 2026-10-22, protocol 0.3 clarified that CHECK-01 is orthogonal to RIU scoring. A material unsupported factual or operational assertion may therefore fail both an RIU and CHECK-01. Three inconsistent intended CHECK-01 scores in the calibration key (F04, F14 and F24) were corrected accordingly.

No frozen prompt, RIU boundary, criticality label, RIU scoring anchor, fixture response or pilot-gold-0.2 record changed.

## Targeted Round 2

R2 and R3 independently rerated only the 10 Round 1 disputed items using protocol 0.3 instructions, without access to each other's prior ratings or the answer key.

Results:

- 9/10 targeted item scores agreed.
- All 3 formerly disputed critical units agreed:
  - F07 / DEC001 / RIU-01 = 0
  - F17 / DEC004 / RIU-05 = 0
  - F27 / DEC010 / RIU-06 = 0.5
- All 6 targeted CHECK-01 scores agreed at 0 (flagged).
- One supporting-unit score dispute remained:
  - F26 / PROC001 / RIU-03: R2 = 1, R3 = 0

## Human adjudication

Adjudicator: AR  
Date: 2026-10-22

### F26 / PROC001 / RIU-03

- Criticality: supporting
- Scoring mode: binary
- R2: 1 / met
- R3: 0 / omitted
- Adjudicated score: **1**
- Adjudicated reason: **met**

Rationale: the frozen RIU states that file extensions are preserved when the proposed renaming keeps or does not touch extensions. The fixture proposes descriptive renaming but does not instruct changing or removing extensions. Under the protocol's negative-constraint/silence rule, this satisfies the requirement.

### F17 / DEC004 / RIU-05 reason classification

- R2: 0 / omitted
- R3: 0 / insufficient
- Adjudicated score: **0**
- Adjudicated reason: **omitted**

Rationale: the fixture lists individual factors but never states how they are combined or used to select among competing requests. The required prioritization rule is absent rather than merely weakly evidenced.

### Task-check reason labels

The six targeted CHECK-01 items have identical scores of 0 after Round 2. R2 and R3 used different free-text reason labels for task checks. Task-check reason labels are not constrained to the RIU reason-code scale and are not a separate inferential outcome in this calibration.

No returned rater sheet is altered. The task-check score plus quoted evidence is the authoritative judgment; the raw reason-label differences are preserved as provenance.

## Disposition of Round 1 blockers

All formerly blocking critical-unit score disagreements are resolved.

All targeted safety-related CHECK-01 score disagreements are resolved.

The remaining supporting-unit disagreement is resolved by human adjudication above.

No unresolved safety, semantic-equivalence or critical-unit scoring dispute remains.

## Method impact

- Protocol clarification required: yes — protocol 0.3
- RIU scoring-anchor change required: no
- Frozen gold change required: no
- New pilot-gold version required: no
- Full recalibration required: no
- Targeted rerating required: yes — completed
- Further rerating required: no

## Final disposition

Calibration is accepted for progression to expansion calibration.

The original Round 1 alpha of 0.959 remains the preregistered agreement result. Adjudication is reported separately and does not alter that coefficient.
