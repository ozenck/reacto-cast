from celery import shared_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import time

@shared_task
def my_long_running_task():
    channel_layer = get_channel_layer()
    for i in range(1,4):
        async_to_sync(channel_layer.group_send)(
            "task_status", {"type": "send_task_status", "message": {"status": f"Task-{i} Started"}}
        )
        
        time.sleep(10)

        async_to_sync(channel_layer.group_send)(
            "task_status", {"type": "send_task_status", "message": {"status": f"Task-{i} Completed"}}
        )
