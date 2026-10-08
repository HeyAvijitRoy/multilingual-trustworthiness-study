# Annotation Schema — RIU Pilot v0.1

This directory stores evaluation metadata separately from the frozen prompt corpus.

## Pilot scope

- 25 tasks total
- 5 tasks from each of the five study domains
- easy / medium / hard coverage
- includes extended-context synthesis tasks
- no model outputs are used to construct these annotations

## Record schema

Each JSONL record contains:

- `task_id`
- `domain`
- `difficulty`
- `task_objective`
- `expected_output_type`
- `safety_relevance`
- `requirement_visibility`
- `constraints`
- `rius`
- `notes`
- `status`

### RIU object

Each required information unit contains:

- `id` — sequential within a task, e.g. `RIU-01`
- `riu_type` — one of `fact`, `action`, `evidence`, `constraint`, `warning`, `qualification`, `comparison`, `uncertainty`
- `criticality` — `critical` or `supporting`
- `description` — language-neutral atomic requirement
- `scoring_rule` — explicit criterion for deciding whether a response satisfies the RIU
- `rationale` — why the unit matters to task correctness, safety, actionability, or interpretation

## Requirement visibility

- `explicit` — principal scoring requirements are named in the prompt.
- `implicit` — important scoring requirements must be independently surfaced.
- `mixed` — some requirements are named while others must be inferred.

## Safety relevance

- `none`
- `low`
- `moderate`
- `high`

## Annotation rules

1. RIUs describe answer requirements, not ideal prose.
2. RIUs must remain valid for EN, BN, and BN-CS variants of the same task.
3. A critical RIU is one whose omission can materially affect correctness, safety, task completion, or decision quality.
4. Supporting RIUs improve completeness but are not necessary for core task success.
5. Scoring rules should permit paraphrases and equivalent reasoning.
6. Do not require facts not supported by the prompt or standard task knowledge needed to answer it.
7. Do not inspect model outputs while constructing or revising gold RIUs.
8. Prompt text remains immutable during annotation.
9. Extended-context items may legitimately contain more RIUs than ordinary tasks.
10. Pilot annotations remain provisional until human/adjudication review; they are not yet the frozen gold set.

## Pilot status values

- `pilot-internal-reviewed` — internally checked for atomicity, scoreability, and alignment with frozen task semantics.
- `human-reviewed` — reviewed/adjudicated by an additional human annotator.
- `frozen` — approved for final model scoring.

## Pilot files

- `pilot_technical.jsonl`
- `pilot_cybersecurity.jsonl`
- `pilot_procedural.jsonl`
- `pilot_decision_support.jsonl`
- `pilot_information_synthesis.jsonl`

The full 500-task annotation set should use the same structure after the pilot is accepted.
