# 🔥 FireForm Reliability Middleware Prototype

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

## 🔧 Reliability Middleware Architecture

![Reliability Layer Architecture](docs/assets/reliability-layer-flow.png)

---

## ⚙️ Middleware Pipeline

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

## 📊 Benchmark (Reproducible)

Evaluation conducted on a fixed synthetic dataset (n=150) simulating noisy emergency incident descriptions.

### Results

```
PS C:\Users\manis\OneDrive\Desktop\FireForm-Reliability-Layer> python benchmark_reliability.py

=========== RUNNING TRUE BENCHMARK ===========

Total Test Cases                  : 150

--------------- RAW EXTRACTION ---------------
Missing Field Cases               : 150
Validation Error Cases            : 144

----------- WITH RELIABILITY LAYER -----------
Structured Success Cases          : 92
Validation Error Cases            : 58
Consistency Warnings Raised       : 7

------------------ METRICS -------------------
Raw Missing Rate                  : 100.00%
Raw Validation Error Rate         : 96.00%
Post-Layer Success Rate           : 61.33%

----------- RECOVERABILITY METRICS -----------
Salvageable Raw Cases             : 65
Unrecoverable Raw Cases           : 85
Post-Layer Recovered Cases        : 59

Effective Repair Rate             : 90.77%
Unsafe Guess Count                : 0
----------------------------------------------
```

### 🔁 Reproduce Benchmark

```bash
python benchmark_reliability.py
```

Dataset is seeded for deterministic evaluation.

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
│   │   └── incident_schema.py
│   │
│   └── reliability/
│       ├── normalizer.py
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

Manish Krishna Kandrakota (MANISH-K-07)
B.Tech Computer Science & Engineering
IEEE-published researcher & Open-source contributor
Systems & Reliability Engineering Enthusiast
