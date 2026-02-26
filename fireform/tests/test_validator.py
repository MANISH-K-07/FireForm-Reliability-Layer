from fireform.validation.schema_validator import validate_incident
from fireform.validation.correction_pipeline import run_corrections

def test_valid_input():
    data = {
        "incident_type": "Fire",
        "severity": "High",
        "incident_time": "2026-02-23T10:20:00",
        "location": {"city": "San Jose", "state": "CA"}
    }

    validated, errors = validate_incident(data)
    assert errors is None


def test_invalid_datetime():
    data = {
        "incident_type": "Fire",
        "severity": "High",
        "incident_time": "Yesterday",
        "location": {"city": "San Jose", "state": "CA"}
    }

    validated, errors = validate_incident(data)
    assert errors is not None


def test_correction_pipeline():
    data = {
        "incident_type": "🔥🔥 BIG FIRE 🔥🔥",
        "severity": "Very Dangerous",
        "incident_time": "Yesterday evening",
        "location": "Near downtown mall"
    }

    corrected = run_corrections(data)
    validated, errors = validate_incident(corrected)

    assert errors is None