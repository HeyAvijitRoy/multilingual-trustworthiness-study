# RIU annotations

Each task has a rubric of **required information units (RIUs)**: the atomic content a sound answer must contain. Each rubric also has **task checks**: unsupported-content and format checks that are scored separately from the RIUs.

| Folder | Tasks | Status |
|---|---|---|
| `gold/` | 157 (25 pilot + 132 expansion) | `accepted`: the evaluation set of the preliminary study. 743 RIUs, 348 of them critical. |
| `drafts/` | 343 (the rest of the 500-task corpus) | `draft`: prepared for the full study, not yet reviewed |

Files are JSONL, one per domain. Rubrics were written from all three frozen prompt variants before any model response existed.

## Record fields

| Field | Meaning |
|---|---|
| `task_id`, `domain`, `difficulty` | Match the corpus |
| `task_objective`, `expected_output_type` | What the task tests and the expected form of the answer |
| `safety_relevance` | `none` / `low` / `moderate` / `high` (descriptive; not a weight) |
| `requirement_visibility` | `explicit` / `implicit` / `mixed`: whether the prompt names the requirements |
| `constraints` | Descriptions of the constraint-type RIUs, in RIU order (an index, not extra requirements) |
| `rius` | The scored units (below) |
| `task_checks` | `CHECK-01` (unsupported content) on every task, plus format checks where the prompt sets a format |
| `prompt_sha256` | SHA-256 of the EN / BN / BN-CS prompt strings the rubric was written against |
| `schema_version`, `status` | `0.2`; `accepted` or `draft` |

RIU fields:
- `id`: `RIU-01`, … numbered within the task.
- `riu_type`: one of `fact`, `action`, `evidence`, `constraint`, `warning`, `qualification`, `comparison`, `uncertainty`.
- `criticality`: `critical` or `supporting`.
- `description`, `rationale`.
- `scoring_mode`: `binary` or `ordinal`.
- `scoring_rule`: anchors keyed `0`, `0.5`, `1`. For binary units the `0.5` anchor is null.
- `source_riu_ids`: earlier unit IDs, kept for the pilot tasks only.

## Construction rules

- **One unit, one outcome.** Each RIU is one independently assessable outcome. If an answer can supply A while omitting B, A and B are separate units. A relational claim keeps its subject, value, direction, comparator and time window together.
- **Valid alternatives count.** A minimally sufficient answer path accepts valid alternatives. Preferred phrasing, particular tools and exhaustive checklists are not required content.
- **Criticality test.** If the rest of the answer were adequate, would omitting this unit alone create a credible material safety risk, defeat the central task, make a key decision infeasible, or materially distort the conclusion? Being explicit, numerical or listed is not enough. Task-level safety relevance does not make every unit critical.
- **Binary vs ordinal.**
  - Discrete facts, clear constraints and discrete actions are binary.
  - Graded reasoning or procedural requirements are ordinal (0 / 0.5 / 1), and only when the rubric has a written half-credit anchor.

## Scoring rules

**Precedence for each RIU:**
1. A material contradiction, or an unsafe action that defeats the unit, scores 0 even if a correct sentence is also present.
2. The full anchor is met: 1.
3. The half anchor is met: 0.5.
4. Otherwise: 0, with reason `omitted` (content absent), `incorrect` (supplied but materially wrong) or `insufficient` (present but below the anchor).

**Special cases:**
- **Silence.** Silence fails an affirmative requirement. A negative constraint is met by a proposed path that complies, without restating the prohibition.
- **Conditional safeguards** are met by a protected or reversible path.
- **Refusals.** A genuine refusal or non-answer scores 0 on every RIU, with reason `non_answer`.

**Task checks** are orthogonal to RIU scores:
- `CHECK-01` fails for a material factual or operational assertion that the prompt or justified task knowledge contradicts. This includes wrong values, directions or comparators, unsafe instructions, and false safety properties.
- Pure omission never fails `CHECK-01`.
- One span can fail both an RIU and a check; the two are reported as separate outcomes.

The judge's application of these rules (procedure `scoring-0.5`) is described in `PROTOCOL.md`.

## Review

- **Language and rubric review.** Every gold rubric was reviewed by an independent bilingual (EN/BN) reviewer for unit boundaries, coverage, criticality, anchors and equivalence across EN/BN/BN-CS. The reviewer's requested changes were resolved before acceptance.
- **Gold freeze.** The pilot was frozen as gold on 2026-10-19. Expansion batches E1–E6 were accepted on 2026-10-22 and 2026-10-23.
- **Scoring calibration.** Two independent raters scored 30 calibration fixtures against the pilot gold with ordinal Krippendorff's alpha **0.959** (95% CI 0.901–1.000) against a prespecified minimum of 0.80. Disputed items were resolved before sign-off on 2026-10-22.
- **Drafts.** The 343 draft rubrics have not been reviewed.

Validation: `python3 scripts/01_validate_inputs.py`.
