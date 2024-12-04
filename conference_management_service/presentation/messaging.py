import nats

class MessagingServices:
    def __init__(self):
        self.nats_client = None

    def init(self, host: str='localhost', port: int =4222):
        self.nats_url = f"nats://{host}:{port}"
        
    async def connect(self):
        """Connect to the NATS server and subscribe to a subject."""
        self.nats_client = await nats.connect(self.nats_url)
        print(f"Connected to NATS at {self.nats_url}")

        # Example: Subscribe to a subject
        async def message_handler(msg):
            print(f"Received message: {msg.data.decode()}")

        await self.nats_client.subscribe("updates", cb=message_handler)

    async def publish_message(self, subject: str, message: str):
        """Publish a message to a NATS subject."""
        if self.nats_client:
            await self.nats_client.publish(subject, message.encode())
            print(f"Sent '{message}' to NATS subject '{subject}'")
        else:
            raise Exception("NATS client is not connected")

    async def close(self):
        """Gracefully close the NATS client connection."""
        if self.nats_client:
            await self.nats_client.close()
            print("NATS connection closed.")

