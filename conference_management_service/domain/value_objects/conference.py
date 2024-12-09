from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from domain.value_objects.user import UserData
from domain.value_objects.attendance_data import AttendanceData  # Import datetime for date and time

@dataclass(frozen=True)  # Makes the class immutable
class ConferenceData:
    id: Optional[str]  # User's name (string)
    name: Optional[str]  # User's language (Type of the Language class)
    start: Optional[datetime]
    end: Optional[datetime]
    attendees: list[AttendanceData]
    speaker: Optional[AttendanceData]