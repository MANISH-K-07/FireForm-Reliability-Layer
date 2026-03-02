def compute_confidence(data):

    score = 1.0

    if data["incident_time"] == "Yesterday evening":
        score -= 0.2

    if data["severity"] == "Very Dangerous":
        score -= 0.1

    return round(score, 2)