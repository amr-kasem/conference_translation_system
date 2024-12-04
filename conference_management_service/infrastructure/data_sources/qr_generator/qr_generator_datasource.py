import qrcode
from PIL import Image

class QRcodeGeneratorImpl(QRcodeGenerator):
    
    def get_qr_for_conference(self, conference_id: str) -> Optional[Image]:
        """
        Generate a QR code for the conference with the given ID.
        
        Args:
            conference_id (str): The ID of the conference to generate the QR code for.
        
        Returns:
            Image: A PIL Image object containing the QR code.
            Returns None if generation fails.
        """
        try:
            # Create a QR Code with the conference ID as data
            qr = qrcode.QRCode(
                version=1,  # Control the size of the QR code
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(conference_id)
            qr.make(fit=True)
            
            # Create an image from the QR Code
            img = qr.make_image(fill='black', back_color='white')
            return img
        except Exception as e:
            print(f"Failed to generate QR code: {e}")
            return None
