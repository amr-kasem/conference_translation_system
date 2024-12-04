from dataclasses import dataclass
@dataclass(frozen=True)
class UserRegister:
    name: str
    home_language: str  # Language is now an enum 