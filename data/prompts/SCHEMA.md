# Prompt Dataset Schema

Each row/item represents one canonical task with three semantically matched language variants.

## Required Fields

```text
task_id
domain
subdomain
difficulty
task_objective
prompt_en
prompt_bn
prompt_bn_en
constraints
required_information_units
critical_information_units
supporting_information_units
expected_output_type
safety_relevance
notes
status
```

## Field Definitions

### `task_id`
Stable identifier, e.g. `CYB-001`.

### `domain`
One of the five primary study domains.

### `subdomain`
More specific task family used to ensure coverage within a domain.

### `difficulty`
`easy`, `medium`, or `hard`.

### `task_objective`
Language-neutral description of what the task is designed to test.

### `prompt_en`
Canonical English prompt.

### `prompt_bn`
Natural Bengali realization of the same task.

### `prompt_bn_en`
Natural Bengali-English code-switched realization of the same task.

### `constraints`
Explicit requirements that must remain equivalent across all language variants.

### `required_information_units`
Structured list of atomic answer requirements.

Each unit should use:

```json
{
  "id": "RIU-1",
  "description": "...",
  "criticality": "critical",
  "scoring_rule": "...",
  "rationale": "..."
}
```

### `critical_information_units`
IDs of required information units whose omission can materially affect correctness, safety, task completion, or decision quality.

### `supporting_information_units`
IDs of useful but nonessential information units.

### `expected_output_type`
Examples: `procedure`, `diagnosis`, `recommendation`, `comparison`, `synthesis`, `explanation`.

### `safety_relevance`
`none`, `low`, `moderate`, or `high`.

### `notes`
Construction or adjudication notes. This field must never contain hidden hints that are unavailable to the evaluated model.

### `status`
Suggested lifecycle values:

- `draft`
- `language-reviewed`
- `scoring-reviewed`
- `frozen`

## Construction Rule

Language variants must not independently evolve. Any semantic change to one variant requires re-checking all three versions and the scoring key.
