# Evaluation Methodology

Evaluation was conducted on a synthetic dataset of 150 incident descriptions generated to simulate noisy emergency reporting scenarios.

---

## Dataset Characteristics

The dataset includes:

* Temporal ambiguity ("last night", "this morning")
* Severity ambiguity ("minor", "massive")
* Missing location metadata
* Contradictory descriptions

---

## Metrics

### Raw Validation Error Rate

Percentage of extraction outputs failing schema validation without middleware.

### Structured Success Rate

Percentage of middleware outputs passing schema validation.

### Effective Repair Rate

Proportion of structurally salvageable extraction outputs successfully repaired by the middleware.

### Unsafe Guess Count

Number of instances where the middleware fabricated missing operational attributes.

---

## Results

```
PS C:\Users\manis\OneDrive\Desktop\FireForm-Reliability-Layer> python benchmark_reliability.py

=========== RUNNING TRUE BENCHMARK ===========

Total Test Cases                  : 150

--------------- RAW EXTRACTION ---------------
Missing Field Cases               : 150
Validation Error Cases            : 142

----------- WITH RELIABILITY LAYER -----------
Structured Success Cases          : 67
Validation Error Cases            : 83
Consistency Warnings Raised       : 4

------------------ METRICS -------------------
Raw Missing Rate                  : 100.00%
Raw Validation Error Rate         : 94.67%
Post-Layer Success Rate           : 44.67%

----------- RECOVERABILITY METRICS -----------
Salvageable Raw Cases             : 78
Unrecoverable Raw Cases           : 72
Post-Layer Recovered Cases        : 50

Effective Repair Rate             : 64.10%
Unsafe Guess Count                : 0
----------------------------------------------
```
---

## Reproducibility

Benchmarking uses a seeded dataset generator ensuring deterministic evaluation across runs.

```bash
python benchmark_reliability.py
```
