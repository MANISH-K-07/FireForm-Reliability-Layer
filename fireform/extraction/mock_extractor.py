from datetime import datetime

def extract_incident_data(user_input):

    text = user_input.lower()

    # -------- Incident Type Detection --------
    if "fire" in text or "smoke" in text:
        incident_type = "Fire"
    elif "explosion" in text:
        incident_type = "Explosion"
    elif "gas" in text or "leak" in text:
        incident_type = "Gas Leak"
    else:
        incident_type = "Unknown"

    # -------- Severity Detection --------
    if "massive" in text or "casualties" in text or "dangerous" in text:
        severity = "Very Dangerous"
    elif "minor" in text or "small" in text:
        severity = "Minor"
    else:
        severity = "Medium"

    # -------- Time Detection --------
    if "yesterday" in text:
        incident_time = "Yesterday evening"
    elif "morning" in text:
        incident_time = "Today morning"
    elif "night" in text:
        incident_time = "Last night"
    else:
        incident_time = datetime.now().isoformat()

    return {
        "incident_type": incident_type,
        "severity": severity,
        "incident_time": incident_time,
        "location": {
            "city": None,
            "state": None
        },
        "description": user_input
    }