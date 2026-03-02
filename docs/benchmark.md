# Reliability Benchmark

## Dataset

Synthetic incident dataset (n=150) simulating:

* Missing extraction fields
* Free-text severity labels
* Invalid timestamps
* Location schema corruption
* Inconsistent nested metadata

Dataset is seeded for reproducibility.

---

## Results

| Metric                  | Raw Extraction | With Reliability Layer |
| ----------------------- | -------------- | ---------------------- |
| Missing Field Rate      | 100%           | —                      |
| Validation Error Rate   | 96.00%         | 38.67%                 |
| Structured Success Rate | —              | 61.33%                 |
| Consistency Warnings    | —              | 7                      |

---

## Recoverability Metrics

| Metric                     | Value  |
| -------------------------- | ------ |
| Salvageable Raw Cases      | 65     |
| Unrecoverable Raw Cases    | 85     |
| Post-Layer Recovered Cases | 59     |
| Effective Repair Rate      | 90.77% |
| Unsafe Guess Count         | 0      |

---

## Key Finding

The Reliability Middleware safely repairs:

> 90.77% of structurally salvageable LLM outputs without introducing fabricated incident attributes.

This demonstrates that structural normalization significantly improves semantic recoverability while preserving operational safety.
