# P08 independent review packet

Status: pending. AI-produced draft annotations; no human acceptance is claimed.

Each task needs bilingual equivalence and full-prompt coverage review. Review all critical units, all ambiguity/boundary questions below, and every prespecified ordinary sample item. Additional ordinary units may be reviewed. Blank identity/decision fields are intentional.

24 tasks; 122 RIUs; 54 critical; 21 ordinary sample units; 75 mandatory unit reviews.

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

## CYBER053

cybersecurity_digital_safety; easy.

### en

A company employee reports that their laptop may have been stolen from a car. List the first organizational actions that should occur.

### bn

একটি কোম্পানির একজন কর্মী জানিয়েছেন, তাঁর ল্যাপটপ হয়তো গাড়ি থেকে চুরি হয়ে গেছে। প্রতিষ্ঠানের পক্ষ থেকে প্রথমে কোন কোন পদক্ষেপ নেওয়া উচিত তার তালিকা দিন।

### bn_cs

একটি company-র একজন employee জানিয়েছেন, তাঁর laptop হয়তো গাড়ি থেকে চুরি হয়ে গেছে। organization-এর পক্ষ থেকে প্রথমে কোন কোন action নেওয়া উচিত তার list দিন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Report the loss to IT or security immediately to start the incident process.
  Rationale: Starts response.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Remotely lock or wipe the device if possible, and revoke its access, sessions or certificates.
  Rationale: Limits data exposure.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Reset credentials that were stored on or used from the laptop.
  Rationale: Protects accounts.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Determine what data was on the device and whether it was encrypted, to assess notification duties.
  Rationale: Assesses impact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): File a police report and record details of the theft.
  Rationale: Often required for insurance and investigation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER060

cybersecurity_digital_safety; hard.

### en

After containing a security incident, an organization wants to return affected systems to service quickly. Explain the validation steps needed before declaring recovery complete.

### bn

একটি সিকিউরিটি ইনসিডেন্ট নিয়ন্ত্রণে আনার পর প্রতিষ্ঠানটি আক্রান্ত সিস্টেমগুলো দ্রুত আবার চালু করতে চায়। পুনরুদ্ধার সম্পূর্ণ ঘোষণা করার আগে কোন কোন যাচাই-ধাপ প্রয়োজন তা ব্যাখ্যা করুন।

### bn_cs

একটি security incident contain করার পর প্রতিষ্ঠানটি affected system-গুলো দ্রুত আবার service-এ ফেরাতে চায়। recovery সম্পূর্ণ ঘোষণা করার আগে কোন কোন validation step প্রয়োজন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Confirm the root cause and attacker access have been removed, including persistence mechanisms and compromised credentials.
  Rationale: Prevents reinfection.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Rebuild or restore systems from known-good sources or verified clean backups, and patch the exploited weakness.
  Rationale: Clean restoration.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Verify system and data integrity before returning to service.
  Rationale: Ensures correctness.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Monitor the restored systems closely for signs of renewed malicious activity.
  Rationale: Detects incomplete eradication.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Test business functionality with system owners before declaring recovery.
  Rationale: Confirms service is usable.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Obtain sign-off and document the recovery decision.
  Rationale: Accountability.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER066

cybersecurity_digital_safety; medium.

### en

A development team wants broad cloud permissions to avoid deployment failures. Explain how least privilege can be introduced without blocking legitimate work.

### bn

একটি ডেভেলপমেন্ট টিম ডিপ্লয়মেন্ট ব্যর্থ হওয়া এড়াতে বিস্তৃত ক্লাউড পারমিশন চায়। বৈধ কাজ আটকে না দিয়ে কীভাবে লিস্ট প্রিভিলেজ নীতি চালু করা যায় তা ব্যাখ্যা করুন।

### bn_cs

একটি development team deployment failure এড়াতে broad cloud permission চায়। legitimate কাজ block না করে কীভাবে least privilege চালু করা যায় তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify the permissions deployments actually use, such as from access logs or policy analysis.
  Rationale: Grounds the policy in evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Grant scoped roles for those needs rather than broad permissions.
  Rationale: Least privilege itself.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Use separate environments or roles, such as broader rights in development and narrower in production.
  Rationale: Risk-tiered access.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Provide a fast path for requesting additional permissions or temporary elevation.
  Rationale: Avoids blocking work.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Roll out gradually, such as audit-only mode before enforcement, and review periodically.
  Rationale: Reduces breakage.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER087

cybersecurity_digital_safety; medium.

### en

A smart device collects location data continuously even when the user is not actively using it. Explain what questions should be asked about necessity, consent, retention, and access.

### bn

একটি স্মার্ট ডিভাইস ব্যবহারকারী সক্রিয়ভাবে ব্যবহার না করলেও সারাক্ষণ লোকেশন ডেটা সংগ্রহ করে। প্রয়োজনীয়তা, সম্মতি, সংরক্ষণের মেয়াদ এবং অ্যাক্সেস নিয়ে কোন কোন প্রশ্ন তোলা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি smart device user active-ভাবে ব্যবহার না করলেও সারাক্ষণ location data collect করে। necessity, consent, retention আর access নিয়ে কোন কোন প্রশ্ন তোলা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Ask whether continuous collection is necessary for the device's features or whether less frequent or on-use collection would suffice.
  Rationale: Named question.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Ask whether users gave informed, specific consent and can turn collection off.
  Rationale: Named question.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Ask how long location data is retained and whether it is deleted or aggregated.
  Rationale: Named question.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Ask who can access the data, including third parties, and how it is protected.
  Rationale: Named question.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER096

cybersecurity_digital_safety; medium.

### en

A new security control causes repeated interruptions during routine work. Explain how to assess whether the control is effective, usable, and proportionate to the risk.

### bn

একটি নতুন নিরাপত্তা নিয়ন্ত্রণ দৈনন্দিন কাজে বারবার বাধা তৈরি করছে। নিয়ন্ত্রণটি কার্যকর, ব্যবহারযোগ্য এবং ঝুঁকির তুলনায় সামঞ্জস্যপূর্ণ কি না তা কীভাবে মূল্যায়ন করবেন ব্যাখ্যা করুন।

### bn_cs

একটি নতুন security control routine কাজে বারবার interruption তৈরি করছে। control-টা effective, usable এবং risk-এর তুলনায় proportionate কি না তা কীভাবে assess করবেন explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Assess effectiveness: evidence that the control reduces the targeted risk, such as blocked attacks or incidents.
  Rationale: Named criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Assess usability: measure interruptions, time lost and workarounds.
  Rationale: Named criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Assess proportionality by comparing risk reduced with operational cost.
  Rationale: Named criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Gather feedback from affected users.
  Rationale: Evidence source.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Consider adjustments that keep protection with less friction, such as tuning triggers or risk-based prompts.
  Rationale: Resolves the trade-off.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC003

decision_support; medium.

### en

A team can fix only one of three issues today: a cosmetic typo, a slow report used weekly, or a broken login affecting five users. Explain which issue should be handled first and what information could change that choice.

### bn

একটি টিম আজ তিনটি সমস্যার মধ্যে শুধু একটি ঠিক করতে পারবে: শুধু দেখতে খারাপ লাগে এমন একটি বানান ভুল, প্রতি সপ্তাহে ব্যবহৃত একটি ধীরগতির রিপোর্ট, অথবা পাঁচজন ব্যবহারকারীর ওপর প্রভাব ফেলা একটি অচল লগইন। কোন সমস্যাটি আগে সমাধান করা উচিত এবং কোন তথ্য পেলে সেই সিদ্ধান্ত বদলাতে পারে তা ব্যাখ্যা করুন।

### bn_cs

একটি team আজ তিনটি issue-র মধ্যে শুধু একটি fix করতে পারবে: একটি cosmetic typo, প্রতি সপ্তাহে ব্যবহৃত একটি slow report, অথবা পাঁচজন user-কে affect করা একটি broken login। কোন issue-টা আগে handle করা উচিত এবং কোন তথ্য পেলে সেই choice বদলাতে পারে তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01: Confirm a conditional alternative choice is not penalized when justified.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Choose the broken login first because it blocks users from working entirely.
  Rationale: The prioritization.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Identify information that could change the choice, such as the login having a workaround, the report being needed today or the typo being in a legal or public context.
  Rationale: Explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Explain why the typo is lowest priority.
  Rationale: Completes ranking.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Explain that the weekly report is slow but still usable.
  Rationale: Completes ranking.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. A different first choice is acceptable only if justified by stated conditional information. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC012

decision_support; easy.

### en

A student has two classes, a 30-minute commute, and a one-hour study block to fit between them. Explain how to choose the best study time.

### bn

একজন শিক্ষার্থীর দুটি ক্লাস আছে, ৩০ মিনিটের যাতায়াত আছে, এবং এর মাঝে এক ঘণ্টা পড়ার সময় বের করতে হবে। পড়ার জন্য সবচেয়ে ভালো সময় কীভাবে বেছে নেবেন তা ব্যাখ্যা করুন।

### bn_cs

একজন student-এর দুটি class আছে, ৩০ মিনিটের commute আছে, এবং এর মাঝে এক ঘণ্টার একটি study block fit করতে হবে। পড়ার জন্য best time কীভাবে বেছে নেবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify the available gaps after accounting for the 30-minute commute and class times.
  Rationale: Feasibility.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Choose a gap that fits a full hour, considering where the student will be.
  Rationale: Core choice.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Consider energy, focus or quiet location.
  Rationale: Quality of study time.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Consider using the commute time if feasible, such as reviewing notes on public transport.
  Rationale: Optional optimization.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Class times are not given; a method is required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC019

decision_support; hard.

### en

A conference has six speakers, two rooms, shared equipment, and three speakers with strict availability windows. Explain how to construct a schedule and resolve conflicts systematically.

### bn

একটি সম্মেলনে ছয়জন বক্তা, দুটি কক্ষ এবং ভাগাভাগি করা যন্ত্রপাতি আছে, আর তিনজন বক্তা শুধু নির্দিষ্ট কঠোর সময়ের মধ্যেই থাকতে পারবেন। কীভাবে একটি সময়সূচি তৈরি করবেন এবং পদ্ধতিগতভাবে সময়ের সংঘাত মেটাবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি conference-এ ছয়জন speaker, দুটি room আর shared equipment আছে, আর তিনজন speaker-এর strict availability window আছে। কীভাবে একটি schedule তৈরি করবেন এবং systematically conflict resolve করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Schedule the three speakers with strict availability windows first.
  Rationale: Most constrained first.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Assign rooms so no room has overlapping sessions.
  Rationale: Room constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Prevent shared-equipment conflicts, such as not scheduling two equipment-dependent sessions at the same time.
  Rationale: Equipment constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Fill remaining slots with the flexible speakers.
  Rationale: Completes the schedule.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Use a systematic conflict-resolution method, such as a grid of rooms by time and checking each constraint, then adjusting flexible items.
  Rationale: Systematic resolution.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Mentions checking for conflicts without a method.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Confirm the schedule with speakers.
  Rationale: Validation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC037

decision_support; medium.

### en

A research team has limited annotation time and a dataset of 10,000 items. Explain how to choose a subset for careful human review without simply taking the first records.

### bn

একটি গবেষক দলের অ্যানোটেশনের জন্য সময় সীমিত, আর ডেটাসেটে ১০,০০০টি আইটেম আছে। শুধু প্রথম দিকের রেকর্ডগুলো না নিয়ে কীভাবে মানুষের মাধ্যমে সতর্ক পর্যালোচনার জন্য একটি উপসেট বেছে নেবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি research team-এর annotation-এর জন্য সময় সীমিত, আর dataset-এ ১০,০০০টি item আছে। শুধু প্রথম দিকের record-গুলো না নিয়ে কীভাবে careful human review-র জন্য একটি subset বেছে নেবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Use random sampling to get a representative subset.
  Rationale: Avoids order bias.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Stratify by important categories so small groups are represented.
  Rationale: Coverage.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Explain why taking the first records is biased, such as records being ordered by time or source.
  Rationale: Explicit premise.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Consider targeted sampling of uncertain or high-risk items, kept separate from the representative sample.
  Rationale: Efficiency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Size the subset to the available time and the precision needed.
  Rationale: Feasibility.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC095

decision_support; medium.

### en

A team has incomplete evidence about whether a recurring problem is getting worse. Explain what decision can be made now, what should wait, and what additional data would reduce uncertainty.

### bn

একটি বারবার ফিরে আসা সমস্যা আরও খারাপ হচ্ছে কি না, সে বিষয়ে একটি টিমের হাতে অসম্পূর্ণ প্রমাণ আছে। এখনই কোন সিদ্ধান্ত নেওয়া যায়, কোনটির জন্য অপেক্ষা করা উচিত এবং কোন বাড়তি ডেটা অনিশ্চয়তা কমাবে তা ব্যাখ্যা করুন।

### bn_cs

একটি recurring problem আরও খারাপ হচ্ছে কি না, সে বিষয়ে একটি team-এর হাতে incomplete evidence আছে। এখনই কোন decision নেওয়া যায়, কোনটার জন্য অপেক্ষা করা উচিত এবং কোন additional data uncertainty কমাবে তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify a low-cost or reversible action that can be taken now, such as monitoring or mitigation.
  Rationale: Explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Identify which costly or irreversible decision should wait for better evidence.
  Rationale: Explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Specify additional data that would reduce uncertainty, such as consistent tracking of frequency and severity over time.
  Rationale: Explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Set a review point or trigger for revisiting the decision.
  Rationale: Closes the loop.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC032

procedural_instructional; easy.

### en

Describe a simple procedure for packing a bag for one overnight stay.

### bn

এক রাত বাইরে থাকার জন্য ব্যাগ গোছানোর একটি সহজ পদ্ধতি বর্ণনা করুন।

### bn_cs

এক রাত বাইরে থাকার জন্য bag pack করার একটি simple procedure describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Make or follow a short checklist of essentials such as clothes, toiletries, medication, phone charger and documents.
  Rationale: The core packing step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check plans or weather to adjust items.
  Rationale: Tailoring.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Pack light, such as only one change of clothes.
  Rationale: Simplicity.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Do a final check of keys, wallet, phone and charger before leaving.
  Rationale: Prevents common omissions.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC039

procedural_instructional; hard.

### en

A household wants a repeatable process for handling important incoming mail so deadlines and required responses are not missed. Design the workflow.

### bn

একটি পরিবার গুরুত্বপূর্ণ চিঠিপত্র সামলানোর একটি পুনরাবৃত্তিযোগ্য প্রক্রিয়া চায়, যাতে কোনো সময়সীমা বা প্রয়োজনীয় জবাব বাদ না পড়ে। ওয়ার্কফ্লোটি তৈরি করুন।

### bn_cs

একটি পরিবার গুরুত্বপূর্ণ incoming mail handle করার একটি repeatable process চায়, যাতে কোনো deadline বা প্রয়োজনীয় response miss না হয়। workflow-টা design করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Sort mail promptly into categories, such as action required, file and discard.
  Rationale: Intake.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Record deadlines and required responses in a calendar or list with reminders.
  Rationale: Prevents missed deadlines.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Assign responsibility within the household.
  Rationale: Ownership.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Keep a single place for pending items and a filing place for completed items.
  Rationale: Organization.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Review pending items on a regular schedule, such as weekly.
  Rationale: Repeatability.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC047

procedural_instructional; medium.

### en

Explain how to pack essential items in carry-on luggage in case checked baggage is delayed.

### bn

চেক-ইন করা লাগেজ দেরিতে পৌঁছালে যেন সমস্যা না হয়, সেজন্য দরকারি জিনিসগুলো ক্যারি-অন লাগেজে কীভাবে গুছিয়ে নেবেন তা ব্যাখ্যা করুন।

### bn_cs

checked baggage delay হলে যেন সমস্যা না হয়, সেজন্য essential item-গুলো carry-on luggage-এ কীভাবে pack করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Pack medication, travel documents and valuables in the carry-on.
  Rationale: Most critical items.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Pack a change of clothes and basic toiletries.
  Rationale: Core essentials for delay.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Pack chargers and electronics.
  Rationale: Common essentials.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Follow carry-on rules such as liquid limits.
  Rationale: Feasibility.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC067

procedural_instructional; medium.

### en

A team is collecting presentation files from multiple speakers. Explain how to organize submission deadlines, file naming, version checks, and final testing.

### bn

একটি টিম একাধিক বক্তার কাছ থেকে প্রেজেন্টেশন ফাইল সংগ্রহ করছে। জমা দেওয়ার সময়সীমা, ফাইলের নামকরণ, ভার্সন যাচাই এবং চূড়ান্ত পরীক্ষা কীভাবে গুছিয়ে করবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি team একাধিক speaker-এর কাছ থেকে presentation file সংগ্রহ করছে। জমা দেওয়ার deadline, file-এর নামকরণ, version check আর চূড়ান্ত testing কীভাবে গুছিয়ে করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Set a submission deadline well before the event, with a reminder.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Define a file-naming convention, such as session, speaker and version.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Check that the latest version is used, such as confirming with speakers or tracking versions.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Test every file on the event computer before the event.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Collect files in one shared location with a backup copy.
  Rationale: Organization.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC096

procedural_instructional; medium.

### en

A delivery needed for a project may arrive late. Propose a procedure for checking impact, identifying alternatives, updating the schedule, and informing affected people.

### bn

একটি প্রজেক্টের জন্য প্রয়োজনীয় একটি ডেলিভারি দেরিতে পৌঁছাতে পারে। প্রভাব যাচাই, বিকল্প খুঁজে বের করা, সময়সূচি হালনাগাদ করা এবং সংশ্লিষ্ট মানুষদের জানানোর একটি পদ্ধতি প্রস্তাব করুন।

### bn_cs

একটি project-এর জন্য প্রয়োজনীয় একটি delivery দেরিতে পৌঁছাতে পারে। impact check করা, alternative খুঁজে বের করা, schedule update করা আর affected মানুষদের জানানোর একটি procedure propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Confirm the expected delay with the supplier and check which tasks depend on the delivery.
  Rationale: Impact check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Identify alternatives, such as another supplier, partial delivery or resequencing tasks.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Update the schedule to reflect the delay or chosen alternative.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Inform affected people with the impact and the plan.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Set a decision point for when to switch to the alternative.
  Rationale: Timeliness.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN006

information_synthesis; easy.

### en

Create a short summary that keeps both benefits and limitations: The new process reduced average handling time from 20 to 14 minutes. Error rates were unchanged. Staff reported more interruptions. The pilot lasted only three weeks.

### bn

সুবিধা ও সীমাবদ্ধতা দুটোই রেখে একটি সংক্ষিপ্ত সারাংশ তৈরি করুন: নতুন প্রক্রিয়ায় গড় হ্যান্ডলিং টাইম ২০ মিনিট থেকে কমে ১৪ মিনিট হয়েছে। ভুলের হার অপরিবর্তিত ছিল। কর্মীরা জানিয়েছেন, কাজে বাধা আগের চেয়ে বেড়েছে। পাইলটটি চলেছিল মাত্র তিন সপ্তাহ।

### bn_cs

benefit আর limitation দুটোই রেখে একটি short summary তৈরি করুন: নতুন process-এ average handling time ২০ মিনিট থেকে কমে ১৪ মিনিট হয়েছে। error rate অপরিবর্তিত ছিল। staff-রা জানিয়েছেন, interruption আগের চেয়ে বেড়েছে। pilot-টা চলেছিল মাত্র তিন সপ্তাহ।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that average handling time fell from 20 to 14 minutes.
  Rationale: Benefit.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that error rates were unchanged.
  Rationale: Result.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that staff reported more interruptions.
  Rationale: Limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): State that the pilot lasted only three weeks.
  Rationale: Limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN025

information_synthesis; medium.

### en

Construct a timeline and state which activities overlapped: Training ran June 1 to June 7. Pilot operation ran June 5 to June 20. Feedback collection ran June 15 to June 22. Final review occurred June 25.

### bn

একটি সময়রেখা তৈরি করুন এবং কোন কাজগুলো একই সময়ে চলেছে তা উল্লেখ করুন: প্রশিক্ষণ চলেছে ১ জুন থেকে ৭ জুন। পাইলট কার্যক্রম চলেছে ৫ জুন থেকে ২০ জুন। মতামত সংগ্রহ চলেছে ১৫ জুন থেকে ২২ জুন। চূড়ান্ত পর্যালোচনা হয়েছে ২৫ জুন।

### bn_cs

একটি timeline তৈরি করুন এবং কোন activity-গুলো overlap করেছে তা উল্লেখ করুন: training চলেছে ১ জুন থেকে ৭ জুন। pilot operation চলেছে ৫ জুন থেকে ২০ জুন। feedback collection চলেছে ১৫ জুন থেকে ২২ জুন। final review হয়েছে ২৫ জুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): List the activities in chronological order with their dates.
  Rationale: Timeline.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that training (June 1–7) overlapped pilot operation from June 5 to June 7.
  Rationale: Overlap.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that pilot operation (June 5–20) overlapped feedback collection from June 15 to June 20.
  Rationale: Overlap.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): State that the June 25 final review did not overlap other activities.
  Rationale: Completeness.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN055

information_synthesis; medium.

### en

A dashboard shows 1,240 users while a monthly report shows 1,198. The dashboard updates daily and the report was generated five days ago. Explain the most relevant possible reason for the difference and what else should be checked.

### bn

একটি ড্যাশবোর্ডে ১,২৪০ জন ব্যবহারকারী দেখাচ্ছে, অথচ একটি মাসিক রিপোর্টে দেখাচ্ছে ১,১৯৮ জন। ড্যাশবোর্ড প্রতিদিন আপডেট হয় এবং রিপোর্টটি পাঁচ দিন আগে তৈরি করা হয়েছে। পার্থক্যের সবচেয়ে প্রাসঙ্গিক সম্ভাব্য কারণ কী এবং আর কী কী যাচাই করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি dashboard-এ ১,২৪০ জন user দেখাচ্ছে, অথচ একটি monthly report-এ দেখাচ্ছে ১,১৯৮ জন। dashboard প্রতিদিন update হয় এবং report-টা পাঁচ দিন আগে generate করা হয়েছে। পার্থক্যের সবচেয়ে relevant সম্ভাব্য কারণ কী এবং আর কী কী check করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify timing as the most relevant reason: the dashboard includes users added in the five days since the report.
  Rationale: The key inference.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check whether both use the same user definition, such as active versus registered.
  Rationale: Definition difference.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check filters, deduplication or time-zone cutoffs.
  Rationale: Processing differences.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Reconcile by recomputing the dashboard figure for the report's date.
  Rationale: Direct test.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Growth of 42 users in five days is plausible but not confirmed. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN095

information_synthesis; medium.

### en

Prepare a manager-facing summary of a four-week pilot without hiding subgroup differences or study limitations. The pilot involved 75 employees across Departments A, B, and C. Thirty employees were from A, 25 from B, and 20 from C. Across all participants, average task-completion time improved by 10 percent compared with the four weeks immediately before the pilot. Department A improved by 14 percent, Department B improved by 9 percent, and Department C showed no measurable improvement. Overall error rates declined from 4.0 percent to 3.5 percent, but the pilot team has not yet tested whether that change is statistically distinguishable from normal variation. Support requests increased sharply during the first week, were still above baseline in week two, and returned approximately to the previous baseline by week three. Participants received a two-hour training session before the pilot. Department C scheduled its training at the end of a busy reporting period and had the lowest attendance rate at 65 percent; the other two departments exceeded 90 percent attendance. The pilot did not randomly assign employees to use or not use the new workflow, and there was no concurrent control group. Managers knew the pilot was being evaluated. Satisfaction averaged 4.1 out of 5 overall, but Department C averaged 3.4. No staff reductions occurred during the pilot. The study covers only four weeks, so the team has no evidence yet about long-term retention, seasonal workloads, or whether support demand will remain at baseline. The summary should distinguish observed outcomes from possible explanations and should not claim that training attendance caused Department C's result.

### bn

উপগোষ্ঠীগুলোর পার্থক্য বা গবেষণার সীমাবদ্ধতা আড়াল না করে চার সপ্তাহের একটি পাইলটের ম্যানেজারদের উপযোগী সারাংশ প্রস্তুত করুন। পাইলটে A, B ও C বিভাগ মিলিয়ে ৭৫ জন কর্মী অংশ নিয়েছেন। এর মধ্যে ৩০ জন ছিলেন বিভাগ A থেকে, ২৫ জন B থেকে এবং ২০ জন C থেকে। পাইলটের ঠিক আগের চার সপ্তাহের তুলনায় সব অংশগ্রহণকারী মিলিয়ে গড়ে কাজ শেষ করার সময় ১০ শতাংশ উন্নত হয়েছে। বিভাগ A-তে উন্নতি হয়েছে ১৪ শতাংশ, বিভাগ B-তে ৯ শতাংশ, আর বিভাগ C-তে পরিমাপযোগ্য কোনো উন্নতি দেখা যায়নি। সামগ্রিক ভুলের হার ৪.০ শতাংশ থেকে কমে ৩.৫ শতাংশ হয়েছে, কিন্তু এই পরিবর্তন স্বাভাবিক ওঠানামা থেকে পরিসংখ্যানগতভাবে আলাদা করা যায় কি না, পাইলট টিম তা এখনো পরীক্ষা করেনি। প্রথম সপ্তাহে সাপোর্ট অনুরোধ হঠাৎ অনেক বেড়ে যায়, দ্বিতীয় সপ্তাহেও তা আগের স্বাভাবিক মাত্রার ওপরে ছিল, এবং তৃতীয় সপ্তাহের মধ্যে মোটামুটি আগের স্বাভাবিক মাত্রায় ফিরে আসে। পাইলটের আগে অংশগ্রহণকারীরা দুই ঘণ্টার একটি প্রশিক্ষণ সেশন পেয়েছিলেন। বিভাগ C তাদের প্রশিক্ষণ রেখেছিল ব্যস্ত একটি রিপোর্টিং মৌসুমের শেষে, এবং সেখানে উপস্থিতির হার ছিল সবচেয়ে কম, ৬৫ শতাংশ; অন্য দুটি বিভাগে উপস্থিতি ৯০ শতাংশ ছাড়িয়েছিল। পাইলটে কর্মীদের দৈবচয়নের ভিত্তিতে নতুন ওয়ার্কফ্লো ব্যবহার করা বা না করার দলে ভাগ করা হয়নি, এবং একই সময়ে কোনো কন্ট্রোল গ্রুপও ছিল না। ম্যানেজাররা জানতেন যে পাইলটটি মূল্যায়ন করা হচ্ছে। সামগ্রিকভাবে সন্তুষ্টির গড় ছিল ৫-এর মধ্যে ৪.১, কিন্তু বিভাগ C-তে গড় ছিল ৩.৪। পাইলট চলাকালে কোনো কর্মী ছাঁটাই হয়নি। গবেষণাটি মাত্র চার সপ্তাহের, তাই দীর্ঘমেয়াদি রিটেনশন, মৌসুমি কাজের চাপ, বা সাপোর্টের চাহিদা স্বাভাবিক মাত্রায় থাকবে কি না—এসব বিষয়ে টিমের কাছে এখনো কোনো প্রমাণ নেই। সারাংশে পর্যবেক্ষিত ফলাফলকে সম্ভাব্য ব্যাখ্যা থেকে আলাদা রাখতে হবে, এবং এমন দাবি করা যাবে না যে প্রশিক্ষণে উপস্থিতির কারণেই বিভাগ C-এর এই ফলাফল হয়েছে।

### bn_cs

subgroup difference বা study limitation লুকিয়ে না রেখে চার সপ্তাহের একটি pilot-এর manager-facing summary তৈরি করুন। pilot-এ Department A, B আর C মিলিয়ে ৭৫ জন employee অংশ নিয়েছেন। এর মধ্যে ৩০ জন ছিলেন A থেকে, ২৫ জন B থেকে এবং ২০ জন C থেকে। pilot-এর ঠিক আগের চার সপ্তাহের তুলনায় সব participant মিলিয়ে average task-completion time ১০ শতাংশ improve হয়েছে। Department A-তে improvement হয়েছে ১৪ শতাংশ, Department B-তে ৯ শতাংশ, আর Department C-তে measurable কোনো improvement দেখা যায়নি। overall error rate ৪.০ শতাংশ থেকে কমে ৩.৫ শতাংশ হয়েছে, কিন্তু এই change normal variation থেকে statistically আলাদা কি না, pilot team সেটা এখনো test করেনি। প্রথম সপ্তাহে support request হঠাৎ অনেক বেড়ে যায়, দ্বিতীয় সপ্তাহেও সেটা baseline-এর ওপরে ছিল, এবং তৃতীয় সপ্তাহের মধ্যে মোটামুটি আগের baseline-এ ফিরে আসে। pilot-এর আগে participant-রা দুই ঘণ্টার একটি training session পেয়েছিলেন। Department C তাদের training রেখেছিল ব্যস্ত একটি reporting period-এর শেষে, এবং সেখানে attendance rate ছিল সবচেয়ে কম, ৬৫ শতাংশ; অন্য দুটি department-এ attendance ৯০ শতাংশ ছাড়িয়েছিল। pilot-এ employee-দের randomly নতুন workflow ব্যবহার করা বা না করার group-এ ভাগ করা হয়নি, এবং একই সময়ে কোনো concurrent control group-ও ছিল না। manager-রা জানতেন যে pilot-টা evaluate করা হচ্ছে। overall satisfaction-এর গড় ছিল ৫-এর মধ্যে ৪.১, কিন্তু Department C-তে গড় ছিল ৩.৪। pilot চলাকালে কোনো staff reduction হয়নি। study-টা মাত্র চার সপ্তাহের, তাই long-term retention, seasonal workload, বা support demand baseline-এ থাকবে কি না—এসব বিষয়ে team-এর কাছে এখনো কোনো evidence নেই। summary-তে observed outcome-কে possible explanation থেকে আলাদা রাখতে হবে, এবং এমন claim করা যাবে না যে training attendance-এর কারণেই Department C-এর এই result হয়েছে।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State the overall 10 percent task-time improvement for 75 employees versus the prior four weeks.
  Rationale: Overall outcome.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State department results: A 14 percent, B 9 percent and C no measurable improvement.
  Rationale: Subgroup outcomes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that error rates fell from 4.0 to 3.5 percent but significance has not been tested.
  Rationale: Outcome with qualifier.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): State that support requests rose sharply in week one and returned to about baseline by week three.
  Rationale: Outcome.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): State satisfaction of 4.1 overall and 3.4 in Department C.
  Rationale: Outcome.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): State that Department C had 65 percent training attendance versus over 90 percent elsewhere, with training at the end of a busy period.
  Rationale: Context.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (critical; all-critical): Do not claim training attendance caused Department C's result; presenting it as a possible explanation complies.
  Rationale: Explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-08** (critical; all-critical): State the design limitations: no random assignment or concurrent control group, managers knew of the evaluation, and only four weeks of data.
  Rationale: Key limitations.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-09** (supporting; ordinary, outside prespecified sample): State that no staff reductions occurred during the pilot.
  Rationale: Context.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Extended-context task. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN099

information_synthesis; hard.

### en

Write a balanced research synthesis that preserves subgroup findings and methodological limitations. Model X achieved 84 percent overall accuracy and Model Y achieved 80 percent on the same held-out test set of 6,000 items. The test set contains four language groups. The largest group represents 52 percent of the items, while the smallest language group represents only 6 percent. On the smallest group, Model Y scored 71 percent and Model X scored 64 percent. On the largest group, X scored 88 percent and Y scored 82 percent. The remaining two groups show differences of less than three percentage points. The researchers report bootstrap confidence intervals for overall accuracy, and those intervals do not overlap, but they did not report subgroup confidence intervals. Both models used the same decoding settings. Model X has approximately twice as many parameters as Model Y. The study reports no latency, memory-use, energy, or inference-cost comparison. Human annotators created the reference labels, and a second annotator independently reviewed 20 percent of the test set. Agreement on that reviewed subset was 91 percent. The paper does not report whether disagreement rates differed by language group. The smallest language group also contains a higher proportion of long-form items than the overall test set. The authors state that X has higher overall accuracy and that Y performs better on the smallest language group; those descriptive statements are supported by the reported scores. However, the available evidence does not establish why the subgroup reversal occurs, whether it would persist in a larger sample, or which model is preferable for deployment. The synthesis should not collapse the overall and subgroup results into a single winner.

### bn

উপগোষ্ঠীভিত্তিক ফলাফল এবং পদ্ধতিগত সীমাবদ্ধতা অক্ষুণ্ন রেখে একটি ভারসাম্যপূর্ণ সমন্বিত গবেষণা-সারাংশ লিখুন। একই ৬,০০০ আইটেমের হেল্ড-আউট টেস্ট সেটে মডেল X-এর সামগ্রিক নির্ভুলতা ৮৪ শতাংশ এবং মডেল Y-এর ৮০ শতাংশ। টেস্ট সেটে চারটি ভাষাগোষ্ঠী আছে। সবচেয়ে বড় গোষ্ঠী মোট আইটেমের ৫২ শতাংশ, আর সবচেয়ে ছোট ভাষাগোষ্ঠী মাত্র ৬ শতাংশ। সবচেয়ে ছোট গোষ্ঠীতে মডেল Y-এর স্কোর ৭১ শতাংশ এবং মডেল X-এর ৬৪ শতাংশ। সবচেয়ে বড় গোষ্ঠীতে X পেয়েছে ৮৮ শতাংশ এবং Y পেয়েছে ৮২ শতাংশ। বাকি দুটি গোষ্ঠীতে পার্থক্য তিন শতাংশ-পয়েন্টের কম। গবেষকেরা সামগ্রিক নির্ভুলতার জন্য বুটস্ট্র্যাপ কনফিডেন্স ইন্টারভাল জানিয়েছেন, এবং সেই ইন্টারভালগুলো একটি আরেকটিকে ওভারল্যাপ করে না, কিন্তু উপগোষ্ঠীগুলোর কনফিডেন্স ইন্টারভাল জানাননি। দুটি মডেলেই একই ডিকোডিং সেটিংস ব্যবহার করা হয়েছে। মডেল X-এর প্যারামিটার সংখ্যা মডেল Y-এর প্রায় দ্বিগুণ। গবেষণায় লেটেন্সি, মেমরি ব্যবহার, শক্তি খরচ বা ইনফারেন্স খরচের কোনো তুলনা নেই। মানুষ অ্যানোটেটররা রেফারেন্স লেবেল তৈরি করেছেন, এবং দ্বিতীয় একজন অ্যানোটেটর স্বাধীনভাবে টেস্ট সেটের ২০ শতাংশ পর্যালোচনা করেছেন। পর্যালোচিত সেই অংশে দুজনের মতৈক্য ছিল ৯১ শতাংশ। ভাষাগোষ্ঠীভেদে মতানৈক্যের হার আলাদা ছিল কি না, গবেষণাপত্রে তা জানানো হয়নি। সবচেয়ে ছোট ভাষাগোষ্ঠীতে পুরো টেস্ট সেটের তুলনায় লং-ফর্ম আইটেমের অনুপাতও বেশি। লেখকেরা বলেছেন, X-এর সামগ্রিক নির্ভুলতা বেশি এবং সবচেয়ে ছোট ভাষাগোষ্ঠীতে Y ভালো করেছে; এই বর্ণনামূলক বক্তব্যগুলো প্রকাশিত স্কোর দিয়ে সমর্থিত। তবে উপগোষ্ঠীতে ফলাফল কেন উল্টে যায়, বড় নমুনাতেও তা টিকে থাকবে কি না, কিংবা ডিপ্লয়মেন্টের জন্য কোন মডেলটি বেশি উপযুক্ত—হাতে থাকা প্রমাণ এসব প্রতিষ্ঠা করে না। সারাংশে সামগ্রিক ও উপগোষ্ঠীর ফলাফল মিলিয়ে একটিমাত্র বিজয়ী ঘোষণা করা যাবে না।

### bn_cs

subgroup finding আর methodological limitation ঠিক রেখে একটি balanced research synthesis লিখুন। একই ৬,০০০ item-এর held-out test set-এ Model X-এর overall accuracy ৮৪ শতাংশ আর Model Y-এর ৮০ শতাংশ। test set-এ চারটি language group আছে। সবচেয়ে বড় group মোট item-এর ৫২ শতাংশ, আর সবচেয়ে ছোট language group মাত্র ৬ শতাংশ। সবচেয়ে ছোট group-এ Model Y-এর score ৭১ শতাংশ আর Model X-এর ৬৪ শতাংশ। সবচেয়ে বড় group-এ X পেয়েছে ৮৮ শতাংশ আর Y পেয়েছে ৮২ শতাংশ। বাকি দুটি group-এ difference তিন percentage point-এর কম। researcher-রা overall accuracy-র জন্য bootstrap confidence interval report করেছেন, এবং সেই interval-গুলো overlap করে না, কিন্তু subgroup confidence interval report করেননি। দুটি model-এই একই decoding settings ব্যবহার করা হয়েছে। Model X-এর parameter সংখ্যা Model Y-এর প্রায় দ্বিগুণ। study-তে latency, memory use, energy বা inference cost-এর কোনো comparison নেই। human annotator-রা reference label তৈরি করেছেন, এবং দ্বিতীয় একজন annotator independently test set-এর ২০ শতাংশ review করেছেন। review করা সেই subset-এ agreement ছিল ৯১ শতাংশ। language group ভেদে disagreement rate আলাদা ছিল কি না, paper-এ সেটা report করা হয়নি। সবচেয়ে ছোট language group-এ পুরো test set-এর তুলনায় long-form item-এর proportion-ও বেশি। author-রা বলেছেন, X-এর overall accuracy বেশি এবং সবচেয়ে ছোট language group-এ Y ভালো perform করেছে; এই descriptive statement-গুলো reported score দিয়ে supported। তবে subgroup-এ result কেন উল্টে যায়, বড় sample-এও সেটা persist করবে কি না, কিংবা deployment-এর জন্য কোন model-টা বেশি preferable—available evidence এসব establish করে না। synthesis-এ overall আর subgroup result মিলিয়ে একটিমাত্র winner ঘোষণা করা যাবে না।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State overall accuracy: Model X 84 percent and Model Y 80 percent on the same 6,000-item test set, with non-overlapping bootstrap intervals.
  Rationale: Overall finding.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State the smallest-group reversal: Y 71 percent versus X 64 percent on a group that is 6 percent of items.
  Rationale: Subgroup finding.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): State that on the largest group (52 percent) X scored 88 and Y 82, and the other two groups differ by under three points.
  Rationale: Subgroup findings.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): State that subgroup confidence intervals were not reported, so the reversal's reliability is uncertain.
  Rationale: Key limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Note that the smallest group has more long-form items, a possible confounder for the reversal.
  Rationale: Limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Note annotation quality limits: 20 percent double-reviewed at 91 percent agreement, with no per-language disagreement rates.
  Rationale: Limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (supporting; ordinary, outside prespecified sample): Note that X has about twice the parameters and no latency, memory, energy or cost comparison was reported.
  Rationale: Deployment limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-08** (critical; all-critical): Do not declare a single overall winner or claim which model is better for deployment; reporting overall and subgroup results separately complies.
  Rationale: Explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-09** (supporting; ordinary, outside prespecified sample): Note that the evidence does not explain why the reversal occurs or whether it would persist.
  Rationale: Explicit limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Extended-context task. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH016

technical_troubleshooting; medium.

### en

A computer receives an IP address but cannot communicate with devices outside its local subnet. Build a troubleshooting sequence that checks addressing, gateway, routing, and firewall behavior.

### bn

একটি কম্পিউটার আইপি অ্যাড্রেস পাচ্ছে, কিন্তু নিজের লোকাল সাবনেটের বাইরের কোনো ডিভাইসের সঙ্গে যোগাযোগ করতে পারছে না। অ্যাড্রেসিং, গেটওয়ে, রাউটিং এবং ফায়ারওয়ালের আচরণ যাচাই করে এমন একটি ধারাবাহিক সমস্যা সমাধানের ক্রম তৈরি করুন।

### bn_cs

একটি computer IP address পাচ্ছে, কিন্তু নিজের local subnet-এর বাইরের কোনো device-এর সঙ্গে যোগাযোগ করতে পারছে না। addressing, gateway, routing আর firewall-এর আচরণ check করে এমন একটি ধারাবাহিক troubleshooting ক্রম তৈরি করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Check the IP address and subnet mask are correct.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Check the default gateway is set and reachable, such as by pinging it.
  Rationale: Most likely cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check routing, such as the route table or a traceroute.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check firewall rules on the host or network.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Order the checks as a sequence and explain how each result directs the next step.
  Rationale: The prompt asks for a sequence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without an order or result-driven progression.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH084

technical_troubleshooting; medium.

### en

A large archive extracts successfully but several files inside cannot be opened. Explain how to investigate archive integrity, file corruption, permissions, paths, and application compatibility.

### bn

একটি বড় আর্কাইভ সফলভাবে এক্সট্র্যাক্ট হলেও ভেতরের কয়েকটি ফাইল খোলা যাচ্ছে না। আর্কাইভের অখণ্ডতা, ফাইল করাপশন, অনুমতি, পাথ এবং অ্যাপ্লিকেশনের সামঞ্জস্য কীভাবে খতিয়ে দেখবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি বড় archive সফলভাবে extract হলেও ভেতরের কয়েকটি file open করা যাচ্ছে না। archive integrity, file corruption, permission, path আর application compatibility কীভাবে খতিয়ে দেখবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Verify archive integrity, such as a checksum against the source or an archive test command.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Check individual files for corruption, such as zero size or comparing with source copies.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check file permissions after extraction.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check path length or invalid characters that truncate names.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Check that the right application and version are used to open the files.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Explain how a possible result points to a specific cause.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without result interpretation.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Keep the original archive while investigating; good practice. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH092

technical_troubleshooting; easy.

### en

A USB webcam works in one application but not another. Describe basic permission and application-setting checks.

### bn

একটি ইউএসবি ওয়েবক্যাম একটি অ্যাপ্লিকেশনে কাজ করে, কিন্তু আরেকটিতে করে না। অনুমতি ও অ্যাপ্লিকেশনের সেটিংস-সংক্রান্ত প্রাথমিক চেকগুলো বর্ণনা করুন।

### bn_cs

একটি USB webcam একটি application-এ কাজ করে, কিন্তু আরেকটিতে করে না। basic permission আর application-setting check-গুলো describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check operating-system camera privacy permissions for the failing application.
  Rationale: Most common cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Check that the other application is closed, since some cameras can be used by only one app at a time.
  Rationale: Common cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Select the correct camera device in the failing application's settings.
  Rationale: App setting.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check browser site permissions if the failing app is web-based.
  Rationale: App setting.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH099

technical_troubleshooting; hard.

### en

A barcode scanner occasionally inserts incorrect characters into a business application. Explain how you would investigate scanner configuration, keyboard layout, encoding, connection quality, and application parsing.

### bn

একটি বারকোড স্ক্যানার মাঝে মাঝে একটি ব্যবসায়িক অ্যাপ্লিকেশনে ভুল অক্ষর বসিয়ে দেয়। স্ক্যানারের কনফিগারেশন, কিবোর্ড লেআউট, এনকোডিং, সংযোগের মান এবং অ্যাপ্লিকেশনের পার্সিং কীভাবে খতিয়ে দেখবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি barcode scanner মাঝে মাঝে একটি ব্যবসায়িক application-এ ভুল character বসিয়ে দেয়। scanner configuration, keyboard layout, encoding, সংযোগের মান আর application-এর parsing কীভাবে খতিয়ে দেখবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Check scanner configuration such as symbology, prefixes and suffixes.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check that the scanner's keyboard layout matches the computer's input language.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check character encoding of special characters.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check connection quality such as wireless interference or cable faults.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Check how the application parses input, such as field length limits or input speed.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Scan known test barcodes into a plain text editor and explain how possible results point to a specific cause.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Suggests testing without result interpretation.

Draft notes: P08 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
