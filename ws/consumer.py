from channels.generic.websocket import AsyncWebsocketConsumer


class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Perform connection setup, authentication, etc.
        await self.accept()

    async def disconnect(self, close_code):
        # Perform cleanup on disconnect
        pass

    async def receive(self, text_data):
        # Handle incoming messages from the WebSocket
        print(text_data)
