def compute_confidence(data):

    score = 1.0

    # -------- Missing Core Fields Penalty --------
    required_fields = ["incident_type", "severity", "incident_time", "report_time", "location"]

    for field in required_fields:
        if not data.get(field):
            score -= 0.15

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
    valid_severity = ["Low", "Medium", "High"]
    if data.get("severity") not in valid_severity:
        score -= 0.1

    # -------- Clamp Between 0 and 1 --------
    score = max(0, min(score, 1))

    return round(score, 2)
