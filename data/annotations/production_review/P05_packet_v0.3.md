# P05 independent review packet

Status: pending. AI-produced draft annotations; no human acceptance is claimed.

Each task needs bilingual equivalence and full-prompt coverage review. Review all critical units, all ambiguity/boundary questions below, and every prespecified ordinary sample item. Additional ordinary units may be reviewed. Blank identity/decision fields are intentional.

25 tasks; 133 RIUs; 59 critical; 21 ordinary sample units; 82 mandatory unit reviews.

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

## CYBER008

cybersecurity_digital_safety; medium.

### en

An organization observes successful logins for one user from geographically distant locations within a short period. Explain how to investigate the event while accounting for VPNs, mobile networks, shared systems, and stolen credentials.

### bn

একটি প্রতিষ্ঠান দেখছে, অল্প সময়ের ব্যবধানে একই ব্যবহারকারীর অ্যাকাউন্টে ভৌগোলিকভাবে অনেক দূরের লোকেশন থেকে সফল লগইন হয়েছে। ভিপিএন, মোবাইল নেটওয়ার্ক, শেয়ার করা সিস্টেম এবং চুরি হওয়া ক্রেডেনশিয়াল বিবেচনায় রেখে ঘটনাটি কীভাবে তদন্ত করবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি প্রতিষ্ঠান দেখছে, অল্প সময়ের ব্যবধানে একই user-এর account-এ ভৌগোলিকভাবে অনেক দূরের location থেকে successful login হয়েছে। VPN, mobile network, shared system আর stolen credential বিবেচনায় রেখে ঘটনাটা কীভাবে investigate করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-07: Conditional safeguard: confirm containment applies only when compromise cannot be excluded.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Check whether one location reflects a VPN or proxy egress point, using IP ownership or the organization's VPN records.
  Rationale: A named benign explanation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Consider mobile-network IP geolocation inaccuracy as a cause of apparent distance.
  Rationale: A named benign explanation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check whether a shared or service system, such as a jump host or shared kiosk, could produce logins under the user's account.
  Rationale: A named benign explanation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Look for stolen-credential indicators, such as a new device, unusual user agent, MFA anomalies or unusual post-login activity.
  Rationale: The malicious explanation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Contact the user through a trusted channel to confirm their location and activity.
  Rationale: Direct evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Explain how a possible result favors or weakens stolen credentials relative to a benign explanation.
  Rationale: Without interpretation the answer lists possibilities but does not investigate.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists explanations but gives no result-to-hypothesis interpretation.
- [ ] **RIU-07** (critical; all-critical, identified-ambiguity-or-boundary): If compromise cannot be ruled out, contain the account, such as by revoking sessions and resetting credentials.
  Rationale: Prevents ongoing misuse while investigating.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Follows the accepted differential-diagnosis convention, plus a critical containment unit because of security risk. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER027

cybersecurity_digital_safety; medium.

### en

A workstation has not received operating-system security updates for several months. Propose a safe remediation plan that considers compatibility, backups, testing, and urgency.

### bn

একটি ওয়ার্কস্টেশনে কয়েক মাস ধরে অপারেটিং সিস্টেমের কোনো সিকিউরিটি আপডেট আসেনি। সামঞ্জস্য, ব্যাকআপ, টেস্টিং এবং জরুরিতা বিবেচনা করে একটি নিরাপদ সমাধান-পরিকল্পনা প্রস্তাব করুন।

### bn_cs

একটি workstation-এ কয়েক মাস ধরে operating-system-এর কোনো security update আসেনি। compatibility, backup, testing আর urgency বিবেচনা করে একটি safe remediation plan propose করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-04: Check that urgency-versus-testing reconciliation is accepted under either unit.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Assess urgency by identifying critical or actively exploited vulnerabilities among the missing updates.
  Rationale: Determines how fast to act.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Back up important data or create a restore point before applying updates.
  Rationale: A named safeguard.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Check compatibility of business applications or drivers with the updates.
  Rationale: A named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Test updates first where feasible, such as on a similar machine, or apply in stages.
  Rationale: A named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Find and fix why updates stopped, such as broken update service or policy.
  Rationale: Prevents recurrence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Reduce exposure until patched for urgent cases, such as limiting network access.
  Rationale: Interim protection.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Urgency may justify patching before full testing; the answer should reconcile them. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER084

cybersecurity_digital_safety; medium.

### en

A company wants to record all employee activity for security monitoring. Explain how privacy, proportionality, transparency, and security objectives should be balanced.

### bn

একটি প্রতিষ্ঠান সিকিউরিটি মনিটরিংয়ের জন্য কর্মীদের সব কার্যকলাপ রেকর্ড করতে চায়। প্রাইভেসি, আনুপাতিকতা, স্বচ্ছতা এবং নিরাপত্তার লক্ষ্যের মধ্যে কীভাবে ভারসাম্য রাখা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি company security monitoring-এর জন্য employee-দের সব activity record করতে চায়। privacy, proportionality, transparency আর security objective-এর মধ্যে কীভাবে balance রাখা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Define the specific security objectives the monitoring is meant to address.
  Rationale: Proportionality depends on a defined purpose.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Apply proportionality: collect only the monitoring needed for those objectives, rather than all activity by default.
  Rationale: The core balancing principle.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Be transparent with employees about what is monitored, why and how data is used.
  Rationale: A named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Protect and limit the monitoring data, such as access control and retention limits.
  Rationale: The data itself creates risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Consider legal requirements or consultation with legal, privacy or employee representatives.
  Rationale: Monitoring may be regulated.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. No jurisdiction-specific law is required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER092

cybersecurity_digital_safety; easy.

### en

An employee is afraid to report a security mistake because they may be blamed. Explain why a healthy reporting culture matters for security.

### bn

দোষ চাপানো হতে পারে—এই ভয়ে একজন কর্মী নিজের করা একটি নিরাপত্তা-সংক্রান্ত ভুল জানাতে ভয় পাচ্ছেন। নিরাপত্তার জন্য একটি সুস্থ রিপোর্টিং সংস্কৃতি কেন গুরুত্বপূর্ণ তা ব্যাখ্যা করুন।

### bn_cs

blame করা হতে পারে—এই ভয়ে একজন employee নিজের করা একটি security mistake report করতে ভয় পাচ্ছেন। security-র জন্য একটি healthy reporting culture কেন গুরুত্বপূর্ণ তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that fear of blame leads people to hide or delay reporting mistakes.
  Rationale: The core mechanism in the scenario.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Explain that prompt reporting lets the security team contain incidents early and limit damage.
  Rationale: The security benefit.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Explain that reports reveal process or system weaknesses so the organization can fix root causes.
  Rationale: Learning benefit.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Distinguish honest mistakes from deliberate misconduct, so a non-blame culture does not mean no accountability.
  Rationale: Avoids an overbroad claim.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Specific programs such as amnesty policies are optional examples. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER099

cybersecurity_digital_safety; hard.

### en

A company measures security training success only by quiz scores. Explain why this may be insufficient and propose behavioral and operational measures that better reflect real risk reduction.

### bn

একটি প্রতিষ্ঠান শুধু কুইজের স্কোর দিয়েই নিরাপত্তা প্রশিক্ষণের সাফল্য মাপে। এটি কেন যথেষ্ট না-ও হতে পারে তা ব্যাখ্যা করুন এবং বাস্তবে ঝুঁকি কতটা কমছে তা আরও ভালোভাবে প্রতিফলিত করে এমন আচরণগত ও কার্যক্রম-সংক্রান্ত পরিমাপ প্রস্তাব করুন।

### bn_cs

একটি company শুধু quiz score দিয়েই security training-এর success মাপে। এটা কেন যথেষ্ট না-ও হতে পারে তা explain করুন এবং বাস্তবে risk কতটা কমছে তা আরও ভালোভাবে reflect করে এমন behavioral আর operational measure propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that quiz scores measure knowledge recall, not whether people behave securely in real situations.
  Rationale: The core limitation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Propose a behavioral measure, such as simulated-phishing click or report rates.
  Rationale: A requested measure type.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Propose an operational measure, such as incident counts, time to report or policy-violation trends.
  Rationale: A requested measure type.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Note that measures should be tracked over time or against a baseline to show risk reduction.
  Rationale: Turns measures into evidence of change.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Caution that measures can be gamed or have confounders, such as simulation difficulty.
  Rationale: Avoids misreading the metrics.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Any concrete behavioral and operational measures are acceptable. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC046

decision_support; medium.

### en

A group trip includes people with different budgets and mobility needs. Explain how lodging choices should be compared fairly.

### bn

একটি দলগত ভ্রমণে বিভিন্ন বাজেট ও চলাফেরার ভিন্ন ভিন্ন প্রয়োজন থাকা মানুষ আছেন। থাকার জায়গার বিকল্পগুলো কীভাবে ন্যায্যভাবে তুলনা করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি group trip-এ আলাদা আলাদা budget আর mobility need থাকা মানুষ আছেন। lodging option-গুলো কীভাবে fairly compare করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Treat mobility needs as requirements: exclude options that are not accessible for members who need it.
  Rationale: Accessibility is not a trade-off item.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Collect each member's budget limits and needs before comparing options.
  Rationale: Fairness requires knowing constraints.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Compare options on total cost per person and fit to everyone's constraints.
  Rationale: The comparison method.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Consider fair cost-sharing or mixed arrangements, such as different room types.
  Rationale: Accommodates budget differences.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Decide transparently with the group.
  Rationale: Fair process.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC053

decision_support; easy.

### en

A small project has time for either additional testing or improved documentation before delivery. Explain what factors should determine the choice.

### bn

একটি ছোট প্রজেক্টে ডেলিভারির আগে হয় বাড়তি টেস্টিং, নয়তো ডকুমেন্টেশন উন্নত করার সময় আছে। কোন কোন বিষয় এই বাছাই ঠিক করে দেওয়া উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি ছোট project-এ delivery-র আগে হয় additional testing, নয়তো documentation improve করার সময় আছে। কোন কোন factor এই choice ঠিক করে দেওয়া উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Consider the risk and impact of remaining defects, such as untested critical paths.
  Rationale: Determines the value of testing.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Consider who will use or maintain the delivery and whether missing documentation blocks them.
  Rationale: Determines the value of documentation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Consider contractual or stakeholder requirements for either.
  Rationale: May decide the choice.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Consider whether a minimal version of the other activity is possible.
  Rationale: Avoids a false binary.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. No single correct choice. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC057

decision_support; medium.

### en

A software project has a feature that users like but that creates recurring maintenance problems. Explain how to decide whether to keep, redesign, or remove it.

### bn

একটি সফটওয়্যার প্রজেক্টের একটি ফিচার ব্যবহারকারীরা পছন্দ করেন, কিন্তু সেটি বারবার রক্ষণাবেক্ষণ-সংক্রান্ত সমস্যা তৈরি করে। ফিচারটি রাখবেন, নতুন করে নকশা করবেন নাকি বাদ দেবেন—তা কীভাবে ঠিক করবেন ব্যাখ্যা করুন।

### bn_cs

একটি software project-এর একটি feature user-রা পছন্দ করেন, কিন্তু সেটা বারবার maintenance problem তৈরি করে। feature-টা রাখবেন, redesign করবেন নাকি remove করবেন—সেটা কীভাবে decide করবেন explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Quantify the user value, such as usage and importance to users.
  Rationale: One side of the decision.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Quantify the maintenance cost and root cause of the recurring problems.
  Rationale: The other side; root cause determines whether redesign can fix it.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Compare the three options, including whether a redesign could keep the value at lower cost.
  Rationale: The prompt names three options.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Consider user communication or migration if the feature is changed or removed.
  Rationale: Manages user impact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC060

decision_support; hard.

### en

A team has evidence that a planned feature may provide little value but leadership already announced it publicly. Explain how to evaluate whether to proceed, modify, delay, or cancel while considering evidence and stakeholder commitments.

### bn

একটি টিমের কাছে প্রমাণ আছে যে পরিকল্পিত একটি ফিচার থেকে খুব সামান্য উপকার আসতে পারে, অথচ নেতৃত্ব ইতিমধ্যে প্রকাশ্যে এটির ঘোষণা দিয়েছে। প্রমাণ এবং অংশীজনদের কাছে দেওয়া প্রতিশ্রুতি বিবেচনা করে এগিয়ে যাওয়া, পরিবর্তন করা, পিছিয়ে দেওয়া নাকি বাতিল করা—কোনটি করবেন তা কীভাবে মূল্যায়ন করবেন ব্যাখ্যা করুন।

### bn_cs

একটি team-এর কাছে evidence আছে যে planned একটি feature থেকে খুব সামান্য value আসতে পারে, অথচ leadership ইতিমধ্যে publicly এটার announcement দিয়েছে। evidence আর stakeholder commitment বিবেচনা করে proceed, modify, delay নাকি cancel—কোনটা করবেন তা কীভাবে evaluate করবেন explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Assess the strength and limits of the evidence that the feature has little value.
  Rationale: The decision depends on evidence quality.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Assess the cost of each path relative to the public commitment, such as reputational or trust impact of changing course.
  Rationale: The stakeholder-commitment side.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Consider all four options, including modifying or delaying, not only proceed or cancel.
  Rationale: The prompt names four options.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Bring the evidence to leadership and decide with them rather than proceeding silently or cancelling unilaterally.
  Rationale: The announcement makes leadership a necessary party.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Plan communication of any change to stakeholders who heard the announcement.
  Rationale: Manages trust.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Sunk cost of the announcement should not by itself decide. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC066

decision_support; medium.

### en

A team must choose between a simple metric everyone understands and a more accurate metric that is harder to explain. Discuss how to make the decision.

### bn

একটি টিমকে এমন একটি সহজ মেট্রিক, যা সবাই বোঝে, আর এমন একটি বেশি নির্ভুল মেট্রিক, যা বোঝানো কঠিন—এর মধ্যে একটি বেছে নিতে হবে। সিদ্ধান্তটি কীভাবে নেওয়া উচিত তা আলোচনা করুন।

### bn_cs

একটি team-কে এমন একটি simple metric, যেটা সবাই বোঝে, আর এমন একটি more accurate metric, যেটা explain করা কঠিন—এর মধ্যে একটি বেছে নিতে হবে। decision-টা কীভাবে নেওয়া উচিত তা discuss করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Consider what decisions the metric will support and how much the accuracy difference would change those decisions.
  Rationale: The core criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Consider the audience and the risk that a misunderstood metric is misused.
  Rationale: The other side of the trade-off.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Consider using both, such as the simple metric for communication and the accurate one for analysis.
  Rationale: A common resolution.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Document the chosen metric's definition and limitations.
  Rationale: Reduces misinterpretation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC044

procedural_instructional; medium.

### en

A traveler has a flight, hotel check-in, and rental pickup on the same day. Build a timeline that includes realistic buffers and confirmation steps.

### bn

একজন যাত্রীর একই দিনে ফ্লাইট, হোটেলে চেক-ইন এবং ভাড়া করা গাড়ি সংগ্রহ করার কাজ আছে। বাস্তবসম্মত বাফার সময় এবং নিশ্চিতকরণের ধাপসহ একটি সময়রেখা তৈরি করুন।

### bn_cs

একজন traveler-এর একই দিনে flight, hotel check-in আর ভাড়া গাড়ি pickup করার কাজ আছে। বাস্তবসম্মত buffer আর confirmation-এর ধাপসহ একটি timeline তৈরি করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Order the events in a feasible sequence, such as flight arrival, rental pickup, then hotel check-in, or justify another order.
  Rationale: The timeline itself.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Include realistic buffers, such as for flight delays, baggage and rental counter queues.
  Rationale: Named requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Confirm each booking in advance, including hotel check-in time and rental pickup hours.
  Rationale: Named requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Plan what to do if the flight is delayed, such as notifying the rental company or hotel.
  Rationale: Contingency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Account for constraints such as hotel check-in start time or rental office closing time.
  Rationale: Feasibility.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Specific clock times are optional. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC056

procedural_instructional; medium.

### en

Explain how to prepare for an appointment that requires several forms, identification documents, and payment information.

### bn

যে অ্যাপয়েন্টমেন্টে কয়েকটি ফরম, পরিচয়পত্র এবং পেমেন্টের তথ্য লাগবে, তার জন্য কীভাবে প্রস্তুতি নেবেন তা ব্যাখ্যা করুন।

### bn_cs

যে appointment-এ কয়েকটি form, identification document আর payment information লাগবে, তার জন্য কীভাবে prepare করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Confirm in advance exactly which forms, IDs and payment methods are required.
  Rationale: Avoids arriving unprepared.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Complete the forms before the appointment.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Gather the original identification documents and check they are valid and unexpired.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Prepare an accepted payment method and amount.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Put everything in one folder and keep copies.
  Rationale: Practical organization.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Copies of sensitive documents should be stored securely; not required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC062

procedural_instructional; easy.

### en

Describe the steps for inviting a small group and collecting attendance confirmations.

### bn

একটি ছোট দলকে আমন্ত্রণ জানানো এবং কে কে আসবেন তার নিশ্চিতকরণ সংগ্রহ করার ধাপগুলো বর্ণনা করুন।

### bn_cs

একটি ছোট group-কে invite করা আর কে কে আসবেন তার confirmation collect করার step-গুলো describe করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Send an invitation with the date, time, place and purpose.
  Rationale: Core invite content.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Ask for a reply by a stated deadline and specify how to reply.
  Rationale: Enables confirmation collection.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Track responses in one list.
  Rationale: Organizes confirmations.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Follow up with people who have not replied before the deadline.
  Rationale: Completes confirmations.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Send a final reminder or details to confirmed attendees.
  Rationale: Closes the loop.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC064

procedural_instructional; medium.

### en

A workshop has limited seats and more interested participants than capacity. Propose a fair registration and waitlist procedure.

### bn

একটি ওয়ার্কশপে আসন সীমিত, কিন্তু আগ্রহী অংশগ্রহণকারী আসনের চেয়ে বেশি। একটি ন্যায্য রেজিস্ট্রেশন ও অপেক্ষমাণ তালিকার পদ্ধতি প্রস্তাব করুন।

### bn_cs

একটি workshop-এ seat সীমিত, কিন্তু আগ্রহী participant capacity-র চেয়ে বেশি। একটি fair registration আর waitlist procedure propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Use a transparent, announced allocation rule, such as first-come with a fixed opening time or a lottery.
  Rationale: Fairness depends on a clear rule.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Create an ordered waitlist and offer released seats in order.
  Rationale: The waitlist procedure.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Require confirmation within a deadline and release unconfirmed seats.
  Rationale: Keeps seats used.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Communicate status clearly to registrants and waitlisted people.
  Rationale: Transparency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Consider measures for equity, such as one registration per person or priority for those who missed previous sessions.
  Rationale: Fairness refinement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC070

procedural_instructional; hard.

### en

An event organizer wants a repeatable post-event closeout process. Design steps for attendance records, expenses, feedback, materials, unresolved issues, and lessons learned.

### bn

একজন অনুষ্ঠান-আয়োজক অনুষ্ঠান শেষে সবকিছু গুছিয়ে বন্ধ করার একটি পুনরাবৃত্তিযোগ্য প্রক্রিয়া চান। উপস্থিতির রেকর্ড, খরচ, মতামত, উপকরণ, অমীমাংসিত বিষয় এবং শিক্ষণীয় দিকগুলোর জন্য ধাপগুলো তৈরি করুন।

### bn_cs

একজন event organizer অনুষ্ঠান শেষে সবকিছু গুছিয়ে বন্ধ করার একটি repeatable process চান। উপস্থিতির record, খরচ, feedback, উপকরণ, অমীমাংসিত issue আর lessons learned-এর জন্য ধাপগুলো design করুন।

### Boundary and ambiguity questions

- [ ] RIU-02, RIU-05: Criticality boundary among named components.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Finalize and store attendance records.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Reconcile expenses against budget and close outstanding payments.
  Rationale: Named component with financial consequences.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Collect and summarize feedback.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Return, store or inventory materials and equipment.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical, identified-ambiguity-or-boundary): List unresolved issues with owners and due dates.
  Rationale: Named component; issues are lost otherwise.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; prespecified-ordinary-sample): Record lessons learned and feed them into the next event's plan or template.
  Rationale: Named component; repeatability.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN001

information_synthesis; easy.

### en

Summarize this situation in two sentences without dropping any key fact: The workshop starts at 10 AM. Registration opens at 9:15 AM. Participants must bring a laptop. Lunch is not provided.

### bn

কোনো মূল তথ্য বাদ না দিয়ে পরিস্থিতিটি দুই বাক্যে সংক্ষেপ করুন: ওয়ার্কশপ সকাল ১০টায় শুরু হবে। রেজিস্ট্রেশন খুলবে সকাল ৯টা ১৫ মিনিটে। অংশগ্রহণকারীদের ল্যাপটপ আনতে হবে। দুপুরের খাবার দেওয়া হবে না।

### bn_cs

কোনো key fact বাদ না দিয়ে situation-টা দুই বাক্যে summarize করুন: workshop সকাল ১০টায় শুরু হবে। registration খুলবে সকাল ৯টা ১৫ মিনিটে। participant-দের laptop আনতে হবে। lunch দেওয়া হবে না।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that the workshop starts at 10 AM.
  Rationale: Key fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that registration opens at 9:15 AM.
  Rationale: Key fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that participants must bring a laptop.
  Rationale: Key fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): State that lunch is not provided.
  Rationale: Key fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
- [ ] CHECK-02: The summary is exactly two sentences.

## SYN015

information_synthesis; medium.

### en

Compare two software options from the facts only: Tool X supports single sign-on and audit logs but lacks offline access. Tool Y supports offline access and costs 25 percent less but does not support single sign-on.

### bn

শুধু দেওয়া তথ্য থেকে দুটি সফটওয়্যার বিকল্প তুলনা করুন: টুল X সিঙ্গেল সাইন-অন ও অডিট লগ সাপোর্ট করে, কিন্তু অফলাইনে ব্যবহারের সুবিধা নেই। টুল Y অফলাইনে ব্যবহার করা যায় এবং এর খরচ ২৫ শতাংশ কম, কিন্তু এটি সিঙ্গেল সাইন-অন সাপোর্ট করে না।

### bn_cs

শুধু দেওয়া fact থেকে দুটি software option compare করুন: Tool X single sign-on আর audit log support করে, কিন্তু offline access নেই। Tool Y offline access দেয় এবং এর খরচ ২৫ শতাংশ কম, কিন্তু এটা single sign-on support করে না।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that Tool X supports single sign-on and audit logs.
  Rationale: Stated fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that Tool X lacks offline access.
  Rationale: Stated fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that Tool Y supports offline access and costs 25 percent less.
  Rationale: Stated facts.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): State that Tool Y does not support single sign-on.
  Rationale: Stated fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Do not add unstated facts, such as Tool Y's audit-log support; a facts-only comparison complies.
  Rationale: The prompt restricts to given facts.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Tool Y's audit-log support is unknown and must not be asserted either way. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN040

information_synthesis; hard.

### en

Organize the following into goals, constraints, and risks: Goal is to launch by November. Budget is fixed at $50,000. Two key staff are unavailable in October. A required vendor integration has not been tested. The launch date may move only with executive approval.

### bn

নিচের তথ্যগুলোকে লক্ষ্য, শর্ত এবং ঝুঁকিতে সাজান: লক্ষ্য হলো নভেম্বরের মধ্যে চালু করা। বাজেট ৫০,০০০ ডলারে নির্দিষ্ট। দুজন গুরুত্বপূর্ণ কর্মী অক্টোবরে থাকবেন না। ভেন্ডরের সঙ্গে একটি প্রয়োজনীয় ইন্টিগ্রেশন এখনো টেস্ট করা হয়নি। চালুর তারিখ শুধু নির্বাহী অনুমোদন পেলেই বদলানো যাবে।

### bn_cs

নিচের তথ্যগুলোকে goal, constraint আর risk-এ organize করুন: goal হলো নভেম্বরের মধ্যে launch করা। budget ৫০,০০০ ডলারে fixed। দুজন key staff অক্টোবরে unavailable থাকবেন। vendor-এর সঙ্গে একটি required integration এখনো test করা হয়নি। launch date শুধু executive approval পেলেই বদলানো যাবে।

### Boundary and ambiguity questions

- [ ] RIU-04: Classification boundary: staff unavailability as constraint versus risk.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Classify launching by November as the goal.
  Rationale: The goal.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Classify the fixed $50,000 budget as a constraint.
  Rationale: A constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Classify that the launch date can move only with executive approval as a constraint.
  Rationale: A constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): Classify the two key staff unavailable in October as a risk.
  Rationale: A risk to the November goal.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Classify the untested required vendor integration as a risk.
  Rationale: A risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Staff unavailability may reasonably also be called a constraint; accept if it is also identified as a threat to the goal. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN087

information_synthesis; medium.

### en

Summarize the risk posture: A service has 99.9 percent uptime. It depends on one database instance. Backups run nightly. Recovery has not been tested in the last year.

### bn

সার্বিক ঝুঁকির অবস্থা সংক্ষেপ করুন: একটি সার্ভিসের আপটাইম ৯৯.৯ শতাংশ। এটি একটিমাত্র ডেটাবেস ইনস্ট্যান্সের ওপর নির্ভরশীল। প্রতি রাতে ব্যাকআপ চলে। গত এক বছরে রিকভারি পরীক্ষা করা হয়নি।

### bn_cs

overall risk posture summarize করুন: একটি service-এর uptime ৯৯.৯ শতাংশ। এটা একটিমাত্র database instance-এর ওপর নির্ভরশীল। প্রতি রাতে backup চলে। গত এক বছরে recovery test করা হয়নি।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify the single database instance as a single point of failure.
  Rationale: A key risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Identify that untested recovery means backups may not restore successfully or quickly.
  Rationale: A key risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Note that 99.9 percent uptime reflects past performance and does not remove these risks.
  Rationale: Avoids false reassurance.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Note that nightly backups imply up to a day of data loss.
  Rationale: Recovery-point implication.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Mitigations are optional. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN092

information_synthesis; medium.

### en

Summarize the registration rules in a clear participant-facing notice while preserving fees, deadlines, capacity rules, and exceptions. Registration for the annual student-success conference opens August 24. Current students may register at no charge if they use an institutional email address. Staff and alumni pay $25, while external guests pay $40. The main auditorium holds 80 people. Registration closes when 80 confirmed seats are reached or at 5:00 PM on September 10, whichever happens first. A registration that is started but not completed does not reserve a seat. Payment for staff, alumni, and guests must clear before the registration is confirmed. A waiting list opens automatically once capacity is reached. People on the waiting list are contacted in order if a confirmed attendee cancels, and they have 12 hours to accept the offered seat. Walk-ins are not permitted because building security requires an advance attendee list. Cancellations received by September 8 qualify for a full refund of paid fees; cancellations after that date are normally nonrefundable, although the organizer may approve an exception for documented emergencies. Students who registered for free should still cancel if they cannot attend so the seat can be offered to someone else. Accessibility accommodations should be requested by September 4, but requests received later will still be considered when feasible. The conference office has not guaranteed that late accommodation requests can be fulfilled. Registration confirmation emails contain a QR code that will be used for check-in, but attendees who cannot display the code may check in with a government- or school-issued photo ID.

### bn

ফি, সময়সীমা, আসনসংখ্যা-সংক্রান্ত নিয়ম এবং ব্যতিক্রমগুলো অক্ষুণ্ন রেখে অংশগ্রহণকারীদের উদ্দেশে একটি পরিষ্কার নোটিশ আকারে রেজিস্ট্রেশনের নিয়মগুলো সংক্ষেপ করুন। বার্ষিক শিক্ষার্থী-সাফল্য সম্মেলনের রেজিস্ট্রেশন শুরু হবে ২৪ আগস্ট। বর্তমান শিক্ষার্থীরা প্রতিষ্ঠানের ইমেইল ঠিকানা ব্যবহার করলে বিনামূল্যে রেজিস্ট্রেশন করতে পারবেন। কর্মী ও প্রাক্তন শিক্ষার্থীদের ফি ২৫ ডলার, আর বাইরের অতিথিদের ফি ৪০ ডলার। প্রধান অডিটোরিয়ামে ৮০ জনের জায়গা আছে। ৮০টি নিশ্চিত আসন পূর্ণ হলে অথবা ১০ সেপ্টেম্বর বিকেল ৫টায়—যেটি আগে ঘটে—রেজিস্ট্রেশন বন্ধ হয়ে যাবে। রেজিস্ট্রেশন শুরু করে শেষ না করলে কোনো আসন সংরক্ষিত হয় না। কর্মী, প্রাক্তন শিক্ষার্থী ও অতিথিদের পেমেন্ট ক্লিয়ার না হওয়া পর্যন্ত রেজিস্ট্রেশন নিশ্চিত হবে না। আসন পূর্ণ হলে স্বয়ংক্রিয়ভাবে একটি অপেক্ষমাণ তালিকা খুলে যাবে। নিশ্চিত কোনো অংশগ্রহণকারী বাতিল করলে অপেক্ষমাণ তালিকায় থাকা ব্যক্তিদের ক্রম অনুযায়ী যোগাযোগ করা হবে, এবং প্রস্তাবিত আসন গ্রহণ করার জন্য তাঁরা ১২ ঘণ্টা সময় পাবেন। ভবনের নিরাপত্তার জন্য অংশগ্রহণকারীদের তালিকা আগে থেকে প্রয়োজন, তাই আগাম রেজিস্ট্রেশন ছাড়া সরাসরি এসে অংশ নেওয়ার অনুমতি নেই। ৮ সেপ্টেম্বরের মধ্যে বাতিলের অনুরোধ পৌঁছালে পরিশোধিত ফি পুরোটা ফেরত পাওয়া যাবে; এর পরে বাতিল করলে সাধারণত টাকা ফেরত দেওয়া হয় না, তবে প্রমাণসহ জরুরি পরিস্থিতিতে আয়োজক ব্যতিক্রম অনুমোদন করতে পারেন। যেসব শিক্ষার্থী বিনামূল্যে রেজিস্ট্রেশন করেছেন, তাঁরাও আসতে না পারলে বাতিল করবেন, যাতে আসনটি অন্য কাউকে দেওয়া যায়। অ্যাক্সেসিবিলিটি-সংক্রান্ত সুবিধার অনুরোধ ৪ সেপ্টেম্বরের মধ্যে করা উচিত, তবে পরে পাওয়া অনুরোধও সম্ভব হলে বিবেচনা করা হবে। দেরিতে আসা এমন অনুরোধ পূরণ করা যাবে—সম্মেলন কার্যালয় এমন কোনো নিশ্চয়তা দেয়নি। রেজিস্ট্রেশন নিশ্চিতকরণের ইমেইলে একটি কিউআর কোড থাকবে, যা চেক-ইনে ব্যবহার করা হবে; তবে যাঁরা কোডটি দেখাতে পারবেন না, তাঁরা সরকারি বা শিক্ষাপ্রতিষ্ঠানের দেওয়া ছবিযুক্ত পরিচয়পত্র দিয়ে চেক-ইন করতে পারবেন।

### bn_cs

fee, deadline, capacity rule আর exception-গুলো ঠিক রেখে participant-দের জন্য একটি clear notice আকারে registration rule-গুলো summarize করুন। annual student-success conference-এর registration শুরু হবে ২৪ আগস্ট। current student-রা institutional email address ব্যবহার করলে free-তে register করতে পারবেন। staff আর alumni-দের fee ২৫ ডলার, আর external guest-দের fee ৪০ ডলার। main auditorium-এ ৮০ জনের জায়গা আছে। ৮০টি confirmed seat পূর্ণ হলে অথবা ১০ সেপ্টেম্বর বিকেল ৫টায়—যেটা আগে ঘটে—registration বন্ধ হয়ে যাবে। registration শুরু করে complete না করলে কোনো seat reserve হয় না। staff, alumni আর guest-দের payment clear না হওয়া পর্যন্ত registration confirm হবে না। capacity পূর্ণ হলে automatically একটি waiting list খুলে যাবে। confirmed কোনো attendee cancel করলে waiting list-এর মানুষদের order অনুযায়ী contact করা হবে, এবং offer করা seat accept করার জন্য তাঁরা ১২ ঘণ্টা সময় পাবেন। building security-র জন্য advance attendee list লাগে, তাই walk-in allowed নয়। ৮ সেপ্টেম্বরের মধ্যে cancellation পৌঁছালে paid fee-র full refund পাওয়া যাবে; এর পরে cancel করলে সাধারণত refund দেওয়া হয় না, তবে documented emergency-র ক্ষেত্রে organizer exception approve করতে পারেন। যেসব student free-তে register করেছেন, তাঁরাও আসতে না পারলে cancel করবেন, যাতে seat-টা অন্য কাউকে offer করা যায়। accessibility accommodation-এর request ৪ সেপ্টেম্বরের মধ্যে করা উচিত, তবে পরে আসা request-ও সম্ভব হলে বিবেচনা করা হবে। late accommodation request পূরণ করা যাবে—conference office এমন কোনো guarantee দেয়নি। registration confirmation email-এ একটি QR code থাকবে, যেটা check-in-এ ব্যবহার করা হবে; তবে যাঁরা code-টা দেখাতে পারবেন না, তাঁরা সরকারি বা school-এর দেওয়া photo ID দিয়ে check-in করতে পারবেন।

### Boundary and ambiguity questions

- [ ] RIU-11: Check that omitting "not guaranteed" defeats the unit.
- [ ] RIU-09: Refund rule bundles the deadline and exception; confirm as one relational unit.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): State that registration opens August 24.
  Rationale: Deadline.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that current students register free if they use an institutional email address.
  Rationale: Fee rule with condition.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State the fees: staff and alumni $25, external guests $40.
  Rationale: Fees.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): State that registration closes at 80 confirmed seats or 5:00 PM September 10, whichever comes first.
  Rationale: Capacity and deadline rule.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): State that an incomplete registration does not reserve a seat.
  Rationale: Capacity rule.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): State that paid registrations are confirmed only when payment clears.
  Rationale: Confirmation rule.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (supporting; ordinary, outside prespecified sample): State that a waiting list opens automatically when capacity is reached, offered in order with 12 hours to accept.
  Rationale: Waitlist rule.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-08** (critical; all-critical): State that walk-ins are not permitted.
  Rationale: Exception rule with access consequence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-09** (critical; all-critical, identified-ambiguity-or-boundary): State that cancellations by September 8 get a full refund and later ones are normally nonrefundable except organizer-approved documented emergencies.
  Rationale: Refund deadline and exception.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-10** (supporting; ordinary, outside prespecified sample): State that free registrants should also cancel if they cannot attend.
  Rationale: Capacity rule.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-11** (supporting; identified-ambiguity-or-boundary): State that accessibility requests should be made by September 4, later requests are considered when feasible but not guaranteed.
  Rationale: Deadline and exception.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-12** (supporting; ordinary, outside prespecified sample): State that check-in uses the QR code, or a government- or school-issued photo ID if the code cannot be shown.
  Rationale: Check-in rule.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Extended-context task. Paraphrase is acceptable; conditions and exceptions must stay attached to their rules. Guaranteeing late accommodations would be an unsupported assertion. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH012

technical_troubleshooting; easy.

### en

Only one device in a home network cannot reach the internet while all other devices work. Explain what this suggests and what to test next.

### bn

একটি বাসার নেটওয়ার্কে শুধু একটি ডিভাইস ইন্টারনেটে যুক্ত হতে পারছে না, অথচ বাকি সব ডিভাইস ঠিকঠাক কাজ করছে। এটি কী ইঙ্গিত দেয় এবং এরপর কী পরীক্ষা করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি home network-এ শুধু একটি device internet-এ যেতে পারছে না, অথচ বাকি সব device ঠিকঠাক কাজ করছে। এটা কী indicate করে এবং এরপর কী test করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that the problem is likely on that device rather than the router or internet service.
  Rationale: The key inference.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check the device's network connection and IP settings, such as a valid IP address, DNS or airplane mode.
  Rationale: Next test.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Restart the device or forget and reconnect to the network.
  Rationale: Simple reset.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Check device-specific blocks such as VPN, firewall, proxy or router MAC filtering or parental controls.
  Rationale: Device-specific cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Try the device on another network to confirm.
  Rationale: Isolation test.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH026

technical_troubleshooting; medium.

### en

An application launches normally for an administrator account but not for a standard user. Explain how permissions, profile settings, dependencies, and file locations should be checked.

### bn

একটি অ্যাপ্লিকেশন অ্যাডমিনিস্ট্রেটর অ্যাকাউন্টে স্বাভাবিকভাবে চালু হয়, কিন্তু স্ট্যান্ডার্ড ব্যবহারকারীর অ্যাকাউন্টে হয় না। অনুমতি, প্রোফাইল সেটিংস, ডিপেন্ডেন্সি এবং ফাইলের অবস্থান কীভাবে পরীক্ষা করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি application administrator account-এ স্বাভাবিকভাবে চালু হয়, কিন্তু standard user account-এ হয় না। permission, profile setting, dependency আর file-এর অবস্থান কীভাবে check করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-05: Negative constraint: silence passes when no admin-rights fix is proposed.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Check whether the app needs write access to protected locations, such as program folders or registry areas.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Compare profile-specific settings or create a new standard profile to test.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check dependencies installed per user versus machine-wide.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Check file locations and paths the app expects, such as user-specific data folders.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical, identified-ambiguity-or-boundary): Do not resolve it by giving the standard user administrator rights; scoped permission changes comply.
  Rationale: Granting admin rights creates a security risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Explain how a possible result favors or weakens a named cause.
  Rationale: Turns checks into diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without result interpretation.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH046

technical_troubleshooting; medium.

### en

A service returns inconsistent results after a configuration change even though the code was not modified. Explain what configuration, caching, deployment, and dependency factors you would examine.

### bn

কোড পরিবর্তন না করা সত্ত্বেও একটি কনফিগারেশন পরিবর্তনের পর একটি সার্ভিস অসামঞ্জস্যপূর্ণ ফলাফল দিচ্ছে। কনফিগারেশন, ক্যাশিং, ডিপ্লয়মেন্ট এবং ডিপেন্ডেন্সির কোন কোন বিষয় আপনি পরীক্ষা করবেন তা ব্যাখ্যা করুন।

### bn_cs

code modify না করা সত্ত্বেও একটি configuration change-এর পর একটি service inconsistent result দিচ্ছে। configuration, caching, deployment আর dependency-র কোন কোন factor আপনি examine করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Diff the configuration before and after the change, and check whether all instances received the same configuration.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check caching, such as stale caches holding results computed under the old configuration.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check deployment state, such as a partial rollout leaving instances on different configurations.
  Rationale: Named area; explains inconsistency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Check dependencies whose behavior changes with the configuration, such as endpoints or feature flags.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Explain how a possible observation, such as results differing by instance, favors or weakens a named cause.
  Rationale: Turns checks into diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists factors without any result-to-cause interpretation.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH076

technical_troubleshooting; medium.

### en

A phone shows strong Wi-Fi signal but internet performance is poor only in one room. Explain how to investigate interference, access-point placement, channel congestion, and device behavior.

### bn

একটি ফোনে ওয়াই-ফাই সিগন্যাল শক্তিশালী দেখালেও শুধু একটি ঘরে ইন্টারনেটের পারফরম্যান্স খারাপ। সিগন্যালে ব্যাঘাত, অ্যাক্সেস পয়েন্টের অবস্থান, চ্যানেলের ভিড় এবং ডিভাইসের আচরণ কীভাবে খতিয়ে দেখবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি phone-এ Wi-Fi signal strong দেখালেও শুধু একটি ঘরে internet-এর performance খারাপ। interference, access point-এর অবস্থান, channel congestion আর device-এর আচরণ কীভাবে investigate করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Check for interference sources in or near the room, such as microwaves or cordless devices.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Assess access-point placement or which access point the phone connects to in that room.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check channel congestion, such as neighboring networks on the same channel, and try another channel or band.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Compare the phone with another device in the same room to identify device behavior.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Explain how a possible result favors or weakens a named cause, noting that signal strength alone does not reflect throughput.
  Rationale: Without interpretation the answer does not investigate the cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without result interpretation.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH080

technical_troubleshooting; hard.

### en

A mobile application synchronizes some records but consistently skips others. Propose an investigation that separates local validation, permissions, network retries, server rules, and data-specific edge cases.

### bn

একটি মোবাইল অ্যাপ কিছু রেকর্ড সিঙ্ক করে, কিন্তু অন্য কিছু রেকর্ড প্রতিবারই বাদ দিয়ে যায়। লোকাল ভ্যালিডেশন, অনুমতি, নেটওয়ার্ক রিট্রাই, সার্ভারের নিয়ম এবং নির্দিষ্ট ডেটার এজ কেস আলাদা করে দেখার মতো একটি অনুসন্ধান প্রস্তাব করুন।

### bn_cs

একটি mobile app কিছু record sync করে, কিন্তু অন্য কিছু record প্রতিবারই বাদ দিয়ে যায়। local validation, permission, network retry, server-এর নিয়ম আর নির্দিষ্ট data-র edge case আলাদা করে দেখার মতো একটি investigation propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Compare skipped and synced records to find shared characteristics.
  Rationale: Starting evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check local validation errors that stop records from being queued.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check permissions or ownership rules that prevent upload of certain records.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check network retry logs and whether failed records are retried or dropped.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Check server-side rules or rejections, such as server logs or error responses.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; prespecified-ordinary-sample): Test data-specific edge cases such as special characters, size limits or null fields.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (critical; all-critical): Explain how a possible result favors or weakens a named cause relative to others.
  Rationale: Without interpretation the investigation does not separate causes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Proposes comparisons but gives no result-to-cause interpretation.

Draft notes: P05 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Follows the accepted differential-diagnosis convention. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
