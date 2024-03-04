import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer


class WSConsumer(AsyncWebsocketConsumer):
    channel_layer = get_channel_layer()

    async def connect(self):
        user = self.scope["user"]
        if user.is_anonymous:
            await self.close()
        else:
            await self.channel_layer.group_add(str(user.id), self.channel_name)
            await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass
