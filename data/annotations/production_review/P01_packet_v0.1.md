# P01 independent review packet

Status: pending. AI-produced draft annotations; no human acceptance is claimed.

Each task needs bilingual equivalence and full-prompt coverage review. Review all critical units, all ambiguity/boundary questions below, and every prespecified ordinary sample item. Additional ordinary units may be reviewed. Blank identity/decision fields are intentional.

25 tasks; 103 RIUs; 41 critical; 18 ordinary sample units; 89 mandatory unit reviews.

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

## CYBER002

cybersecurity_digital_safety; easy.

### en

A person reused the same password on several websites and one of those sites reported a breach. Explain what they should do next.

### bn

একজন ব্যক্তি কয়েকটি ওয়েবসাইটে একই পাসওয়ার্ড ব্যবহার করেছেন, আর তার মধ্যে একটি সাইট জানিয়েছে যে সেখানে ডেটা ফাঁসের ঘটনা ঘটেছে। এরপর তাঁর কী করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একজন ব্যক্তি কয়েকটি website-এ একই password reuse করেছেন, আর তার মধ্যে একটি site জানিয়েছে যে সেখানে breach হয়েছে। এরপর তাঁর কী করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-02: Confirm that changes at the breached site and other reuse sites are independently assessable; do not require every hypothetical account or a named password manager.
- [ ] RIU-03: Recovery and session revocation are conditional on observed compromise or provider guidance; no proof of compromise is supplied.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Replace the password at the breached site through a trusted route with a strong password unique to that account.
  Rationale: Leaving the known exposed credential active preserves direct access to the breached account.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Change that reused password on the other accounts to distinct strong passwords so the breached secret no longer works there.
  Rationale: Changing only the breached account leaves the stated cross-site credential-stuffing exposure unresolved.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary): Check the affected accounts for suspicious logins or changes and follow appropriate recovery/reporting steps if unauthorized activity is found.
  Rationale: Helps identify actual misuse rather than assuming password replacement repairs every existing compromise.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Enable available multifactor authentication on the affected accounts as an additional barrier to misuse of passwords.
  Rationale: Adds account protection but does not replace changing the reused secret.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants retain one breached site and multiple sites sharing the same secret. Revocation of sessions is conditional on evidence or supported recovery, not compulsory on every site. No presumption that the other sites were breached. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER037

cybersecurity_digital_safety; medium.

### en

A remote-access service receives repeated connection attempts from many external addresses. Explain how defenders should assess whether this is routine scanning or a meaningful threat.

### bn

একটি রিমোট অ্যাক্সেস সার্ভিসে বাইরের অনেক আইপি অ্যাড্রেস থেকে বারবার সংযোগের চেষ্টা আসছে। এটি নিয়মিত স্ক্যানিং নাকি অর্থবহ কোনো হুমকি—নিরাপত্তা দল তা কীভাবে মূল্যায়ন করবে ব্যাখ্যা করুন।

### bn_cs

একটি remote-access service-এ বাইরের অনেক address থেকে বারবার connection attempt আসছে। এটা routine scanning নাকি meaningful কোনো threat—defender-রা সেটা কীভাবে assess করবেন explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-03: Inspect success/outcome versus corroborating post-access behavior as distinct evidence; no mandatory list of all telemetry fields.
- [ ] RIU-04: Check ordinal anchors and avoid requiring blanket blocking of every source or service shutdown.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary): Inspect the connection/authentication events for timing, rate, targets and outcomes, distinguishing failed connection attempts from successful access.
  Rationale: Builds an interpretable event pattern rather than deciding from the number of source addresses alone.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Compare the observed pattern with the service’s normal exposure/baseline and its authentication, patching or access-control posture.
  Rationale: Places scanning in context without requiring a particular threat-intelligence feed or guaranteed vulnerability.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Seek corroborating evidence of targeted exploitation or compromise, such as suspicious successful sessions, commands, account activity or related endpoint/network events.
  Rationale: Tests threat significance using independent behavior rather than source volume alone.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): Use the evidence to distinguish routine unsuccessful scanning from attempted exploitation or compromise, escalating/containing credible adverse evidence and keeping uncertain cases under investigation.
  Rationale: A blanket benign or malicious verdict based only on many external attempts defeats the assessment objective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Explicitly withholds a compromise verdict pending success/behavior evidence, but gives no practical evidence-based disposition or escalation rule.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. BN refers to external IP addresses, while EN/BN-CS say addresses; the shared network context supports source-address evidence without imposing an IP-version requirement. Repetition or many sources alone neither proves compromise nor guarantees benign scanning. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER048

cybersecurity_digital_safety; medium.

### en

A company discovers that a cloud storage bucket containing internal documents was publicly accessible for an unknown period. Describe how to investigate exposure, contain risk, assess impact, and preserve evidence.

### bn

একটি প্রতিষ্ঠান জানতে পেরেছে, অভ্যন্তরীণ ডকুমেন্ট থাকা একটি ক্লাউড স্টোরেজ বাকেট অজানা সময় ধরে পাবলিকলি অ্যাক্সেসযোগ্য ছিল। কতটা উন্মুক্ত হয়েছে তা তদন্ত, ঝুঁকি নিয়ন্ত্রণ, প্রভাব মূল্যায়ন এবং প্রমাণ সংরক্ষণ কীভাবে করবেন তা বর্ণনা করুন।

### bn_cs

একটি প্রতিষ্ঠান জানতে পেরেছে, internal document থাকা একটি cloud storage bucket অজানা সময় ধরে publicly accessible ছিল। exposure-এর তদন্ত, risk contain করা, impact মূল্যায়ন আর evidence সংরক্ষণ কীভাবে করবেন তা describe করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-03: Separate evidence collection/time-window reconstruction from the impact interpretation; no requirement to recover unavailable records or assert confirmed exfiltration.
- [ ] RIU-04: Review feasible evidence preservation alongside containment; no rigid order that leaves a public bucket exposed until exhaustive imaging finishes.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary): Establish the scope and plausible time window of public access using bucket/object permissions, configuration history and available access/audit records, marking gaps where logs cannot determine exposure.
  Rationale: Constrains what is known without equating absent logs with no access.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Remove unintended public access and verify that only intended authorized access remains, preserving necessary legitimate access where feasible.
  Rationale: Without access containment the disclosed document exposure can continue.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Assess impact from the documents’ sensitivity and available evidence of actual or possible access/use, clearly separating confirmed access from uncertain exposure.
  Rationale: Treating unknown exposure as either confirmed theft or proven safety materially distorts the incident impact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): Preserve relevant logs, permission/configuration state and other incident evidence before it is lost, without delaying urgent access containment.
  Rationale: Loss or destruction of the limited evidence can make the requested exposure investigation infeasible.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants preserve an unknown public-access duration and internal documents. Public accessibility is not proof that documents were downloaded. Containment and evidence retention should proceed together; no specific provider, statutory notification rule or compromised credential is assumed. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER073

cybersecurity_digital_safety; easy.

### en

A developer accidentally commits an API key to a private repository. Explain the correct response even if the repository was never public.

### bn

একজন ডেভেলপার ভুল করে একটি এপিআই-কি একটি প্রাইভেট রিপোজিটরিতে কমিট করে ফেলেছেন। রিপোজিটরিটি কখনো পাবলিক না হয়ে থাকলেও সঠিক রেসপন্স কী তা ব্যাখ্যা করুন।

### bn_cs

একজন developer ভুল করে একটি API key একটি private repository-তে commit করে ফেলেছেন। repository-টা কখনো public না হয়ে থাকলেও correct response কী তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01: Invalidation is mandatory; replacement is conditional on continued service need, not a required new credential when the key is no longer needed.
- [ ] RIU-04: Check whether coordinated history cleanup is proportionate; do not require destructive force-push or pretend every clone can be erased.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Revoke or invalidate the committed API key promptly, even though the repository has always been private; issue a new key if the service still needs one.
  Rationale: The exposed key remains usable until invalidated; repository privacy alone does not contain that risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Remove the key from tracked code and replace needed application use with an appropriately protected secret/configuration mechanism.
  Rationale: Prevents continued propagation without prescribing one secret-management product.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Review relevant repository access and API usage/audit records for exposure or unauthorized use, with further response guided by what is found.
  Rationale: Assesses possible misuse without inventing that any unauthorized access occurred.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Address retained repository copies/history through an appropriate coordinated cleanup, recognizing that deletion of the latest file does not erase existing commits or clones.
  Rationale: Reduces residual propagation; even complete history cleanup cannot make an already exposed key safe.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Explain that collaborators, integrations, existing history or copied repositories can expose a key even when the repository was never public.
  Rationale: Supplies the requested private-repository caveat rather than treating public visibility as the only exposure route.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Private repository status does not establish that the key was unseen; all variants preserve this qualification. No particular Git command, scanner or secret store is required. History cleanup is not a substitute for revocation. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER080

cybersecurity_digital_safety; hard.

### en

A critical application depends on an unsupported library that cannot be replaced immediately. Explain how to manage the risk using compensating controls, monitoring, isolation, and a migration plan.

### bn

একটি গুরুত্বপূর্ণ অ্যাপ্লিকেশন এমন একটি লাইব্রেরির ওপর নির্ভরশীল, যার আর কোনো সাপোর্ট নেই এবং যা এখনই বদলানো সম্ভব নয়। কম্পেনসেটিং কন্ট্রোল, মনিটরিং, আইসোলেশন এবং মাইগ্রেশন পরিকল্পনা ব্যবহার করে ঝুঁকি কীভাবে সামলাবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি critical application এমন একটি unsupported library-র ওপর নির্ভরশীল, যেটা এখনই replace করা সম্ভব নয়। compensating control, monitoring, isolation আর migration plan ব্যবহার করে risk কীভাবে manage করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-03: Ensure compensating safeguards and isolation earn credit for distinct operational propositions; network isolation alone must not be counted twice as both complete units.
- [ ] RIU-04: Review the proposed ordinal distinction and critical rationale; accept migration plans with a justified checkpoint rather than an invented guaranteed completion date.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Apply feasible compensating safeguards to reduce the unsupported library’s exploitable exposure, such as restricting risky functionality or enforcing additional validation/access controls around its use.
  Rationale: With replacement unavailable, a plan offering only observation and a future date leaves current exposure untreated.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Monitor application/library-related security signals and relevant threat or vulnerability information, with an actionable investigation/escalation response.
  Rationale: Makes changes in residual risk detectable without imposing an exhaustive telemetry stack.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary): Isolate or restrict the application/library’s reachable interfaces, privileges or communications to limit attack surface and possible spread while preserving necessary service.
  Rationale: Provides the specifically requested containment layer; no air-gap or guaranteed zero exposure is assumed.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): Define a concrete migration path to a supported alternative, with ownership, staged validation and a completion target or review checkpoint.
  Rationale: An indefinite unsupported dependency defeats the requested migration component and perpetuates the residual risk; a bare wish to migrate is insufficient.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Identifies a plausible supported replacement direction but supplies neither accountable next steps nor a target/review checkpoint; a vague promise to upgrade someday scores 0.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. The library is unsupported and cannot be replaced immediately in all variants. The four named control areas are distinct; do not require a specific WAF, network product, known exploit or replacement date. A compensating control must be tied to plausible exposure, rather than merely naming a tool. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC027

decision_support; medium.

### en

A team wants to replace a familiar tool with a newer one that offers better features but requires retraining. Explain how to evaluate whether switching is worthwhile.

### bn

একটি টিম পরিচিত একটি টুলের বদলে একটি নতুন টুল নিতে চায়, যার ফিচার ভালো কিন্তু নতুন করে প্রশিক্ষণ লাগবে। টুল বদলানো সার্থক হবে কি না তা কীভাবে মূল্যায়ন করবেন ব্যাখ্যা করুন।

### bn_cs

একটি team পরিচিত একটি tool-এর বদলে একটি নতুন tool নিতে চায়, যার feature ভালো কিন্তু retraining লাগবে। switch করা worthwhile হবে কি না তা কীভাবে evaluate করবেন explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-02, RIU-04: Distinguish assessing training burden from the final tradeoff judgment; no mandatory weighted scoring formula or numerical payback period.
- [ ] RIU-03: Check that compatibility examples remain alternatives rather than a compulsory exhaustive procurement checklist.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Evaluate whether the newer features address real team needs or improve actual work compared with the familiar tool.
  Rationale: Feature novelty alone does not establish a benefit worth buying.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; identified-ambiguity-or-boundary): Account for retraining effort and temporary productivity disruption when estimating the switching burden.
  Rationale: Captures the explicit transition tradeoff without inventing training hours.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary): Check relevant adoption and migration constraints, such as workflow compatibility, data transfer or support, using a trial or other concrete evidence where useful.
  Rationale: Tests whether the claimed gains are feasible without requiring every possible integration check.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): Decide whether to switch, defer or retain the tool by weighing achievable benefits against retraining and other relevant transition costs over an appropriate time horizon.
  Rationale: A feature-only recommendation omits the central worthwhile-versus-retraining decision.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants retain improved features and required retraining; better features do not guarantee net value. No actual price, team size, training duration or scoring weights are provided. A pilot is an alternative source of evidence, not an obligatory product. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC062

decision_support; easy.

### en

Two sources report slightly different counts for the same month. Explain what information should be verified before choosing one number.

### bn

দুটি উৎস একই মাসের জন্য সামান্য ভিন্ন সংখ্যা দেখাচ্ছে। একটি সংখ্যা বেছে নেওয়ার আগে কোন কোন তথ্য যাচাই করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

দুটি source একই মাসের জন্য সামান্য আলাদা count দেখাচ্ছে। একটি number বেছে নেওয়ার আগে কোন কোন তথ্য verify করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-02: Do not split every possible metadata field into a mandatory RIU; examples are alternative diagnostics within definition and period checks.
- [ ] RIU-04: No universal rule that newer/official/larger is always correct; an explicitly deferred decision is valid.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary): Check that both counts use the same definition, included population/items, units and deduplication or exclusion rules.
  Rationale: Nominally similar counts may measure different sets.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; identified-ambiguity-or-boundary): Verify the exact month boundaries, time zone/cutoff and reporting/update dates so the figures refer to comparable periods and versions.
  Rationale: The same month label can conceal different extraction windows or later revisions.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Check each source’s provenance and counting/collection method for known errors, missing records or corrections.
  Rationale: Helps judge credibility rather than automatically preferring the larger or newer value.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): Choose or reconcile a count only using the verified common definition and source evidence, or state what remains unresolved if there is not enough information.
  Rationale: Selecting an arbitrary number without resolving comparability defeats the central decision.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants give slight differences for the same month but no source hierarchy or actual count. A reliable answer may leave the choice unresolved pending reconciliation. A count definition differs from the collection/correction process. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC076

decision_support; medium.

### en

A technical team needs to explain a system outage to nontechnical users. Explain how to decide what technical detail is necessary and what should be omitted.

### bn

একটি টেকনিক্যাল টিমকে প্রযুক্তি সম্পর্কে অনভিজ্ঞ ব্যবহারকারীদের কাছে একটি সিস্টেম বিভ্রাটের ব্যাখ্যা দিতে হবে। কোন টেকনিক্যাল বিবরণ দরকার এবং কোনটি বাদ দেওয়া উচিত তা কীভাবে ঠিক করবেন ব্যাখ্যা করুন।

### bn_cs

একটি technical team-কে nontechnical user-দের কাছে একটি system outage explain করতে হবে। কোন technical detail দরকার এবং কোনটা বাদ দেওয়া উচিত তা কীভাবে decide করবেন explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-02, RIU-03: An include/omit decision rule is sufficient; no fabricated cause, deadline or exhaustive incident-template fields required.
- [ ] RIU-04: Check the boundary between useful uncertainty guidance and an unsolicited requirement to publish confidential internals.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Identify the users’ practical information needs, including service impact and any action they need to take.
  Rationale: Makes detail selection audience-dependent rather than indiscriminately removing all technical content.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Include or translate technical details when they explain user impact, required action or meaningful recovery/status information in understandable language.
  Rationale: Omitting all useful technical substance would defeat the requested explanation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Omit or move unnecessary internal implementation details and unexplained jargon out of the main explanation when they do not help users understand the outage or act.
  Rationale: An unfiltered engineering account defeats the task’s nontechnical audience requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Distinguish confirmed facts from unknown causes or estimates rather than inventing a simplified certainty for the audience.
  Rationale: Preserves accuracy while simplifying the account.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants ask how to decide what detail to include/omit, not for an invented incident report. No cause, resolution time or affected population is supplied. Security sensitivity is conditional on the content proposed. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC080

decision_support; hard.

### en

A cross-cultural team interprets direct and indirect feedback differently. Propose a communication approach that preserves clarity while reducing unnecessary interpersonal friction.

### bn

ভিন্ন ভিন্ন সংস্কৃতির সদস্য নিয়ে গঠিত একটি টিম সরাসরি ও পরোক্ষ ফিডব্যাককে ভিন্নভাবে বোঝে। স্পষ্টতা বজায় রেখে অপ্রয়োজনীয় পারস্পরিক টানাপোড়েন কমায়—এমন একটি যোগাযোগ পদ্ধতি প্রস্তাব করুন।

### bn_cs

আলাদা আলাদা culture-এর সদস্য নিয়ে গঠিত একটি cross-cultural team direct আর indirect feedback-কে আলাদাভাবে বোঝে। clarity বজায় রেখে অপ্রয়োজনীয় interpersonal friction কমায়—এমন একটি communication approach propose করুন।

### Boundary and ambiguity questions

- [ ] RIU-02, RIU-03: Clarity and respectful delivery are separately assessable joint objectives; do not require one prescribed feedback script.
- [ ] RIU-01: Cultural sensitivity must not become unsupported claims about whole national or ethnic groups.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary): Ask about or agree on team members’ feedback preferences and shared expectations instead of assuming one cultural communication style applies to everyone.
  Rationale: Establishes a shared basis for adapting the approach.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Express the substantive issue, expected change or next step explicitly enough that indirect politeness does not obscure the message.
  Rationale: Without actionable meaning the proposed approach fails the requested clarity objective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Deliver feedback respectfully using specific behavior/impact rather than personal judgment, adapting tone or setting to reduce avoidable embarrassment or friction.
  Rationale: A clear but personally hostile approach fails the joint interpersonal objective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Check the recipient’s understanding and invite clarification or response to catch differing interpretations.
  Rationale: Closes the interpretation loop without requiring a particular meeting format.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants preserve differing interpretations of direct/indirect feedback. Do not stereotype a culture or infer individuals’ preferences from nationality. Any tactful feedback method can work; no named framework is mandatory. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC087

decision_support; medium.

### en

A policy has high compliance on paper but staff use unofficial workarounds. Explain how to decide whether enforcement, redesign, training, or tooling is the right response.

### bn

কাগজে-কলমে একটি নীতি মানার হার অনেক বেশি, কিন্তু কর্মীরা অনানুষ্ঠানিক বিকল্প পথ ব্যবহার করছেন। কড়াকড়ি প্রয়োগ, নতুন করে নকশা, প্রশিক্ষণ নাকি প্রয়োজনীয় টুল দেওয়া—কোনটি সঠিক পদক্ষেপ তা কীভাবে ঠিক করবেন ব্যাখ্যা করুন।

### bn_cs

কাগজে-কলমে একটি policy-র compliance অনেক বেশি, কিন্তু staff-রা unofficial workaround ব্যবহার করছেন। enforcement, redesign, training নাকি tooling—কোনটা সঠিক response তা কীভাবে decide করবেন explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-03: Root-cause evidence and the intervention choice are distinct; do not require deploying every option.
- [ ] RIU-03: Review ordinal partial credit: a substantive cause-response link can earn half; mentioning all four labels without a decision cannot.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary): Investigate actual staff workflows and why workarounds occur, including whether the obstacle is understanding, impractical policy design, missing tools or deliberate bypass.
  Rationale: Distinguishes causes that imply different interventions.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Assess the workaround’s effects on the policy’s underlying goal, including material risk and useful work that the official process obstructs.
  Rationale: Paper compliance alone does not show whether the policy is effective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Match enforcement, redesign, training and/or tooling to the diagnosed cause and risk rather than choosing one automatically from reported compliance.
  Rationale: The central response choice is infeasible without a cause-to-intervention link.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Links at least one named response to a specific plausible cause but does not explain how the competing causes would change the choice; a bare list of four options scores 0.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check whether the chosen change improves actual behavior and the underlying policy outcome, revising it if workarounds persist.
  Rationale: Tests whether the decision works beyond improved paperwork.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants contrast high on-paper compliance with actual workarounds. The response may combine options; none is known to be optimal. A full legal audit or punitive action is not required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC003

procedural_instructional; medium.

### en

Explain how to prepare a document for sharing so another person can read it without accidentally editing the original.

### bn

একটি ডকুমেন্ট শেয়ার করার আগে কীভাবে প্রস্তুত করলে অন্য একজন সেটি পড়তে পারবেন, কিন্তু ভুল করে মূল ফাইলটি এডিট করে ফেলবেন না, তা ব্যাখ্যা করুন।

### bn_cs

একটি document share করার আগে কীভাবে prepare করলে অন্য একজন সেটা পড়তে পারবেন, কিন্তু ভুল করে original-টা edit করে ফেলবেন না, তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01: A separate copy is valid even if the copy itself is editable; the prompt protects the original, not necessarily all derivative copies.
- [ ] RIU-02, RIU-03: Do not impose exact file format, password or export settings; review whether accessibility is preserved by the selected method.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Use a sharing path that protects the original from recipient edits, such as a view-only share or a separately shared copy/export that does not grant edit access to the original.
  Rationale: Recipient ability to overwrite the original directly defeats the task’s core protection objective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; identified-ambiguity-or-boundary): Provide the recipient with a readable compatible version or view they can actually access.
  Rationale: A protected but inaccessible/unreadable file does not fulfill the reading objective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Check the intended recipient’s access/permission or the shared copy before sending/finalizing the share to confirm the original is protected and the document can be read.
  Rationale: Verifies that the chosen share method has the intended effect without requiring a specific test account.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants preserve both readability and original protection. Read-only permissions, a separately shared copy, or a suitable view/export may be valid. PDF is not inherently proof of access control, and no specific office suite is required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC026

procedural_instructional; medium.

### en

A group project has four students contributing to one paper. Design a process for dividing work while maintaining one consistent argument and writing style.

### bn

একটি গ্রুপ প্রজেক্টে চারজন শিক্ষার্থী মিলে একটি পেপার লিখছেন। একটিমাত্র সামঞ্জস্যপূর্ণ যুক্তি ও লেখার ধরন বজায় রেখে কাজ ভাগ করার একটি প্রক্রিয়া তৈরি করুন।

### bn_cs

একটি group project-এ চারজন student মিলে একটি paper লিখছেন। একটিমাত্র consistent argument আর writing style বজায় রেখে কাজ ভাগ করার একটি process design করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-04: Distinguish a common argument/outline from final cross-section integration; do not double-count a mere instruction to use the outline.
- [ ] RIU-02: Four students all need meaningful responsibility; exact equality of words or one section per person is not required.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Agree on a shared central argument and outline before or while allocating the paper’s contributions.
  Rationale: Separate sections without a common argument can defeat the explicit single-argument objective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Assign clear contribution responsibilities across the four students with a shared handoff/review arrangement.
  Rationale: A process that never divides responsibility fails the central work-allocation objective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Agree on practical common style conventions or a shared example covering relevant voice, terminology and citation/format choices.
  Rationale: Gives contributors a common drafting reference without prescribing a particular style guide.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): Integrate and revise the contributions together or through an accountable editor/review pass so the final paper has coherent reasoning and a consistent style.
  Rationale: Shared initial instructions alone cannot ensure the independently written sections become one coherent paper.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants retain four contributors to one paper, consistent argument and style. No equal word quota, named collaboration app, compulsory lead author or particular citation style is specified. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC037

procedural_instructional; medium.

### en

Explain how to plan several errands in one afternoon while considering opening hours, travel time, and priority.

### bn

দোকান খোলার সময়, যাতায়াতের সময় এবং অগ্রাধিকার বিবেচনা করে একই বিকেলে কয়েকটি কাজ কীভাবে পরিকল্পনা করবেন তা ব্যাখ্যা করুন।

### bn_cs

opening hours, যাতায়াতের সময় আর priority বিবেচনা করে একই বিকেলে কয়েকটি errand কীভাবে plan করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-04: Input gathering and the resulting scheduling logic are distinct; no invented exact itinerary is required.
- [ ] RIU-04: Review ordinal anchor and allow a valid conditional planning algorithm instead of requiring numeric times that the prompt does not provide.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): List the errands with their relevant opening/closing windows and estimate the time needed to complete each.
  Rationale: Supplies the timing inputs without inventing real opening hours.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Estimate travel times between relevant stops, allowing realistic transitions within the afternoon.
  Rationale: Prevents treating geographically separate errands as simultaneous.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Identify which errands have highest importance or binding deadlines and which may be deferred.
  Rationale: Makes prioritization explicit instead of simply minimizing travel.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): Build a feasible sequence that fits travel and service time inside opening windows and the available afternoon, prioritizing essential errands and deferring lower-priority ones if needed.
  Rationale: A list of inputs without an executable ordering misses the central planning objective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Proposes a meaningful ordering based on either time windows or priorities but does not integrate travel time into feasibility; a route known to violate a stated window would score 0.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. BN names shop opening hours while EN/BN-CS refer to opening hours generally. This does not restrict all errands to purchases. No locations, durations or actual business hours are supplied, so a planning method is sufficient. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC060

procedural_instructional; hard.

### en

An organization handles many appointment requests manually and experiences double-booking. Design a procedure for intake, confirmation, conflict checking, changes, and cancellation.

### bn

একটি প্রতিষ্ঠান অনেক অ্যাপয়েন্টমেন্টের অনুরোধ হাতে হাতে সামলায় এবং প্রায়ই একই সময়ে দুটি বুকিং হয়ে যায়। অনুরোধ গ্রহণ, নিশ্চিতকরণ, সময়ের সংঘাত যাচাই, পরিবর্তন এবং বাতিলের জন্য একটি পদ্ধতি তৈরি করুন।

### bn_cs

একটি প্রতিষ্ঠান অনেক appointment request manually handle করে এবং প্রায়ই double-booking হয়ে যায়। intake, confirmation, conflict checking, change আর cancellation-এর জন্য একটি procedure design করুন।

### Boundary and ambiguity questions

- [ ] RIU-02, RIU-03: Review conflict checking versus committed reservation/confirmation as distinct operational outcomes; no requirement for software locking syntax.
- [ ] RIU-04, RIU-05: Change and cancellation are independently assessable lifecycle paths, not a mandatory platform feature list.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Capture each request’s requester/contact, required service or resource and proposed time/duration in a consistent intake record.
  Rationale: Provides enough information to assess a booking without requiring irrelevant personal data.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Check proposed appointments against the authoritative current schedule and relevant resource/time constraints before committing them, coordinating concurrent requests so one slot is not promised twice.
  Rationale: A stale or independent conflict check leaves the stated double-booking failure unresolved.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Record the committed appointment in the shared schedule and send a clear confirmation of the agreed time/service to the requester.
  Rationale: An unrecorded or ambiguous commitment can create exactly the duplicate booking the procedure is meant to prevent.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Handle requested changes by rechecking the revised slot, updating the authoritative booking and informing the affected parties of the confirmed change.
  Rationale: Prevents changes from bypassing the normal booking controls.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; identified-ambiguity-or-boundary): Handle cancellation by updating the authoritative booking to release the slot and notifying the relevant requester/staff.
  Rationale: Keeps availability accurate after cancellations.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants retain manual high-volume booking and double-booking. A shared authoritative schedule and coordinated confirmation can be manual or digital. No named booking product, staff count or fixed cancellation penalty is required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC092

procedural_instructional; easy.

### en

Describe a simple procedure for what to do if a scheduled speaker cancels shortly before a meeting.

### bn

মিটিংয়ের অল্প আগে নির্ধারিত বক্তা আসতে না পারার কথা জানালে কী করবেন, তার একটি সহজ পদ্ধতি বর্ণনা করুন।

### bn_cs

meeting-এর অল্প আগে scheduled speaker cancel করলে কী করবেন, তার একটি simple procedure describe করুন।

### Boundary and ambiguity questions

- [ ] RIU-02: Accept any feasible alternative; do not require finding a new speaker when none is available.
- [ ] RIU-03, RIU-04: Notification and update of shared meeting records are distinct; a single message/invite update may express both propositions.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Quickly establish what the cancellation affects and whether a replacement, remote contribution or useful agenda adjustment is feasible in the remaining time.
  Rationale: Avoids selecting an unavailable fallback without requiring a detailed investigation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Choose a workable meeting fallback, such as a substitute, revised agenda or reschedule/cancellation, consistent with the remaining time and purpose.
  Rationale: Without an executable fallback the requested cancellation procedure has no operational response.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Promptly tell the organizer and affected attendees the change and any updated time, format or preparation they need.
  Rationale: A fallback without communication can leave attendees following an invalid plan.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Update relevant agenda/invitation/materials to reflect the chosen fallback and coordinate any necessary follow-up.
  Rationale: Keeps meeting records aligned without requiring unnecessary changes if the plan stays intact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants specify little time before the meeting; no fixed replacement speaker, topic, budget or reschedule window is given. Replacement, revised agenda and postponement are alternatives. A procedure need not promise a substitute exists. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN020

information_synthesis; hard.

### en

Compare two models from these results without declaring one universally better: Model A has 92 percent overall accuracy and 78 percent recall on the minority class. Model B has 89 percent overall accuracy and 86 percent minority-class recall. Model B also takes twice as long to run.

### bn

কোনো একটিকে সব ক্ষেত্রে ভালো ঘোষণা না করে এই ফলাফল থেকে দুটি মডেল তুলনা করুন: মডেল A-এর সামগ্রিক নির্ভুলতা ৯২ শতাংশ এবং সংখ্যালঘু শ্রেণিতে রিকল ৭৮ শতাংশ। মডেল B-এর সামগ্রিক নির্ভুলতা ৮৯ শতাংশ এবং সংখ্যালঘু শ্রেণিতে রিকল ৮৬ শতাংশ। এ ছাড়া মডেল B চালাতে দ্বিগুণ সময় লাগে।

### bn_cs

কোনো একটাকে universally better ঘোষণা না করে এই result থেকে দুটি model compare করুন: Model A-এর overall accuracy ৯২ শতাংশ এবং minority class-এ recall ৭৮ শতাংশ। Model B-এর overall accuracy ৮৯ শতাংশ এবং minority-class recall ৮৬ শতাংশ। এ ছাড়া Model B run করতে দ্বিগুণ সময় লাগে।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-02: Keep each relational comparison together; do not separately score every number and duplicate its directional claim.
- [ ] RIU-04: A balanced tradeoff meets the negative constraint without explicitly saying no universal winner; a refusal/nonanswer still scores 0.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): State that A has higher overall accuracy than B: 92% versus 89%, equivalently a 3 percentage-point advantage.
  Rationale: Reversing or omitting this side of the central tradeoff distorts the comparison.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): State that B has higher minority-class recall than A: 86% versus 78%, equivalently an 8 percentage-point advantage.
  Rationale: The minority-class improvement is the main counterweight to A’s overall accuracy.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): State that B takes twice as long to run as A, so A has the runtime advantage.
  Rationale: Omitting the explicitly supplied runtime penalty materially changes the deployment tradeoff.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): Avoid a universal winner and relate any preference to the relative importance of overall accuracy, minority-class recall and runtime.
  Rationale: The prompt explicitly asks for a conditional comparison rather than an all-purpose ranking; one-sided superiority defeats that objective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants retain A 92% accuracy/78% minority recall, B 89%/86%, and B twice A’s runtime. Correct comparisons may state the supplied values or equivalent percentage-point differences. No precision, calibration, statistical significance or fairness conclusion is supplied. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN045

information_synthesis; medium.

### en

Turn this incident note into immediate and follow-up actions: The affected account has been disabled. Logs must be preserved. The user's device needs review. The manager must be informed today. A lessons-learned meeting should occur next week.

### bn

এই ইনসিডেন্ট নোটটিকে তাৎক্ষণিক এবং পরবর্তী করণীয়তে ভাগ করুন: আক্রান্ত অ্যাকাউন্টটি নিষ্ক্রিয় করা হয়েছে। লগগুলো সংরক্ষণ করতে হবে। ব্যবহারকারীর ডিভাইসটি পর্যালোচনা করা দরকার। আজই ম্যানেজারকে জানাতে হবে। আগামী সপ্তাহে শিক্ষণীয় বিষয় নিয়ে একটি মিটিং হওয়া উচিত।

### bn_cs

এই incident note-টাকে immediate আর follow-up action-এ ভাগ করুন: affected account-টা disable করা হয়েছে। log-গুলো preserve করতে হবে। user-এর device-টা review করা দরকার। আজই manager-কে inform করতে হবে। আগামী সপ্তাহে একটি lessons-learned meeting হওয়া উচিত।

### Boundary and ambiguity questions

- [ ] RIU-01: Completed account disablement should be recognized in content but not counted again as a new instruction.
- [ ] RIU-03: The note does not prescribe a precise device-review deadline; accept immediate assessment or an explicit follow-up path that does not ignore it.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary): Recognize that the affected account has already been disabled, rather than presenting disabling it as an outstanding action.
  Rationale: Preserves the completed-versus-pending distinction without requiring re-disabling.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Include preservation of the incident logs as an immediate action.
  Rationale: Delayed or omitted preservation risks losing the evidence the note explicitly requires.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary): Include a review of the user’s device among the remaining actions.
  Rationale: Retains the explicit device task without inventing findings or a precise deadline.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Include informing the manager today among the immediate actions.
  Rationale: Omission or changing the stated deadline defeats the note’s time-bound notification.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Include a lessons-learned meeting next week among follow-up actions.
  Rationale: Preserves the future learning task and its supplied timing.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants distinguish the already-disabled account from outstanding actions. Disabling it again is not a new required step. Device review may begin immediately or be staged, but no later deadline than supplied should be invented. Next-week meeting remains a follow-up. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
- [ ] CHECK-02: Present actions in distinguishable immediate and follow-up groups or equivalently clear temporal organization; labels may vary and no specific table layout is required. Content facts and deadlines remain RIUs.

## SYN053

information_synthesis; easy.

### en

One report says a task is complete. Another says one approval is still pending. Explain why the status should not simply be labeled complete and what should be clarified.

### bn

একটি রিপোর্ট বলছে একটি কাজ সম্পন্ন হয়েছে। আরেকটি বলছে একটি অনুমোদন এখনো বাকি। কেন অবস্থাটিকে সরাসরি সম্পন্ন বলে চিহ্নিত করা উচিত নয় এবং কী স্পষ্ট করা দরকার তা ব্যাখ্যা করুন।

### bn_cs

একটি report বলছে একটি task complete হয়েছে। আরেকটি বলছে একটি approval এখনো pending। কেন status-টাকে সরাসরি complete label করা উচিত নয় এবং কী clarify করা দরকার তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-02: Withhold unconditional completion without assuming every administrative approval always blocks all definitions of completion.
- [ ] RIU-03: Do not require a fabricated approver identity or assert that approval has been granted.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Explain that the pending approval means unconditional completion is not yet established, even if the underlying work is reported finished.
  Rationale: Ignoring the unresolved gate materially misstates the status.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; identified-ambiguity-or-boundary): Clarify what each report means by complete and whether the pending approval is required for final completion or only a separate administrative step.
  Rationale: Resolves the differing status definitions without inventing the approval’s authority.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Identify which approval is pending and obtain its current disposition or confirmation from the responsible source before closing the status.
  Rationale: Makes the needed clarification operational without imposing a deadline or named owner.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants preserve conflicting completion/approval reports. An approval may be a completion gate but its scope is unknown; do not presume it is irrelevant or automatically equate work completion with authorized closure. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN065

information_synthesis; medium.

### en

After a new workflow launched, processing time improved and staff satisfaction declined. Explain why the evidence supports two separate outcomes rather than one overall verdict.

### bn

নতুন একটি ওয়ার্কফ্লো চালুর পর প্রসেসিং টাইম উন্নত হয়েছে এবং কর্মীদের সন্তুষ্টি কমেছে। কেন প্রমাণগুলো একটি সামগ্রিক রায়ের বদলে দুটি আলাদা ফলাফল সমর্থন করে তা ব্যাখ্যা করুন।

### bn_cs

নতুন একটি workflow launch হওয়ার পর processing time improve হয়েছে এবং staff satisfaction কমেছে। কেন evidence-গুলো একটি overall verdict-এর বদলে দুটি আলাদা outcome support করে তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-03: A complete interpretation must distinguish outcome dimensions; do not require a formal utility function or assert the launch caused either change.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): State that processing time improved after the workflow launch.
  Rationale: Losing the positive efficiency result materially distorts the supplied evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that staff satisfaction declined after the workflow launch.
  Rationale: Losing the negative staff outcome materially distorts the supplied evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Explain that processing time and satisfaction are different outcome dimensions, so evidence of improvement in one and worsening in the other does not by itself establish one overall success/failure verdict.
  Rationale: Simply listing the two results without their distinct-outcome implication misses the central explanation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants use temporal after-launch wording, which does not by itself prove workflow causation. The task asks for separate outcomes rather than a weighted aggregate verdict; no weight scheme or new data is available. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN077

information_synthesis; medium.

### en

A release can proceed only if no critical bugs remain, backups are verified, and rollback is tested. There are zero critical bugs, backups are verified, but rollback testing failed. State whether release criteria are met and why.

### bn

একটি রিলিজ এগোতে পারবে কেবল তখনই, যদি কোনো গুরুতর বাগ না থাকে, ব্যাকআপ যাচাই করা থাকে এবং রোলব্যাক টেস্ট করা থাকে। গুরুতর বাগের সংখ্যা শূন্য, ব্যাকআপ যাচাই করা হয়েছে, কিন্তু রোলব্যাক টেস্ট ব্যর্থ হয়েছে। রিলিজের মানদণ্ড পূরণ হয়েছে কি না এবং কেন, তা উল্লেখ করুন।

### bn_cs

একটি release proceed করতে পারবে কেবল তখনই, যদি কোনো critical bug না থাকে, backup verify করা থাকে এবং rollback test করা থাকে। critical bug-এর সংখ্যা শূন্য, backup verify করা হয়েছে, কিন্তু rollback testing fail করেছে। release criteria পূরণ হয়েছে কি না এবং কেন, তা উল্লেখ করুন।

### Boundary and ambiguity questions

- [ ] RIU-03: EN/BN/BN-CS all say rollback is tested then explicitly that testing failed; review the operational reading that passing readiness, rather than mere test execution, is required.
- [ ] RIU-03, RIU-04: Failed-condition evidence and no-go conclusion are distinct; do not require an invented rollback repair procedure.

### RIU checklist

- [ ] **RIU-01** (supporting; prespecified-ordinary-sample): Recognize that the no-critical-bug condition is satisfied because there are zero critical bugs.
  Rationale: Retains one supplied satisfied condition without making it decisive alone.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Recognize that the backup-verification condition is satisfied.
  Rationale: Retains the other satisfied condition separately from rollback readiness.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Explain that failed rollback testing leaves the rollback condition unsatisfied, even though the test was attempted.
  Rationale: Treating attempted but failed testing as sufficient reverses the operational release criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): Conclude that the release criteria are not met and release should not proceed under the stated all-conditions rule.
  Rationale: The task’s central conjunction decision must be no-go, not a majority vote across conditions.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants preserve zero critical bugs, verified backups and failed rollback testing. The fact that testing occurred is insufficient: failed testing does not establish a usable rollback. No extra approval gate is introduced. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH036

technical_troubleshooting; medium.

### en

An update statement affects far more rows than expected in a test environment. Explain what should be reviewed before the statement is ever used in production.

### bn

টেস্ট এনভায়রনমেন্টে একটি আপডেট স্টেটমেন্ট প্রত্যাশার চেয়ে অনেক বেশি সারিকে প্রভাবিত করেছে। প্রোডাকশনে কখনো ব্যবহার করার আগে কী কী পর্যালোচনা করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

test environment-এ একটি update statement প্রত্যাশার চেয়ে অনেক বেশি row affect করেছে। production-এ কখনো use করার আগে কী কী review করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-02: Scope logic and data/parameter validation are separately assessable; do not mandate every WHERE/join/subquery example.
- [ ] RIU-04: A test-only or non-destructive review path meets the conditional safety requirement; no obligation to execute a live transaction or restore backup now.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Review and correct the update’s row-selection logic, including the WHERE condition and any joins/subquery scope, against the intended target set.
  Rationale: The observed excessive row impact points to a scope failure that could materially corrupt production data.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; identified-ambiguity-or-boundary): Verify relevant parameters, data assumptions and expected row count using a non-destructive preview or equivalent test against representative data.
  Rationale: Checks that the corrected logic selects the intended records without requiring an invented numeric count.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Review relevant triggers, cascades or other indirect effects if they could explain the larger-than-expected change.
  Rationale: Tests indirect causes without assuming triggers exist or requiring an exhaustive database audit.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): Do not use the statement in production until its scope and effects are verified; any eventual production application must have proportionate rollback/recovery protection.
  Rationale: Executing an unverified broad update risks irreversible material data corruption; a verified diagnostic-only plan satisfies the production hold without reciting an unused rollback command.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants preserve that excessive impact happened in test and production use has not occurred. No SQL statement or schema is supplied. A SELECT preview or an equivalent non-destructive verification may be valid; no specific SQL dialect is required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH050

technical_troubleshooting; hard.

### en

A production API shows a gradual increase in response time over several hours and returns to normal after restart. Propose an investigation focused on resource leaks, connection pools, caching, background work, and observability data.

### bn

প্রোডাকশনে চলা একটি এপিআইয়ের সাড়া দেওয়ার সময় কয়েক ঘণ্টা ধরে ধীরে ধীরে বাড়তে থাকে এবং রিস্টার্ট করার পর আবার স্বাভাবিক হয়ে যায়। রিসোর্স লিক, কানেকশন পুল, ক্যাশিং, ব্যাকগ্রাউন্ডে চলা কাজ এবং অবজারভেবিলিটি ডেটাকে কেন্দ্র করে একটি অনুসন্ধান পরিকল্পনা প্রস্তাব করুন।

### bn_cs

production-এ চলা একটি API-র response time কয়েক ঘণ্টা ধরে ধীরে ধীরে বাড়তে থাকে এবং restart করার পর আবার স্বাভাবিক হয়ে যায়। resource leak, connection pool, caching, background work আর observability data-কে focus করে একটি investigation plan propose করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-05: Resource-specific leak evidence and a cross-signal time series are distinct; the same memory metric alone cannot fully satisfy observability correlation.
- [ ] RIU-06: Review critical and ordinal boundaries; a specific evidence-to-cause test is required, not proving all five hypotheses or conducting unsafe production stress.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary): Inspect time-correlated resource growth or unreleased resources across the slowdown, such as memory, handles, threads or objects, and compare with the restart reset.
  Rationale: Tests resource leakage rather than treating the restart pattern as a confirmed diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Inspect connection-pool utilization, waits, exhaustion and release behavior as latency grows.
  Rationale: Tests the separately named connection-pool mechanism.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Inspect cache size/eviction, hit/miss behavior or stale/accumulating entries over the slowdown period.
  Rationale: Tests the separately named caching mechanism without assuming that a larger cache always helps.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Correlate background jobs, queues or periodic work and their resource demand with worsening latency.
  Rationale: Tests background contention separately from request-path or pool behavior.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; identified-ambiguity-or-boundary): Collect and correlate request latency/throughput with relevant metrics, logs or traces before and after restart so candidate mechanisms can be compared over time.
  Rationale: Provides the requested observability basis without mandating every telemetry tool.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical, identified-ambiguity-or-boundary): Use the correlated evidence and controlled follow-up tests to distinguish the candidate causes rather than accepting restart relief as proof of one cause or as the permanent fix.
  Rationale: A list of metrics without a result-to-hypothesis investigation fails the central diagnostic objective.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Links a specific observed growth/wait/cache/job signal to at least one testable cause but does not specify a comparison or follow-up test to distinguish it from alternatives.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants preserve hours-long worsening and temporary restart relief. This pattern suggests accumulating state but does not prove a memory leak. No particular tracing vendor, database or scheduled-restart workaround is required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH066

technical_troubleshooting; medium.

### en

A newly installed memory module is recognized but the system becomes unstable. Explain the checks you would make before concluding the module is defective.

### bn

নতুন লাগানো একটি মেমরি মডিউল শনাক্ত হচ্ছে, কিন্তু সিস্টেম অস্থিতিশীল হয়ে গেছে। মডিউলটি ত্রুটিপূর্ণ—এই উপসংহারে পৌঁছানোর আগে কী কী চেক করবেন তা ব্যাখ্যা করুন।

### bn_cs

নতুন install করা একটি memory module recognize হচ্ছে, কিন্তু system unstable হয়ে গেছে। module-টা defective—এই conclusion-এ যাওয়ার আগে কী কী check করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-03: Physical compatibility and configured operating settings are distinct; do not assume any particular generation of RAM.
- [ ] RIU-02: Safe handling is conditional on physical access; an evidence-only diagnostic path need not repeat irrelevant hardware disassembly warnings.
- [ ] RIU-04: Diagnostic restraint should not become a compulsory assertion of one proven cause; accept appropriate module/slot or stability comparisons.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary): Check the module’s supported type, capacity, speed/voltage and population requirements against the system and any existing memory.
  Rationale: Tests compatibility despite successful recognition without requiring every specification as a separate fact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; identified-ambiguity-or-boundary): Check seating and the correct slot/population arrangement using safe power-off handling if physical reseating is proposed.
  Rationale: Tests installation as an alternative cause without forcing needless invasive work.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary): Check memory/firmware configuration, including unstable overclock or timing profiles, against supported stable settings.
  Rationale: Tests configuration-related instability rather than assuming a defective part.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Run an appropriate memory stability test or controlled comparison of modules/slots and interpret whether the instability follows the module, slot or configuration.
  Rationale: Obtains discriminating evidence before concluding the module is defective; no particular test brand or fixed duration is required.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants preserve that the module is recognized and instability follows installation. Recognition alone proves neither full compatibility nor a defect. Physical checks require a powered-down, disconnected and static-conscious path if proposed; no opening a powered system. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH082

technical_troubleshooting; easy.

### en

A spreadsheet contains numbers that are being treated as text. Describe simple checks to identify why.

### bn

একটি স্প্রেডশিটের সংখ্যাগুলোকে টেক্সট হিসেবে ধরা হচ্ছে। কেন এমন হচ্ছে তা শনাক্ত করতে কোন কোন সহজ চেক করা যায় তা বর্ণনা করুন।

### bn_cs

একটি spreadsheet-এর number-গুলোকে text হিসেবে treat করা হচ্ছে। কেন এমন হচ্ছে তা identify করতে কোন কোন সহজ check করা যায় তা describe করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-04: A displayed numeric format is not proof of numeric storage; a small test is supporting, not a compulsory repair of the whole sheet.
- [ ] RIU-02, RIU-03: Character contamination and locale/separator mismatch are distinct diagnostic routes; do not require all examples or assume a specific locale.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary): Check the affected cells’ stored type and formatting against cells recognized as numbers, including whether text format or import settings were applied.
  Rationale: Distinguishes cell representation/import handling from the number’s visible appearance.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; identified-ambiguity-or-boundary): Inspect the underlying cell contents for text-forcing characters or contamination, such as a leading apostrophe, whitespace or pasted nonnumeric characters.
  Rationale: Tests a distinct content-level cause without requiring every possible character.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Check whether decimal/grouping separators or regional/import conventions differ from the spreadsheet’s expected numeric format.
  Rationale: Tests a common parsing mismatch separately from text-forcing prefixes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Use a small reversible comparison or conversion test to see which suspected cause makes the value recognized as numeric before applying broad changes.
  Rationale: Connects the checks to diagnosis without requiring destructive mass editing or a fixed formula.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants request identifying why, not compulsory bulk conversion or a particular spreadsheet product. A format-only change may fail to convert stored text and must not be asserted to guarantee conversion. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH096

technical_troubleshooting; medium.

### en

A scanner produces faded images only from one computer. Describe how to separate scanner hardware, driver, application profile, and image-setting causes.

### bn

একটি স্ক্যানার শুধু একটি নির্দিষ্ট কম্পিউটার থেকে স্ক্যান করলে ফ্যাকাশে ছবি দিচ্ছে। স্ক্যানারের হার্ডওয়্যার, ড্রাইভার, অ্যাপ্লিকেশন প্রোফাইল এবং ছবির সেটিংস—কোনটি কারণ তা কীভাবে আলাদা করবেন বর্ণনা করুন।

### bn_cs

একটি scanner শুধু একটি নির্দিষ্ট computer থেকে scan করলে faded image দিচ্ছে। scanner hardware, driver, application profile আর image setting—কোনটা কারণ তা কীভাবে আলাদা করবেন describe করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-05: The controlled cross-computer test and its causal interpretation earn separate credit only when the response supplies both propositions.
- [ ] RIU-03, RIU-04: Application profiles can contain image settings; confirm the two units target application-specific behavior versus direct image controls without requiring duplicate resets.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary): Compare the same source and scanner across the affected and a known-working computer, keeping relevant settings comparable to test whether the fault follows the host or scanner.
  Rationale: Uses the defining one-computer contrast without assuming hardware can never be involved.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Compare the affected computer’s scanner driver/version/configuration with a supported or known-working setup.
  Rationale: Tests the named driver cause independently of hardware.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Compare an alternate scanning application or a neutral/reset application profile to test whether fading follows an application-specific profile.
  Rationale: Separates application configuration from the shared scanner driver.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Check relevant image settings such as brightness, contrast, color mode or automatic correction and compare a controlled scan with appropriate defaults.
  Rationale: Tests direct image-processing settings without requiring every listed control.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical, identified-ambiguity-or-boundary): Interpret the controlled comparisons to distinguish scanner hardware from host driver, application-profile and image-setting explanations rather than replacing hardware solely because scans are faded.
  Rationale: The prompt asks to separate causes; a disconnected checklist without result-to-cause reasoning does not accomplish that.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Explains the hardware-versus-host implication of a controlled cross-computer comparison but does not connect additional driver/application/setting comparisons to a more specific cause.

Draft notes: P01 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All variants preserve faded output on only one computer. Hardware is less likely but not logically excluded. No model-specific calibration utility, replacement scanner or driver reinstall is compulsory. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
