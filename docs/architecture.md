# Architecture

The reliability middleware sits between an upstream extraction module and the FireForm incident schema validator.

---

## Pipeline Stages

### 1. Extraction Layer

Simulated LLM output using a mock extractor producing:

* Incomplete metadata
* Natural language timestamps
* Non-standard severity levels
* Missing location fields

---

### 2. Missing Field Detection

Identifies schema-required attributes that are absent or null.

---

### 3. Schema-Aware Correction

Performs deterministic normalization:

* Timestamp resolution
* Severity mapping
* Location recovery

without fabricating unavailable operational data.

---

### 4. Validation Layer

Ensures corrected outputs comply with the FireForm incident schema.

---

### 5. Consistency Engine

Detects logical contradictions such as:

* Explosion with Low severity
* Severe event descriptions with Medium severity
* High severity incidents reporting no impact

---

### 6. Confidence Adjustment

Penalizes outputs exhibiting consistency violations to prevent unsafe operational overconfidence.
