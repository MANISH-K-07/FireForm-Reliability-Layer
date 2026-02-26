def detect_missing_fields(data):
    missing = []
    required = ["incident_type", "incident_time", "severity", "location"]

    for field in required:
        if field not in data or data[field] is None:
            missing.append(field)

    return missing