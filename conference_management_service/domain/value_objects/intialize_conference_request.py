from dataclasses import dataclass
from typing import Callable

from conference_management_service.domain.value_objects.speaker_change_data import SpeakerChangeData

@dataclass(frozen=True)  # Makes the class immutable
class InitializeConferenceRequest:
    conference_id: str
    on_speaker_change: Callable[[SpeakerChangeData],None]
