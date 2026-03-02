from fireform.extraction.mock_extractor import extract_incident_data
from fireform.reliability.missing import detect_missing_fields
from fireform.reliability.validator import validate_incident
from fireform.reliability.correction import run_corrections
from fireform.reliability.confidence import compute_confidence


def reliability_layer(user_input):

    # Step 1 — Extract structured data
    extracted = extract_incident_data(user_input)

    # Step 2 — Detect missing fields
    missing = detect_missing_fields(extracted)

    # Step 3 — Confidence scoring
    confidence = compute_confidence(extracted)

    # Step 4 — Try correction IF missing fields detected
    if missing:
        corrected = run_corrections(extracted)
    else:
        corrected = extracted

    # Step 5 — Validate corrected data
    validated, errors = validate_incident(corrected)

    return {
        "confidence": confidence,
        "missing_fields": missing,
        "validated_output": validated,
        "validation_errors": errors
    }