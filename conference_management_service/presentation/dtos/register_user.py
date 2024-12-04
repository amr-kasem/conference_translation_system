from pydantic import BaseModel

class RegisterUserDto(BaseModel):
    name: str
    home_language: str  # Language is now an enum