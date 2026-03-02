# Design Principles

---

## Safety Over Completion

Irrecoverable outputs are rejected rather than auto-completed to prevent unsafe incident reporting.

---

## Deterministic Correction

All normalization steps are rule-based and reproducible.

---

## No Hallucinated Metadata

Missing operational attributes such as location are never fabricated.

---

## Logical Consistency

Cross-field consistency checks prevent structurally valid but logically unsafe outputs from entering operational systems.

---

## Confidence Calibration

Confidence scores are reduced when consistency violations are detected, reflecting reduced reliability.
