from datetime import datetime, timedelta

# Normalize incident_time strings into ISO datetime
def normalize_incident_time(value):
    now = datetime.now()
    if not isinstance(value, str):
        return value

    text = value.lower()

    if "last night" in text:
        return (now - timedelta(days=1)).replace(hour=20, minute=0, second=0, microsecond=0).isoformat()
    elif "yesterday" in text:
        return (now - timedelta(days=1)).replace(hour=18, minute=0, second=0, microsecond=0).isoformat()
    elif "this morning" in text:
        return now.replace(hour=9, minute=0, second=0, microsecond=0).isoformat()
    elif "today" in text:
        return now.replace(microsecond=0).isoformat()
    
    return now.replace(microsecond=0).isoformat()


# Map raw severity strings to standard levels
def correct_severity(value):
    mapping = {
        "very dangerous": "High",
        "dangerous": "Medium",
        "minor": "Low"
    }
    if isinstance(value, str):
        return mapping.get(value.lower(), value)  # default to original if not mapped
    return value


# Run full correction pipeline
def run_corrections(data):

    # Incident time
    if "incident_time" in data:
        data["incident_time"] = normalize_incident_time(data["incident_time"])

    # Report time auto-add
    if "report_time" not in data:
        data["report_time"] = datetime.now().replace(microsecond=0).isoformat()

    # Location fix
    if isinstance(data.get("location"), dict):
        if not data["location"].get("city"):
            data["location"]["city"] = "Unknown"
        if not data["location"].get("state"):
            data["location"]["state"] = "Unknown"
    elif isinstance(data.get("location"), str):
        # naive string → dict conversion if LLM returned string
        data["location"] = {"city": "Unknown", "state": "Unknown"}

    # Severity fix
    if "severity" in data:
        data["severity"] = correct_severity(data["severity"])

    return data