from fireform.validation.correction_pipeline import run_corrections
from fireform.validation.schema_validator import validate_incident
from fireform.validation.missing_field_handler import detect_missing_fields
from fireform.validation.confidence_scoring import compute_confidence


# Temporary extractor (simulated LLM output)
def extract_incident_data(user_input):
    return {
        "incident_type": user_input,
        "severity": "Very Dangerous",
        "incident_time": "Yesterday evening",
        "location": "Near downtown mall"
    }


def reliability_layer(user_input):

    # Step 1 — Extract structured data
    extracted_data = extract_incident_data(user_input)

    # Step 2 — Detect missing fields
    missing = detect_missing_fields(extracted_data)

    # Step 3 — Confidence score
    confidence = compute_confidence(extracted_data)
    threshold = 0.8

    # Step 4 — Validate
    validated, errors = validate_incident(extracted_data)

    # Step 5 — Correction if needed
    if errors:
        corrected_data = run_corrections(extracted_data)
        validated, errors = validate_incident(corrected_data)

        return {
            "confidence": confidence,
            "missing_fields": missing,
            "validation_error": errors,
            "extracted": extracted_data,
            "validated": validated
        }

    return {
        "confidence": confidence,
        "missing_fields": missing,
        "validation_error": None,
        "extracted": extracted_data,
        "validated": validated
    }