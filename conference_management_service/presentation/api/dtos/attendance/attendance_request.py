from pydantic import BaseModel

class AttendanceRequestDto(BaseModel):
    user: str
    language: str  # Language is now an enum
