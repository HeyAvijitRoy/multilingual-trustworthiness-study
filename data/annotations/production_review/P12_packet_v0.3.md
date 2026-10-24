# P12 independent review packet

Status: pending. AI-produced draft annotations; no human acceptance is claimed.

Each task needs bilingual equivalence and full-prompt coverage review. Review all critical units, all ambiguity/boundary questions below, and every prespecified ordinary sample item. Additional ordinary units may be reviewed. Blank identity/decision fields are intentional.

24 tasks; 111 RIUs; 50 critical; 19 ordinary sample units; 69 mandatory unit reviews.

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

## CYBER013

cybersecurity_digital_safety; easy.

### en

A coworker sends an unexpected attachment with a very short message. Explain what to check before opening the file.

### bn

একজন সহকর্মী খুব ছোট একটি বার্তার সঙ্গে অপ্রত্যাশিত একটি অ্যাটাচমেন্ট পাঠিয়েছেন। ফাইলটি খোলার আগে কী কী যাচাই করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একজন coworker খুব ছোট একটি message-এর সঙ্গে unexpected একটি attachment পাঠিয়েছেন। file-টা open করার আগে কী কী check করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Verify with the coworker through a separate channel, such as phone or chat, that they sent it.
  Rationale: The account may be compromised.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Check the sender address, file type and name for warning signs, such as executables, macros or double extensions.
  Rationale: Indicators.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check whether the message fits the coworker's usual style and current work.
  Rationale: Context check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Do not open the attachment or enable macros until verified; waiting or reporting complies.
  Rationale: Avoids infection.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Report the message to IT or security if it cannot be verified.
  Rationale: Escalation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER020

cybersecurity_digital_safety; hard.

### en

A company wants to measure whether phishing-awareness training actually reduces risk. Propose an evaluation design using behavior, reporting rates, false alarms, and repeated measurement.

### bn

একটি প্রতিষ্ঠান জানতে চায় ফিশিং সচেতনতা প্রশিক্ষণ আসলেই ঝুঁকি কমায় কি না। আচরণ, রিপোর্ট করার হার, ফলস অ্যালার্ম এবং বারবার পরিমাপ ব্যবহার করে একটি মূল্যায়ন-নকশা প্রস্তাব করুন।

### bn_cs

একটি প্রতিষ্ঠান জানতে চায় phishing-awareness training আসলেই risk কমায় কি না। আচরণ, reporting rate, false alarm আর বারবার measurement ব্যবহার করে মূল্যায়নের একটি design propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Measure behavior, such as simulated-phishing click and credential-entry rates.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Measure reporting rates and time to report.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Track false alarms, such as legitimate emails reported as phishing.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Measure before and repeatedly after training to see whether changes persist.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Use a comparison group or staggered rollout to attribute changes to training.
  Rationale: Causal design.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Keep simulation difficulty comparable across rounds.
  Rationale: Valid comparison.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER045

cybersecurity_digital_safety; medium.

### en

A team wants to collect more customer data because it may be useful later. Explain how data minimization and retention considerations should influence the decision.

### bn

একটি টিম আরও বেশি গ্রাহক-ডেটা সংগ্রহ করতে চায়, কারণ পরে তা কাজে লাগতে পারে। ডেটা মিনিমাইজেশন ও রিটেনশন-সংক্রান্ত বিবেচনা সিদ্ধান্তকে কীভাবে প্রভাবিত করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি team আরও বেশি customer data collect করতে চায়, কারণ পরে সেটা কাজে লাগতে পারে। data minimization আর retention-এর বিবেচনা decision-টাকে কীভাবে influence করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that data minimization means collecting only data needed for a defined, current purpose.
  Rationale: Named principle.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Explain that extra data increases breach impact, compliance obligations and cost.
  Rationale: Risk of over-collection.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Define retention periods and deletion for any data collected.
  Rationale: Named principle.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Note legal requirements and customer expectations or consent.
  Rationale: Compliance.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Require a concrete use case before collecting new fields.
  Rationale: Decision rule.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER057

cybersecurity_digital_safety; medium.

### en

A company receives a report that confidential information may have been emailed to the wrong external recipient. Describe a practical incident-response sequence.

### bn

একটি প্রতিষ্ঠান খবর পেয়েছে যে গোপনীয় তথ্য হয়তো ভুল করে বাইরের একজন প্রাপকের কাছে ইমেইল করা হয়েছে। একটি বাস্তবসম্মত ইনসিডেন্ট রেসপন্সের ধাপক্রম বর্ণনা করুন।

### bn_cs

একটি company report পেয়েছে যে confidential তথ্য হয়তো ভুল করে বাইরের একজন recipient-এর কাছে email করা হয়েছে। একটি practical incident-response sequence describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Confirm what was sent, to whom and when.
  Rationale: Scope.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Contact the recipient promptly to request deletion and confirmation, and attempt recall if available.
  Rationale: Containment.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Report to privacy or security staff to assess impact and notification obligations.
  Rationale: Escalation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Document the incident and actions taken.
  Rationale: Record.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Identify preventive measures, such as autocomplete changes or external-recipient warnings.
  Rationale: Prevention.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER077

cybersecurity_digital_safety; medium.

### en

A CI/CD pipeline has permission to deploy directly to production from every branch. Explain the security risks and a safer deployment-control design.

### bn

একটি সিআই/সিডি পাইপলাইনের যেকোনো ব্রাঞ্চ থেকে সরাসরি প্রোডাকশনে ডিপ্লয় করার অনুমতি আছে। এর নিরাপত্তা-ঝুঁকি এবং ডিপ্লয়মেন্ট নিয়ন্ত্রণের একটি নিরাপদ নকশা ব্যাখ্যা করুন।

### bn_cs

একটি CI/CD pipeline-এর যেকোনো branch থেকে সরাসরি production-এ deploy করার permission আছে। এর security risk আর deployment control-এর একটি safe design explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that any branch, including untested or malicious changes, can reach production.
  Rationale: Core risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Explain that compromised pipeline credentials or branches give a path to production.
  Rationale: Supply-chain risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Restrict production deployment to a protected branch with required review and passing tests.
  Rationale: Core control.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Require approval for production deploys and separate pipeline credentials by environment.
  Rationale: Additional controls.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Log deployments and provide rollback.
  Rationale: Accountability.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC024

decision_support; medium.

### en

A five-person project team needs task tracking, file sharing, and discussion. Explain how to decide whether one integrated platform or several specialized tools is more appropriate.

### bn

পাঁচজনের একটি প্রজেক্ট টিমের কাজ ট্র্যাক করা, ফাইল শেয়ার করা এবং আলোচনার ব্যবস্থা দরকার। একটি সমন্বিত প্ল্যাটফর্ম নাকি কয়েকটি আলাদা বিশেষায়িত টুল বেশি উপযুক্ত, তা কীভাবে ঠিক করবেন ব্যাখ্যা করুন।

### bn_cs

পাঁচজনের একটি project team-এর task tracking, file sharing আর discussion-এর ব্যবস্থা দরকার। একটি integrated platform নাকি কয়েকটি আলাদা specialized tool বেশি উপযুক্ত, তা কীভাবে decide করবেন explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Assess whether an integrated platform meets each need (tracking, files, discussion) adequately.
  Rationale: Fit.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Weigh the overhead of switching between multiple tools against the capability of specialized tools.
  Rationale: Core trade-off.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Consider cost, learning effort and tools the team already uses.
  Rationale: Practicality.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Consider integration between tools if several are chosen.
  Rationale: Practicality.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC084

decision_support; medium.

### en

A department wants to standardize a process that different teams currently perform in different ways. Explain what should be standardized and where flexibility may still be useful.

### bn

একটি বিভাগ এমন একটি প্রক্রিয়াকে একই মানদণ্ডে আনতে চায়, যা বিভিন্ন টিম এখন ভিন্ন ভিন্নভাবে করে। কোন অংশগুলো একরকম করা উচিত এবং কোথায় নমনীয়তা এখনো কাজে আসতে পারে তা ব্যাখ্যা করুন।

### bn_cs

একটি department এমন একটি process standardize করতে চায়, যেটা বিভিন্ন team এখন আলাদা আলাদাভাবে করে। কোন অংশগুলো standardize করা উচিত এবং কোথায় flexibility এখনো কাজে আসতে পারে তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Standardize elements that affect quality, compliance, handoffs or reporting.
  Rationale: What to standardize.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Keep flexibility where teams have legitimately different needs or where local variation does not harm outcomes.
  Rationale: Where flexibility helps.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Compare current team practices to find what works best.
  Rationale: Evidence base.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Involve the teams and review the standard after adoption.
  Rationale: Adoption.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC092

decision_support; easy.

### en

A delivery is expected today but tracking has not updated since yesterday. Explain how to plan without assuming either that it will arrive or that it is lost.

### bn

আজ একটি পার্সেল আসার কথা, কিন্তু গতকাল থেকে ট্র্যাকিং আপডেট হয়নি। এটি আসবেই অথবা হারিয়ে গেছে—কোনোটিই ধরে না নিয়ে কীভাবে পরিকল্পনা করবেন তা ব্যাখ্যা করুন।

### bn_cs

আজ একটি delivery আসার কথা, কিন্তু গতকাল থেকে tracking update হয়নি। এটা আসবেই অথবা lost হয়ে গেছে—কোনোটাই ধরে না নিয়ে কীভাবে plan করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Plan for both outcomes, such as preparing a fallback if the item is needed today.
  Rationale: Explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Contact the carrier or seller for status.
  Rationale: Information.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Explain that delayed tracking updates are common and do not by themselves show loss.
  Rationale: Avoids assuming loss.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Set a time to escalate or file a claim if it does not arrive.
  Rationale: Decision trigger.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC099

decision_support; hard.

### en

An organization must decide whether to adopt a new technology with strong potential benefits but limited long-term evidence. Explain how to use pilots, reversibility, monitoring, exit criteria, and staged commitment.

### bn

একটি প্রতিষ্ঠানকে সিদ্ধান্ত নিতে হবে, সম্ভাব্য উপকার অনেক কিন্তু দীর্ঘমেয়াদি প্রমাণ সীমিত—এমন একটি নতুন প্রযুক্তি গ্রহণ করবে কি না। পাইলট, সিদ্ধান্ত ফিরিয়ে নেওয়ার সুযোগ, মনিটরিং, সরে আসার মানদণ্ড এবং ধাপে ধাপে প্রতিশ্রুতি কীভাবে ব্যবহার করবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি প্রতিষ্ঠানকে decide করতে হবে, potential benefit অনেক কিন্তু long-term evidence সীমিত—এমন একটি নতুন technology adopt করবে কি না। pilot, reversibility, monitoring, exit criteria আর staged commitment কীভাবে ব্যবহার করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Start with a limited pilot to gather evidence.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Prefer reversible commitments, such as avoiding lock-in and keeping the old option available.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Define metrics and monitoring for benefits and harms.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Define exit criteria in advance for stopping or rolling back.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Expand in stages based on evidence at each stage.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC022

procedural_instructional; easy.

### en

Describe a simple procedure for taking useful notes from an academic article without copying entire paragraphs.

### bn

পুরো অনুচ্ছেদ হুবহু না টুকে একটি একাডেমিক প্রবন্ধ থেকে কাজে লাগার মতো নোট নেওয়ার একটি সহজ পদ্ধতি বর্ণনা করুন।

### bn_cs

পুরো paragraph হুবহু copy না করে একটি academic article থেকে কাজে লাগার মতো note নেওয়ার একটি simple procedure describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Write notes in your own words, summarizing key points.
  Rationale: Core requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Record the full citation and page numbers.
  Rationale: Source tracking.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Use quotation marks for any short direct quotes.
  Rationale: Avoids plagiarism.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Note the article's question, method, findings and limitations.
  Rationale: Useful structure.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC042

procedural_instructional; easy.

### en

Describe the steps for confirming a hotel reservation before leaving home.

### bn

বাসা থেকে বের হওয়ার আগে হোটেলের রিজার্ভেশন নিশ্চিত করার ধাপগুলো বর্ণনা করুন।

### bn_cs

বাসা থেকে বের হওয়ার আগে hotel reservation confirm করার step-গুলো describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check the confirmation details: dates, name, room type and number of guests.
  Rationale: Core check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Contact the hotel directly to confirm the reservation.
  Rationale: Confirmation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Confirm check-in time and late arrival arrangements.
  Rationale: Practicality.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Keep the confirmation number accessible offline.
  Rationale: Access.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC050

procedural_instructional; hard.

### en

A multi-day trip includes several prepaid reservations with cancellation deadlines. Propose a procedure for tracking confirmations, deadlines, changes, and backup plans.

### bn

কয়েক দিনের একটি ভ্রমণে অগ্রিম টাকা দেওয়া কয়েকটি রিজার্ভেশন আছে, যেগুলোর বাতিল করার নির্দিষ্ট শেষ সময় আছে। নিশ্চিতকরণ, সময়সীমা, পরিবর্তন এবং বিকল্প পরিকল্পনার হিসাব রাখার একটি পদ্ধতি প্রস্তাব করুন।

### bn_cs

কয়েক দিনের একটি trip-এ অগ্রিম টাকা দেওয়া কয়েকটি reservation আছে, যেগুলোর cancellation deadline আছে। confirmation, deadline, পরিবর্তন আর backup plan track করার একটি procedure propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Keep one list of reservations with confirmation numbers and cancellation terms.
  Rationale: Tracking.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Add cancellation deadlines to a calendar with reminders before each.
  Rationale: Deadlines.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Record any changes and reconfirm after changes.
  Rationale: Changes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Identify backup options for key reservations.
  Rationale: Backup.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC077

procedural_instructional; medium.

### en

A reimbursement request is missing one receipt but includes other supporting information. Explain how to document and review the exception without inventing evidence.

### bn

একটি খরচ ফেরতের আবেদনে একটি রসিদ নেই, তবে অন্যান্য সহায়ক তথ্য আছে। কোনো প্রমাণ বানিয়ে না দিয়ে এই ব্যতিক্রমটি কীভাবে নথিভুক্ত ও পর্যালোচনা করবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি reimbursement request-এ একটি receipt নেই, তবে অন্যান্য supporting information আছে। কোনো evidence বানিয়ে না দিয়ে এই exception-টা কীভাবে document আর review করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Document the missing receipt explicitly, such as in a signed missing-receipt statement with date, amount and purpose.
  Rationale: Transparency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Attach other supporting evidence, such as a card statement or booking confirmation.
  Rationale: Supporting evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Do not create or alter a receipt; honest documentation of the gap complies.
  Rationale: Explicit constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Have the exception reviewed by an approver under the policy.
  Rationale: Review.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC086

procedural_instructional; medium.

### en

Explain how to migrate a recurring manual spreadsheet task into a more structured workflow without losing the ability to verify results.

### bn

নিয়মিত হাতে করা একটি স্প্রেডশিটের কাজকে কীভাবে আরও কাঠামোবদ্ধ ওয়ার্কফ্লোতে নেওয়া যায়, অথচ ফলাফল যাচাই করার সুযোগ হারায় না, তা ব্যাখ্যা করুন।

### bn_cs

নিয়মিত manually করা একটি spreadsheet task-কে কীভাবে আরও structured workflow-তে migrate করা যায়, অথচ result verify করার সুযোগ হারায় না, তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Document the current steps, inputs and outputs.
  Rationale: Understanding.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Design the structured workflow, such as templates, validation rules or scripts.
  Rationale: Migration.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Run the old and new processes in parallel and compare results before switching.
  Rationale: Verification.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Keep checks or logs in the new workflow so results remain verifiable.
  Rationale: Ongoing verification.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Keep the original spreadsheet until the new workflow is validated.
  Rationale: Rollback.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN007

information_synthesis; medium.

### en

Summarize the following without overstating certainty: A pilot with 40 users found fewer support requests after training. The users volunteered for the pilot. No control group was used. Satisfaction scores were high.

### bn

নিশ্চয়তাকে বাড়িয়ে না বলে নিচের তথ্যগুলো সংক্ষেপ করুন: ৪০ জন ব্যবহারকারীকে নিয়ে করা একটি পাইলটে দেখা গেছে, প্রশিক্ষণের পর সাপোর্ট অনুরোধ কমেছে। ব্যবহারকারীরা স্বেচ্ছায় পাইলটে যোগ দিয়েছিলেন। কোনো কন্ট্রোল গ্রুপ ছিল না। সন্তুষ্টির স্কোর বেশি ছিল।

### bn_cs

certainty-কে বাড়িয়ে না বলে নিচের তথ্যগুলো summarize করুন: ৪০ জন user নিয়ে করা একটি pilot-এ দেখা গেছে, training-এর পর support request কমেছে। user-রা স্বেচ্ছায় pilot-এ যোগ দিয়েছিলেন। কোনো control group ছিল না। satisfaction score বেশি ছিল।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that support requests were fewer after training in a 40-user pilot.
  Rationale: Result.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that users volunteered and there was no control group, so the decrease cannot be attributed to training with confidence.
  Rationale: Limitations.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): State that satisfaction scores were high.
  Rationale: Result.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Do not claim the training proved effective; hedged wording complies.
  Rationale: Explicit constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN012

information_synthesis; easy.

### en

Compare two travel options: Train takes 3 hours and costs $65 with downtown arrival. Flight takes 1 hour and costs $110 but requires 45 minutes of airport travel at each end.

### bn

দুটি যাতায়াত-বিকল্প তুলনা করুন: ট্রেনে লাগে ৩ ঘণ্টা, খরচ ৬৫ ডলার, এবং শহরের কেন্দ্রে গিয়ে পৌঁছায়। ফ্লাইটে লাগে ১ ঘণ্টা, খরচ ১১০ ডলার, কিন্তু দুই প্রান্তেই বিমানবন্দরে আসা-যাওয়ায় ৪৫ মিনিট করে লাগে।

### bn_cs

দুটি travel option compare করুন: train-এ লাগে ৩ ঘণ্টা, খরচ ৬৫ ডলার, এবং downtown-এ গিয়ে পৌঁছায়। flight-এ লাগে ১ ঘণ্টা, খরচ ১১০ ডলার, কিন্তু দুই প্রান্তেই airport-এ আসা-যাওয়ায় ৪৫ মিনিট করে লাগে।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that the train takes 3 hours, costs $65 and arrives downtown.
  Rationale: Facts.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that the flight takes 1 hour plus 45 minutes of airport travel at each end, about 2.5 hours, and costs $110.
  Rationale: Facts with total.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Conclude that the flight saves only about 30 minutes for $45 more.
  Rationale: Comparison.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Note that airport check-in or security time may further reduce the flight's advantage, if mentioned as unstated.
  Rationale: Caveat.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Adding check-in time is acceptable only if flagged as an assumption. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN022

information_synthesis; easy.

### en

Summarize this project timeline in order: Requirements approved January 8. Development began January 15. Testing began February 12. Launch occurred March 1.

### bn

প্রজেক্টের এই সময়রেখা ক্রম অনুযায়ী সংক্ষেপ করুন: চাহিদাগুলো অনুমোদিত হয় ৮ জানুয়ারি। ডেভেলপমেন্ট শুরু হয় ১৫ জানুয়ারি। টেস্টিং শুরু হয় ১২ ফেব্রুয়ারি। চালু করা হয় ১ মার্চ।

### bn_cs

project-এর এই timeline order অনুযায়ী summarize করুন: requirement approve হয় ৮ জানুয়ারি। development শুরু হয় ১৫ জানুয়ারি। testing শুরু হয় ১২ ফেব্রুয়ারি। launch হয় ১ মার্চ।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State requirements approval on January 8.
  Rationale: Date.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State development began January 15.
  Rationale: Date.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State testing began February 12.
  Rationale: Date.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): State launch on March 1.
  Rationale: Date.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN036

information_synthesis; medium.

### en

Extract the scheduling constraints and identify whether they can all be satisfied: Meeting must be 60 minutes. Alex is available 9–11 AM. Priya is available 10 AM–noon. Sam is available 10:30–11:30 AM.

### bn

সময়সূচির শর্তগুলো বের করুন এবং সবগুলো একসঙ্গে পূরণ করা সম্ভব কি না তা নির্ণয় করুন: মিটিংটি ৬০ মিনিটের হতে হবে। অ্যালেক্স সকাল ৯টা থেকে ১১টা পর্যন্ত ফাঁকা। প্রিয়া সকাল ১০টা থেকে দুপুর ১২টা পর্যন্ত ফাঁকা। স্যাম সকাল ১০টা ৩০ মিনিট থেকে ১১টা ৩০ মিনিট পর্যন্ত ফাঁকা।

### bn_cs

scheduling constraint-গুলো extract করুন এবং সবগুলো একসঙ্গে satisfy করা সম্ভব কি না তা identify করুন: meeting-টা ৬০ মিনিটের হতে হবে। অ্যালেক্স সকাল ৯টা থেকে ১১টা পর্যন্ত available। প্রিয়া সকাল ১০টা থেকে দুপুর ১২টা পর্যন্ত available। স্যাম সকাল ১০টা ৩০ মিনিট থেকে ১১টা ৩০ মিনিট পর্যন্ত available।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): List the constraints: 60 minutes; Alex 9–11, Priya 10–12, Sam 10:30–11:30.
  Rationale: Extraction.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Identify that the common availability is 10:30–11:00, only 30 minutes.
  Rationale: Calculation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Conclude that the constraints cannot all be satisfied.
  Rationale: Answer.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Suggest options, such as shortening the meeting or asking someone to extend availability.
  Rationale: Useful.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN090

information_synthesis; hard.

### en

Create a balanced risk assessment: A system has had no major incidents in two years. It runs on unsupported software. Network access is tightly restricted. Full backups are tested quarterly. The application cannot be patched without replacing a core component.

### bn

একটি ভারসাম্যপূর্ণ ঝুঁকি-মূল্যায়ন তৈরি করুন: একটি সিস্টেমে দুই বছরে কোনো বড় ঘটনা ঘটেনি। এটি এমন সফটওয়্যারে চলে, যার আর সাপোর্ট দেওয়া হয় না। নেটওয়ার্ক অ্যাক্সেস কঠোরভাবে সীমিত। পূর্ণ ব্যাকআপ প্রতি তিন মাসে পরীক্ষা করা হয়। একটি মূল কম্পোনেন্ট না বদলে অ্যাপ্লিকেশনটি প্যাচ করা যায় না।

### bn_cs

একটি balanced risk assessment তৈরি করুন: একটি system-এ দুই বছরে কোনো major incident ঘটেনি। এটা unsupported software-এ চলে। network access কঠোরভাবে restricted। full backup quarterly test করা হয়। একটি core component replace না করে application-টা patch করা যায় না।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify unsupported software that cannot be patched without replacing a core component as the main risk.
  Rationale: Main risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Note that tight network restriction reduces exposure.
  Rationale: Mitigating control.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Note that quarterly tested full backups support recovery.
  Rationale: Mitigating control.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Note that two years without major incidents does not prove low future risk.
  Rationale: Avoids false reassurance.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Suggest planning replacement of the core component.
  Rationale: Direction.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH007

technical_troubleshooting; medium.

### en

A laptop battery drains unusually fast even when only basic applications are open. Describe what evidence you would collect before deciding the battery itself is faulty.

### bn

শুধু সাধারণ কিছু অ্যাপ্লিকেশন খোলা থাকলেও একটি ল্যাপটপের ব্যাটারি অস্বাভাবিক দ্রুত ফুরিয়ে যাচ্ছে। ব্যাটারিটিই ত্রুটিপূর্ণ—এই সিদ্ধান্ত নেওয়ার আগে কী কী প্রমাণ সংগ্রহ করবেন তা বর্ণনা করুন।

### bn_cs

শুধু basic কিছু application open থাকলেও একটি laptop-এর battery অস্বাভাবিক দ্রুত drain হচ্ছে। battery নিজেই faulty—এই decision নেওয়ার আগে কী কী প্রমাণ collect করবেন তা describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check battery health or capacity reports.
  Rationale: Battery evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Check which processes or apps use the most power or CPU in the background.
  Rationale: Software cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check power settings and display brightness.
  Rationale: Settings cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Compare drain in safe mode or after closing background apps.
  Rationale: Isolation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Explain how a possible result points to battery fault versus software or settings.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without interpretation.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH032

technical_troubleshooting; easy.

### en

A user can connect to a database server but cannot see a table they expect. Describe likely permission and schema-related checks.

### bn

একজন ব্যবহারকারী ডেটাবেস সার্ভারে সংযুক্ত হতে পারছেন, কিন্তু যে টেবিলটি থাকার কথা সেটি দেখতে পাচ্ছেন না। অনুমতি ও স্কিমা-সংক্রান্ত সম্ভাব্য পরীক্ষাগুলো বর্ণনা করুন।

### bn_cs

একজন user database server-এ connect করতে পারছেন, কিন্তু যে table-টা থাকার কথা সেটা দেখতে পাচ্ছেন না। সম্ভাব্য permission আর schema-related check-গুলো describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check that the user has permission on the table or schema.
  Rationale: Likely cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Check that they are connected to the correct database and schema, or that the table exists there.
  Rationale: Likely cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check name qualification or case sensitivity.
  Rationale: Common cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Compare with a user who can see the table.
  Rationale: Isolation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH056

technical_troubleshooting; medium.

### en

Cloud costs increased sharply this month without an obvious traffic increase. Explain what usage and configuration evidence you would inspect before drawing conclusions.

### bn

ট্রাফিক চোখে পড়ার মতো না বাড়লেও এই মাসে ক্লাউডের খরচ হঠাৎ অনেক বেড়ে গেছে। কোনো উপসংহারে পৌঁছানোর আগে ব্যবহার ও কনফিগারেশন-সংক্রান্ত কোন কোন প্রমাণ খতিয়ে দেখবেন তা ব্যাখ্যা করুন।

### bn_cs

traffic চোখে পড়ার মতো না বাড়লেও এই মাসে cloud cost হঠাৎ অনেক বেড়ে গেছে। কোনো conclusion-এ পৌঁছানোর আগে usage আর configuration-এর কোন কোন প্রমাণ inspect করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Break down costs by service, account and resource to locate the increase.
  Rationale: Locates the cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check for new or forgotten resources, such as idle instances or snapshots.
  Rationale: Common cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check configuration changes, such as instance sizes, autoscaling, storage tiers or logging levels.
  Rationale: Common cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Check data transfer and egress charges.
  Rationale: Common cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Check pricing or billing changes and credits ending.
  Rationale: Non-usage cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH060

technical_troubleshooting; hard.

### en

A managed database has normal CPU usage but application latency is rising. Design an investigation that considers connection saturation, locks, storage latency, slow queries, and network path.

### bn

একটি ম্যানেজড ডেটাবেসে সিপিইউ ব্যবহার স্বাভাবিক, কিন্তু অ্যাপ্লিকেশনের লেটেন্সি বাড়ছে। কানেকশন স্যাচুরেশন, লক, স্টোরেজ লেটেন্সি, ধীর কোয়েরি এবং নেটওয়ার্ক পাথ বিবেচনা করে একটি অনুসন্ধান পরিকল্পনা তৈরি করুন।

### bn_cs

একটি managed database-এ CPU-র ব্যবহার স্বাভাবিক, কিন্তু application latency বাড়ছে। connection saturation, lock, storage latency, ধীর query আর network path বিবেচনা করে একটি অনুসন্ধান পরিকল্পনা design করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Check connection counts against limits and pool waits.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check lock waits and blocking queries.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check storage I/O latency.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Identify slow queries from query logs or performance insights.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Measure network latency between app and database.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Correlate latency increases with these metrics to explain which cause applies.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without result interpretation.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH088

technical_troubleshooting; medium.

### en

A data pipeline silently drops a small percentage of records with no obvious error. Design an investigation using source counts, stage-by-stage reconciliation, logs, validation rules, and retry behavior.

### bn

একটি ডেটা পাইপলাইন কোনো স্পষ্ট এরর ছাড়াই নিঃশব্দে অল্প শতাংশ রেকর্ড বাদ দিয়ে ফেলছে। উৎসের রেকর্ড-সংখ্যা, প্রতিটি ধাপে মিলিয়ে দেখা, লগ, ভ্যালিডেশন রুল এবং রিট্রাই আচরণ ব্যবহার করে একটি অনুসন্ধান পরিকল্পনা তৈরি করুন।

### bn_cs

একটি data pipeline কোনো স্পষ্ট error ছাড়াই নিঃশব্দে অল্প শতাংশ record বাদ দিয়ে ফেলছে। source-এর count, প্রতিটি stage-এ মিলিয়ে দেখা, log, validation rule আর retry behavior ব্যবহার করে একটি অনুসন্ধান পরিকল্পনা design করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Compare source record counts with final output counts.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Reconcile counts at each stage to locate where records disappear.
  Rationale: Named area; localizes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Review logs at the losing stage for warnings or skipped records.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check validation rules that may filter records silently.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Check retry behavior, such as records dropped after failed retries.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Compare the dropped records for common characteristics.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P12 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
