from dataclasses import dataclass
from typing import List

from domain.entities.language import Language

@dataclass(frozen=True)
class UserData:
    id: str
    name: str
    home_language: Language  # Language is now an enum
