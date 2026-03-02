def detect_missing_fields(data):

    missing = []

    # -------- INCIDENT TYPE --------
    if not data.get("incident_type"):
        missing.append("incident_type")

    # -------- SEVERITY --------
    if not data.get("severity"):
        missing.append("severity")

    # -------- INCIDENT TIME --------
    if not data.get("incident_time"):
        missing.append("incident_time")

    # -------- REPORT TIME --------
    if not data.get("report_time"):
        missing.append("report_time")

    # -------- LOCATION --------
    location = data.get("location")

    # location missing OR wrong datatype
    if not isinstance(location, dict):
        missing.extend(["city", "state"])

    else:
        if not location.get("city"):
            missing.append("city")
        if not location.get("state"):
            missing.append("state")

    return missing
