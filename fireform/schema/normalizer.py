from datetime import datetime


def normalize_severity(data):

    severity = data.get("severity")

    # Already valid — keep it
    if severity in ["Minor", "Medium", "High"]:
        return severity

    desc = (data.get("description") or "").lower()

    # Semantic recovery from description
    if any(word in desc for word in ["severe", "massive", "dangerous", "casualties"]):
        return "High"

    elif any(word in desc for word in ["minor", "small"]):
        return "Minor"

    else:
        return "Medium"


def normalize_extracted_json(data: dict) -> dict:

    # -------------------------------
    # 1. INCIDENT TIME
    # -------------------------------
    if "incident_time" not in data:
        data["incident_time"] = None

    # -------------------------------
    # 2. LOCATION STRUCTURE
    # -------------------------------
    if "location" not in data:
        data["location"] = {"city": None, "state": None}

    elif isinstance(data["location"], str):
        data["location"] = {"city": None, "state": None}

    elif isinstance(data["location"], dict):
        data["location"].setdefault("city", None)
        data["location"].setdefault("state", None)

    # -------------------------------
    # 3. REPORT TIME
    # -------------------------------
    if "report_time" not in data:
        data["report_time"] = datetime.utcnow()

    # -------------------------------
    # 4. INCIDENT TYPE
    # -------------------------------
    data.setdefault("incident_type", None)

    # -------------------------------
    # 5. DESCRIPTION
    # -------------------------------
    data.setdefault("description", "")

    # -------------------------------
    # 6. SEVERITY RECOVERY
    # -------------------------------
    data["severity"] = normalize_severity(data)

    return data
