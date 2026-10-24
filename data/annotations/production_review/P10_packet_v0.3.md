# P10 independent review packet

Status: pending. AI-produced draft annotations; no human acceptance is claimed.

Each task needs bilingual equivalence and full-prompt coverage review. Review all critical units, all ambiguity/boundary questions below, and every prespecified ordinary sample item. Additional ordinary units may be reviewed. Blank identity/decision fields are intentional.

24 tasks; 113 RIUs; 52 critical; 20 ordinary sample units; 72 mandatory unit reviews.

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

## CYBER033

cybersecurity_digital_safety; easy.

### en

A small office shares one Wi-Fi password with employees and visitors. Explain why separating access could improve security.

### bn

একটি ছোট অফিস কর্মী ও অতিথিদের সঙ্গে একই ওয়াই-ফাই পাসওয়ার্ড শেয়ার করে। অ্যাক্সেস আলাদা করলে কেন নিরাপত্তা বাড়তে পারে তা ব্যাখ্যা করুন।

### bn_cs

একটি ছোট office employee আর visitor-দের সঙ্গে একই Wi-Fi password share করে। access আলাদা করলে কেন security বাড়তে পারে তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that a shared password gives visitors access to the same network as office devices and data.
  Rationale: The core risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Explain that a widely shared password is hard to control or revoke when people leave.
  Rationale: Revocation problem.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Recommend a separate guest network isolated from internal devices.
  Rationale: The core remedy.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Recommend changing the employee password and limiting who knows it.
  Rationale: Hardening.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER040

cybersecurity_digital_safety; hard.

### en

A company wants to permit third-party vendor access to a small set of internal systems. Design an access model that limits exposure and supports monitoring, revocation, and accountability.

### bn

একটি প্রতিষ্ঠান থার্ড-পার্টি ভেন্ডরকে অল্প কয়েকটি অভ্যন্তরীণ সিস্টেমে অ্যাক্সেস দিতে চায়। ঝুঁকির পরিসর সীমিত রাখে এবং মনিটরিং, অ্যাক্সেস প্রত্যাহার ও জবাবদিহি নিশ্চিত করে—এমন একটি অ্যাক্সেস মডেল তৈরি করুন।

### bn_cs

একটি company third-party vendor-কে অল্প কয়েকটি internal system-এ access দিতে চায়। exposure সীমিত রাখে এবং monitoring, revocation আর accountability support করে—এমন একটি access model design করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Give each vendor person a named individual account rather than shared credentials.
  Rationale: Accountability.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Limit access to only the specific systems needed, through a controlled path such as a VPN, jump host or vendor portal.
  Rationale: Limits exposure.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Require MFA for vendor access.
  Rationale: Authentication strength.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Log and monitor vendor sessions.
  Rationale: Monitoring.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Make access time-limited or approval-based and revoke it promptly when work ends or the contract changes.
  Rationale: Revocation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Review vendor access periodically and define contractual security obligations.
  Rationale: Governance.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER055

cybersecurity_digital_safety; medium.

### en

An employee reports entering credentials into a fake login page. Explain the immediate account, device, logging, and communication steps that should follow.

### bn

একজন কর্মী জানিয়েছেন, তিনি একটি ভুয়া লগইন পেজে তাঁর ক্রেডেনশিয়াল দিয়ে ফেলেছেন। এরপর অ্যাকাউন্ট, ডিভাইস, লগিং এবং যোগাযোগ-সংক্রান্ত কোন কোন তাৎক্ষণিক পদক্ষেপ নেওয়া উচিত তা ব্যাখ্যা করুন।

### bn_cs

একজন employee জানিয়েছেন, তিনি একটি fake login page-এ তাঁর credential দিয়ে ফেলেছেন। এরপর account, device, logging আর communication-এর কোন কোন immediate step নেওয়া উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Reset the password immediately and revoke active sessions or tokens.
  Rationale: Account step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check and reset MFA if it may have been captured, and change the password anywhere it was reused.
  Rationale: Account step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Review sign-in and account activity logs for unauthorized access after the credential entry.
  Rationale: Logging step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Check the device for malware if a download or attachment was involved.
  Rationale: Device step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Report to security and warn colleagues if the phishing page may target others.
  Rationale: Communication step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER068

cybersecurity_digital_safety; medium.

### en

A multi-account cloud environment has inconsistent security controls across teams. Propose a governance approach that provides centralized safeguards without preventing necessary local autonomy.

### bn

একাধিক অ্যাকাউন্ট নিয়ে গঠিত একটি ক্লাউড এনভায়রনমেন্টে বিভিন্ন টিমের নিরাপত্তা নিয়ন্ত্রণ একরকম নয়। প্রয়োজনীয় স্থানীয় স্বাধীনতা বাধাগ্রস্ত না করে কেন্দ্রীয় সুরক্ষা দেয়—এমন একটি গভর্নেন্স পদ্ধতি প্রস্তাব করুন।

### bn_cs

একাধিক account নিয়ে গঠিত একটি cloud environment-এ বিভিন্ন team-এর security control একরকম নয়। প্রয়োজনীয় local autonomy আটকে না দিয়ে centralized safeguard দেয়—এমন একটি governance approach propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Define a small set of mandatory baseline controls enforced centrally across all accounts, such as logging, identity and guardrail policies.
  Rationale: Centralized safeguards.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Allow teams autonomy within the guardrails, such as choosing services and configurations that do not violate baselines.
  Rationale: Local autonomy.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Monitor compliance centrally, for example with automated posture checks.
  Rationale: Visibility.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Provide an exception process with justification and expiry.
  Rationale: Flexibility with control.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Provide shared templates or tooling that make compliant setups easy.
  Rationale: Adoption.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER075

cybersecurity_digital_safety; medium.

### en

A team stores application secrets directly in configuration files. Explain the risks and a practical migration path to safer secret management.

### bn

একটি টিম অ্যাপ্লিকেশনের সিক্রেট সরাসরি কনফিগারেশন ফাইলে রাখে। এর ঝুঁকি এবং আরও নিরাপদ সিক্রেট ম্যানেজমেন্টে যাওয়ার একটি বাস্তবসম্মত পথ ব্যাখ্যা করুন।

### bn_cs

একটি team application secret সরাসরি configuration file-এ রাখে। এর risk আর আরও safe secret management-এ migrate করার একটি practical পথ explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that secrets in config files can leak through version control, backups or broad file access.
  Rationale: The core risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Move secrets to a secrets manager or vault, or environment injection at runtime.
  Rationale: The core remedy.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Rotate the secrets that were stored in the files, because they may already be exposed.
  Rationale: Exposed secrets stay valid otherwise.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Migrate incrementally, application by application, testing each change.
  Rationale: Practical path.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Add scanning to prevent new secrets being committed.
  Rationale: Prevention.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC007

decision_support; medium.

### en

A researcher has limited time before a deadline and must choose between collecting more data, improving analysis, polishing figures, or expanding the literature review. Explain how to make the choice based on the paper's current weaknesses.

### bn

একজন গবেষকের সময়সীমার আগে হাতে সময় কম, এবং তাঁকে আরও ডেটা সংগ্রহ, বিশ্লেষণ উন্নত করা, চিত্রগুলো পরিমার্জন করা অথবা সাহিত্য পর্যালোচনা বাড়ানো—এর মধ্যে বেছে নিতে হবে। গবেষণাপত্রের বর্তমান দুর্বলতার ভিত্তিতে কীভাবে এই সিদ্ধান্ত নেবেন তা ব্যাখ্যা করুন।

### bn_cs

একজন researcher-এর deadline-এর আগে হাতে সময় কম, এবং তাঁকে আরও data collect করা, analysis improve করা, figure polish করা অথবা literature review বাড়ানো—এর মধ্যে বেছে নিতে হবে। paper-এর বর্তমান weakness-এর ভিত্তিতে কীভাবে এই choice করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify the paper's most serious current weakness, such as from reviewer feedback or self-assessment against the claims.
  Rationale: Core basis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Prioritize the activity that most strengthens the main claims, typically analysis or data over figure polish.
  Rationale: The choice rule.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Consider feasibility within the remaining time, such as whether new data can be collected and analyzed in time.
  Rationale: Feasibility.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Consider minimal versions of lower-priority tasks.
  Rationale: Balance.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC016

decision_support; medium.

### en

A shared lab has limited equipment and three groups need it for different lengths of time before separate deadlines. Propose a scheduling rule that is transparent and practical.

### bn

একটি শেয়ার করা ল্যাবে যন্ত্রপাতি সীমিত, এবং তিনটি দলের আলাদা আলাদা সময়সীমার আগে ভিন্ন ভিন্ন সময়ের জন্য সেগুলো দরকার। স্বচ্ছ ও বাস্তবসম্মত একটি সময়সূচির নিয়ম প্রস্তাব করুন।

### bn_cs

একটি shared lab-এ equipment সীমিত, এবং তিনটি group-এর আলাদা আলাদা deadline-এর আগে বিভিন্ন সময়ের জন্য সেগুলো দরকার। transparent আর practical একটি scheduling rule propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Use a clear rule, such as earliest deadline first with time requests stated in advance.
  Rationale: Transparency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Check that each group's required time fits before its deadline.
  Rationale: Practicality.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Publish the schedule in a shared calendar.
  Rationale: Transparency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Define how to handle conflicts or changes, such as swapping slots by agreement.
  Rationale: Practicality.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC022

decision_support; easy.

### en

A small team needs a place to share meeting notes. Explain what factors matter when choosing between email, a shared document, and a team wiki.

### bn

একটি ছোট টিমের মিটিংয়ের নোট শেয়ার করার একটি জায়গা দরকার। ইমেইল, একটি শেয়ার করা ডকুমেন্ট এবং টিমের উইকির মধ্যে বেছে নেওয়ার সময় কোন বিষয়গুলো গুরুত্বপূর্ণ তা ব্যাখ্যা করুন।

### bn_cs

একটি ছোট team-এর meeting note share করার একটি জায়গা দরকার। email, একটি shared document আর team wiki-র মধ্যে বেছে নেওয়ার সময় কোন factor-গুলো গুরুত্বপূর্ণ তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Consider how easily notes can be found later and searched.
  Rationale: Key factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Consider whether people need to edit notes collaboratively.
  Rationale: Key factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Consider access control and who needs to see the notes.
  Rationale: Key factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Relate the factors to the three options, such as email being easy but scattered, documents being collaborative and wikis being structured.
  Rationale: The comparison.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC030

decision_support; hard.

### en

A university is considering an AI-assisted writing tool for staff use. Propose an evaluation framework covering privacy, accuracy, accessibility, workflow fit, oversight, cost, and failure handling.

### bn

একটি বিশ্ববিদ্যালয় কর্মীদের ব্যবহারের জন্য এআই-সহায়িত একটি লেখার টুল বিবেচনা করছে। প্রাইভেসি, নির্ভুলতা, অ্যাক্সেসিবিলিটি, কাজের ধারার সঙ্গে খাপ খাওয়া, তদারকি, খরচ এবং ভুল বা ব্যর্থতা সামলানো নিয়ে একটি মূল্যায়ন কাঠামো প্রস্তাব করুন।

### bn_cs

একটি university staff-দের ব্যবহারের জন্য একটি AI-assisted writing tool বিবেচনা করছে। privacy, নির্ভুলতা, accessibility, কাজের ধারার সঙ্গে খাপ খাওয়া, তদারকি, খরচ আর failure handling নিয়ে একটি evaluation framework propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Evaluate privacy: what data the tool sends, stores or uses for training, and compliance with institutional rules.
  Rationale: Named criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Evaluate accuracy, including fabricated content or citations, with testing on realistic tasks.
  Rationale: Named criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Evaluate accessibility for staff with disabilities.
  Rationale: Named criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Evaluate workflow fit through a pilot with representative staff.
  Rationale: Named criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Define oversight, such as human review responsibility and usage guidelines.
  Rationale: Named criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Evaluate total cost, including licensing and support.
  Rationale: Named criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (supporting; ordinary, outside prespecified sample): Plan failure handling, such as reporting errors and fallback when the tool is unavailable.
  Rationale: Named criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC097

decision_support; medium.

### en

A pilot program shows promising results but the sample is small. Explain how to decide whether to expand, continue testing, or stop.

### bn

একটি পাইলট কর্মসূচি আশাব্যঞ্জক ফল দেখিয়েছে, কিন্তু নমুনার আকার ছোট। কর্মসূচিটি সম্প্রসারণ করা, আরও পরীক্ষা চালিয়ে যাওয়া নাকি বন্ধ করা—তা কীভাবে ঠিক করবেন ব্যাখ্যা করুন।

### bn_cs

একটি pilot program promising result দেখিয়েছে, কিন্তু sample ছোট। program-টা expand করা, আরও testing চালিয়ে যাওয়া নাকি stop করা—সেটা কীভাবে decide করবেন explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that a small sample makes the results uncertain, so promising results may not hold.
  Rationale: Core caution.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Consider costs and risks of expanding if the effect turns out smaller.
  Rationale: Decision factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Consider continuing testing with a larger or more representative sample before full expansion.
  Rationale: Option.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Define criteria in advance for expanding, continuing or stopping.
  Rationale: Decision rule.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC012

procedural_instructional; easy.

### en

Describe a simple way to record meeting decisions and action items so everyone knows what happens next.

### bn

মিটিংয়ের সিদ্ধান্ত এবং করণীয় কাজগুলো লিখে রাখার একটি সহজ উপায় বর্ণনা করুন, যাতে এরপর কী হবে তা সবাই জানেন।

### bn_cs

meeting-এর decision আর action item-গুলো record করার একটি সহজ উপায় describe করুন, যাতে এরপর কী হবে তা সবাই জানেন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Record each decision clearly during or right after the meeting.
  Rationale: Decisions.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Record each action item with an owner and due date.
  Rationale: Actions.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Share the notes promptly in one agreed place.
  Rationale: Visibility.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Review open actions at the next meeting.
  Rationale: Follow-up.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC019

procedural_instructional; hard.

### en

A team wants to reduce unnecessary meetings without losing coordination. Propose a procedure for deciding which updates should be asynchronous and which require live discussion.

### bn

একটি টিম সমন্বয় না হারিয়ে অপ্রয়োজনীয় মিটিং কমাতে চায়। কোন আপডেটগুলো অ্যাসিনক্রোনাসভাবে দেওয়া যাবে আর কোনগুলোর জন্য সরাসরি আলোচনা লাগবে, তা ঠিক করার একটি পদ্ধতি প্রস্তাব করুন।

### bn_cs

একটি team coordination না হারিয়ে অপ্রয়োজনীয় meeting কমাতে চায়। কোন update-গুলো asynchronous হতে পারে আর কোনগুলোর জন্য live discussion লাগবে, তা decide করার একটি procedure propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Use criteria such as complexity, need for discussion, urgency or conflict to classify updates.
  Rationale: Decision criteria.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Make routine status updates asynchronous in a shared written channel.
  Rationale: Async path.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Reserve live meetings for decisions, conflicts or complex problems.
  Rationale: Live path.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Review whether coordination problems arise and adjust.
  Rationale: Keeps coordination.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC075

procedural_instructional; medium.

### en

Explain how to reconcile a list of purchases against receipts and a payment statement when some descriptions do not match exactly.

### bn

কিছু বিবরণ হুবহু না মিললে কেনাকাটার একটি তালিকাকে রসিদ ও পেমেন্ট স্টেটমেন্টের সঙ্গে কীভাবে মিলিয়ে দেখবেন তা ব্যাখ্যা করুন।

### bn_cs

কিছু description হুবহু না মিললে purchase-এর একটি list-কে receipt আর payment statement-এর সঙ্গে কীভাবে reconcile করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Match items primarily by amount and date rather than by description.
  Rationale: Core matching method.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Use merchant names, reference numbers or locations to resolve ambiguous matches.
  Rationale: Secondary evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): List unmatched items and investigate them, such as by contacting the merchant or bank.
  Rationale: Exceptions.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Record the matches and notes for audit.
  Rationale: Documentation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC084

procedural_instructional; medium.

### en

A user is moving from an old computer to a new one. Propose a procedure for inventory, backup, transfer, validation, and secure cleanup of the old device.

### bn

একজন ব্যবহারকারী পুরোনো কম্পিউটার থেকে নতুন কম্পিউটারে যাচ্ছেন। কী কী আছে তার তালিকা, ব্যাকআপ, স্থানান্তর, যাচাই এবং পুরোনো ডিভাইসটি নিরাপদে মুছে পরিষ্কার করার একটি পদ্ধতি প্রস্তাব করুন।

### bn_cs

একজন user পুরোনো computer থেকে নতুন computer-এ যাচ্ছেন। inventory, backup, transfer, validation আর পুরোনো device-টা securely cleanup করার একটি procedure propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Inventory files, applications, settings and licenses to move.
  Rationale: Named step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Back up the old computer before transferring.
  Rationale: Named step; safeguard.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Transfer data and reinstall applications on the new computer.
  Rationale: Named step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Validate that files and applications work on the new computer before wiping the old one.
  Rationale: Named step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Securely wipe the old device and sign out of or deauthorize accounts and licenses.
  Rationale: Named step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN027

information_synthesis; medium.

### en

Create a concise timeline and flag the dependency problem: Database upgrade planned for Saturday. Application testing was scheduled for Friday. The test environment did not receive the new database version until Sunday. Production release was planned for Monday.

### bn

একটি সংক্ষিপ্ত সময়রেখা তৈরি করুন এবং ডিপেন্ডেন্সির সমস্যাটি চিহ্নিত করুন: ডেটাবেস আপগ্রেডের পরিকল্পনা ছিল শনিবার। অ্যাপ্লিকেশন টেস্টিং নির্ধারিত ছিল শুক্রবার। টেস্ট এনভায়রনমেন্টে ডেটাবেসের নতুন ভার্সন পৌঁছায় রবিবারে। প্রোডাকশন রিলিজের পরিকল্পনা ছিল সোমবার।

### bn_cs

একটি concise timeline তৈরি করুন এবং dependency problem-টা flag করুন: database upgrade-এর plan ছিল শনিবার। application testing schedule করা ছিল শুক্রবার। test environment-এ database-এর নতুন version পৌঁছায় রবিবারে। production release-এর plan ছিল সোমবার।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Order the events: testing Friday, planned upgrade Saturday, new version in test Sunday, release Monday.
  Rationale: Timeline.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Flag that application testing on Friday happened before the test environment had the new database version, so it did not test against that version.
  Rationale: The dependency problem.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Flag that Monday's release is at risk because testing against the new version has not been done.
  Rationale: Consequence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Suggest retesting against the new version before release.
  Rationale: Remedy.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN057

information_synthesis; medium.

### en

A project owner says launch risk is low. The testing team reports two unresolved defects, one of which affects a common workflow. Summarize what can be stated factually and what remains an assessment.

### bn

প্রজেক্টের দায়িত্বপ্রাপ্ত ব্যক্তি বলছেন চালুর ঝুঁকি কম। টেস্টিং টিম দুটি অমীমাংসিত ত্রুটির কথা জানিয়েছে, যার একটি বহুল ব্যবহৃত একটি ওয়ার্কফ্লোকে প্রভাবিত করে। কোনটি তথ্য হিসেবে বলা যায় আর কোনটি মূল্যায়ন হিসেবেই থেকে যায় তা সংক্ষেপ করুন।

### bn_cs

project owner বলছেন launch risk কম। testing team দুটি unresolved defect report করেছে, যার একটি common একটি workflow-কে affect করে। কোনটা factually বলা যায় আর কোনটা assessment হিসেবেই থেকে যায় তা summarize করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State as fact that the testing team reported two unresolved defects, one affecting a common workflow.
  Rationale: Fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Identify the project owner's "low risk" as an assessment, not established fact.
  Rationale: Assessment.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Note that the defect in a common workflow is in tension with a low-risk assessment.
  Rationale: Tension.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Identify what would resolve the question, such as defect severity or workarounds.
  Rationale: Next step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN073

information_synthesis; easy.

### en

Determine whether any option works: Room A seats 20 and has a projector. Room B seats 35 but has no projector. The event needs seats for 30 and a projector.

### bn

কোনো বিকল্প কাজ করে কি না নির্ধারণ করুন: কক্ষ A-তে ২০টি আসন আছে এবং একটি প্রজেক্টর আছে। কক্ষ B-তে ৩৫টি আসন আছে, কিন্তু প্রজেক্টর নেই। অনুষ্ঠানের জন্য ৩০টি আসন এবং একটি প্রজেক্টর দরকার।

### bn_cs

কোনো option কাজ করে কি না determine করুন: Room A-তে ২০টি seat আছে এবং একটি projector আছে। Room B-তে ৩৫টি seat আছে, কিন্তু projector নেই। event-এর জন্য ৩০টি seat আর একটি projector দরকার।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that Room A has a projector but only 20 seats.
  Rationale: Check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that Room B has 35 seats but no projector.
  Rationale: Check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Conclude that neither room satisfies both requirements.
  Rationale: Answer.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Suggest a workaround such as bringing a projector to Room B.
  Rationale: Useful.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN079

information_synthesis; hard.

### en

Determine whether the project deadline is feasible: Design takes 3 days. Development takes 5 days after design. Testing takes 2 days after development. Design starts Monday. Work happens only Monday through Friday. The deadline is Friday of the following week.

### bn

প্রজেক্টের সময়সীমা পূরণ করা সম্ভব কি না নির্ধারণ করুন: ডিজাইনে ৩ দিন লাগে। ডিজাইনের পরে ডেভেলপমেন্টে ৫ দিন লাগে। ডেভেলপমেন্টের পরে টেস্টিংয়ে ২ দিন লাগে। ডিজাইন শুরু হবে সোমবার। কাজ হয় শুধু সোমবার থেকে শুক্রবার। সময়সীমা পরের সপ্তাহের শুক্রবার।

### bn_cs

project deadline feasible কি না determine করুন: design-এ ৩ দিন লাগে। design-এর পরে development-এ ৫ দিন লাগে। development-এর পরে testing-এ ২ দিন লাগে। design শুরু হবে সোমবার। কাজ হয় শুধু সোমবার থেকে শুক্রবার। deadline পরের সপ্তাহের শুক্রবার।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Schedule design Monday to Wednesday of week one.
  Rationale: Calculation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Schedule development over five working days: Thursday and Friday of week one, and Monday to Wednesday of week two.
  Rationale: Calculation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Schedule testing Thursday and Friday of week two and conclude the deadline is feasible.
  Rationale: Answer.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Note that there is no buffer, so any delay would miss the deadline.
  Rationale: Risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN097

information_synthesis; medium.

### en

Summarize the operational situation for incident leadership and explicitly separate observations from possible causes. On Monday the service processed 20 percent more requests than the average Monday during the previous eight weeks. Median response time increased from 4 minutes to 7 minutes between 10:15 AM and 12:40 PM. Staffing was at the normal Monday level, and no scheduled staff absence was recorded. One internal case-routing tool was intermittently unavailable during parts of the same period. Monitoring shows three tool interruptions lasting 6, 11, and 4 minutes, but the slower response time continued for more than 30 minutes after the final recorded interruption. The queue of unassigned cases reached 86 at 11:20 AM; the normal Monday peak is approximately 45. A database dashboard showed CPU utilization within its usual range, while one application server briefly reached 88 percent memory utilization. No application crash was recorded. At 11:35 AM supervisors temporarily reassigned four employees from nonurgent work to the queue, and the backlog began declining at 12:05 PM. Response time returned below 5 minutes by 1:10 PM. No configuration deployment occurred Monday morning. A network-maintenance event occurred Sunday night and was reported complete before 5:00 AM Monday; no evidence currently links it to the slowdown. The routing-tool team is still investigating its interruptions. The available observations support several plausible contributors—including higher volume and tool instability—but do not establish one verified root cause. The summary must not state that the internal tool, staffing, database, application server, or Sunday maintenance caused the slowdown unless the evidence above actually supports that conclusion.

### bn

ইনসিডেন্ট পরিচালনাকারী নেতৃত্বের জন্য অপারেশনাল পরিস্থিতির সারাংশ তৈরি করুন এবং পর্যবেক্ষণগুলোকে সম্ভাব্য কারণ থেকে স্পষ্টভাবে আলাদা রাখুন। সোমবার সার্ভিসটি আগের আট সপ্তাহের গড় সোমবারের তুলনায় ২০ শতাংশ বেশি রিকোয়েস্ট প্রসেস করেছে। সকাল ১০টা ১৫ মিনিট থেকে দুপুর ১২টা ৪০ মিনিটের মধ্যে রেসপন্স টাইমের মধ্যমা ৪ মিনিট থেকে বেড়ে ৭ মিনিট হয়েছে। জনবল ছিল সোমবারের স্বাভাবিক মাত্রায়, এবং নির্ধারিত কোনো কর্মী-অনুপস্থিতি রেকর্ড করা হয়নি। একই সময়ের কিছু অংশে একটি অভ্যন্তরীণ কেস-রাউটিং টুল মাঝে মাঝে অনুপলব্ধ ছিল। মনিটরিংয়ে টুলটির তিনটি বিঘ্ন দেখা গেছে, যেগুলো ৬, ১১ এবং ৪ মিনিট স্থায়ী ছিল, কিন্তু শেষ রেকর্ড করা বিঘ্নের পরও ৩০ মিনিটের বেশি সময় ধরে রেসপন্স টাইম ধীর ছিল। সকাল ১১টা ২০ মিনিটে কাউকে বরাদ্দ না করা কেসের কিউ ৮৬-তে পৌঁছায়; সোমবারের স্বাভাবিক সর্বোচ্চ সংখ্যা প্রায় ৪৫। একটি ডেটাবেস ড্যাশবোর্ডে সিপিইউ ব্যবহার স্বাভাবিক সীমার মধ্যে ছিল, আর একটি অ্যাপ্লিকেশন সার্ভারে অল্প সময়ের জন্য মেমরি ব্যবহার ৮৮ শতাংশে পৌঁছেছিল। কোনো অ্যাপ্লিকেশন ক্র্যাশ রেকর্ড হয়নি। সকাল ১১টা ৩৫ মিনিটে সুপারভাইজাররা কম জরুরি কাজ থেকে চারজন কর্মীকে সাময়িকভাবে কিউতে সরিয়ে দেন, এবং দুপুর ১২টা ০৫ মিনিটে জমে থাকা কাজ কমতে শুরু করে। দুপুর ১টা ১০ মিনিটের মধ্যে রেসপন্স টাইম আবার ৫ মিনিটের নিচে নেমে আসে। সোমবার সকালে কোনো কনফিগারেশন ডিপ্লয়মেন্ট হয়নি। রবিবার রাতে একটি নেটওয়ার্ক রক্ষণাবেক্ষণ হয়েছিল এবং সোমবার ভোর ৫টার আগেই তা সম্পন্ন বলে জানানো হয়েছিল; বর্তমানে কোনো প্রমাণ এটিকে ধীরগতির সঙ্গে যুক্ত করে না। রাউটিং টুলের টিম এখনো এর বিঘ্নগুলোর কারণ তদন্ত করছে। হাতে থাকা পর্যবেক্ষণগুলো কয়েকটি সম্ভাব্য প্রভাবককে সমর্থন করে—যার মধ্যে আছে বাড়তি রিকোয়েস্টের চাপ ও টুলের অস্থিতিশীলতা—কিন্তু যাচাই করা কোনো একক মূল কারণ প্রতিষ্ঠা করে না। উপরের প্রমাণ সত্যিই সেই উপসংহার সমর্থন না করলে সারাংশে বলা যাবে না যে অভ্যন্তরীণ টুল, জনবল, ডেটাবেস, অ্যাপ্লিকেশন সার্ভার বা রবিবারের রক্ষণাবেক্ষণ ধীরগতির কারণ।

### bn_cs

incident leadership-এর জন্য operational situation-এর summary তৈরি করুন এবং observation-গুলোকে possible cause থেকে স্পষ্টভাবে আলাদা রাখুন। সোমবার service-টা আগের আট সপ্তাহের average সোমবারের তুলনায় ২০ শতাংশ বেশি request process করেছে। সকাল ১০টা ১৫ মিনিট থেকে দুপুর ১২টা ৪০ মিনিটের মধ্যে median response time ৪ মিনিট থেকে বেড়ে ৭ মিনিট হয়েছে। staffing ছিল সোমবারের normal level-এ, এবং scheduled কোনো staff absence record করা হয়নি। একই সময়ের কিছু অংশে একটি internal case-routing tool মাঝে মাঝে unavailable ছিল। monitoring-এ tool-টার তিনটি interruption দেখা গেছে, যেগুলো ৬, ১১ আর ৪ মিনিট স্থায়ী ছিল, কিন্তু শেষ recorded interruption-এর পরও ৩০ মিনিটের বেশি সময় ধরে response time slow ছিল। সকাল ১১টা ২০ মিনিটে unassigned case-এর queue ৮৬-তে পৌঁছায়; সোমবারের normal peak প্রায় ৪৫। একটি database dashboard-এ CPU utilization usual range-এর মধ্যে ছিল, আর একটি application server-এ অল্প সময়ের জন্য memory utilization ৮৮ শতাংশে পৌঁছেছিল। কোনো application crash record হয়নি। সকাল ১১টা ৩৫ মিনিটে supervisor-রা nonurgent কাজ থেকে চারজন employee-কে temporarily queue-তে reassign করেন, এবং দুপুর ১২টা ০৫ মিনিটে backlog কমতে শুরু করে। দুপুর ১টা ১০ মিনিটের মধ্যে response time আবার ৫ মিনিটের নিচে নেমে আসে। সোমবার সকালে কোনো configuration deployment হয়নি। রবিবার রাতে একটি network-maintenance event হয়েছিল এবং সোমবার ভোর ৫টার আগেই সেটা complete বলে report করা হয়েছিল; বর্তমানে কোনো evidence এটাকে slowdown-এর সঙ্গে link করে না। routing-tool team এখনো এর interruption-গুলো investigate করছে। available observation-গুলো কয়েকটি plausible contributor-কে support করে—যার মধ্যে আছে higher volume আর tool instability—কিন্তু verified কোনো single root cause establish করে না। উপরের evidence সত্যিই সেই conclusion support না করলে summary-তে বলা যাবে না যে internal tool, staffing, database, application server বা রবিবারের maintenance slowdown-এর কারণ।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State the observations: 20 percent more requests than the average Monday, and median response time rising from 4 to 7 minutes between 10:15 AM and 12:40 PM.
  Rationale: Observations.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): State that the unassigned queue peaked at 86 at 11:20 AM versus a normal peak of about 45.
  Rationale: Observation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): State that the routing tool had three interruptions (6, 11 and 4 minutes) but slowness continued over 30 minutes after the last one.
  Rationale: Observation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): State that database CPU was normal, one app server briefly reached 88 percent memory, and no crash occurred.
  Rationale: Observations.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): State that four staff were reassigned at 11:35 AM, the backlog declined from 12:05 PM and response time was under 5 minutes by 1:10 PM.
  Rationale: Observations.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Present higher volume and tool instability as plausible contributors without a verified single root cause.
  Rationale: Possible causes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (critical; all-critical): Do not state that the tool, staffing, database, app server or Sunday maintenance caused the slowdown; presenting them as possible or unlinked complies.
  Rationale: Explicit constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-08** (supporting; ordinary, outside prespecified sample): Note that staffing was normal, no deployment occurred and the maintenance has no evidence linking it.
  Rationale: Context.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Extended-context task. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
- [ ] CHECK-02: Observations are presented separately from possible causes.

## TECH003

technical_troubleshooting; medium.

### en

A computer shows very little free disk space even though the user does not remember saving large files. Describe a safe troubleshooting sequence.

### bn

একটি কম্পিউটারে ডিস্কের খালি জায়গা খুব কম দেখাচ্ছে, যদিও ব্যবহারকারীর বড় কোনো ফাইল সেভ করার কথা মনে পড়ছে না। সমস্যা খুঁজে বের করার একটি নিরাপদ ধাপক্রম বর্ণনা করুন।

### bn_cs

একটি computer-এ free disk space খুব কম দেখাচ্ছে, যদিও user-এর বড় কোনো file save করার কথা মনে পড়ছে না। একটি safe troubleshooting sequence describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Use a storage analysis tool to identify what is using space.
  Rationale: Evidence first.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check common hidden consumers such as temporary files, update caches, recycle bin, restore points or large logs.
  Rationale: Likely causes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Use built-in cleanup tools for safe categories.
  Rationale: Safe cleanup.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Do not delete unknown system or program files manually; identifying first and using safe tools complies.
  Rationale: Safety.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Consider malware or runaway processes if space keeps disappearing.
  Rationale: Further cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH022

technical_troubleshooting; easy.

### en

A PDF opens correctly on one computer but appears corrupted on another. Describe the first troubleshooting steps.

### bn

একটি পিডিএফ ফাইল এক কম্পিউটারে ঠিকভাবে খুলছে, কিন্তু আরেকটিতে ফাইলটি নষ্ট হয়ে গেছে বলে মনে হচ্ছে। সমস্যা সমাধানের প্রথম ধাপগুলো বর্ণনা করুন।

### bn_cs

একটি PDF এক computer-এ ঠিকভাবে open হচ্ছে, কিন্তু আরেকটিতে corrupted দেখাচ্ছে। প্রথম troubleshooting step-গুলো describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check whether the file transferred completely, such as comparing file size or re-downloading.
  Rationale: Distinguishes file damage from viewer issues.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Try opening it with another or updated PDF viewer on the failing computer.
  Rationale: Distinguishes viewer issues.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check for missing fonts or viewer settings.
  Rationale: Further cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Ask the sender for a fresh copy if the file is damaged.
  Rationale: Remedy.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH030

technical_troubleshooting; hard.

### en

A web application behaves correctly in one browser but fails in another after a recent deployment. Propose a systematic investigation that separates browser compatibility, cached assets, client-side code, and server behavior.

### bn

সাম্প্রতিক একটি ডিপ্লয়মেন্টের পর একটি ওয়েব অ্যাপ্লিকেশন একটি ব্রাউজারে ঠিকভাবে কাজ করছে, কিন্তু আরেকটিতে ব্যর্থ হচ্ছে। ব্রাউজারের সামঞ্জস্য, ক্যাশে সংরক্ষিত অ্যাসেট, ক্লায়েন্ট-সাইড কোড এবং সার্ভারের আচরণ আলাদা করে যাচাই করার একটি পদ্ধতিগত অনুসন্ধান প্রস্তাব করুন।

### bn_cs

সাম্প্রতিক একটি deployment-এর পর একটি web application একটি browser-এ ঠিকভাবে কাজ করছে, কিন্তু আরেকটিতে fail করছে। browser compatibility, cached asset, client-side code আর server behavior আলাদা করার জন্য একটি systematic investigation propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Clear the cache or use a private window in the failing browser to test cached assets.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Check the browser console for errors and compatibility issues with features used.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Inspect client-side code changes in the deployment for browser-specific behavior.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Compare network requests and server responses between browsers.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Explain how a possible result favors or weakens a named cause.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without result interpretation.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH052

technical_troubleshooting; easy.

### en

A cloud file appears updated on one device but not another. Describe simple synchronization checks before assuming data was lost.

### bn

একটি ক্লাউড ফাইল একটি ডিভাইসে আপডেট হয়েছে দেখাচ্ছে, কিন্তু আরেকটি ডিভাইসে নয়। ডেটা হারিয়ে গেছে ধরে নেওয়ার আগে সিঙ্ক-সংক্রান্ত কোন কোন সহজ চেক করা উচিত তা বর্ণনা করুন।

### bn_cs

একটি cloud file একটি device-এ updated দেখাচ্ছে, কিন্তু আরেকটিতে নয়। data হারিয়ে গেছে ধরে নেওয়ার আগে কোন কোন সহজ synchronization check করা উচিত তা describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check sync status on both devices, such as whether the sync client is running, paused or signed in.
  Rationale: Most common cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check the file in the web version of the cloud service to see the true latest version.
  Rationale: Source of truth.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check for conflict copies or version history.
  Rationale: Recovery evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Check network connectivity and storage space on the lagging device.
  Rationale: Common causes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Do not delete or overwrite copies before confirming the latest version; read-only checks comply.
  Rationale: Avoids real data loss.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH086

technical_troubleshooting; medium.

### en

A shared document shows conflicting edits from two users. Explain what version history and synchronization information should be reviewed before restoring anything.

### bn

একটি শেয়ার করা ডকুমেন্টে দুইজন ব্যবহারকারীর পরস্পরবিরোধী সম্পাদনা দেখা যাচ্ছে। কোনো কিছু পুনরুদ্ধার করার আগে সংস্করণের ইতিহাস ও সিঙ্ক-সংক্রান্ত কোন কোন তথ্য পর্যালোচনা করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি shared document-এ দুইজন user-এর conflicting edit দেখা যাচ্ছে। কোনো কিছু restore করার আগে version history আর synchronization-এর কোন কোন তথ্য review করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Review version history to identify each user's edits and when they were made.
  Rationale: Core evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Check sync status or offline editing that could explain the conflict.
  Rationale: Cause evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check for conflict copies created by the sync system.
  Rationale: Evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Confirm with both users which changes are needed before restoring, so neither user's work is lost.
  Rationale: Avoids losing work.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Do not restore an old version that discards edits without saving a copy of the current version; saving a copy first complies.
  Rationale: Safeguard.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P10 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
