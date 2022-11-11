import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from donations.ws_routes import websockets_urlpatterns as donations_ws_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")


application = ProtocolTypeRouter(
    {
        "websocket": URLRouter(donations_ws_urlpatterns),
    }
)
