# P06 independent review packet

Status: pending. AI-produced draft annotations; no human acceptance is claimed.

Each task needs bilingual equivalence and full-prompt coverage review. Review all critical units, all ambiguity/boundary questions below, and every prespecified ordinary sample item. Additional ordinary units may be reviewed. Blank identity/decision fields are intentional.

25 tasks; 124 RIUs; 50 critical; 21 ordinary sample units; 72 mandatory unit reviews.

## Reviewer procedure

- [ ] Record validator identity, EN/BN competence, actual date and draft hashes in a new review log.
- [ ] For every task compare EN, BN and BN-CS facts, quantities, constraints and requested output.
- [ ] Check complete coverage, atomicity/overlap, omission-consequence rationale and alternative valid paths.
- [ ] Review each marked critical/ambiguity/sample unit and its zero/full/half anchors.
- [ ] Apply protocol 0.3 silence, conditional safeguard, contradiction and CHECK-01 rules.
- [ ] Record disputes per task/RIU, proposed change, resolution and adjudicator; leave unresolved items pending.
- [ ] Escalate systematic rule errors to every affected unit, including other batches; revalidate revisions.
- [ ] Obtain explicit validator and study-lead acceptance before any status promotion or gold assembly.

Ordinary sampling: ceil(n/5) per domain/difficulty/scoring-mode stratum of supporting RIUs, ranked by prespecified SHA-256. See the JSON packet for exact selections and counts.

## Escalation

A systematic rule error requires review of every affected unit in the batch and other drafted batches, including units outside the ordinary sample. Log scope, rule, affected IDs, revisions and resolution; rerun validation and regenerate packets before independent acceptance. No silent frozen edits.

## CYBER028

cybersecurity_digital_safety; medium.

### en

A company suspects a laptop may have been tampered with while unattended during travel. Describe a cautious investigation and containment approach that avoids destroying evidence.

### bn

একটি প্রতিষ্ঠান সন্দেহ করছে, ভ্রমণের সময় নজরের বাইরে থাকা অবস্থায় একটি ল্যাপটপে কেউ কারসাজি করে থাকতে পারে। প্রমাণ নষ্ট না করে সতর্কভাবে তদন্ত ও কনটেইনমেন্টের একটি পদ্ধতি বর্ণনা করুন।

### bn_cs

একটি company সন্দেহ করছে, travel-এর সময় unattended অবস্থায় একটি laptop-এ কেউ tamper করে থাকতে পারে। evidence নষ্ট না করে সতর্কভাবে investigation আর containment-এর একটি approach describe করুন।

### Boundary and ambiguity questions

- [ ] RIU-01: Boundary: powering the device off may lose volatile evidence; draft does not require a specific choice.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Do not wipe, reimage or casually use the laptop before evidence is preserved; isolating it unchanged complies.
  Rationale: Explicit prompt requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Isolate the laptop from networks and stop using it for work.
  Rationale: Containment.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Record chain of custody and physical condition, such as seals, screws, ports or damage.
  Rationale: Evidence handling.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Involve security or forensic specialists to image and examine the device.
  Rationale: Proper investigation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Reset or revoke credentials that were used on or stored on the laptop.
  Rationale: Protects accounts if the device was compromised.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Review account and network logs for suspicious activity linked to the device.
  Rationale: Additional evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Powering off versus keeping running is debated; either is acceptable if justified. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER064

cybersecurity_digital_safety; medium.

### en

A cloud administrator discovers several unused access keys that have not been rotated for a long time. Propose a safe cleanup process.

### bn

একজন ক্লাউড অ্যাডমিনিস্ট্রেটর কয়েকটি অব্যবহৃত অ্যাক্সেস-কি খুঁজে পেয়েছেন, যেগুলো দীর্ঘদিন রোটেট করা হয়নি। নিরাপদভাবে এগুলো পরিষ্কার করার একটি প্রক্রিয়া প্রস্তাব করুন।

### bn_cs

একজন cloud administrator কয়েকটি unused access key খুঁজে পেয়েছেন, যেগুলো দীর্ঘদিন rotate করা হয়নি। safely cleanup করার একটি process propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Verify each key is actually unused, such as from last-used data and logs, and identify its owner or dependent application.
  Rationale: Avoids breaking a hidden dependency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Deactivate keys first and observe for breakage before deleting them.
  Rationale: A reversible step before an irreversible one.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Delete keys after the observation period if nothing breaks.
  Rationale: Completes cleanup.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Review logs for misuse of the old keys before or during cleanup.
  Rationale: Long-lived keys may already be compromised.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Prevent recurrence, such as rotation policy, short-lived credentials or alerts on unused keys.
  Rationale: Addresses the underlying problem.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Notifying owners is part of RIU-01. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER085

cybersecurity_digital_safety; medium.

### en

An organization wants to retain detailed user logs indefinitely because they might be useful later. Explain the privacy and security tradeoffs.

### bn

একটি প্রতিষ্ঠান বিস্তারিত ইউজার লগ অনির্দিষ্টকাল সংরক্ষণ করতে চায়, কারণ পরে সেগুলো কাজে লাগতে পারে। প্রাইভেসি ও নিরাপত্তার দিক থেকে এর ট্রেড-অফগুলো ব্যাখ্যা করুন।

### bn_cs

একটি প্রতিষ্ঠান detailed user log অনির্দিষ্টকাল retain করতে চায়, কারণ পরে সেগুলো কাজে লাগতে পারে। privacy আর security-র tradeoff-গুলো explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that indefinite retention increases privacy risk and the harm of a breach because more personal data is exposed.
  Rationale: The core privacy/security cost.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Acknowledge the security benefit of logs for investigations and detection.
  Rationale: The other side.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Mention legal or regulatory limits such as data-minimization or storage-limitation principles.
  Rationale: Compliance dimension.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Propose a defined retention period tied to purpose, or aggregation or anonymization of older logs.
  Rationale: Resolves the trade-off.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Mention storage cost or difficulty of managing large log volumes.
  Rationale: Operational cost.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. No specific retention period required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER093

cybersecurity_digital_safety; easy.

### en

A team receives too many security warnings and starts ignoring them. Explain what alert fatigue is and why it creates risk.

### bn

একটি টিম এত বেশি সিকিউরিটি ওয়ার্নিং পায় যে তারা সেগুলো উপেক্ষা করতে শুরু করেছে। অ্যালার্ট ফ্যাটিগ কী এবং কেন এটি ঝুঁকি তৈরি করে তা ব্যাখ্যা করুন।

### bn_cs

একটি team এত বেশি security warning পায় যে তারা সেগুলো ignore করতে শুরু করেছে। alert fatigue কী এবং কেন এটা risk তৈরি করে তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Define alert fatigue as desensitization from a high volume of alerts, often many false or low-value ones, leading people to ignore or dismiss them.
  Rationale: The definition asked for.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Explain that real threats can be missed or responded to late because they are hidden among ignored alerts.
  Rationale: The core risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Mention that it can lead to disabling or bypassing alerts entirely.
  Rationale: A further risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Indicate a remedy direction such as tuning, prioritizing or consolidating alerts.
  Rationale: Useful but not requested.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. The prompt asks what and why; remedies are supporting. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER100

cybersecurity_digital_safety; hard.

### en

After a serious incident, leadership wants to impose many new security rules immediately. Explain how to prioritize controls using evidence, root causes, usability, and measurable risk reduction.

### bn

একটি গুরুতর ঘটনার পর নেতৃত্ব সঙ্গে সঙ্গে অনেকগুলো নতুন নিরাপত্তা নিয়ম চাপিয়ে দিতে চায়। প্রমাণ, মূল কারণ, ব্যবহারযোগ্যতা এবং পরিমাপযোগ্য ঝুঁকি-হ্রাস ব্যবহার করে কোন নিয়ন্ত্রণগুলো আগে নেওয়া উচিত তা কীভাবে নির্ধারণ করবেন ব্যাখ্যা করুন।

### bn_cs

একটি serious incident-এর পর leadership সঙ্গে সঙ্গে অনেকগুলো নতুন security rule চাপিয়ে দিতে চায়। evidence, root cause, usability আর measurable risk reduction ব্যবহার করে কোন control-গুলো আগে নেওয়া উচিত তা কীভাবে prioritize করবেন explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Base priorities on the incident's root causes and evidence of how it happened, not on the volume of new rules.
  Rationale: A named factor and the core principle.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Assess usability and operational impact of each control, since unusable rules lead to workarounds.
  Rationale: A named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Estimate and later measure the risk reduction each control achieves.
  Rationale: A named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Rank or phase controls by combining risk reduction, root-cause relevance and cost or usability, rather than imposing all at once.
  Rationale: The prompt asks how to prioritize.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Names factors but does not combine them into an order or phasing.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Communicate the plan and rationale to leadership and affected staff.
  Rationale: Manages leadership pressure.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Immediate containment fixes for the specific incident may be fast-tracked; acceptable within RIU-04. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC032

decision_support; easy.

### en

A team has one spare laptop and two employees temporarily need it. Explain what information should determine who receives it first.

### bn

একটি টিমের হাতে একটি বাড়তি ল্যাপটপ আছে, আর দুজন কর্মীর সাময়িকভাবে সেটি দরকার। কে আগে পাবেন তা কোন তথ্যের ভিত্তিতে ঠিক করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি team-এর হাতে একটি spare laptop আছে, আর দুজন employee-র temporarily সেটা দরকার। কে আগে পাবেন তা কোন information-এর ভিত্তিতে ঠিক করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Compare the urgency and business impact of each person's need, such as deadlines or blocked work.
  Rationale: The primary criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Compare how long each needs it and whether usage could be scheduled or shared.
  Rationale: Determines feasibility of sequencing.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check whether either has an alternative, such as a repair timeline or another device.
  Rationale: Affects need.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Use a transparent rule and communicate it.
  Rationale: Fairness.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC035

decision_support; medium.

### en

A project has two developers and one analyst but three workstreams all need progress this week. Explain how to allocate people based on dependencies, bottlenecks, deadlines, and specialization.

### bn

একটি প্রজেক্টে দুজন ডেভেলপার ও একজন অ্যানালিস্ট আছেন, কিন্তু তিনটি কাজের ধারাতেই এই সপ্তাহে অগ্রগতি দরকার। ডিপেন্ডেন্সি, যেখানে কাজ আটকে যাচ্ছে, সময়সীমা এবং বিশেষ দক্ষতার ভিত্তিতে কীভাবে লোক ভাগ করে দেবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি project-এ দুজন developer আর একজন analyst আছেন, কিন্তু তিনটি workstream-এই এই সপ্তাহে progress দরকার। dependency, bottleneck, deadline আর specialization-এর ভিত্তিতে কীভাবে লোক allocate করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Identify dependencies between workstreams and prioritize work that unblocks others.
  Rationale: A named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Identify the bottleneck and assign capacity to it.
  Rationale: A named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Account for each workstream's deadline.
  Rationale: A named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Match people to work requiring their specialization, such as the analyst to analysis.
  Rationale: A named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Combine the factors into an allocation of the three people, recognizing that one workstream may get partial or shared support.
  Rationale: The prompt asks how to allocate.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Discusses factors but gives no allocation approach.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Communicate the allocation and review progress during the week.
  Rationale: Adapts to change.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC039

decision_support; hard.

### en

A technology budget can fund either broad upgrades for many users or a full replacement for one failing critical system. Explain how to structure the decision and what evidence is needed.

### bn

একটি প্রযুক্তি বাজেট দিয়ে হয় অনেক ব্যবহারকারীর জন্য ব্যাপক আপগ্রেড করা যাবে, নয়তো বারবার বিকল হতে থাকা একটি গুরুত্বপূর্ণ সিস্টেম পুরোপুরি বদলানো যাবে। সিদ্ধান্তটি কীভাবে কাঠামোবদ্ধ করবেন এবং কোন কোন প্রমাণ দরকার তা ব্যাখ্যা করুন।

### bn_cs

একটি technology budget দিয়ে হয় অনেক user-এর জন্য broad upgrade করা যাবে, নয়তো ক্রমশ fail করতে থাকা একটি critical system পুরোপুরি replace করা যাবে। decision-টা কীভাবে structure করবেন এবং কোন কোন evidence দরকার তা explain করুন।

### Boundary and ambiguity questions

- [ ] Task-level: Language drift: BN "বারবার বিকল হতে থাকা" (repeatedly failing) vs BN-CS "ক্রমশ fail করতে থাকা" (progressively failing) vs EN "failing"; confirm the difference is immaterial.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Gather evidence on the failing system: failure frequency, impact of outages and risk of total failure.
  Rationale: A key evidence need.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Gather evidence on the benefit of the broad upgrades, such as productivity or security gains across users.
  Rationale: A key evidence need.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Compare both options on risk reduction and benefit per cost within the same framework.
  Rationale: The decision structure.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Compares the options but on different or incomplete criteria.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Consider partial options, such as phased upgrades or interim mitigation for the critical system.
  Rationale: Avoids a false binary.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Consider consequences of deferring each option.
  Rationale: Opportunity cost.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Language note: EN "failing", BN "repeatedly failing", BN-CS "progressively failing"; the scoring units do not depend on the failure pattern. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC047

decision_support; medium.

### en

A traveler can take a short connection with a higher chance of missing the next flight or a longer connection that adds three hours. Explain what evidence should guide the choice.

### bn

একজন যাত্রী এমন একটি অল্প সময়ের কানেকশন নিতে পারেন, যাতে পরের ফ্লাইট মিস হওয়ার সম্ভাবনা বেশি, অথবা এমন একটি লম্বা কানেকশন নিতে পারেন, যাতে যাত্রায় তিন ঘণ্টা বেশি লাগবে। কোন কোন প্রমাণ এই সিদ্ধান্তকে পথ দেখানো উচিত তা ব্যাখ্যা করুন।

### bn_cs

একজন traveler এমন একটি short connection নিতে পারেন, যাতে পরের flight miss হওয়ার chance বেশি, অথবা এমন একটি longer connection নিতে পারেন, যাতে যাত্রায় তিন ঘণ্টা বেশি লাগবে। কোন কোন evidence এই choice-কে guide করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Assess the probability of missing the short connection, such as minimum connection time, terminal change or on-time record.
  Rationale: Core evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Assess the consequence of missing it, such as next available flight, overnight stay or a missed event.
  Rationale: Core evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check whether flights are on one ticket so the airline rebooks a missed connection.
  Rationale: Changes the consequence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Weigh the certain three-hour cost against the expected cost of a missed connection.
  Rationale: The decision.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC067

decision_support; medium.

### en

A model performs better overall after an update but worse for one important subgroup. Explain what evidence is needed before deciding whether the update should be adopted.

### bn

একটি আপডেটের পর একটি মডেল সামগ্রিকভাবে ভালো করছে, কিন্তু একটি গুরুত্বপূর্ণ উপগোষ্ঠীর ক্ষেত্রে খারাপ করছে। আপডেটটি গ্রহণ করা হবে কি না সেই সিদ্ধান্তের আগে কোন কোন প্রমাণ দরকার তা ব্যাখ্যা করুন।

### bn_cs

একটি update-এর পর একটি model overall ভালো perform করছে, কিন্তু একটি গুরুত্বপূর্ণ subgroup-এর ক্ষেত্রে খারাপ করছে। update-টা adopt করা হবে কি না সেই decision-এর আগে কোন কোন evidence দরকার তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Measure how large the subgroup degradation is and whether it is statistically reliable given subgroup size.
  Rationale: Size and reliability of the harm.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Assess the consequences of errors for the subgroup, such as fairness or harm.
  Rationale: Determines whether the trade-off is acceptable.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Investigate why performance dropped, such as data or feature changes.
  Rationale: Points to a fix.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Consider options such as fixing the regression, subgroup-specific handling or staged rollout.
  Rationale: Alternatives to adopt-or-reject.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Avoid relying on overall metrics alone.
  Rationale: The core caution.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC045

procedural_instructional; medium.

### en

Explain how to prepare for a trip when the destination weather may change significantly during the week.

### bn

সপ্তাহজুড়ে গন্তব্যের আবহাওয়া উল্লেখযোগ্যভাবে বদলে যেতে পারে—এমন একটি ভ্রমণের জন্য কীভাবে প্রস্তুতি নেবেন তা ব্যাখ্যা করুন।

### bn_cs

সপ্তাহজুড়ে destination-এর weather উল্লেখযোগ্যভাবে বদলে যেতে পারে—এমন একটি trip-এর জন্য কীভাবে prepare করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check the forecast range for the week shortly before leaving and during the trip.
  Rationale: The source of information.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Pack layers or versatile clothing covering the range of expected conditions.
  Rationale: The core preparation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Include weather protection such as rain gear or sun protection.
  Rationale: Specific items.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Plan flexible activities with indoor or rescheduling alternatives.
  Rationale: Itinerary flexibility.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC057

procedural_instructional; medium.

### en

A person has been asked to submit documents through an online portal before an appointment. Describe a procedure for verifying completion and keeping copies.

### bn

একজন ব্যক্তিকে অ্যাপয়েন্টমেন্টের আগে একটি অনলাইন পোর্টালের মাধ্যমে কাগজপত্র জমা দিতে বলা হয়েছে। জমা দেওয়া সম্পূর্ণ হয়েছে কি না যাচাই করা এবং কপি রেখে দেওয়ার একটি পদ্ধতি বর্ণনা করুন।

### bn_cs

একজন ব্যক্তিকে appointment-এর আগে একটি online portal-এর মাধ্যমে document submit করতে বলা হয়েছে। submission complete হয়েছে কি না verify করা আর copy রেখে দেওয়ার একটি procedure describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check the portal for a submission confirmation or status showing each document was received.
  Rationale: Verifies completion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Save the confirmation, such as a screenshot, receipt number or email.
  Rationale: A record.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Keep copies of the submitted documents.
  Rationale: Explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Contact the office if confirmation is missing or unclear, well before the appointment.
  Rationale: Resolves problems in time.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Secure storage of copies is good practice; not required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC065

procedural_instructional; medium.

### en

Explain how to prepare a run-of-show for a 90-minute event with several speakers and a question period.

### bn

কয়েকজন বক্তা ও একটি প্রশ্নোত্তর পর্বসহ ৯০ মিনিটের একটি অনুষ্ঠানের মিনিট-ধরে-ধরে অনুষ্ঠানসূচি কীভাবে তৈরি করবেন তা ব্যাখ্যা করুন।

### bn_cs

কয়েকজন speaker আর একটি Q&A পর্বসহ ৯০ মিনিটের একটি event-এর run-of-show কীভাবে তৈরি করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Build a timed sequence of segments with start times and durations that fits within 90 minutes.
  Rationale: The run-of-show itself.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Allocate a specific time block for the question period.
  Rationale: A named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Include transitions and responsibilities, such as who introduces speakers and technical cues.
  Rationale: Operational detail.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Build in buffer and a plan for overruns.
  Rationale: Speakers often overrun.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Share the run-of-show with speakers and staff in advance.
  Rationale: Coordination.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC072

procedural_instructional; easy.

### en

Describe a simple process for checking a monthly statement for unexpected charges.

### bn

মাসিক স্টেটমেন্টে অপ্রত্যাশিত কোনো চার্জ আছে কি না তা যাচাই করার একটি সহজ প্রক্রিয়া বর্ণনা করুন।

### bn_cs

monthly statement-এ unexpected কোনো charge আছে কি না তা check করার একটি simple process describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Compare each charge against receipts, records or known recurring payments.
  Rationale: The core check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Look for warning signs such as unfamiliar merchants, duplicate charges or unexpected subscription renewals.
  Rationale: Targeted review.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Contact the bank or merchant promptly about unrecognized charges.
  Rationale: The response to an unexpected charge.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Do this monthly, soon after the statement arrives.
  Rationale: Disputes have time limits.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC079

procedural_instructional; hard.

### en

Several teams share one project budget but submit expenses at different times. Propose a procedure that keeps commitments, actual spending, pending reimbursements, and remaining funds visible.

### bn

কয়েকটি টিম একটি প্রজেক্ট বাজেট ভাগাভাগি করে ব্যবহার করে, কিন্তু ভিন্ন ভিন্ন সময়ে খরচ জমা দেয়। প্রতিশ্রুত খরচ, প্রকৃত খরচ, অপেক্ষমাণ রিইমবার্সমেন্ট এবং অবশিষ্ট অর্থ—সবকিছু দৃশ্যমান রাখে এমন একটি পদ্ধতি প্রস্তাব করুন।

### bn_cs

কয়েকটি team একটি project budget share করে ব্যবহার করে, কিন্তু আলাদা আলাদা সময়ে expense submit করে। commitment, actual spending, pending reimbursement আর remaining fund—সবকিছু visible রাখে এমন একটি procedure propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Maintain one shared tracker for the budget.
  Rationale: The single source of truth.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Record commitments when they are made, before invoices or expenses arrive.
  Rationale: Prevents overspending from late submissions.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Record actual spending when paid.
  Rationale: A named category.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Track pending reimbursements separately until paid.
  Rationale: A named category.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Calculate remaining funds as budget minus actual spending, commitments and pending reimbursements.
  Rationale: Correct remaining-funds logic.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Review the tracker on a regular schedule with the teams.
  Rationale: Keeps it current.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN002

information_synthesis; easy.

### en

Summarize the following while preserving all dates: Applications open March 1. The priority deadline is March 20. Final submissions close April 5. Decisions are released April 25.

### bn

সব তারিখ ঠিক রেখে নিচের তথ্যগুলো সংক্ষেপ করুন: আবেদন শুরু হবে ১ মার্চ। অগ্রাধিকার-ভিত্তিক আবেদনের শেষ তারিখ ২০ মার্চ। চূড়ান্ত জমা বন্ধ হবে ৫ এপ্রিল। ফলাফল প্রকাশ করা হবে ২৫ এপ্রিল।

### bn_cs

সব date ঠিক রেখে নিচের তথ্যগুলো summarize করুন: application শুরু হবে ১ মার্চ। priority deadline ২০ মার্চ। final submission বন্ধ হবে ৫ এপ্রিল। decision release করা হবে ২৫ এপ্রিল।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that applications open March 1.
  Rationale: Date.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State the priority deadline of March 20.
  Rationale: Date.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that final submissions close April 5.
  Rationale: Date.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): State that decisions are released April 25.
  Rationale: Date.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN016

information_synthesis; medium.

### en

Compare two study designs: Study A has 500 participants but no control group. Study B has 120 participants with random assignment to treatment and control. Both measure the same outcome after four weeks.

### bn

দুটি গবেষণা-নকশা তুলনা করুন: গবেষণা A-তে ৫০০ জন অংশগ্রহণকারী আছেন, কিন্তু কোনো কন্ট্রোল গ্রুপ নেই। গবেষণা B-তে ১২০ জন অংশগ্রহণকারী আছেন, যাঁদের দৈবচয়নের মাধ্যমে ট্রিটমেন্ট ও কন্ট্রোল গ্রুপে ভাগ করা হয়েছে। দুটি গবেষণাই চার সপ্তাহ পর একই ফলাফল পরিমাপ করে।

### bn_cs

দুটি study design compare করুন: Study A-তে ৫০০ জন participant আছেন, কিন্তু কোনো control group নেই। Study B-তে ১২০ জন participant আছেন, যাঁদের random assignment-এর মাধ্যমে treatment আর control group-এ ভাগ করা হয়েছে। দুটি study-ই চার সপ্তাহ পর একই outcome measure করে।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that Study B's randomization and control group support causal conclusions, while Study A cannot separate the intervention from other changes.
  Rationale: The core design comparison.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Note that Study A's larger sample gives more precise estimates of its outcome but does not fix the lack of control.
  Rationale: Sample size versus bias.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Note that both measure the same outcome at four weeks, allowing comparison of results.
  Rationale: Stated fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Note Study B's smaller sample limits precision or subgroup analysis.
  Rationale: Balanced limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN070

information_synthesis; hard.

### en

A multilingual evaluation finds lower average scores in Language B than Language A, but prompt difficulty was not perfectly balanced. Explain what result can be reported and why language alone should not yet be treated as the proven cause.

### bn

একটি বহুভাষিক মূল্যায়নে দেখা গেছে, ভাষা A-এর তুলনায় ভাষা B-তে গড় স্কোর কম, কিন্তু প্রম্পটগুলোর কাঠিন্য পুরোপুরি সমান রাখা হয়নি। কোন ফলাফল জানানো যায় এবং কেন এখনই শুধু ভাষাকেই প্রমাণিত কারণ হিসেবে ধরা উচিত নয় তা ব্যাখ্যা করুন।

### bn_cs

একটি multilingual evaluation-এ দেখা গেছে, Language A-এর তুলনায় Language B-তে average score কম, কিন্তু prompt difficulty পুরোপুরি balanced ছিল না। কোন result report করা যায় এবং কেন এখনই শুধু language-কেই proven cause হিসেবে ধরা উচিত নয় তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Report the observed difference: Language B had lower average scores than Language A in this evaluation.
  Rationale: The reportable result.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Explain that unbalanced prompt difficulty is a confounder, so the difference could be partly or entirely due to harder prompts in Language B.
  Rationale: The core reason.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): State that a causal language claim requires controlling for difficulty, such as matched prompts or adjusting for difficulty.
  Rationale: The remedy.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Mention other possible factors such as translation quality or sample size.
  Rationale: Additional confounders.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN088

information_synthesis; medium.

### en

Create a prioritized risk summary: Launch is in five days. One high-severity bug has a workaround. Two medium bugs have no workaround. Security review is complete. Performance testing is only 60 percent complete. Training materials are ready.

### bn

অগ্রাধিকার অনুযায়ী সাজানো একটি ঝুঁকি-সারাংশ তৈরি করুন: চালু হতে আর পাঁচ দিন বাকি। উচ্চ মাত্রার একটি বাগের সাময়িক সমাধান আছে। মাঝারি মাত্রার দুটি বাগের কোনো সাময়িক সমাধান নেই। নিরাপত্তা পর্যালোচনা শেষ হয়েছে। পারফরম্যান্স টেস্টিং মাত্র ৬০ শতাংশ সম্পন্ন। প্রশিক্ষণের উপকরণ প্রস্তুত।

### bn_cs

prioritized একটি risk summary তৈরি করুন: launch হতে আর পাঁচ দিন বাকি। high-severity একটি bug-এর workaround আছে। medium মাত্রার দুটি bug-এর কোনো workaround নেই। security review complete হয়েছে। performance testing মাত্র ৬০ শতাংশ complete। training material ready।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-02, RIU-03: Multiple defensible orderings; confirm units do not force one ranking.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Identify incomplete performance testing (60 percent) as a top risk with five days left.
  Rationale: Unknown performance risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Identify the two medium bugs without workarounds as a significant risk.
  Rationale: Unmitigated defects.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary): Note the high-severity bug has a workaround, lowering its immediate risk but still needing attention.
  Rationale: Correct relative ranking.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Note that security review is complete and training materials are ready.
  Rationale: Completed items.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Present the risks in an explicit priority order with a reason.
  Rationale: The prompt asks for prioritization.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists risks without an order or without reasons.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Reasonable orderings that justify ranking differ; the high-severity bug may rank above medium bugs if the workaround is fragile. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN093

information_synthesis; medium.

### en

Create a concise project-status synthesis that distinguishes completed work, work in progress, dependencies, and schedule risk. Dataset A contains 5,000 records. Its duplicate-removal and field-standardization steps are complete, and a quality check found no unresolved blocking errors. Dataset B contains 8,000 records. Sixty percent of Dataset B has been cleaned; the remaining records include older entries with inconsistent date formats and missing category labels. Two analysts are working on Dataset B today, but one will be unavailable tomorrow. The team originally planned to finish cleaning both datasets by Friday afternoon. Statistical analysis is not allowed to begin on the combined data until both datasets pass the same validation rules. A preliminary descriptive analysis has been run on the cleaned portion of Dataset A only, but those preliminary numbers must not be presented as final study results. The target date for the full analysis to begin is Monday morning. If Dataset B is not ready by Friday, the team can use Monday morning for final cleaning, but doing so would delay the first full analysis by at least one business day. The report deadline itself has not changed and remains the following Thursday at noon. The visualization specialist needs validated summary tables at least 24 hours before the report deadline. No additional analyst has yet been assigned. The project manager has asked the team to report by 3:00 PM Friday whether Monday analysis remains realistic. The available information does not establish how long the remaining inconsistent records will take to correct, so the synthesis should describe that as an uncertainty rather than inventing a completion estimate.

### bn

সম্পন্ন কাজ, চলমান কাজ, পারস্পরিক নির্ভরতা এবং সময়সূচির ঝুঁকি আলাদা করে প্রজেক্টের অবস্থার একটি সংক্ষিপ্ত সমন্বিত সারাংশ তৈরি করুন। ডেটাসেট A-তে ৫,০০০টি রেকর্ড আছে। এর ডুপ্লিকেট সরানো এবং ফিল্ড স্ট্যান্ডার্ডাইজেশনের ধাপ সম্পন্ন হয়েছে, এবং একটি মান-যাচাইয়ে কাজ আটকে দেওয়ার মতো কোনো অমীমাংসিত এরর পাওয়া যায়নি। ডেটাসেট B-তে ৮,০০০টি রেকর্ড আছে। ডেটাসেট B-এর ৬০ শতাংশ পরিষ্কার করা হয়েছে; বাকি রেকর্ডগুলোর মধ্যে এমন পুরোনো এন্ট্রি আছে, যেগুলোর তারিখের ফরম্যাট অসামঞ্জস্যপূর্ণ এবং ক্যাটাগরি লেবেল অনুপস্থিত। আজ দুজন অ্যানালিস্ট ডেটাসেট B নিয়ে কাজ করছেন, কিন্তু তাঁদের একজনকে আগামীকাল পাওয়া যাবে না। টিমের মূল পরিকল্পনা ছিল শুক্রবার বিকেলের মধ্যে দুটি ডেটাসেটেরই পরিষ্কারের কাজ শেষ করা। দুটি ডেটাসেটই একই ভ্যালিডেশন রুলে উত্তীর্ণ না হওয়া পর্যন্ত একত্রিত ডেটার ওপর পরিসংখ্যানগত বিশ্লেষণ শুরু করার অনুমতি নেই। শুধু ডেটাসেট A-এর পরিষ্কার অংশের ওপর একটি প্রাথমিক বর্ণনামূলক বিশ্লেষণ চালানো হয়েছে, কিন্তু সেই প্রাথমিক সংখ্যাগুলো চূড়ান্ত গবেষণা-ফলাফল হিসেবে উপস্থাপন করা যাবে না। পূর্ণ বিশ্লেষণ শুরুর লক্ষ্য সোমবার সকাল। শুক্রবারের মধ্যে ডেটাসেট B প্রস্তুত না হলে টিম সোমবার সকালটা শেষ পর্যায়ের পরিষ্কারের কাজে ব্যবহার করতে পারে, কিন্তু তাতে প্রথম পূর্ণ বিশ্লেষণ অন্তত এক কর্মদিবস পিছিয়ে যাবে। রিপোর্ট জমার সময়সীমা অবশ্য বদলায়নি; সেটি এখনো পরের বৃহস্পতিবার দুপুর ১২টা। ভিজ্যুয়ালাইজেশন বিশেষজ্ঞের রিপোর্টের সময়সীমার অন্তত ২৪ ঘণ্টা আগে যাচাইকৃত সারাংশ-টেবিল দরকার। এখনো কোনো অতিরিক্ত অ্যানালিস্ট নিয়োগ দেওয়া হয়নি। প্রজেক্ট ম্যানেজার টিমকে শুক্রবার বিকেল ৩টার মধ্যে জানাতে বলেছেন, সোমবার বিশ্লেষণ শুরু করা এখনো বাস্তবসম্মত কি না। বাকি অসামঞ্জস্যপূর্ণ রেকর্ডগুলো ঠিক করতে কত সময় লাগবে, তা হাতে থাকা তথ্য থেকে নির্ধারণ করা যায় না, তাই সারাংশে বিষয়টিকে অনিশ্চয়তা হিসেবে বর্ণনা করতে হবে, নিজে থেকে কাজ শেষ হওয়ার কোনো সময় অনুমান করে বসানো যাবে না।

### bn_cs

completed work, work in progress, dependency আর schedule risk আলাদা করে project status-এর একটি concise synthesis তৈরি করুন। Dataset A-তে ৫,০০০টি record আছে। এর duplicate removal আর field standardization-এর step complete হয়েছে, এবং একটি quality check-এ unresolved কোনো blocking error পাওয়া যায়নি। Dataset B-তে ৮,০০০টি record আছে। Dataset B-এর ৬০ শতাংশ clean করা হয়েছে; বাকি record-গুলোর মধ্যে এমন পুরোনো entry আছে, যেগুলোর date format inconsistent এবং category label missing। আজ দুজন analyst Dataset B নিয়ে কাজ করছেন, কিন্তু তাঁদের একজন আগামীকাল unavailable থাকবেন। team-এর original plan ছিল শুক্রবার বিকেলের মধ্যে দুটি dataset-এরই cleaning শেষ করা। দুটি dataset-ই একই validation rule pass না করা পর্যন্ত combined data-র ওপর statistical analysis শুরু করার অনুমতি নেই। শুধু Dataset A-এর clean করা অংশের ওপর একটি preliminary descriptive analysis run করা হয়েছে, কিন্তু সেই preliminary number-গুলো final study result হিসেবে present করা যাবে না। full analysis শুরুর target date সোমবার সকাল। শুক্রবারের মধ্যে Dataset B ready না হলে team সোমবার সকালটা final cleaning-এ ব্যবহার করতে পারে, কিন্তু তাতে প্রথম full analysis অন্তত এক business day পিছিয়ে যাবে। report deadline অবশ্য বদলায়নি; সেটা এখনো পরের বৃহস্পতিবার দুপুর ১২টা। visualization specialist-এর report deadline-এর অন্তত ২৪ ঘণ্টা আগে validated summary table দরকার। এখনো কোনো additional analyst assign করা হয়নি। project manager team-কে শুক্রবার বিকেল ৩টার মধ্যে জানাতে বলেছেন, সোমবার analysis শুরু করা এখনো realistic কি না। বাকি inconsistent record-গুলো correct করতে কত সময় লাগবে, তা available information থেকে নির্ধারণ করা যায় না, তাই synthesis-এ বিষয়টাকে uncertainty হিসেবে describe করতে হবে, নিজে থেকে কোনো completion estimate বানিয়ে দেওয়া যাবে না।

### Boundary and ambiguity questions

- [ ] RIU-05: Bundled schedule-risk unit; confirm it is one relational outcome.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that Dataset A (5,000 records) is complete: deduplication and standardization done with no unresolved blocking errors.
  Rationale: Completed work.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that Dataset B (8,000 records) is 60 percent cleaned, with remaining older entries having inconsistent dates and missing category labels.
  Rationale: Work in progress.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that statistical analysis cannot start until both datasets pass the same validation rules.
  Rationale: The key dependency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): State that preliminary descriptive results on Dataset A only must not be presented as final results.
  Rationale: A presentation constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical, identified-ambiguity-or-boundary): State the schedule risk: one of two analysts is unavailable tomorrow, no extra analyst is assigned, and the Friday cleaning target may slip, delaying Monday analysis by at least one business day.
  Rationale: Schedule risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): State that the report deadline remains next Thursday at noon and that the visualization specialist needs validated tables 24 hours before.
  Rationale: Downstream deadlines.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (supporting; ordinary, outside prespecified sample): State that the project manager needs a status by 3:00 PM Friday on whether Monday analysis is realistic.
  Rationale: Reporting requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-08** (critical; all-critical): Describe the time needed to fix the remaining records as uncertain, without inventing a completion estimate.
  Rationale: Explicit instruction.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Extended-context task. Inventing a completion time would fail RIU-08 and CHECK-01. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH013

technical_troubleshooting; easy.

### en

A user can open websites by IP address but not by domain name. Explain the most likely issue and the checks you would make.

### bn

একজন ব্যবহারকারী আইপি অ্যাড্রেস দিয়ে ওয়েবসাইট খুলতে পারছেন, কিন্তু ডোমেইন নাম দিয়ে পারছেন না। সবচেয়ে সম্ভাব্য সমস্যাটি কী এবং আপনি কী কী পরীক্ষা করবেন তা ব্যাখ্যা করুন।

### bn_cs

একজন user IP address দিয়ে website খুলতে পারছেন, কিন্তু domain name দিয়ে পারছেন না। সবচেয়ে সম্ভাব্য issue-টা কী এবং আপনি কী কী check করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify DNS resolution as the most likely issue.
  Rationale: The key inference.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Check the configured DNS servers on the device or router.
  Rationale: Next check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Test resolution with a tool such as nslookup or by trying a known public DNS server.
  Rationale: Confirms the diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Flush the DNS cache or check the hosts file.
  Rationale: Local causes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Check whether other devices on the network are affected to separate device from network.
  Rationale: Isolation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH019

technical_troubleshooting; hard.

### en

A remote employee's VPN connects successfully but some internal resources are unreachable. Explain how to distinguish split-tunneling, DNS, route, access-control, and application-level causes.

### bn

দূর থেকে কাজ করা একজন কর্মীর ভিপিএন সফলভাবে যুক্ত হচ্ছে, কিন্তু কিছু অভ্যন্তরীণ রিসোর্সে পৌঁছানো যাচ্ছে না। স্প্লিট টানেলিং, ডিএনএস, রুট, অ্যাক্সেস নিয়ন্ত্রণ এবং অ্যাপ্লিকেশন স্তরের কারণগুলোর মধ্যে কীভাবে পার্থক্য করবেন তা ব্যাখ্যা করুন।

### bn_cs

remote-এ কাজ করা একজন employee-র VPN সফলভাবে connect হচ্ছে, কিন্তু কিছু internal resource-এ reach করা যাচ্ছে না। split-tunneling, DNS, route, access-control আর application-level কারণগুলো কীভাবে distinguish করবেন explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Check split-tunnel configuration for whether the unreachable networks are included in the tunnel.
  Rationale: Named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Test name resolution of the internal resources over the VPN.
  Rationale: Named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Inspect the client routing table for routes to the resources.
  Rationale: Named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Check firewall or access-control rules for the user's VPN group.
  Rationale: Named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Test whether the host is reachable while the application fails, indicating an application-level cause.
  Rationale: Named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Explain how a possible result favors or weakens a named cause relative to others.
  Rationale: Without interpretation the answer does not distinguish causes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without result interpretation.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Follows the accepted convention. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH027

technical_troubleshooting; medium.

### en

A web application becomes slow only after a user has been logged in for several hours. Describe evidence that could distinguish client-side memory growth, session issues, network degradation, and server-side load.

### bn

একটি ওয়েব অ্যাপ্লিকেশন কেবল তখনই ধীর হয়ে যায়, যখন ব্যবহারকারী কয়েক ঘণ্টা ধরে লগইন অবস্থায় থাকেন। ক্লায়েন্ট-সাইডে মেমরি বেড়ে যাওয়া, সেশন-সংক্রান্ত সমস্যা, নেটওয়ার্কের মান কমে যাওয়া এবং সার্ভার-সাইডের লোড—এগুলোর মধ্যে পার্থক্য করতে পারে এমন প্রমাণ বর্ণনা করুন।

### bn_cs

একটি web application শুধু তখনই slow হয়ে যায়, যখন user কয়েক ঘণ্টা ধরে logged in থাকেন। client-side memory growth, session issue, network degradation আর server-side load—এগুলোর মধ্যে পার্থক্য করতে পারে এমন প্রমাণ describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Monitor browser memory over time to detect client-side memory growth.
  Rationale: Named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Test whether logging out and in or refreshing the session restores speed.
  Rationale: Named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Measure network latency over time or compare on another network.
  Rationale: Named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check server metrics and whether other users are slow at the same time.
  Rationale: Named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Explain how a possible result favors one named cause over another.
  Rationale: The prompt asks to distinguish causes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists evidence without explaining which result points where.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH047

technical_troubleshooting; medium.

### en

A scheduled job runs correctly when started manually but fails overnight. Describe how you would investigate environment, permissions, working directory, timing, and external dependencies.

### bn

নির্ধারিত সময়ে স্বয়ংক্রিয়ভাবে চলার কথা এমন একটি কাজ ম্যানুয়ালি চালু করলে ঠিকভাবে চলে, কিন্তু রাতে চলার সময় ব্যর্থ হয়। এনভায়রনমেন্ট, অনুমতি, ওয়ার্কিং ডিরেক্টরি, সময় এবং বাইরের ডিপেন্ডেন্সি কীভাবে খতিয়ে দেখবেন তা বর্ণনা করুন।

### bn_cs

নির্ধারিত সময়ে চলার কথা এমন একটি job manually চালু করলে ঠিকভাবে চলে, কিন্তু রাতে চলার সময় fail করে। environment, permission, working directory, timing আর external dependency কীভাবে খতিয়ে দেখবেন তা describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Compare the scheduler's environment variables and PATH with the interactive shell.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check that the scheduled job's account has the needed permissions.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check that the job does not depend on a relative working directory.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check timing issues such as overlapping jobs, maintenance windows or time-zone settings.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Check external dependencies available at night, such as network shares, databases or APIs.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Use the job's logs or a controlled scheduled run to explain how a possible result favors or weakens a named cause.
  Rationale: Turns checks into diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Mentions logs or a test run but gives no result interpretation.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH077

technical_troubleshooting; medium.

### en

A mobile device receives calls but cannot send text messages after changing carriers. Explain what account, network, messaging, and device settings should be checked.

### bn

মোবাইল অপারেটর বদলানোর পর একটি ফোনে কল আসছে, কিন্তু টেক্সট মেসেজ পাঠানো যাচ্ছে না। অ্যাকাউন্ট, নেটওয়ার্ক, মেসেজিং এবং ডিভাইসের সেটিংসের কোন কোন বিষয় চেক করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

carrier বদলানোর পর একটি mobile device-এ call receive করা যাচ্ছে, কিন্তু text message পাঠানো যাচ্ছে না। account, network, messaging আর device settings-এর কোন কোন বিষয় check করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Check the account with the new carrier, such as SMS service activation and completed number porting.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check network settings such as carrier settings updates or APN.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check the message center (SMSC) number or messaging app settings, including disabling previous-carrier messaging features such as iMessage or RCS linked to the old setup.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Check device settings such as SIM recognition or a restart after the change.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Explain how a possible result, such as texts failing only to certain recipients, points to a specific cause.
  Rationale: Turns checks into diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without any result interpretation.

Draft notes: P06 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
