# Preliminary 157-task model evaluation protocol

**Protocol ID:** prelim-157-0.1  
**Freeze date:** 2026-10-23  
**Snapshot:** `data/evaluation/PRELIM_157_FREEZE.json`

## Purpose

This is a preliminary evaluation for time-bounded reporting before the final 500-task production-gold study. It does not replace the planned 500-task confirmatory evaluation.

The evaluation uses exactly 157 accepted tasks:
- 25 frozen pilot tasks;
- all 132 accepted E1-E6 expansion-calibration tasks.

Each task is evaluated in three frozen prompt conditions: English (`en`), Bengali (`bn`), and Bengali-English code-switching (`bn_cs`). This yields **471 prompt instances per model**.

## Model panel

The model panel is frozen before any evaluation response is generated:

| Provider | Model ID | Reasoning configuration |
|---|---|---|
| OpenAI | `gpt-6-astra` | standard mode, medium effort |
| Anthropic | `claude-opus-5-5` | adaptive thinking, medium effort |
| Google | `gemini-4-argon` | medium thinking level |

Official model references as checked on 2026-10-23:
- https://developers.openai.com/api/docs/models/gpt-6-astra
- https://platform.claude.com/docs/en/models/opus-5-5/overview
- https://ai.google.dev/gemini-api/docs/models/gemini-4-argon

The exact request configuration is pinned in `PRELIM_157_MODELS.json`.

## Generation design

- One independent generation per task-language-model cell.
- Total planned responses: **1,413**.
- Each request is stateless; no prior conversation is supplied.
- No web search, tools, retrieval, code execution, or external grounding is enabled.
- The frozen prompt text is passed unchanged as the user message.
- Common system instruction: **"Answer the user's request directly."**
- Reasoning intensity is fixed at each provider's medium level.
- Sampling controls such as temperature/top-p/top-k are omitted rather than forcing non-equivalent controls across providers.
- Output limit: 32,768 tokens for every provider.
- Request timeout: 900 seconds.
- Prompt order is deterministically shuffled with seed 20261023 separately for each provider.
- Run index is 1 for every cell.

The output limit is intentionally high relative to the task lengths so response truncation is unlikely to create artificial omission. Any request that reaches its output limit is retained and marked as truncated rather than silently retried with a different configuration.

## Failure and retry policy

A transport/API failure may be retried with the **same** model, prompt and parameters. Retries do not create additional study generations.

- Retry rate-limit, timeout, and transient 5xx failures.
- Use bounded exponential backoff.
- Do not alter the prompt, reasoning level, output limit, system instruction, or provider after a failure.
- Record every attempt and final status.
- A final unresolved API failure is missing data, not a model refusal.
- A successful model response that refuses or gives no substantive answer remains a model outcome and is scored under protocol 0.3.

## Raw-output preservation

Each successful or failed request is recorded as one JSONL row containing at least:

- snapshot ID;
- task ID;
- domain and difficulty;
- language condition;
- provider and requested model ID;
- model ID/version returned by the provider where available;
- run index;
- prompt SHA-256;
- request parameters;
- UTC generation timestamp;
- latency;
- provider request/response identifier where available;
- usage/token metadata where available;
- finish/stop status;
- raw visible response text;
- error metadata when applicable.

Raw response files are append-only inputs to scoring. Derived scores and analyses are stored separately.

## Integrity boundary

The 157-task membership, prompt corpus, accepted annotations, model panel, generation settings, scoring definitions, and preliminary analysis plan are frozen before examining evaluation responses.

The remaining 343 production tasks are outside this preliminary analysis and remain available for the later full 500-task study. No preliminary model outcome may be used to rewrite frozen prompts, accepted 157-task RIUs, criticality labels, or scoring anchors.

## Reporting language

Any abstract or manuscript using these results must identify the result as a **preliminary 157-task evaluation** (471 matched prompt instances per model) rather than the final 500-task evaluation.
