from dataclasses import dataclass
from typing import List

from domain.value_objects.language import LanguageData

@dataclass(frozen=True)
class UserData:
    id: str
    name: str
    home_language: LanguageData  # Language is now an enum
