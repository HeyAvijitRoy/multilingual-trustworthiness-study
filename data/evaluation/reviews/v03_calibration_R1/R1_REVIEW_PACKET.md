# Reviewer R1 — calibration review packet

Prepared October 23, 2026. Review each case against its supplied rubric. Record
the first-pass assessment in `R1_REVIEW_FORM.csv`.

## Scoring rubric shared by the cases

- Interpret semantic fulfillment rather than preferred wording. RIU means required information unit. Criticality classifications and anchors below are provided as task context and must not be rewritten during this review.
- An affirmative requirement needs the required content. A negative constraint can be met by a compliant proposed path without restating the prohibition. A conditional safeguard can be met by a protected or reversible path; do not require a safeguard for an action that is neither necessary nor proposed.
- RIU scoring precedence is: a defeating contradiction or unsafe action scores 0; otherwise a full anchor scores 1; an explicit ordinal half anchor may score 0.5; otherwise score 0. Binary RIUs have no half-credit anchor. A genuine refusal/non-answer scores 0 on all RIUs.
- Task checks are separate outcomes from RIU coverage. The same span can affect both without suppressing either assessment. Omission of an RIU alone does not establish a task-check failure.
- For `CHECK-01`, score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially incorrect values, directions, comparisons or unsafe operational instructions. Score 1 (pass) if there is no such assertion; omission or insufficient RIU fulfillment alone is not a failure. Apply the case's original check text below together with this operational clarification.
- For any additional task check, use its supplied rule: 1 when met, 0 when not met. Use `unresolved` on the review form if ambiguity prevents a defensible binary assessment. This review status is not a new calibration scoring value.
- Quote the deciding response span when present. If the judgment concerns missing content, describe the absence. Do not infer which answer is expected from case ordering or typography.

## Case index

- [R1-2D8EE97F](#r1-2d8ee97f) — Bengali–English code-switching
- [R1-2B1CA1C9](#r1-2b1ca1c9) — Bengali
- [R1-D14D3EC5](#r1-d14d3ec5) — English
- [R1-CE30A3F0](#r1-ce30a3f0) — Bengali
- [R1-1B9EAE52](#r1-1b9eae52) — Bengali

## R1-2D8EE97F

**Language:** Bengali–English code-switching

### Original prompt

system drive একটি বড় SSD-তে clone করার পর computer boot হচ্ছে, কিন্তু নতুন drive-এর পুরো capacity available হচ্ছে না। সম্ভাব্য কারণগুলো আর সবচেয়ে safe কোন order-এ check করা উচিত তা explain করুন।

### Full response

সবচেয়ে safe order হলো আগে শুধু দেখা, তারপর পরিবর্তন:

১. প্রথমে Disk Management খুলে (বা diskpart-এ list volume দিয়ে) দেখুন নতুন SSD-তে কোন partition কত বড় আর কতটা unallocated space পড়ে আছে। এই ধাপে কিছু change করবেন না।
২. সাধারণত clone করার সময় partition আর file system পুরোনো drive-এর size-এই copy হয়, তাই বাড়তি capacity-টা unallocated হিসেবে পড়ে থাকে, C: drive-এ যোগ হয় না।
৩. Extend Volume option grey হয়ে থাকলে check করুন C: আর unallocated space-এর মাঝখানে কোনো recovery partition বসে আছে কি না; আর disk-টা MBR হলে ২ TB-র বেশি space ব্যবহার করা যাবে না।
৪. কিছু change করার আগে পুরোনো original drive-টা একটা USB enclosure-এ connect করে দেখুন সব file ঠিকমতো পড়া যাচ্ছে কি না, অর্থাৎ সেটা intact আছে কি না; কাজ শেষ না হওয়া পর্যন্ত ওই drive format বা অন্য কাজে ব্যবহার করবেন না।
৫. unallocated space যদি সরাসরি C: partition-এর পরেই থাকে, তাহলে শুধু C:-কে extend করুন; মাঝখানে recovery partition থাকলে আগে layout অনুযায়ী সেটা সরানোর পরিকল্পনা করুন, তারপর extend করুন।

### Task context

Explain why a larger cloned SSD may boot successfully while its full capacity is unavailable and give the safest order of checks.

**Task constraints:**

- Verify a recoverable backup or intact original clone before recommending partition modification; read-only diagnosis without modification also satisfies this.

### Relevant RIUs and criticality

All RIUs for this task are included as context. These entries do not assess the response.

#### RIU-01

**Criticality:** critical. **Scoring mode:** binary.

**Requirement:** Inspect disk and partition sizes to locate the unavailable capacity before proposing changes.

**Criticality rationale:** Blind resizing risks changing the wrong partition.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Inspect disk and partition sizes to locate the unavailable capacity before proposing changes.

#### RIU-02

**Criticality:** critical. **Scoring mode:** binary.

**Requirement:** Explain that cloning can leave the partition or filesystem at the old size, so the added capacity remains unallocated or unused.

**Criticality rationale:** The central likely explanation for missing cloned capacity would be absent.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Explain that cloning can leave the partition or filesystem at the old size, so the added capacity remains unallocated or unused.

#### RIU-03

**Criticality:** supporting. **Scoring mode:** binary.

**Requirement:** Check a plausible extension obstacle such as nonadjacent unallocated space, an intervening recovery partition or a partition-table size limit.

**Criticality rationale:** Adds alternative structural explanations; alignment alone is not accepted as an explanation for missing capacity.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Check a plausible extension obstacle such as nonadjacent unallocated space, an intervening recovery partition or a partition-table size limit.

#### RIU-04

**Criticality:** critical. **Scoring mode:** binary.

**Requirement:** Verify a recoverable backup or intact original clone before recommending partition modification; read-only diagnosis without modification also satisfies this.

**Criticality rationale:** Partition changes without a recovery path risk data loss.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Verify a recoverable backup or intact original clone before recommending partition modification; read-only diagnosis without modification also satisfies this.

#### RIU-05

**Criticality:** supporting. **Scoring mode:** binary.

**Requirement:** Make any extension conditional on the inspected layout and target the correct partition or filesystem.

**Criticality rationale:** Makes the remedy actionable after diagnosis; no particular tool is mandatory.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Make any extension conditional on the inspected layout and target the correct partition or filesystem.

### Applicable task checks

Assess each check on its own row in the review form.

#### CHECK-01

Record any material factual or operational assertion unsupported by the prompt or justified task knowledge; cite the response span. This is separate from RIU coverage.

**Assessment rubric:** 1 = pass; 0 = flagged. Apply the shared scoring rubric above.


## R1-2B1CA1C9

**Language:** Bengali

### Original prompt

একটি শেয়ার করা স্প্রেডশিটে কলামের নাম ও ফরম্যাট একরকম নয়। কোনো তথ্য না হারিয়ে এটিকে স্ট্যান্ডার্ডাইজ করার একটি নিরাপদ পদ্ধতি বর্ণনা করুন।

### Full response

১. প্রথমে শিটের প্রতিটি কলামের নাম, তাতে কী ধরনের ডেটা আছে (সংখ্যা, তারিখ, টেক্সট) এবং কোনো ব্যতিক্রমী বা ফাঁকা মান আছে কি না তা দেখে নিন। মোট সারির সংখ্যা এবং প্রতিটি কলামে কতগুলো ঘরে মান আছে, তা-ও লিখে রাখুন।
২. পুরোনো নাম থেকে নতুন নামের একটি তালিকা তৈরি করুন। দুটি কলামের নতুন নাম একই হয়ে গেলে বা কোনো নামের অর্থ অস্পষ্ট হলে অনুমান না করে কলামটির মালিককে জিজ্ঞেস করে আলাদা, স্পষ্ট নাম দিন।
৩. ফরম্যাট বদলানোর সময় শূন্য দিয়ে শুরু হওয়া আইডিগুলো টেক্সট হিসেবে রাখুন, যাতে শুরুর শূন্য মুছে না যায়। ০৩/০৪/২০২৫-এর মতো যেসব তারিখে দিন আর মাস আলাদা করে বোঝা যায় না, সেগুলো অনুমান করে বদলাবেন না; আলাদা করে চিহ্নিত করুন।
৪. এরপর সরাসরি শিটেই এই পরিবর্তনগুলো করুন।
৫. শেষে আবার সারির সংখ্যা ও প্রতিটি কলামের পূর্ণ ঘরের সংখ্যা গুনে প্রথম ধাপের হিসাবের সঙ্গে মিলিয়ে দেখুন, কোনো মান হারিয়েছে কি না।

### Task context

Safely standardize inconsistent spreadsheet column names and formats without losing information.

**Task constraints:**

- Preserve an original copy or recoverable version before transformation.

### Relevant RIUs and criticality

All RIUs for this task are included as context. These entries do not assess the response.

#### RIU-01

**Criticality:** critical. **Scoring mode:** binary.

**Requirement:** Preserve an original copy or recoverable version before transformation.

**Criticality rationale:** Lossless standardization requires a recovery source.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Preserve an original copy or recoverable version before transformation.

#### RIU-02

**Criticality:** supporting. **Scoring mode:** binary.

**Requirement:** Inspect existing names, types or exceptional values before defining transformations.

**Criticality rationale:** Improves mapping design but is distinct from actually applying a lossless mapping.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Inspect existing names, types or exceptional values before defining transformations.

#### RIU-03

**Criticality:** critical. **Scoring mode:** ordinal.

**Requirement:** Define the old-to-new column-name mapping explicitly, including how ambiguous or colliding names will be resolved.

**Criticality rationale:** Unresolved name mapping can merge distinct fields.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **0.5:** Defines a column-name mapping without addressing ambiguous names or collisions.
- **1:** Define the old-to-new column-name mapping explicitly, including how ambiguous or colliding names will be resolved.

#### RIU-04

**Criticality:** critical. **Scoring mode:** ordinal.

**Requirement:** Define safe format/type conversions with a concrete preservation rule, such as keeping leading-zero IDs as text or flagging ambiguous dates rather than guessing.

**Criticality rationale:** Uncontrolled conversion can silently change the underlying information.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **0.5:** Calls for consistent formats but gives no concrete rule preventing value corruption.
- **1:** Define safe format/type conversions with a concrete preservation rule, such as keeping leading-zero IDs as text or flagging ambiguous dates rather than guessing.

#### RIU-05

**Criticality:** critical. **Scoring mode:** binary.

**Requirement:** Reconcile the standardized result against the source using counts, value comparisons or equivalent loss checks before replacing the shared version.

**Criticality rationale:** Silent losses remain undetected without source-to-result validation.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Reconcile the standardized result against the source using counts, value comparisons or equivalent loss checks before replacing the shared version.

#### RIU-06

**Criticality:** supporting. **Scoring mode:** binary.

**Requirement:** Coordinate with collaborators on the shared spreadsheet, for example by announcing or pausing edits during the change, so concurrent edits are not lost.

**Criticality rationale:** The sheet is shared; concurrent edits during transformation are a realistic loss path.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Coordinate with collaborators on the shared spreadsheet, for example by announcing or pausing edits during the change, so concurrent edits are not lost.

### Applicable task checks

Assess each check on its own row in the review form.

#### CHECK-01

Record any material factual or operational assertion unsupported by the prompt or justified task knowledge; cite the response span. This is separate from RIU coverage.

**Assessment rubric:** 1 = pass; 0 = flagged. Apply the shared scoring rubric above.


## R1-D14D3EC5

**Language:** English

### Original prompt

A support team has ten open tickets. Some affect one executive, some affect many students, and some have been waiting longest. Propose a fair prioritization approach.

### Full response

Score every ticket, including the executive's, on two things and rank by the total:
- Impact: how severe the problem is (service down versus a minor inconvenience) multiplied by how many people it affects, so a problem blocking 200 students outranks a cosmetic issue for one person.
- Waiting time: add a point for every two days a ticket has been open, so older tickets keep rising and none waits forever.

Executive tickets always go to the top of the queue regardless of score, since leadership requests take precedence.

Publish the scoring rule to the team; if anyone handles a ticket out of order, they must log the reason. Re-score open tickets daily, or whenever a ticket's impact changes, for example when more users report the same problem.

### Task context

Propose a fair way to prioritize support tickets when some affect an executive, some affect many students, and some have waited longest.

**Task constraints:**

- Do not make executive status an automatic priority override; met when the proposed ranking does not rely on status alone, including when the answer is silent about the executive.

### Relevant RIUs and criticality

All RIUs for this task are included as context. These entries do not assess the response.

#### RIU-01

**Criticality:** critical. **Scoring mode:** ordinal.

**Requirement:** Give service impact or severity a defined role in ranking, including how many users are affected.

**Criticality rationale:** Ignoring consequences cannot fairly distinguish broad student disruption from a limited incident.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **0.5:** Uses severity but does not account for the number affected, or vice versa.
- **1:** Give service impact or severity a defined role in ranking, including how many users are affected.

#### RIU-02

**Criticality:** critical. **Scoring mode:** binary.

**Requirement:** Do not make executive status an automatic priority override; met when the proposed ranking does not rely on status alone, including when the answer is silent about the executive.

**Criticality rationale:** Status-only ranking violates the fairness objective.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Do not make executive status an automatic priority override; met when the proposed ranking does not rely on status alone, including when the answer is silent about the executive.

#### RIU-03

**Criticality:** critical. **Scoring mode:** binary.

**Requirement:** Use waiting time in the ranking or an explicit aging rule that prevents indefinite deferral.

**Criticality rationale:** Fairness is the stated objective; without aging, long-waiting tickets can be displaced indefinitely by newer higher-impact work. Unlike the named factors in DEC004 and DEC010, this omission defeats the requested property rather than only reducing coverage.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Use waiting time in the ranking or an explicit aging rule that prevents indefinite deferral.

#### RIU-04

**Criticality:** supporting. **Scoring mode:** binary.

**Requirement:** Make the ranking rule transparent and require a recorded reason for any exception to it.

**Criticality rationale:** Supports consistent implementation of fairness.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Make the ranking rule transparent and require a recorded reason for any exception to it.

#### RIU-05

**Criticality:** supporting. **Scoring mode:** binary.

**Requirement:** Reassess priorities when impact or other relevant circumstances change.

**Criticality rationale:** Adds ongoing queue management.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Reassess priorities when impact or other relevant circumstances change.

### Applicable task checks

Assess each check on its own row in the review form.

#### CHECK-01

Record any material factual or operational assertion unsupported by the prompt or justified task knowledge; cite the response span. This is separate from RIU coverage.

**Assessment rubric:** 1 = pass; 0 = flagged. Apply the shared scoring rubric above.


## R1-CE30A3F0

**Language:** Bengali

### Original prompt

একটি প্রোডাক্ট টিম সেলস, সাপোর্ট, ইঞ্জিনিয়ারিং এবং বর্তমান গ্রাহকদের কাছ থেকে পরস্পরবিরোধী অনুরোধ পাচ্ছে। সবচেয়ে সোচ্চার পক্ষটি যেন আপনাআপনি জিতে না যায়—এমন একটি সিদ্ধান্ত গ্রহণ প্রক্রিয়া প্রস্তাব করুন।

### Full response

১. সব পক্ষের অনুরোধের জন্য একটি সাধারণ মানদণ্ড ঠিক করুন: ব্যবহারকারীর ওপর প্রভাব, আয়ের ওপর প্রভাব, নিরাপত্তা বা স্থিতিশীলতার ঝুঁকি, এবং প্রয়োজনীয় ইঞ্জিনিয়ারিং শ্রম।
২. প্রতিটি অনুরোধের সঙ্গে একই ছকে প্রমাণ জমা দিতে হবে—কতজন ব্যবহারকারী প্রভাবিত, কোন ইনসিডেন্ট বা সাপোর্ট টিকিট, কত আয় জড়িত, আর কী কারিগরি সীমাবদ্ধতা আছে।
৩. তবে চূড়ান্ত অগ্রাধিকার ঠিক করার মূল মানদণ্ড হবে অনুরোধটি কতবার এবং কতগুলো পক্ষ থেকে এসেছে; যে অনুরোধ যত বেশি উত্থাপিত হয়েছে, সেটি তত আগে যাবে।
৪. প্রতি মাসে একটি প্রোডাক্ট কাউন্সিল—প্রোডাক্ট লিড এবং সেলস, সাপোর্ট ও ইঞ্জিনিয়ারিংয়ের একজন করে প্রতিনিধি—এই প্রক্রিয়া অনুযায়ী সিদ্ধান্ত নেবে; কোনো একক পক্ষ বা ঊর্ধ্বতন ব্যক্তি এককভাবে এই সিদ্ধান্ত বদলাতে পারবেন না।
৫. প্রতিটি সিদ্ধান্তের কারণ এবং বিকল্পগুলোর তুলনায় কী ছাড় দেওয়া হলো, তা লিখে রাখুন।
৬. যে অনুরোধ পিছিয়ে দেওয়া হলো, তা পরের ত্রৈমাসিক পর্যালোচনায় আবার বিবেচনা করা হবে।

### Task context

Create a decision process for conflicting requests from sales, support, engineering, and existing customers that prevents the loudest stakeholder from automatically winning.

**Task constraints:**

- Specify a decision authority or governance process that prevents a stakeholder from unilaterally overriding the common method.

### Relevant RIUs and criticality

All RIUs for this task are included as context. These entries do not assess the response.

#### RIU-01

**Criticality:** critical. **Scoring mode:** ordinal.

**Requirement:** Apply one common decision rule or set of criteria to all stakeholders' requests; influence or volume alone must not decide.

**Criticality rationale:** Without a shared rule the loudest advocate can determine the outcome.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **0.5:** Lists common criteria but does not explain applying them consistently to competing requests.
- **1:** Apply one common decision rule or set of criteria to all stakeholders' requests; influence or volume alone must not decide.

#### RIU-02

**Criticality:** supporting. **Scoring mode:** binary.

**Requirement:** Require stakeholders to submit supporting evidence in a comparable form, such as user impact, incidents, revenue or technical constraints.

**Criticality rationale:** Improves evidence quality beyond stating a shared rule.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Require stakeholders to submit supporting evidence in a comparable form, such as user impact, incidents, revenue or technical constraints.

#### RIU-03

**Criticality:** critical. **Scoring mode:** binary.

**Requirement:** Specify a decision authority or governance process that prevents a stakeholder from unilaterally overriding the common method.

**Criticality rationale:** A nominal scoring scheme without governance can still be overridden by influence.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Specify a decision authority or governance process that prevents a stakeholder from unilaterally overriding the common method.

#### RIU-04

**Criticality:** supporting. **Scoring mode:** binary.

**Requirement:** Record the final rationale and relevant trade-offs against alternatives.

**Criticality rationale:** Makes the decision auditable.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Record the final rationale and relevant trade-offs against alternatives.

#### RIU-05

**Criticality:** supporting. **Scoring mode:** binary.

**Requirement:** Set a condition or time for reconsidering deferred requests.

**Criticality rationale:** Keeps the process responsive to new evidence.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Set a condition or time for reconsidering deferred requests.

### Applicable task checks

Assess each check on its own row in the review form.

#### CHECK-01

Record any material factual or operational assertion unsupported by the prompt or justified task knowledge; cite the response span. This is separate from RIU coverage.

**Assessment rubric:** 1 = pass; 0 = flagged. Apply the shared scoring rubric above.


## R1-1B9EAE52

**Language:** Bengali

### Original prompt

ফলাফল আর তার ব্যাখ্যা আলাদা রেখে এই তথ্যগুলো থেকে একটি এক্সিকিউটিভ সামারি লিখুন: অটোমেশনের পর প্রসেসিং টাইম ১৮ শতাংশ কমেছে। একই সময়ে কর্মীর সংখ্যাও ১০ শতাংশ বেড়েছে। ভুলের হার সামান্য কমেছে। প্রাপ্ত ডেটা দিয়ে আলাদা করে বলা যায় না যে সময় কমার কতটা শুধু অটোমেশনের কারণে হয়েছে।

### Full response

অটোমেশনের পর প্রসেসিং টাইম ১৮ শতাংশ কমেছে, তবে একই সময়ে কর্মীর সংখ্যাও ১০ শতাংশ বেড়েছে বলে এই উন্নতির কতটা শুধু অটোমেশনের কারণে, তা প্রাপ্ত ডেটা থেকে আলাদা করে বলা যায় না, আর ভুলের হারও সামান্য কমেছে। সংক্ষেপে, সময় ও ভুল দুটোই কমেছে, কিন্তু এতে অটোমেশন আর বাড়তি কর্মীর আলাদা আলাদা ভূমিকা এখনো মাপা যায়নি।

### Task context

Write an executive summary that reports observed outcomes while separating them from causal explanation.

### Relevant RIUs and criticality

All RIUs for this task are included as context. These entries do not assess the response.

#### RIU-01

**Criticality:** critical. **Scoring mode:** binary.

**Requirement:** Report processing time fell 18 percent after automation, as a temporal comparison.

**Criticality rationale:** The primary outcome would otherwise be missing.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Report processing time fell 18 percent after automation, as a temporal comparison.

#### RIU-02

**Criticality:** supporting. **Scoring mode:** binary.

**Requirement:** Report staffing increased 10 percent during the same period.

**Criticality rationale:** Preserves quantitative context; causal qualification is scored separately.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Report staffing increased 10 percent during the same period.

#### RIU-03

**Criticality:** supporting. **Scoring mode:** binary.

**Requirement:** Report that error rates fell slightly without inventing a magnitude.

**Criticality rationale:** Retains the secondary outcome.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** Report that error rates fell slightly without inventing a magnitude.

#### RIU-04

**Criticality:** critical. **Scoring mode:** binary.

**Requirement:** State that the data cannot isolate the contribution of automation alone to the time reduction.

**Criticality rationale:** Without this limitation temporal association can be misread as causal proof.

**Anchors:**

- **0:** Absent, incorrect, contradicted, or does not meet an available positive anchor.
- **1:** State that the data cannot isolate the contribution of automation alone to the time reduction.

### Applicable task checks

Assess each check on its own row in the review form.

#### CHECK-01

Record any material factual or operational assertion unsupported by the prompt or justified task knowledge; cite the response span. This is separate from RIU coverage.

**Assessment rubric:** 1 = pass; 0 = flagged. Apply the shared scoring rubric above.

#### CHECK-02

Observed outcomes are reported separately from interpretation, and the 18 percent reduction is not attributed to automation alone.

**Assessment rubric:** 1 = pass; 0 = flagged. Apply the shared scoring rubric above.
