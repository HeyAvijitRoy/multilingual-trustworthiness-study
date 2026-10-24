# P14 independent review packet

Status: pending. AI-produced draft annotations; no human acceptance is claimed.

Each task needs bilingual equivalence and full-prompt coverage review. Review all critical units, all ambiguity/boundary questions below, and every prespecified ordinary sample item. Additional ordinary units may be reviewed. Blank identity/decision fields are intentional.

24 tasks; 109 RIUs; 47 critical; 20 ordinary sample units; 67 mandatory unit reviews.

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

## CYBER036

cybersecurity_digital_safety; medium.

### en

A company is considering exposing an internal service directly to the internet for convenience. Explain the main risks and safer design alternatives.

### bn

সুবিধার কথা ভেবে একটি প্রতিষ্ঠান একটি অভ্যন্তরীণ সার্ভিস সরাসরি ইন্টারনেটে উন্মুক্ত করার কথা বিবেচনা করছে। প্রধান ঝুঁকিগুলো এবং আরও নিরাপদ ডিজাইনের বিকল্পগুলো ব্যাখ্যা করুন।

### bn_cs

convenience-এর কথা ভেবে একটি company একটি internal service সরাসরি internet-এ expose করার কথা ভাবছে। প্রধান risk-গুলো আর আরও safe design alternative-গুলো explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that the service becomes reachable by attackers worldwide, exposing vulnerabilities and weak authentication to scanning and exploitation.
  Rationale: Core risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Propose access through a VPN, zero-trust access proxy or bastion instead of direct exposure.
  Rationale: Safer design.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): If exposure is needed, add strong authentication, a WAF or reverse proxy, patching and monitoring.
  Rationale: Conditional safeguards.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Note that internal services were often not designed for internet exposure.
  Rationale: Context.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER047

cybersecurity_digital_safety; medium.

### en

A department wants to copy production customer data into a test environment. Explain the risks and safer alternatives.

### bn

একটি বিভাগ প্রোডাকশনের গ্রাহক-ডেটা একটি টেস্ট এনভায়রনমেন্টে কপি করতে চায়। এর ঝুঁকিগুলো এবং আরও নিরাপদ বিকল্পগুলো ব্যাখ্যা করুন।

### bn_cs

একটি department production customer data একটি test environment-এ copy করতে চায়। এর risk-গুলো আর আরও safe alternative-গুলো explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that test environments often have weaker access controls and monitoring, increasing exposure of customer data.
  Rationale: Core risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Mention legal or privacy obligations around using customer data for testing.
  Rationale: Compliance.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Recommend synthetic data or masked or anonymized data instead of real customer data.
  Rationale: Safer alternative.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): If real data is unavoidable, minimize it, restrict access and delete it after use.
  Rationale: Conditional safeguards.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER072

cybersecurity_digital_safety; easy.

### en

A web application displays detailed error messages to users. Explain why this can be a security concern and what a safer error-handling approach should do.

### bn

একটি ওয়েব অ্যাপ্লিকেশন ব্যবহারকারীদের বিস্তারিত এরর মেসেজ দেখায়। এটি কেন নিরাপত্তার জন্য উদ্বেগের বিষয় হতে পারে এবং আরও নিরাপদ এরর হ্যান্ডলিং পদ্ধতির কী করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি web application user-দের detailed error message দেখায়। এটা কেন security concern হতে পারে এবং আরও safe error-handling approach-এর কী করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that detailed errors can reveal internal information such as stack traces, queries, paths or versions that help attackers.
  Rationale: Core concern.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Show users a generic message while logging full details server-side.
  Rationale: Safer approach.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Include a reference ID so support can match the user's report to logs.
  Rationale: Usability.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Disable debug output in production.
  Rationale: Configuration.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER079

cybersecurity_digital_safety; hard.

### en

An organization wants to improve software supply-chain security across dozens of development teams. Propose a phased program covering dependencies, build integrity, secrets, signing, review, and monitoring.

### bn

একটি প্রতিষ্ঠান কয়েক ডজন ডেভেলপমেন্ট টিম জুড়ে সফটওয়্যার সাপ্লাই-চেইনের নিরাপত্তা উন্নত করতে চায়। ডিপেন্ডেন্সি, বিল্ডের অখণ্ডতা, সিক্রেট, সাইনিং, রিভিউ এবং মনিটরিং অন্তর্ভুক্ত করে ধাপে ধাপে বাস্তবায়নযোগ্য একটি কর্মসূচি প্রস্তাব করুন।

### bn_cs

একটি প্রতিষ্ঠান কয়েক ডজন development team জুড়ে software supply-chain security উন্নত করতে চায়। dependency, build integrity, secret, signing, review আর monitoring নিয়ে ধাপে ধাপে বাস্তবায়নযোগ্য একটি program propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Inventory and scan dependencies, such as an SBOM and vulnerability scanning.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Protect build integrity, such as isolated, reproducible builds with restricted pipeline access.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Remove secrets from code and use a secrets manager with scanning.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Sign artifacts and verify signatures before deployment.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Require code review, including for dependency changes.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Monitor for new vulnerabilities and anomalies in builds and dependencies.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (critical; all-critical): Phase the program, such as starting with high-risk teams or quick wins, then expanding with standards and tooling.
  Rationale: The prompt asks for a phased program.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists elements without phasing or sequencing.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC026

decision_support; medium.

### en

A researcher can analyze a dataset using a spreadsheet, Python, or a BI tool. Explain how dataset size, reproducibility, collaboration, visualization, and skill level should influence the choice.

### bn

একজন গবেষক একটি ডেটাসেট স্প্রেডশিট, পাইথন অথবা একটি বিআই টুল দিয়ে বিশ্লেষণ করতে পারেন। ডেটাসেটের আকার, পুনরুৎপাদনযোগ্যতা, একসঙ্গে কাজ করার সুবিধা, ভিজ্যুয়ালাইজেশন এবং দক্ষতার স্তর কীভাবে এই বাছাইকে প্রভাবিত করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একজন researcher একটি dataset spreadsheet, Python অথবা একটি BI tool দিয়ে analyze করতে পারেন। dataset-এর size, reproducibility, collaboration, visualization আর skill level কীভাবে এই choice-কে influence করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Explain that large datasets favor Python or BI tools over spreadsheets.
  Rationale: Named factor with direction.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Explain that scripted analysis in Python supports reproducibility better than manual spreadsheet steps.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Consider collaboration needs, such as shared dashboards in BI tools or shared code.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Consider visualization needs, such as interactive dashboards in BI tools.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Consider the researcher's skill level.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Combine factors into a recommendation rule for the situation.
  Rationale: The decision.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Discusses factors without combining them.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC073

decision_support; easy.

### en

A coworker misunderstood a short written message and the issue is becoming confusing. Explain when switching to a live conversation may be better.

### bn

একজন সহকর্মী ছোট একটি লিখিত বার্তা ভুল বুঝেছেন, এবং বিষয়টি ক্রমেই জট পাকিয়ে যাচ্ছে। কখন সরাসরি কথোপকথনে চলে যাওয়া ভালো হতে পারে তা ব্যাখ্যা করুন।

### bn_cs

একজন coworker ছোট একটি written message ভুল বুঝেছেন, এবং বিষয়টা ক্রমেই confusing হয়ে যাচ্ছে। কখন live conversation-এ switch করা ভালো হতে পারে তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Switch when back-and-forth messages are increasing confusion or not resolving the misunderstanding.
  Rationale: Core trigger.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Switch when tone or emotions may be misread.
  Rationale: Trigger.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Switch when the issue is complex or urgent.
  Rationale: Trigger.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Follow up in writing with the agreed outcome.
  Rationale: Record.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC075

decision_support; medium.

### en

A project has many stakeholders who need different levels of detail. Propose a communication approach that avoids sending everyone the same long update.

### bn

একটি প্রজেক্টের অনেক অংশীজন আছেন, যাঁদের ভিন্ন ভিন্ন মাত্রার বিস্তারিত তথ্য দরকার। সবাইকে একই দীর্ঘ আপডেট না পাঠিয়ে যোগাযোগের একটি পদ্ধতি প্রস্তাব করুন।

### bn_cs

একটি project-এর অনেক stakeholder আছেন, যাঁদের আলাদা আলাদা level-এর detail দরকার। সবাইকে একই লম্বা update না পাঠিয়ে communication-এর একটি approach propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Group stakeholders by information need, such as executives, team members and partners.
  Rationale: Segmentation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Tailor content and frequency to each group, such as a short summary for executives and details for the team.
  Rationale: Tailoring.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Keep a shared detailed source that anyone can consult.
  Rationale: Single source.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Keep core facts consistent across versions.
  Rationale: Consistency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC079

decision_support; hard.

### en

A team discovers that an earlier report contained an important error that affected decisions. Explain how to decide what to correct, whom to notify, how much context to provide, and how to prevent quiet replacement of the record.

### bn

একটি টিম জানতে পেরেছে যে আগের একটি রিপোর্টে একটি গুরুত্বপূর্ণ ভুল ছিল, যা বিভিন্ন সিদ্ধান্তে প্রভাব ফেলেছে। কী সংশোধন করবেন, কাকে জানাবেন, কতটা প্রেক্ষাপট দেবেন এবং কীভাবে রেকর্ডটি নিঃশব্দে বদলে ফেলা ঠেকাবেন—তা কীভাবে ঠিক করবেন ব্যাখ্যা করুন।

### bn_cs

একটি team জানতে পেরেছে যে আগের একটি report-এ একটি গুরুত্বপূর্ণ error ছিল, যেটা বিভিন্ন decision-এ প্রভাব ফেলেছে। কী correct করবেন, কাকে notify করবেন, কতটা context দেবেন এবং কীভাবে record-টা নিঃশব্দে replace করা ঠেকাবেন—সেটা কীভাবে decide করবেন explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify the error and every affected figure or conclusion to correct.
  Rationale: What to correct.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Notify the people who received the report or made decisions based on it.
  Rationale: Whom to notify.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Explain what changed, why and the possible impact on decisions, in proportion to the error.
  Rationale: Context.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Do not silently replace the report; keep a visible correction notice or version history.
  Rationale: Explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Address how to prevent similar errors.
  Rationale: Prevention.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC086

decision_support; medium.

### en

A team wants to allow exceptions to a standard process for urgent cases. Explain how to design exception criteria without making the standard meaningless.

### bn

একটি টিম জরুরি ক্ষেত্রে প্রচলিত প্রক্রিয়ার ব্যতিক্রমের সুযোগ রাখতে চায়। মূল নিয়মটিকে অর্থহীন না করে ব্যতিক্রমের মানদণ্ড কীভাবে তৈরি করবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি team urgent case-এ standard process-এর exception-এর সুযোগ রাখতে চায়। standard-টাকে অর্থহীন না করে exception criteria কীভাবে design করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Define specific, objective criteria for what counts as urgent.
  Rationale: Prevents abuse.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Require approval or documentation for each exception.
  Rationale: Control.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Keep essential safeguards that still apply in exceptions.
  Rationale: Preserves the standard.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Review exception frequency and adjust the standard if exceptions become routine.
  Rationale: Feedback.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC025

procedural_instructional; medium.

### en

Explain how to turn broad research notes into a structured outline before writing the first full draft.

### bn

প্রথম পূর্ণাঙ্গ খসড়া লেখার আগে বিস্তৃত গবেষণা-নোটকে কীভাবে একটি কাঠামোবদ্ধ রূপরেখায় রূপ দেওয়া যায় তা ব্যাখ্যা করুন।

### bn_cs

প্রথম full draft লেখার আগে broad research note-কে কীভাবে একটি structured outline-এ রূপ দেওয়া যায় তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Define the paper's main argument or research question.
  Rationale: Organizing principle.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Group notes into themes or sections that support the argument.
  Rationale: Structuring.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Order sections logically and identify gaps.
  Rationale: Outline.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Link notes and sources to each section.
  Rationale: Traceability.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC036

procedural_instructional; medium.

### en

A family shares one calendar but frequently misses appointments. Propose a procedure for entering, confirming, and reminding people about events.

### bn

একটি পরিবার একটিমাত্র যৌথ ক্যালেন্ডার ব্যবহার করে, কিন্তু প্রায়ই অ্যাপয়েন্টমেন্ট মিস করে। ইভেন্ট যোগ করা, নিশ্চিত করা এবং সবাইকে মনে করিয়ে দেওয়ার একটি পদ্ধতি প্রস্তাব করুন।

### bn_cs

একটি পরিবার একটিমাত্র shared calendar ব্যবহার করে, কিন্তু প্রায়ই appointment miss করে। event add করা, confirm করা আর সবাইকে reminder দেওয়ার একটি procedure propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Enter every event promptly with who, when and where.
  Rationale: Entering.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Assign responsibility and confirm attendance for each event.
  Rationale: Confirming.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Set reminders for the people involved.
  Rationale: Reminding.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Review the week ahead together regularly.
  Rationale: Prevents misses.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC053

procedural_instructional; easy.

### en

Explain how to cancel or reschedule an appointment without creating confusion.

### bn

কোনো বিভ্রান্তি তৈরি না করে কীভাবে একটি অ্যাপয়েন্টমেন্ট বাতিল বা নতুন সময়ে সরিয়ে নেবেন তা ব্যাখ্যা করুন।

### bn_cs

কোনো confusion তৈরি না করে কীভাবে একটি appointment cancel বা reschedule করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Contact the provider through the official channel as early as possible.
  Rationale: Core step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Get a confirmation of the cancellation or the new time in writing.
  Rationale: Avoids confusion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Update your own calendar and remove the old time.
  Rationale: Consistency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check cancellation policies or fees.
  Rationale: Avoids surprises.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC059

procedural_instructional; hard.

### en

A customer has repeatedly received different answers from a service organization. Propose a procedure for escalating the issue while keeping communication factual and traceable.

### bn

একজন গ্রাহক একটি সেবা প্রতিষ্ঠান থেকে বারবার ভিন্ন ভিন্ন উত্তর পেয়েছেন। যোগাযোগ তথ্যনির্ভর ও পরে খুঁজে দেখার উপযোগী রেখে বিষয়টি ঊর্ধ্বতন পর্যায়ে নেওয়ার একটি পদ্ধতি প্রস্তাব করুন।

### bn_cs

একজন customer একটি service organization থেকে বারবার আলাদা আলাদা answer পেয়েছেন। communication factual আর traceable রেখে issue-টা escalate করার একটি procedure propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Keep a log of each contact: date, person, channel and answer, with reference numbers.
  Rationale: Traceability.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Summarize the conflicting answers factually and request a single written resolution.
  Rationale: Factual escalation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Escalate to a supervisor or formal complaint channel if unresolved.
  Rationale: Escalation path.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Use written channels where possible and keep copies.
  Rationale: Traceability.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC088

procedural_instructional; medium.

### en

A department wants to automate a repetitive data-transfer process currently performed manually each week. Design a safe transition procedure with validation, rollback, ownership, logging, and exception handling.

### bn

একটি বিভাগ প্রতি সপ্তাহে হাতে করা একটি পুনরাবৃত্ত ডেটা-স্থানান্তরের কাজ অটোমেট করতে চায়। যাচাই, রোলব্যাক, দায়িত্বের মালিকানা, লগিং এবং ব্যতিক্রম সামলানোসহ নিরাপদভাবে এই রূপান্তরের একটি পদ্ধতি তৈরি করুন।

### bn_cs

একটি department প্রতি সপ্তাহে হাতে করা একটি পুনরাবৃত্ত data-transfer-এর কাজ automate করতে চায়। validation, rollback, ownership, logging আর exception handling-সহ নিরাপদভাবে এই পরিবর্তনের একটি procedure তৈরি করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Validate automated output against the manual process, such as running both in parallel.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Keep the manual process available as rollback until the automation is proven.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Assign an owner for the automation.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Log each run and its results.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Define how exceptions and failures alert someone and are handled.
  Rationale: Named element.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN019

information_synthesis; hard.

### en

Compare these data sources while preserving their limitations: Source A is updated daily but covers only registered users. Source B covers the whole population but is updated quarterly. Source C is a survey updated monthly with a 55 percent response rate.

### bn

সীমাবদ্ধতাগুলো বজায় রেখে এই ডেটা উৎসগুলো তুলনা করুন: উৎস A প্রতিদিন আপডেট হয়, কিন্তু শুধু নিবন্ধিত ব্যবহারকারীদের তথ্য রাখে। উৎস B পুরো জনগোষ্ঠীকে অন্তর্ভুক্ত করে, কিন্তু প্রতি তিন মাসে একবার আপডেট হয়। উৎস C একটি জরিপ, যা প্রতি মাসে আপডেট হয় এবং এর সাড়া দেওয়ার হার ৫৫ শতাংশ।

### bn_cs

limitation-গুলো বজায় রেখে এই data source-গুলো compare করুন: Source A প্রতিদিন update হয়, কিন্তু শুধু registered user-দের cover করে। Source B পুরো population cover করে, কিন্তু quarterly update হয়। Source C একটি survey, যেটা monthly update হয় এবং এর response rate ৫৫ শতাংশ।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that Source A is daily but covers only registered users.
  Rationale: Facts and limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that Source B covers the whole population but is updated only quarterly.
  Rationale: Facts and limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that Source C is a monthly survey with a 55 percent response rate, which may introduce nonresponse bias.
  Rationale: Facts and limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Explain trade-offs between timeliness and coverage across sources.
  Rationale: Comparison.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN044

information_synthesis; medium.

### en

Extract action items, owners, and dependencies: Jordan will clean the data. After cleaning, Mei will run the analysis. Once results are ready, Omar will prepare the chart. The team will review everything Friday.

### bn

করণীয়, দায়িত্বপ্রাপ্ত ব্যক্তি এবং পারস্পরিক নির্ভরতাগুলো বের করুন: জর্ডান ডেটা পরিষ্কার করবেন। পরিষ্কার শেষ হলে মেই বিশ্লেষণ চালাবেন। ফলাফল তৈরি হলে ওমর চার্ট তৈরি করবেন। শুক্রবার টিম সবকিছু পর্যালোচনা করবে।

### bn_cs

action item, owner আর dependency-গুলো extract করুন: জর্ডান data clean করবেন। cleaning শেষ হলে মেই analysis run করবেন। result ready হলে ওমর chart তৈরি করবেন। শুক্রবার team সবকিছু review করবে।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that Jordan cleans the data.
  Rationale: Action and owner.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that Mei runs the analysis after cleaning.
  Rationale: Action, owner and dependency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that Omar prepares the chart once results are ready.
  Rationale: Action, owner and dependency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): State that the team reviews everything on Friday.
  Rationale: Action and owner.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN052

information_synthesis; easy.

### en

Two sources report different room numbers for the same event. Source A says Room 204. Source B says Room 240. Both agree the event starts at 11 AM. Summarize the agreement and conflict.

### bn

একই অনুষ্ঠানের জন্য দুটি উৎস ভিন্ন কক্ষ নম্বর দিচ্ছে। উৎস A বলছে কক্ষ ২০৪। উৎস B বলছে কক্ষ ২৪০। দুটি উৎসই একমত যে অনুষ্ঠান সকাল ১১টায় শুরু হবে। কোথায় মিল আর কোথায় বিরোধ তা সংক্ষেপ করুন।

### bn_cs

একই event-এর জন্য দুটি source আলাদা room number দিচ্ছে। Source A বলছে Room ২০৪। Source B বলছে Room ২৪০। দুটি source-ই একমত যে event সকাল ১১টায় শুরু হবে। agreement আর conflict summarize করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State the agreement: the event starts at 11 AM.
  Rationale: Agreement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State the conflict: Source A says Room 204 and Source B says Room 240.
  Rationale: Conflict.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Do not decide which room is correct; suggest confirming with the organizer.
  Rationale: Avoids unsupported resolution.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN064

information_synthesis; medium.

### en

A survey finds that 70 percent of respondents prefer Option A, but only 35 percent of invited people responded. Explain what can be reported confidently and what limitation should accompany the result.

### bn

একটি জরিপে দেখা গেছে, উত্তরদাতাদের ৭০ শতাংশ বিকল্প A পছন্দ করেন, কিন্তু আমন্ত্রিতদের মাত্র ৩৫ শতাংশ উত্তর দিয়েছেন। কোন বিষয়টি আত্মবিশ্বাসের সঙ্গে জানানো যায় এবং ফলাফলের সঙ্গে কোন সীমাবদ্ধতা উল্লেখ করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি survey-তে দেখা গেছে, respondent-দের ৭০ শতাংশ Option A prefer করেন, কিন্তু invited মানুষদের মাত্র ৩৫ শতাংশ respond করেছেন। কোন বিষয়টা confidently report করা যায় এবং result-এর সঙ্গে কোন limitation উল্লেখ করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that 70 percent of respondents preferred Option A can be reported confidently.
  Rationale: Supported claim.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that the 35 percent response rate means respondents may not represent all invited people, so the result may not reflect the whole group.
  Rationale: Limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Note that the preference among all invitees could be higher or lower.
  Rationale: Calibration.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Suggest checking respondent characteristics or following up with nonrespondents.
  Rationale: Next step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN076

information_synthesis; medium.

### en

A dataset must contain at least 1,000 records, have under 5 percent missing values, and include both 2025 and 2026 data. Dataset X has 1,200 records, 3 percent missing, but only 2025. Dataset Y has 950 records, 2 percent missing, and both years. Explain whether either qualifies.

### bn

একটি ডেটাসেটে অন্তত ১,০০০টি রেকর্ড থাকতে হবে, অনুপস্থিত মান ৫ শতাংশের কম হতে হবে, এবং ২০২৫ ও ২০২৬—দুই বছরেরই ডেটা থাকতে হবে। ডেটাসেট X-এ ১,২০০টি রেকর্ড আছে, অনুপস্থিত মান ৩ শতাংশ, কিন্তু শুধু ২০২৫ সালের ডেটা আছে। ডেটাসেট Y-এ ৯৫০টি রেকর্ড আছে, অনুপস্থিত মান ২ শতাংশ, এবং দুই বছরের ডেটাই আছে। কোনোটি যোগ্য কি না ব্যাখ্যা করুন।

### bn_cs

একটি dataset-এ অন্তত ১,০০০টি record থাকতে হবে, missing value ৫ শতাংশের কম হতে হবে, এবং ২০২৫ আর ২০২৬—দুই বছরেরই data থাকতে হবে। Dataset X-এ ১,২০০টি record আছে, missing value ৩ শতাংশ, কিন্তু শুধু ২০২৫ সালের data আছে। Dataset Y-এ ৯৫০টি record আছে, missing value ২ শতাংশ, এবং দুই বছরের data-ই আছে। কোনোটা qualify করে কি না explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that Dataset X fails because it lacks 2026 data, though it meets size and missingness.
  Rationale: Check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that Dataset Y fails because it has only 950 records, though it meets missingness and year coverage.
  Rationale: Check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Conclude that neither dataset qualifies.
  Rationale: Answer.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Suggest options such as combining or adding records, if done appropriately.
  Rationale: Useful.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH035

technical_troubleshooting; medium.

### en

Two reports that should use the same database show different totals. Describe a structured way to check filters, joins, time ranges, duplicates, and refresh timing.

### bn

একই ডেটাবেস ব্যবহার করার কথা এমন দুটি রিপোর্টে মোট সংখ্যা ভিন্ন আসছে। ফিল্টার, জয়েন, সময়ের পরিসর, ডুপ্লিকেট এবং রিফ্রেশের সময় যাচাই করার একটি কাঠামোবদ্ধ উপায় বর্ণনা করুন।

### bn_cs

একই database ব্যবহার করার কথা এমন দুটি report-এ total ভিন্ন আসছে। filter, join, time range, duplicate আর refresh timing check করার একটি গোছানো উপায় describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Compare filters in both reports.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Compare joins that may duplicate or drop rows.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Compare time ranges and time zones.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check for duplicates.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Check refresh timing of each report.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Reconcile step by step, such as on a small slice, to explain which difference causes the gap.
  Rationale: Structured diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without a reconciliation approach.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH040

technical_troubleshooting; hard.

### en

A read replica shows stale data longer than expected even though replication is enabled. Propose a troubleshooting plan covering replication lag, network delay, workload, configuration, and application read routing.

### bn

রেপ্লিকেশন চালু থাকা সত্ত্বেও একটি রিড রেপ্লিকায় প্রত্যাশার চেয়ে বেশি সময় ধরে পুরোনো ডেটা দেখা যাচ্ছে। রেপ্লিকেশন ল্যাগ, নেটওয়ার্ক বিলম্ব, কাজের চাপ, কনফিগারেশন এবং অ্যাপ্লিকেশনের রিড রাউটিং অন্তর্ভুক্ত করে সমস্যা সমাধানের একটি পরিকল্পনা প্রস্তাব করুন।

### bn_cs

replication চালু থাকা সত্ত্বেও একটি read replica-তে প্রত্যাশার চেয়ে বেশি সময় ধরে stale data দেখা যাচ্ছে। replication lag, network delay, workload, configuration আর application read routing cover করে সমস্যা সমাধানের একটি plan propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Measure replication lag metrics.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check network delay between primary and replica.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check replica workload, such as heavy queries slowing replay.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Check replication configuration.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Check whether the app routes reads that need fresh data to the replica, or caches results.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Explain how a possible result points to a specific cause.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without interpretation.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH042

technical_troubleshooting; easy.

### en

A web developer changes CSS but sees no visual difference in the browser. Describe the simplest troubleshooting sequence.

### bn

একজন ওয়েব ডেভেলপার সিএসএস পরিবর্তন করেছেন, কিন্তু ব্রাউজারে দৃশ্যমান কোনো পার্থক্য দেখছেন না। সমস্যা সমাধানের সবচেয়ে সহজ ধাপক্রমটি বর্ণনা করুন।

### bn_cs

একজন web developer CSS change করেছেন, কিন্তু browser-এ কোনো দৃশ্যমান পার্থক্য দেখছেন না। সবচেয়ে সহজ troubleshooting sequence-টা describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Hard refresh or clear the browser cache.
  Rationale: Most common cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Check the file was saved and the page loads the edited stylesheet, such as in the network tab.
  Rationale: Common cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check in developer tools whether the rule is applied or overridden by specificity.
  Rationale: Common cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check for build steps or deployment that must run.
  Rationale: Common cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH065

technical_troubleshooting; medium.

### en

A laptop fan runs loudly almost all the time even when the user is doing light work. Describe how to separate normal cooling behavior from a hardware or software problem.

### bn

ব্যবহারকারী হালকা কাজ করলেও একটি ল্যাপটপের ফ্যান প্রায় সারাক্ষণ জোরে চলছে। স্বাভাবিক কুলিং আচরণ আর হার্ডওয়্যার বা সফটওয়্যারের সমস্যার মধ্যে কীভাবে পার্থক্য করবেন তা বর্ণনা করুন।

### bn_cs

user হালকা কাজ করলেও একটি laptop-এর fan প্রায় সারাক্ষণ জোরে চলছে। স্বাভাবিক cooling behavior আর hardware বা software problem-এর মধ্যে কীভাবে পার্থক্য করবেন তা describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check CPU usage and background processes for software load.
  Rationale: Software cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check temperatures to see whether they are actually high.
  Rationale: Evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check for dust or blocked vents, and whether the laptop is on a soft surface.
  Rationale: Hardware cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Check power and fan settings or firmware updates.
  Rationale: Settings cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Explain how a possible result points to normal behavior, software or hardware.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without interpretation.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH095

technical_troubleshooting; medium.

### en

An external monitor works at a lower resolution but becomes unstable at its native resolution. Explain what cable, port, adapter, graphics, and refresh-rate factors should be checked.

### bn

একটি এক্সটার্নাল মনিটর কম রেজোলিউশনে ঠিকঠাক চলে, কিন্তু এর নেটিভ রেজোলিউশনে অস্থিতিশীল হয়ে যায়। ক্যাবল, পোর্ট, অ্যাডাপ্টার, গ্রাফিক্স এবং রিফ্রেশ রেট-সংক্রান্ত কোন কোন বিষয় চেক করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি external monitor কম resolution-এ ঠিকঠাক চলে, কিন্তু native resolution-এ unstable হয়ে যায়। cable, port, adapter, graphics আর refresh rate-এর কোন কোন বিষয় check করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Check that the cable supports the bandwidth needed, such as the right HDMI or DisplayPort version.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check the port supports the resolution and refresh rate.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check adapters or docks that may limit bandwidth.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Check graphics drivers and capabilities.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Try a lower refresh rate at native resolution.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Explain how a possible result points to a specific factor.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without interpretation.

Draft notes: P14 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
