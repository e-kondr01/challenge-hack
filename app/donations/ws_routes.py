from django.urls import path

from .consumers import BalanceConsumer, DonationConsumer

websockets_urlpatterns = [
    path("ws/donations/", DonationConsumer.as_asgi()),
    path("ws/balance/", BalanceConsumer.as_asgi()),
]
