REQUIRED_FIELDS = [
    "incident_type",
    "incident_time",
    "location"
]

def classify_recoverability(raw):
    """
    Determines whether an invalid extraction is realistically repairable
    by deterministic middleware WITHOUT hallucination.
    """

    if not isinstance(raw, dict):
        return "unrecoverable"

    missing = [f for f in REQUIRED_FIELDS if f not in raw]

    # NO- Completely absent : cannot fabricate
    if len(missing) == len(REQUIRED_FIELDS):
        return "unrecoverable"

    # NO- Critical operational data absent
    if "incident_type" not in raw:
        return "unrecoverable"

    # NO- Location absent : unsafe to infer
    if "location" not in raw:
        return "unrecoverable"

    # NO- Time absent entirely : cannot guess
    if "incident_time" not in raw:
        return "unrecoverable"

    time_val = str(raw.get("incident_time", "")).lower()

    # YES- Missing but inferable
    if any(x in time_val for x in [
        "yesterday", "evening", "morning",
        "afternoon", "tonight", "last night"
    ]):
        return "salvageable"

    # YES- Format errors
    if any(x in time_val for x in ["pm", "am", "/", "-"]):
        return "salvageable"

    # YES- Soft inconsistency
    if raw.get("incident_type") == "fire" and raw.get("response_required") == "medical_only":
        return "salvageable"

    return "salvageable"
