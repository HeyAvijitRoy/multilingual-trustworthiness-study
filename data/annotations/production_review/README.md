# Production draft preparation — 2026-10-23

These artifacts prepare annotation review. They do not freeze a production protocol, certify semantic equivalence, accept annotations, or authorize study evaluation. All new records are AI-produced `draft` annotations, with `agent-internal` method review and both independent-human and language-equivalence review fields `pending`.

The separate [`../PRODUCTION_BATCHES_v0.1.json`](../PRODUCTION_BATCHES_v0.1.json) assigns the 343 remaining task IDs into 14 outcome-independent batches: seven of 25 and seven of 24. The first two batches span all five domains and all three difficulties. The historical `SCALING_QUEUE.json`, `EXPANSION_BATCHES.json`, 25 pilot records and 132 accepted expansion records remain unchanged. No response, judge score or preliminary model outcome was read to select membership or draft these annotations. No generation/judge/provider call was made by this workflow.

## Current state

| Batch | Draft tasks | Machine-validated tasks | RIUs | Critical | Supporting | Binary | Ordinal | Ordinary sample | Mandatory unit reviews | Human reviewed | Approved |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| P01 | 25 | 25 | 100 | 39 | 61 | 96 | 4 | 18 | 86 | 0 | 0 |
| P02 | 25 | 25 | 109 | 45 | 64 | 106 | 3 | 18 | 87 | 0 | 0 |
| P03 | 25 | 25 | 129 | 57 | 72 | 122 | 7 | 22 | 89 | 0 | 0 |
| P04 | 25 | 25 | 125 | 51 | 74 | 119 | 6 | 22 | 77 | 0 | 0 |
| P05 | 25 | 25 | 133 | 59 | 74 | 128 | 5 | 21 | 82 | 0 | 0 |
| P06 | 25 | 25 | 124 | 50 | 74 | 116 | 8 | 21 | 72 | 0 | 0 |
| P07 | 25 | 25 | 132 | 56 | 76 | 125 | 7 | 21 | 78 | 0 | 0 |
| P08 | 24 | 24 | 122 | 54 | 68 | 118 | 4 | 21 | 75 | 0 | 0 |
| P09 | 24 | 24 | 119 | 55 | 64 | 116 | 3 | 21 | 76 | 0 | 0 |
| P10 | 24 | 24 | 113 | 52 | 61 | 112 | 1 | 20 | 72 | 0 | 0 |
| P11 | 24 | 24 | 118 | 55 | 63 | 111 | 7 | 20 | 75 | 0 | 0 |
| P12 | 24 | 24 | 111 | 50 | 61 | 109 | 2 | 19 | 69 | 0 | 0 |
| P13 | 24 | 24 | 115 | 51 | 64 | 110 | 5 | 20 | 71 | 0 | 0 |
| P14 | 24 | 24 | 109 | 47 | 62 | 103 | 6 | 20 | 67 | 0 | 0 |
| Total | 343 | 343 | 1659 | 721 | 938 | 1591 | 68 | 284 | 1076 | 0 | 0 |

**Updated 2026-10-24:** All 343 production tasks (P01–P14) now have AI-drafted, machine-validated records and v0.3 review packets. The P03–P14 drafts were added on 2026-10-24 without reading any study response, judge score or model outcome. Every record remains `draft`, with `agent-internal` method review and pending independent human and language-equivalence review. **No production annotation is accepted or promoted to gold.** The historical accepted count remains 157, and their records are unchanged. Together, the 157 accepted and 343 drafted tasks cover the 500-task corpus exactly, with no overlap. No `full/` annotations or production-gold freeze have been assembled.

P03–P14 follow conventions already present in the accepted records:
- technical differential-diagnosis tasks have supporting cause-area checks plus one critical ordinal result-interpretation unit;
- extraction tasks treat each explicitly listed item as critical;
- prompt-named decision factors are supporting, with one critical unit for combining them;
- the extended-context tasks (SYN092–SYN099) receive fine-grained relational units.

Task-level language-equivalence observations, such as DEC039's BN versus BN-CS "repeatedly" versus "progressively failing", are recorded in the ambiguity files for the reviewer.

All 1,029 frozen prompt strings for P01–P14 (EN, BN, BN-CS) were inspected during drafting. Each record contains its three prompt hashes, task-specific units, omission-consequence rationales, full/zero anchors, concrete half anchors where applicable and language/boundary notes. This is an AI interpretation, not a completed independent equivalence review.

Current review snapshots are:

- [`P01_packet_v0.3.md`](P01_packet_v0.3.md) and [`P01_packet_v0.3.json`](P01_packet_v0.3.json).
- [`P02_packet_v0.3.md`](P02_packet_v0.3.md) and [`P02_packet_v0.3.json`](P02_packet_v0.3.json).
- Task-specific issue inputs: [`P01_ambiguities.json`](P01_ambiguities.json), [`P02_ambiguities.json`](P02_ambiguities.json).

Earlier v0.1/v0.2 packet files are retained as superseded, unaccepted AI construction snapshots. They do not match the current draft hashes and must not be used for acceptance. Their preservation records revisions rather than completed human review.

## Review selection and escalation

The algorithm was specified in the production plan before drafting: within each batch, stratify supporting RIUs by domain, difficulty and scoring mode. Select `ceil(n/5)` per stratum by SHA-256 rank of `salt|batch_id|task_id|riu_id`, with the public fixed salt in the plan. This produces 18 ordinary units in each batch (29.5% of P01 supporting units; 28.1% of P02), independently of model outcomes and ambiguity flags. The JSON packets list exact selections and all stratum denominators.

Every critical unit and every explicitly identified unit-level ambiguity/boundary item is mandatory in addition to that sample. Task-level ambiguity questions and bilingual equivalence/full-prompt coverage require review for every task, including questions with no single RIU ID. Ordinary sampling does not excuse missing coverage review. Checklists intentionally include the unsampled units too.

A systematic rule error triggers review of **every affected unit**, including ordinary units outside the sample and affected units in other drafted batches. Record the rule, scope, exact task/RIU IDs, revised judgments and resolution; revalidate and issue a new review snapshot. Unresolved critical, safety or equivalence issues block approval. Existing frozen material needs separate versioning and authorized review if affected; this workflow never edits it.

The reviewer should work from a copy/new review log and record actual identity, EN/BN competence, date, reviewed hashes, initial and final judgments, disagreement and resolution. No blank identity or decision field may be interpreted as acceptance. Formal validator and study-lead sign-off, and production protocol approval, remain necessary before promotion/gold assembly.

## Second-pass construction audit

The draft-only audit identified a broad/narrow overlap between CYBER080 compensating protection and isolation. The current annotation expresses one operational protection outcome that includes its isolation boundary, plus separate monitoring and migration outcomes; it does not demand an additional unrelated control to earn credit.

The audit also reviewed all ten drafted technical tasks for redundant generic diagnostic-conclusion units. It removed the broad final unit from TECH050, TECH096, TECH090, TECH037, TECH067 and TECH097. The specific cause-area checks already express the diagnostic work; a proven root cause or extra generic synthesis paragraph is not imposed. The requested ordered sequence for TECH067/TECH097 is a separate format check. Tasks are permitted to have no critical RIUs, with critical outcomes NA under the protocol; criticality is not forced by quotas.

These changes reduced the initial 216 RIUs/90 critical units to the current 209/84. The v0.1 packets preserve the initial drafts. The v0.2 snapshots record the content refinement, and v0.3 reconciles the remaining CYBER080/TECH096 boundary wording. None of these snapshots constitutes independent acceptance or a change to frozen definitions.

## Reproducible checks

From the repository root:

```bash
python3 scripts/prepare_production_batches.py --check --packets
python3 scripts/validate_pilot_annotations.py --scope batch --annotation-dir data/annotations/production/P01
python3 scripts/validate_pilot_annotations.py --scope batch --annotation-dir data/annotations/production/P02
python3 -m unittest discover -s scripts -p test_production_batches.py -v
python3 scripts/prepare_scaling_queue.py --check
python3 scripts/prepare_expansion_batches.py --check
python3 scripts/freeze_prompt_corpus.py --check
```

All passed on the current drafts; the dedicated suite contains seven tests. Schema/hash validation establishes structural integrity, not rubric correctness or human acceptance. The tests cover unique/disjoint reserved membership, <=25 tasks per batch, assignment invariance to source row order, missing/duplicate rejection, prespecified ordinary sampling, mandatory review coverage, pending-status enforcement, and read-only/no-overwrite evidence handling.

`prepare_production_batches.py` generates membership and review packets only; it never automatically creates annotation content or accepts gold. The plan and existing packets are not overwritten if bytes differ, including human edits. `--check` writes nothing. After changing a draft, retain the old packet and use a new version, for example `--packets --packet-revision 0.4`; pass that revision to `--check` too. If the underlying source membership changes, create an explicit new plan version rather than replacing this prospectively assigned plan. Annotation directories contain only domain-specific JSONL files.
