# P13 independent review packet

Status: pending. AI-produced draft annotations; no human acceptance is claimed.

Each task needs bilingual equivalence and full-prompt coverage review. Review all critical units, all ambiguity/boundary questions below, and every prespecified ordinary sample item. Additional ordinary units may be reviewed. Blank identity/decision fields are intentional.

24 tasks; 115 RIUs; 51 critical; 20 ordinary sample units; 71 mandatory unit reviews.

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

## CYBER035

cybersecurity_digital_safety; medium.

### en

A network-monitoring system reports an unusual increase in outbound traffic from one workstation. Describe the first steps to validate and investigate the alert.

### bn

একটি নেটওয়ার্ক মনিটরিং সিস্টেম জানাচ্ছে যে একটি ওয়ার্কস্টেশন থেকে বাইরের দিকে যাওয়া ট্রাফিক অস্বাভাবিকভাবে বেড়েছে। অ্যালার্টটি যাচাই ও তদন্ত করার প্রথম ধাপগুলো বর্ণনা করুন।

### bn_cs

একটি network-monitoring system report করছে যে একটি workstation থেকে outbound traffic অস্বাভাবিকভাবে বেড়েছে। alert-টা validate আর investigate করার প্রথম step-গুলো describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Validate the alert by checking traffic volume, destinations, protocols and timing.
  Rationale: Validation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Identify which process or user on the workstation generated the traffic.
  Rationale: Attribution.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Check for legitimate explanations, such as backups, cloud sync or large uploads.
  Rationale: Avoids false positives.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Isolate the workstation if exfiltration or malware is suspected, preserving evidence.
  Rationale: Containment.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Check destinations against threat intelligence.
  Rationale: Malicious indicator.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER046

cybersecurity_digital_safety; medium.

### en

A database backup is encrypted but the encryption key is stored on the same server. Explain the security weakness and a better key-management approach.

### bn

একটি ডেটাবেস ব্যাকআপ এনক্রিপ্ট করা আছে, কিন্তু এনক্রিপশন-কি একই সার্ভারে রাখা হয়েছে। এর নিরাপত্তা-দুর্বলতা এবং কি-ম্যানেজমেন্টের একটি ভালো পদ্ধতি ব্যাখ্যা করুন।

### bn_cs

একটি database backup encrypt করা আছে, কিন্তু encryption key একই server-এ রাখা হয়েছে। এর security weakness আর key management-এর একটি ভালো approach explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that anyone who compromises the server gets both the backup and its key, so encryption adds little protection.
  Rationale: Core weakness.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Store keys separately, such as in a key management service or hardware security module, with restricted access.
  Rationale: Better approach.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Rotate keys and log key access.
  Rationale: Key hygiene.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Keep a secure, recoverable key backup so backups can still be restored.
  Rationale: Avoids unrecoverable backups.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER082

cybersecurity_digital_safety; easy.

### en

A website asks a user to accept all tracking cookies before continuing. Explain what privacy considerations the user should understand.

### bn

একটি ওয়েবসাইট সামনে এগোনোর আগে ব্যবহারকারীকে সব ট্র্যাকিং কুকি গ্রহণ করতে বলছে। ব্যবহারকারীর কোন কোন প্রাইভেসি-বিষয়ক দিক বোঝা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি website সামনে এগোনোর আগে user-কে সব tracking cookie accept করতে বলছে। user-এর কোন কোন privacy consideration বোঝা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that tracking cookies can follow browsing across sites and build a profile for advertising or data sharing.
  Rationale: Core consideration.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Distinguish necessary cookies from tracking or advertising cookies.
  Rationale: Understanding choices.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Point out options such as rejecting non-essential cookies, managing preferences or leaving the site.
  Rationale: User choice.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Mention browser controls such as blocking third-party cookies or clearing cookies.
  Rationale: Further protection.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. No jurisdiction-specific law required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER090

cybersecurity_digital_safety; hard.

### en

An organization wants to use security telemetry for a new purpose unrelated to the reason it was originally collected. Explain how purpose limitation, consent, necessity, and governance should be considered.

### bn

একটি প্রতিষ্ঠান সিকিউরিটি টেলিমেট্রি এমন একটি নতুন কাজে ব্যবহার করতে চায়, যার সঙ্গে মূলত যে কারণে তা সংগ্রহ করা হয়েছিল তার কোনো সম্পর্ক নেই। উদ্দেশ্য-সীমাবদ্ধতা, সম্মতি, প্রয়োজনীয়তা এবং গভর্নেন্স কীভাবে বিবেচনা করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি প্রতিষ্ঠান security telemetry এমন একটি নতুন purpose-এ ব্যবহার করতে চায়, যার সঙ্গে মূলত যে কারণে সেটা collect করা হয়েছিল তার কোনো সম্পর্ক নেই। purpose limitation, consent, necessity আর governance কীভাবে বিবেচনা করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that purpose limitation means data collected for security should not be reused for incompatible purposes without justification or a new legal basis.
  Rationale: Named principle.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Ask whether people were informed or consented, and whether the new use would surprise them.
  Rationale: Named principle.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Assess whether the new purpose needs this data or could use less or aggregated data.
  Rationale: Named principle.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Require governance review, such as privacy, legal or ethics approval and documentation.
  Rationale: Named principle.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Consider harms such as chilling effects or misuse against employees.
  Rationale: Risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC025

decision_support; medium.

### en

A department needs a survey tool for 500 responses containing no sensitive data. Propose selection criteria covering usability, export, collaboration, cost, accessibility, and data ownership.

### bn

একটি বিভাগের এমন একটি সার্ভে টুল দরকার, যাতে ৫০০টি উত্তর সংগ্রহ করা যাবে এবং কোনো সংবেদনশীল তথ্য থাকবে না। ব্যবহারের সহজতা, ডেটা এক্সপোর্ট, একসঙ্গে কাজ করার সুবিধা, খরচ, অ্যাক্সেসিবিলিটি এবং ডেটার মালিকানা নিয়ে বাছাইয়ের মানদণ্ড প্রস্তাব করুন।

### bn_cs

একটি department-এর এমন একটি survey tool দরকার, যাতে ৫০০টি response collect করা যাবে এবং কোনো sensitive data থাকবে না। usability, export, collaboration, cost, accessibility আর data ownership নিয়ে selection criteria propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Usability for creators and respondents.
  Rationale: Named criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Export of responses in usable formats such as CSV.
  Rationale: Named criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Collaboration among staff on surveys and results.
  Rationale: Named criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Cost at the needed scale of 500 responses.
  Rationale: Named criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Accessibility for respondents with disabilities.
  Rationale: Named criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; prespecified-ordinary-sample): Data ownership and the ability to delete or retain data.
  Rationale: Named criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (critical; all-critical): Explain how to apply the criteria, such as required versus nice-to-have or weighting.
  Rationale: Turns criteria into a selection method.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists criteria without saying how to use them.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC072

decision_support; easy.

### en

A team needs to announce a routine process change that affects everyone next month. Explain what communication channel or combination of channels would be effective.

### bn

একটি টিমকে একটি নিয়মিত প্রক্রিয়াগত পরিবর্তনের ঘোষণা দিতে হবে, যা আগামী মাসে সবার ওপর প্রভাব ফেলবে। কোন যোগাযোগ-মাধ্যম বা মাধ্যমগুলোর কোন সমন্বয় কার্যকর হবে তা ব্যাখ্যা করুন।

### bn_cs

একটি team-কে একটি routine process change-এর announcement দিতে হবে, যেটা আগামী মাসে সবাইকে affect করবে। কোন communication channel বা channel-গুলোর কোন combination effective হবে তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Use a primary written channel that reaches everyone, such as email or the main team channel, with the change, date and actions needed.
  Rationale: Reach and clarity.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Reinforce with a second channel, such as a meeting mention or intranet page.
  Rationale: Combination.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Send a reminder close to the change date.
  Rationale: Timing.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Provide a place for questions.
  Rationale: Feedback.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC085

decision_support; medium.

### en

A new approval rule reduces errors but adds two days to every request. Explain how to evaluate whether the added delay is justified.

### bn

একটি নতুন অনুমোদন-নিয়ম ভুলের সংখ্যা কমিয়েছে, কিন্তু প্রতিটি অনুরোধে দুই দিন করে সময় বাড়িয়েছে। এই বাড়তি দেরি যুক্তিসংগত কি না তা কীভাবে মূল্যায়ন করবেন ব্যাখ্যা করুন।

### bn_cs

একটি নতুন approval rule error কমিয়েছে, কিন্তু প্রতিটি request-এ দুই দিন করে সময় বাড়িয়েছে। এই added delay justified কি না তা কীভাবে evaluate করবেন explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Quantify the errors prevented and their cost or harm.
  Rationale: Benefit side.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Quantify the cost of the two-day delay, such as for urgent requests.
  Rationale: Cost side.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Compare benefit and cost.
  Rationale: Decision.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Consider alternatives such as applying the rule only to high-risk requests or speeding up the approval step.
  Rationale: Alternatives.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC093

decision_support; easy.

### en

A student is unsure whether an assignment will take one hour or three hours. Explain how to plan the evening with that uncertainty.

### bn

একজন শিক্ষার্থী নিশ্চিত নন যে একটি অ্যাসাইনমেন্টে এক ঘণ্টা লাগবে নাকি তিন ঘণ্টা। এই অনিশ্চয়তা মাথায় রেখে সন্ধ্যার পরিকল্পনা কীভাবে করবেন তা ব্যাখ্যা করুন।

### bn_cs

একজন student নিশ্চিত নন যে একটি assignment-এ এক ঘণ্টা লাগবে নাকি তিন ঘণ্টা। এই uncertainty মাথায় রেখে সন্ধ্যার plan কীভাবে করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Start the assignment early in the evening so the longer estimate still fits.
  Rationale: Plans for the worst case.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Check progress after about an hour to re-estimate the remaining time.
  Rationale: Updates the plan.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Keep optional activities flexible until the assignment is done.
  Rationale: Buffer.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Plan by the larger estimate if the deadline is firm.
  Rationale: Risk-aware planning.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC100

decision_support; hard.

### en

A team must make a high-impact decision before all requested evidence will be available. Design a process that documents assumptions, separates known facts from estimates, identifies reversible steps, and defines when the decision should be revisited.

### bn

একটি টিমকে চাওয়া সব প্রমাণ হাতে আসার আগেই উচ্চ প্রভাবের একটি সিদ্ধান্ত নিতে হবে। এমন একটি প্রক্রিয়া তৈরি করুন, যা ধরে নেওয়া বিষয়গুলো লিখে রাখে, নিশ্চিতভাবে জানা তথ্যকে আনুমানিক হিসাব থেকে আলাদা করে, ফিরিয়ে নেওয়া যায় এমন পদক্ষেপ চিহ্নিত করে এবং কখন সিদ্ধান্তটি আবার বিবেচনা করা হবে তা নির্ধারণ করে।

### bn_cs

একটি team-কে চাওয়া সব evidence হাতে আসার আগেই high-impact একটি decision নিতে হবে। এমন একটি process design করুন, যেটা assumption-গুলো document করে, known fact-কে estimate থেকে আলাদা করে, reversible step identify করে এবং কখন decision-টা revisit করা হবে তা নির্ধারণ করে।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Document the assumptions the decision relies on.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Separate known facts from estimates, labeling each.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Identify reversible steps that can proceed now and irreversible steps to delay.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Define when the decision will be revisited, such as when specific evidence arrives or at a set date.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Record who made the decision and the rationale.
  Rationale: Accountability.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC024

procedural_instructional; medium.

### en

A student has gathered many sources but is not sure which are most relevant to the research question. Provide a procedure for screening and prioritizing them.

### bn

একজন শিক্ষার্থী অনেক উৎস সংগ্রহ করেছেন, কিন্তু কোনগুলো তাঁর গবেষণা-প্রশ্নের জন্য সবচেয়ে প্রাসঙ্গিক তা নিশ্চিত নন। উৎসগুলো যাচাই-বাছাই করে অগ্রাধিকার ঠিক করার একটি পদ্ধতি দিন।

### bn_cs

একজন student অনেক source collect করেছেন, কিন্তু কোনগুলো তাঁর research question-এর জন্য সবচেয়ে relevant তা নিশ্চিত নন। source-গুলো screen করে prioritize করার একটি procedure দিন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Restate the research question and define relevance criteria.
  Rationale: Basis for screening.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Screen titles and abstracts against the criteria to sort sources into relevant, maybe and not relevant.
  Rationale: Screening.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Assess quality and credibility of relevant sources.
  Rationale: Prioritization.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Prioritize sources that directly address the question for full reading.
  Rationale: Prioritization.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Keep a log of decisions.
  Rationale: Traceability.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC030

procedural_instructional; hard.

### en

A team is preparing to rerun an experiment six months later. Design a reproducibility checklist that captures code, data, parameters, environment, exclusions, and analysis decisions.

### bn

একটি দল ছয় মাস পরে একটি এক্সপেরিমেন্ট আবার চালানোর প্রস্তুতি নিচ্ছে। কোড, ডেটা, প্যারামিটার, এনভায়রনমেন্ট, বাদ দেওয়ার নিয়ম এবং বিশ্লেষণের সিদ্ধান্তগুলো ধরে রাখে এমন একটি পুনরুৎপাদনযোগ্যতার চেকলিস্ট তৈরি করুন।

### bn_cs

একটি team ছয় মাস পরে একটি experiment আবার rerun করার প্রস্তুতি নিচ্ছে। code, data, parameter, environment, exclusion আর analysis decision capture করে এমন একটি reproducibility checklist তৈরি করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Record the exact code version, such as a commit hash.
  Rationale: Named item.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Archive the exact data version used, with checksums or snapshots.
  Rationale: Named item.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Record all parameters and random seeds.
  Rationale: Named item.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Record the environment, such as package versions or a container.
  Rationale: Named item.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Document exclusion rules and excluded records.
  Rationale: Named item.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Document analysis decisions and their rationale.
  Rationale: Named item.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC035

procedural_instructional; medium.

### en

Explain how to prepare a home before leaving for a two-week trip while avoiding unnecessary tasks.

### bn

দুই সপ্তাহের ভ্রমণে বের হওয়ার আগে অপ্রয়োজনীয় কাজ এড়িয়ে বাসা কীভাবে প্রস্তুত করবেন তা ব্যাখ্যা করুন।

### bn_cs

দুই সপ্তাহের trip-এ বের হওয়ার আগে অপ্রয়োজনীয় task এড়িয়ে বাসা কীভাবে prepare করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Secure the home: lock doors and windows.
  Rationale: Core step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Deal with perishables and empty trash.
  Rationale: Prevents spoilage.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Unplug non-essential appliances or adjust thermostat.
  Rationale: Safety and cost.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Arrange for mail, plants or pets.
  Rationale: Two-week needs.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Focus on tasks that matter for two weeks and skip unnecessary deep cleaning.
  Rationale: Explicit request.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC052

procedural_instructional; easy.

### en

Describe a simple process for confirming an appointment time, location, and required documents.

### bn

একটি অ্যাপয়েন্টমেন্টের সময়, স্থান এবং প্রয়োজনীয় কাগজপত্র নিশ্চিত করার একটি সহজ প্রক্রিয়া বর্ণনা করুন।

### bn_cs

একটি appointment-এর সময়, location আর প্রয়োজনীয় কাগজপত্র confirm করার একটি সহজ process describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Confirm the date and time with the provider.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Confirm the exact location, such as address, room or online link.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Ask for and list the required documents.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Record the confirmation and set a reminder.
  Rationale: Follow-through.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC087

procedural_instructional; medium.

### en

A shared online form collects submissions that must be reviewed by two people. Propose a procedure for intake, assignment, status tracking, decisions, and archiving.

### bn

একটি শেয়ার করা অনলাইন ফর্মে জমা পড়া প্রতিটি আবেদন দুজনকে পর্যালোচনা করতে হয়। আবেদন গ্রহণ, দায়িত্ব ভাগ করে দেওয়া, অবস্থা ট্র্যাক করা, সিদ্ধান্ত এবং আর্কাইভ করার একটি পদ্ধতি প্রস্তাব করুন।

### bn_cs

একটি shared online form-এ জমা পড়া প্রতিটি submission দুজনকে review করতে হয়। intake, assignment, status tracking, decision আর archiving-এর একটি procedure propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Log each submission with an ID in a tracker.
  Rationale: Intake.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Assign two named reviewers to each submission.
  Rationale: Assignment.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Track status through stages until both reviews are done.
  Rationale: Status tracking.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Define how a decision is reached when reviewers disagree.
  Rationale: Decisions.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Archive completed submissions and decisions.
  Rationale: Archiving.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN013

information_synthesis; easy.

### en

Compare these backup options: Local drive requires a one-time $90 purchase and manual backups. Cloud service costs $8 per month and backs up automatically but depends on internet access.

### bn

এই ব্যাকআপ বিকল্পগুলো তুলনা করুন: লোকাল ড্রাইভের জন্য একবারই ৯০ ডলার দিয়ে কিনতে হয় এবং ব্যাকআপ হাতে নিতে হয়। ক্লাউড সার্ভিসের খরচ মাসে ৮ ডলার এবং এটি স্বয়ংক্রিয়ভাবে ব্যাকআপ নেয়, কিন্তু ইন্টারনেট সংযোগের ওপর নির্ভরশীল।

### bn_cs

এই backup option-গুলো compare করুন: local drive-এর জন্য একবারই ৯০ ডলার দিয়ে কিনতে হয় এবং backup manually নিতে হয়। cloud service-এর খরচ মাসে ৮ ডলার এবং এটা automatically backup নেয়, কিন্তু internet access-এর ওপর নির্ভরশীল।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that the local drive costs $90 once but requires manual backups.
  Rationale: Facts.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that the cloud service costs $8 per month, backs up automatically and depends on internet access.
  Rationale: Facts.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Note that the cloud's cumulative cost passes $90 after about 11 to 12 months.
  Rationale: Cost comparison.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Note the trade-off between automatic reliability and manual effort and internet dependence.
  Rationale: Trade-off.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN030

information_synthesis; hard.

### en

Summarize the release history and identify the most plausible point for regression investigation: Version 2.1 launched Monday with no issue. Configuration changed Tuesday evening. Errors began Wednesday morning. Version 2.1 code was unchanged Wednesday. Configuration was rolled back Wednesday afternoon and errors stopped.

### bn

রিলিজের ইতিহাস সংক্ষেপ করুন এবং রিগ্রেশন তদন্তের জন্য সবচেয়ে সম্ভাব্য সূত্রটি চিহ্নিত করুন: ভার্সন ২.১ সোমবার কোনো সমস্যা ছাড়াই চালু হয়। মঙ্গলবার সন্ধ্যায় কনফিগারেশন বদলানো হয়। বুধবার সকালে এরর দেখা দিতে শুরু করে। বুধবার ভার্সন ২.১-এর কোডে কোনো পরিবর্তন হয়নি। বুধবার বিকেলে কনফিগারেশন আগের অবস্থায় ফিরিয়ে নেওয়া হয় এবং এরর বন্ধ হয়ে যায়।

### bn_cs

release history summarize করুন এবং regression investigation-এর জন্য সবচেয়ে plausible point-টা identify করুন: Version ২.১ সোমবার কোনো issue ছাড়াই launch হয়। মঙ্গলবার সন্ধ্যায় configuration change করা হয়। বুধবার সকালে error শুরু হয়। বুধবার Version ২.১-এর code-এ কোনো change হয়নি। বুধবার বিকেলে configuration rollback করা হয় এবং error বন্ধ হয়ে যায়।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Summarize the sequence: 2.1 launched Monday without issues, configuration changed Tuesday evening, errors Wednesday morning, rollback Wednesday afternoon stopped errors.
  Rationale: Sequence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Identify the Tuesday evening configuration change as the most plausible regression point.
  Rationale: Answer.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Support it with the evidence: code was unchanged and errors stopped after the configuration rollback.
  Rationale: Justification.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Avoid claiming certainty beyond the evidence, or note other contributors are not excluded.
  Rationale: Calibration.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN037

information_synthesis; medium.

### en

Separate requirements from context: The team currently uses spreadsheets. The new process must preserve historical records, allow two reviewers per request, and launch before October 1. Staff would like mobile access if possible.

### bn

চাহিদা আর প্রেক্ষাপট আলাদা করুন: টিমটি বর্তমানে স্প্রেডশিট ব্যবহার করে। নতুন প্রক্রিয়ায় পুরোনো রেকর্ড সংরক্ষিত রাখতে হবে, প্রতিটি অনুরোধে দুজন রিভিউয়ারের সুযোগ রাখতে হবে এবং ১ অক্টোবরের আগে চালু করতে হবে। সম্ভব হলে কর্মীরা মোবাইল থেকে ব্যবহারের সুবিধা চান।

### bn_cs

requirement আর context আলাদা করুন: team-টা বর্তমানে spreadsheet ব্যবহার করে। নতুন process-এ historical record preserve করতে হবে, প্রতিটি request-এ দুজন reviewer-এর সুযোগ রাখতে হবে এবং ১ অক্টোবরের আগে launch করতে হবে। সম্ভব হলে staff-রা mobile access চান।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify preserving historical records as a requirement.
  Rationale: Requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Identify allowing two reviewers per request as a requirement.
  Rationale: Requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Identify launching before October 1 as a requirement.
  Rationale: Requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Identify current spreadsheet use as context.
  Rationale: Context.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Identify mobile access as a preference, not a requirement.
  Rationale: Preference.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN050

information_synthesis; hard.

### en

Convert this mixed update into completed work, current risks, next actions, and unresolved decisions: Data migration is complete. Validation found a 1.5 percent record mismatch. Users can access the new system. Legacy access remains enabled until Friday. The team has not decided whether the mismatch is acceptable.

### bn

এই মিশ্র আপডেটটিকে সম্পন্ন কাজ, বর্তমান ঝুঁকি, পরবর্তী করণীয় এবং অমীমাংসিত সিদ্ধান্তে ভাগ করুন: ডেটা মাইগ্রেশন সম্পন্ন হয়েছে। যাচাইয়ে ১.৫ শতাংশ রেকর্ডে অমিল পাওয়া গেছে। ব্যবহারকারীরা নতুন সিস্টেমে প্রবেশ করতে পারছেন। পুরোনো সিস্টেমে অ্যাক্সেস শুক্রবার পর্যন্ত চালু থাকবে। অমিলটি গ্রহণযোগ্য কি না, টিম এখনো সে বিষয়ে সিদ্ধান্ত নেয়নি।

### bn_cs

এই mixed update-টাকে completed work, current risk, next action আর unresolved decision-এ ভাগ করুন: data migration complete হয়েছে। validation-এ ১.৫ শতাংশ record mismatch পাওয়া গেছে। user-রা নতুন system access করতে পারছেন। legacy access শুক্রবার পর্যন্ত enabled থাকবে। mismatch-টা acceptable কি না, team এখনো সে বিষয়ে decide করেনি।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Classify data migration and user access to the new system as completed work.
  Rationale: Completed.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Classify the 1.5 percent record mismatch as a current risk.
  Rationale: Risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Classify legacy access ending Friday as a risk or deadline that limits time to resolve the mismatch.
  Rationale: Risk/time.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Identify investigating or resolving the mismatch before Friday as a next action.
  Rationale: Next action.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Classify whether the mismatch is acceptable as an unresolved decision.
  Rationale: Unresolved decision.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN075

information_synthesis; medium.

### en

Determine which hotel satisfies all constraints: Hotel A costs $140, is 5 minutes from the venue, and is nonrefundable. Hotel B costs $120, is 20 minutes away, and is refundable. Budget is $130 and refundable booking is required.

### bn

কোন হোটেল সব শর্ত পূরণ করে তা নির্ধারণ করুন: হোটেল A-এর ভাড়া ১৪০ ডলার, ভেন্যু থেকে ৫ মিনিটের দূরত্বে, এবং টাকা ফেরতযোগ্য নয়। হোটেল B-এর ভাড়া ১২০ ডলার, ২০ মিনিট দূরে, এবং টাকা ফেরতযোগ্য। বাজেট ১৩০ ডলার এবং ফেরতযোগ্য বুকিং বাধ্যতামূলক।

### bn_cs

কোন hotel সব constraint পূরণ করে তা determine করুন: Hotel A-এর ভাড়া ১৪০ ডলার, venue থেকে ৫ মিনিটের দূরত্বে, এবং nonrefundable। Hotel B-এর ভাড়া ১২০ ডলার, ২০ মিনিট দূরে, এবং refundable। budget ১৩০ ডলার এবং refundable booking বাধ্যতামূলক।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that Hotel A fails: $140 exceeds the $130 budget and it is nonrefundable.
  Rationale: Check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that Hotel B satisfies both: $120 and refundable.
  Rationale: Check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Conclude that Hotel B is the option that satisfies all constraints.
  Rationale: Answer.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Note that B is farther (20 minutes) but distance is not a constraint.
  Rationale: Context.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH008

technical_troubleshooting; medium.

### en

A workstation periodically becomes unresponsive for 20 to 30 seconds with no visible error. Propose a diagnostic strategy using system logs and performance indicators to narrow down the root cause.

### bn

একটি ওয়ার্কস্টেশন মাঝে মাঝে ২০ থেকে ৩০ সেকেন্ডের জন্য সাড়া দেওয়া বন্ধ করে দেয়, অথচ কোনো দৃশ্যমান এরর দেখা যায় না। মূল কারণের পরিসর ছোট করে আনতে সিস্টেম লগ ও পারফরম্যান্সের সূচক ব্যবহার করে সমস্যা নির্ণয়ের একটি কৌশল প্রস্তাব করুন।

### bn_cs

একটি workstation মাঝে মাঝে ২০ থেকে ৩০ সেকেন্ডের জন্য unresponsive হয়ে যায়, অথচ কোনো visible error দেখা যায় না। root কারণ narrow down করতে system log আর performance indicator ব্যবহার করে একটি diagnostic strategy propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Record when freezes happen to correlate them with logs and metrics.
  Rationale: Correlation basis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Review system event logs around freeze times.
  Rationale: Named evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Monitor CPU, memory, disk and network indicators during freezes.
  Rationale: Named evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check scheduled tasks or background processes coinciding with freezes.
  Rationale: Likely cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Explain how a possible correlation narrows the root cause.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Collects data without interpretation.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH033

technical_troubleshooting; easy.

### en

An imported CSV has dates displayed incorrectly in a database table. Explain what should be verified before modifying the stored data.

### bn

ইমপোর্ট করা একটি সিএসভি ফাইলের তারিখগুলো ডেটাবেস টেবিলে ভুলভাবে দেখাচ্ছে। সংরক্ষিত ডেটা পরিবর্তন করার আগে কী কী যাচাই করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

import করা একটি CSV-র date-গুলো database table-এ ভুলভাবে দেখাচ্ছে। stored data modify করার আগে কী কী verify করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check whether the stored values are wrong or only displayed differently, such as display format or time zone.
  Rationale: Avoids unnecessary changes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Check the date format in the source CSV against the import format, such as day-month versus month-day.
  Rationale: Likely cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Check the column data type in the table.
  Rationale: Cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Back up the table before modifying stored data; read-only checks comply.
  Rationale: Safeguard.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH039

technical_troubleshooting; hard.

### en

A database transaction occasionally deadlocks under peak load. Explain what evidence you would collect and how you would reason about lock order, transaction scope, indexing, and concurrency.

### bn

সর্বোচ্চ লোডের সময় একটি ডেটাবেস ট্রানজ্যাকশনে মাঝে মাঝে ডেডলক হচ্ছে। কী কী প্রমাণ সংগ্রহ করবেন এবং লক নেওয়ার ক্রম, ট্রানজ্যাকশনের পরিসর, ইনডেক্সিং ও কনকারেন্সি নিয়ে কীভাবে বিশ্লেষণ করবেন তা ব্যাখ্যা করুন।

### bn_cs

peak load-এর সময় একটি database transaction-এ মাঝে মাঝে deadlock হচ্ছে। কী কী প্রমাণ collect করবেন এবং lock order, transaction scope, indexing আর concurrency নিয়ে কীভাবে reasoning করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Collect deadlock graphs or logs showing the transactions and resources involved.
  Rationale: Evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check whether transactions acquire locks in different orders.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Check whether transactions are longer or broader than needed.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check whether missing indexes cause scans that lock more rows.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Relate deadlocks to concurrency levels at peak load.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Explain how a possible finding in the deadlock evidence points to a specific cause.
  Rationale: Reasoning.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists areas without interpreting evidence.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH057

technical_troubleshooting; medium.

### en

A serverless function succeeds for small requests but times out for larger ones. Explain how to investigate execution limits, downstream calls, memory, and payload size.

### bn

একটি সার্ভারলেস ফাংশন ছোট রিকোয়েস্টে সফল হয়, কিন্তু বড় রিকোয়েস্টে টাইমআউট হয়ে যায়। এক্সিকিউশনের সীমা, ডাউনস্ট্রিম কল, মেমরি এবং পেলোডের আকার কীভাবে খতিয়ে দেখবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি serverless function ছোট request-এ সফল হয়, কিন্তু বড় request-এ time out হয়ে যায়। execution limit, downstream call, memory আর payload size কীভাবে খতিয়ে দেখবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Compare the timeout setting and execution limits with actual duration for large requests.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Measure downstream call latency for large requests.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check memory usage and allocation, since memory can also set CPU.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check payload size limits.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Test increasing request sizes or use traces to explain which factor causes the timeout.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists areas without result interpretation.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH064

technical_troubleshooting; medium.

### en

A desktop shuts down unexpectedly during heavy workloads but stays stable when idle. Explain how to investigate power, temperature, memory, and workload-specific causes.

### bn

একটি ডেস্কটপ ভারী কাজের সময় হঠাৎ বন্ধ হয়ে যায়, কিন্তু কোনো কাজ না চললে স্থিতিশীল থাকে। পাওয়ার, তাপমাত্রা, মেমরি এবং নির্দিষ্ট ধরনের কাজের সঙ্গে সম্পর্কিত কারণগুলো কীভাবে খতিয়ে দেখবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি desktop heavy workload-এর সময় হঠাৎ shut down হয়ে যায়, কিন্তু idle অবস্থায় stable থাকে। power, temperature, memory আর workload-specific কারণগুলো কীভাবে investigate করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Check power supply capacity and stability under load.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Monitor temperatures under load for thermal shutdown.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Test memory stability.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Check whether shutdowns occur only with specific workloads, such as GPU-heavy tasks.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Explain how a possible result points to a specific cause.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without interpretation.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Power off and unplug before inspecting internal components.
  Rationale: Safety.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P13 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
