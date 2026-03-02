from datetime import datetime

def extract_incident_data(user_input):

    return {
        "incident_type": "Fire",
        "incident_time": "Yesterday evening",
        "report_time": datetime.now().isoformat(),
        "severity": "Very Dangerous",
        "location": {
            "city": None,
            "state": None
        },
        "description": user_input
    }