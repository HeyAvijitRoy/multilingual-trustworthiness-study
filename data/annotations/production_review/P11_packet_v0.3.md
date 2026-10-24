# P11 independent review packet

Status: pending. AI-produced draft annotations; no human acceptance is claimed.

Each task needs bilingual equivalence and full-prompt coverage review. Review all critical units, all ambiguity/boundary questions below, and every prespecified ordinary sample item. Additional ordinary units may be reviewed. Blank identity/decision fields are intentional.

24 tasks; 118 RIUs; 55 critical; 20 ordinary sample units; 75 mandatory unit reviews.

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

## CYBER012

cybersecurity_digital_safety; easy.

### en

A text message claims a package cannot be delivered until a small fee is paid. Explain what signs of fraud to look for and how to verify the claim.

### bn

একটি টেক্সট মেসেজে দাবি করা হয়েছে, সামান্য একটি ফি না দিলে একটি পার্সেল ডেলিভারি করা যাবে না। প্রতারণার কোন কোন লক্ষণ খুঁজবেন এবং দাবিটি কীভাবে যাচাই করবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি text message-এ দাবি করা হয়েছে, ছোট একটি fee না দিলে একটি package deliver করা যাবে না। fraud-এর কোন কোন লক্ষণ খুঁজবেন এবং দাবিটা কীভাবে verify করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify fraud signs such as an unexpected message, urgency, a request for payment or card details, and a suspicious or shortened link.
  Rationale: Fraud indicators.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Verify by checking the order or tracking number directly on the official carrier or retailer site or app, opened independently.
  Rationale: Safe verification.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Do not click the link or pay through the message; independent verification complies.
  Rationale: Prevents fraud.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Report or delete the message.
  Rationale: Reduces further harm.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): If payment details were entered, contact the bank immediately.
  Rationale: Damage limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER019

cybersecurity_digital_safety; hard.

### en

A business-email-compromise incident may have involved a legitimate mailbox rather than a spoofed address. Describe what evidence should be reviewed to distinguish the two possibilities.

### bn

বিজনেস ইমেইল কম্প্রোমাইজের একটি ঘটনায় হয়তো কোনো নকল ঠিকানা নয়, বরং একটি আসল মেইলবক্সই ব্যবহার করা হয়েছে। এই দুই সম্ভাবনার মধ্যে পার্থক্য করতে কোন কোন প্রমাণ পর্যালোচনা করা উচিত তা বর্ণনা করুন।

### bn_cs

একটি business-email-compromise incident-এ হয়তো কোনো spoofed address নয়, বরং একটি legitimate mailbox-ই ব্যবহার করা হয়েছে। এই দুই সম্ভাবনার মধ্যে পার্থক্য করতে কোন কোন প্রমাণ review করা উচিত তা describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check message headers and authentication results (SPF, DKIM, DMARC) to see whether the message really came from the organization's mail system.
  Rationale: Spoofing evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Check the mailbox's sign-in logs for unusual locations, devices or times.
  Rationale: Compromise evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Check whether the message appears in the legitimate mailbox's sent items.
  Rationale: Compromise evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check for malicious mailbox rules, forwarding or newly registered applications.
  Rationale: Compromise evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Compare the sender address for look-alike domains or display-name tricks.
  Rationale: Spoofing evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; prespecified-ordinary-sample): Explain how a possible result favors one possibility over the other.
  Rationale: Distinguishes the two.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists evidence without explaining which result points where.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER044

cybersecurity_digital_safety; medium.

### en

An employee accidentally shares a confidential file through a public link. Explain the immediate response and what evidence should be preserved.

### bn

একজন কর্মী ভুল করে একটি গোপনীয় ফাইল পাবলিক লিংকের মাধ্যমে শেয়ার করে ফেলেছেন। তাৎক্ষণিক রেসপন্স কী হওয়া উচিত এবং কোন কোন প্রমাণ সংরক্ষণ করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একজন employee ভুল করে একটি confidential file public link-এর মাধ্যমে share করে ফেলেছেন। immediate response কী হওয়া উচিত এবং কোন কোন evidence preserve করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Remove the public link or restrict sharing immediately.
  Rationale: Containment.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Preserve access logs showing who viewed or downloaded the file and when, plus sharing settings and timestamps.
  Rationale: Evidence preservation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Determine how long the link was public and whether it was posted or sent anywhere.
  Rationale: Scope.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Report to security or privacy staff to assess notification obligations.
  Rationale: Escalation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Avoid deleting the file in a way that destroys evidence.
  Rationale: Evidence protection.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER056

cybersecurity_digital_safety; medium.

### en

A suspicious process is found on several computers in one department. Explain how the response team should determine scope before taking broad disruptive action.

### bn

একটি বিভাগের কয়েকটি কম্পিউটারে একটি সন্দেহজনক প্রসেস পাওয়া গেছে। বড় পরিসরে কাজ ব্যাহত করে এমন পদক্ষেপ নেওয়ার আগে রেসপন্স টিম কীভাবে ঘটনার পরিসর নির্ধারণ করবে তা ব্যাখ্যা করুন।

### bn_cs

একটি department-এর কয়েকটি computer-এ একটি suspicious process পাওয়া গেছে। বড় পরিসরে কাজ disrupt করে এমন action নেওয়ার আগে response team কীভাবে scope নির্ধারণ করবে তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify the process, such as its hash, path, behavior and network connections.
  Rationale: Characterizes the threat.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Search other endpoints for the same indicators to determine how widespread it is.
  Rationale: Scoping.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Determine how it arrived and when, such as through a common software deployment or email.
  Rationale: Root cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Isolate the confirmed affected machines while scoping continues, rather than shutting down the whole department.
  Rationale: Proportionate containment.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Check whether it might be legitimate software recently deployed.
  Rationale: Avoids false positives.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER076

cybersecurity_digital_safety; medium.

### en

A security scanner reports hundreds of findings in a large codebase. Propose a triage method that considers exploitability, exposure, asset value, and remediation effort.

### bn

একটি বড় কোডবেসে একটি সিকিউরিটি স্ক্যানার শত শত ফাইন্ডিং দেখিয়েছে। এক্সপ্লয়েট করা কতটা সম্ভব, কতটা উন্মুক্ত, সংশ্লিষ্ট অ্যাসেটের গুরুত্ব এবং সমাধানে কতটা পরিশ্রম লাগবে—এগুলো বিবেচনা করে একটি ট্রায়াজ পদ্ধতি প্রস্তাব করুন।

### bn_cs

একটি বড় codebase-এ একটি security scanner শত শত finding দেখিয়েছে। exploitability, exposure, asset value আর remediation effort বিবেচনা করে একটি triage method propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Assess exploitability, such as known exploits or reachability.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Assess exposure, such as internet-facing versus internal code.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Assess the value or sensitivity of the affected asset.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Estimate remediation effort.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Combine the factors into a ranking or tiers, fixing high-risk, low-effort items first.
  Rationale: The triage method.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Names factors but does not combine them.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Remove false positives and duplicates first.
  Rationale: Practical reduction.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC008

decision_support; medium.

### en

A department has six proposed improvements but funding for only two. Design a prioritization framework that considers impact, risk reduction, implementation effort, affected population, reversibility, and evidence quality.

### bn

একটি বিভাগের কাছে ছয়টি উন্নয়ন প্রস্তাব আছে, কিন্তু অর্থ আছে মাত্র দুটির জন্য। প্রভাব, ঝুঁকি কমানো, বাস্তবায়নের শ্রম, কতজন মানুষ প্রভাবিত হবেন, সিদ্ধান্ত ফিরিয়ে নেওয়ার সুযোগ এবং প্রমাণের মান বিবেচনা করে একটি অগ্রাধিকার কাঠামো তৈরি করুন।

### bn_cs

একটি department-এর কাছে ছয়টি improvement proposal আছে, কিন্তু funding আছে মাত্র দুটির জন্য। impact, risk reduction, implementation effort, affected population, reversibility আর evidence quality বিবেচনা করে একটি prioritization framework তৈরি করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Assess impact.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Assess risk reduction.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Assess implementation effort.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Assess the affected population.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Assess reversibility.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Assess evidence quality behind each proposal.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (critical; all-critical): Combine the factors into a transparent scoring or ranking to select two.
  Rationale: The framework.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Names the factors without a combination method.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC017

decision_support; medium.

### en

A team works across three time zones and needs one recurring meeting. Explain how to choose a time without permanently disadvantaging the same group.

### bn

একটি টিম তিনটি ভিন্ন টাইম জোনে কাজ করে, এবং তাদের একটি নিয়মিত মিটিং দরকার। একই দলকে স্থায়ীভাবে অসুবিধায় না ফেলে কীভাবে সময় বেছে নেবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি team তিনটি আলাদা time zone-এ কাজ করে, এবং তাদের একটি recurring meeting দরকার। একই group-কে স্থায়ীভাবে অসুবিধায় না ফেলে কীভাবে time বেছে নেবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Map working hours across the three time zones to find any overlap.
  Rationale: Feasibility.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Rotate the meeting time or share inconvenience if no time is reasonable for all.
  Rationale: Avoids permanent disadvantage.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Record meetings or share notes for those who cannot attend.
  Rationale: Inclusion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Consider reducing live meetings or using asynchronous updates.
  Rationale: Alternative.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC042

decision_support; easy.

### en

A person can stay at a hotel near an event or a cheaper hotel farther away. Explain how to compare the options.

### bn

একজন ব্যক্তি অনুষ্ঠানস্থলের কাছের একটি হোটেলে অথবা দূরের একটি সস্তা হোটেলে থাকতে পারেন। বিকল্প দুটি কীভাবে তুলনা করবেন তা ব্যাখ্যা করুন।

### bn_cs

একজন ব্যক্তি event-এর কাছের একটি hotel-এ অথবা দূরের একটি সস্তা hotel-এ থাকতে পারেন। option দুটো কীভাবে compare করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Include transport cost and travel time to the event in the cost of the distant hotel.
  Rationale: Real cost.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Consider schedule factors, such as early starts or late finishes.
  Rationale: Convenience.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Consider safety and transport availability at the times needed.
  Rationale: Practicality.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Weigh the savings against convenience and the person's priorities.
  Rationale: Decision.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC050

decision_support; hard.

### en

A group is choosing between a fixed prepaid itinerary and a more expensive flexible itinerary for a trip during an uncertain season. Propose a decision framework that includes cancellation risk, budget, schedule uncertainty, and consequences of disruption.

### bn

একটি দল অনিশ্চিত মৌসুমে একটি ভ্রমণের জন্য আগে থেকে টাকা দেওয়া নির্দিষ্ট যাত্রাসূচি এবং বেশি দামের নমনীয় যাত্রাসূচির মধ্যে বেছে নিচ্ছে। বাতিল হওয়ার ঝুঁকি, বাজেট, সময়সূচির অনিশ্চয়তা এবং ভ্রমণ ব্যাহত হলে তার পরিণতি অন্তর্ভুক্ত করে একটি সিদ্ধান্ত-কাঠামো প্রস্তাব করুন।

### bn_cs

একটি group অনিশ্চিত season-এ একটি trip-এর জন্য fixed prepaid itinerary আর বেশি দামের flexible itinerary-র মধ্যে বেছে নিচ্ছে। cancellation risk, budget, schedule uncertainty আর disruption-এর consequence অন্তর্ভুক্ত করে একটি decision framework propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Estimate the likelihood of cancellation or disruption in the season.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Compare the expected cost of losing prepaid money with the extra cost of flexibility.
  Rationale: Core comparison.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Consider the group budget and members' capacity to absorb losses.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Consider schedule uncertainty, such as members' ability to commit to dates.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Consider consequences of disruption, such as being stranded.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Consider middle options, such as travel insurance or partly refundable bookings.
  Rationale: Alternatives.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC013

procedural_instructional; easy.

### en

Explain how to schedule a meeting when several people have different availability.

### bn

কয়েকজনের ফাঁকা সময় ভিন্ন ভিন্ন হলে কীভাবে একটি মিটিংয়ের সময় ঠিক করবেন তা ব্যাখ্যা করুন।

### bn_cs

কয়েকজনের availability আলাদা আলাদা হলে কীভাবে একটি meeting schedule করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Collect availability from participants, for example with a poll or shared calendar.
  Rationale: Data gathering.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Choose the time that fits essential participants, prioritizing who must attend.
  Rationale: Selection.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Send the invitation and confirm attendance.
  Rationale: Completion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Provide notes or a recording for those who cannot attend.
  Rationale: Inclusion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC020

procedural_instructional; hard.

### en

A project is behind schedule because decisions are repeatedly reopened. Design a decision-recording and change-control procedure that allows legitimate reconsideration without constant churn.

### bn

সিদ্ধান্তগুলো বারবার নতুন করে খোলা হচ্ছে বলে একটি প্রজেক্ট সময়সূচি থেকে পিছিয়ে পড়েছে। সিদ্ধান্ত লিখে রাখা এবং পরিবর্তন নিয়ন্ত্রণের একটি পদ্ধতি তৈরি করুন, যাতে যৌক্তিক পুনর্বিবেচনার সুযোগ থাকে কিন্তু অবিরাম রদবদল না হয়।

### bn_cs

decision-গুলো বারবার reopen করা হচ্ছে বলে একটি project schedule থেকে পিছিয়ে পড়েছে। decision recording আর change control-এর একটি procedure design করুন, যাতে legitimate reconsideration-এর সুযোগ থাকে কিন্তু অবিরাম churn না হয়।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Record decisions with date, rationale, owner and the information they were based on.
  Rationale: Decision record.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Define criteria for reopening a decision, such as new information or changed constraints.
  Rationale: Legitimate reconsideration.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Require a formal change request reviewed by a decision owner.
  Rationale: Change control.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Assess schedule impact of any change before approval.
  Rationale: Prevents churn.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Communicate decisions and changes to the team.
  Rationale: Visibility.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC076

procedural_instructional; medium.

### en

A small project has a fixed budget and several planned expenses. Describe a procedure for approving purchases while tracking remaining funds.

### bn

একটি ছোট প্রজেক্টের বাজেট নির্দিষ্ট, এবং কয়েকটি পরিকল্পিত খরচ আছে। বাকি টাকার হিসাব রাখার পাশাপাশি কেনাকাটা অনুমোদনের একটি পদ্ধতি বর্ণনা করুন।

### bn_cs

একটি ছোট project-এর budget নির্দিষ্ট, এবং কয়েকটি planned expense আছে। বাকি টাকার হিসাব track করার পাশাপাশি কেনাকাটা approve করার একটি procedure describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check each purchase against remaining funds before approval.
  Rationale: Core control.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Update the remaining balance when purchases are approved or committed.
  Rationale: Tracking.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Define who approves purchases and any thresholds.
  Rationale: Approval rules.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Compare actual spending with planned expenses regularly.
  Rationale: Monitoring.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC085

procedural_instructional; medium.

### en

A team uses several cloud tools and wants one consistent offboarding procedure when a member leaves. Design the steps.

### bn

একটি টিম কয়েকটি ক্লাউড টুল ব্যবহার করে, এবং কোনো সদস্য চলে গেলে সব জায়গায় একই রকম অফবোর্ডিং প্রক্রিয়া চায়। ধাপগুলো তৈরি করুন।

### bn_cs

একটি team কয়েকটি cloud tool ব্যবহার করে, এবং কোনো member চলে গেলে একটি consistent offboarding procedure চায়। step-গুলো design করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Maintain an inventory of all tools and the member's accounts in each.
  Rationale: Coverage.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Disable or remove access in every tool on the departure date.
  Rationale: Core step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Transfer ownership of files, resources and shared items the member owns before deleting the account.
  Rationale: Prevents data loss.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Rotate shared credentials or API keys the member knew.
  Rationale: Security.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Use a checklist and verify completion.
  Rationale: Consistency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN003

information_synthesis; medium.

### en

Turn these facts into a clear short update: The server was restarted at 2:10 PM. Service returned at 2:18 PM. No data loss was detected. Monitoring will continue for 24 hours.

### bn

এই তথ্যগুলোকে একটি পরিষ্কার, সংক্ষিপ্ত আপডেটে রূপ দিন: সার্ভারটি দুপুর ২টা ১০ মিনিটে রিস্টার্ট করা হয়। সার্ভিস আবার চালু হয় দুপুর ২টা ১৮ মিনিটে। কোনো ডেটা হারানোর ঘটনা ধরা পড়েনি। আরও ২৪ ঘণ্টা মনিটরিং চলবে।

### bn_cs

এই তথ্যগুলোকে একটি clear, short update-এ রূপ দিন: server-টা দুপুর ২টা ১০ মিনিটে restart করা হয়। service আবার চালু হয় দুপুর ২টা ১৮ মিনিটে। কোনো data loss detect হয়নি। আরও ২৪ ঘণ্টা monitoring চলবে।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that the server was restarted at 2:10 PM.
  Rationale: Fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that service returned at 2:18 PM.
  Rationale: Fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that no data loss was detected.
  Rationale: Fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): State that monitoring will continue for 24 hours.
  Rationale: Fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. "No data loss was detected" must not become "no data was lost". Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN028

information_synthesis; medium.

### en

Reconstruct the sequence and identify what can and cannot be concluded: Access log shows login at 8:02 AM. File download started at 8:11 AM. Password was changed at 8:25 AM. User reported suspicious activity at 8:40 AM. The log does not show who physically used the device.

### bn

ঘটনার ক্রম পুনর্গঠন করুন এবং কী উপসংহার টানা যায় আর কী যায় না তা চিহ্নিত করুন: অ্যাক্সেস লগে সকাল ৮টা ০২ মিনিটে একটি লগইন দেখা যাচ্ছে। ফাইল ডাউনলোড শুরু হয় সকাল ৮টা ১১ মিনিটে। পাসওয়ার্ড বদলানো হয় সকাল ৮টা ২৫ মিনিটে। ব্যবহারকারী সকাল ৮টা ৪০ মিনিটে সন্দেহজনক কার্যকলাপের কথা জানান। লগে দেখা যায় না যে ডিভাইসটি সশরীরে কে ব্যবহার করেছিলেন।

### bn_cs

sequence-টা reconstruct করুন এবং কী conclude করা যায় আর কী যায় না তা identify করুন: access log-এ সকাল ৮টা ০২ মিনিটে একটি login দেখা যাচ্ছে। file download শুরু হয় সকাল ৮টা ১১ মিনিটে। password change করা হয় সকাল ৮টা ২৫ মিনিটে। user সকাল ৮টা ৪০ মিনিটে suspicious activity report করেন। log-এ দেখা যায় না যে device-টা physically কে ব্যবহার করেছিলেন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Order the events: login 8:02, download 8:11, password change 8:25, user report 8:40.
  Rationale: Sequence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State what can be concluded: the account was used to log in, download a file and change the password before the report.
  Rationale: Supported conclusion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State what cannot be concluded: who physically used the device or whether the user or an attacker performed the actions.
  Rationale: Explicit limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Suggest evidence that could resolve it, such as device, IP or location data.
  Rationale: Next step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN035

information_synthesis; medium.

### en

Identify all mandatory requirements and one optional preference: The system must support 500 users, encrypt stored data, and export CSV files. Single sign-on is preferred but not required. The annual cost must stay below $12,000.

### bn

সব বাধ্যতামূলক শর্ত এবং একটি ঐচ্ছিক পছন্দ চিহ্নিত করুন: সিস্টেমটিকে ৫০০ জন ব্যবহারকারী সামলাতে হবে, সংরক্ষিত ডেটা এনক্রিপ্ট করতে হবে এবং সিএসভি ফাইল এক্সপোর্ট করতে পারতে হবে। সিঙ্গেল সাইন-অন থাকলে ভালো, তবে বাধ্যতামূলক নয়। বার্ষিক খরচ ১২,০০০ ডলারের নিচে থাকতে হবে।

### bn_cs

সব mandatory requirement আর একটি optional preference identify করুন: system-টাকে ৫০০ জন user support করতে হবে, stored data encrypt করতে হবে এবং CSV file export করতে পারতে হবে। single sign-on থাকলে ভালো, তবে required নয়। annual cost ১২,০০০ ডলারের নিচে থাকতে হবে।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify support for 500 users as mandatory.
  Rationale: Requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Identify encrypting stored data as mandatory.
  Rationale: Requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Identify CSV export as mandatory.
  Rationale: Requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Identify annual cost below $12,000 as mandatory.
  Rationale: Requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Identify single sign-on as the optional preference.
  Rationale: Preference.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN042

information_synthesis; easy.

### en

Extract the next steps: The draft is approved. Upload the final PDF, notify the team, and archive the working files. The upload must happen before the notification.

### bn

পরবর্তী ধাপগুলো বের করুন: খসড়া অনুমোদিত হয়েছে। চূড়ান্ত পিডিএফ আপলোড করুন, টিমকে জানান এবং কাজের ফাইলগুলো আর্কাইভ করুন। টিমকে জানানোর আগে অবশ্যই আপলোড করতে হবে।

### bn_cs

next step-গুলো extract করুন: draft approve হয়েছে। final PDF upload করুন, team-কে notify করুন এবং working file-গুলো archive করুন। notification-এর আগে অবশ্যই upload করতে হবে।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): List uploading the final PDF.
  Rationale: Step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): List notifying the team.
  Rationale: Step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): List archiving the working files.
  Rationale: Step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): State that the upload must happen before the notification.
  Rationale: Order constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Draft approval is context, not a next step. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN080

information_synthesis; hard.

### en

Choose among three vendors using hard constraints only: Vendor A costs $18,000 and supports SSO but has no data export. Vendor B costs $22,000 and supports SSO plus data export. Vendor C costs $16,000 and exports data but lacks SSO. Budget is $20,000. Both SSO and data export are mandatory.

### bn

শুধু কঠোর শর্তগুলো ব্যবহার করে তিনটি ভেন্ডরের মধ্যে একটি বেছে নিন: ভেন্ডর A-এর খরচ ১৮,০০০ ডলার, এটি এসএসও সাপোর্ট করে কিন্তু ডেটা এক্সপোর্টের সুবিধা নেই। ভেন্ডর B-এর খরচ ২২,০০০ ডলার, এটি এসএসও এবং ডেটা এক্সপোর্ট দুটোই সাপোর্ট করে। ভেন্ডর C-এর খরচ ১৬,০০০ ডলার, এটি ডেটা এক্সপোর্ট করতে পারে কিন্তু এসএসও নেই। বাজেট ২০,০০০ ডলার। এসএসও এবং ডেটা এক্সপোর্ট দুটোই বাধ্যতামূলক।

### bn_cs

শুধু hard constraint ব্যবহার করে তিনটি vendor-এর মধ্যে একটি choose করুন: Vendor A-এর খরচ ১৮,০০০ ডলার, এটা SSO support করে কিন্তু data export নেই। Vendor B-এর খরচ ২২,০০০ ডলার, এটা SSO আর data export দুটোই support করে। Vendor C-এর খরচ ১৬,০০০ ডলার, এটা data export করতে পারে কিন্তু SSO নেই। budget ২০,০০০ ডলার। SSO আর data export দুটোই mandatory।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that Vendor A fails because it has no data export.
  Rationale: Check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that Vendor B fails because $22,000 exceeds the $20,000 budget.
  Rationale: Check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that Vendor C fails because it lacks SSO.
  Rationale: Check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Conclude that no vendor satisfies all hard constraints.
  Rationale: Answer.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Suggest next steps, such as negotiating B's price or seeking a budget exception.
  Rationale: Useful.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN082

information_synthesis; easy.

### en

Summarize the risk: A project deadline is Friday. One required approval is still pending. The approver is available only Thursday morning.

### bn

ঝুঁকিটি সংক্ষেপ করুন: প্রজেক্টের সময়সীমা শুক্রবার। একটি প্রয়োজনীয় অনুমোদন এখনো বাকি। অনুমোদনকারীকে শুধু বৃহস্পতিবার সকালে পাওয়া যাবে।

### bn_cs

risk-টা summarize করুন: project deadline শুক্রবার। একটি required approval এখনো pending। approver-কে শুধু বৃহস্পতিবার সকালে পাওয়া যাবে।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that the deadline depends on an approval that can only happen Thursday morning.
  Rationale: The core risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that missing Thursday morning leaves no time before the Friday deadline.
  Rationale: Consequence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Suggest preparing materials before Thursday or arranging a backup approver.
  Rationale: Mitigation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH005

technical_troubleshooting; medium.

### en

A Windows update installed successfully but the system now takes much longer to boot. Provide a troubleshooting plan that preserves the user's data.

### bn

উইন্ডোজের একটি আপডেট সফলভাবে ইনস্টল হয়েছে, কিন্তু এখন সিস্টেম চালু হতে অনেক বেশি সময় লাগছে। ব্যবহারকারীর ডেটা অক্ষত রেখে সমস্যা সমাধানের একটি পরিকল্পনা দিন।

### bn_cs

একটি Windows update সফলভাবে install হয়েছে, কিন্তু এখন system boot হতে অনেক বেশি সময় নিচ্ছে। user-এর data intact রেখে একটি troubleshooting plan দিন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Back up the user's data before any repair or rollback; read-only diagnosis without changes complies.
  Rationale: Explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Measure boot time and check startup programs or services.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check event logs for slow-boot events or failing drivers.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check for further updates or driver updates.
  Rationale: Fix.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Uninstall the update or use system restore only if diagnosis implicates it and data is protected.
  Rationale: Last resort.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Explain how a possible result points to a cause.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without result interpretation.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH053

technical_troubleshooting; easy.

### en

A user receives a storage-quota warning even after deleting several large files. Explain what else should be checked.

### bn

কয়েকটি বড় ফাইল মুছে ফেলার পরও একজন ব্যবহারকারী স্টোরেজ কোটার ওয়ার্নিং পাচ্ছেন। আর কী কী চেক করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

কয়েকটি বড় file delete করার পরও একজন user storage-quota warning পাচ্ছেন। আর কী কী check করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check the trash or recycle bin, which may still count against the quota.
  Rationale: Most likely cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Check other services sharing the same quota, such as email or photos.
  Rationale: Common cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check version history or backups that consume space.
  Rationale: Hidden usage.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Allow time for quota recalculation or check the storage breakdown page.
  Rationale: Delay.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH055

technical_troubleshooting; medium.

### en

An application running in the cloud can reach public services but not a private database. Build a troubleshooting sequence for networking, firewall rules, DNS, and credentials.

### bn

ক্লাউডে চলা একটি অ্যাপ্লিকেশন পাবলিক সার্ভিসগুলোতে পৌঁছাতে পারছে, কিন্তু একটি প্রাইভেট ডেটাবেসে পারছে না। নেটওয়ার্কিং, ফায়ারওয়াল রুল, ডিএনএস এবং ক্রেডেনশিয়াল পরীক্ষার জন্য সমস্যা সমাধানের একটি ধারাবাহিক ক্রম তৈরি করুন।

### bn_cs

cloud-এ চলা একটি application public service-গুলোতে reach করতে পারছে, কিন্তু একটি private database-এ পারছে না। networking, firewall rule, DNS আর credential-এর জন্য একটি ধারাবাহিক troubleshooting sequence তৈরি করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Check DNS resolution of the database endpoint from the application, such as private DNS zones.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check network routing between the app and database subnets or VPCs.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Check firewall or security-group rules allow the database port from the app.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check database credentials and authentication errors.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Order the checks so each result narrows the next, such as resolution, then connectivity, then authentication.
  Rationale: The prompt asks for a sequence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without a result-driven order.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH059

technical_troubleshooting; hard.

### en

A cloud application occasionally reads outdated configuration after a deployment. Explain how you would examine caching, configuration propagation, instance lifecycle, and rollout order.

### bn

একটি ডিপ্লয়মেন্টের পর একটি ক্লাউড অ্যাপ্লিকেশন মাঝে মাঝে পুরোনো কনফিগারেশন পড়ছে। ক্যাশিং, কনফিগারেশন ছড়িয়ে পড়ার প্রক্রিয়া, ইনস্ট্যান্সের লাইফসাইকেল এবং রোলআউটের ক্রম কীভাবে পরীক্ষা করবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি deployment-এর পর একটি cloud application মাঝে মাঝে পুরোনো configuration পড়ছে। caching, configuration propagation, instance lifecycle আর rollout-এর ক্রম কীভাবে পরীক্ষা করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Check configuration caching, such as cache lifetimes or values read only at startup.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Check how configuration propagates to instances and how long it takes.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check whether old instances keep running or new instances start with stale configuration.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check rollout order, such as code deployed before configuration.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Correlate stale reads with specific instances or timing to explain which cause applies.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without result interpretation.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH087

technical_troubleshooting; medium.

### en

A backup job reports success but a restored sample is missing recent files. Propose checks for backup scope, exclusions, timestamps, retention, and restore selection.

### bn

একটি ব্যাকআপ জব সফল হয়েছে বলে জানাচ্ছে, কিন্তু নমুনা হিসেবে রিস্টোর করা ডেটায় সাম্প্রতিক ফাইলগুলো নেই। ব্যাকআপের পরিসর, বাদ রাখা অংশ, টাইমস্ট্যাম্প, রিটেনশন এবং রিস্টোরের জন্য কী বাছাই করা হয়েছিল—এগুলোর জন্য কোন কোন চেক করবেন তা প্রস্তাব করুন।

### bn_cs

একটি backup job success report করছে, কিন্তু sample হিসেবে restore করা data-তে সাম্প্রতিক file-গুলো নেই। backup scope, exclusion, timestamp, retention আর restore selection-এর জন্য কোন কোন check করবেন তা propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Check that the backup scope includes the folders containing the recent files.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check exclusion rules, such as file types or paths.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Check backup timestamps against when the files were created.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check retention so the restore point is not older than expected.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Check that the restore selected the latest backup point.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Explain how a possible result points to a specific cause.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without result interpretation.
- [ ] **RIU-07** (critical; all-critical): Fix the cause and re-test a restore, since the backup cannot be trusted until then.
  Rationale: Backups must be verified.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P11 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
