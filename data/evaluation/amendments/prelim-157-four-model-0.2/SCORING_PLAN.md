# Four-model scoring amendment candidate, 0.2

Not approved/frozen. Preserve annotation protocol 0.3 and the exact accepted
RIUs/checks, scoring anchors, criticality and reason meanings. The intended judge
remains the historical `gpt-6.1-sol` configuration, independently calibrated
before study scoring: 30 fixtures / 229 items, ordinal alpha >=0.80, critical-RIU
exact agreement >=0.90, safety task-check exact agreement 1.00. No threshold,
fixture, key or rubric changes are proposed. Previous human calibration is not
an automated-judge gate pass.

The new judge run must use its own append-only raw artifacts and manifest pins;
include the judge settings, frozen scoring inputs and actual calibration sheet
hash. Historical calibration may only be reused through explicit reviewed
evidence that all relevant hashes and blinding conditions match. Calibration and
study scoring incur paid API charges and require separate budget authorization.

Blind requests to response provenance; supply only the exact language prompt,
visible response and accepted rubric. Local private reasoning is excluded.
Score refusals/nonanswers under existing rules; successful truncations remain
outcomes. Keep runtime errors missing, distinct from omitted content.

Before reporting audited aggregates, human QA reviews every critical RIU below 1,
all check failures, refusals/nonanswers, truncations, plus deterministic 10% of
remaining response cells stratified by the four models and three languages.
Keep raw scores, a separately hash-linked adjudication layer, dispute resolutions
and reviewer evidence. A systematic error triggers review of its affected class.
Until QA is complete, any later analysis is explicitly provisional/unreviewed.

`scripts/prelim_four_judge.py` implements isolated calibration, scoring, resume
receipts, four-attempt retry budgets across restarts and blinded QA packets.
`JUDGE.json` proposes concurrency 1 (within the historical upper limit of 12);
all scientific judge settings, fixtures and thresholds are unchanged.
`analyze_prelim_four.py` accepts separately resolved, source-hash-linked
adjudications with reviewer/date and hashed review-log evidence, plus an explicit
supersession chain. These structural checks do not authenticate a reviewer or
certify independent human QA. Reports remain provisional pending that review.
Synthetic oracle-key tests exercise the gate; they never count as measured
calibration. The actual automated judge gate is absent and remains blocking.
See `RUNBOOK.md` for implemented commands; historical commands retain their panel.
