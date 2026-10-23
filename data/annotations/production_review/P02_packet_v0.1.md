# P02 independent review packet

Status: pending. AI-produced draft annotations; no human acceptance is claimed.

Each task needs bilingual equivalence and full-prompt coverage review. Review all critical units, all ambiguity/boundary questions below, and every prespecified ordinary sample item. Additional ordinary units may be reviewed. Blank identity/decision fields are intentional.

25 tasks; 113 RIUs; 49 critical; 18 ordinary sample units; 91 mandatory unit reviews.

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

## CYBER003

cybersecurity_digital_safety; medium.

### en

A user is deciding whether to enable multi-factor authentication on an important account. Explain why it matters and what type of second factor is preferable.

### bn

একজন ব্যবহারকারী একটি গুরুত্বপূর্ণ অ্যাকাউন্টে মাল্টি-ফ্যাক্টর অথেনটিকেশন চালু করবেন কি না ভাবছেন। এটি কেন গুরুত্বপূর্ণ এবং কোন ধরনের দ্বিতীয় ফ্যাক্টর বেশি ভালো তা ব্যাখ্যা করুন।

### bn_cs

একজন user একটি গুরুত্বপূর্ণ account-এ multi-factor authentication enable করবেন কি না ভাবছেন। এটা কেন গুরুত্বপূর্ণ এবং কোন ধরনের second factor বেশি ভালো তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-02: The fallback hierarchy illustrates an acceptable path, not a requirement to list every method when a justified phishing-resistant choice is given. Review passkey user-verification wording and avoid treating any biometric alone as remotely shared proof.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that MFA adds verification beyond a password so a stolen or reused password alone is less likely to permit account access.
  Rationale: The requested reason for enabling MFA is absent without the independent-factor protection.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Prefer an available phishing-resistant factor such as a FIDO/WebAuthn security key or appropriately configured passkey, explaining its stronger resistance to phishing; if unavailable, an authenticator app is generally preferable to SMS as a practical fallback.
  Rationale: The prompt explicitly requests a preferable factor; equating all second factors or recommending password-only access defeats that security choice.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants ask why MFA matters and which second factor is preferable. FIDO/WebAuthn security keys or appropriately user-verified passkeys are valid phishing-resistant examples; code-based authenticators may be a practical fallback. Do not describe TOTP or SMS as phishing-resistant or claim MFA prevents all attacks. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER015

cybersecurity_digital_safety; medium.

### en

A phishing email uses a real company logo and a convincing sender name. Explain what deeper indicators should be examined.

### bn

একটি ফিশিং ইমেইলে আসল কোম্পানির লোগো এবং বিশ্বাসযোগ্য প্রেরকের নাম ব্যবহার করা হয়েছে। আরও গভীরে কোন কোন লক্ষণ পরীক্ষা করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি phishing email-এ আসল company-র logo আর convincing sender name ব্যবহার করা হয়েছে। আরও গভীরে কোন কোন indicator examine করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-02: Sender identity and link destination are separate indicators; accept safe equivalent inspection without demanding raw headers from an ordinary user.
- [ ] RIU-03: Examples are alternatives, not all required; polished language and a real company logo do not neutralize other phishing indicators.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Inspect the actual sender address/domain and reply-to/header details for mismatches or misleading lookalike domains rather than trusting the display name.
  Rationale: Tests sender identity beneath the convincing surface label.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; identified-ambiguity-or-boundary): Inspect the true destination of links using a safe non-opening method for mismatches, lookalike domains or suspicious redirection.
  Rationale: Tests the actual link target without visiting or executing suspicious content.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Examine what the message asks for and its context, such as unexpected credentials/payment, urgency, unusual attachments or a request inconsistent with normal business.
  Rationale: Tests behavioral/context evidence without making grammar errors a necessary phishing signature.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Verify a questionable request through an independently known company/contact route rather than replying, clicking or calling only the details supplied in the message.
  Rationale: Provides independent corroboration instead of letting the suspect email authenticate itself.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants identify the message as phishing; the task asks deeper indicators rather than instructions to detonate links. Logo authenticity does not authenticate the email. Sender-domain checks do not mean a matching display name proves safety. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER024

cybersecurity_digital_safety; medium.

### en

A managed laptop shows signs of unusual pop-ups and browser redirects. Describe a safe response process that preserves useful evidence and reduces further risk.

### bn

প্রতিষ্ঠানের কেন্দ্রীয় ব্যবস্থাপনায় থাকা একটি ল্যাপটপে অস্বাভাবিক পপ-আপ এবং ব্রাউজার রিডাইরেক্টের লক্ষণ দেখা যাচ্ছে। কাজে লাগার মতো প্রমাণ সংরক্ষণ করে এবং আরও ঝুঁকি কমিয়ে একটি নিরাপদ রেসপন্স প্রক্রিয়া বর্ণনা করুন।

### bn_cs

একটি managed laptop-এ অস্বাভাবিক pop-up আর browser redirect-এর লক্ষণ দেখা যাচ্ছে। কাজে লাগার মতো evidence preserve করে এবং আরও risk কমিয়ে একটি safe response process describe করুন।

### Boundary and ambiguity questions

- [ ] RIU-01: Containment should fit the managed environment and observed risk; do not require abrupt network loss if authorized remote support needs a safer alternative.
- [ ] RIU-03: No need to revisit malicious pages solely for screenshots; safe existing evidence is sufficient.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Stop interacting with suspicious pop-ups/redirects and reduce further exposure using a safe containment path appropriate to the managed environment, such as disconnecting affected network access when warranted and following IT guidance.
  Rationale: Continued risky interaction or untrusted cleanup can amplify compromise; the stated risk-reduction objective needs an immediate protective path.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Promptly report the symptoms to the organization’s IT/security support through a trusted channel and follow its authorized response process.
  Rationale: Managed systems need coordinated response rather than unsupervised changes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Preserve useful evidence such as times, URLs/screenshots when safely obtainable and relevant alerts/logs, avoiding unnecessary deletion/reset/cleanup that destroys it.
  Rationale: Destructive cleanup before preserving evidence can defeat the explicit evidence-retention objective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Have the authorized response assess relevant browser extensions/settings and endpoint/security findings, apply justified cleanup, and verify the behavior is resolved before normal use.
  Rationale: Provides an evidence-led resolution path without assuming a proven malware family or requiring an exhaustive forensic image.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants specify a managed device and symptoms, not confirmed malware. No compulsory personal antivirus installation, reimage or account reset is assumed. Evidence collection should be proportionate and should not require continued unsafe browsing. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER062

cybersecurity_digital_safety; easy.

### en

A team shares one cloud API key among several applications. Explain the security problems this creates.

### bn

একটি টিম কয়েকটি অ্যাপ্লিকেশনের মধ্যে একটি মাত্র ক্লাউড এপিআই-কি শেয়ার করে ব্যবহার করছে। এতে কী কী নিরাপত্তা সমস্যা তৈরি হয় তা ব্যাখ্যা করুন।

### bn_cs

একটি team কয়েকটি application-এর মধ্যে একটি মাত্র cloud API key share করে ব্যবহার করছে। এতে কী কী security problem তৈরি হয় তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-02: Common-secret blast radius differs from inability to grant distinct scopes; do not assume the key has administrator privileges.
- [ ] RIU-04: Rotation coupling is a security-response consequence; no requirement to execute a live key change or guarantee outages occur.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Explain that compromise or leakage from one application exposes the same credential used by the others, broadening the blast radius.
  Rationale: Without the cross-application exposure link the central security consequence of sharing is missing.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; identified-ambiguity-or-boundary): Explain that a single shared key prevents clean per-application permission scoping and can give an application access it does not need.
  Rationale: Identifies loss of least-privilege separation without assuming exact permissions.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Explain that shared-key activity is harder to attribute to a particular application, impairing audit or incident investigation.
  Rationale: Preserves the accountability consequence separately from access scope.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Explain that rotating or revoking the key affects all dependent applications, complicating incident containment and coordinated updates.
  Rationale: Identifies operational coupling during a security response.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants retain one shared key across several applications, not merely shared infrastructure. No breach is stated. Separate keys are a valid remedy but the prompt asks for problems, so a full remediation plan is not a required RIU. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER070

cybersecurity_digital_safety; hard.

### en

An organization relies heavily on one cloud provider and wants to understand security concentration risk. Explain what dependencies, recovery assumptions, identities, and data controls should be assessed.

### bn

একটি প্রতিষ্ঠান একটি মাত্র ক্লাউড প্রোভাইডারের ওপর ব্যাপকভাবে নির্ভরশীল এবং এ থেকে তৈরি নিরাপত্তার কেন্দ্রীভবন-ঝুঁকি বুঝতে চায়। কোন কোন ডিপেন্ডেন্সি, পুনরুদ্ধার-সংক্রান্ত অনুমান, আইডেন্টিটি এবং ডেটা নিয়ন্ত্রণ মূল্যায়ন করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি প্রতিষ্ঠান একটি মাত্র cloud provider-এর ওপর ব্যাপকভাবে নির্ভরশীল এবং এ থেকে তৈরি security concentration risk বুঝতে চায়। কোন কোন dependency, recovery assumption, identity আর data control assess করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-02: Dependency map and recovery feasibility are distinct; assess common account/control dependencies rather than equating geographic diversity with full independence.
- [ ] RIU-04: Data-control examples are alternatives chosen for relevant dependencies; no universal requirement for a specific sovereignty or licensing conclusion.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Map critical services and their shared provider/region/control-plane or third-party dependencies to identify where one provider failure or compromise could affect multiple essential functions together.
  Rationale: Without correlated dependency mapping the assessment misses the concentration risk at its center.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Test recovery assumptions against loss or compromise of provider access, including whether backups, restoration paths and required keys/control services remain available independently enough to recover.
  Rationale: A recovery plan relying on the same failed or compromised access path can make essential recovery infeasible.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Assess identity and administrative dependencies, such as common accounts/federation, privilege concentration and emergency access, for cross-service takeover or lockout risk.
  Rationale: Examines the specifically named identity layer without mandating one identity product.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Assess data-control dependencies, including access, encryption/key custody, backup/export portability and retention/residency needs where relevant.
  Rationale: Determines whether data remains protected and recoverable without assuming particular legal duties.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Explain residual correlated risks and practical mitigations or tradeoffs rather than treating a second region, backup or second provider as automatic independence.
  Rationale: Connects findings to an evidence-based concentration assessment without imposing a universal multi-cloud answer.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants name dependencies, recovery assumptions, identities and data controls. Multi-cloud migration is not prescribed. Region separation or copies inside the same provider may retain correlated control-plane, account or provider dependencies. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC002

decision_support; easy.

### en

A student has one hour available and must either revise lecture notes, start an assignment due next week, or prepare for a quiz tomorrow. Explain the most reasonable priority.

### bn

একজন শিক্ষার্থীর হাতে এক ঘণ্টা সময় আছে, এবং তাঁকে লেকচার নোট রিভিশন দেওয়া, আগামী সপ্তাহে জমার একটি অ্যাসাইনমেন্ট শুরু করা, অথবা আগামীকালের কুইজের প্রস্তুতি—এর মধ্যে একটি বেছে নিতে হবে। সবচেয়ে যুক্তিসংগত অগ্রাধিকার কোনটি তা ব্যাখ্যা করুন।

### bn_cs

একজন student-এর হাতে এক ঘণ্টা সময় আছে, এবং তাঁকে lecture note revise করা, আগামী সপ্তাহে জমার একটি assignment শুরু করা, অথবা আগামীকালের quiz-এর প্রস্তুতি—এর মধ্যে একটি বেছে নিতে হবে। সবচেয়ে reasonable priority কোনটা তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01: Quiz preparation may include relevant lecture-note revision; do not treat all use of notes as choosing the wrong competing task.
- [ ] RIU-02: No invented quiz importance, assignment difficulty or detailed 60-minute allocation is required.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Prioritize preparing for tomorrow’s quiz during the available hour under the supplied facts.
  Rationale: The nearest known assessment deadline is the central requested priority; arbitrarily preferring next week’s assignment ignores the supplied urgency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Explain that the quiz’s tomorrow deadline makes focused preparation more urgent than starting the assignment due next week or untargeted note revision.
  Rationale: Supports the choice with the actual relative deadlines rather than an invented grading weight.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants give one hour, a quiz tomorrow and assignment next week; no contrary importance or readiness facts are supplied. A plan should not promise to complete all three as if the either/or constraint were absent. No detailed timetable is requested. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC028

decision_support; medium.

### en

An organization is selecting a system that will be used for at least five years. Design an evaluation framework covering functionality, integration, security, accessibility, vendor dependence, migration cost, support, and exit strategy.

### bn

একটি প্রতিষ্ঠান এমন একটি সিস্টেম বাছাই করছে, যা অন্তত পাঁচ বছর ব্যবহার করা হবে। কার্যকারিতা, অন্য সিস্টেমের সঙ্গে ইন্টিগ্রেশন, নিরাপত্তা, অ্যাক্সেসিবিলিটি, ভেন্ডরের ওপর নির্ভরতা, মাইগ্রেশনের খরচ, সাপোর্ট এবং ভবিষ্যতে সরে আসার কৌশল নিয়ে একটি মূল্যায়ন কাঠামো তৈরি করুন।

### bn_cs

একটি প্রতিষ্ঠান এমন একটি system বাছাই করছে, যেটা অন্তত পাঁচ বছর ব্যবহার করা হবে। functionality, integration, security, accessibility, vendor dependence, migration cost, support আর exit strategy নিয়ে একটি evaluation framework তৈরি করুন।

### Boundary and ambiguity questions

- [ ] RIU-05, RIU-08: Vendor-dependence diagnosis and an executable exit route are distinct; no automatic preference for open source or multi-vendor procurement.
- [ ] RIU-06, RIU-08: Initial migration cost must not be conflated with future exit cost; one span can earn both only if it distinguishes the two.
- [ ] RIU-09: Accept qualitative evidence/prioritization; no compulsory weighted sum or fabricated vendor scores.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Evaluate functionality against current and plausible needs over the intended use of at least five years.
  Rationale: Ensures feature fit is assessed over the stated horizon rather than a short demo.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Evaluate integration with required existing systems, workflows and data interfaces.
  Rationale: Captures the explicitly requested interoperability dimension.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Evaluate security controls and relevant risk/maintenance obligations across the system lifecycle.
  Rationale: Captures the explicitly requested security dimension without inventing a regulation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Evaluate accessibility for intended users and assistive use needs using relevant requirements or demonstrations.
  Rationale: Captures the explicit accessibility dimension separately from feature count.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; identified-ambiguity-or-boundary): Evaluate dependence on the vendor or proprietary components, including lock-in and continuity implications.
  Rationale: Captures dependency risk rather than equating popularity with safety.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; identified-ambiguity-or-boundary): Estimate migration/adoption cost, including moving data and relevant training or transition disruption.
  Rationale: Captures the explicitly requested cost of switching into the system.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (supporting; ordinary, outside prespecified sample): Evaluate support availability, maintenance commitments and sustainable service over the use horizon.
  Rationale: Captures support as distinct from technical functionality.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-08** (supporting; identified-ambiguity-or-boundary): Evaluate an exit strategy, including usable data export and feasibility/cost of transition to a replacement.
  Rationale: Captures eventual departure rather than only initial migration.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-09** (critical; all-critical, identified-ambiguity-or-boundary): Use documented evidence and priorities to compare candidates across the dimensions over at least five years and make tradeoffs visible before selecting.
  Rationale: An unconnected feature checklist without a comparison/decision framework fails the requested evaluation framework.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants retain at least five years and eight named dimensions. Units reflect independent evaluation dimensions; no fixed weights, vendors, purchase price, assumed disability profile or inevitable vendor failure is supplied. Migration into a system differs from eventual exit. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC070

decision_support; hard.

### en

An experiment shows a statistically significant difference but the effect is small and operationally costly to act on. Explain how statistical evidence, effect size, uncertainty, cost, and practical value should be considered together.

### bn

একটি এক্সপেরিমেন্টে পরিসংখ্যানগতভাবে তাৎপর্যপূর্ণ পার্থক্য দেখা গেছে, কিন্তু প্রভাবটি ছোট এবং সে অনুযায়ী কাজ করা পরিচালনাগতভাবে ব্যয়বহুল। পরিসংখ্যানগত প্রমাণ, প্রভাবের আকার, অনিশ্চয়তা, খরচ এবং বাস্তব মূল্য একসঙ্গে কীভাবে বিবেচনা করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি experiment-এ statistically significant পার্থক্য দেখা গেছে, কিন্তু effect-টা ছোট এবং সে অনুযায়ী কাজ করা operationally ব্যয়বহুল। statistical evidence, effect size, uncertainty, cost আর practical value একসঙ্গে কীভাবে বিবেচনা করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-02, RIU-03: Magnitude and uncertainty are different; no requirement to invent numerical confidence bounds or an economic conversion unavailable in the task.
- [ ] RIU-04: A justified conditional decision or further test is valid; significance does not compel adoption and small does not prove zero practical value.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that statistical significance alone does not establish a practically worthwhile effect or require operational action.
  Rationale: Equating significance with value defeats the central distinction in the prompt.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; identified-ambiguity-or-boundary): Assess the effect’s magnitude in relevant operational units and against a meaningful benefit threshold rather than only its significance label.
  Rationale: Interprets how large the small effect is for the actual objective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Consider uncertainty in the effect estimate and study evidence, such as its plausible range and how well it applies to the intended operation.
  Rationale: Avoids treating a significant point estimate as exact or universally applicable.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): Weigh plausible practical benefits against implementation cost, disruption and risk to decide whether to act, test further or defer.
  Rationale: The operational decision is infeasible without combining benefit and cost rather than reporting statistics alone.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Explicitly compares likely benefit with operational cost but gives no decision rule or conditional next step; merely saying consider everything scores 0.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants state a significant but small effect with costly operational action. No p-value, sample size, confidence interval or budget is supplied; neither automatic adoption nor automatic rejection follows. Practical significance is separate from hypothesis-test significance. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC077

decision_support; medium.

### en

A team is receiving repeated questions because an earlier announcement was unclear. Explain how to decide whether to send a correction, FAQ, or completely rewritten message.

### bn

আগের একটি ঘোষণা অস্পষ্ট হওয়ায় একটি টিম বারবার একই প্রশ্ন পাচ্ছে। একটি সংশোধনী, একটি প্রায়শ জিজ্ঞাসিত প্রশ্নের তালিকা, নাকি পুরোপুরি নতুন করে লেখা বার্তা—কোনটি পাঠাবেন তা কীভাবে ঠিক করবেন ব্যাখ্যা করুন।

### bn_cs

আগের একটি announcement অস্পষ্ট হওয়ায় একটি team বারবার একই question পাচ্ছে। একটি correction, একটি FAQ, নাকি completely rewritten message—কোনটা পাঠাবেন তা কীভাবে decide করবেন explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-02: Review whether all three decision options are explained without requiring a fabricated diagnosis or excluding a justified combination.
- [ ] RIU-03: A clear update to the original message is sufficient; a brand-new broadcast is not always required.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Review the repeated questions and original announcement to identify whether confusion comes from a narrow error, recurring missing details or the core structure/message.
  Rationale: Provides the evidence needed to distinguish the revision options.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Match the format to the confusion: a targeted correction for a specific error, FAQ for recurring discrete questions, and a rewrite when the main explanation or structure is broadly unclear.
  Rationale: A format choice without a scope-to-format decision rule misses the central task.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Makes a correct scope-to-format distinction for at least two options but leaves the third unexplained; a bare list of formats scores 0.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary): Make the updated explanation easy to find and unambiguous about what it replaces or clarifies so recipients do not keep relying on conflicting versions.
  Rationale: Prevents a clarification from adding another inconsistent message without prescribing a channel.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants supply repeated questions after an unclear announcement; no specific erroneous fact or question list is supplied. Correction, FAQ and rewrite can be combined if justified; selecting one on invented facts is not required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC088

decision_support; medium.

### en

An organization wants one policy to apply across teams with very different risk levels and workflows. Propose a layered design that separates universal requirements from context-specific controls.

### bn

একটি প্রতিষ্ঠান এমন সব টিমে একটিমাত্র নীতি প্রয়োগ করতে চায়, যাদের ঝুঁকির মাত্রা ও কাজের ধারা একেবারেই আলাদা। সবার জন্য প্রযোজ্য আবশ্যিক শর্ত আর প্রেক্ষাপট-নির্দিষ্ট নিয়ন্ত্রণ আলাদা রেখে একটি স্তরভিত্তিক নকশা প্রস্তাব করুন।

### bn_cs

একটি প্রতিষ্ঠান এমন সব team-এ একটিমাত্র policy apply করতে চায়, যাদের risk level আর workflow একেবারেই আলাদা। universal requirement আর context-specific control আলাদা রেখে একটি layered design propose করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-02: Universal outcomes and tailored implementation are distinct; alternatives may satisfy the same baseline rather than waive it.
- [ ] RIU-03: No mandatory numerical scoring matrix or external compliance standard should be inferred.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Define a common baseline of non-negotiable requirements or outcomes that applies to every team.
  Rationale: Without a universal layer the proposal does not implement the organization-wide policy design.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Define context-specific control layers selected by team risk and workflow rather than imposing identical detailed procedures on all teams.
  Rationale: Without contextual control selection the requested layered design is lost.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Explain how teams determine and document their applicable layer, with proportionate rationale and accountability for exceptions or equivalent controls.
  Rationale: Makes tailoring governable without assuming unrestricted exemption from the baseline.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Review whether the baseline and tailored controls meet their goals as risk or workflows change and adjust through an accountable process.
  Rationale: Keeps the layered design relevant over time without requiring a fixed audit frequency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants preserve one organization-wide policy and heterogeneous risk/workflows. Contextual controls may vary while meeting a shared outcome. No policy subject, numerical risk score or regulatory regime is supplied. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC005

procedural_instructional; medium.

### en

Explain how to archive completed project files while keeping them searchable and preserving important context.

### bn

শেষ হয়ে যাওয়া প্রজেক্টের ফাইলগুলো কীভাবে আর্কাইভ করবেন যাতে সেগুলো খোঁজা যায় এবং গুরুত্বপূর্ণ প্রেক্ষাপটও সংরক্ষিত থাকে, তা ব্যাখ্যা করুন।

### bn_cs

শেষ হয়ে যাওয়া project-এর file-গুলো কীভাবে archive করবেন যাতে সেগুলো searchable থাকে এবং গুরুত্বপূর্ণ context-ও সংরক্ষিত থাকে, তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-02, RIU-03: Search metadata and interpretive context may share a document but are distinct propositions; no forced duplication of identical labels.
- [ ] RIU-04: A permissions/readability check is sufficient; no invented compliance retention schedule or compulsory multi-site backup.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Identify and collect the completed project’s authoritative files/versions in a designated archive without silently confusing drafts with final outputs.
  Rationale: Defines what is being preserved without requiring destruction of the working copy.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Organize and label/index the archive with enough meaningful names or metadata to find files by project, topic, date or other relevant retrieval cues.
  Rationale: A preserved but unfindable collection fails the explicit searchability objective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Preserve the context needed to interpret the files, such as purpose, decisions, dates, relationships or required dependencies, linked to the relevant artifacts.
  Rationale: Files without their explanatory context fail the other central archive objective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Check that archived files and their index/context can be accessed and read by intended future users with appropriate permissions.
  Rationale: Verifies practical reuse without prescribing one storage platform or retention period.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants require searchable completed files and important context. An index, sensible metadata/naming and a README are alternative mechanisms. No mandatory deletion of working files, exact folder tree or proprietary archive format. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC015

procedural_instructional; medium.

### en

Explain how to hand off a project task from one team member to another without losing context or deadlines.

### bn

প্রেক্ষাপট বা সময়সীমা না হারিয়ে কীভাবে একটি প্রজেক্টের কাজ একজন সদস্যের কাছ থেকে আরেকজনের কাছে হস্তান্তর করা যায় তা ব্যাখ্যা করুন।

### bn_cs

context বা deadline না হারিয়ে কীভাবে একটি project task একজন team member-এর কাছ থেকে আরেকজনের কাছে hand off করা যায় তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-03: Completed-work context and actionable remaining-work state are distinct; do not require a long project history irrelevant to the task.
- [ ] RIU-04: Review the ordinal handoff distinction; confirmation can be informal and proportionate rather than a signature workflow.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Transfer the task’s objective, current status and relevant decisions/materials so the receiving member understands the context and work already done.
  Rationale: Without substantive context the handoff loses the information the prompt explicitly protects.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Make the actual deadline and relevant upcoming milestones/commitments explicit to the receiving member.
  Rationale: A transfer that drops the time boundary can directly miss the protected deadline.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary): Identify the remaining actions, dependencies, blockers and useful contacts relevant to completing the task.
  Rationale: Makes the work state actionable rather than only reciting history.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): Confirm that the new owner has accepted responsibility and has the necessary access/understanding, with ownership recorded or communicated to affected people.
  Rationale: A packet sent without an accountable receiving owner can leave the task unattended.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Obtains explicit acknowledgment of new ownership but does not confirm access/understanding or make the ownership change visible where needed.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants specify a team-member handoff without context/deadline loss. No task status, actual date or tracking tool is given. A shared note or conversation plus confirmation can work. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC027

procedural_instructional; medium.

### en

Explain how to verify that every claim in a draft is either supported by evidence, clearly identified as interpretation, or presented as common background knowledge.

### bn

একটি খসড়ার প্রতিটি দাবি হয় প্রমাণ দিয়ে সমর্থিত, নয়তো স্পষ্টভাবে ব্যাখ্যা বা মতামত হিসেবে চিহ্নিত, অথবা সাধারণ পটভূমি-জ্ঞান হিসেবে উপস্থাপিত—এটি কীভাবে যাচাই করবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি draft-এর প্রতিটি claim হয় evidence দিয়ে supported, নয়তো স্পষ্টভাবে interpretation হিসেবে চিহ্নিত, অথবা common background knowledge হিসেবে উপস্থাপিত—এটা কীভাবে verify করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-04: Inventory/category assignment differs from deciding whether common knowledge is justified for the audience.
- [ ] RIU-03: Explicitly labeling an unsupported assertion as opinion does not make an invalid factual premise acceptable; review inference boundaries.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary): Inventory the draft’s substantive claims and classify each as evidence-backed, explicit interpretation or common background knowledge.
  Rationale: Ensures every claim enters the audit rather than only checking existing citations.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): For an evidence-backed claim, check that a credible cited/source item actually supports the scope and strength of that claim.
  Rationale: A citation that does not support the assertion cannot meet the central evidence-verification objective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Clearly label interpretations as such and distinguish them from established findings while checking that the underlying evidence permits the inference.
  Rationale: Unlabeled inference can misrepresent opinion as established fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Use the common-background category only for information reasonably shared by the intended audience, sourcing specialist, disputed or non-obvious assertions instead.
  Rationale: Prevents the background label from becoming an escape for unsupported substantive claims.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Revise, qualify, source or remove claims that do not meet any justified category, and recheck the resulting draft.
  Rationale: An audit that identifies unsupported claims but leaves them asserted fails the all-claims requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. BN includes interpretation or opinion while EN/BN-CS say interpretation; both require explicit labeling rather than treating opinion as evidence. No citation style or particular reference manager is prescribed. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC093

procedural_instructional; easy.

### en

Explain how to prepare an alternative way to access an important document if the internet is unavailable.

### bn

ইন্টারনেট না থাকলে একটি গুরুত্বপূর্ণ ডকুমেন্ট দেখার বিকল্প উপায় কীভাবে আগে থেকে প্রস্তুত রাখবেন তা ব্যাখ্যা করুন।

### bn_cs

internet না থাকলে একটি গুরুত্বপূর্ণ document access করার alternative উপায় কীভাবে আগে থেকে prepare করে রাখবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-02: Preparing a real offline artifact and testing it are distinct; no obligation to test on every device or force use of one format.
- [ ] RIU-04: Protection is proportionate and conditional on the document; do not invent a secrecy classification.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Prepare an authorized accessible offline copy or equivalent non-internet-dependent access path before connectivity is lost.
  Rationale: An online-only link cannot meet the central offline-access objective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Test that the prepared document can actually be opened/read without internet, including any necessary viewer, permissions or local credentials.
  Rationale: A cached pointer or access-controlled file that fails offline defeats the purported alternative.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Keep the offline version sufficiently current and clearly identifiable as the intended document.
  Rationale: Reduces the chance of relying on an obsolete or wrong copy.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Store the offline copy so authorized users can reach it while maintaining protection appropriate to the document.
  Rationale: Preserves useful access without assuming that offline preparation authorizes public disclosure.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants require preparation before internet loss, not retrieval from the cloud after loss. Authorized local/offline copy or an appropriate printed copy can work. No requirement to buy a device, use removable storage or expose confidential material. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC099

procedural_instructional; hard.

### en

A small organization wants a simple continuity plan for losing access to its main office for several days. Propose a procedure covering people, communication, systems, documents, priorities, and return to normal operations.

### bn

একটি ছোট প্রতিষ্ঠান কয়েক দিনের জন্য প্রধান অফিসে ঢুকতে না পারলে কী হবে, তার জন্য একটি সহজ কন্টিনিউটি প্ল্যান চায়। কর্মী, যোগাযোগ, সিস্টেম, কাগজপত্র, অগ্রাধিকার এবং স্বাভাবিক কাজে ফিরে আসা অন্তর্ভুক্ত করে একটি পদ্ধতি প্রস্তাব করুন।

### bn_cs

একটি ছোট প্রতিষ্ঠান কয়েক দিনের জন্য main office-এ access না পেলে কী হবে, তার জন্য একটি simple continuity plan চায়। people, communication, system, document, priority আর normal operation-এ ফিরে আসা cover করে একটি procedure propose করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-02: Staff responsibility/availability and communication are distinct; safety action should match actual circumstances rather than an invented physical emergency.
- [ ] RIU-03, RIU-04: System operation and document access can share tools but remain different outcomes; no assumed office hardware access during the outage.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Account for staff availability and welfare and assign continuity responsibilities or cover for essential roles.
  Rationale: Addresses the named people component without assuming a hazardous event.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Establish a reliable way to contact staff and relevant external parties and communicate the temporary operating arrangement.
  Rationale: An uncommunicated continuity arrangement can leave essential work uncoordinated during office loss.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Provide an authorized feasible temporary way to access or operate the essential systems needed for priority work.
  Rationale: A plan that cannot run required systems cannot maintain its central operations.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Make necessary documents/records available through authorized alternative access with suitable protection.
  Rationale: Addresses the distinct document-access component without requiring all records be copied.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Identify essential services/tasks to sustain first and defer lower-priority work so available people and resources fit the outage.
  Rationale: Without priorities the small organization may expend limited continuity capacity on nonessential work.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Define checks and coordination for returning to the office/normal systems, reconciling temporary work and informing affected people when normal operations resume.
  Rationale: Completes the requested return-to-normal phase rather than stopping at temporary relocation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants specify a small organization and several days without the main office. No disaster cause, new site, headcount or numerical recovery target is supplied. Remote, alternate-site or scaled-back service paths are valid if feasible. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN032

information_synthesis; easy.

### en

Extract all constraints: The meeting must be 30 minutes, occur after 1 PM, include both team leads, and avoid Wednesday.

### bn

সব শর্ত বের করুন: মিটিংটি ৩০ মিনিটের হতে হবে, দুপুর ১টার পরে হতে হবে, দুই টিম লিডকেই থাকতে হবে এবং বুধবার বাদ দিতে হবে।

### bn_cs

সব constraint extract করুন: meeting-টা ৩০ মিনিটের হতে হবে, দুপুর ১টার পরে হতে হবে, দুই team lead-কেই থাকতে হবে এবং বুধবার avoid করতে হবে।

### Boundary and ambiguity questions

- [ ] RIU-02: EN after and BN/BN-CS পরে preserve a strict lower bound; do not silently change to at or after 1 PM.
- [ ] RIU-01, RIU-03, RIU-04: Criticality reflects all-constraints extraction as the central task; no added scheduling feasibility or calendar data is required.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): State that the meeting duration must be 30 minutes.
  Rationale: Omitting any requested constraint makes the extracted constraint set materially incomplete.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): State that the meeting must occur after 1 PM, excluding a 1 PM start.
  Rationale: Changing the strict comparator changes the feasible meeting set.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): State that both team leads must attend.
  Rationale: One lead alone does not satisfy the shared attendance constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): State that Wednesday must be avoided.
  Rationale: Dropping the excluded day changes the feasible meeting set.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants preserve 30 minutes, strictly after 1 PM, both team leads, and no Wednesday. No actual availability is provided and scheduling a specific slot is not required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN046

information_synthesis; medium.

### en

Create an ordered task list: Before migration, export current settings and verify backups. During migration, record any exceptions. After migration, validate user access and compare record counts.

### bn

ক্রম অনুযায়ী একটি কাজের তালিকা তৈরি করুন: মাইগ্রেশনের আগে বর্তমান সেটিংস এক্সপোর্ট করুন এবং ব্যাকআপ যাচাই করুন। মাইগ্রেশন চলাকালে যেকোনো ব্যতিক্রম লিখে রাখুন। মাইগ্রেশনের পরে ব্যবহারকারীদের অ্যাক্সেস যাচাই করুন এবং রেকর্ডের সংখ্যা মিলিয়ে দেখুন।

### bn_cs

order অনুযায়ী একটি task list তৈরি করুন: migration-এর আগে বর্তমান settings export করুন এবং backup verify করুন। migration চলাকালে যেকোনো exception record করুন। migration-এর পরে user access validate করুন এবং record count মিলিয়ে দেখুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-02: Each content unit includes its phase; chronological list presentation remains an orthogonal format check.
- [ ] RIU-04, RIU-05: Access validation and record-count comparison test independent acceptance properties; no additional mandatory integrity algorithm is inferred.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary): Include exporting current settings before migration.
  Rationale: Preserves one explicitly requested preparation step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Include verifying backups before migration.
  Rationale: Deferring backup verification until after migration can remove a material recovery safeguard.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Include recording any exceptions during migration.
  Rationale: Preserves the required contemporaneous exception record.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): Include validating user access after migration.
  Rationale: A migrated system can remain unusable to intended users without this required acceptance check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical, identified-ambiguity-or-boundary): Include comparing record counts after migration.
  Rationale: Omitting the stated data-count check can leave material migration incompleteness undetected.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants preserve two pre-migration actions, exception recording during migration and two post-migration checks. No relative order is specified between actions within the same phase. Export and backup verification are independent actions. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
- [ ] CHECK-02: Present an ordered list or equivalently clear pre-migration, during-migration and post-migration sequence. Order within a phase is flexible. Phase-specific content remains RIUs, and the format check does not add content units.

## SYN059

information_synthesis; hard.

### en

A security review finds no confirmed breach, but one endpoint shows suspicious activity, an account had an unusual login, and network logs are incomplete for the relevant hour. Summarize the evidence and uncertainty without declaring either safety or compromise.

### bn

একটি নিরাপত্তা পর্যালোচনায় নিশ্চিত কোনো ব্রিচ পাওয়া যায়নি, কিন্তু একটি এন্ডপয়েন্টে সন্দেহজনক কার্যকলাপ দেখা গেছে, একটি অ্যাকাউন্টে অস্বাভাবিক লগইন হয়েছে এবং সংশ্লিষ্ট এক ঘণ্টার নেটওয়ার্ক লগ অসম্পূর্ণ। নিরাপদ বা কম্প্রোমাইজড—কোনোটিই ঘোষণা না করে প্রমাণ ও অনিশ্চয়তা সংক্ষেপ করুন।

### bn_cs

একটি security review-তে confirmed কোনো breach পাওয়া যায়নি, কিন্তু একটি endpoint-এ suspicious activity দেখা গেছে, একটি account-এ unusual login হয়েছে এবং সংশ্লিষ্ট এক ঘণ্টার network log incomplete। safe বা compromised—কোনোটাই declare না করে evidence আর uncertainty summarize করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-05: The no-confirmed-breach fact and balanced overall inference are distinct; lack of confirmation is not proof of safety.
- [ ] RIU-04: Missing logs create an evidence limit, not affirmative evidence of attacker log deletion or a confirmed breach.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): State that the security review found no confirmed breach.
  Rationale: Removing the confirmation boundary turns concerns into an unsupported breach claim.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that one endpoint showed suspicious activity.
  Rationale: Omitting this adverse observation can materially understate the risk evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that an account had an unusual login.
  Rationale: Omitting this separate adverse observation materially changes the evidence set.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): State that network logs for the relevant hour are incomplete, limiting what can be established about activity during that period.
  Rationale: Treating incomplete logs as clean coverage falsely strengthens the conclusion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical, identified-ambiguity-or-boundary): Keep the overall conclusion unresolved: the evidence neither establishes safety nor confirms compromise.
  Rationale: An unqualified safe or compromised verdict directly violates the central inference constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants state no confirmed breach, suspicious endpoint activity, unusual account login and incomplete network logs for the relevant hour. Neither the three observations nor the missing logs prove compromise. The requested concise form has no exact word count. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN066

information_synthesis; medium.

### en

A model achieves 95 percent accuracy on a test set collected from one institution. Explain what conclusion is supported and why performance elsewhere remains uncertain.

### bn

একটি প্রতিষ্ঠান থেকে সংগ্রহ করা টেস্ট সেটে একটি মডেল ৯৫ শতাংশ নির্ভুলতা অর্জন করেছে। কোন উপসংহার সমর্থিত এবং অন্য জায়গায় এর পারফরম্যান্স কেন অনিশ্চিত থেকে যায় তা ব্যাখ্যা করুন।

### bn_cs

একটি institution থেকে collect করা test set-এ একটি model ৯৫ শতাংশ accuracy অর্জন করেছে। কোন conclusion supported এবং অন্য জায়গায় এর performance কেন uncertain থেকে যায় তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-02: Do not infer the test was biased, leaked or invalid; one-site evidence can be valid within its scope yet insufficient for broad generalization.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): State that the model achieved 95% accuracy on the supplied test set from one institution.
  Rationale: The supported performance claim must retain its value and evaluated population rather than generalizing it to all settings.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Explain that performance elsewhere is uncertain because other institutions may differ in population, measurement or operating conditions not represented by this test set.
  Rationale: Without the distribution/scope limitation the explanation incorrectly generalizes the test result.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Identify representative external or multi-institution evaluation as a way to assess generalization before assuming the same accuracy elsewhere.
  Rationale: Makes the evidence gap actionable without requiring a new study result.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants state one institution’s test set and 95% accuracy. Neither representativeness nor leakage is established. No confidence interval or external benchmark result can be invented. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN084

information_synthesis; medium.

### en

Summarize the risks and controls: Customer data will be moved to a new system. A full backup exists. A test migration succeeded on 10 percent of records. The final migration window is six hours. Rollback has not yet been timed.

### bn

ঝুঁকি ও নিয়ন্ত্রণব্যবস্থাগুলো সংক্ষেপ করুন: গ্রাহকদের ডেটা একটি নতুন সিস্টেমে সরানো হবে। একটি পূর্ণ ব্যাকআপ আছে। ১০ শতাংশ রেকর্ডের ওপর একটি পরীক্ষামূলক মাইগ্রেশন সফল হয়েছে। চূড়ান্ত মাইগ্রেশনের জন্য সময় ছয় ঘণ্টা। রোলব্যাকে কত সময় লাগে তা এখনো মাপা হয়নি।

### bn_cs

risk আর control-গুলো summarize করুন: customer data একটি নতুন system-এ move করা হবে। একটি full backup আছে। ১০ শতাংশ record-এর ওপর একটি test migration সফল হয়েছে। final migration window ছয় ঘণ্টা। rollback-এ কত সময় লাগে তা এখনো মাপা হয়নি।

### Boundary and ambiguity questions

- [ ] RIU-02: Existing backup is a control but not evidence of restore success; no compulsory new backup job is part of the summary task.
- [ ] RIU-03, RIU-05: Distinguish partial forward-migration test evidence from untimed rollback; neither proves final-window feasibility.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Identify the planned move of customer data to a new system as the operation whose integrity/availability needs protection.
  Rationale: Preserves the migration context without inventing sensitive categories or legal duties.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): State that a full backup exists as a recovery safeguard, without claiming restoration has been verified or timed.
  Rationale: Dropping or overstating the principal stated recovery control materially alters the risk picture.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): State that a test migration succeeded for 10% of records, providing partial validation rather than proof that the full migration will succeed.
  Rationale: A limited successful test cannot establish full-scale readiness.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): State that the final migration has a six-hour window, creating a completion/time feasibility constraint.
  Rationale: The supplied time boundary materially shapes operational feasibility.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical, identified-ambiguity-or-boundary): State that rollback duration is not yet measured, leaving uncertainty about whether recovery can fit the available migration window.
  Rationale: Omission would hide a central unresolved recovery/time risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants preserve customer data, full backup, successful test on 10% of records, a six-hour window and untimed rollback. A full backup is not the same as a verified restore. Linear scaling from a 10% test is not guaranteed. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH037

technical_troubleshooting; medium.

### en

A scheduled data import sometimes creates duplicate records. Propose a diagnostic approach that considers source duplication, retry behavior, keys, transaction logic, and timing.

### bn

নির্ধারিত সময়ে স্বয়ংক্রিয়ভাবে চলা একটি ডেটা ইমপোর্ট মাঝে মাঝে ডুপ্লিকেট রেকর্ড তৈরি করছে। উৎসে থাকা ডুপ্লিকেট, রিট্রাই করার আচরণ, ডেটাবেস-কি, ট্রানজ্যাকশনের লজিক এবং সময় বিবেচনা করে সমস্যা নির্ণয়ের একটি পদ্ধতি প্রস্তাব করুন।

### bn_cs

নির্ধারিত সময়ে চলা একটি data import মাঝে মাঝে duplicate record তৈরি করছে। source-এ duplication, retry behavior, key, transaction logic আর timing বিবেচনা করে সমস্যা নির্ণয়ের একটি approach propose করুন।

### Boundary and ambiguity questions

- [ ] RIU-02, RIU-04: Retry policy and transactional partial-state handling can interact but earn separate credit only for distinct propositions.
- [ ] RIU-06: No required destructive cleanup or speculative root-cause verdict; preserve records while investigating.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Check whether the input already contains duplicate logical records or repeated source batches before the import writes them.
  Rationale: Tests source duplication independently of importer behavior.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; identified-ambiguity-or-boundary): Inspect retry/replay behavior and whether partially completed or repeated imports are idempotent.
  Rationale: Tests duplicate creation when work is retried rather than assuming each job runs once.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check the logical record keys, matching/upsert rules and enforced uniqueness against how records should be identified.
  Rationale: Tests whether the same entity can be inserted under an absent or unsuitable key.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Review transaction boundaries and partial-failure/commit handling for windows that insert records without recording successful completion consistently.
  Rationale: Tests transaction logic as distinct from input and retry policy.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Correlate duplicate timestamps with overlapping scheduled jobs, concurrency or timing races.
  Rationale: Tests the named temporal/concurrent cause rather than treating scheduling as inherently serial.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical, identified-ambiguity-or-boundary): Trace representative duplicate records through input identifiers and run/retry/commit logs to compare the hypotheses and locate where a second write is introduced.
  Rationale: A disconnected checklist cannot distinguish the causes of the intermittent duplicates.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Links a representative duplicate to a specific source/run/retry/transaction pattern but does not specify a discriminating comparison or reproduction.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants name five cause areas and an intermittent scheduled import. No actual schema, database or job overlap is established. Repair must not be compulsory deletion of apparent duplicates without establishing identity and provenance. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH062

technical_troubleshooting; easy.

### en

A laptop keyboard has several keys that suddenly stop responding. Describe basic checks before recommending hardware replacement.

### bn

একটি ল্যাপটপের কিবোর্ডের কয়েকটি বাটন হঠাৎ সাড়া দেওয়া বন্ধ করে দিয়েছে। হার্ডওয়্যার বদলানোর পরামর্শ দেওয়ার আগে কোন কোন প্রাথমিক চেক করা উচিত তা বর্ণনা করুন।

### bn_cs

একটি laptop keyboard-এর কয়েকটি key হঠাৎ respond করা বন্ধ করে দিয়েছে। hardware replacement suggest করার আগে কোন কোন basic check করা উচিত তা describe করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-04: Application/restart scope and an independent input/diagnostic comparison are distinct; accept proportionate equivalent tests.
- [ ] RIU-03: Do not require opening the laptop or removing keycaps; any physical procedure must avoid unsafe power/liquid handling.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Check whether the same keys fail across applications or after a simple restart, distinguishing a transient/application issue from a persistent system-level problem.
  Rationale: Tests software scope before condemning the hardware.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check relevant keyboard/accessibility/layout settings or recent configuration changes that can alter key response.
  Rationale: Tests a distinct simple configuration route without assuming a particular operating system.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary): Inspect the affected keys for obvious obstruction or damage using safe, non-destructive handling rather than forced disassembly.
  Rationale: Tests a physical explanation without inventing a spill or requiring key removal.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Use an appropriate controlled input comparison, such as an external keyboard or preboot/diagnostic test, to see whether the failure follows the built-in keyboard before deciding on replacement.
  Rationale: Provides discriminating evidence; recognition of a built-in hardware fault is not assumed from symptoms alone.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants preserve several suddenly nonresponsive laptop keys. No spill, damage or hardware defect is given. External keyboard and preboot tests are alternative comparisons, not all compulsory. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH067

technical_troubleshooting; medium.

### en

A monitor intermittently loses signal for one or two seconds while the computer continues running. Propose a troubleshooting sequence for cable, display, graphics, power, and driver causes.

### bn

কম্পিউটার চালু থাকা অবস্থাতেই মনিটর মাঝে মাঝে এক-দুই সেকেন্ডের জন্য সিগন্যাল হারিয়ে ফেলে। ক্যাবল, ডিসপ্লে, গ্রাফিক্স, পাওয়ার এবং ড্রাইভার-সংক্রান্ত কারণ পরীক্ষার জন্য সমস্যা সমাধানের একটি ধাপক্রম প্রস্তাব করুন।

### bn_cs

computer চালু থাকা অবস্থাতেই monitor মাঝে মাঝে এক-দুই সেকেন্ডের জন্য signal হারিয়ে ফেলে। cable, display, graphics, power আর driver-এর কারণ check করার জন্য একটি troubleshooting sequence propose করুন।

### Boundary and ambiguity questions

- [ ] RIU-03, RIU-05: Graphics operating conditions/event evidence and driver-change evidence are distinct; do not require a replacement GPU.
- [ ] RIU-04: Power testing means safe external checks; no hazardous work inside mains-powered equipment.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Check and, where feasible, safely reseat or substitute the display cable/connector/port to test a connection fault.
  Rationale: Tests the named cable route with proportionate reversible checks.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Compare with another display or input/source where feasible to see whether the fault follows the monitor.
  Rationale: Separates display behavior from the running computer.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Inspect graphics-output conditions such as GPU/display event evidence or resolution/refresh compatibility while correlating the brief losses.
  Rationale: Tests the named graphics path without presuming the GPU is defective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Check external display power connections/settings and relevant power-state behavior for momentary interruption while the computer remains running.
  Rationale: Tests monitor/power-path interruption rather than assuming a full computer shutdown.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; identified-ambiguity-or-boundary): Check supported graphics/display drivers and recent changes, using a justified update or rollback comparison where appropriate.
  Rationale: Tests the driver route without making reinstall a universal first step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Order reversible low-risk checks before invasive changes and change one relevant factor at a time, using whether the signal loss follows each comparison to narrow the cause.
  Rationale: Without an interpretable sequence the plan cannot separate the named competing causes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Specifies a reasonable low-risk-to-invasive sequence but does not explain how comparison results narrow the cause; an unsequenced list scores 0.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants preserve one-to-two-second signal loss while the computer keeps running. This is not proof of GPU failure or system power loss. No live PSU opening, monitor opening or forced firmware flashing is required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH090

technical_troubleshooting; hard.

### en

A nightly export contains occasional character corruption only in multilingual text fields. Propose a diagnostic strategy covering source encoding, transformations, transport, destination encoding, and rendering.

### bn

রাতে তৈরি হওয়া একটি এক্সপোর্ট ফাইলে মাঝে মাঝে শুধু বহুভাষিক টেক্সট ফিল্ডে অক্ষর নষ্ট হয়ে যায়। উৎসের এনকোডিং, মাঝের রূপান্তর, স্থানান্তর, গন্তব্যের এনকোডিং এবং রেন্ডারিং অন্তর্ভুক্ত করে সমস্যা নির্ণয়ের একটি কৌশল প্রস্তাব করুন।

### bn_cs

রাতে তৈরি হওয়া একটি export file-এ মাঝে মাঝে শুধু বহুভাষিক text field-এ character নষ্ট হয়ে যায়। source encoding, মাঝের transformation, transport, destination encoding আর rendering বিবেচনা করে সমস্যা নির্ণয়ের একটি strategy propose করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-04: Source and destination decoding are different boundaries; no assumed UTF-8 conversion as a universal repair.
- [ ] RIU-05: If bytes/code points are intact, a rendering problem must not be treated as permission to overwrite the data.
- [ ] RIU-06: Review ordinal positive anchors; boundary tracing must be operational rather than simply saying check the whole pipeline.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary): Inspect representative affected source text and its actual bytes/declared encoding, including multilingual characters, to establish whether corruption exists before export.
  Rationale: Locates the source boundary rather than assuming the export begins with clean text.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Trace intermediate transformations/serialization for incorrect decoding, re-encoding, truncation or lossy conversion of the affected fields.
  Rationale: Tests the separately named transformation stage.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Compare bytes or appropriate integrity evidence across transport boundaries to determine whether transfer changes the exported content.
  Rationale: Tests transport separately from producer and consumer interpretation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Check the destination’s stored bytes, declared encoding and import/decoding settings against the actual export encoding.
  Rationale: Tests a destination decoding/storage mismatch without assuming one platform.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Check whether display/font/rendering produces the apparent corruption when underlying stored text is intact, using another trusted viewer or code-point inspection.
  Rationale: Separates presentation defects from irreversible data corruption.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical, identified-ambiguity-or-boundary): Reproduce with a small representative multilingual sample and compare the same data at successive pipeline boundaries to locate the first divergence, including intermittent run/configuration differences.
  Rationale: An unlinked list of encodings cannot determine where the intermittent corruption is introduced.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Tracks a representative multilingual sample across at least two meaningful pipeline boundaries but does not identify how the first divergence or intermittent differences would locate the fault.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants name source encoding, transformations, transport, destination encoding and rendering. No file encoding or corrupt byte sample is supplied. Valid Unicode normalization does not necessarily indicate corruption; font rendering differs from stored byte damage. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH097

technical_troubleshooting; medium.

### en

A docking station provides power and display output but its USB ports do not work. Explain a structured troubleshooting sequence.

### bn

একটি ডকিং স্টেশন থেকে পাওয়ার ও ডিসপ্লে আউটপুট পাওয়া যাচ্ছে, কিন্তু এর ইউএসবি পোর্টগুলো কাজ করছে না। সমস্যা সমাধানের একটি সুসংগঠিত ধাপক্রম ব্যাখ্যা করুন।

### bn_cs

একটি docking station power আর display output দিচ্ছে, কিন্তু এর USB port-গুলো কাজ করছে না। একটি structured troubleshooting sequence explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01: A charging-only or inadequately capable cable can leave other functions working; avoid inferring a specific cable fault is already proven.
- [ ] RIU-04: Respect managed security restrictions; no bypassing USB controls to force a device to work.
- [ ] RIU-05: An alternative diagnostic route is valid; no requirement to own a second computer if equivalent evidence isolates the failure.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary): Check the upstream dock-to-host connection, supported host port and cable for USB data capability and seating rather than inferring data works from power/display alone.
  Rationale: Targets the defining separation between working power/display and failed USB.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Compare a known-working USB device directly on the host and on multiple dock ports, disconnecting other peripherals as useful to isolate device versus dock USB failure.
  Rationale: Separates peripheral failure from dock-path failure without requiring every port be populated.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Use a safe reconnect or dock/host power-cycle comparison and check whether the host detects the dock’s USB hub/controller.
  Rationale: Tests connection/enumeration state before major configuration changes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Check relevant host USB/dock drivers, supported firmware, settings or management restrictions for the specific dock/host configuration.
  Rationale: Tests software/compatibility/policy routes without prescribing an unnecessary universal firmware flash.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical, identified-ambiguity-or-boundary): Use controlled cable/port/device or alternate-host comparisons in a structured order to decide whether the USB fault follows the dock, upstream connection or host before replacement.
  Rationale: A list of generic resets cannot localize the selective USB failure or justify replacement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Provides an orderly USB-focused sequence with at least one controlled comparison but does not explain how results distinguish dock, connection and host.

Draft notes: P02 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants preserve power/display functioning but USB failing; these functions do not prove the upstream USB data path works. No particular Thunderbolt generation, OS or dock firmware is supplied. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
