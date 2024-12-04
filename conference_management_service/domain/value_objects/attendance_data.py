from dataclasses import dataclass
from datetime import datetime

from domain.value_objects.user import UserData
from domain.value_objects.language import LanguageData
@dataclass(frozen=True)
class AttendanceData:
    id: str
    user: UserData
    language: LanguageData  # Language is now an enum
    start: datetime
    end: datetime