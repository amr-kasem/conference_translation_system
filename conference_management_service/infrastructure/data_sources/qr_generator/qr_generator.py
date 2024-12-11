from abc import ABC, abstractmethod
from io import BytesIO
from typing import Optional

class QRcodeGenerator(ABC):
    
    @abstractmethod
    def get_qr_for_conference(self, conference_id: str) -> Optional[BytesIO]:
        """
        Generate a QR code for a specific conference using its ID.
        
        Args:
            conference_id (str): The ID of the conference for which to generate the QR code.
        
        Returns:
            Image: A PIL Image object representing the QR code for the conference.
            Returns None if the QR code generation fails.
        """
        pass