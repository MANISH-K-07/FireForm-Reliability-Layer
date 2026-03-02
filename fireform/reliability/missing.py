def detect_missing_fields(data):

    missing = []

    if not data["location"]["city"]:
        missing.append("city")

    if not data["location"]["state"]:
        missing.append("state")

    return missing