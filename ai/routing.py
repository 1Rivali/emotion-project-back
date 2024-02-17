from django.urls import re_path
from .consumer import EmotionConsumer

websocket_urlpatterns = [re_path(r"ws/socket-server", EmotionConsumer.as_asgi())]
