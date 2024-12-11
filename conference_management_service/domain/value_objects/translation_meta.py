from dataclasses import dataclass
from typing import Optional

from domain.value_objects.attendance_data import AttendanceData

@dataclass(frozen=True)  # Makes the class immutable
class TranslationMeta:
    languages: set[str]
    speaker_queue: list[AttendanceData]
    speaker: Optional[str]
