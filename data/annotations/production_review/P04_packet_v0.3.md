# P04 independent review packet

Status: pending. AI-produced draft annotations; no human acceptance is claimed.

Each task needs bilingual equivalence and full-prompt coverage review. Review all critical units, all ambiguity/boundary questions below, and every prespecified ordinary sample item. Additional ordinary units may be reviewed. Blank identity/decision fields are intentional.

25 tasks; 125 RIUs; 51 critical; 22 ordinary sample units; 77 mandatory unit reviews.

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

## CYBER007

cybersecurity_digital_safety; medium.

### en

A privileged account is used by multiple administrators. Explain the security problems this creates and a safer access model.

### bn

একটি প্রিভিলেজড অ্যাকাউন্ট একাধিক অ্যাডমিনিস্ট্রেটর মিলে ব্যবহার করছেন। এতে কী কী নিরাপত্তা সমস্যা তৈরি হয় এবং অ্যাক্সেসের আরও নিরাপদ মডেল কী হতে পারে তা ব্যাখ্যা করুন।

### bn_cs

একটি privileged account একাধিক administrator মিলে ব্যবহার করছেন। এতে কী কী security problem তৈরি হয় এবং আরও safe একটি access model কী হতে পারে তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that shared use removes individual accountability because actions cannot be attributed to a specific administrator.
  Rationale: The core problem.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Explain that the shared password is hard to protect and rotate, for example when an administrator leaves or the password is shared widely.
  Rationale: A second distinct problem.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Propose individual named administrator accounts or individually attributed privileged access.
  Rationale: The core of a safer model.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Apply least privilege or just-in-time elevation rather than standing full privileges.
  Rationale: Reduces exposure.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Require MFA and logging or session recording for privileged access.
  Rationale: Supports detection and accountability.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. A privileged-access-management vault with checkout and individual attribution satisfies RIU-03. Emergency break-glass accounts may be mentioned but are not required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER017

cybersecurity_digital_safety; medium.

### en

An organization is seeing several similar phishing reports from different departments. Propose how the security team should triage the reports and communicate with users.

### bn

একটি প্রতিষ্ঠানের বিভিন্ন বিভাগ থেকে একই ধরনের কয়েকটি ফিশিং রিপোর্ট আসছে। সিকিউরিটি টিম কীভাবে রিপোর্টগুলো ট্রায়াজ করবে এবং ব্যবহারকারীদের সঙ্গে যোগাযোগ করবে তা প্রস্তাব করুন।

### bn_cs

একটি প্রতিষ্ঠানের বিভিন্ন department থেকে একই ধরনের কয়েকটি phishing report আসছে। security team কীভাবে report-গুলো triage করবে এবং user-দের সঙ্গে communicate করবে তা propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Group the reports into a campaign using shared indicators such as sender, subject, links or attachments.
  Rationale: Recognizes a coordinated campaign.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Determine whether anyone clicked, entered credentials or opened attachments, and prioritize those cases.
  Rationale: Identifies actual compromise risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Contain the campaign, for example by blocking the sender or URLs and removing the messages from mailboxes.
  Rationale: Reduces further exposure.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Communicate to users with a clear warning describing the message and what to do if they interacted with it.
  Rationale: The prompt asks how to communicate with users.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Thank or acknowledge reporters and encourage continued reporting.
  Rationale: Sustains reporting behavior.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. No specific email platform is required. Communication can be targeted or organization-wide if justified. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER022

cybersecurity_digital_safety; easy.

### en

A laptop is lost during travel but was protected by a password. Explain what additional factors determine the data risk.

### bn

ভ্রমণের সময় একটি ল্যাপটপ হারিয়ে গেছে, তবে সেটি পাসওয়ার্ড দিয়ে সুরক্ষিত ছিল। ডেটার ঝুঁকি নির্ধারণে আর কোন কোন বিষয় ভূমিকা রাখে তা ব্যাখ্যা করুন।

### bn_cs

travel-এর সময় একটি laptop হারিয়ে গেছে, তবে সেটা password দিয়ে protected ছিল। data risk নির্ধারণে আর কোন কোন factor ভূমিকা রাখে তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01: Confirm encryption is the single critical factor under the omission-consequence test.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Identify whether the disk was encrypted as a key factor, explaining that a login password alone may not protect data if the drive can be read directly.
  Rationale: Without encryption the password provides limited protection.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Identify the sensitivity of the data stored on the laptop as a factor.
  Rationale: Determines the impact if data is exposed.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Identify whether the laptop was locked or powered off, versus left signed in or asleep, when lost.
  Rationale: Affects whether the password must even be bypassed.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Identify password strength or whether saved sessions and credentials could give access to accounts or cloud services.
  Rationale: Weak passwords or saved sessions extend the risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Identify whether remote lock or wipe is available and whether accounts can be signed out remotely.
  Rationale: Affects how much exposure can be reduced.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. The prompt asks for factors, not a response procedure; actions such as reporting are optional. Specific encryption products are not required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER026

cybersecurity_digital_safety; medium.

### en

A laptop's antivirus detects and quarantines a file used by a business application. Explain how to investigate without simply disabling protection.

### bn

একটি ল্যাপটপের অ্যান্টিভাইরাস একটি ব্যবসায়িক অ্যাপ্লিকেশনের ব্যবহৃত একটি ফাইল শনাক্ত করে কোয়ারেন্টাইনে রেখেছে। শুধু সুরক্ষা বন্ধ করে না দিয়ে কীভাবে বিষয়টি তদন্ত করবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি laptop-এর antivirus একটি business application-এর ব্যবহৃত একটি file detect করে quarantine করেছে। শুধু protection disable না করে কীভাবে বিষয়টা investigate করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-03: Explicit negative constraint: silence passes when the path never disables protection.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify the detection details: the file path, detection name and the file's origin.
  Rationale: The starting evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Verify the file's legitimacy, for example by checking its digital signature, hash reputation, vendor or a multi-engine scan.
  Rationale: Distinguishes a false positive from real malware.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Do not disable antivirus protection to make the application work; a narrowly scoped, verified exclusion or vendor fix complies.
  Rationale: Explicit prompt requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Contact the application vendor or IT security, or submit the file as a false positive.
  Rationale: Escalation path.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Restore the file or add a narrow exclusion only after it is verified as legitimate.
  Rationale: The safe resolution path.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Leaving the file quarantined until verification is acceptable. Exclusions must be specific to the verified file or path. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER030

cybersecurity_digital_safety; hard.

### en

An organization wants to allow personal devices for limited work access. Propose minimum security controls and boundaries that reduce risk without requiring full device ownership.

### bn

একটি প্রতিষ্ঠান সীমিত কাজের অ্যাক্সেসের জন্য কর্মীদের ব্যক্তিগত ডিভাইস ব্যবহারের অনুমতি দিতে চায়। পুরো ডিভাইসের নিয়ন্ত্রণ না নিয়েও ঝুঁকি কমায় এমন ন্যূনতম নিরাপত্তা নিয়ন্ত্রণ ও সীমারেখা প্রস্তাব করুন।

### bn_cs

একটি প্রতিষ্ঠান limited work access-এর জন্য personal device ব্যবহারের অনুমতি দিতে চায়। পুরো device ownership না নিয়েও risk কমায় এমন minimum security control আর boundary propose করুন।

### Boundary and ambiguity questions

- [ ] RIU-03, RIU-06: Separation mechanism (RIU-03) versus stated privacy boundary (RIU-06): confirm both are distinct outcomes.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Require strong authentication such as MFA for work access from personal devices.
  Rationale: The minimum control on account access.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Limit access scope to the work resources needed, such as email or specific apps, rather than full network access.
  Rationale: The prompt specifies limited work access.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Separate work data from personal data, for example with managed work apps or containers, without managing the whole device.
  Rationale: Allows control without full device ownership.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Require baseline device hygiene such as a screen lock, supported operating system and updates, checked at access time where possible.
  Rationale: Reduces the chance the device is compromised.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Provide a way to remove work data or revoke access if the device is lost or the person leaves, limited to work data.
  Rationale: Contains exposure without wiping personal data.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): State the privacy boundary: the organization does not access or wipe personal data.
  Rationale: Defines the ownership boundary the prompt asks for.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Any MAM/MDM product is optional; the boundary is the key concept. Full-device enrolment would contradict the prompt's constraint and is an incorrect path for RIU-03. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC045

decision_support; medium.

### en

A traveler must choose between an early morning flight with lower delay risk and an evening flight that better fits work obligations. Explain how to evaluate the tradeoff.

### bn

একজন যাত্রীকে দেরি হওয়ার ঝুঁকি কম এমন একটি ভোরের ফ্লাইট এবং কাজের দায়িত্বের সঙ্গে বেশি মানানসই একটি সন্ধ্যার ফ্লাইটের মধ্যে বেছে নিতে হবে। এই লাভ-ক্ষতির হিসাব কীভাবে মূল্যায়ন করবেন তা ব্যাখ্যা করুন।

### bn_cs

একজন traveler-কে delay risk কম এমন একটি early morning flight আর work obligation-এর সঙ্গে বেশি মানানসই একটি evening flight-এর মধ্যে বেছে নিতে হবে। এই tradeoff কীভাবে evaluate করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Assess the consequence of a delay on the evening flight, such as missing a fixed-time event at the destination.
  Rationale: Determines how much the lower delay risk matters.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Assess the cost of the early flight to work obligations, such as missed work or meetings.
  Rationale: The other side of the trade-off.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Consider options that reduce either cost, such as working remotely or a buffer.
  Rationale: Practical mitigations.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Consider personal factors such as fatigue or travel to the airport early in the morning.
  Rationale: Affects the real cost.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. No single correct choice. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC052

decision_support; easy.

### en

A team can either finish all planned features or reduce scope to meet the promised date. Explain how to think about the tradeoff.

### bn

একটি টিম হয় পরিকল্পিত সব ফিচার শেষ করতে পারে, নয়তো প্রতিশ্রুত তারিখ রক্ষা করতে কাজের পরিধি কমাতে পারে। এই লাভ-ক্ষতির বিষয়টি কীভাবে ভাববেন তা ব্যাখ্যা করুন।

### bn_cs

একটি team হয় planned সব feature শেষ করতে পারে, নয়তো promised date রক্ষা করতে scope কমাতে পারে। এই tradeoff নিয়ে কীভাবে ভাববেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Assess the consequence of missing the promised date, such as contractual, customer or dependent-team impact.
  Rationale: One side of the trade-off.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Assess which features are essential to the release's value and which could be deferred.
  Rationale: The other side of the trade-off.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Consider quality risk from rushing all features, such as reduced testing.
  Rationale: A hidden cost of keeping full scope.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Communicate the trade-off and decision to stakeholders.
  Rationale: Ensures agreement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. A recommendation is not required. Partial options (phased release) are acceptable as part of RIU-02. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC056

decision_support; medium.

### en

A team can automate a manual process now or continue manually for three months and automate later. Explain how volume, error rate, setup cost, and expected change should affect the decision.

### bn

একটি টিম হাতে করা একটি প্রক্রিয়া এখনই অটোমেট করতে পারে, অথবা আরও তিন মাস হাতে চালিয়ে পরে অটোমেট করতে পারে। কাজের পরিমাণ, ভুলের হার, প্রাথমিক সেটআপের খরচ এবং সম্ভাব্য পরিবর্তন এই সিদ্ধান্তকে কীভাবে প্রভাবিত করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি team হাতে করা একটি process এখনই automate করতে পারে, অথবা আরও তিন মাস manually চালিয়ে পরে automate করতে পারে। volume, error rate, setup cost আর সম্ভাব্য পরিবর্তন এই decision-কে কীভাবে affect করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-03: Criticality boundary: confirm setup cost as supporting while volume, error rate and change are critical.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that higher volume favors automating sooner because savings accumulate faster.
  Rationale: A named factor with direction.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Explain that a higher error rate in the manual process favors automating sooner.
  Rationale: A named factor with direction.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary): Explain that high setup cost favors waiting unless savings over the period justify it.
  Rationale: A named factor with direction.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Explain that expected changes to the process within three months favor waiting, since automation may need rework.
  Rationale: A named factor with direction.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Combine the factors, for example by comparing three months of manual cost and errors with setup cost and rework risk.
  Rationale: Turns factors into a decision.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = States each factor's direction but does not combine them.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Each factor requires its direction of effect; mere listing fails. Setup cost is supporting because its direction is conditional. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC059

decision_support; hard.

### en

A legacy system is expensive to maintain but replacing it would disrupt several dependent processes. Explain how to structure a keep-versus-replace decision using risk, cost, dependencies, migration effort, and future needs.

### bn

একটি লিগেসি সিস্টেম রক্ষণাবেক্ষণ করা ব্যয়বহুল, কিন্তু এটি বদলালে এর ওপর নির্ভরশীল কয়েকটি প্রক্রিয়া ব্যাহত হবে। ঝুঁকি, খরচ, ডিপেন্ডেন্সি, মাইগ্রেশনের শ্রম এবং ভবিষ্যৎ প্রয়োজন ব্যবহার করে রেখে দেওয়া বনাম বদলানোর সিদ্ধান্ত কীভাবে কাঠামোবদ্ধ করবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি legacy system maintain করা ব্যয়বহুল, কিন্তু এটা replace করলে এর ওপর নির্ভরশীল কয়েকটি process disrupt হবে। risk, cost, dependency, migration effort আর ভবিষ্যৎ প্রয়োজন ব্যবহার করে keep-versus-replace decision কীভাবে structure করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-06: Check the integration unit is not met by a list of factors alone.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Assess risk of keeping the system, such as failure, security or support risk.
  Rationale: A named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Compare total costs over time of maintaining versus replacing, including transition costs.
  Rationale: A named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Map the dependent processes and how each would be affected by replacement.
  Rationale: A named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Estimate migration effort, including data migration, testing and training.
  Rationale: A named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Assess whether the system can meet future needs.
  Rationale: A named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical, identified-ambiguity-or-boundary): Combine the factors into a structured decision, such as a weighted comparison or decision criteria with thresholds.
  Rationale: The prompt asks how to structure the decision.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists the factors but does not say how they are combined or weighed into a decision.
- [ ] **RIU-07** (supporting; prespecified-ordinary-sample): Consider intermediate options such as phased replacement or wrapping the legacy system.
  Rationale: Avoids a false binary.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Named factors are supporting and the integrating structure is critical, mirroring the differential-diagnosis convention for listed dimensions. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC065

decision_support; medium.

### en

A dashboard metric increased after the data pipeline was changed. Explain how to determine whether the increase reflects real behavior or a measurement change.

### bn

ডেটা পাইপলাইন বদলানোর পর ড্যাশবোর্ডের একটি মেট্রিক বেড়ে গেছে। এই বৃদ্ধি বাস্তব আচরণের প্রতিফলন নাকি পরিমাপ পদ্ধতির পরিবর্তনের ফল, তা কীভাবে নির্ধারণ করবেন ব্যাখ্যা করুন।

### bn_cs

data pipeline change করার পর dashboard-এর একটি metric বেড়ে গেছে। এই বৃদ্ধি real behavior-এর প্রতিফলন নাকি measurement change-এর ফল, সেটা কীভাবে determine করবেন explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check whether the increase coincides with the pipeline change date.
  Rationale: Timing is the first discriminator.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Review what changed in the pipeline, such as definitions, filters, deduplication or data sources.
  Rationale: Identifies a measurement mechanism.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Compare the new and old pipeline on the same period, for example by running both in parallel or recomputing history.
  Rationale: A direct test.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check independent or related measures not affected by the change for a matching trend.
  Rationale: Corroborates real behavior.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Annotate or restate the metric if a measurement change is confirmed.
  Rationale: Prevents misleading decisions.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Any comparison method is acceptable. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC002

procedural_instructional; easy.

### en

Describe the steps for creating a clear folder structure for documents from several different projects.

### bn

কয়েকটি ভিন্ন প্রজেক্টের ডকুমেন্টের জন্য একটি পরিষ্কার ফোল্ডার কাঠামো তৈরির ধাপগুলো বর্ণনা করুন।

### bn_cs

কয়েকটি আলাদা project-এর document-এর জন্য একটি clear folder structure তৈরির step-গুলো describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Create a top-level folder per project.
  Rationale: The core organizing principle.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Use consistent subfolders within each project, such as by document type or phase.
  Rationale: Makes projects navigable.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Use a consistent naming convention for folders and files.
  Rationale: Supports findability.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Move existing documents into the structure and avoid duplicates.
  Rationale: Applies the structure.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Keep the structure shallow or document it so others can follow it.
  Rationale: Maintains clarity.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Alternatives such as organizing by client then project are acceptable for RIU-01 if projects remain separate. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC008

procedural_instructional; medium.

### en

A department is migrating years of loosely organized files into a new shared repository. Design a phased procedure for inventory, naming, ownership, permissions, migration, and validation.

### bn

একটি বিভাগ বহু বছরের এলোমেলোভাবে রাখা ফাইল একটি নতুন শেয়ার করা রিপোজিটরিতে সরিয়ে নিচ্ছে। ইনভেন্টরি, নামকরণ, মালিকানা, অনুমতি, স্থানান্তর এবং যাচাইয়ের জন্য ধাপে ধাপে বাস্তবায়নযোগ্য একটি পদ্ধতি তৈরি করুন।

### bn_cs

একটি department বহু বছরের এলোমেলোভাবে রাখা file একটি নতুন shared repository-তে migrate করছে। inventory, naming, ownership, permission, migration আর validation-এর জন্য একটি phased procedure design করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Inventory existing files, identifying what exists, duplicates and obsolete material.
  Rationale: The first phase.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Define a naming convention and apply it during migration.
  Rationale: A named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Assign an owner for each content area or folder.
  Rationale: Ownership drives decisions about what to keep and who may access it.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Define permissions in the new repository according to owners and needs.
  Rationale: Prevents exposure.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Migrate in phases, such as by department area, rather than all at once.
  Rationale: The prompt asks for phases.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Validate the migration by checking counts, access and a sample of files, keeping the source until validated.
  Rationale: Ensures nothing is lost.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Keeping the source until validation is part of RIU-06. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC017

procedural_instructional; medium.

### en

Explain how to close a completed task in a project tracker so the record remains useful for future review.

### bn

প্রজেক্ট ট্র্যাকারে একটি সম্পন্ন কাজ কীভাবে ক্লোজ করলে রেকর্ডটি ভবিষ্যতের পর্যালোচনার জন্য কাজে লাগবে তা ব্যাখ্যা করুন।

### bn_cs

project tracker-এ একটি completed task কীভাবে close করলে record-টা ভবিষ্যতের review-র জন্য কাজে লাগবে তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Record what was done or the outcome before closing.
  Rationale: The core of a useful record.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Link or attach relevant deliverables or evidence.
  Rationale: Allows later review.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Note any decisions, issues or follow-ups, and create follow-up tasks if needed.
  Rationale: Prevents lost loose ends.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Set the status to done with the completion date and owner.
  Rationale: Basic tracking data.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Tracker-specific fields are not required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC055

procedural_instructional; medium.

### en

A service provider gives conflicting instructions by phone and email. Explain how to clarify the correct procedure and keep a useful record.

### bn

একটি সেবা প্রদানকারী প্রতিষ্ঠান ফোনে ও ইমেইলে পরস্পরবিরোধী নির্দেশনা দিয়েছে। সঠিক প্রক্রিয়াটি কীভাবে স্পষ্ট করে নেবেন এবং কাজে লাগার মতো রেকর্ড রাখবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি service provider phone-এ আর email-এ conflicting instruction দিয়েছে। সঠিক procedure-টা কীভাবে clarify করে নেবেন এবং কাজে লাগার মতো record রাখবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Contact the provider to ask which instruction is correct, pointing out the specific conflict.
  Rationale: Resolves the conflict.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Get the confirmed procedure in writing, such as a follow-up email.
  Rationale: Creates a reliable record.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Record the details of each contact: date, time, person spoken to and what was said.
  Rationale: A useful record.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Keep the conflicting messages together with the resolution.
  Rationale: Preserves evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. No escalation is required unless the provider does not resolve the conflict. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC090

procedural_instructional; hard.

### en

An organization wants a repeatable process for granting and removing access across many systems when people change roles. Design the workflow with approvals, timing, verification, and exception handling.

### bn

মানুষের ভূমিকা বদলালে বহু সিস্টেমে অ্যাক্সেস দেওয়া ও সরানোর জন্য একটি প্রতিষ্ঠান পুনরাবৃত্তিযোগ্য প্রক্রিয়া চায়। অনুমোদন, সময়, যাচাই এবং ব্যতিক্রম সামলানোসহ ওয়ার্কফ্লোটি তৈরি করুন।

### bn_cs

মানুষের role বদলালে বহু system-এ access দেওয়া আর সরানোর জন্য একটি প্রতিষ্ঠান repeatable process চায়। approval, timing, verification আর exception handling-সহ workflow-টা design করুন।

### Boundary and ambiguity questions

- [ ] RIU-04, RIU-05, RIU-06: Named components marked supporting; confirm under the omission-consequence test.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Trigger the workflow from an authoritative role-change event, such as an HR record update.
  Rationale: Ensures changes are not missed.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Require approval by an appropriate owner, such as the manager or system owner, before granting new access.
  Rationale: A named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Remove access no longer needed for the new role, not only add new access.
  Rationale: Prevents privilege accumulation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Set timing targets, such as removing old access on the change date and granting new access before the start.
  Rationale: A named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Verify changes were applied in each system, for example through confirmation or periodic access review.
  Rationale: A named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; identified-ambiguity-or-boundary): Handle exceptions with documented justification, an approver and an expiry or review date.
  Rationale: A named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Role-based access templates are acceptable but not required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN039

information_synthesis; hard.

### en

Identify contradictions or tensions in the requirements: The service must be available 24/7. Maintenance requires a two-hour full shutdown each month. No user may experience planned downtime. The budget does not include a redundant environment.

### bn

চাহিদাগুলোর মধ্যে বৈপরীত্য বা টানাপোড়েন চিহ্নিত করুন: সার্ভিসটিকে ২৪/৭ সচল থাকতে হবে। রক্ষণাবেক্ষণের জন্য প্রতি মাসে দুই ঘণ্টা পুরোপুরি বন্ধ রাখতে হয়। কোনো ব্যবহারকারীকেই পরিকল্পিত ডাউনটাইমের মুখে পড়তে হবে না। বাজেটে কোনো রিডান্ড্যান্ট এনভায়রনমেন্ট রাখা হয়নি।

### bn_cs

requirement-গুলোর মধ্যে contradiction বা tension identify করুন: service-টাকে ২৪/৭ available থাকতে হবে। maintenance-এর জন্য প্রতি মাসে দুই ঘণ্টা full shutdown লাগে। কোনো user-কেই planned downtime-এর মুখে পড়তে হবে না। budget-এ কোনো redundant environment রাখা হয়নি।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-02: Check a single sentence naming both conflicts earns both units.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Identify that the monthly two-hour full shutdown contradicts 24/7 availability.
  Rationale: A direct contradiction.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Identify that the shutdown contradicts the requirement that no user experiences planned downtime.
  Rationale: A direct contradiction.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Identify that avoiding downtime during maintenance would normally require redundancy, which the budget excludes.
  Rationale: Explains why the contradiction cannot be resolved as stated.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Suggest a resolution path, such as revising a requirement, funding redundancy or changing the maintenance method.
  Rationale: Useful but not requested.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. RIU-01 and RIU-02 are distinct contradictions. A resolution path is supporting because the prompt asks only to identify. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN048

information_synthesis; medium.

### en

Turn this project note into prioritized actions and dependencies: Security review found two high-risk issues and five low-risk issues. Launch is in ten days. One high-risk issue requires vendor input expected in four days. The other can be fixed internally in two days. Documentation is also incomplete.

### bn

এই প্রজেক্ট নোটটিকে অগ্রাধিকারভিত্তিক করণীয় ও পারস্পরিক নির্ভরতায় রূপ দিন: নিরাপত্তা পর্যালোচনায় দুটি উচ্চ-ঝুঁকির এবং পাঁচটি নিম্ন-ঝুঁকির সমস্যা পাওয়া গেছে। চালু হতে আর দশ দিন বাকি। একটি উচ্চ-ঝুঁকির সমস্যার জন্য ভেন্ডরের মতামত দরকার, যা চার দিনের মধ্যে আসার কথা। অন্যটি দুই দিনের মধ্যে প্রতিষ্ঠানের ভেতরেই ঠিক করা সম্ভব। ডকুমেন্টেশনও অসম্পূর্ণ।

### bn_cs

এই project note-টাকে prioritized action আর dependency-তে রূপ দিন: security review-তে দুটি high-risk আর পাঁচটি low-risk issue পাওয়া গেছে। launch হতে আর দশ দিন বাকি। একটি high-risk issue-র জন্য vendor input দরকার, যেটা চার দিনের মধ্যে আসার কথা। অন্যটা দুই দিনের মধ্যে internally fix করা সম্ভব। documentation-ও incomplete।

### Boundary and ambiguity questions

- [ ] RIU-03: Boundary: is the contingency requirement over-inferred from the note? Draft treats schedule-risk recognition as critical.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Prioritize fixing the internally fixable high-risk issue first (two days).
  Rationale: Highest-risk work with no dependency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Identify that the other high-risk issue depends on vendor input expected in four days.
  Rationale: The key dependency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Identify that the vendor-dependent issue leaves limited time before launch and needs a contingency or launch decision if vendor input is late.
  Rationale: Schedule risk on the critical path.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Place the five low-risk issues after the high-risk ones, or triage them for deferral.
  Rationale: Correct relative priority.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Include completing the documentation as an action.
  Rationale: An explicit item.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Specific day-by-day schedules are optional. The arithmetic (4 days vendor plus fix time within 10 days) need not be exact. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN062

information_synthesis; easy.

### en

Given that 18 of 20 users completed a task successfully after training, state what the data directly supports and what it does not prove about future users.

### bn

প্রশিক্ষণের পর ২০ জন ব্যবহারকারীর মধ্যে ১৮ জন একটি কাজ সফলভাবে শেষ করেছেন—এই তথ্য সরাসরি কী সমর্থন করে এবং ভবিষ্যতের ব্যবহারকারীদের সম্পর্কে কী প্রমাণ করে না তা উল্লেখ করুন।

### bn_cs

training-এর পর ২০ জন user-এর মধ্যে ১৮ জন একটি task successfully শেষ করেছেন—এই data সরাসরি কী support করে এবং future user-দের সম্পর্কে কী prove করে না তা উল্লেখ করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that the data supports that 18 of 20 (90%) of these trained users completed the task.
  Rationale: The directly supported claim.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that it does not prove future users will succeed at the same rate, because the sample is small and may not be representative.
  Rationale: The core limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): State that, without a comparison group, it does not show that the training caused the success.
  Rationale: A second distinct limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Note uncertainty in the 90% estimate, such as a wide confidence range with 20 users.
  Rationale: Quantifies the limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Statistics vocabulary is optional. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN068

information_synthesis; medium.

### en

A controlled experiment finds a small statistically significant improvement, while a larger observational dataset shows no clear difference. Explain how to present both findings without dismissing either source.

### bn

একটি নিয়ন্ত্রিত এক্সপেরিমেন্টে ছোট কিন্তু পরিসংখ্যানগতভাবে তাৎপর্যপূর্ণ উন্নতি পাওয়া গেছে, অথচ এর চেয়ে বড় একটি পর্যবেক্ষণমূলক ডেটাসেটে স্পষ্ট কোনো পার্থক্য দেখা যায়নি। কোনো উৎসকে বাতিল না করে দুটি ফলাফল কীভাবে উপস্থাপন করবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি controlled experiment-এ ছোট কিন্তু statistically significant improvement পাওয়া গেছে, অথচ এর চেয়ে বড় একটি observational dataset-এ clear কোনো difference দেখা যায়নি। কোনো source-কে dismiss না করে দুটি finding কীভাবে present করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Report both findings accurately: a small significant improvement in the experiment and no clear difference in the observational data.
  Rationale: Both must be presented.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Explain differences in design strength: the experiment supports causal inference, while the observational data may be confounded but reflect broader real-world conditions.
  Rationale: Explains why both are informative.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Note that a small effect may be hard to detect in noisy observational data, so no clear difference is not proof of no effect.
  Rationale: Reconciles the findings.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): State an overall conclusion with appropriate uncertainty, such as a possible small effect whose real-world size is uncertain.
  Rationale: The synthesis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Do not dismiss either source; presenting both with their strengths and limits complies.
  Rationale: Explicit prompt constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. No requirement for formal statistics. "Statistically significant" must not be equated with large or important. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN086

information_synthesis; medium.

### en

Create a risk summary without exaggeration: The vendor has announced end of support in nine months. The system is stable today. Migration planning has not begun. Replacement options are available but untested.

### bn

অতিরঞ্জন ছাড়া একটি ঝুঁকি-সারাংশ তৈরি করুন: ভেন্ডর ঘোষণা দিয়েছে যে নয় মাস পর সাপোর্ট বন্ধ হয়ে যাবে। সিস্টেমটি এখন স্থিতিশীল। মাইগ্রেশনের পরিকল্পনা শুরু হয়নি। বিকল্প সমাধান পাওয়া যায়, তবে সেগুলো পরীক্ষা করা হয়নি।

### bn_cs

exaggeration ছাড়া একটি risk summary তৈরি করুন: vendor ঘোষণা দিয়েছে যে নয় মাস পর support বন্ধ হয়ে যাবে। system-টা এখন stable। migration planning শুরু হয়নি। replacement option পাওয়া যায়, তবে সেগুলো untested।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that vendor support ends in nine months.
  Rationale: The core risk timing.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that migration planning has not started, which leaves limited time.
  Rationale: The aggravating factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): State that the system is stable today.
  Rationale: Balances the summary.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): State that replacement options exist but are untested.
  Rationale: Option status.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Avoid exaggeration such as claiming imminent failure or crisis.
  Rationale: Explicit tone requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Exaggeration such as "the system will fail" would also be an unsupported assertion under CHECK-01. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH025

technical_troubleshooting; medium.

### en

A browser extension appears to interfere with a web application, but the behavior is inconsistent. Propose a controlled way to confirm or reject that hypothesis.

### bn

একটি ব্রাউজার এক্সটেনশন একটি ওয়েব অ্যাপ্লিকেশনের কাজে বাধা দিচ্ছে বলে মনে হচ্ছে, কিন্তু সমস্যাটি সব সময় একইভাবে ঘটে না। এই অনুমানটি নিশ্চিত বা বাতিল করার জন্য একটি নিয়ন্ত্রিত উপায় প্রস্তাব করুন।

### bn_cs

একটি browser extension একটি web application-এ interfere করছে বলে মনে হচ্ছে, কিন্তু behavior-টা সবসময় একরকম না। এই hypothesis confirm বা reject করার জন্য একটি নিয়ন্ত্রিত উপায় propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Test the application with the extension disabled or in a clean profile, keeping other conditions the same.
  Rationale: The controlled comparison.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Re-enable the extension and check whether the problem returns.
  Rationale: Confirms causation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Repeat the test several times or over a defined period because the behavior is inconsistent.
  Rationale: Addresses intermittency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Record conditions and results, such as page, action, time and extension state.
  Rationale: Makes the comparison rigorous.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): State what result would confirm the hypothesis and what result would reject it.
  Rationale: The prompt asks to confirm or reject.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Proposes the comparison but does not state confirming and rejecting outcomes.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Testing other extensions is optional. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH045

technical_troubleshooting; medium.

### en

A unit test passes when run alone but fails when the full test suite runs. Propose likely causes and a methodical debugging approach.

### bn

একটি ইউনিট টেস্ট আলাদাভাবে চালালে পাস করে, কিন্তু পুরো টেস্ট স্যুট চালালে ব্যর্থ হয়। সম্ভাব্য কারণগুলো এবং ডিবাগ করার একটি পদ্ধতিগত উপায় প্রস্তাব করুন।

### bn_cs

একটি unit test আলাদাভাবে চালালে pass করে, কিন্তু পুরো test suite চালালে fail করে। সম্ভাব্য কারণগুলো আর debugging-এর একটি পদ্ধতিগত উপায় propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify shared state or test-order dependence as the likely cause, such as global variables, singletons or shared fixtures.
  Rationale: The primary cause class.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Identify external shared resources, such as files, databases, ports or environment variables, left changed by other tests.
  Rationale: A second cause class.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Mention timing or parallel-execution effects as a possible cause.
  Rationale: A third cause class.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Narrow down the interfering test, such as by running subsets, bisecting the suite or randomizing order.
  Rationale: The methodical approach.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Explain how a possible result of the narrowing step identifies or excludes a cause.
  Rationale: Turns the approach into diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Proposes narrowing the suite but gives no result-to-cause interpretation.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Fixing the isolation is optional. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH073

technical_troubleshooting; easy.

### en

A user's phone storage is almost full even though photos were recently moved to cloud storage. Explain what categories of local data should be checked.

### bn

ছবিগুলো সম্প্রতি ক্লাউড স্টোরেজে সরিয়ে নেওয়া হলেও একজন ব্যবহারকারীর ফোনের স্টোরেজ প্রায় পূর্ণ। কোন কোন ধরনের লোকাল ডেটা পরীক্ষা করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

photo-গুলো সম্প্রতি cloud storage-এ move করা হলেও একজন user-এর phone storage প্রায় full। কোন কোন ধরনের local data check করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check whether photos are still stored locally, such as originals kept after cloud backup or a recently deleted album.
  Rationale: The most likely explanation given the premise.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Check app data and caches, such as messaging media or streaming downloads.
  Rationale: A common large category.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check downloaded files and offline media.
  Rationale: Another category.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check system data or other storage reported by the phone.
  Rationale: Explains unexplained usage.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Use the phone's storage settings to see category sizes.
  Rationale: The practical method.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Deletion is not required; the prompt asks what to check. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH075

technical_troubleshooting; medium.

### en

A mobile app crashes immediately after an operating-system update. Describe how to distinguish app incompatibility, corrupted local data, permissions, and device-specific issues.

### bn

অপারেটিং সিস্টেম আপডেটের পর থেকে একটি মোবাইল অ্যাপ সঙ্গে সঙ্গেই ক্র্যাশ করছে। অ্যাপের অসামঞ্জস্য, নষ্ট হয়ে যাওয়া লোকাল ডেটা, অনুমতি এবং ডিভাইস-নির্দিষ্ট সমস্যার মধ্যে কীভাবে পার্থক্য করবেন তা বর্ণনা করুন।

### bn_cs

operating-system update-এর পর থেকে একটি mobile app সঙ্গে সঙ্গেই crash করছে। app incompatibility, corrupted local data, permission আর device-specific issue-র মধ্যে কীভাবে পার্থক্য করবেন তা describe করুন।

### Boundary and ambiguity questions

- [ ] RIU-02: Conditional safeguard embedded in the unit: confirm the backup requirement applies only if clearing data is proposed.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Check for app incompatibility with the new OS, such as an app update, release notes or other users' reports.
  Rationale: A named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; identified-ambiguity-or-boundary): Test for corrupted local data by clearing the app's cache or data, or reinstalling, after backing up anything needed.
  Rationale: A named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Check whether permissions changed after the update and whether the app needs them re-granted.
  Rationale: A named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Compare with another device on the same OS version to detect a device-specific issue.
  Rationale: A named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Explain how at least one possible result favors or weakens a named cause relative to another.
  Rationale: Without interpretation the answer does not distinguish the causes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Says to compare or rule out causes but gives no result-to-cause example.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Follows the accepted convention. Clearing data may lose local content; RIU-02 requires backing up needed data first. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH079

technical_troubleshooting; hard.

### en

A phone repeatedly loses access to a work account after several hours and requires reauthentication. Explain how to investigate token lifetime, device clock, conditional access, app state, and network changes.

### bn

একটি ফোন কয়েক ঘণ্টা পরপর বারবার কাজের অ্যাকাউন্টের অ্যাক্সেস হারায় এবং আবার পরিচয় যাচাই করতে হয়। টোকেনের মেয়াদ, ডিভাইসের ঘড়ি, কন্ডিশনাল অ্যাক্সেস, অ্যাপের অবস্থা এবং নেটওয়ার্ক পরিবর্তন কীভাবে খতিয়ে দেখবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি phone কয়েক ঘণ্টা পরপর বারবার কাজের account-এর access হারায় এবং আবার reauthentication লাগে। token lifetime, device-এর ঘড়ি, conditional access, app state আর network পরিবর্তন কীভাবে investigate করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Check token or session lifetime policies against the hours after which access is lost.
  Rationale: A named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Check that the device clock and time zone are set automatically and correctly.
  Rationale: A named area; clock skew invalidates tokens.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Review conditional access policies and sign-in logs for the device, such as compliance or location conditions.
  Rationale: A named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check app state, such as background restrictions, battery optimization or a corrupted app cache.
  Rationale: A named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Check whether access loss coincides with network changes, such as switching between Wi-Fi and mobile data or VPN.
  Rationale: A named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Use sign-in log evidence or timing correlation to explain how a possible result favors or weakens a named cause.
  Rationale: Without interpretation the answer lists areas but does not diagnose the cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Proposes correlating timing or reviewing logs but gives no result-to-hypothesis interpretation.

Draft notes: P04 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Follows the accepted differential-diagnosis convention. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
