from abc import ABC, abstractmethod
from PIL import Image  # Import the Pillow Image class
from typing import Optional

class QRcodeGenerator(ABC):
    
    @abstractmethod
    def get_qr_for_conference(self, conference_id: str) -> Optional[Image]:
        """
        Generate a QR code for a specific conference using its ID.
        
        Args:
            conference_id (str): The ID of the conference for which to generate the QR code.
        
        Returns:
            Image: A PIL Image object representing the QR code for the conference.
            Returns None if the QR code generation fails.
        """
        pass