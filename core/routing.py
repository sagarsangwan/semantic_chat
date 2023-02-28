from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    path('<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]
