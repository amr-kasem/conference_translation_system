import asyncio
import json
import logging
from typing import Callable
from aiortc import RTCPeerConnection, RTCConfiguration, RTCIceServer, RTCSessionDescription
from aiohttp import ClientSession, WSMsgType, ClientConnectorError
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration
class Config:
    SIGNALING_SERVER = "ws://localhost:8080/ws"
    TURN_SERVER = RTCIceServer(
        urls=["turn:192.168.50.247:3478"],
        username="username",
        credential="password"
    )
    STUN_SERVER = RTCIceServer(
        urls=["stun:stun.l.google.com:19302"]
    )
    SILENCE_THRESHOLD = 3  # Seconds of silence
    AUDIO_OUTPUT_FILE = "received_audio.wav"
    FRAME_RATE = 48000
    TARGET_RATE = 16000
    RECONNECT_DELAY = 5  # Seconds to wait before reconnecting
    MAX_RECONNECT_ATTEMPTS = 3

class WebRTCCallee:
    def __init__(self, conference_id: str):
        self.pc = None
        self.ws = None
        self.closed = False
        self.reconnect_attempts = 0
        self.conference_id = conference_id
        self.allowed_publisher_id = None
        self.ice_candidate_buffer = []
        self._stop_future = None
        self.on_chunk_callback = None

    def set_speaker(self, speaker_id: str):
        self.allowed_publisher_id = speaker_id

    async def initialize(self,on_chunk_callback:Callable):
        """Initialize WebRTC peer connection with proper configuration."""
        config = RTCConfiguration(iceServers=[Config.TURN_SERVER])
        self.pc = RTCPeerConnection(configuration=config)
        self.on_chunk_callback = on_chunk_callback
        # Set up event handlers
        self._setup_event_handlers()

    def _setup_event_handlers(self):
        """Set up all WebRTC event handlers."""
        @self.pc.on("connectionstatechange")
        async def on_connectionstatechange():
            logger.info(f"Connection state changed to: {self.pc.connectionState}")
            if self.pc.connectionState == "failed":
                await self._handle_connection_failure()
            elif self.pc.connectionState == "connected":
                self.reconnect_attempts = 0

        @self.pc.on("track")
        def on_track(track):
            if track.kind == "audio":
                logger.info("Audio track received")
                processor = AudioProcessorTrack(track)
                self.pc.addTrack(processor)

        @self.pc.on("iceconnectionstatechange")
        async def on_iceconnectionstatechange():
            logger.info(f"ICE connection state: {self.pc.iceConnectionState}")

        @self.pc.on("signalingstatechange")
        async def on_signalingstatechange():
            logger.info(f"Signaling state: {self.pc.signalingState}")

    async def connect(self):
        """Establish connection to signaling server and handle WebRTC setup."""
        try:
            if self.closed:
                return

            # await self.initialize()
            async with ClientSession() as session:
                self.ws = await session.ws_connect(
                    f"{Config.SIGNALING_SERVER}?id={self.conference_id}",
                    heartbeat=30.0
                )

                logger.info("Connected to signaling server")
                await self._handle_signaling()

        except ClientConnectorError as e:
            logger.error(f"Failed to connect to signaling server: {e}")
            await self._handle_connection_failure()
        except Exception as e:
            logger.error(f"Unexpected error during connection: {e}")
            await self.close()

    async def _handle_connection_failure(self):
        """Handle WebRTC connection failures with reconnection logic."""
        if self.reconnect_attempts < Config.MAX_RECONNECT_ATTEMPTS:
            self.reconnect_attempts += 1
            logger.info(f"Attempting to reconnect... (Attempt {self.reconnect_attempts})")
            await asyncio.sleep(Config.RECONNECT_DELAY)
            await self.connect()
        else:
            logger.error("Max reconnection attempts reached")
            await self.close()

    async def _handle_peer_failure(self):
        """Handle WebRTC connection failures with reconnection logic."""
        await self.end_call()
        logger.info(f"Ended call with peer")


    async def _handle_signaling(self):
        """Handle WebRTC signaling messages."""
        try:
            async for msg in self.ws:
                if msg.type == WSMsgType.TEXT:
                    data = json.loads(msg.data)
                    await self._process_signaling_message(data)
                elif msg.type == WSMsgType.CLOSED:
                    logger.warning("WebSocket connection closed")
                    break
                elif msg.type == WSMsgType.ERROR:
                    logger.error("WebSocket error")
                    break
        except Exception as e:
            logger.error(f"Signaling error: {e}")
            if not self.closed:
                await self._handle_connection_failure()

    async def _process_signaling_message(self, data):
        """Process individual signaling messages."""
        try:
            # Check sender ID before processing any message
            sender_id = data.get("sender_id")
            if sender_id and sender_id != self.allowed_publisher_id:
                logger.warning(f"Rejecting connection from unauthorized publisher: {sender_id}")
                await self.ws.send_json({
                    "type": "connection_rejected",
                    "target": sender_id,
                    "reason": "Unauthorized publisher"
                })
                return

            if data["type"] == "offer":
                await self._handle_offer(data)
            elif data["type"] == "candidate":
                await self._handle_ice_candidate(data)
            
        except Exception as e:
            logger.error(f"Error processing signaling message: {e}")
            raise

    async def _handle_offer(self, data):
        """Handle incoming SDP offer."""
        try:
            if data.get("sender_id") == self.allowed_publisher_id:
                sdp = RTCSessionDescription(sdp=data["sdp"], type=data["type"])
                await self.pc.setRemoteDescription(sdp)
                logger.info("Remote description set")

                # Process any buffered ICE candidates
                for candidate in self.ice_candidate_buffer:
                    await self.pc.addIceCandidate(candidate)
                self.ice_candidate_buffer.clear()

                # Create and send answer
                answer = await self.pc.createAnswer()
                await self.pc.setLocalDescription(answer)
                await self.ws.send_json({
                    "type": "answer",
                    "sdp": self.pc.localDescription.sdp,
                    "target": self.allowed_publisher_id
                })
            else:
                logger.warning("Rejected offer from unauthorized publisher")

        except Exception as e:
            logger.error(f"Error setting remote description: {e}")
            raise

    async def _handle_ice_candidate(self, data):
        """Handle incoming ICE candidates."""
        try:
            candidate_data = data["candidate"]
            candidate_dict = {
                "candidate": candidate_data["candidate"],
                "sdpMid": candidate_data["sdpMid"],
                "sdpMLineIndex": candidate_data["sdpMLineIndex"]
            }

            if self.pc.remoteDescription:
                await self.pc.addIceCandidate(candidate_dict)
                logger.info("ICE candidate added")
            else:
                self.ice_candidate_buffer.append(candidate_dict)
                logger.info("ICE candidate buffered")

        except Exception as e:
            logger.error(f"Error handling ICE candidate: {e}")

    async def end_call(self):
        if self.pc:
            await self.pc.close()
            
    async def close(self):
        """Safely close all connections and cleanup resources."""
        self.closed = True
        if self.ws and not self.ws.closed:
            await self.ws.close()
        if self._stop_future and not self._stop_future.done():
            self._stop_future.set_result(True)  # Resolve the future to stop `_start`
        print("Stop signal sent.")
            
    async def _start(self):
        await self.connect()
        self._stop_future = asyncio.Future()
        print("Running...")
        try:
            await self._stop_future  # Wait until the stop signal is given
        except asyncio.CancelledError:
            print("Task cancelled.")
        finally:
            print("Stopped.")      
              
    def start(self):
        asyncio.create_task(self._start())
        
    def change_speaker(self,speaker:str):
        self.allowed_publisher_id = speaker