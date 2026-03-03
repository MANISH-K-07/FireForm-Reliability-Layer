from datetime import datetime

def compute_confidence(data):
    """
    Computes a confidence score [0,1] for the reliability of the structured incident output.
    Penalizes missing fields, invalid severity, unknown incident types, and garbage descriptions.
    """

    score = 1.0

    # -------- Missing Core Fields Penalty --------
    required_fields = ["incident_type", "severity", "incident_time", "report_time", "location"]
    for field in required_fields:
        if not data.get(field):
            score -= 0.2  # heavy penalty for missing core field

    # -------- Location Structure Penalty --------
    location = data.get("location")
    if isinstance(location, dict):
        if not location.get("city"):
            score -= 0.05
        if not location.get("state"):
            score -= 0.05
    else:
        score -= 0.1

    # -------- Severity Sanity Check --------
    valid_severities = ["Minor", "Medium", "High"]
    if data.get("severity") not in valid_severities or data.get("severity") is None:
        score -= 0.4  # heavier penalty for missing/invalid severity

    # -------- Incident Type Check --------
    if data.get("incident_type") in [None, "Unknown"]:
        score -= 0.3  # penalize unknown incident type

    # -------- Reject empty/garbage descriptions --------
    desc = data.get("description") or ""
    if len(desc.strip()) < 5 or all(not c.isalnum() for c in desc):
        score -= 0.3  # garbage input penalty

    # -------- Clamp Between 0 and 1 --------
    score = max(0, min(score, 1))

    return round(score, 2)
