from datetime import datetime

def correct_datetime(value):
    if isinstance(value, str):
        if "yesterday" in value.lower():
            return datetime.now().isoformat()
    return value


def correct_location(value):
    if isinstance(value, str):
        # naive correction simulation
        return {
            "city": "Unknown",
            "state": "Unknown"
        }
    return value


def correct_severity(value):
    mapping = {
        "very dangerous": "High",
        "dangerous": "Medium",
        "minor": "Low"
    }
    if isinstance(value, str):
        return mapping.get(value.lower(), "Medium")
    return value


def run_corrections(data):
    if "incident_time" in data:
        data["incident_time"] = correct_datetime(data["incident_time"])

    if "location" in data:
        data["location"] = correct_location(data["location"])

    if "severity" in data:
        data["severity"] = correct_severity(data["severity"])

    return data