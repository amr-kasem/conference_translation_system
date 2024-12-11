from dataclasses import dataclass

from domain.value_objects.attendance_data import AttendanceData
@dataclass(frozen=True)
class JoinRequest:
    attendence: AttendanceData
    conference_id: str