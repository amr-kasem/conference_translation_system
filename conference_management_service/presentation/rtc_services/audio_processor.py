
from aiortc import  MediaStreamTrack
import numpy as np
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AudioProcessorTrack(MediaStreamTrack):
    
    kind = "audio"

    def __init__(self, track: MediaStreamTrack):
        super().__init__()
        self.track = track

    async def recv(self):
        try:
            frame = await self.track.recv()
            
            # Process audio data
            audio_data = np.frombuffer(frame.to_ndarray(), dtype=np.int16)


            # Save to WAV file
            if audio_data:
                bytes_stream=audio_data.tobytes()
                self.hand
            return frame

        except Exception as e:
            logger.error(f"Error processing audio frame: {e}")
            raise

    def stop(self):
        """Safely close the WAV file and clean up resources."""
        super().stop()
