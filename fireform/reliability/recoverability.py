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

    # ❌ Completely absent → cannot fabricate
    if len(missing) == len(REQUIRED_FIELDS):
        return "unrecoverable"

    # ❌ Critical operational data absent
    if "incident_type" not in raw:
        return "unrecoverable"

    # ❌ Location absent → unsafe to infer
    if "location" not in raw:
        return "unrecoverable"

    # ❌ Time absent entirely → cannot guess
    if "incident_time" not in raw:
        return "unrecoverable"

    time_val = str(raw.get("incident_time", "")).lower()

    # ✅ Missing but inferable
    if any(x in time_val for x in [
        "yesterday", "evening", "morning",
        "afternoon", "tonight", "last night"
    ]):
        return "salvageable"

    # ✅ Format errors
    if any(x in time_val for x in ["pm", "am", "/", "-"]):
        return "salvageable"

    # ✅ Soft inconsistency
    if raw.get("incident_type") == "fire" and raw.get("response_required") == "medical_only":
        return "salvageable"

    return "salvageable"
