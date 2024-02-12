from django.urls import path
from .consumers import TaskStatusConsumer

websocket_urlpatterns = [
    path('ws/task-status/', TaskStatusConsumer.as_asgi()),
]


