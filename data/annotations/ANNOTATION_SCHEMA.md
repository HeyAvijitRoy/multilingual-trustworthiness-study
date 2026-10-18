# RIU annotation schema 0.2

This version replaces 0.1. Annotations are separate from the prompt corpus, now at version 0.3 (Bengali and BN-CS rewritten; English byte-identical to v0.2 at commit `74604be07b2246e1d7f063088a35799721290e81`). `PROMPT_FREEZE.json` pins every file under `data/prompts/`; record hashes additionally pin each language string. Neither file hashes nor a schema PASS certify language equivalence.

## Record fields

| Field | Meaning |
|---|---|
| `schema_version` | `0.2` |
| `task_id`, `domain`, `difficulty` | Must match the frozen corpus |
| `task_objective`, `expected_output_type` | Nonempty description of the task and response form |
| `safety_relevance` | `none`, `low`, `moderate`, `high`; not a criticality multiplier |
| `requirement_visibility` | `explicit`, `implicit`, `mixed`; descriptive, not a scoring weight |
| `constraints` | Exact descriptions of constraint-type RIUs, in RIU order; an index, not additional scored requirements |
| `rius` | Nonempty list; no minimum of three and no forced critical unit |
| `task_checks` | Separate unsupported-content and applicable format checks |
| `prompt_sha256` | SHA-256 of UTF-8 `prompt_en`, `prompt_bn`, `prompt_bn_cs`, keyed `en`, `bn`, `bn_cs` |
| `review` | Method-review provenance plus independent-human and language-equivalence review-log references, or `pending` |
| `status` | `draft`, `method-audited`, `human-reviewed`, `frozen` |
| `notes` | Provenance and limitations |

`method-audited` means internal rubric review, not independent human validation. Human-reviewed/frozen records require both human and bilingual review references. The validator verifies the references are supplied; a reviewer must verify their authenticity and contents. Freeze additionally requires the sign-off process in `ANNOTATION_PROTOCOL.md`.

## RIU fields

| Field | Meaning |
|---|---|
| `id` | Sequential within task, `RIU-01`, etc. |
| `source_riu_ids` | Corresponding 0.1 unit IDs for migration; empty for newly annotated tasks |
| `riu_type` | `fact`, `action`, `evidence`, `constraint`, `warning`, `qualification`, `comparison`, `uncertainty` |
| `criticality` | `critical` or `supporting`, using the omission-consequence test |
| `description` | One independently assessable proposition or operational requirement |
| `rationale` | Concrete consequence of omission, or supporting contribution |
| `scoring_mode` | `binary` or `ordinal` |
| `scoring_rule` | Object with exactly `0`, `0.5`, `1`; `1` equals the description; binary `0.5` is JSON null |

A relational proposition may retain its subject, value, direction, comparator and time window together. Do not split a number from its referent or treat every example in an alternative list as mandatory. Independently satisfiable outcomes, such as password change and session revocation, are separate units. See the protocol for safeguards against fragmentation and overlap.

`task_checks` entries contain sequential `id`, `kind` (`unsupported_content` or `format`), and a nonempty `rule`. They do not increase the RIU denominator. Recording an error can coexist with a failed RIU, but it is never subtracted a second time from coverage.

## Migration

0.1 IDs are local to the old version; never join old scores to 0.2 by RIU ID alone. Use `(schema_version, task_id, riu_id)`. `source_riu_ids` records splits and merges. SYN091's old RIU-09 is replaced by separate task checks. Re-score all responses if an annotation version changes; no responses exist for this revision.

## Validation

From the repository root:

```sh
python3 scripts/validate_prompt_corpus.py
python3 scripts/validate_pilot_annotations.py
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/prepare_scaling_queue.py --check
```

Future annotation directories must contain only annotation JSONL files:

```sh
python3 scripts/validate_pilot_annotations.py --scope batch --annotation-dir data/annotations/full
python3 scripts/validate_pilot_annotations.py --scope full --annotation-dir data/annotations/full
```

Batch mode checks every supplied record and forbids duplicate task IDs. Full mode additionally requires exact coverage of all 500 frozen tasks. Both verify frozen prompt bytes. Neither command runs models or edits prompts.
