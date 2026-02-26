from fireform.schemas.incident_schema import IncidentReport
from pydantic import ValidationError

def validate_incident(data):
    try:
        validated = IncidentReport(**data)
        return validated.dict(), None
    except ValidationError as e:
        return None, e.errors()