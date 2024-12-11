from pydantic import BaseModel

from datetime import datetime
from typing import Optional
from presentation.api.dtos.attendance.attendance import AttendanceDto
from presentation.api.dtos.user.user import UserDto

class ConferenceDto(BaseModel):
    id: str  # User's name (string)
    name: str  # User's language (Type of the Language class)
    start: Optional[datetime]
    end: Optional[datetime]
    attendees: list[AttendanceDto]
    speaker: Optional[UserDto]