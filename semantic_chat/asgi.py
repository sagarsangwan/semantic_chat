"""
ASGI config for semantic_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

from django.urls import path
from core.consumers import ChatConsumer
import os
from channels.auth import AuthMiddlewareStack
import core.routing
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'semantic_chat.settings')

application = get_asgi_application()
django_asgi_app = get_asgi_application()
# ws_patterns = [
#     path('<str:room_name>/', ChatConsumer.as_asgi()),
# ]

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": AuthMiddlewareStack(

        AuthMiddlewareStack(

            URLRouter(
                core.routing.websocket_urlpatterns

            )
        )
    ),

})
