from django.urls import re_path
from ws.consumer import WSConsumer

websocket_urlpatterns = [
    re_path(r'ws/$', WSConsumer.as_asgi()),
    # Add more URL patterns for your WebSocket consumers
]