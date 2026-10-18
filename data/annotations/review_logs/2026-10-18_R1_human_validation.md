# Human validation by R1

- Validator: **R1** (anonymized ID; identity held by the study lead)
- Date: 2026-10-18
- Role: the study's single human validator, competent in English and Bengali, under the one-validator rule in `ANNOTATION_PROTOCOL.md`
- Recorded by: Claude (AI), from the study lead's report on 2026-10-18

## Scope

1. **Prompt corpus v0.3:** the Bengali (`prompt_bn`) and Bengali-English code-switched (`prompt_bn_cs`) realizations of all 500 tasks, checked for language quality and semantic equivalence with `prompt_en`. Byte-pinned in `data/annotations/PROMPT_FREEZE.json`.
2. **The 25 pilot RIU records** after rubric revision 2 (`data/annotations/pilot_*.jsonl`), checked for unit boundaries, coverage, criticality, scoring anchors, requirement visibility, task checks and equivalence across EN, BN and BN-CS.

## Outcome

**Validated.** R1 confirmed both items as they stand, with no changes requested.

- The five judgment calls listed in `2026-10-18_AI_pilot_validation.md` are accepted as currently written.
- No disagreements were recorded, so no adjudication was needed.

## Provenance

The study lead reported this outcome. R1 checked the prompts and records directly and confirmed them; no decision sheet was used or is expected for this validation. `pilot_human_review_sheet.csv` remains available as an optional aid for future validation rounds.

## Effect on records

- **Pilot records:** the `review.independent_human_review` and `review.language_equivalence_review` fields reference this log, and `status` is `human-reviewed`. The records are not `frozen`; gold freeze still requires the sign-off step in `ANNOTATION_PROTOCOL.md`.
- **Corpus:** v0.3 documentation states that it was validated by R1 and frozen by the study lead.

## Addendum: corpus v0.3.1 (2026-10-18)

R1 confirmed the one-line English clarification in SYN079 ("The deadline is Friday of the following week."), which aligns the English with the existing Bengali and BN-CS wording. Reported by the study lead the same day. Corpus v0.3.1 is validated and frozen.
