from fireform.extraction.mock_extractor import extract_incident_data
from fireform.reliability.missing import detect_missing_fields
from fireform.reliability.validator import validate_incident
from fireform.reliability.correction import run_corrections
from fireform.reliability.confidence import compute_confidence
from fireform.reliability.consistency import check_consistency
from fireform.schema.normalizer import normalize_extracted_json


def reliability_layer(user_input):

    # Step 1 — Extract structured data (simulate LLM) & Normalize
    extracted = extract_incident_data(user_input)

    extracted = normalize_extracted_json(extracted)

    # Step 2 — Detect missing fields
    missing = detect_missing_fields(extracted)

    # Step 3 — Base confidence scoring
    confidence = compute_confidence(extracted)

    # Step 4 — Run correction layer if missing OR messy LLM output
    if missing:
        corrected = run_corrections(extracted)
    else:
        corrected = run_corrections(extracted)   # Always run cleanup anyway

    # Step 5 — Validate corrected data
    validated, errors = validate_incident(corrected)

    result = {
        "confidence": confidence,
        "missing_fields": missing,
        "validated_output": validated,
        "validation_errors": errors
    }

    # Step 6 — Consistency Check ONLY if validation passed
    if validated:

        consistency = check_consistency(validated)

        result["consistency_errors"] = consistency["consistency_errors"]
        result["consistency_warnings"] = consistency["consistency_warnings"]

        # Confidence penalty
        if consistency["consistency_errors"]:
            result["confidence"] -= 0.3
        elif consistency["consistency_warnings"]:
            result["confidence"] -= 0.1

        # Clamp confidence between 0 and 1
        result["confidence"] = max(0, min(result["confidence"], 1))

    return result
