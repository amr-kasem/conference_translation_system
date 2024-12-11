from dataclasses import dataclass

@dataclass(frozen=True)
class RaiseHandRequest:
    attendence: str
    conference_id: str