from dataclasses import dataclass
from io import BytesIO
from typing import Callable

from domain.entities.conference import Conference

@dataclass(frozen=True)  # Makes the class immutable
class InitializeConferenceRequest:
    conference_id: str
    on_speaker_change: Callable[[str],None]
