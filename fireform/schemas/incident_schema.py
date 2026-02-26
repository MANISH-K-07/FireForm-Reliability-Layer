from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Location(BaseModel):
    city: str
    state: str

class IncidentReport(BaseModel):
    incident_type: str
    incident_time: datetime
    severity: str
    location: Location
    description: Optional[str] = None