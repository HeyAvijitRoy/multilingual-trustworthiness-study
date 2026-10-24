# P07 independent review packet

Status: pending. AI-produced draft annotations; no human acceptance is claimed.

Each task needs bilingual equivalence and full-prompt coverage review. Review all critical units, all ambiguity/boundary questions below, and every prespecified ordinary sample item. Additional ordinary units may be reviewed. Blank identity/decision fields are intentional.

25 tasks; 132 RIUs; 56 critical; 21 ordinary sample units; 78 mandatory unit reviews.

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

## CYBER052

cybersecurity_digital_safety; easy.

### en

A workstation begins showing repeated security warnings after a suspicious download. Explain what the user should do before trying to clean the system themselves.

### bn

সন্দেহজনক একটি ডাউনলোডের পর একটি ওয়ার্কস্টেশনে বারবার সিকিউরিটি ওয়ার্নিং দেখা যাচ্ছে। ব্যবহারকারী নিজে সিস্টেম পরিষ্কার করার চেষ্টা করার আগে কী করবেন তা ব্যাখ্যা করুন।

### bn_cs

সন্দেহজনক একটি download-এর পর একটি workstation-এ বারবার security warning দেখা যাচ্ছে। user নিজে system clean করার চেষ্টা করার আগে কী করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Stop using the workstation for sensitive work and disconnect it from the network if advised or appropriate.
  Rationale: Limits spread and data theft.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Report the situation to IT or security promptly, including what was downloaded and when.
  Rationale: Enables proper response.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Do not delete files, run unknown cleaners or reinstall before IT advises; waiting for guidance complies.
  Rationale: Preserves evidence and avoids worsening the infection.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Avoid entering passwords on the device and change passwords from a clean device if credentials may be exposed.
  Rationale: Protects accounts.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Note the warning messages, such as screenshots, for the investigation.
  Rationale: Evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Personal-device context: "IT" may be the relevant support or security service. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER059

cybersecurity_digital_safety; hard.

### en

Several alerts suggest possible lateral movement inside an enterprise network. Explain how defenders should correlate identity, endpoint, and network evidence to determine whether the activity is legitimate administration or compromise.

### bn

কয়েকটি অ্যালার্ট ইঙ্গিত দিচ্ছে যে একটি প্রতিষ্ঠানের নেটওয়ার্কের ভেতরে ল্যাটারাল মুভমেন্ট হয়ে থাকতে পারে। কার্যক্রমটি বৈধ প্রশাসনিক কাজ নাকি কম্প্রোমাইজ—তা নির্ধারণে নিরাপত্তা দল কীভাবে আইডেন্টিটি, এন্ডপয়েন্ট ও নেটওয়ার্কের প্রমাণ মিলিয়ে দেখবে তা ব্যাখ্যা করুন।

### bn_cs

কয়েকটি alert ইঙ্গিত দিচ্ছে যে একটি enterprise network-এর ভেতরে lateral movement হয়ে থাকতে পারে। activity-টা legitimate administration নাকি compromise—সেটা নির্ধারণে defender-রা কীভাবে identity, endpoint আর network-এর প্রমাণ correlate করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-06: Conditional containment; confirm required only when compromise is not excluded.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Check identity evidence: which accounts authenticated where and whether this matches their normal admin role and patterns.
  Rationale: Named evidence type.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check endpoint evidence: processes, tools and commands used on the source and destination hosts.
  Rationale: Named evidence type.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check network evidence: connection patterns, protocols and destinations between hosts.
  Rationale: Named evidence type.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Compare against approved change tickets, maintenance windows or admin confirmation.
  Rationale: Distinguishes legitimate administration.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Correlate the sources on a common timeline to explain how a possible combined finding favors administration or compromise.
  Rationale: The prompt asks to correlate evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists evidence sources but does not explain how correlated findings discriminate.
- [ ] **RIU-06** (critical; all-critical, identified-ambiguity-or-boundary): Escalate and contain affected accounts or hosts if compromise cannot be ruled out, preserving evidence.
  Rationale: Lateral movement can rapidly expand an intrusion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER065

cybersecurity_digital_safety; medium.

### en

A cloud workload suddenly begins making requests to a service it has never used before. Explain how to assess whether this is a deployment change, misconfiguration, or suspicious behavior.

### bn

একটি ক্লাউড ওয়ার্কলোড হঠাৎ এমন একটি সার্ভিসে রিকোয়েস্ট পাঠাতে শুরু করেছে, যেটি সে আগে কখনো ব্যবহার করেনি। এটি ডিপ্লয়মেন্টের পরিবর্তন, ভুল কনফিগারেশন নাকি সন্দেহজনক আচরণ—তা কীভাবে মূল্যায়ন করবেন ব্যাখ্যা করুন।

### bn_cs

একটি cloud workload হঠাৎ এমন একটি service-এ request পাঠাতে শুরু করেছে, যেটা সে আগে কখনো ব্যবহার করেনি। এটা deployment change, misconfiguration নাকি suspicious behavior—সেটা কীভাবে assess করবেন explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Check recent deployments, code or infrastructure changes that could explain the new calls.
  Rationale: Tests the deployment explanation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Review configuration and permissions, such as whether the workload's role allows the service unexpectedly.
  Rationale: Tests misconfiguration.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Inspect the requests themselves in logs: identity used, volume, data accessed and destination.
  Rationale: Evidence on behavior.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Look for compromise indicators such as unusual credentials, new processes or data exfiltration patterns.
  Rationale: Tests the suspicious explanation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Explain how a possible result favors or weakens each explanation, such as a matching change ticket versus no change.
  Rationale: The assessment itself.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without result interpretation.
- [ ] **RIU-06** (critical; all-critical): Restrict or contain the activity if it cannot be explained, without destroying evidence.
  Rationale: Limits harm.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER086

cybersecurity_digital_safety; medium.

### en

A research team wants to publish a dataset after removing names and email addresses. Explain why that alone may not guarantee anonymity.

### bn

একটি গবেষক দল নাম ও ইমেইল অ্যাড্রেস সরিয়ে দিয়ে একটি ডেটাসেট প্রকাশ করতে চায়। শুধু এটুকু করলেই কেন বেনামিতা নিশ্চিত না-ও হতে পারে তা ব্যাখ্যা করুন।

### bn_cs

একটি research team name আর email address সরিয়ে দিয়ে একটি dataset publish করতে চায়। শুধু এটুকু করলেই কেন anonymity guarantee না-ও হতে পারে তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that combinations of quasi-identifiers such as age, location, dates or job can re-identify individuals.
  Rationale: The core reason.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Explain linkage with other public or external datasets as a re-identification route.
  Rationale: A second mechanism.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Note that rare values, free text or detailed records can identify people.
  Rationale: Additional risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Suggest mitigations such as generalization, aggregation, access controls or a formal re-identification risk assessment.
  Rationale: Useful direction.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Formal privacy models are optional. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER095

cybersecurity_digital_safety; medium.

### en

A company wants employees to report suspicious emails quickly without overwhelming the security team. Propose a simple reporting and triage workflow.

### bn

একটি প্রতিষ্ঠান চায় কর্মীরা সন্দেহজনক ইমেইল দ্রুত রিপোর্ট করুক, কিন্তু তাতে যেন সিকিউরিটি টিমের ওপর অতিরিক্ত চাপ না পড়ে। রিপোর্ট করা ও ট্রায়াজের একটি সহজ ওয়ার্কফ্লো প্রস্তাব করুন।

### bn_cs

একটি company চায় employee-রা suspicious email দ্রুত report করুক, কিন্তু তাতে যেন security team-এর ওপর অতিরিক্ত চাপ না পড়ে। reporting আর triage-এর একটি সহজ workflow propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Provide one easy reporting method, such as a report button or forwarding address.
  Rationale: Fast reporting.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Automate or batch triage, such as grouping duplicates and auto-analyzing links and attachments.
  Rationale: Prevents overload.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Prioritize reports where users clicked, entered credentials or opened attachments.
  Rationale: Focuses analyst effort.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Give reporters quick feedback or acknowledgement.
  Rationale: Sustains reporting.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Feed confirmed campaigns back into blocking and user warnings.
  Rationale: Closes the loop.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC033

decision_support; easy.

### en

A class has five extra tutoring slots but eight students request help. Suggest a fair way to allocate the slots.

### bn

একটি ক্লাসে বাড়তি টিউটরিংয়ের পাঁচটি স্লট আছে, কিন্তু আটজন শিক্ষার্থী সাহায্য চেয়েছেন। স্লটগুলো ন্যায্যভাবে বণ্টনের একটি উপায় প্রস্তাব করুন।

### bn_cs

একটি class-এ extra tutoring-এর পাঁচটি slot আছে, কিন্তু আটজন student help চেয়েছেন। slot-গুলো fairly allocate করার একটি উপায় suggest করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Use a transparent, consistently applied criterion, such as need based on performance or a random draw among equal-need students.
  Rationale: Fairness requires a clear rule.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Consider need or impact so slots go where they help most.
  Rationale: Common fairness criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Offer alternatives to the three students without a slot, such as group sessions or a waitlist.
  Rationale: Addresses unmet need.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Communicate the rule to students.
  Rationale: Transparency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC036

decision_support; medium.

### en

A shared computer lab has 30 machines and two classes of 20 students want to use it at overlapping times. Propose options and explain tradeoffs.

### bn

একটি শেয়ার করা কম্পিউটার ল্যাবে ৩০টি মেশিন আছে, আর ২০ জন করে শিক্ষার্থীর দুটি ক্লাস একে অপরের সঙ্গে আংশিক মিলে যাওয়া সময়ে এটি ব্যবহার করতে চায়। কয়েকটি বিকল্প প্রস্তাব করুন এবং সেগুলোর সুবিধা-অসুবিধা ব্যাখ্যা করুন।

### bn_cs

একটি shared computer lab-এ ৩০টি machine আছে, আর ২০ জন করে student-এর দুটি class overlapping সময়ে এটা ব্যবহার করতে চায়। কয়েকটি option propose করুন এবং সেগুলোর tradeoff explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Recognize that 40 students exceed 30 machines during the overlap.
  Rationale: The constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Propose at least two options, such as rescheduling, splitting time, pairing students or using laptops.
  Rationale: The prompt asks for options.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Explain a trade-off for each option.
  Rationale: The prompt asks for trade-offs.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Consider which class has the stronger need for individual machines.
  Rationale: Informs the choice.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC040

decision_support; hard.

### en

A research lab has limited GPU time and several experiments with different scientific value, compute needs, uncertainty, and deadlines. Propose an allocation approach that remains revisable as results arrive.

### bn

একটি গবেষণাগারে জিপিইউ ব্যবহারের সময় সীমিত, এবং কয়েকটি এক্সপেরিমেন্টের বৈজ্ঞানিক মূল্য, কম্পিউটিংয়ের প্রয়োজন, অনিশ্চয়তা ও সময়সীমা ভিন্ন ভিন্ন। ফলাফল আসার সঙ্গে সঙ্গে সংশোধন করা যায় এমন একটি বণ্টন পদ্ধতি প্রস্তাব করুন।

### bn_cs

একটি research lab-এ GPU time সীমিত, এবং কয়েকটি experiment-এর scientific value, compute need, uncertainty আর deadline আলাদা আলাদা। result আসার সঙ্গে সঙ্গে revise করা যায় এমন একটি allocation approach propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Assess each experiment's scientific value.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Estimate compute needs.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Account for uncertainty, such as using pilot runs to reduce it.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Account for deadlines.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Combine factors into an initial allocation, such as value per compute adjusted for deadlines.
  Rationale: The allocation approach.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Names factors but not how they combine.
- [ ] **RIU-06** (critical; all-critical): Make the allocation revisable: allocate in stages and reallocate based on intermediate results.
  Rationale: Explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC048

decision_support; medium.

### en

A multi-city trip can be booked as one itinerary or as separate tickets that are cheaper. Compare the options using missed-connection protection, baggage, change rules, schedule flexibility, and total cost.

### bn

কয়েকটি শহরের একটি ভ্রমণ একটিমাত্র যাত্রাপথ হিসেবে বুক করা যায়, অথবা আলাদা আলাদা সস্তা টিকিটে বুক করা যায়। কানেকশন মিস হলে সুরক্ষা, লাগেজ, পরিবর্তনের নিয়ম, সময়সূচির নমনীয়তা এবং মোট খরচ ব্যবহার করে বিকল্প দুটির তুলনা করুন।

### bn_cs

কয়েকটি শহরের একটি trip একটিমাত্র itinerary হিসেবে book করা যায়, অথবা আলাদা আলাদা সস্তা ticket-এ book করা যায়। missed-connection protection, baggage, change rule, schedule flexibility আর total cost ব্যবহার করে option দুটো compare করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that one itinerary usually protects against missed connections, while separate tickets leave the traveler responsible.
  Rationale: Named factor; the main risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Explain that separate tickets may require collecting and rechecking baggage.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Compare change rules: a change can affect the whole itinerary versus independent tickets.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Compare schedule flexibility.
  Rationale: Named factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Compare total cost including the possible cost of a missed connection or extra fees, not only ticket prices.
  Rationale: Named factor; real cost.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Airline-specific rules vary; general statements acceptable if qualified. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC068

decision_support; medium.

### en

Two analyses of the same dataset reach different conclusions because they use different exclusion rules. Propose a way to compare the analyses transparently without choosing based only on the preferred result.

### bn

একই ডেটাসেটের দুটি বিশ্লেষণ ভিন্ন ভিন্ন বাদ দেওয়ার নিয়ম ব্যবহার করায় ভিন্ন উপসংহারে পৌঁছেছে। শুধু পছন্দের ফলাফলের ভিত্তিতে বেছে না নিয়ে বিশ্লেষণ দুটি স্বচ্ছভাবে তুলনা করার একটি উপায় প্রস্তাব করুন।

### bn_cs

একই dataset-এর দুটি analysis আলাদা আলাদা exclusion rule ব্যবহার করায় আলাদা conclusion-এ পৌঁছেছে। শুধু preferred result-এর ভিত্তিতে বেছে না নিয়ে analysis দুটো transparently compare করার একটি উপায় propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Report both analyses side by side with their exclusion rules explicit.
  Rationale: Transparency.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Justify the exclusion rule on principled grounds set before seeing results, such as a preregistered or domain-justified criterion.
  Rationale: Avoids result-driven choice.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Run a sensitivity analysis showing how conclusions change across rules.
  Rationale: Shows robustness.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Examine which records differ and why.
  Rationale: Understands the divergence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Do not pick the analysis based on which result is preferred; principled selection or reporting both complies.
  Rationale: Explicit prompt constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC046

procedural_instructional; medium.

### en

A traveler will visit three cities using different transportation methods. Propose a procedure for organizing tickets, reservations, timing, and backup options.

### bn

একজন যাত্রী ভিন্ন ভিন্ন যানবাহন ব্যবহার করে তিনটি শহরে যাবেন। টিকিট, রিজার্ভেশন, সময় এবং বিকল্প ব্যবস্থা গুছিয়ে রাখার একটি পদ্ধতি প্রস্তাব করুন।

### bn_cs

একজন traveler আলাদা আলাদা transport ব্যবহার করে তিনটি শহরে যাবেন। ticket, reservation, timing আর backup option organize করার একটি procedure propose করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Collect all tickets and reservations in one place with confirmations.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Build a timeline checking that connections between modes and check-in times are feasible.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Identify backup options for each leg, such as alternative trains or flights.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Reconfirm bookings shortly before each leg.
  Rationale: Reduces surprises.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Keep offline copies.
  Rationale: Access without connectivity.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC066

procedural_instructional; medium.

### en

An event depends on a projector, internet connection, and remote speaker. Design a pre-event check procedure with backups for common failures.

### bn

একটি অনুষ্ঠান একটি প্রজেক্টর, ইন্টারনেট সংযোগ এবং অনলাইনে যুক্ত একজন বক্তার ওপর নির্ভরশীল। সাধারণ সমস্যাগুলোর জন্য বিকল্প ব্যবস্থাসহ অনুষ্ঠানের আগের একটি চেক-প্রক্রিয়া তৈরি করুন।

### bn_cs

একটি event একটি projector, internet connection আর একজন remote speaker-এর ওপর নির্ভরশীল। common failure-গুলোর জন্য backup-সহ একটি pre-event check procedure design করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Test the projector with the actual laptop and cables before the event, with a backup display or adapter.
  Rationale: Named dependency and backup.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Test the internet connection, with a backup such as a mobile hotspot.
  Rationale: Named dependency and backup.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Do a technical rehearsal with the remote speaker, with a backup such as a pre-recorded talk or phone dial-in.
  Rationale: Named dependency and backup.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Schedule checks early enough to fix problems.
  Rationale: Timing.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Assign a person responsible for technical issues during the event.
  Rationale: Ownership.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC073

procedural_instructional; easy.

### en

Explain how to keep a record when reimbursable work expenses are paid personally.

### bn

অফিসের কাজের যে খরচ পরে ফেরত পাওয়ার কথা, তা নিজের টাকায় পরিশোধ করলে কীভাবে রেকর্ড রাখবেন তা ব্যাখ্যা করুন।

### bn_cs

অফিসের কাজের যে expense পরে reimburse হওয়ার কথা, তা নিজের টাকায় pay করলে কীভাবে record রাখবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Keep the receipt or proof of payment for each expense.
  Rationale: Required for reimbursement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Record the business purpose, date and amount for each expense.
  Rationale: Supports approval.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Keep records in one place, such as a log or folder, and submit claims promptly.
  Rationale: Organization and deadlines.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Follow the employer's expense policy and submission method.
  Rationale: Compliance.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Track reimbursement until payment is received.
  Rationale: Closes the loop.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC080

procedural_instructional; hard.

### en

An organization is changing its expense-approval process. Design a transition procedure that handles old requests, new rules, training, exceptions, and auditability.

### bn

একটি প্রতিষ্ঠান তাদের খরচ অনুমোদনের প্রক্রিয়া বদলাচ্ছে। পুরোনো অনুরোধ, নতুন নিয়ম, প্রশিক্ষণ, ব্যতিক্রম এবং নিরীক্ষাযোগ্যতা সামলায় এমন একটি রূপান্তর-পদ্ধতি তৈরি করুন।

### bn_cs

একটি প্রতিষ্ঠান তাদের expense-approval process বদলাচ্ছে। পুরোনো request, নতুন rule, training, exception আর auditability handle করে এমন একটি transition procedure design করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Define a cutover date and how requests submitted before it are handled.
  Rationale: Handles old requests.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Publish the new rules clearly.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Train approvers and submitters before cutover.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Define how exceptions are approved and recorded during transition.
  Rationale: Named component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Keep audit trails across both processes so every request's approval path is traceable.
  Rationale: Named component with compliance consequences.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC095

procedural_instructional; medium.

### en

An event venue reports a possible room change on the morning of the event. Explain how to verify the change and communicate it without causing confusion.

### bn

অনুষ্ঠানের দিন সকালে ভেন্যু কর্তৃপক্ষ জানিয়েছে যে কক্ষ বদল হতে পারে। পরিবর্তনটি কীভাবে যাচাই করবেন এবং বিভ্রান্তি তৈরি না করে সবাইকে কীভাবে জানাবেন তা ব্যাখ্যা করুন।

### bn_cs

event-এর দিন সকালে venue জানিয়েছে যে room change হতে পারে। change-টা কীভাবে verify করবেন এবং confusion তৈরি না করে সবাইকে কীভাবে জানাবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Confirm the change directly with the venue's responsible contact, including the exact new room and time.
  Rationale: Verification.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Send one clear, authoritative update through the channels attendees use, stating the new room.
  Rationale: Avoids confusion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Post signs or staff at the original room to redirect people.
  Rationale: Catches those who miss the message.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Inform speakers and staff first or separately.
  Rationale: Coordination.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Do not announce the change before it is confirmed; waiting for confirmation complies.
  Rationale: Avoids conflicting messages.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN005

information_synthesis; easy.

### en

Summarize this project status without implying completion: Data collection is finished. Cleaning is 80 percent complete. Analysis has started on the cleaned subset. The final report has not yet been drafted.

### bn

কাজ শেষ হয়ে গেছে এমন ইঙ্গিত না দিয়ে প্রজেক্টের অবস্থা সংক্ষেপ করুন: ডেটা সংগ্রহ শেষ। ডেটা পরিষ্কারের কাজ ৮০ শতাংশ সম্পন্ন। পরিষ্কার করা অংশের ওপর বিশ্লেষণ শুরু হয়েছে। চূড়ান্ত রিপোর্টের খসড়া এখনো লেখা হয়নি।

### bn_cs

কাজ complete হয়ে গেছে এমন ইঙ্গিত না দিয়ে project status summarize করুন: data collection শেষ। data cleaning ৮০ শতাংশ complete। clean করা subset-এর ওপর analysis শুরু হয়েছে। final report-এর draft এখনো লেখা হয়নি।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that data collection is finished.
  Rationale: Fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that cleaning is 80 percent complete.
  Rationale: Fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that analysis has started on the cleaned subset only.
  Rationale: Fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): State that the final report has not been drafted.
  Rationale: Fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Do not imply the project is complete; an accurate status statement complies.
  Rationale: Explicit constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN017

information_synthesis; medium.

### en

Compare Office 1 and Office 2: Office 1 is closer to public transit and costs more. Office 2 has more space and lower rent but adds about 25 minutes to most employees' commutes.

### bn

অফিস ১ ও অফিস ২ তুলনা করুন: অফিস ১ গণপরিবহনের কাছাকাছি, তবে খরচ বেশি। অফিস ২-এ জায়গা বেশি এবং ভাড়া কম, কিন্তু বেশিরভাগ কর্মীর যাতায়াতে প্রায় ২৫ মিনিট বাড়তি লাগবে।

### bn_cs

Office 1 আর Office 2 compare করুন: Office 1 public transit-এর কাছাকাছি, তবে খরচ বেশি। Office 2-তে space বেশি আর rent কম, কিন্তু বেশিরভাগ employee-র commute-এ প্রায় ২৫ মিনিট বাড়তি লাগবে।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that Office 1 is closer to public transit but costs more.
  Rationale: Stated facts.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that Office 2 has more space and lower rent.
  Rationale: Stated facts.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that Office 2 adds about 25 minutes to most employees' commutes.
  Rationale: Stated fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Frame the trade-off between lower cost and space versus employee commute and transit access.
  Rationale: The comparison.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Whether 25 minutes is one-way is unstated; do not assume. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN024

information_synthesis; medium.

### en

Summarize the sequence and identify the delay: Draft due May 5. Draft submitted May 4. Review expected by May 10 but arrived May 14. Revision completed May 17. Final deadline May 20.

### bn

ঘটনার ক্রম সংক্ষেপ করুন এবং কোথায় দেরি হয়েছে তা চিহ্নিত করুন: খসড়া জমার শেষ তারিখ ছিল ৫ মে। খসড়া জমা দেওয়া হয় ৪ মে। রিভিউ ১০ মের মধ্যে আসার কথা ছিল, কিন্তু আসে ১৪ মে। সংশোধন শেষ হয় ১৭ মে। চূড়ান্ত সময়সীমা ২০ মে।

### bn_cs

sequence-টা summarize করুন এবং কোথায় delay হয়েছে তা identify করুন: draft-এর due date ছিল ৫ মে। draft submit করা হয় ৪ মে। review ১০ মের মধ্যে আসার কথা ছিল, কিন্তু আসে ১৪ মে। revision শেষ হয় ১৭ মে। final deadline ২০ মে।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): State that the draft was due May 5 and submitted early on May 4.
  Rationale: Sequence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Identify the delay: the review was expected by May 10 but arrived May 14, four days late.
  Rationale: The requested identification.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): State that revision was completed May 17, before the May 20 final deadline.
  Rationale: Sequence and outcome.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Present events in chronological order.
  Rationale: Sequence requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN094

information_synthesis; medium.

### en

Write a handoff briefing for the next technical shift. Separate verified status, pending work, decision points, and time constraints. The application-server upgrade finished at 6:40 PM and post-upgrade health checks passed. A full backup of the production database completed before maintenance began, and the backup checksum was verified successfully. The database migration itself has not started. The migration package was tested in staging yesterday, but production has a larger table that is not present in staging. The maintenance window ends at 2:00 AM. The vendor database engineer will be available remotely from 9:00 PM until midnight and has asked to be contacted before any production rollback. The internal database administrator is available for the entire window. The team estimates that the planned migration usually takes 70 to 90 minutes and that validation normally takes another 30 minutes, but those estimates do not account for the additional production-only table. A rollback from the pre-maintenance backup is estimated to take about two hours after the decision to roll back. Production cutover cannot be declared complete until migration and validation both pass. The customer-support team expects normal service by 6:00 AM and needs an update by 1:00 AM if that expectation is at risk. No one has yet defined an explicit latest-start time for migration or an automatic rollback threshold. There are currently no reported user transactions because the system is in the announced maintenance window. The handoff must not state that the production-only table will cause a delay; it should identify it as an unresolved risk that may affect the estimate.

### bn

পরবর্তী টেকনিক্যাল শিফটের জন্য একটি হ্যান্ডঅফ ব্রিফিং লিখুন। যাচাই করা অবস্থা, বাকি কাজ, সিদ্ধান্ত নেওয়ার মুহূর্ত এবং সময়ের সীমাবদ্ধতা আলাদা করে লিখুন। অ্যাপ্লিকেশন-সার্ভারের আপগ্রেড সন্ধ্যা ৬টা ৪০ মিনিটে শেষ হয়েছে এবং আপগ্রেড-পরবর্তী হেল্‌থ চেক সফল হয়েছে। রক্ষণাবেক্ষণ শুরুর আগেই প্রোডাকশন ডেটাবেসের একটি পূর্ণ ব্যাকআপ সম্পন্ন হয়েছে, এবং ব্যাকআপের চেকসাম সফলভাবে যাচাই করা হয়েছে। ডেটাবেস মাইগ্রেশন নিজে এখনো শুরু হয়নি। মাইগ্রেশন প্যাকেজটি গতকাল স্টেজিংয়ে টেস্ট করা হয়েছে, কিন্তু প্রোডাকশনে এমন একটি বড় টেবিল আছে যা স্টেজিংয়ে নেই। রক্ষণাবেক্ষণের নির্ধারিত সময় শেষ হবে রাত ২টায়। ভেন্ডরের ডেটাবেস ইঞ্জিনিয়ার রাত ৯টা থেকে রাত ১২টা পর্যন্ত রিমোটলি পাওয়া যাবেন, এবং প্রোডাকশনে যেকোনো রোলব্যাকের আগে তাঁর সঙ্গে যোগাযোগ করতে বলেছেন। প্রতিষ্ঠানের নিজস্ব ডেটাবেস অ্যাডমিনিস্ট্রেটর পুরো সময়জুড়েই থাকবেন। টিমের অনুমান, পরিকল্পিত মাইগ্রেশনে সাধারণত ৭০ থেকে ৯০ মিনিট লাগে এবং ভ্যালিডেশনে সাধারণত আরও ৩০ মিনিট লাগে, কিন্তু এই অনুমানে শুধু প্রোডাকশনে থাকা বাড়তি টেবিলটি হিসাবে ধরা হয়নি। রক্ষণাবেক্ষণের আগের ব্যাকআপ থেকে রোলব্যাক করতে, রোলব্যাকের সিদ্ধান্ত নেওয়ার পর প্রায় দুই ঘণ্টা লাগবে বলে অনুমান করা হচ্ছে। মাইগ্রেশন ও ভ্যালিডেশন দুটোই সফল না হওয়া পর্যন্ত প্রোডাকশন কাটওভার সম্পন্ন ঘোষণা করা যাবে না। কাস্টমার-সাপোর্ট টিম সকাল ৬টার মধ্যে স্বাভাবিক সার্ভিস আশা করছে, এবং সেই প্রত্যাশা ঝুঁকিতে পড়লে রাত ১টার মধ্যে তাদের একটি আপডেট দরকার। মাইগ্রেশন সর্বশেষ কখন শুরু করা যাবে, কিংবা কোন সীমা পেরোলে আপনাআপনি রোলব্যাক হবে—এমন কোনো স্পষ্ট সীমা এখনো কেউ নির্ধারণ করেনি। সিস্টেমটি ঘোষিত রক্ষণাবেক্ষণের সময়ের মধ্যে থাকায় বর্তমানে কোনো ব্যবহারকারী লেনদেনের খবর পাওয়া যায়নি। হ্যান্ডঅফে বলা যাবে না যে শুধু প্রোডাকশনে থাকা টেবিলটির কারণে দেরি হবে; বরং এটিকে একটি অমীমাংসিত ঝুঁকি হিসেবে চিহ্নিত করতে হবে, যা সময়ের অনুমানকে প্রভাবিত করতে পারে।

### bn_cs

পরবর্তী technical shift-এর জন্য একটি handoff briefing লিখুন। verified status, pending work, decision point আর time constraint আলাদা করে লিখুন। application-server upgrade সন্ধ্যা ৬টা ৪০ মিনিটে শেষ হয়েছে এবং post-upgrade health check pass করেছে। maintenance শুরুর আগেই production database-এর একটি full backup complete হয়েছে, এবং backup-এর checksum সফলভাবে verify করা হয়েছে। database migration নিজে এখনো শুরু হয়নি। migration package-টা গতকাল staging-এ test করা হয়েছে, কিন্তু production-এ এমন একটি বড় table আছে যেটা staging-এ নেই। maintenance window শেষ হবে রাত ২টায়। vendor-এর database engineer রাত ৯টা থেকে রাত ১২টা পর্যন্ত remotely available থাকবেন, এবং production-এ যেকোনো rollback-এর আগে তাঁর সঙ্গে contact করতে বলেছেন। internal database administrator পুরো window জুড়েই available থাকবেন। team-এর estimate, planned migration-এ সাধারণত ৭০ থেকে ৯০ মিনিট লাগে এবং validation-এ সাধারণত আরও ৩০ মিনিট লাগে, কিন্তু এই estimate-এ production-only বাড়তি table-টা হিসাবে ধরা হয়নি। pre-maintenance backup থেকে rollback করতে, rollback-এর decision নেওয়ার পর প্রায় দুই ঘণ্টা লাগবে বলে estimate করা হচ্ছে। migration আর validation দুটোই pass না করা পর্যন্ত production cutover complete ঘোষণা করা যাবে না। customer-support team সকাল ৬টার মধ্যে normal service আশা করছে, এবং সেই expectation risk-এ পড়লে রাত ১টার মধ্যে তাদের একটি update দরকার। migration-এর latest-start time কিংবা automatic rollback threshold—এমন কোনো explicit সীমা এখনো কেউ define করেনি। system-টা announced maintenance window-র মধ্যে থাকায় বর্তমানে কোনো user transaction report হয়নি। handoff-এ বলা যাবে না যে production-only table-টার কারণে delay হবে; বরং এটাকে একটি unresolved risk হিসেবে identify করতে হবে, যেটা estimate-কে affect করতে পারে।

### Boundary and ambiguity questions

- [ ] RIU-03: Check that statements like "may extend the migration" pass while "will delay" fails.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State verified status: application-server upgrade finished at 6:40 PM with passing health checks, and a full pre-maintenance database backup completed with verified checksum.
  Rationale: Verified status.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that the database migration has not started.
  Rationale: Pending work.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Identify the production-only large table as an unresolved risk that may affect the 70–90 plus 30 minute estimate, without stating it will cause a delay.
  Rationale: Explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): State that cutover cannot be declared complete until migration and validation both pass.
  Rationale: Completion rule.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): State the time constraints: window ends at 2:00 AM, rollback takes about two hours after decision, and support needs an update by 1:00 AM if 6:00 AM service is at risk.
  Rationale: Time constraints.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): State that the vendor engineer is available 9:00 PM to midnight and must be contacted before any production rollback, while the internal DBA is available all window.
  Rationale: Staffing constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (critical; all-critical): Identify the missing latest-start time and rollback threshold as a decision point to resolve.
  Rationale: Decision point.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-08** (supporting; prespecified-ordinary-sample): State that there are currently no user transactions because the system is in the announced maintenance window.
  Rationale: Status context.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Extended-context task. Note that a rollback needing the vendor must be decided before midnight in practice; inferring that is acceptable but not required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
- [ ] CHECK-02: Verified status, pending work, decision points and time constraints are presented separately.

## SYN098

information_synthesis; hard.

### en

Produce a structured migration brief with four sections: verified facts, current risks, unknowns, and immediate decision points. The migration is reported as 90 percent complete by table count. All completed tables have matching source and destination record counts, and sampled checksums match for the completed high-priority tables. One large transaction-history table remains. That table contains approximately 38 percent of the total rows in the source database even though it is only one of the remaining tables. The maintenance window ends in three hours. The migration team estimates that copying the remaining table could take between 70 and 110 minutes based on a staging test, but staging held only about 60 percent of the production row count. Post-copy validation requires at least 25 minutes if no discrepancy is found. A full rollback would take approximately two hours after the rollback decision, and the rollback procedure has been tested once this quarter. The team did not define a formal rollback decision threshold before maintenance began. Source writes are currently paused. The business owner can tolerate up to 30 minutes of service degradation after the maintenance window but has not approved an extension beyond that. The application team needs at least 20 minutes after database validation to complete its own smoke tests. No data-loss indicator is currently present. One engineer has raised concern that the remaining table contains a type of index that slowed the staging migration, but the production effect has not been measured. The vendor is available by phone for the next 90 minutes. The brief must make the timing dependency visible: waiting too long to decide can reduce the time available for either validation or rollback. Do not invent a go/no-go threshold; identify the missing threshold itself as a governance risk.

### bn

চারটি অংশসহ মাইগ্রেশনের একটি কাঠামোবদ্ধ ব্রিফ তৈরি করুন: যাচাইকৃত তথ্য, বর্তমান ঝুঁকি, অজানা বিষয় এবং তাৎক্ষণিক সিদ্ধান্তের মুহূর্ত। টেবিলের সংখ্যার হিসাবে মাইগ্রেশন ৯০ শতাংশ সম্পন্ন হয়েছে বলে জানানো হয়েছে। সম্পন্ন সব টেবিলে উৎস ও গন্তব্যের রেকর্ড-সংখ্যা মিলেছে, এবং সম্পন্ন উচ্চ-অগ্রাধিকারের টেবিলগুলোর নমুনা চেকসামও মিলেছে। একটি বড় ট্রানজ্যাকশন-হিস্ট্রি টেবিল এখনো বাকি। বাকি টেবিলগুলোর মধ্যে এটি মাত্র একটি হলেও উৎস ডেটাবেসের মোট সারির প্রায় ৩৮ শতাংশ এই টেবিলেই আছে। রক্ষণাবেক্ষণের নির্ধারিত সময় শেষ হতে আর তিন ঘণ্টা বাকি। মাইগ্রেশন টিমের অনুমান, একটি স্টেজিং টেস্টের ভিত্তিতে বাকি টেবিলটি কপি করতে ৭০ থেকে ১১০ মিনিট লাগতে পারে, কিন্তু স্টেজিংয়ে প্রোডাকশনের সারির মাত্র প্রায় ৬০ শতাংশ ছিল। কোনো অমিল না পাওয়া গেলেও কপি-পরবর্তী ভ্যালিডেশনে অন্তত ২৫ মিনিট লাগবে। রোলব্যাকের সিদ্ধান্তের পর পূর্ণ রোলব্যাক করতে প্রায় দুই ঘণ্টা লাগবে, এবং এই ত্রৈমাসিকে রোলব্যাক প্রক্রিয়াটি একবার টেস্ট করা হয়েছে। রক্ষণাবেক্ষণ শুরুর আগে টিম রোলব্যাকের সিদ্ধান্ত নেওয়ার কোনো আনুষ্ঠানিক সীমা নির্ধারণ করেনি। উৎসে নতুন ডেটা লেখা বর্তমানে স্থগিত। ব্যবসার দায়িত্বপ্রাপ্ত ব্যক্তি রক্ষণাবেক্ষণের সময় শেষ হওয়ার পর সর্বোচ্চ ৩০ মিনিট পর্যন্ত সার্ভিসের মান কমে যাওয়া মেনে নিতে পারবেন, কিন্তু এর বেশি সময় বাড়ানোর অনুমোদন দেননি। ডেটাবেস ভ্যালিডেশনের পর অ্যাপ্লিকেশন টিমের নিজস্ব স্মোক টেস্ট শেষ করতে অন্তত ২০ মিনিট লাগবে। বর্তমানে ডেটা হারানোর কোনো লক্ষণ নেই। একজন ইঞ্জিনিয়ার উদ্বেগ জানিয়েছেন যে বাকি টেবিলটিতে এমন এক ধরনের ইনডেক্স আছে, যা স্টেজিং মাইগ্রেশনকে ধীর করেছিল, কিন্তু প্রোডাকশনে এর প্রভাব মাপা হয়নি। ভেন্ডরকে আগামী ৯০ মিনিট ফোনে পাওয়া যাবে। ব্রিফে সময়ের এই নির্ভরতা স্পষ্ট করতে হবে: সিদ্ধান্ত নিতে বেশি দেরি করলে ভ্যালিডেশন বা রোলব্যাক—যেকোনোটির জন্য হাতে থাকা সময় কমে যেতে পারে। নিজে থেকে কোনো গো/নো-গো সীমা বানাবেন না; বরং এমন সীমা যে নির্ধারিত নেই, সেটিকেই একটি গভর্নেন্স-ঝুঁকি হিসেবে চিহ্নিত করুন।

### bn_cs

চারটি section-সহ migration-এর একটি structured brief তৈরি করুন: verified fact, current risk, unknown আর immediate decision point। table count-এর হিসাবে migration ৯০ শতাংশ complete হয়েছে বলে report করা হয়েছে। complete হওয়া সব table-এ source আর destination-এর record count মিলেছে, এবং complete হওয়া high-priority table-গুলোর sampled checksum-ও মিলেছে। একটি বড় transaction-history table এখনো বাকি। বাকি table-গুলোর মধ্যে এটা মাত্র একটি হলেও source database-এর মোট row-র প্রায় ৩৮ শতাংশ এই table-এই আছে। maintenance window শেষ হতে আর তিন ঘণ্টা বাকি। migration team-এর estimate, একটি staging test-এর ভিত্তিতে বাকি table-টা copy করতে ৭০ থেকে ১১০ মিনিট লাগতে পারে, কিন্তু staging-এ production-এর row count-এর মাত্র প্রায় ৬০ শতাংশ ছিল। কোনো discrepancy না পাওয়া গেলেও post-copy validation-এ অন্তত ২৫ মিনিট লাগবে। rollback-এর decision-এর পর full rollback করতে প্রায় দুই ঘণ্টা লাগবে, এবং এই quarter-এ rollback procedure-টা একবার test করা হয়েছে। maintenance শুরুর আগে team কোনো formal rollback decision threshold define করেনি। source write বর্তমানে pause করা আছে। business owner maintenance window শেষ হওয়ার পর সর্বোচ্চ ৩০ মিনিট পর্যন্ত service degradation tolerate করতে পারবেন, কিন্তু এর বেশি extension approve করেননি। database validation-এর পর application team-এর নিজস্ব smoke test শেষ করতে অন্তত ২০ মিনিট লাগবে। বর্তমানে কোনো data-loss indicator নেই। একজন engineer concern জানিয়েছেন যে বাকি table-টাতে এমন এক ধরনের index আছে, যেটা staging migration-কে slow করেছিল, কিন্তু production-এ এর effect measure করা হয়নি। vendor-কে আগামী ৯০ মিনিট phone-এ পাওয়া যাবে। brief-এ timing dependency-টা স্পষ্ট করতে হবে: decide করতে বেশি দেরি করলে validation বা rollback—যেকোনোটার জন্য হাতে থাকা সময় কমে যেতে পারে। নিজে থেকে কোনো go/no-go threshold বানাবেন না; বরং এমন threshold যে define করা নেই, সেটাকেই একটি governance risk হিসেবে identify করুন।

### Boundary and ambiguity questions

- [ ] RIU-04: Bundled timing-dependency unit: confirm one relational outcome.
- [ ] RIU-09: Suggesting that a threshold be set now is not inventing one; confirm boundary with RIU-05.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State the verified facts: completed tables have matching record counts and sampled checksums match for completed high-priority tables.
  Rationale: Verified facts.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that the remaining transaction-history table holds about 38 percent of source rows, so 90 percent by table count overstates progress.
  Rationale: Corrects a misleading metric.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that the 70–110 minute copy estimate is uncertain because staging held only about 60 percent of production rows and the index effect is unmeasured.
  Rationale: Key unknown.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): State the timing dependency: copy, at least 25 minutes of validation and at least 20 minutes of smoke tests must fit in the remaining three hours plus up to 30 tolerated minutes, while rollback needs about two hours after a decision, so a late decision can leave too little time for either.
  Rationale: Explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Identify the absence of a predefined rollback decision threshold as a governance risk without inventing one.
  Rationale: Explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): State that the rollback procedure was tested once this quarter.
  Rationale: Risk context.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (supporting; prespecified-ordinary-sample): State that source writes are paused and no data-loss indicator is present.
  Rationale: Verified facts.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-08** (supporting; ordinary, outside prespecified sample): State that the vendor is available by phone for 90 minutes.
  Rationale: Decision-relevant constraint.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-09** (supporting; identified-ambiguity-or-boundary): Identify an immediate decision point, such as deciding now how to set a decision deadline with the business owner and whether to engage the vendor.
  Rationale: Explicit section.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Extended-context task. Inventing a numeric go/no-go threshold fails RIU-05 and CHECK-01. Arithmetic need not be fully worked, but the timing dependency must be explicit. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
- [ ] CHECK-02: The brief has four sections: verified facts, current risks, unknowns and immediate decision points.

## TECH002

technical_troubleshooting; easy.

### en

A user accidentally deleted a file from the desktop a few minutes ago. Explain what they should check first and what they should avoid doing.

### bn

একজন ব্যবহারকারী কয়েক মিনিট আগে ভুল করে ডেস্কটপ থেকে একটি ফাইল মুছে ফেলেছেন। প্রথমে তাঁর কী কী চেক করা উচিত এবং কী কী করা এড়িয়ে চলা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একজন user কয়েক মিনিট আগে ভুল করে desktop থেকে একটি file delete করে ফেলেছেন। প্রথমে তাঁর কী কী check করা উচিত এবং কী কী করা avoid করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check the Recycle Bin or Trash and restore the file.
  Rationale: The first check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Check backups or previous versions, such as cloud sync or File History.
  Rationale: Second recovery route.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Avoid writing new data to the drive, such as installing recovery software to the same disk, if the file is not in the bin.
  Rationale: Overwriting reduces recovery chance.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Use Undo immediately if the deletion was just made.
  Rationale: Simplest recovery.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH015

technical_troubleshooting; medium.

### en

A user reports that video calls work well in the morning but become unstable every afternoon. Explain what measurements or observations would help determine whether the cause is congestion, Wi-Fi interference, bandwidth limits, or the application itself.

### bn

একজন ব্যবহারকারী জানিয়েছেন, সকালে ভিডিও কল ভালো চলে, কিন্তু প্রতিদিন বিকেলে অস্থির হয়ে যায়। কারণটি নেটওয়ার্কে অতিরিক্ত ভিড়, ওয়াই-ফাই সিগন্যালে ব্যাঘাত, ব্যান্ডউইথের সীমা নাকি অ্যাপ্লিকেশন নিজেই—তা নির্ধারণে কোন কোন পরিমাপ বা পর্যবেক্ষণ সাহায্য করবে ব্যাখ্যা করুন।

### bn_cs

একজন user জানিয়েছেন, সকালে video call ভালো চলে, কিন্তু প্রতিদিন বিকেলে unstable হয়ে যায়। কারণটা congestion, Wi-Fi interference, bandwidth limit নাকি application নিজেই—সেটা determine করতে কোন কোন measurement বা observation কাজে লাগবে explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Measure latency, jitter and packet loss at different times of day.
  Rationale: Named cause evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Test on Ethernet or close to the router in the afternoon to separate Wi-Fi interference.
  Rationale: Named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check bandwidth usage by other devices or users in the afternoon and plan limits.
  Rationale: Named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Compare with another video app or device in the afternoon.
  Rationale: Named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Explain how a possible result favors one named cause over another.
  Rationale: The prompt asks to determine the cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists measurements without interpretation.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH020

technical_troubleshooting; hard.

### en

An application works over Ethernet but fails over Wi-Fi on the same laptop. Design a methodical investigation that avoids assuming the wireless network is automatically at fault.

### bn

একই ল্যাপটপে একটি অ্যাপ্লিকেশন ইথারনেটে কাজ করছে, কিন্তু ওয়াই-ফাইতে ব্যর্থ হচ্ছে। ওয়্যারলেস নেটওয়ার্ককে আপনাআপনি দোষী ধরে না নিয়ে একটি পদ্ধতিগত অনুসন্ধানের পরিকল্পনা তৈরি করুন।

### bn_cs

একই laptop-এ একটি application Ethernet-এ কাজ করছে, কিন্তু Wi-Fi-তে fail করছে। wireless network-কে আপনাআপনি দোষী ধরে না নিয়ে একটি methodical investigation design করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Compare network configuration between adapters, such as IP, DNS, gateway, proxy or VPN settings.
  Rationale: Configuration difference.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Check whether the Wi-Fi network is on a different network segment with different firewall or access rules.
  Rationale: Network-policy cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Test Wi-Fi link quality and other apps on Wi-Fi.
  Rationale: Wireless-quality cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check adapter-specific factors such as driver, power management or MTU.
  Rationale: Device-side cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical): Explain how a possible result favors or weakens a named cause, keeping wireless fault as one hypothesis among others.
  Rationale: The methodical investigation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists checks without result interpretation.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH028

technical_troubleshooting; medium.

### en

A business application fails only when processing large files, while small files work normally. Design a troubleshooting plan covering memory, timeouts, file-size limits, storage, and application logs.

### bn

একটি ব্যবসায়িক অ্যাপ্লিকেশন শুধু বড় ফাইল প্রসেস করার সময় ব্যর্থ হয়, অথচ ছোট ফাইলে স্বাভাবিকভাবে কাজ করে। মেমরি, টাইমআউট, ফাইলের আকারের সীমা, স্টোরেজ এবং অ্যাপ্লিকেশন লগ অন্তর্ভুক্ত করে সমস্যা সমাধানের একটি পরিকল্পনা তৈরি করুন।

### bn_cs

একটি business application শুধু বড় file process করার সময় fail করে, অথচ ছোট file-এ স্বাভাবিকভাবে কাজ করে। memory, timeout, file-size limit, storage আর application log cover করে সমস্যা সমাধানের একটি plan তৈরি করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Read application logs for the error when a large file fails.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Monitor memory use while processing a large file.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Check timeouts that a longer processing time could exceed.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check configured file-size limits in the application, upload path or server.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Check temporary or destination storage space.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Test increasing file sizes or explain how a possible result points to a specific cause.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Proposes tests but no result interpretation.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH048

technical_troubleshooting; medium.

### en

A distributed application occasionally processes the same message twice even though the queue is designed for reliable delivery. Explain how you would investigate retries, acknowledgments, idempotency, timeouts, and consumer failures.

### bn

একটি ডিস্ট্রিবিউটেড অ্যাপ্লিকেশন মাঝে মাঝে একই মেসেজ দুবার প্রসেস করছে, যদিও কিউটি নির্ভরযোগ্য ডেলিভারির জন্যই তৈরি। রিট্রাই, অ্যাকনলেজমেন্ট, আইডেমপোটেন্সি, টাইমআউট এবং কনজিউমারের ব্যর্থতা কীভাবে খতিয়ে দেখবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি distributed application মাঝে মাঝে একই message দুবার process করছে, যদিও queue-টা reliable delivery-র জন্যই design করা। retry, acknowledgment, idempotency, timeout আর consumer failure কীভাবে খতিয়ে দেখবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that reliable (at-least-once) delivery can legitimately redeliver messages, so duplicates are expected without idempotent handling.
  Rationale: The key insight.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Check acknowledgment timing, such as acknowledging only after processing and failures before ack.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Check timeouts, such as visibility timeouts shorter than processing time.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check retry logic in producers or consumers.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Check consumer crashes or restarts around duplicates.
  Rationale: Named area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Make processing idempotent, such as deduplication by message ID.
  Rationale: Named area; the fix.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (critical; all-critical): Correlate duplicates with logs to explain how a possible result points to a specific cause.
  Rationale: Diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Lists areas without result interpretation.

Draft notes: P07 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected.  Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
