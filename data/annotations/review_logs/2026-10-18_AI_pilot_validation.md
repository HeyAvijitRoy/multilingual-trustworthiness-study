# AI validation of the 25-task pilot after rubric revision 2

- Date: 2026-10-18
- Validator: Claude (AI model, claude-opus-5-5), acting at the study lead's request
- Objects validated: the 25 pilot records in `data/annotations/pilot_*.jsonl` after rubric revision 2 (see `PILOT_AUDIT.md`), against prompt corpus v0.3 and `ANNOTATION_PROTOCOL.md`

> **This is an AI validation, not an independent human review.**
> - The validator also wrote the v0.3 Bengali/BN-CS prompts, the pre-review (`2026-10-18_AI_bengali_prereview.md`) and rubric revision 2, so it is not independent of the work it checks.
> - Under `ANNOTATION_PROTOCOL.md`, a second pass by the same agent does not satisfy independent review.
> - The records' `independent_human_review` and `language_equivalence_review` fields therefore remain `pending`, and every status remains `method-audited`.
> - This log is evidence for, and a starting point for, the human reviewers. It does not replace them.

## Method

Each record was re-read in full against its EN prompt, its v0.3 BN and BN-CS prompts and the protocol. The checks were:
- unit atomicity and the counterexample test;
- duplicate credit between units;
- coverage of the prompt's explicit requirements;
- the omission-consequence test for criticality;
- whether binary and ordinal anchors are complete, meaning no common answer pattern falls between anchors;
- requirement visibility;
- task checks.

Automated checks also passed: `validate_pilot_annotations.py` (structure, hashes, anchors, constraint index) and `validate_prompt_corpus.py` (numeric equivalence and the language guards).

## Verdicts

**Agree** means the reviewer would sign off on the record as written for human calibration.

| Task | Verdict | Basis |
|---|---|---|
| TECH001 | Agree | "Major change" boundary now explicit. |
| TECH004 | Agree | Unchanged; was sound. |
| TECH006 | Agree | RIU-06 anchor gap closed; log overlap and profile/local-data confound resolved; visibility `mixed`. |
| TECH009 | Agree | Inspection, explanation and conditional extension no longer share credit. |
| TECH010 | Agree | Data-preservation safeguard now critical, consistent with TECH006 and TECH009. |
| CYBER001 | Agree | Conditional wording no longer penalizes immediate action; credential-reuse unit added. |
| CYBER004 | Agree | Unchanged; was sound. |
| CYBER006 | Agree | Exception justification and decision log now distinct. |
| CYBER009 | Agree | Pre-enforcement validation vs. progressive rollout, and stop signal vs. rollback mechanism, now distinct; infrequent operations split out. |
| CYBER010 | Agree | Visibility `mixed`; feedback tuning recalibrated as supporting. |
| PROC001 | Agree | Silence rule explicit for both constraints; padding unit removed. |
| PROC004 | Agree | Half anchor no longer rewards timestamp-only selection. |
| PROC006 | Agree | Shared-sheet coordination unit added. |
| PROC009 | Agree | Unchanged; was sound. |
| PROC010 | Agree | Label and effective date separated; archive ladder complete; notification added; access overlap removed. |
| DEC001 | Agree | Invented-deadline rule moved to the unsupported-content check. |
| DEC004 | Agree | Unchanged; was sound. |
| DEC006 | Agree | Duplicate exception credit removed; silence rule explicit; aging criticality justified. |
| DEC009 | Agree | Rule vs. evidence boundary explicit; visibility `mixed`. |
| DEC010 | Agree | Visibility `mixed`. |
| SYN004 | Agree | Unchanged; was sound. |
| SYN008 | Agree | Outcome/explanation separation now scored as a task check. |
| SYN009 | Agree | RIU-04 rationale corrected. |
| SYN091 | Agree | Food and walk-in rules recalibrated as supporting; Bengali sentence segmentation defined. |
| SYN100 | Agree | Short-observation-period reason now required; RIU-09/19 and RIU-13/14 boundaries explicit; retention reading neutral. |

**Language equivalence** of the 25 pilot prompts across EN, BN and BN-CS: consistent under `LANGUAGE_GUIDE.md` and the automated checks. This is a self-check by the author of the v0.3 text, not an independent equivalence review.

## Judgment calls for the human reviewers

These are defensible either way and should be decided by humans, not by this validator:

1. **SYN100 RIU-05 and RIU-18 (critical).** The response-rate change and future satisfaction may be supporting rather than critical; they are kept critical because the prompt says "without dropping caveats" and asks what "remains unknown".
2. **SYN100 RIU-14.** The full anchor now requires both stated reasons. An answer that limits causation without giving any reason scores 0; confirm this strictness is intended.
3. **DEC006 RIU-02 (critical).** This encodes a fairness norm that rejects automatic executive priority; SLA-based VIP tiers exist in practice.
4. **CYBER001 RIU-08.** Credential reuse was added as supporting; confirm it belongs under "immediate steps".
5. **SYN091 RIU-06.** The English says "remote installation clinic" while the Bengali says রিমোট ইনস্টলেশন সহায়তা সেশন; confirm raters treat these as equivalent.
