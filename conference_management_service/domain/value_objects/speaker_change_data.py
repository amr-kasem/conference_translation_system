from dataclasses import dataclass

@dataclass(frozen=True)  # Makes the class immutable
class SpeakerChangeData:
    speaker_id: str
    conference_id: str