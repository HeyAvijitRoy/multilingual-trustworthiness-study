# Judge validation sets

Both sets pair a prompt and a constructed response with a rubric and human reference scores. `scripts/03_validate_judge.py` compares the automated judge with the references.

Acceptance thresholds, all required:
- ordinal Krippendorff's alpha ≥ 0.80 over RIUs;
- critical-RIU exact agreement ≥ 0.90;
- safety-check exact agreement = 1.00.

## `heldout/`: 88 fixtures (validation of procedure `scoring-0.5`)

**Design.** 90 new fixture families: 5 domains × 3 languages × 6, with 2 acceptable, 2 unacceptable and 2 borderline responses per stratum.
- Each fixture has 4 RIUs (at least 2 critical) and `CHECK-01`; some also have a format check `CHECK-02`.
- Coverage targets the cases the procedure has to get right: negative constraints met by silence or violated, protected paths vs omitted safeguards, non-material vs material errors, false safety properties, inherently unsafe instructions, policy choices that defeat a requirement, multi-part format checks, distributed vs integrated rules, half credit, contradictions and refusals.
- The scenarios are new, with no translated variants and no overlap with the study prompts. `phenotype` records the intended category.

**References.** An independent bilingual reviewer scored every item blind to the intended category, and disagreements with the intended category were then resolved. Two fixtures with unresolved references were removed before the freeze, leaving 88 fixtures with 352 RIU items (183 critical) and 99 safety checks.

**Re-rate.** After the judge pass there were 8 disagreements. The reviewer then re-rated all items of those 8 fixtures blind, mixed with 12 decoy fixtures where reviewer and judge had agreed. The order was seeded random (seed 20261024), and the reviewer saw neither the judge scores nor which fixtures were disputed.
- **Decoys:** all 62 items kept their original reference.
- **Disputed fixtures:** 6 references changed and 2 stayed.

`references.csv` holds the final scores; `score_before_rerate` keeps the earlier value wherever it changed. `rerate.json` lists the disputed and decoy fixtures and the order used.

## `calibration/`: the original 30 fixtures

These 30 controlled responses are built on study tasks, covering partial reasoning, conditional safeguards, contradictions, wrong numbers and format failures in all three languages. The references are the answer key used for the human scoring calibration.

The automated judge with the earlier procedure (`scoring-0.3`) was assessed on this set on 2026-10-24 and failed the safety-check threshold (25/30). The set is now exposed to procedure development and is kept for transparency, not as held-out evidence.

## Results

Stored judge scores are in `results/validation/`.

| Set | Procedure | References | Alpha | Critical exact | Safety exact | Meets thresholds |
|---|---|---|---:|---:|---:|---|
| calibration | scoring-0.3 | answer key | 0.9605 | 0.990 (97/98) | 0.833 (25/30) | no |
| heldout | scoring-0.5 | before re-rate | 0.9774 | 0.995 (182/183) | 0.960 (95/99) | no |
| heldout | scoring-0.5 | final | 0.9906 | 1.000 (183/183) | 1.000 (99/99) | yes |
