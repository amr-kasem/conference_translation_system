from dataclasses import dataclass
from io import BytesIO

@dataclass(frozen=True)  # Makes the class immutable
class VadRequest:
    conference_id:str
    data: BytesIO
