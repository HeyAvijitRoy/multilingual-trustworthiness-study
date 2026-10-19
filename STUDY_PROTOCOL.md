# Study Protocol

## Working Aim

The study measures whether semantically equivalent prompts produce systematically different trustworthiness outcomes across English, Bengali and Bengali-English code-switched conditions.

The scientific contribution is the **empirical analysis of language-conditioned trustworthiness failure**. The prompt corpus is the controlled experimental instrument used to measure that failure.

## Primary Research Questions

1. Does response completeness differ across the three language conditions?
2. Are trustworthiness-critical information units omitted more often in Bengali than in English?
3. Does natural Bengali-English code-switching recover information that is omitted in predominantly Bengali responses?
4. Do language-conditioned differences vary by task domain and difficulty?
5. Are observed differences consistent across model families?
6. Are language-conditioned failures stable across repeated generations?
7. When omissions occur, do they materially affect correctness, safety, actionability, or decision quality?

## Experimental Unit

Each evaluation item is one canonical task represented by three matched prompt variants:

- `en` — English
- `bn` — natural contemporary Bengali
- `bn_cs` — natural Bengali-English code-switching with Bengali as the matrix language

The three variants share:

- task objective
- factual context
- constraints
- required output elements
- difficulty
- safety relevance
- required information units

## Corpus Size

Target: **500 frozen evaluation tasks / 1,500 prompt instances**.

| Domain | Tasks |
|---|---:|
| Technical troubleshooting | 100 |
| Cybersecurity and digital safety | 100 |
| Procedural and instructional | 100 |
| Decision support and constraint-heavy tasks | 100 |
| Information synthesis and extended-context tasks | 100 |
| **Total** | **500** |

## Difficulty Distribution

The frozen corpus uses an exact per-domain allocation:

- Easy: 25 tasks
- Medium: 50 tasks
- Hard: 25 tasks

Across five domains this produces:

- Easy: 125
- Medium: 250
- Hard: 125

Difficulty is defined by task structure rather than topic prestige.

### Easy

One primary objective with limited interaction among constraints or evidence.

### Medium

Integration of multiple factors, steps, constraints, comparisons or evidence elements.

### Hard

Reconciliation of several interacting constraints, dependencies, uncertainties, trade-offs or evidence sources, with important caveats retained.

## Prompt Construction Principles

### English

The English prompt is the canonical semantic specification.

### Bengali

The Bengali condition uses natural contemporary Bengali rather than rigid word-for-word translation.

Technical vocabulary follows realistic Bengali professional usage. Established terms such as `driver`, `cache`, `deployment`, `credential`, `CI`, `API`, and similar concepts may remain transliterated or in English when forced Bengali translation would sound artificial, obscure the intended concept, or introduce semantic drift.

Bengali predominates in the condition's syntax and discourse.

### Bengali-English Code-Switching

The BN-CS condition models plausible Bengali technical/professional discourse rather than an English prompt with Bengali framing.

Language design:

> **Bengali remains the matrix language; English enters primarily through lexical, interface, software, professional, and domain terminology.**

The code-switched condition preserves semantic equivalence without:

- additional hints;
- omitted constraints;
- reduced task difficulty;
- changed factual context;
- independent divergence from the Bengali or English specification.

The v0.2 construction regenerated BN-CS from the Bengali prompt using a controlled domain lexicon. Review found that substitution produced grammatical corruption and left key domain terms as Bengali calques, so corpus v0.3 replaces it: BN and BN-CS are hand-written in parallel, sentence by sentence, under [LANGUAGE_GUIDE.md](data/prompts/LANGUAGE_GUIDE.md). English prompts are unchanged from v0.2. The version history is recorded in [CORPUS_CHANGELOG.md](data/prompts/CORPUS_CHANGELOG.md).

## Extended-Context Subset

`SYN091`–`SYN100` form the `extended_context` subset.

These prompts are intentionally much longer than ordinary corpus items and contain multiple facts, dependencies, caveats, timing constraints, subgroup findings, or unknowns. Their purpose is to test **information retention and omission under denser context**, not merely general summarization ability.

The extended-context subset is characterized by:

- substantially greater length than ordinary items;
- multiple independently scoreable facts;
- at least one caveat, dependency, uncertainty or negative constraint;
- self-contained information;
- semantic matching across language conditions.

## Required Information Units

After prompt-language QA, each frozen task will receive atomic expected-answer elements. Every required information unit (RIU) will include:

- identifier
- description
- criticality
- rationale
- scoring rule

Criticality levels:

- `critical` — omission alone, with the rest of the answer adequate, creates a credible material safety risk, defeats the central task, makes a key decision infeasible, or materially distorts the conclusion;
- `supporting` — useful but not necessary for successful completion.

## Requirement Visibility

During annotation, each task will also be labeled:

- `explicit` — the prompt directly names the principal dimensions to address;
- `implicit` — important requirements are not directly named in the prompt and depend on the model surfacing them;
- `mixed` — some requirements are visible while others depend on inference or retrieval.

This variable is recorded during annotation rather than added to the source prompt CSVs. It can be used as a secondary factor when interpreting omission rates.

## Outcome Measures

Primary measures:

- required-information-unit coverage
- critical omission rate
- complete-task success
- instruction adherence
- factual/correctness error rate
- actionability

Secondary measures:

- refusal or non-answer rate
- unsupported-content rate
- verbosity/compression differences
- consistency across repeated runs
- differences by requirement visibility

## Evaluation Design

The evaluation design prioritizes structured scoring. RIU scores follow deterministic checks or explicit rules where possible, with blinded reviewer assessment of ambiguous cases. Model-based judging is a supplemental measure validated against reviewer labels.

## Statistical Plan

The analysis preserves the pairing of language variants within each task.

Candidate analyses include:

- McNemar tests for paired binary outcomes
- Wilcoxon signed-rank tests for paired ordinal or non-normal measures
- mixed-effects logistic or ordinal regression
- interaction analysis for language × difficulty, language × domain, and language × model

A representative model for a binary critical-omission outcome is:

```text
CriticalOmission ~ Language + Model + Difficulty + Domain
                 + Language:Difficulty
                 + Language:Domain
                 + (1 | TaskID)
```

Final statistical choices will be determined after inspecting outcome distributions and model assumptions.

## Corpus QA and Freeze Policy

Corpus freeze depends on automated checks and reviewer assessment covering:

- 500 unique IDs
- 100 tasks per domain
- 25/50/25 difficulty allocation per domain
- no missing prompt variants
- no exact duplicate prompts
- natural Bengali terminology
- Bengali-matrix BN-CS
- semantic equivalence across EN / BN / BN-CS
- extended-context length and constraint preservation

The repository includes:

```text
scripts/revise_corpus_v02.py
scripts/validate_prompt_corpus.py
```

The final evaluation set is frozen **before full model evaluation**. Corpus v0.3 passed automated QA and was validated by R1 and approved and frozen by the study lead on 2026-10-18 (`data/annotations/review_logs/2026-10-18_R1_human_validation.md`). Corpus v0.3.1 (one English clarification, SYN079, R1-confirmed) is the frozen evaluation set, pinned in `data/annotations/PROMPT_FREEZE.json`.

Development items used to debug scoring logic, prompt construction or experiment code remain distinct from the inferential test set after evaluation begins.

## Reproducibility

Planned generation records contain at least:

- task ID
- language condition
- model/provider
- model version where available
- generation timestamp
- generation parameters
- prompt text or immutable prompt hash
- run index
- raw output

The analysis design uses immutable raw outputs and stores derived results separately.

## Annotation protocol amendment (0.2; before evaluation)

[ANNOTATION_PROTOCOL.md](data/annotations/ANNOTATION_PROTOCOL.md) governs RIU construction, criticality and scoring and supersedes earlier broad RIU definitions above. Explicit mention in a prompt does not automatically make a unit critical. Supporting units still count toward coverage and strict complete-task success.

Discrete facts/actions remain binary; only requirements with written partial anchors allow 0/0.5/1. Planned reporting includes strict binary sensitivity alongside rubric coverage. Literal omission, incorrectness and partial fulfillment are distinct outcomes; format and unsupported-content checks remain outside RIU denominators. Overall results average task-level scores within domains, then domains equally, preserving paired tasks and accounting for repeated runs. Scoring and inferential choices are independent of observed language effects. Final estimands, contrasts, agreement thresholds and analysis choices are recorded before model outcomes are inspected; outcome-based diagnostics do not change the primary hypothesis.

The 25-task pilot was validated by the study's single validator (R1, 2026-10-18) after internal revision and signed off as frozen gold `pilot-gold-0.2` by R1 and the study lead on 2026-10-19 (`data/annotations/review_logs/2026-10-19_pilot_gold_signoff.md`). Review flags and subdomain sampling limitations are recorded in [PILOT_AUDIT.md](data/annotations/PILOT_AUDIT.md). No evaluation generations have been performed. Model evaluation follows adjudicated gold freeze, with byte-pinned prompts unchanged during annotation. Corpus v0.3 (2026-10-18) is a versioned, study-lead-authorized language repair made before any model run; further prompt changes require another versioned release, not edits during annotation.
