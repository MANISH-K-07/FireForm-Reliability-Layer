def compute_confidence(data):
    score = 1.0

    if isinstance(data.get("incident_time"), str):
        score -= 0.3

    if isinstance(data.get("location"), str):
        score -= 0.3

    severity = data.get("severity", "").lower()
    if severity not in ["low", "medium", "high"]:
        score -= 0.2

    incident_type = data.get("incident_type", "")
    if any(char in incident_type for char in ["🔥", "!", "@", "#"]):
        score -= 0.2

    return max(score, 0.0)