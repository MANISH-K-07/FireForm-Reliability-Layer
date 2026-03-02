# Design Principles

The FireForm Reliability Middleware follows strict safety-oriented principles.

---

## 1. Never Fabricate Operational Data

The system does not invent:

* City or state values
* Damage metrics
* Casualty counts
* Incident timestamps

Missing data remains explicitly missing.

---

## 2. Structural Determinism Before Semantics

Schema shape must be stabilized before attempting any correction.

This prevents:

* Validation crashes
* Random rejection of identical reports
* Non-deterministic system behavior

---

## 3. Recover When Safe, Reject When Unsafe

If data is structurally salvageable:

→ Repair conservatively

If logically inconsistent or unverifiable:

→ Reject explicitly

---

## 4. Zero Unsafe Guess Policy

The benchmark enforces:

Unsafe Guess Count = 0

No fabricated attributes are introduced during repair.

---

## 5. Traceable Corrections

Every normalization and correction step preserves visibility into:

* Original extraction
* Applied normalization
* Validation outcome
* Final confidence score

---

## 6. Safety Over Completion

In emergency systems:

Rejecting an unsafe report is preferable to accepting a fabricated one.
