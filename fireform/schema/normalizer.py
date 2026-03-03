from datetime import datetime

VALID_SEVERITIES = ["Minor", "Medium", "High"]

def normalize_severity(data):
    """
    Only normalize severity if description contains a clear signal.
    Otherwise, return None to avoid hallucinating Medium on garbage input.
    """
    severity = data.get("severity")
    desc = (data.get("description") or "").lower()

    # Keep valid severity only if description signals it
    if severity in VALID_SEVERITIES:
        if any(word in desc for word in ["severe", "massive", "dangerous", "casualties", "explosion"]):
            return "High"
        if any(word in desc for word in ["minor", "small"]):
            return "Minor"
        # Description has no signal → discard LLM default
        return None

    # Semantic recovery from description
    if len(desc.strip()) < 5:
        return None

    if any(word in desc for word in ["severe", "massive", "dangerous", "casualties", "explosion"]):
        return "High"
    if any(word in desc for word in ["minor", "small"]):
        return "Minor"

    return None


def normalize_extracted_json(data: dict) -> dict:
    """Ensure schema compliance and safe normalization."""

    # 1. INCIDENT TIME
    if "incident_time" not in data:
        data["incident_time"] = None

    # 2. LOCATION STRUCTURE
    if "location" not in data or isinstance(data["location"], str):
        data["location"] = {"city": None, "state": None}
    elif isinstance(data["location"], dict):
        data["location"].setdefault("city", None)
        data["location"].setdefault("state", None)

    # 3. REPORT TIME
    if "report_time" not in data:
        data["report_time"] = datetime.utcnow()

    # 4. INCIDENT TYPE
    data.setdefault("incident_type", None)

    # 5. DESCRIPTION
    data.setdefault("description", "")

    # 6. SAFE SEVERITY NORMALIZATION
    data["severity"] = normalize_severity(data)

    return data
