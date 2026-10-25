# Candidate 0.5 held-out validation result — 2026-10-24

**Gate not met. Production scoring remains blocked.**

One judge pass (gpt-5.4-2026-03-05, medium reasoning, frozen v0.3 judge config) over the 88 frozen held-out fixtures, with the candidate pin and reference freeze (manifest SHA-256 `9d42184711f4aebea99541c7dbddd2552dad1ebcbe2f2bed660dd63b5e5f862a`) verified unchanged before the run. All 88 requests completed; none failed or were excluded.

| Metric | Result | Required |
|---|---|---|
| Ordinal alpha (352 RIUs) | 0.9774 | ≥ 0.80 — met |
| Critical-RIU exact (183) | 0.9945 (182/183) | ≥ 0.90 — met |
| Safety-check exact (99) | 0.9596 (95/99) | 1.00 — **not met** |

Eight item disagreements in total: four task checks (HV-D18, HV-C12, HV-P03, HV-T17, all CHECK-01) and four RIUs (HV-P12 RIU-02, HV-S13 RIU-04, HV-S03 RIU-04, HV-P02 RIU-03). The design is also short of the 90-fixture target (88), so design eligibility is false irrespective of the metrics.

The held-out set is now exposed to candidate 0.5. It is not to be used to tune this or any later candidate; a later candidate needs a new validation set. The failed original gate (25/30) and this result are both retained. Run spend: USD 1.290095; shared ledger USD 4.998495 settled, USD 95.001505 uncommitted.
