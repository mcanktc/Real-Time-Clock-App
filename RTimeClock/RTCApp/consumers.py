from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ClockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.clock
        return await self.accept()
    