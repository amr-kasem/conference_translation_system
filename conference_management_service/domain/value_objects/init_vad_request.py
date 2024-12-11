from dataclasses import dataclass
from typing import Callable, Optional

@dataclass(frozen=True)  # Makes the class immutable
class InitVadRequest:
    on_voice_recieved: Optional[Callable]
    vad_host: str
    vad_port: int
