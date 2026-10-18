# RIU pilot 0.2 manifest

The 25-task pilot has been internally audited and revised. **Local structural checks pass and all 25 records are human-validated (R1, 2026-10-18); gold freeze remains pending.** See [the audit](PILOT_AUDIT.md), [schema](ANNOTATION_SCHEMA.md), [protocol](ANNOTATION_PROTOCOL.md) and [scaling plan](SCALING_PLAN.md).

| Domain | Tasks |
|---|---|
| Technical troubleshooting | TECH001, TECH004, TECH006, TECH009, TECH010 |
| Cybersecurity and digital safety | CYBER001, CYBER004, CYBER006, CYBER009, CYBER010 |
| Procedural and instructional | PROC001, PROC004, PROC006, PROC009, PROC010 |
| Decision support | DEC001, DEC004, DEC006, DEC009, DEC010 |
| Information synthesis | SYN004, SYN008, SYN009, SYN091, SYN100 |

- 25 tasks; 5/domain; easy, medium and hard represented in every domain.
- 159 RIUs after rubric revision 2: 80 critical (50.3%), 79 supporting.
- 138 binary units; 21 with explicit 0/0.5/1 anchors.
- AI validation after revision 2: all 25 records agreed ([log](review_logs/2026-10-18_AI_pilot_validation.md)). Human validation: R1 confirmed all 25 ([log](review_logs/2026-10-18_R1_human_validation.md)). Reviewer packet: [review_logs/pilot_human_review_packet.md](review_logs/pilot_human_review_packet.md).
- All records `human-reviewed` under the single-validator protocol; not yet frozen gold.
- Extended-context items SYN091 and SYN100 retained.
- Prompt corpus v0.3 (2026-10-18): BN and BN-CS rewritten, English unchanged from `74604be07b2246e1d7f063088a35799721290e81`. Pilot RIU text is unchanged; prompt hashes were re-pinned. Corpus v0.3.1 changes only SYN079 (not a pilot task). See [CORPUS_CHANGELOG.md](../prompts/CORPUS_CHANGELOG.md).
- No evaluation model calls or model outputs.
- A deterministic queue prepares all 500 tasks, without inventing annotations for the remaining 475.

The old 130-unit/100-critical result is superseded, not a comparable scoring denominator. The new protocol removes overlaps, splits independently omittable facts, calibrates criticality by omission consequence, and separates format/unsupported-content checks from content coverage. Independent review is necessary to establish agreement and resolve frozen-language concerns; automated validation cannot certify these properties.
