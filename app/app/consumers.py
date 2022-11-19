import json

from channels.generic.websocket import (
    AsyncJsonWebsocketConsumer as IncorrectEncodingConsumer,
)


class AsyncJsonWebsocketConsumer(IncorrectEncodingConsumer):
    """
    Переопределяет AsyncJsonWebsocketConsumer, чтобы он правильно кодировал
    кириллицу.
    """

    @classmethod
    async def encode_json(cls, content):
        return json.dumps(content, ensure_ascii=False)
