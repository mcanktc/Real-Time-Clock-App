from RTCApp.routing import websocket_urlpatterns
from channels.routing import URLRouter


URLRouter(websocket_urlpatterns)

