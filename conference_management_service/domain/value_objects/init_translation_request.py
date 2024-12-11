from dataclasses import dataclass
from typing import Callable, Optional

@dataclass(frozen=True)  # Makes the class immutable
class InitTranslationRequest:
    translation_host: str
    translation_port: int
