# Gold sign-off: 25-task RIU pilot

- Object: `data/annotations/pilot_*.jsonl`, schema 0.2, rubric revision 2, against corpus v0.3.1
- Protocol: `ANNOTATION_PROTOCOL.md` 0.2 (single-validator amendment, 2026-10-18), accepted as the pilot gold protocol
- Gold version: **pilot-gold-0.2**, hash-pinned in `data/annotations/PILOT_GOLD_FREEZE.json`
- Sign-off date: 2026-10-19
- Recorded by: Claude (AI), from the sign-off sheet completed by the study lead. Claude prepared the gate checklist below and made no approval decision.

## Sign-off

| Role | Decision | Date | Recorded as |
|---|---|---|---|
| Human validator (R1) | Approved as gold | 2026-10-19 | "approved (10/19/2026) by R1" |
| Study lead (AR) | Approved as gold | 2026-10-19 | "Approved, AR - 10/19/2026" |

The study lead decided that subdomain expansion is **not needed** before this pilot freeze. Expansion calibration still gates production annotation (`SCALING_PLAN.md`); it does not gate the pilot gold.

## Gate checklist (`ANNOTATION_PROTOCOL.md`, "Human calibration and freeze gate")

| Requirement | State | Evidence |
|---|---|---|
| Human validator review of boundaries, coverage, criticality, anchors, EN/BN/BN-CS equivalence | Met | `2026-10-18_R1_human_validation.md`; all 25 `review` fields cite it |
| Validator ID, date, decisions, changes recorded | Met | R1, 2026-10-18, no changes requested |
| Unresolved safety / equivalence / critical-unit disputes | None | R1 log; the five AI judgment calls were accepted by R1 |
| Frozen-language flags (TECH006, DEC006, CYBER009, SYN100) | Closed | Corpus v0.3 repair, `CORPUS_CHANGELOG.md` |
| Automated checks (2026-10-19) | Pass | Corpus validator; pilot validator (25 tasks, 159 RIUs, 80 critical, 138 binary / 21 ordinal); unit tests; queue `--check` |
| Prompt bytes pinned | Pass | `PROMPT_FREEZE.json`, corpus v0.3.1 |
| Accepted protocol versioned | Met | Protocol 0.2 |
| Subdomain expansion before freeze | Not required for the pilot | Study lead decision above |
| Final annotations hashed | Met | Hashes below; enforced by `validate_pilot_annotations.py` |
| Explicit human sign-off | Met | Sign-off table above |

## Change applied at freeze

The only edit was setting `status` from `human-reviewed` to `frozen` on all 25 records. No unit, anchor, criticality or prompt text changed.

Hashes of the frozen files (SHA-256):

```
6f16fa8c599cdd23fa0b0bad01782dcc142b319ba6d37874d45840c1af60a39b  pilot_technical.jsonl
43d7fd4a7d4b9f08826e445c1e403ecd94986f6db22549fe6db368f3ec9d8365  pilot_cybersecurity.jsonl
841e8f7cff2a8d41b6e9e10c4a3cca8f47792a518ae8febbfe8b517b988b813a  pilot_procedural.jsonl
b4b98325a17005fadcb65308da792ce428c16a99982278c32c352580f3dc2714  pilot_decision_support.jsonl
b2246db64d271c94b5354eb295683749f7b402ed0a68c4e80d8a6c68583827b5  pilot_information_synthesis.jsonl
```

Hashes of the same files before the status edit (commit `5c8c220`), as reviewed:

```
51b4efa436b9c229d46a44deb5fbb103e4e63c4dfee5752a011f0e5c317989a0  pilot_technical.jsonl
8f8f44924eb30f537b473242a387db650fbcd665bc1410808ed510e61c0e505f  pilot_cybersecurity.jsonl
8a8cdba5fe76c3b65a4fbc0c15f42f64ed9dc397f5065a67f42aa0ba8eee963e  pilot_procedural.jsonl
35baf6ff18982633a3786f50e39eb048040cd031bdb3769e8632e52b47d3bd29  pilot_decision_support.jsonl
af63b6a884cfff8913813ba1ec42a8183db3eb480fd345bf3f23352e6bd8f7b2  pilot_information_synthesis.jsonl
```

Any later change to these records requires a new gold version and consistent rescoring (`ANNOTATION_PROTOCOL.md`).

## Limitations to carry into reporting

- Single human validator: no inter-annotator agreement exists for the gold itself.
- The pilot is purposive (each domain covers one subdomain); it does not validate the method across all 500 tasks.
- Human-authored calibration fixtures and the study lead's agreement threshold are still outstanding. Both are required before model runs.
