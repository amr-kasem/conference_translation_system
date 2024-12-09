from datetime import datetime
from typing import Optional
from presentation.api.dtos.language.language import LanguageDto
from presentation.api.dtos.user.user import UserDto
from pydantic import BaseModel


class AttendanceDto(BaseModel):
    id: str
    user: UserDto
    language: LanguageDto  # Language is now an enum
    start: datetime
    end: Optional[datetime]