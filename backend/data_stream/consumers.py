from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TaskStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "task_status",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "task_status",
            self.channel_name
        )

    async def send_task_status(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
