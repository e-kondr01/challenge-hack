import json

from channels.generic.websocket import (
    AsyncJsonWebsocketConsumer as IncorrectEncodingConsumer,
)
from users.models import User


class AsyncJsonWebsocketConsumer(IncorrectEncodingConsumer):
    """
    Переопределяет AsyncJsonWebsocketConsumer, чтобы он правильно кодировал
    кириллицу.
    """

    @classmethod
    async def encode_json(cls, content):
        return json.dumps(content, ensure_ascii=False)


def get_donation_consumer_group_name(user: User) -> str:
    """
    Возвращает название группы Channels для донатов пользователю.
    """

    return f"donations-{user.pk}"


class DonationConsumer(AsyncJsonWebsocketConsumer):
    """
    Consumer для отправки новых донатов, приходящих пользователю.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = ""

    async def donation_new(self, event):
        await self.send_json(event["data"])

    async def connect(self):
        if not self.scope["user"].is_anonymous:
            # Принимаем только авторизованных пользователей
            self.group_name = get_donation_consumer_group_name(self.scope["user"])

            await self.channel_layer.group_add(self.group_name, self.channel_name)
            await self.accept()

        else:
            await self.close()

    async def disconnect(self, _):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
