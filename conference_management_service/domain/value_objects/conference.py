from dataclasses import dataclass
from datetime import datetime  # Import datetime for date and time
@dataclass(frozen=True)  # Makes the class immutable
class ConferenceData:
    id: str  # User's name (string)
    name: str  # User's language (Type of the Language class)
    start: datetime
    end: datetime
    running: bool