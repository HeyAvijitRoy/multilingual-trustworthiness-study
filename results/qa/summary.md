# QA sample study

60 study responses (352 items) were rated by a reviewer against the rubrics, separately from the judge, and compared with the initial judge scores. 45 responses are one per model x language x domain; 15 are responses where the judge scored a critical item below 1.

Agreement is measured before score review. Corrections recorded after examining disagreements are used in results/analysis/; they do not retroactively improve the independent QA agreement.

## Agreement

| Measure | QA vs judge | 95% CI | Held-out threshold | |
|---|---:|---|---:|---|
| Ordinal alpha, RIUs (n=290) | 0.843 | 0.760–0.919 | ≥ 0.8 | met |
| Critical RIU exact (n=140) | 0.979 | 0.949–1.000 | ≥ 0.9 | met |
| CHECK-01 exact (n=60) | 0.933 | 0.867–0.983 | 1.0 | not met |
| All task checks exact (n=62) | 0.935 | 0.867–0.984 | 1.0 | not met |
| Format checks exact (n=2) | 1.000 | — | — | — |

Exact agreement on all RIUs: 0.955.

| Subset | RIUs | Alpha | RIU exact | Critical exact | CHECK-01 exact |
|---|---:|---:|---:|---:|---:|
| main | 206 | 0.859 | 0.971 | 0.990 | 0.956 |
| extra | 84 | 0.794 | 0.917 | 0.947 | 0.867 |
| sol | 69 | n/a | 1.000 | 1.000 | 1.000 |
| qwen | 84 | 0.776 | 0.940 | 0.977 | 0.947 |
| gemma | 137 | 0.848 | 0.942 | 0.967 | 0.885 |
| en | 101 | 0.873 | 0.970 | 0.963 | 0.850 |
| bn | 93 | 0.770 | 0.925 | 0.976 | 0.950 |
| bn_cs | 96 | 0.896 | 0.969 | 1.000 | 1.000 |

Sol has no disagreements, so its alpha is undefined.

## Direction

RIU disagreements: the QA rating is higher on 11 and lower on 2. Mean RIU score is 0.845 (QA) against 0.814 (judge).

| Critical coverage in the sampled responses | QA | Judge |
|---|---:|---:|
| en | 0.863 | 0.789 |
| bn | 0.708 | 0.653 |
| bn_cs | 0.809 | 0.809 |
| BN − EN | -0.155 | -0.137 |

## Disagreements (17 of 352 items, 4.8%)

The initial review classified 3 items as judge errors (0.9% of sampled items), 7 as judgement calls and 7 as items where the QA rating was more lenient than the anchor as written (mostly anchors with several required parts). These are recorded review dispositions, not a population estimate of judge error. For CHECK-01, a few task rubrics use the word unsupported while the scoring standard requires a contradiction, so those dispositions depend on which reading is applied.

The recorded dispositions do not require changing the sampled omission counts. The QA ratings record scores and notes, but not independent omission/non-answer reason codes; it therefore does not establish that the primary omission estimate is free of classification error.

| Item | Model, language | QA | Judge | Disposition | Note |
|---|---|---:|---:|---|---|
| QA-01 RIU-04 | qwen, bn | 0 | 1 | judgement call | Exposure versus exploitation distinction present but brief. |
| QA-03 RIU-04 | gemma, bn_cs | 1 | 0 | judge error | Read "tickets in the last two weeks" too literally against "launched two weeks ago". |
| QA-07 CHECK-01 | qwen, en | 0 | 1 | judgement call | Box named as end-to-end encrypted; inaccurate, materiality debatable. |
| QA-10 RIU-05 | gemma, bn_cs | 1 | 0 | QA rating more lenient than the anchor | Checks screen use but never compares travel with ordinary use. |
| QA-13 RIU-05 (critical) | qwen, en | 1 | 0 | judgement call | Flags scope/deadline negotiation but asserts the adjusted scope meets the deadline. |
| QA-14 RIU-06 (critical) | gemma, en | 1 | 0 | QA rating more lenient than the anchor | Choice rule uses strategic value and complexity only; two paths share identical conditions. |
| QA-14 CHECK-01 | gemma, en | 1 | 0 | judge error | Failed an unsupported 30%-budget assumption; the standard requires contradiction. |
| QA-15 RIU-03 | qwen, bn | 1 | 0 | QA rating more lenient than the anchor | Frames partial accommodation as integration; no test of reduced-scope acceptability. |
| QA-15 RIU-05 | qwen, bn | 1 | 0 | QA rating more lenient than the anchor | Evaluates a full restart, not restarting the affected part. |
| QA-29 RIU-02 | qwen, bn_cs | 1 | 0 | QA rating more lenient than the anchor | Gives reset commands; no local-network condition is checked. |
| QA-31 RIU-01 | gemma, bn | 1 | 0 | QA rating more lenient than the anchor | Arrival times shared; luggage needs and budget limits not collected. |
| QA-35 CHECK-01 | gemma, en | 0 | 1 | judge error | Passed an invented "100% uptime" figure because it is unsupported, not contradicted. |
| QA-43 RIU-02 | gemma, bn | 1 | 0 | judgement call | Self-contradiction on announcing layoffs in a meeting, applied to a group-meeting anchor. |
| QA-43 RIU-05 (critical) | gemma, bn | 1 | 0 | judgement call | Same contradiction applied to the conditional-choice anchor. |
| QA-58 RIU-04 | gemma, bn | 0 | 1 | judgement call | Lock-file hash comparison present; mismatch investigation thin. |
| QA-58 CHECK-01 | gemma, bn | 0 | 1 | judgement call | Hash mismatch presented as proof of tampering; materiality debatable. |
| QA-59 RIU-02 | gemma, en | 1 | 0 | QA rating more lenient than the anchor | Covers use and overlap; does not consult affected users on ongoing need. |
