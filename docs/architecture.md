# Architecture Overview

## System Positioning

The Reliability Middleware sits between:

LLM Extraction → Reliability Layer → Schema Validator → Operational Systems

Its purpose is to stabilize and validate structured outputs before downstream use.

---

## Middleware Pipeline

### 1. Extraction (LLM Output)

Produces partially structured JSON with possible:

* Missing keys
* Invalid types
* Free-text substitutions
* Nested schema corruption

---

### 2. Structural Normalization Layer

Enforces deterministic schema structure before validation.

Responsibilities:

* Inject missing schema keys
* Standardize location structure
* Preserve recoverability without hallucinating data
* Prevent validator crashes

This layer ensures identical incident descriptions produce structurally stable intermediate representations.

---

### 3. Missing Field Detection

Identifies incomplete fields that impact operational readiness.

---

### 4. Correction Engine

Performs limited semantic recovery when safe:

* Severity normalization
* Recoverable metadata alignment

---

### 5. Schema Validation

Strict Pydantic enforcement against the incident schema.

---

### 6. Cross-Field Consistency Engine

Detects logical contradictions such as:

* High severity but “no damage”
* Explosion labeled “Low”
* Severe description but Minor classification

---

### 7. Confidence Calibration

Outputs a confidence score reflecting:

* Structural completeness
* Logical coherence
* Repair interventions performed

---

## Design Philosophy

The middleware enforces:

* Deterministic structure
* Conservative correction
* Explicit rejection of unsafe outputs
* Full traceability from input to validated report
