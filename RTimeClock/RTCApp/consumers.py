from channels.generic.websocket import AsyncJsonWebsocketConsumer
import asyncio
from django.utils import timezone  

class ClockConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()  
        self.clock_task = asyncio.create_task(self.tick())

    async def tick(self):
        try:
            while True:
                now = timezone.now()
                await self.send_json({"time": str(now)})  
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            pass
