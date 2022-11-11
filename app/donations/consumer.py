from channels.generic.websocket import AsyncJsonWebsocketConsumer


class DonationConsumer(AsyncJsonWebsocketConsumer):
    async def new_donation(self, event):
        await self.send_json(event["data"])

    async def connect(self):

        self.group_name = "donations"

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
