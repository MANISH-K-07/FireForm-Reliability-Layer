# 🔥 FireForm Reliability Middleware Prototype

[![GitHub Repo Size](https://img.shields.io/github/repo-size/MANISH-K-07/FireForm-Reliability-Layer)](https://github.com/MANISH-K-07/FireForm-Reliability-Layer)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![GitHub License](https://img.shields.io/github/license/MANISH-K-07/FireForm-Reliability-Layer)](https://github.com/MANISH-K-07/FireForm-Reliability-Layer/blob/main/LICENSE)
[![GitHub Pages](https://img.shields.io/badge/demo-GitHub%20Pages-brightgreen)](https://MANISH-K-07.github.io/FireForm-Reliability-Layer/)


A safety-preserving reliability layer for structured emergency incident extraction.

This repository contains a modular middleware prototype designed to sit between a Large Language Model (LLM) extraction system and FireForm’s structured incident schema validator.

The goal is to transform noisy, partially structured incident reports into schema-compliant, logically consistent, and operationally safe structured outputs — without hallucinating missing data.

---

## 🚨 Why This Matters

Emergency reporting systems cannot tolerate:

* Missing operational metadata
* Contradictory severity classifications
* Fabricated location data
* Overconfident corrections
* Structurally unstable extraction outputs

Real-world LLM extractors frequently produce:

* Missing keys
* Free-text severity labels
* Invalid datetime formats
* Schema-incompatible nested structures
* Non-deterministic outputs for identical reports

This reliability layer prioritizes:

* Structural validity
* Logical consistency
* Deterministic correction
* Schema stability
* Safety over aggressive auto-completion

---

## ⚙️ Reliability Middleware Pipeline

### 1. Extraction (LLM Output)

Raw structured output from extraction system may include:

* Missing fields
* Invalid timestamps
* Location as string
* Free-text severity
* Schema violations

### 2. Structural Normalization Layer (NEW)

Enforces deterministic schema shape before validation by:

* Injecting missing schema keys
* Converting string locations → structured format
* Standardizing datetime placeholders
* Preventing validator crashes from absent keys
* Preserving semantic recoverability without hallucination

This step ensures that:

> Identical incident descriptions produce structurally stable normalized outputs despite stochastic extraction failures.

### 3. Missing Field Detection

Identifies incomplete extraction outputs.

### 4. Schema-Aware Correction

Recovers:

* Natural language timestamps ("last night", "yesterday evening")
* Severity inconsistencies
* Recoverable metadata

### 5. Validation Enforcement

Ensures strict compliance with incident schema.

### 6. Cross-Field Consistency Engine

Detects logical contradictions such as:

* Explosion incidents labeled "Low" severity
* Severe fire reports marked "minor"
* High severity events with “no damage” descriptions

### 7. Confidence Calibration

Penalizes inconsistent outputs to avoid unsafe overconfidence.

---

## 🧪 Example Middleware Run

The following example demonstrates how the Reliability Layer converts a noisy incident description into a schema-compliant structured report without fabricating operational metadata.

### Input

```
Severe fire but no visible damage today
```

### Middleware Output

```
PS C:\Users\manis\OneDrive\Desktop\FireForm-Reliability-Layer> python test_pipeline.py

================ INCIDENT REPORT =================
Original Input    : Severe fire but no visible damage today

Incident Type     : Fire
Severity          : High
Incident Time     : 2026-03-02 22:40:36
Report Time       : 2026-03-02 22:40:36.640497
Location          : None, None

Missing Fields    : ['city', 'state']

Consistency Errors:
  None

Consistency Warnings:
  None

Final Confidence  : 0.9
==================================================
```

### Observations

* Severity safely normalized from free-text description
* Missing location preserved as explicitly unknown
* No fabricated city/state values introduced
* Timestamp retained from extraction output
* Structured report passes strict schema validation

This illustrates the middleware's core design principle:

> Recover when safe. Reject when unsafe. Never hallucinate.

---

## 📊 Benchmark (Reproducible)

Evaluation conducted on a fixed synthetic dataset (n=150) simulating noisy emergency incident descriptions.

### Results

```
PS C:\Users\manis\OneDrive\Desktop\FireForm-Reliability-Layer> python benchmark_reliability.py

=========== RUNNING TRUE BENCHMARK ===========

Total Test Cases                  : 150

--------------- RAW EXTRACTION ---------------
Missing Field Cases               : 150
Validation Error Cases            : 146

----------- WITH RELIABILITY LAYER -----------
Structured Success Cases          : 62
Validation Error Cases            : 88
Consistency Warnings Raised       : 4

------------------ METRICS -------------------
Raw Missing Rate                  : 100.00%
Raw Validation Error Rate         : 97.33%
Post-Layer Success Rate           : 41.33%

----------- RECOVERABILITY METRICS -----------
Salvageable Raw Cases             : 65
Unrecoverable Raw Cases           : 85
Post-Layer Recovered Cases        : 56

Effective Repair Rate             : 86.15%
Unsafe Guess Count                : 0
----------------------------------------------
```

### 🔁 Reproduce Benchmark

```bash
python benchmark_reliability.py
```

Dataset is seeded for deterministic evaluation.

---

## 🔎 Middleware in Action (Consistency Intervention Example)

The following example demonstrates how the Reliability Layer detects semantic contradictions in incident descriptions and penalizes confidence to avoid unsafe over-trust in structured outputs.

### Input

```
Massive explosion reported but everything seems safe with no injuries or damage
```

### Output

```
================ INCIDENT REPORT =================
Original Input    : Massive explosion reported but everything seems safe with no injuries or damage

Incident Type     : Explosion
Severity          : High
Incident Time     : 2026-03-02 22:46:52
Report Time       : 2026-03-02 22:46:52.065873
Location          : None, None

Missing Fields    : ['city', 'state']

Consistency Errors:
  None

Consistency Warnings:
  - High severity conflicts with low-impact description

Final Confidence  : 0.8
==================================================
```

### Interpretation

Although the extractor assigns a **High severity** classification based on the phrase *"Massive explosion"*,
the Reliability Layer identifies a contradiction with the description:

> *"everything seems safe with no injuries or damage"*

Instead of overriding the severity or fabricating incident attributes, the middleware:

* Raises a cross-field consistency warning
* Applies a confidence penalty
* Preserves traceability to the original description

This ensures that logically inconsistent reports are not passed downstream with unsafe confidence levels.

---

## ⚠️ Rejection Example: Unsafe / Low Confidence Input

The reliability layer enforces a confidence threshold of 0.75. Inputs that are gibberish, missing core fields, or have no valid severity are safely rejected to prevent unsafe or hallucinated incident data.

### Input

```
asdf qwer zzzz nothing makes sense 12345 ???
```

### Output

```
PS C:\Users\manis\OneDrive\Desktop\FireForm-Reliability-Layer> python test_pipeline.py

================ INCIDENT REPORT =================
Original Input    : asdf qwer zzzz nothing makes sense 12345 ???

⚠️  REPORT REJECTED BY RELIABILITY LAYER
Reason: Unsafe or Low Confidence Repair

Validation Errors:
  - {'type': 'string_type', 'loc': ('severity',), 'msg': 'Input should be a valid string', 'input': None, 'url': 'https://errors.pydantic.dev/2.12/v/string_type'}

Final Confidence  : 0
==================================================
```

### Notes

* The input’s confidence score was computed as 0, below the threshold of 0.75.
* Severity could not be safely inferred from the meaningless text.
* Demonstrates that the layer prevents unsafe auto-corrections and prioritizes operational safety.

---

## 🛡 Design Principles

* Never fabricate missing operational data
* Reject irrecoverable outputs instead of guessing
* Reduce validation errors without increasing risk
* Preserve traceability between raw text and structured output
* Enforce structural determinism before semantic correction

---

## 📂 Repository Structure

```
FireForm-Reliability-Layer/
│
├── fireform/
│   ├── extraction/
│   │   └── mock_extractor.py
│   │
│   ├── schema/
│       ├── normalizer.py
│   │   └── incident_schema.py
│   │
│   └── reliability/
│       ├── missing.py
│       ├── validator.py
│       ├── consistency.py
│       ├── correction.py
│       ├── confidence.py
│       └── recoverability.py
│
├── main.py
├── benchmark_reliability.py
├── generate_inputs.py
├── test_pipeline.py
└── README.md
```

---

## 🎯 Project Goal

This prototype demonstrates architectural readiness to implement a production-grade reliability middleware layer for FireForm’s multi-agency incident reporting system.

The focus is structural recoverability, logical coherence, and operational safety — not extraction accuracy.

---

## 👨‍💻 Author

- Manish Krishna Kandrakota (MANISH-K-07)
- B.Tech Computer Science & Engineering
- IEEE-published researcher & Open-source contributor
- Systems & Reliability Engineering Enthusiast
