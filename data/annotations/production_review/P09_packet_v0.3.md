# P09 independent review packet

Status: pending. AI-produced draft annotations; no human acceptance is claimed.

Each task needs bilingual equivalence and full-prompt coverage review. Review all critical units, all ambiguity/boundary questions below, and every prespecified ordinary sample item. Additional ordinary units may be reviewed. Blank identity/decision fields are intentional.

24 tasks; 119 RIUs; 55 critical; 21 ordinary sample units; 76 mandatory unit reviews.

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

## CYBER032

cybersecurity_digital_safety; easy.

### en

A user wants to use public Wi-Fi for online banking. Explain the risks and safer alternatives.

### bn

একজন ব্যবহারকারী অনলাইন ব্যাংকিংয়ের জন্য পাবলিক ওয়াই-ফাই ব্যবহার করতে চান। এর ঝুঁকিগুলো এবং আরও নিরাপদ বিকল্পগুলো ব্যাখ্যা করুন।

### bn_cs

একজন user online banking-এর জন্য public Wi-Fi ব্যবহার করতে চান। এর risk-গুলো আর আরও safe alternative-গুলো explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain the risk of fake or rogue hotspots and interception on shared networks.
  Rationale: The core risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Explain that HTTPS protects traffic content but certificate warnings or fake sites remain risks.
  Rationale: Calibrates the risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Recommend a safer alternative such as mobile data or a personal hotspot.
  Rationale: The core alternative.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Recommend the bank's official app, verifying the network name and never ignoring certificate warnings.
  Rationale: Additional safeguards.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Recommend MFA and logging out afterwards.
  Rationale: Account protection.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. A trusted VPN is an acceptable alternative. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER039

cybersecurity_digital_safety; hard.

### en

A security team sees intermittent encrypted outbound connections from a server that normally should communicate only internally. Explain how to investigate the behavior without assuming it is malicious.

### bn

একটি সিকিউরিটি টিম দেখছে, যে সার্ভারের সাধারণত শুধু অভ্যন্তরীণ যোগাযোগ করার কথা, সেটি থেকে মাঝে মাঝে বাইরের দিকে এনক্রিপ্টেড সংযোগ যাচ্ছে। আচরণটিকে ক্ষতিকর ধরে না নিয়ে কীভাবে তদন্ত করবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি security team দেখছে, যে server-এর সাধারণত শুধু internally communicate করার কথা, সেটা থেকে মাঝে মাঝে encrypted outbound connection যাচ্ছে। behavior-টাকে malicious ধরে না নিয়ে কীভাবে investigate করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify the destination, ports, timing pattern and data volume of the connections.
  Rationale: Characterizes the behavior.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Identify the process or service on the server making the connections.
  Rationale: Links behavior to software.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check for legitimate explanations, such as updates, licensing, telemetry or recent changes, with system owners.
  Rationale: Avoids assuming malice.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Check threat intelligence or reputation for the destinations and look for other compromise indicators.
  Rationale: Tests the malicious hypothesis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Explain how a possible result favors a legitimate or malicious explanation.
  Rationale: Turns evidence into a conclusion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without result interpretation.
- [ ] **RIU-06** (critical; all-critical): Contain or block the traffic if it cannot be explained, preserving evidence.
  Rationale: Limits possible exfiltration.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER067

cybersecurity_digital_safety; medium.

### en

A security review finds that logging is enabled in the cloud but important administrative events are not being retained long enough. Explain how retention should be designed.

### bn

একটি সিকিউরিটি রিভিউয়ে দেখা গেছে, ক্লাউডে লগিং চালু আছে, কিন্তু গুরুত্বপূর্ণ প্রশাসনিক ইভেন্টগুলো যথেষ্ট দিন সংরক্ষণ করা হচ্ছে না। লগ রিটেনশন কীভাবে ডিজাইন করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি security review-তে দেখা গেছে, cloud-এ logging enabled আছে, কিন্তু গুরুত্বপূর্ণ administrative event-গুলো যথেষ্ট দিন retain করা হচ্ছে না। retention কীভাবে design করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Set retention based on investigation needs and legal or compliance requirements, long enough to cover incidents discovered late.
  Rationale: Core design principle.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Store logs in a protected, tamper-resistant location separate from the systems they record, such as a separate account or immutable storage.
  Rationale: Prevents attackers deleting evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Prioritize longer retention for high-value administrative events than for routine logs.
  Rationale: Tiered retention.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Use cheaper archival tiers for older logs.
  Rationale: Cost control.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Restrict access to logs and test that they can be retrieved.
  Rationale: Usability and protection.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. No specific number of days required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER088

cybersecurity_digital_safety; medium.

### en

A company wants to combine data from several internal systems to build employee-risk profiles. Explain the privacy, fairness, access, retention, and governance questions that should be resolved first.

### bn

একটি প্রতিষ্ঠান কয়েকটি অভ্যন্তরীণ সিস্টেমের ডেটা একত্র করে কর্মীদের ঝুঁকি-প্রোফাইল তৈরি করতে চায়। প্রাইভেসি, ন্যায্যতা, অ্যাক্সেস, সংরক্ষণের মেয়াদ এবং গভর্নেন্স নিয়ে কোন কোন প্রশ্নের সমাধান আগে করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি company কয়েকটি internal system-এর data একত্র করে employee-risk profile তৈরি করতে চায়। privacy, fairness, access, retention আর governance নিয়ে কোন কোন প্রশ্নের সমাধান আগে করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Ask whether combining the data has a legitimate, defined purpose and is proportionate, considering the privacy intrusion.
  Rationale: Named privacy question.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Ask how profiles could be unfair or biased, and whether employees can contest decisions based on them.
  Rationale: Named fairness question.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Ask who can access the profiles and for what decisions.
  Rationale: Named access question.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Ask how long profiles are kept and when they are deleted.
  Rationale: Named retention question.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Ask who governs the program, such as oversight, approval and legal review.
  Rationale: Named governance question.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER097

cybersecurity_digital_safety; medium.

### en

A help desk receives frequent requests to bypass authentication controls for convenience. Explain how staff should handle these requests consistently and safely.

### bn

একটি হেল্প ডেস্কে প্রায়ই সুবিধার জন্য অথেনটিকেশন নিয়ন্ত্রণ এড়িয়ে যাওয়ার অনুরোধ আসে। কর্মীদের কীভাবে এসব অনুরোধ ধারাবাহিকভাবে ও নিরাপদে সামলানো উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি help desk-এ প্রায়ই convenience-এর জন্য authentication control bypass করার request আসে। staff-দের কীভাবে এসব request consistently আর safely handle করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Do not bypass authentication controls for convenience; following the documented process complies.
  Rationale: Bypasses enable social engineering.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Use a documented, consistent procedure with identity verification for any legitimate exception.
  Rationale: Consistency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Escalate unusual or pressured requests and log them.
  Rationale: Detects social engineering.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Offer legitimate alternatives such as account recovery or easier MFA methods.
  Rationale: Addresses convenience needs.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Review the frequency of requests to identify usability problems to fix.
  Rationale: Root cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC005

decision_support; medium.

### en

A project has four unfinished tasks before launch: documentation, one minor bug, a security review, and performance testing. Explain how you would decide the order rather than simply following the task list.

### bn

চালু করার আগে একটি প্রজেক্টে চারটি কাজ বাকি: ডকুমেন্টেশন, একটি ছোট বাগ, একটি নিরাপত্তা পর্যালোচনা এবং পারফরম্যান্স টেস্টিং। কাজের তালিকার ক্রম অন্ধভাবে না মেনে কীভাবে ক্রম ঠিক করবেন তা ব্যাখ্যা করুন।

### bn_cs

launch-এর আগে একটি project-এ চারটি কাজ বাকি: documentation, একটি minor bug, একটি security review আর performance testing। task list-এর ক্রম অন্ধভাবে না মেনে কীভাবে order ঠিক করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Prioritize by risk to the launch, such as placing the security review early because its findings may require changes.
  Rationale: Core ordering logic.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Place performance testing early enough to fix problems it finds.
  Rationale: Ordering logic.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Assess the minor bug's impact before deciding its order.
  Rationale: Ordering logic.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Do documentation in parallel or later since it depends on final behavior.
  Rationale: Ordering logic.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Consider dependencies, effort and who is available.
  Rationale: Additional factors.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Defensible alternative orders are acceptable with risk-based justification. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC013

decision_support; easy.

### en

A team needs a 45-minute meeting this week but no time works for everyone. Explain how to choose a time fairly.

### bn

একটি টিমের এই সপ্তাহে ৪৫ মিনিটের একটি মিটিং দরকার, কিন্তু এমন কোনো সময় নেই যা সবার জন্য সুবিধাজনক। ন্যায্যভাবে কীভাবে সময় বেছে নেবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি team-এর এই সপ্তাহে ৪৫ মিনিটের একটি meeting দরকার, কিন্তু এমন কোনো time নেই যেটা সবার জন্য কাজ করে। fairly কীভাবে time বেছে নেবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify who is essential and prioritize their availability.
  Rationale: Core criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Choose the time that excludes the fewest essential people.
  Rationale: Selection rule.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Provide a way for those who cannot attend to contribute, such as a recording, notes or input in advance.
  Rationale: Fairness for those excluded.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Rotate inconvenient times across meetings if this recurs.
  Rationale: Fairness over time.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC015

decision_support; medium.

### en

A project plan has tasks A, B, C, and D. B depends on A, D depends on both B and C, and only two people are available. Explain how to sequence the work efficiently.

### bn

একটি প্রজেক্ট পরিকল্পনায় A, B, C এবং D—এই চারটি কাজ আছে। B নির্ভর করে A-এর ওপর, D নির্ভর করে B ও C দুটোর ওপর, এবং কাজ করার মতো মাত্র দুজন মানুষ আছেন। কাজগুলো দক্ষতার সঙ্গে কোন ক্রমে সাজাবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি project plan-এ A, B, C আর D—এই চারটি task আছে। B depend করে A-এর ওপর, D depend করে B আর C দুটোর ওপর, এবং কাজ করার মতো মাত্র দুজন মানুষ আছেন। কাজগুলো efficiently কোন sequence-এ সাজাবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Start A and C in parallel with the two people, since neither has a dependency.
  Rationale: Efficient start.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Do B after A finishes.
  Rationale: Dependency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Do D only after both B and C finish.
  Rationale: Dependency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Note that the A–B path is likely the critical path and durations would refine the plan.
  Rationale: Efficiency insight.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC020

decision_support; hard.

### en

A maintenance task requires two hours of downtime but the system supports users in multiple regions. Propose how to choose a maintenance window using usage data, risk, staffing, communication, and rollback needs.

### bn

একটি রক্ষণাবেক্ষণের কাজে দুই ঘণ্টা ডাউনটাইম লাগবে, কিন্তু সিস্টেমটি একাধিক অঞ্চলের ব্যবহারকারীদের সেবা দেয়। ব্যবহারের ডেটা, ঝুঁকি, জনবল, যোগাযোগ এবং রোলব্যাকের প্রয়োজন বিবেচনা করে রক্ষণাবেক্ষণের সময় কীভাবে বেছে নেবেন তা প্রস্তাব করুন।

### bn_cs

একটি maintenance task-এ দুই ঘণ্টা downtime লাগবে, কিন্তু system-টা একাধিক region-এর user-দের সেবা দেয়। usage data, risk, staffing, communication আর rollback-এর প্রয়োজন বিবেচনা করে maintenance window কীভাবে বেছে নেবেন তা propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Use usage data across regions to find the lowest combined-impact window.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Consider risk, such as avoiding peak business periods or month-end in any region.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Ensure skilled staff are available during and after the window.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Communicate the window in advance to users in each region in their local time.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Plan rollback time within or near the window, such as reserving time to restore service if maintenance fails.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC096

decision_support; medium.

### en

A manager must choose between acting now on a moderate risk or waiting two weeks for better information. Explain how reversibility, consequence severity, and information value should influence the choice.

### bn

একজন ম্যানেজারকে মাঝারি মাত্রার একটি ঝুঁকির ক্ষেত্রে এখনই ব্যবস্থা নেওয়া, অথবা আরও ভালো তথ্যের জন্য দুই সপ্তাহ অপেক্ষা করা—এর মধ্যে বেছে নিতে হবে। সিদ্ধান্ত ফিরিয়ে নেওয়ার সুযোগ, পরিণতির গুরুতরতা এবং তথ্যের মূল্য কীভাবে এই বাছাইকে প্রভাবিত করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একজন manager-কে moderate একটি risk-এর ক্ষেত্রে এখনই action নেওয়া, অথবা আরও ভালো information-এর জন্য দুই সপ্তাহ অপেক্ষা করা—এর মধ্যে বেছে নিতে হবে। reversibility, consequence severity আর information value কীভাবে এই choice-কে influence করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that reversible actions favor acting now while irreversible ones favor waiting for information.
  Rationale: Named factor with direction.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Explain that severe consequences of the risk materializing during two weeks favor acting now.
  Rationale: Named factor with direction.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Explain that waiting is worthwhile only if the new information could change the decision.
  Rationale: Named factor with direction.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Consider interim measures that reduce risk while waiting.
  Rationale: Combines options.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC033

procedural_instructional; easy.

### en

Explain how to label and store household documents so important records can be found quickly.

### bn

গুরুত্বপূর্ণ রেকর্ড যেন দ্রুত খুঁজে পাওয়া যায়, সেজন্য সংসারের কাগজপত্র কীভাবে লেবেল দিয়ে সংরক্ষণ করবেন তা ব্যাখ্যা করুন।

### bn_cs

গুরুত্বপূর্ণ record যেন দ্রুত খুঁজে পাওয়া যায়, সেজন্য household document-গুলো কীভাবে label করে store করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Group documents into clear categories, such as identity, finance, property, medical and insurance.
  Rationale: Organization.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Label folders clearly, including dates or years where relevant.
  Rationale: Labeling.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Keep vital originals, such as passports and deeds, in a secure, protected place.
  Rationale: Protection of critical records.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Keep an index or digital copies of important documents.
  Rationale: Retrieval and backup.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Review and discard outdated documents periodically.
  Rationale: Maintenance.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC040

procedural_instructional; hard.

### en

A family needs to coordinate shared responsibilities among people with different schedules. Propose a procedure for assigning tasks, handling changes, and preventing work from silently going undone.

### bn

একটি পরিবারের সদস্যদের সময়সূচি আলাদা, অথচ তাঁদের যৌথ দায়িত্বগুলো সমন্বয় করতে হবে। কাজ ভাগ করা, পরিবর্তন সামলানো এবং কোনো কাজ যেন নিঃশব্দে অসম্পূর্ণ পড়ে না থাকে তা নিশ্চিত করার একটি পদ্ধতি প্রস্তাব করুন।

### bn_cs

একটি পরিবারের সদস্যদের schedule আলাদা, অথচ তাঁদের shared responsibility-গুলো coordinate করতে হবে। task assign করা, change handle করা আর কোনো কাজ যেন নিঃশব্দে অসম্পূর্ণ পড়ে না থাকে তা নিশ্চিত করার একটি procedure propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Assign each task to a named person with a due date or frequency in a shared list or calendar.
  Rationale: Assignment.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Require people to hand off or reassign a task explicitly when they cannot do it.
  Rationale: Handles changes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Mark tasks done and review the list regularly so undone tasks are visible.
  Rationale: Prevents silent failures.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Consider each person's schedule when assigning.
  Rationale: Feasibility.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC048

procedural_instructional; medium.

### en

A traveler has a tight international connection involving a terminal change. Explain how to prepare in advance and what sequence of checks to make on the travel day.

### bn

একজন যাত্রীর আন্তর্জাতিক যাত্রায় খুব অল্প সময়ের একটি কানেক্টিং ফ্লাইট আছে, যেখানে টার্মিনাল বদলাতে হবে। আগে থেকে কীভাবে প্রস্তুতি নেবেন এবং যাত্রার দিন কোন ক্রমে কী কী যাচাই করবেন তা ব্যাখ্যা করুন।

### bn_cs

একজন traveler-এর international trip-এ খুব tight একটি connection আছে, যেখানে terminal change করতে হবে। আগে থেকে কীভাবে prepare করবেন এবং travel-এর দিন কোন sequence-এ কী কী check করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check in advance whether the connection meets the airport's minimum connection time and how to change terminals.
  Rationale: Feasibility.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check whether immigration, customs or security rescreening is needed in transit.
  Rationale: Transit requirements.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Choose a seat near the front and keep baggage to carry-on if possible.
  Rationale: Speed.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): On the day, check flight status and the connecting gate as soon as possible after landing.
  Rationale: Day-of check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Know the rebooking options if the connection is missed, such as whether flights are on one ticket.
  Rationale: Contingency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC068

procedural_instructional; medium.

### en

A one-day conference has parallel sessions, shared rooms, volunteers, catering, and last-minute speaker changes. Design an operational procedure for coordination and escalation.

### bn

একদিনের একটি সম্মেলনে সমান্তরাল সেশন, ভাগাভাগি করে ব্যবহৃত কক্ষ, স্বেচ্ছাসেবক, খাবার পরিবেশন এবং শেষ মুহূর্তে বক্তা পরিবর্তনের মতো বিষয় আছে। সমন্বয় ও এস্কেলেশনের জন্য একটি পরিচালনাগত পদ্ধতি তৈরি করুন।

### bn_cs

একদিনের একটি conference-এ parallel session, ভাগাভাগি করা room, volunteer, খাবারের ব্যবস্থা আর শেষ মুহূর্তে speaker বদলের মতো বিষয় আছে। সমন্বয় আর escalation-এর জন্য একটি operational procedure তৈরি করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Designate a central coordinator or control point and a communication channel for staff and volunteers.
  Rationale: Coordination.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Define an escalation path for problems, including who decides on what.
  Rationale: Escalation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Assign volunteers to rooms or roles with briefings.
  Rationale: Volunteers.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Coordinate catering timing with the session schedule.
  Rationale: Catering.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Have a process for last-minute speaker changes, including updating schedules and signage.
  Rationale: Speaker changes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Manage shared rooms with turnover checks between sessions.
  Rationale: Shared rooms.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC097

procedural_instructional; medium.

### en

A shared online service becomes unavailable during an important work period. Explain how a team should switch to a temporary fallback while preserving work for later reconciliation.

### bn

গুরুত্বপূর্ণ কাজের সময়ে একটি শেয়ার করা অনলাইন সার্ভিস অনুপলব্ধ হয়ে গেছে। পরে মিলিয়ে নেওয়ার জন্য কাজ সংরক্ষণ করে রেখে একটি টিম কীভাবে সাময়িক বিকল্প ব্যবস্থায় চলে যাবে তা ব্যাখ্যা করুন।

### bn_cs

গুরুত্বপূর্ণ কাজের সময়ে একটি shared online service unavailable হয়ে গেছে। পরে reconcile করার জন্য কাজ সংরক্ষণ করে রেখে একটি team কীভাবে temporary fallback-এ switch করবে তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Announce the outage and the fallback method to the team.
  Rationale: Coordination.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Record work done during the outage in a structured, time-stamped way, such as a shared document with who did what.
  Rationale: Preserves work.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Avoid duplicate work by assigning ownership during the fallback.
  Rationale: Coordination.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Reconcile fallback work into the service after recovery and verify nothing is lost or duplicated.
  Rationale: Explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Check the service status and expected recovery time.
  Rationale: Situational awareness.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN010

information_synthesis; hard.

### en

Create a balanced summary: System uptime improved from 98.7 to 99.4 percent after migration. Monthly infrastructure cost rose 22 percent. Major incidents decreased from four to one. The comparison covers only six months before and six months after migration.

### bn

একটি ভারসাম্যপূর্ণ সারাংশ তৈরি করুন: মাইগ্রেশনের পর সিস্টেমের আপটাইম ৯৮.৭ থেকে বেড়ে ৯৯.৪ শতাংশ হয়েছে। মাসিক ইনফ্রাস্ট্রাকচার খরচ ২২ শতাংশ বেড়েছে। বড় ধরনের ঘটনা চারটি থেকে কমে একটিতে নেমেছে। তুলনাটি শুধু মাইগ্রেশনের আগের ছয় মাস এবং পরের ছয় মাসের ওপর ভিত্তি করে।

### bn_cs

একটি balanced summary তৈরি করুন: migration-এর পর system uptime ৯৮.৭ থেকে বেড়ে ৯৯.৪ শতাংশ হয়েছে। monthly infrastructure cost ২২ শতাংশ বেড়েছে। major incident চারটি থেকে কমে একটিতে নেমেছে। comparison-টা শুধু migration-এর আগের ছয় মাস আর পরের ছয় মাস cover করে।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that uptime improved from 98.7 to 99.4 percent.
  Rationale: Benefit.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that monthly infrastructure cost rose 22 percent.
  Rationale: Cost.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that major incidents fell from four to one.
  Rationale: Benefit.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): State that the comparison covers only six months before and after.
  Rationale: Limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN026

information_synthesis; medium.

### en

Summarize the incident timeline and calculate the total service disruption: Error first detected at 1:40 PM. Service became unavailable at 1:47 PM. Partial recovery occurred at 2:12 PM. Full service returned at 2:31 PM.

### bn

ঘটনার সময়রেখা সংক্ষেপ করুন এবং সার্ভিস মোট কতক্ষণ ব্যাহত ছিল তা হিসাব করুন: এরর প্রথম ধরা পড়ে দুপুর ১টা ৪০ মিনিটে। সার্ভিস অনুপলব্ধ হয়ে যায় দুপুর ১টা ৪৭ মিনিটে। আংশিক পুনরুদ্ধার হয় দুপুর ২টা ১২ মিনিটে। পূর্ণ সার্ভিস ফিরে আসে দুপুর ২টা ৩১ মিনিটে।

### bn_cs

incident timeline summarize করুন এবং total service disruption কতক্ষণ ছিল তা calculate করুন: error প্রথম detect হয় দুপুর ১টা ৪০ মিনিটে। service unavailable হয়ে যায় দুপুর ১টা ৪৭ মিনিটে। partial recovery হয় দুপুর ২টা ১২ মিনিটে। full service ফিরে আসে দুপুর ২টা ৩১ মিনিটে।

### Boundary and ambiguity questions

- [ ] RIU-02: Accept 51 minutes only if explicitly defined as from first detection.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): List the events in order with their times.
  Rationale: Timeline.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Calculate the disruption from unavailability at 1:47 PM to full service at 2:31 PM as 44 minutes.
  Rationale: The requested calculation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Distinguish full unavailability (1:47–2:12, 25 minutes) from partial service (2:12–2:31, 19 minutes).
  Rationale: Precision.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Note that the error was detected seven minutes before the service became unavailable.
  Rationale: Context.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. An answer counting from 1:40 PM (51 minutes) must explain that it includes the pre-outage error period. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN056

information_synthesis; medium.

### en

A user says a system was unavailable for an hour. Monitoring shows a 12-minute outage. Support logs show intermittent errors for 47 minutes. Summarize these perspectives without collapsing them into one number.

### bn

একজন ব্যবহারকারী বলছেন সিস্টেমটি এক ঘণ্টা অনুপলব্ধ ছিল। মনিটরিংয়ে দেখা যাচ্ছে ১২ মিনিটের একটি বিভ্রাট। সাপোর্ট লগে ৪৭ মিনিট ধরে মাঝে মাঝে এরর দেখা গেছে। এগুলোকে একটি সংখ্যায় মিশিয়ে না ফেলে ভিন্ন ভিন্ন দৃষ্টিকোণগুলো সংক্ষেপ করুন।

### bn_cs

একজন user বলছেন system-টা এক ঘণ্টা unavailable ছিল। monitoring-এ দেখা যাচ্ছে ১২ মিনিটের একটি outage। support log-এ ৪৭ মিনিট ধরে intermittent error দেখা গেছে। এগুলোকে একটি number-এ মিশিয়ে না ফেলে আলাদা আলাদা perspective summarize করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Attribute the one-hour unavailability to the user's report.
  Rationale: Perspective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Attribute the 12-minute outage to monitoring.
  Rationale: Perspective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Attribute 47 minutes of intermittent errors to support logs.
  Rationale: Perspective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Do not merge them into one duration; explaining that they measure different things complies.
  Rationale: Explicit constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN072

information_synthesis; easy.

### en

Select an option that satisfies all requirements: Option A costs $80 and arrives Friday. Option B costs $60 and arrives Monday. Budget is $75 and the item is needed by Saturday.

### bn

সব শর্ত পূরণ করে এমন একটি বিকল্প বেছে নিন: বিকল্প A-এর দাম ৮০ ডলার এবং এটি শুক্রবার পৌঁছাবে। বিকল্প B-এর দাম ৬০ ডলার এবং এটি সোমবার পৌঁছাবে। বাজেট ৭৫ ডলার এবং জিনিসটি শনিবারের মধ্যে দরকার।

### bn_cs

সব requirement পূরণ করে এমন একটি option select করুন: Option A-এর দাম ৮০ ডলার এবং এটা শুক্রবার পৌঁছাবে। Option B-এর দাম ৬০ ডলার এবং এটা সোমবার পৌঁছাবে। budget ৭৫ ডলার এবং item-টা শনিবারের মধ্যে দরকার।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that Option A exceeds the $75 budget at $80.
  Rationale: Constraint check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that Option B arrives Monday, after the Saturday need date.
  Rationale: Constraint check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Conclude that neither option satisfies all requirements.
  Rationale: The correct answer.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Suggest a next step, such as seeking another option or relaxing a constraint with approval.
  Rationale: Useful.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Choosing A or B as satisfying all requirements is incorrect. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN096

information_synthesis; medium.

### en

Create a decision brief that compares the available procurement options against the stated constraints rather than simply selecting the option with the most features. Option A costs $20,000, can be deployed in two weeks, supports all mandatory requirements, and lacks one preferred reporting feature. The vendor says that preferred feature may be added later, but no date is committed. Option B costs $28,000, includes all mandatory and preferred features, and requires approximately six weeks for deployment. Option C costs $23,500 and could be deployed in four weeks, but one mandatory integration is currently available only through a beta connector. The approved project budget is capped at $25,000 unless a vice president authorizes an exception. The preferred reporting feature is explicitly classified as desirable rather than mandatory. The current system can remain in service for two more months, although support tickets have increased by 15 percent during the past quarter. A separate security review found no critical findings for A or B; C's beta connector has not yet completed the organization's security review. Procurement reports that Vendor A offers a one-year price guarantee, Vendor B offers three years, and Vendor C has not committed to future pricing. The operations team prefers deployment within one month but has said six weeks is tolerable if there is a strong justification. No option has yet been tested with the organization's full production data volume. The brief should identify which constraints each option satisfies or violates, distinguish mandatory requirements from preferences, and identify unresolved evidence that a decision-maker should consider before approval.

### bn

সবচেয়ে বেশি ফিচারযুক্ত বিকল্পটি সরাসরি বেছে না নিয়ে, উল্লেখিত শর্তগুলোর আলোকে উপলব্ধ ক্রয়-বিকল্পগুলোর তুলনা করে একটি সিদ্ধান্ত-ব্রিফ তৈরি করুন। বিকল্প A-এর খরচ ২০,০০০ ডলার, দুই সপ্তাহে ডিপ্লয় করা যায়, সব বাধ্যতামূলক চাহিদা পূরণ করে, কিন্তু একটি পছন্দনীয় রিপোর্টিং ফিচার নেই। ভেন্ডর বলছে, সেই পছন্দনীয় ফিচারটি পরে যোগ করা হতে পারে, তবে কোনো তারিখের প্রতিশ্রুতি দেওয়া হয়নি। বিকল্প B-এর খরচ ২৮,০০০ ডলার, এতে সব বাধ্যতামূলক ও পছন্দনীয় ফিচার আছে, এবং ডিপ্লয় করতে প্রায় ছয় সপ্তাহ লাগে। বিকল্প C-এর খরচ ২৩,৫০০ ডলার এবং চার সপ্তাহে ডিপ্লয় করা যেতে পারে, কিন্তু একটি বাধ্যতামূলক ইন্টিগ্রেশন বর্তমানে শুধু একটি বেটা কানেক্টরের মাধ্যমে পাওয়া যায়। কোনো ভাইস প্রেসিডেন্ট ব্যতিক্রম অনুমোদন না করলে অনুমোদিত প্রজেক্ট বাজেটের সর্বোচ্চ সীমা ২৫,০০০ ডলার। পছন্দনীয় রিপোর্টিং ফিচারটিকে স্পষ্টভাবে কাঙ্ক্ষিত হিসেবে শ্রেণিভুক্ত করা হয়েছে, বাধ্যতামূলক হিসেবে নয়। বর্তমান সিস্টেমটি আরও দুই মাস চালু রাখা যাবে, যদিও গত ত্রৈমাসিকে সাপোর্ট টিকিট ১৫ শতাংশ বেড়েছে। আলাদা একটি নিরাপত্তা পর্যালোচনায় A বা B-এর ক্ষেত্রে কোনো গুরুতর সমস্যা পাওয়া যায়নি; C-এর বেটা কানেক্টরের ক্ষেত্রে প্রতিষ্ঠানের নিরাপত্তা পর্যালোচনা এখনো শেষ হয়নি। ক্রয় বিভাগ জানিয়েছে, ভেন্ডর A এক বছরের মূল্য-নিশ্চয়তা দেয়, ভেন্ডর B তিন বছরের, আর ভেন্ডর C ভবিষ্যৎ মূল্য নিয়ে কোনো প্রতিশ্রুতি দেয়নি। অপারেশনস টিম এক মাসের মধ্যে ডিপ্লয়মেন্ট পছন্দ করে, তবে জানিয়েছে যে জোরালো যুক্তি থাকলে ছয় সপ্তাহও মেনে নেওয়া যায়। কোনো বিকল্পই এখনো প্রতিষ্ঠানের পূর্ণ প্রোডাকশন ডেটা ভলিউম দিয়ে পরীক্ষা করা হয়নি। ব্রিফে দেখাতে হবে কোন বিকল্প কোন শর্ত পূরণ বা লঙ্ঘন করে, বাধ্যতামূলক চাহিদাকে পছন্দ থেকে আলাদা করতে হবে, এবং অনুমোদনের আগে সিদ্ধান্তগ্রহীতার বিবেচনা করা উচিত এমন অমীমাংসিত প্রমাণগুলো চিহ্নিত করতে হবে।

### bn_cs

সবচেয়ে বেশি feature-যুক্ত option-টা সরাসরি select না করে, stated constraint-গুলোর আলোকে available procurement option-গুলো compare করে একটি decision brief তৈরি করুন। Option A-এর খরচ ২০,০০০ ডলার, দুই সপ্তাহে deploy করা যায়, সব mandatory requirement পূরণ করে, কিন্তু একটি preferred reporting feature নেই। vendor বলছে, সেই preferred feature-টা পরে add করা হতে পারে, তবে কোনো date commit করা হয়নি। Option B-এর খরচ ২৮,০০০ ডলার, এতে সব mandatory আর preferred feature আছে, এবং deploy করতে প্রায় ছয় সপ্তাহ লাগে। Option C-এর খরচ ২৩,৫০০ ডলার এবং চার সপ্তাহে deploy করা যেতে পারে, কিন্তু একটি mandatory integration বর্তমানে শুধু একটি beta connector-এর মাধ্যমে পাওয়া যায়। কোনো vice president exception authorize না করলে approved project budget-এর সর্বোচ্চ সীমা ২৫,০০০ ডলার। preferred reporting feature-টাকে স্পষ্টভাবে desirable হিসেবে classify করা হয়েছে, mandatory হিসেবে নয়। বর্তমান system-টা আরও দুই মাস চালু রাখা যাবে, যদিও গত quarter-এ support ticket ১৫ শতাংশ বেড়েছে। আলাদা একটি security review-তে A বা B-এর ক্ষেত্রে কোনো critical finding পাওয়া যায়নি; C-এর beta connector-এর ক্ষেত্রে organization-এর security review এখনো complete হয়নি। procurement জানিয়েছে, Vendor A এক বছরের price guarantee দেয়, Vendor B তিন বছরের, আর Vendor C future pricing নিয়ে কোনো commitment দেয়নি। operations team এক মাসের মধ্যে deployment prefer করে, তবে জানিয়েছে যে strong justification থাকলে ছয় সপ্তাহও tolerable। কোনো option-ই এখনো organization-এর full production data volume দিয়ে test করা হয়নি। brief-এ দেখাতে হবে কোন option কোন constraint পূরণ বা লঙ্ঘন করে, mandatory requirement-কে preference থেকে আলাদা করতে হবে, এবং approval-এর আগে decision-maker-এর বিবেচনা করা উচিত এমন unresolved evidence identify করতে হবে।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that Option A ($20,000, two weeks) meets the budget, all mandatory requirements and the one-month preference, but lacks the preferred reporting feature with no committed date.
  Rationale: Option A assessment.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that Option B ($28,000) exceeds the $25,000 cap unless a vice president approves an exception, and its six-week deployment exceeds the preferred month but is tolerable with strong justification.
  Rationale: Option B assessment.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that Option C ($23,500, four weeks) is within budget, but a mandatory integration relies on a beta connector that has not completed security review.
  Rationale: Option C assessment.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Distinguish the reporting feature as desirable, not mandatory.
  Rationale: Explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Note price guarantees: A one year, B three years, C none.
  Rationale: Cost-risk evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Note the current system can run two more months but support tickets rose 15 percent.
  Rationale: Timing context.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (critical; all-critical): Identify unresolved evidence, including that no option has been tested at full production data volume and C's security review is pending.
  Rationale: Explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-08** (supporting; prespecified-ordinary-sample): Do not select the option with the most features merely because it has them; a constraint-based comparison complies.
  Rationale: Explicit constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Extended-context task. A recommendation is optional; if given it must respect the constraints. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH017

technical_troubleshooting; medium.

### en

Two devices on the same office network intermittently receive duplicate-IP warnings. Explain how you would confirm the conflict and identify its source without disrupting the network.

### bn

একই অফিস নেটওয়ার্কের দুটি ডিভাইসে মাঝে মাঝে ডুপ্লিকেট আইপির ওয়ার্নিং আসছে। নেটওয়ার্কে বিঘ্ন না ঘটিয়ে কীভাবে এই আইপি কনফ্লিক্ট নিশ্চিত করবেন এবং এর উৎস শনাক্ত করবেন তা ব্যাখ্যা করুন।

### bn_cs

একই office network-এর দুটি device-এ মাঝে মাঝে duplicate-IP warning আসছে। network disrupt না করে কীভাবে conflict-টা confirm করবেন এবং এর source identify করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Confirm the conflict using the ARP table or MAC addresses associated with the IP address.
  Rationale: Confirmation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Identify the conflicting device from its MAC address, such as via switch MAC tables or DHCP records.
  Rationale: Source identification.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Check for static IPs set inside the DHCP range or a second DHCP server.
  Rationale: Root cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Avoid disruptive actions such as disconnecting devices or changing network-wide settings before identifying the source; passive checks comply.
  Rationale: Explicit constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH085

technical_troubleshooting; medium.

### en

A dataset exported from one system has different row counts after import into another. Describe how to check delimiters, encoding, headers, null values, rejected rows, and duplicate handling.

### bn

একটি সিস্টেম থেকে এক্সপোর্ট করা একটি ডেটাসেট আরেকটি সিস্টেমে ইমপোর্ট করার পর সারির সংখ্যা মিলছে না। ডিলিমিটার, এনকোডিং, হেডার, নাল ভ্যালু, বাতিল হওয়া সারি এবং ডুপ্লিকেট সামলানোর পদ্ধতি কীভাবে যাচাই করবেন তা বর্ণনা করুন।

### bn_cs

একটি system থেকে export করা একটি dataset আরেকটি system-এ import করার পর row-র সংখ্যা মিলছে না। delimiter, encoding, header, null value, বাতিল হওয়া row আর duplicate handling কীভাবে check করবেন তা describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Check that the delimiter and quoting are interpreted correctly, such as commas inside fields.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check encoding mismatches that corrupt or split rows.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check whether the header row is counted or skipped consistently.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check how null or empty values are handled.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Check import logs for rejected rows.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; prespecified-ordinary-sample): Check duplicate handling, such as deduplication or key conflicts.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (critical; all-critical): Compare counts at each step or identify the missing or extra rows to explain which cause applies.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without result interpretation.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH093

technical_troubleshooting; easy.

### en

A Bluetooth mouse is paired but the pointer does not move. Explain the first troubleshooting steps.

### bn

একটি ব্লুটুথ মাউস পেয়ার করা আছে, কিন্তু পয়েন্টার নড়ছে না। সমস্যা সমাধানের প্রথম ধাপগুলো ব্যাখ্যা করুন।

### bn_cs

একটি Bluetooth mouse pair করা আছে, কিন্তু pointer নড়ছে না। প্রথম troubleshooting step-গুলো explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check the mouse battery or charge and its power switch.
  Rationale: Most common cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check whether the mouse is connected, not just paired, and reconnect it.
  Rationale: Common cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Remove and re-pair the mouse.
  Rationale: Reset.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Test the mouse on another surface or device.
  Rationale: Isolation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH100

technical_troubleshooting; hard.

### en

A shared USB-C dock works reliably with some laptops but intermittently disconnects from others. Design an investigation covering power delivery, cable capability, firmware, port standards, drivers, and workload.

### bn

যৌথভাবে ব্যবহৃত একটি ইউএসবি-সি ডক কিছু ল্যাপটপের সঙ্গে নির্ভরযোগ্যভাবে কাজ করে, কিন্তু অন্য কয়েকটির সঙ্গে মাঝে মাঝে সংযোগ বিচ্ছিন্ন হয়ে যায়। পাওয়ার ডেলিভারি, ক্যাবলের সক্ষমতা, ফার্মওয়্যার, পোর্টের স্ট্যান্ডার্ড, ড্রাইভার এবং কাজের চাপ অন্তর্ভুক্ত করে একটি অনুসন্ধান পরিকল্পনা তৈরি করুন।

### bn_cs

একটি shared USB-C dock কিছু laptop-এর সঙ্গে নির্ভরযোগ্যভাবে কাজ করে, কিন্তু অন্য কয়েকটির সঙ্গে মাঝে মাঝে disconnect হয়ে যায়। power delivery, cable capability, firmware, port standard, driver আর workload বিবেচনা করে একটি investigation design করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Check power delivery requirements of the affected laptops against the dock's output.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check cable capability, such as data and power rating.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Check and update dock and laptop firmware.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Check port standards, such as Thunderbolt versus USB-C alternate modes.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Check drivers on affected laptops.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Check whether disconnects correlate with workload, such as multiple displays or high power draw.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (critical; all-critical): Compare working and failing laptops to explain how a possible result points to a specific cause.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without result interpretation.

Draft notes: P09 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
