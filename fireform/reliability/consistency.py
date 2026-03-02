from datetime import datetime

def check_consistency(data):

    errors = []
    warnings = []

    # 🔴 Rule: Explosion cannot be Low severity
    if data.get("incident_type") == "Explosion":
        if data.get("severity") in ["Low", "Minor"]:
            errors.append("Explosion cannot have Low severity")

    # 🔴 Rule: Fire + casualties → should not be Low
    desc = data.get("description", "").lower()
    if data.get("incident_type") == "Fire":
        if "casualty" in desc or "death" in desc:
            if data.get("severity") in ["Low", "Medium"]:
                warnings.append("Fire with casualties should have High severity")

    # 🔴 Rule: High severity but description suggests no impact
    if data.get("severity") == "High":
        if any(phrase in desc for phrase in ["no damage", "minor impact", "no injuries"]):
            warnings.append("High severity conflicts with low-impact description")
    if "severe" in desc and data.get("severity") in ["Low", "Medium"]:
        warnings.append("Description indicates severe event but severity not High")

    # 🔴 Rule: Incident time cannot be in future
    incident_time = data.get("incident_time")
    if isinstance(incident_time, datetime):
        if incident_time > datetime.now():
            errors.append("Incident time is in the future")

    # 🔴 Rule: Report time before incident time
    report_time = data.get("report_time")
    if isinstance(report_time, datetime) and isinstance(incident_time, datetime):
        if report_time < incident_time:
            errors.append("Report time cannot be before incident time")

    return {
        "consistency_errors": errors,
        "consistency_warnings": warnings
    }
