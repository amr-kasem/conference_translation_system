from dataclasses import dataclass

@dataclass(frozen=True)
class StopSpeakingRequest:
    attendence: str
    conference_id: str