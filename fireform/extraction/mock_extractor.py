from datetime import datetime
import random
import hashlib


def extract_incident_data(user_input):
    """
    Simulates an LLM extraction of incident data.
    Deterministic chaos injection to test reliability layer.
    """

    # Deterministic seed based on input
    seed = int(hashlib.md5(user_input.encode()).hexdigest(), 16) % (10**8)
    random.seed(seed)

    text = user_input.lower()

    # -------- Incident Type --------
    if "fire" in text or "smoke" in text:
        incident_type = "Fire"
    elif "explosion" in text:
        incident_type = "Explosion"
    elif "gas" in text or "leak" in text:
        incident_type = "Gas Leak"
    else:
        incident_type = "Unknown"

    # -------- Severity --------
    if "massive" in text or "casualties" in text or "dangerous" in text:
        severity = "Very Dangerous"
    elif "minor" in text or "small" in text:
        severity = "Minor"
    else:
        # **Do NOT default to Medium for garbage input**
        severity = None

    # -------- Time --------
    if "yesterday" in text:
        incident_time = "Yesterday evening"
    elif "morning" in text:
        incident_time = "Today morning"
    elif "night" in text:
        incident_time = "Last night"
    else:
        incident_time = datetime.now().isoformat()

    data = {
        "incident_type": incident_type,
        "severity": severity,
        "incident_time": incident_time,
        "location": {
            "city": None,
            "state": None
        },
        "description": user_input
    }

    # ---------- CHAOS INJECTION ----------
    if random.random() < 0.3:
        data.pop("location")
    elif random.random() < 0.2:
        data["location"] = "Near downtown mall"

    if random.random() < 0.15:
        data["severity"] = "extremely bad"

    if random.random() < 0.2:
        data.pop("severity")

    if random.random() < 0.25:
        data["incident_time"] = "32nd of Feb"

    if random.random() < 0.3:
        data.pop("incident_time")

    if random.random() < 0.4:
        pass
    else:
        data["report_time"] = datetime.now()

    return data
