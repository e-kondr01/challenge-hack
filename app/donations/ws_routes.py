from django.urls import path

from .consumer import DonationConsumer

websockets_urlpatterns = [
    path("ws/donations/", DonationConsumer.as_asgi()),
]
