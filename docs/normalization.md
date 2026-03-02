# Structural Normalization Layer

## Motivation

LLM-based extraction systems often produce structurally inconsistent JSON outputs even for identical input descriptions.

Common failure modes include:

* Missing required schema keys
* Free-text field substitutions
* Location represented as string instead of object
* Invalid datetime formats
* Nested object corruption

Such inconsistencies can cause:

* Schema validation failures
* Downstream processing crashes
* Non-deterministic incident acceptance
* Operational risk in emergency workflows

---

## Objective

The Structural Normalization Layer enforces schema stability **before validation** without introducing fabricated operational data.

This ensures:

* Deterministic schema structure
* Validator safety
* Recoverability of partially extractable incidents
* Prevention of unsafe auto-completion

---

## Normalization Strategy

### 1. Incident Time Stabilization

Ensures presence of `incident_time` key:

* Missing → injected as `None`
* Preserves recoverability for correction engine

---

### 2. Location Structure Enforcement

Handles LLM outputs such as:

```
"location": "Near downtown mall"
```

Converted into:

```
"location": {
  "city": null,
  "state": null
}
```

---

### 3. Report Time Injection

If missing:

```
report_time ← system timestamp
```

---

### 4. Severity Key Stabilization

Prevents validator crash by:

```
severity ← null (if absent)
```

Allows semantic recovery in later stages.

---

## Outcome

This layer guarantees:

> Structurally deterministic normalized outputs despite stochastic extraction behavior.

Identical incident descriptions now produce schema-stable intermediate representations, enabling safe downstream correction and validation.

---

## Design Principle

The Normalization Layer:

* Does not infer missing operational metadata
* Does not hallucinate location/severity
* Only stabilizes schema structure
* Enables recoverability without fabrication
