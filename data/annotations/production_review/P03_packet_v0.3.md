# P03 independent review packet

Status: pending. AI-produced draft annotations; no human acceptance is claimed.

Each task needs bilingual equivalence and full-prompt coverage review. Review all critical units, all ambiguity/boundary questions below, and every prespecified ordinary sample item. Additional ordinary units may be reviewed. Blank identity/decision fields are intentional.

25 tasks; 129 RIUs; 57 critical; 22 ordinary sample units; 89 mandatory unit reviews.

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

## CYBER005

cybersecurity_digital_safety; medium.

### en

An employee's account was locked after many failed login attempts. Describe the evidence that should be checked before deciding whether the cause was user error or an attack.

### bn

অনেকবার ব্যর্থ লগইন চেষ্টার পর একজন কর্মীর অ্যাকাউন্ট লক হয়ে গেছে। কারণটি ব্যবহারকারীর ভুল নাকি কোনো আক্রমণ—এই সিদ্ধান্ত নেওয়ার আগে কোন কোন প্রমাণ যাচাই করা উচিত তা বর্ণনা করুন।

### bn_cs

অনেকবার failed login attempt-এর পর একজন employee-র account lock হয়ে গেছে। কারণটা user error নাকি কোনো attack—এই decision নেওয়ার আগে কোন কোন প্রমাণ check করা উচিত তা describe করুন।

### Boundary and ambiguity questions

- [ ] RIU-02, RIU-04: Boundary: attempts against multiple accounts can be pattern evidence (RIU-02) or related-signal evidence (RIU-04); reviewers should accept either placement without double credit for a single phrase.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Check the source of the failed attempts, such as IP addresses, locations or devices, and whether they match the employee's usual ones.
  Rationale: The main discriminator between user error and an external attack.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Examine the pattern and timing of attempts, such as many rapid attempts, attempts outside working hours or attempts against multiple accounts.
  Rationale: Distinguishes scripted attacks from a user repeatedly mistyping.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Ask or verify with the employee whether they recently changed their password or have a device or app still using an old password.
  Rationale: A common benign cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Check for related signals such as any successful login after the failures, password-reset requests or similar lockouts for other accounts.
  Rationale: Indicates whether the account may already be compromised.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Reserve the user-error versus attack conclusion until the evidence has been reviewed.
  Rationale: The prompt asks for evidence before deciding.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Alternative indicators are acceptable; no particular log system is required. Multiple-account attempts may be met in RIU-02 or RIU-04 but count once per unit. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER016

cybersecurity_digital_safety; medium.

### en

A user clicked a suspicious link but did not enter any information. Explain what risk remains and what actions are reasonable next steps.

### bn

একজন ব্যবহারকারী একটি সন্দেহজনক লিংকে ক্লিক করেছেন, কিন্তু কোনো তথ্য দেননি। এরপরও কী ঝুঁকি থেকে যায় এবং পরবর্তী কোন পদক্ষেপগুলো যুক্তিসংগত তা ব্যাখ্যা করুন।

### bn_cs

একজন user একটি suspicious link-এ click করেছেন, কিন্তু কোনো information দেননি। এরপরও কী risk থেকে যায় এবং পরবর্তী কোন পদক্ষেপগুলো reasonable তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-04: Check that "scan the device" via IT counts as met.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that some risk remains even without entering information, such as a drive-by download, browser exploit or confirming the address to attackers.
  Rationale: The prompt asks what risk remains.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Indicate that the risk is usually lower than if credentials or data had been entered.
  Rationale: Avoids overstating the risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Report the click to IT or security, or follow the organization's reporting procedure.
  Rationale: Enables investigation and protection of others.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Run or request a malware scan or device check, and keep the system and browser updated.
  Rationale: Detects anything delivered by the visit.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Watch for follow-up signs such as unexpected downloads, pop-ups or account alerts, and change passwords if anything was entered after all.
  Rationale: Covers delayed indicators.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Personal and workplace contexts are both acceptable; reporting may be to IT or the relevant service. No requirement to disconnect the device unless symptoms appear. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER025

cybersecurity_digital_safety; medium.

### en

An employee wants to install unapproved software to complete a work task faster. Explain the security concerns and a practical way to handle the request.

### bn

একজন কর্মী কাজ দ্রুত শেষ করতে অনুমোদনহীন একটি সফটওয়্যার ইনস্টল করতে চান। এর নিরাপত্তা-উদ্বেগগুলো এবং অনুরোধটি সামলানোর একটি বাস্তবসম্মত উপায় ব্যাখ্যা করুন।

### bn_cs

একজন employee কাজ দ্রুত শেষ করতে unapproved একটি software install করতে চান। এর security concern-গুলো আর request-টা handle করার একটি practical উপায় explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-05: Negative constraint: check that silence passes when the proposed path is review-first.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that unapproved software may be malicious, vulnerable or unpatched, or may come from an untrusted source.
  Rationale: The primary security concern.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Mention data-handling or compliance concerns, such as the software sending work data to third parties or violating licensing.
  Rationale: A second, distinct concern.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Route the request through IT or security review instead of installing it unilaterally.
  Rationale: The practical handling path the prompt requires.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Offer a way to meet the business need, such as an approved alternative or expedited review.
  Rationale: Addresses the employee's legitimate goal.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; identified-ambiguity-or-boundary): Do not advise installing the software before approval; a review-first path complies without restating this.
  Rationale: Installation before review defeats the control.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. The practical path may be a formal request, a sandboxed evaluation or an approved equivalent. Blanket prohibition without addressing the need is insufficient for RIU-04 only. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER042

cybersecurity_digital_safety; easy.

### en

A team keeps confidential files in a shared folder that everyone in the department can open. Explain why access should be reviewed.

### bn

একটি টিম গোপনীয় ফাইলগুলো এমন একটি শেয়ার করা ফোল্ডারে রাখে, যেটি বিভাগের সবাই খুলতে পারে। কেন অ্যাক্সেস রিভিউ করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি team confidential file-গুলো এমন একটি shared folder-এ রাখে, যেটা department-এর সবাই open করতে পারে। কেন access review করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-03, RIU-04: Check that a "why" answer is not penalized for lacking a detailed procedure; only the least-privilege direction and recurring review are required.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that department-wide access exposes confidential files to people who do not need them, increasing the risk of unauthorized viewing, leakage or misuse.
  Rationale: This is the core reason the review is needed.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Explain that broad access makes it harder to trace who viewed or changed files, or to limit damage from a compromised or departing account.
  Rationale: Adds the accountability and blast-radius dimension.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary): Indicate that a review should restrict access to people or roles with a business need (least privilege).
  Rationale: Connects the explanation to the purpose of a review.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Mention that access should be reviewed periodically or when roles change, not only once.
  Rationale: Access drifts as people join, move or leave.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. The prompt asks why, not for a full procedure; a brief least-privilege direction suffices. No specific platform, regulation or review frequency is required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## CYBER050

cybersecurity_digital_safety; hard.

### en

A company suspects sensitive records may have been copied by an authorized employee before departure. Explain how to investigate access and transfer activity while avoiding unsupported assumptions about intent.

### bn

একটি প্রতিষ্ঠান সন্দেহ করছে, অনুমোদিত অ্যাক্সেস থাকা একজন কর্মী চাকরি ছাড়ার আগে সংবেদনশীল রেকর্ড কপি করে থাকতে পারেন। উদ্দেশ্য নিয়ে ভিত্তিহীন অনুমান এড়িয়ে অ্যাক্সেস ও ডেটা স্থানান্তরের কার্যকলাপ কীভাবে তদন্ত করবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি company সন্দেহ করছে, authorized একজন employee চাকরি ছাড়ার আগে sensitive record copy করে থাকতে পারেন। intent নিয়ে unsupported assumption এড়িয়ে access আর transfer activity কীভাবে investigate করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-03: Confirm that hedged language about suspicion without a legitimate-use check is insufficient, while a clear separation of activity from intent passes.
- [ ] RIU-01, RIU-02: Access review and transfer-channel review are distinct units; a single sentence may meet both only if it names transfer evidence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Review access and activity logs for the records in question (what was accessed, when and from which accounts or devices), compared against the employee's normal pattern.
  Rationale: Establishes whether unusual access occurred.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Examine transfer channels such as downloads, email to external addresses, removable media, printing, cloud uploads or sync, as available.
  Rationale: Access alone does not show copying or removal.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Do not treat access or transfer evidence as proof of malicious intent; consider legitimate job-related explanations and report findings as facts about activity.
  Rationale: The prompt explicitly requires avoiding unsupported assumptions about intent.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Preserve logs and relevant evidence before they expire or are overwritten, with documented handling.
  Rationale: Evidence may be lost or challenged otherwise.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Involve appropriate functions such as HR, legal or privacy before interviews or action against the employee.
  Rationale: Investigations of individuals have legal and fairness implications.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; prespecified-ordinary-sample): Use findings to scope impact and containment, such as which records were affected and whether access is revoked.
  Rationale: Turns investigation into a decision.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Mentions containment or impact generically without linking it to what the evidence shows.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Authorized access is part of the premise; the answer must separate activity evidence from intent. No specific DLP or SIEM product is required. Device-forensics examples are alternatives. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC044

decision_support; medium.

### en

A traveler has three hotel options: one cheapest but nonrefundable, one flexible but farther away, and one central but most expensive. Explain how to choose based on uncertainty and priorities.

### bn

একজন যাত্রীর সামনে তিনটি হোটেলের বিকল্প আছে: একটি সবচেয়ে সস্তা কিন্তু টাকা ফেরতযোগ্য নয়, একটি শর্তে নমনীয় কিন্তু বেশি দূরে, আর একটি শহরের কেন্দ্রে কিন্তু সবচেয়ে দামি। অনিশ্চয়তা ও নিজের অগ্রাধিকারের ভিত্তিতে কীভাবে বেছে নেবেন তা ব্যাখ্যা করুন।

### bn_cs

একজন traveler-এর সামনে তিনটি hotel option আছে: একটি সবচেয়ে সস্তা কিন্তু nonrefundable, একটি flexible কিন্তু বেশি দূরে, আর একটি central কিন্তু সবচেয়ে দামি। uncertainty আর priority-র ভিত্তিতে কীভাবে choose করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-02, RIU-04: Check overlap: RIU-02 requires a comparison across all three dimensions; RIU-04 is the narrower point that distance has a cost.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Assess how likely the plans are to change, linking higher uncertainty to the value of the flexible option.
  Rationale: Uncertainty is the stated decision basis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Compare the options on cost, flexibility and location (travel time or cost from the distant hotel) together.
  Rationale: The three options trade off these dimensions.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Relate the choice to the traveler's priorities, such as budget, convenience or schedule.
  Rationale: Priorities are a stated basis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Account for the real cost of the distant hotel, such as transport cost or time, when comparing it with the central hotel.
  Rationale: Headline prices mislead.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Mentions distance as a drawback without considering its cost or time.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. No single correct choice is required; the answer should give a method. Numeric expected-cost calculations are optional. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC055

decision_support; medium.

### en

A project sponsor asks for a new feature one week before launch. Explain how to evaluate the request without automatically saying yes or no.

### bn

চালু হওয়ার এক সপ্তাহ আগে প্রজেক্টের স্পনসর একটি নতুন ফিচার চেয়েছেন। আপনাআপনি হ্যাঁ বা না না বলে অনুরোধটি কীভাবে মূল্যায়ন করবেন তা ব্যাখ্যা করুন।

### bn_cs

launch-এর এক সপ্তাহ আগে project sponsor একটি নতুন feature চেয়েছেন। আপনাআপনি হ্যাঁ বা না না বলে request-টা কীভাবে evaluate করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Clarify the value and urgency of the feature, including whether it is needed at launch or can follow later.
  Rationale: Determines whether the request justifies risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Estimate the effort and risk to the launch, including testing time and effects on existing work.
  Rationale: The main constraint one week before launch.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Identify options beyond yes or no, such as a reduced version, a post-launch release or a trade-off with other scope.
  Rationale: The prompt rules out automatic yes or no.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Make the trade-off explicit to the sponsor and agree a decision with the relevant stakeholders.
  Rationale: Ensures an informed, shared decision.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Do not commit to the feature before assessing its impact on the launch; an assessment-first path complies.
  Rationale: Committing first defeats the evaluation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Any reasonable estimation method is acceptable. A decision recommendation is not required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC064

decision_support; medium.

### en

A survey has 1,000 responses but one subgroup contains only 15 respondents. Explain how that should affect interpretation of subgroup comparisons.

### bn

একটি জরিপে ১,০০০টি উত্তর আছে, কিন্তু একটি উপগোষ্ঠীতে মাত্র ১৫ জন উত্তরদাতা। উপগোষ্ঠীগুলোর মধ্যে তুলনার ব্যাখ্যায় এটি কীভাবে প্রভাব ফেলা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি survey-তে ১,০০০টি response আছে, কিন্তু একটি subgroup-এ মাত্র ১৫ জন respondent। subgroup comparison-এর interpretation-এ এটা কীভাবে প্রভাব ফেলা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that results for 15 respondents are highly uncertain: small differences can arise by chance and estimates can change substantially with a few responses.
  Rationale: The core statistical point.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Advise against strong or definitive conclusions about differences between this subgroup and others.
  Rationale: Prevents the central misinterpretation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Suggest reporting uncertainty, for example confidence intervals or the subgroup size, alongside the results.
  Rationale: Makes the limitation visible.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Note that the overall 1,000 responses do not make the small subgroup estimate reliable.
  Rationale: A common misconception.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Suggest options such as collecting more data, combining categories or treating the result as exploratory.
  Rationale: Constructive next steps.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Statistical-test terminology is optional. Representativeness concerns are acceptable additions but not required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC082

decision_support; easy.

### en

A simple approval process requires three signatures even for low-risk purchases. Explain what should be considered before simplifying it.

### bn

একটি সাধারণ অনুমোদন প্রক্রিয়ায় কম ঝুঁকির কেনাকাটাতেও তিনটি স্বাক্ষর লাগে। প্রক্রিয়াটি সহজ করার আগে কী কী বিবেচনা করা উচিত তা ব্যাখ্যা করুন।

### bn_cs

একটি সাধারণ approval process-এ low-risk purchase-এও তিনটি signature লাগে। process-টা simplify করার আগে কী কী বিবেচনা করা উচিত তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Define what counts as low-risk, for example by amount, vendor or category, before changing the rule.
  Rationale: Simplification depends on a clear risk boundary.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Consider why the three signatures exist, such as fraud prevention, budget control or compliance requirements.
  Rationale: Removing a control without understanding its purpose can create risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Weigh the cost of delay and staff time against the risk the extra signatures reduce.
  Rationale: The core trade-off.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Keep a compensating control for simplified purchases, such as spending limits, audit sampling or after-the-fact review.
  Rationale: Maintains oversight.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Pilot or monitor the simplified process to check for misuse or errors.
  Rationale: Evidence that the change works.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. No specific threshold is required. Regulatory requirements are an example of control purpose, not a separate unit. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## DEC090

decision_support; hard.

### en

A department is considering replacing manual approvals with automated rules. Propose criteria for deciding which decisions can be automated and which still require human judgment.

### bn

একটি বিভাগ হাতে করা অনুমোদনের বদলে স্বয়ংক্রিয় নিয়ম চালুর কথা ভাবছে। কোন সিদ্ধান্তগুলো অটোমেট করা যায় আর কোনগুলোতে এখনো মানুষের বিচারবুদ্ধি দরকার, তা ঠিক করার মানদণ্ড প্রস্তাব করুন।

### bn_cs

একটি department manual approval-এর বদলে automated rule চালুর কথা ভাবছে। কোন decision-গুলো automate করা যায় আর কোনগুলোতে এখনো human judgment দরকার, তা ঠিক করার criteria propose করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-03: Boundary between rule clarity (RIU-01) and exceptions (RIU-03): accept separate credit only if the answer addresses both routine clarity and edge-case handling.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Include a criterion based on how clear, rule-based and consistent the decision is (well-defined inputs and thresholds favor automation).
  Rationale: The central automation criterion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Include a criterion based on the impact or risk of a wrong decision, keeping high-impact or irreversible decisions for humans.
  Rationale: Prevents automating decisions whose errors are costly.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; identified-ambiguity-or-boundary): Include exceptions, ambiguity or context-dependence as reasons to require human judgment.
  Rationale: Edge cases need judgment.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Consider data quality and availability for the automated rule.
  Rationale: Rules fail on poor inputs.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Provide oversight for automated decisions, such as escalation paths, audit sampling or periodic review of outcomes.
  Rationale: Automation still needs monitoring.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Mentions monitoring or review only generically without a mechanism such as escalation or sampling.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Consider fairness, accountability or regulatory requirements that may require a human decision-maker.
  Rationale: Some decisions must remain explainable or human.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Criteria may be phrased as questions or a matrix. Volume or frequency may support a criterion but is not separately required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC007

procedural_instructional; medium.

### en

Explain how to create a simple document-review workflow where one person drafts, another reviews, and a final version is clearly approved.

### bn

ডকুমেন্ট রিভিউয়ের একটি সহজ ওয়ার্কফ্লো কীভাবে তৈরি করা যায় তা ব্যাখ্যা করুন, যেখানে একজন খসড়া লিখবেন, আরেকজন রিভিউ করবেন এবং চূড়ান্ত সংস্করণটি স্পষ্টভাবে অনুমোদিত হবে।

### bn_cs

document review-র একটি সহজ workflow কীভাবে তৈরি করা যায় তা explain করুন, যেখানে একজন draft লিখবেন, আরেকজন review করবেন এবং final version-টা স্পষ্টভাবে approve হবে।

### Boundary and ambiguity questions

- [ ] RIU-01: The prompt names two people plus approval; accept the reviewer also approving if roles are explicit.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Assign distinct roles for drafter, reviewer and approver.
  Rationale: The workflow structure the prompt specifies.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Provide a review step where the reviewer gives feedback and the drafter revises.
  Rationale: The review cycle.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Mark the final approved version clearly, such as with an approval record, status label or locked final file.
  Rationale: The prompt requires a clearly approved final version.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Use version naming or tracking so drafts are not confused with the final.
  Rationale: Prevents using the wrong version.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Store the workflow and documents in a shared location everyone uses.
  Rationale: Practical coordination.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Approver may be the reviewer or a third person if stated clearly. Tool choice is open. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC016

procedural_instructional; medium.

### en

A team receives requests through email, chat, and verbal conversations. Design a simple intake procedure so requests are not lost or duplicated.

### bn

একটি টিম ইমেইল, চ্যাট এবং মুখে মুখে কথোপকথনের মাধ্যমে বিভিন্ন অনুরোধ পায়। অনুরোধ যেন হারিয়ে না যায় বা দুবার না আসে, সেজন্য অনুরোধ গ্রহণের একটি সহজ পদ্ধতি তৈরি করুন।

### bn_cs

একটি team email, chat আর মুখে মুখে কথোপকথনের মাধ্যমে বিভিন্ন request পায়। request যেন হারিয়ে না যায় বা duplicate না হয়, সেজন্য একটি simple intake procedure design করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Record every request in one central place such as a tracker, shared list or ticket system, regardless of channel.
  Rationale: Prevents loss.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Check for duplicates before adding a request, for example by searching existing entries or linking related requests.
  Rationale: Prevents duplication.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Capture verbal requests by writing them into the central place promptly.
  Rationale: Verbal requests are the most easily lost.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Assign an owner and status to each request.
  Rationale: Ensures follow-up.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Acknowledge or confirm receipt to the requester.
  Rationale: Reduces repeat requests.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Any tool is acceptable. RIU-03 is separate because verbal capture is a distinct failure point. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC028

procedural_instructional; medium.

### en

A research team is preparing a dataset for publication. Design a release procedure covering documentation, licensing, sensitive information, versioning, validation, and reproducibility.

### bn

একটি গবেষক দল প্রকাশের জন্য একটি ডেটাসেট প্রস্তুত করছে। ডকুমেন্টেশন, লাইসেন্স, সংবেদনশীল তথ্য, ভার্সনিং, যাচাই এবং পুনরুৎপাদনযোগ্যতা অন্তর্ভুক্ত করে একটি প্রকাশ-প্রক্রিয়া তৈরি করুন।

### bn_cs

একটি গবেষক দল প্রকাশের জন্য একটি dataset তৈরি করছে। documentation, licensing, সংবেদনশীল তথ্য, versioning, যাচাই আর reproducibility অন্তর্ভুক্ত করে প্রকাশের একটি procedure design করুন।

### Boundary and ambiguity questions

- [ ] RIU-04, RIU-05, RIU-06: Criticality boundary for explicitly listed components; confirm supporting labels.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Prepare documentation such as a data dictionary, collection methods and known limitations.
  Rationale: An explicit component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Choose and state a license or terms of use.
  Rationale: An explicit component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Review and remove or protect sensitive information, such as de-identifying data and checking re-identification risk or consent.
  Rationale: An explicit component with privacy risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; identified-ambiguity-or-boundary): Assign a version and keep a changelog or persistent identifier.
  Rationale: An explicit component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Validate the data, such as checking integrity, completeness and consistency with documentation.
  Rationale: An explicit component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; identified-ambiguity-or-boundary): Support reproducibility by providing code, processing steps or checksums so others can reproduce derived results.
  Rationale: An explicit component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Criticality uses the omission-consequence test: sensitive-information handling, license and documentation are critical; versioning, validation and reproducibility are supporting. No specific repository or license is required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC082

procedural_instructional; easy.

### en

Describe a simple procedure for moving photos from a phone to a computer while keeping the originals until the copy is verified.

### bn

ফোন থেকে কম্পিউটারে ছবি সরানোর একটি সহজ পদ্ধতি বর্ণনা করুন, যেখানে কপি যাচাই না হওয়া পর্যন্ত মূল ছবিগুলো রেখে দেওয়া হবে।

### bn_cs

phone থেকে computer-এ photo move করার একটি simple procedure describe করুন, যেখানে copy verify না হওয়া পর্যন্ত original-গুলো রেখে দেওয়া হবে।

### Boundary and ambiguity questions

- [ ] RIU-03: Explicit prompt requirement: silence may pass only if no deletion is proposed before verification; check BN/BN-CS wording ("রেখে দেওয়া হবে") for equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Copy the photos from the phone to the computer using a cable, app or cloud sync.
  Rationale: The core transfer step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Verify the copy, for example by comparing counts or sizes or opening a sample of photos, including videos if relevant.
  Rationale: The prompt requires verification before deletion.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Keep the originals on the phone until the copy is verified; deleting only after verification complies.
  Rationale: An explicit requirement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Organize the copied photos in a clear folder on the computer.
  Rationale: Makes the copy usable.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Consider a second backup copy before deleting originals.
  Rationale: Extra protection; optional for a simple procedure.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. "Move" in the prompt does not require deletion; deletion is optional after verification. Specific operating systems or apps are not required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## PROC100

procedural_instructional; hard.

### en

A multi-team project is approaching launch with several unresolved risks. Design a final readiness procedure that identifies blockers, owners, fallback options, go/no-go criteria, and post-launch monitoring.

### bn

একাধিক টিমের একটি প্রজেক্ট চালু হওয়ার কাছাকাছি, কিন্তু কয়েকটি ঝুঁকির এখনো সমাধান হয়নি। প্রতিবন্ধকতা, দায়িত্বপ্রাপ্ত ব্যক্তি, বিকল্প ব্যবস্থা, চালু করা হবে কি হবে না তার মানদণ্ড এবং চালুর পরের মনিটরিং চিহ্নিত করে এমন একটি চূড়ান্ত প্রস্তুতি-যাচাই পদ্ধতি তৈরি করুন।

### bn_cs

একাধিক team-এর একটি project launch-এর কাছাকাছি, কিন্তু কয়েকটি risk-এর এখনো সমাধান হয়নি। blocker, দায়িত্বপ্রাপ্ত owner, fallback option, go/no-go criteria আর launch-এর পরের monitoring চিহ্নিত করে এমন একটি চূড়ান্ত readiness procedure তৈরি করুন।

### Boundary and ambiguity questions

- [ ] RIU-05: Criticality boundary: monitoring is explicitly requested; confirm supporting vs critical under the omission-consequence test.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify and track blockers and unresolved risks across teams in a shared list.
  Rationale: An explicit component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Assign an owner to each blocker or risk.
  Rationale: An explicit component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Define fallback options such as rollback, feature flags or phased rollout.
  Rationale: An explicit component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Define explicit go/no-go criteria in advance, linked to the unresolved risks.
  Rationale: The decision gate is central.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = States that a go/no-go decision will be made but gives no concrete criteria.
- [ ] **RIU-05** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Plan post-launch monitoring with defined metrics, responsibilities or time window.
  Rationale: An explicit component.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Hold a final readiness review or decision meeting with the relevant teams.
  Rationale: Coordinates the multi-team decision.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. All five listed components are explicit. Post-launch monitoring is supporting because its omission does not defeat the readiness decision itself, although it is listed; reviewers may challenge this. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN033

information_synthesis; easy.

### en

Identify the required deliverables: Submit the cleaned CSV, a one-page methodology note, and a screenshot of the final dashboard. Do not submit raw personal data.

### bn

যা যা জমা দিতে হবে তা চিহ্নিত করুন: পরিষ্কার করা সিএসভি, এক পৃষ্ঠার একটি পদ্ধতি-নোট এবং চূড়ান্ত ড্যাশবোর্ডের একটি স্ক্রিনশট জমা দিন। কাঁচা ব্যক্তিগত ডেটা জমা দেবেন না।

### bn_cs

যা যা submit করতে হবে সেই deliverable-গুলো চিহ্নিত করুন: পরিষ্কার করা CSV, এক পৃষ্ঠার একটি methodology note আর চূড়ান্ত dashboard-এর একটি screenshot জমা দিন। কাঁচা personal data জমা দেবেন না।

### Boundary and ambiguity questions

- [ ] RIU-04: This is an extraction task: the prohibition must be stated, so silence does not satisfy RIU-04 even though it is a constraint.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): List the cleaned CSV as a required deliverable.
  Rationale: An explicit deliverable.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): List the one-page methodology note as a required deliverable.
  Rationale: An explicit deliverable, including its length.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): List the screenshot of the final dashboard as a required deliverable.
  Rationale: An explicit deliverable.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical, identified-ambiguity-or-boundary): State that raw personal data must not be submitted.
  Rationale: An explicit prohibition; omission could lead to a privacy breach.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. The one-page limit is part of the methodology-note unit. "Cleaned" and "final" qualifiers should be preserved but paraphrase is acceptable. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN047

information_synthesis; medium.

### en

Extract decisions, actions, and open questions separately: The team agreed to keep the current vendor through December. Nina will request a renewal quote. The migration date is still undecided. The team needs to know whether data export has an extra fee.

### bn

সিদ্ধান্ত, করণীয় এবং অমীমাংসিত প্রশ্নগুলো আলাদা করে বের করুন: টিম ডিসেম্বর পর্যন্ত বর্তমান ভেন্ডরকে রাখার বিষয়ে একমত হয়েছে। নিনা নবায়নের জন্য মূল্য-প্রস্তাব চাইবেন। মাইগ্রেশনের তারিখ এখনো ঠিক হয়নি। ডেটা এক্সপোর্টের জন্য বাড়তি ফি আছে কি না তা টিমের জানা দরকার।

### bn_cs

decision, action আর open question-গুলো আলাদা করে extract করুন: team ডিসেম্বর পর্যন্ত বর্তমান vendor-কে রাখার বিষয়ে একমত হয়েছে। নিনা একটি renewal quote চাইবেন। migration date এখনো ঠিক হয়নি। data export-এর জন্য extra fee আছে কি না তা team-এর জানা দরকার।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Classify keeping the current vendor through December as a decision.
  Rationale: The only decision.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Classify Nina requesting a renewal quote as an action, with Nina as owner.
  Rationale: The only action and its owner.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical): Classify the undecided migration date as an open question.
  Rationale: An open question.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (critical; all-critical): Classify whether data export has an extra fee as an open question.
  Rationale: An open question.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Paraphrase and Bengali transliteration of Nina are acceptable. Misclassification (for example listing the migration date as a decision) is incorrect. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
- [ ] CHECK-02: Decisions, actions and open questions are presented as separate groups.

## SYN060

information_synthesis; hard.

### en

Two studies evaluate the same intervention. Study A reports a large benefit in 60 volunteers with no control group. Study B reports a small benefit in 400 participants with a control group. Explain how to synthesize the evidence without averaging the results mechanically.

### bn

দুটি গবেষণা একই হস্তক্ষেপ মূল্যায়ন করেছে। গবেষণা A কন্ট্রোল গ্রুপ ছাড়া ৬০ জন স্বেচ্ছাসেবীর মধ্যে বড় উপকারের কথা জানিয়েছে। গবেষণা B কন্ট্রোল গ্রুপসহ ৪০০ জন অংশগ্রহণকারীর মধ্যে ছোট উপকারের কথা জানিয়েছে। ফলাফলগুলো যান্ত্রিকভাবে গড় না করে প্রমাণগুলো কীভাবে সমন্বিতভাবে বিশ্লেষণ করবেন তা ব্যাখ্যা করুন।

### bn_cs

দুটি study একই intervention evaluate করেছে। Study A control group ছাড়া ৬০ জন volunteer-এর মধ্যে বড় benefit report করেছে। Study B control group-সহ ৪০০ জন participant-এর মধ্যে ছোট benefit report করেছে। result-গুলো mechanically average না করে evidence কীভাবে synthesize করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-03: Check that a cautious "probably modest benefit" conclusion is required; refusing any conclusion is insufficient.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Explain that Study B's control group and larger sample make its estimate more credible than Study A's.
  Rationale: The core weighting judgment.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Explain that Study A's lack of a control group means its large benefit may reflect placebo, natural improvement, selection of volunteers or other bias.
  Rationale: Explains why the larger effect is less trustworthy.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (critical; all-critical, identified-ambiguity-or-boundary): Conclude that the evidence suggests a benefit is likely but probably smaller than Study A implies.
  Rationale: The supported synthesis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Do not average the two effect sizes mechanically or treat them as equally informative; weighting by design quality complies.
  Rationale: Explicitly prohibited.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; prespecified-ordinary-sample): Suggest what would strengthen the conclusion, such as further controlled studies or checking population differences.
  Rationale: Identifies remaining uncertainty.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Volunteer selection is an example of bias. Formal meta-analysis terms are optional. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN067

information_synthesis; medium.

### en

A service received fewer complaints after a redesign, but total usage also fell by 25 percent. Explain what additional rate or denominator would be important before concluding complaints truly decreased.

### bn

নতুন করে নকশা করার পর একটি সার্ভিসে অভিযোগ কমেছে, কিন্তু মোট ব্যবহারও ২৫ শতাংশ কমে গেছে। অভিযোগ সত্যিই কমেছে—এমন উপসংহার টানার আগে কোন হার বা হরের হিসাব গুরুত্বপূর্ণ হবে তা ব্যাখ্যা করুন।

### bn_cs

redesign-এর পর একটি service-এ complaint কমেছে, কিন্তু total usage-ও ২৫ শতাংশ কমে গেছে। complaint সত্যিই কমেছে—এমন conclusion টানার আগে কোন additional rate বা denominator গুরুত্বপূর্ণ হবে তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify a complaint rate per unit of usage (such as complaints per user, session or transaction) as the needed measure.
  Rationale: The core answer.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): Explain that a 25% fall in usage alone could reduce complaint counts even if the complaint rate stayed the same or rose.
  Rationale: Explains why raw counts mislead.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): State that complaints truly decreased only if the rate fell, comparing before and after periods.
  Rationale: The conclusion condition.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Mention another factor worth checking, such as whether the redesign made complaining harder or changed who uses the service.
  Rationale: A second confound.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Any appropriate usage denominator is acceptable. A worked numerical example is optional. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## SYN085

information_synthesis; medium.

### en

Summarize the operational risk: One employee knows how to run a critical weekly process. Documentation is incomplete. The employee will be on leave next month. Another staff member has observed the process once.

### bn

পরিচালনাগত ঝুঁকিটি সংক্ষেপ করুন: একটি গুরুত্বপূর্ণ সাপ্তাহিক প্রক্রিয়া কীভাবে চালাতে হয় তা কেবল একজন কর্মী জানেন। ডকুমেন্টেশন অসম্পূর্ণ। ওই কর্মী আগামী মাসে ছুটিতে থাকবেন। আরেকজন কর্মী প্রক্রিয়াটি একবার দেখেছেন।

### bn_cs

operational risk-টা summarize করুন: একটি critical weekly process কীভাবে চালাতে হয় তা কেবল একজন employee জানেন। documentation incomplete। ওই employee আগামী মাসে leave-এ থাকবেন। আরেকজন staff member process-টা একবার দেখেছেন।

### Boundary and ambiguity questions

- [ ] RIU-05: Confirm mitigation is supporting, not critical, because the prompt asks only to summarize the risk.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Identify the single-person dependency for a critical weekly process as the core risk.
  Rationale: The central risk.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical): State that the risk becomes urgent next month when the employee is on leave.
  Rationale: Timing of the exposure.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Note that incomplete documentation limits others' ability to run the process.
  Rationale: A contributing factor.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Note that the backup staff member has observed the process only once and is not yet ready.
  Rationale: Weak backup capacity.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Suggest mitigation such as completing documentation or supervised practice before the leave.
  Rationale: A summary of risk is more useful with mitigation; this remains supporting.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. The prompt asks for a summary; mitigation is supporting. Exaggeration such as asserting certain failure is a correctness issue. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH024

technical_troubleshooting; medium.

### en

A desktop application works after reinstalling but fails again after the user's settings are restored. Explain how you would investigate the configuration as a possible cause.

### bn

একটি ডেস্কটপ অ্যাপ্লিকেশন নতুন করে ইনস্টল করার পর কাজ করে, কিন্তু ব্যবহারকারীর আগের সেটিংস ফিরিয়ে আনার পর আবার ব্যর্থ হয়। কনফিগারেশনকে সম্ভাব্য কারণ ধরে কীভাবে তদন্ত করবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি desktop application reinstall করার পর কাজ করে, কিন্তু user-এর settings restore করার পর আবার fail করে। configuration-কে সম্ভাব্য কারণ ধরে কীভাবে investigate করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01, RIU-02: Check the two critical units are distinct: confirming that settings trigger the failure versus isolating which setting does.

### RIU checklist

- [ ] **RIU-01** (critical; all-critical, identified-ambiguity-or-boundary): Confirm the pattern by testing the clean install with default settings, then restoring settings and observing whether the failure returns.
  Rationale: Establishes configuration as the trigger.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (critical; all-critical, identified-ambiguity-or-boundary): Restore settings incrementally or bisect them to identify the specific file, option or value that causes the failure.
  Rationale: Pinpoints the faulty configuration; this is the central investigation.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; prespecified-ordinary-sample): Keep a backup of the user's original settings before modifying or deleting them; working on a copy complies.
  Rationale: Prevents losing the user's configuration.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Compare the restored settings with defaults or with a working user, looking for version-incompatible or corrupt entries.
  Rationale: Explains why the settings fail.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Check application logs for errors when the settings load.
  Rationale: Additional evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Restoring a subset of settings is an acceptable form of bisection. Product-specific paths are not required. The two critical units are the confirmation and isolation steps the prompt asks for; they are not generic area checks. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH044

technical_troubleshooting; medium.

### en

A REST API endpoint works locally but returns a server error after deployment. Explain how to isolate environment variables, dependencies, database connectivity, permissions, and request differences.

### bn

একটি রেস্ট এপিআই এন্ডপয়েন্ট লোকাল এনভায়রনমেন্টে কাজ করে, কিন্তু ডিপ্লয় করার পর সার্ভার এরর দেয়। এনভায়রনমেন্ট ভেরিয়েবল, ডিপেন্ডেন্সি, ডেটাবেস সংযোগ, অনুমতি এবং রিকোয়েস্টের পার্থক্য কীভাবে আলাদা করে যাচাই করবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি REST API endpoint লোকালি ঠিকঠাক কাজ করে, কিন্তু deploy করার পর server error দেয়। environment variable, dependency, database connectivity, permission আর request-এর পার্থক্য কীভাবে আলাদা করে যাচাই করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] RIU-01: Logs are not named in the prompt; confirm they are a supporting evidence unit rather than overlap with the area checks.

### RIU checklist

- [ ] **RIU-01** (supporting; identified-ambiguity-or-boundary, prespecified-ordinary-sample): Read the deployed server's logs or error details for the failing request.
  Rationale: The primary evidence source.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Compare environment variables and configuration between local and deployed environments.
  Rationale: A named isolation area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Compare dependency versions and installed packages, for example via lock files or build manifests.
  Rationale: A named isolation area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Test database connectivity and credentials from the deployed environment.
  Rationale: A named isolation area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Check permissions such as file-system access, service accounts or network rules in the deployed environment.
  Rationale: A named isolation area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; prespecified-ordinary-sample): Compare the actual requests sent to local and deployed endpoints, such as headers, payload, authentication or URL.
  Rationale: A named isolation area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (critical; all-critical): Use a controlled local-versus-deployed comparison or log evidence to explain how a possible result supports or weakens a named cause.
  Rationale: Without result interpretation the answer lists areas but does not isolate the deployment failure.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Proposes a local-versus-deployed comparison but gives no possible result-to-hypothesis interpretation.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Follows the accepted convention (for example TECH049): each named area is supporting and the interpretation unit is critical. Any stack is acceptable. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH068

technical_troubleshooting; medium.

### en

A workstation reports occasional memory errors only under sustained load. Explain how you would distinguish RAM faults from overheating, power instability, motherboard issues, and software corruption.

### bn

একটি ওয়ার্কস্টেশনে শুধু দীর্ঘ সময় ধরে ভারী লোড থাকলে মাঝে মাঝে মেমরি এরর দেখা যায়। র‍্যামের ত্রুটি, অতিরিক্ত গরম হওয়া, পাওয়ারের অস্থিতিশীলতা, মাদারবোর্ডের সমস্যা এবং সফটওয়্যার করাপশন—এগুলোর মধ্যে কীভাবে পার্থক্য করবেন তা ব্যাখ্যা করুন।

### bn_cs

একটি workstation-এ শুধু দীর্ঘ সময় ভারী load থাকলে মাঝে মাঝে memory error দেখা যায়। RAM-এর ত্রুটি, overheating, power instability, motherboard issue আর software corruption—এগুলোর মধ্যে কীভাবে পার্থক্য করবেন তা explain করুন।

### Boundary and ambiguity questions

- [ ] No additional ambiguity identified by draft author; independently verify coverage and equivalence.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Test RAM directly with a memory diagnostic and isolate modules or slots by testing one at a time.
  Rationale: A named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; ordinary, outside prespecified sample): Monitor temperatures under load to check whether errors coincide with overheating.
  Rationale: A named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check power stability, for example by monitoring voltages or testing with a known-good power supply.
  Rationale: A named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Treat the motherboard as a likely cause when errors persist with known-good RAM in different slots after other causes are excluded.
  Rationale: A named cause, usually by elimination.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; ordinary, outside prespecified sample): Check for software corruption, for example with system-file checks or testing under a clean or live operating system.
  Rationale: A named cause.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (critical; all-critical): Explain how at least one possible test result favors or weakens a named cause relative to another.
  Rationale: Without interpretation the answer does not perform the requested differential diagnosis.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Says to compare or rule out causes after tests but gives no result-to-hypothesis example.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Follows the accepted TECH004 convention. Overclocking settings may be mentioned as a contributing factor but are not required. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH070

technical_troubleshooting; hard.

### en

A computer sometimes fails to boot after being powered off overnight but starts normally after several attempts. Propose a safe diagnostic strategy that avoids replacing components prematurely.

### bn

একটি কম্পিউটার সারা রাত বন্ধ থাকার পর মাঝে মাঝে বুট হয় না, কিন্তু কয়েকবার চেষ্টা করলে স্বাভাবিকভাবে চালু হয়। তাড়াহুড়ো করে যন্ত্রাংশ বদলানো এড়িয়ে সমস্যা নির্ণয়ের একটি নিরাপদ কৌশল প্রস্তাব করুন।

### bn_cs

একটি computer সারা রাত power off থাকার পর মাঝে মাঝে boot হয় না, কিন্তু কয়েকবার চেষ্টা করলে স্বাভাবিকভাবে চালু হয়। তাড়াহুড়ো করে component replace করা এড়িয়ে একটি safe diagnostic strategy propose করুন।

### Boundary and ambiguity questions

- [ ] RIU-05: Boundary: is swapping in a known-good PSU a replacement? Draft treats a one-at-a-time diagnostic swap as compliant.
- [ ] RIU-07: Check the interpretation unit is not satisfied by merely listing checks.

### RIU checklist

- [ ] **RIU-01** (supporting; ordinary, outside prespecified sample): Record the exact symptoms of a failed cold boot, such as no power, fans but no display, beep codes or error messages.
  Rationale: Symptoms narrow the cause area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; prespecified-ordinary-sample): Investigate power-related causes such as the power supply or CMOS battery, using measurements, logs or a known-good part comparison.
  Rationale: Cold-start failures often involve power.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check firmware or operating-system evidence after a successful boot, such as event logs, BIOS logs or fast-startup settings.
  Rationale: Software or firmware evidence.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; ordinary, outside prespecified sample): Check connections and reseat RAM or cables with power removed.
  Rationale: Low-cost checks for intermittent contact.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (critical; all-critical, identified-ambiguity-or-boundary): Do not replace components before tests implicate them; one-at-a-time diagnostic swaps with known-good parts comply.
  Rationale: The prompt explicitly asks to avoid premature replacement.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-06** (supporting; ordinary, outside prespecified sample): Remove power and follow anti-static precautions before working inside the case.
  Rationale: Safety during internal checks.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-07** (critical; all-critical, identified-ambiguity-or-boundary): Use a controlled comparison or repeated cold-start observations to explain how a possible result favors or weakens a named cause relative to alternatives.
  Rationale: Without result interpretation the answer lists checks but does not diagnose the intermittent fault.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
  0.5 = Proposes repeated observation or a single-change comparison but gives no possible result and its diagnostic implication.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Follows the accepted differential-diagnosis convention: individual cause-area checks are supporting and result interpretation is critical. A one-at-a-time diagnostic swap with a known-good part is testing, not premature replacement. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.

## TECH072

technical_troubleshooting; easy.

### en

A phone connects to home Wi-Fi but mobile apps say they are offline. Describe simple checks before reinstalling apps.

### bn

একটি ফোন বাসার ওয়াই-ফাইতে যুক্ত হচ্ছে, কিন্তু মোবাইল অ্যাপগুলো বলছে সেগুলো অফলাইন। অ্যাপ আবার ইনস্টল করার আগে কোন কোন সহজ চেক করা উচিত তা বর্ণনা করুন।

### bn_cs

একটি phone home Wi-Fi-তে connect হচ্ছে, কিন্তু mobile app-গুলো offline দেখাচ্ছে। app reinstall করার আগে কোন কোন সহজ check করা উচিত তা describe করুন।

### Boundary and ambiguity questions

- [ ] RIU-02, RIU-05: Both isolate network versus device; confirm they are distinct units (other devices vs mobile data).

### RIU checklist

- [ ] **RIU-01** (critical; all-critical): Test whether the internet works at all on the phone, for example by opening a website, to distinguish a Wi-Fi-without-internet problem from an app problem.
  Rationale: Determines the cause area.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-02** (supporting; identified-ambiguity-or-boundary): Check whether other devices on the same Wi-Fi have internet, or restart the router.
  Rationale: Isolates the router or internet service.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-03** (supporting; ordinary, outside prespecified sample): Check phone settings that block app data, such as VPN, data saver, background-data restrictions or date and time.
  Rationale: Common phone-side causes.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-04** (supporting; prespecified-ordinary-sample): Toggle Wi-Fi or restart the phone, or forget and rejoin the network.
  Rationale: Simple resets.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.
- [ ] **RIU-05** (supporting; identified-ambiguity-or-boundary): Check whether the apps work on mobile data, to separate a network issue from an app issue.
  Rationale: A further isolation step.
  Anchors: 0 = Absent, incorrect, contradicted, or does not meet an available positive anchor.; 1 = description above.

Draft notes: P03 preparatory AI draft; corpus v0.3.1; protocol 0.3; schema 0.2. All EN/BN/BN-CS prompt strings inspected. Reinstalling is the step to avoid until checks are done. No critical RIU beyond RIU-01; other checks are alternatives of similar value. Equivalent wording, script and numerals accepted. Defeating contradictions override positive anchors; genuine refusals/nonanswers score 0 on all RIUs. Conditional safeguards apply to the actions proposed, not to unproposed destructive actions. No study response, judge score or model outcome was read while drafting. No independent human acceptance or language-equivalence certification. Production protocol approval and independent review pending.

Task checks:

- [ ] CHECK-01: Score 0 (flagged) for a material factual or operational assertion contradicted by the prompt or justified task knowledge, including materially wrong numeric values, directions or comparators and unsafe operational instructions; cite the response span. Score 1 (pass) if no such assertion is present. Pure omission or insufficient RIU fulfillment alone does not fail this check. CHECK-01 is orthogonal to RIU coverage: the same span can fail both an RIU and CHECK-01, and an RIU failure must not suppress this check.
