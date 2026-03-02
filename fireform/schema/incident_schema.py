from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Location(BaseModel):
    city: Optional[str]
    state: Optional[str]

class IncidentReport(BaseModel):
    incident_type: str
    incident_time: datetime
    report_time: datetime
    severity: str
    location: Location
    description: Optional[str]