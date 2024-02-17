import base64
import json

from channels.generic.websocket import WebsocketConsumer
import ai.emotion

from PIL import Image
import io


class EmotionConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(
        self,
        text_data=None,
        bytes_data=None,
    ):
        emotion = ai.emotion.process_image(io.BytesIO(base64.b64decode(text_data)))
        self.send(text_data=json.dumps({"emotion": emotion}))
