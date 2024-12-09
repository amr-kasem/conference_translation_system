from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from domain.value_objects.user import UserData
from domain.value_objects.language import LanguageData
@dataclass(frozen=True)
class AttendanceData:
    id: str
    user: UserData
    language: LanguageData  # Language is now an enum
    start: Optional[datetime]
    end: Optional[datetime]
    def __eq__(self, other):
        if isinstance(other, AttendanceData):
            return self.id == other.id
        return False