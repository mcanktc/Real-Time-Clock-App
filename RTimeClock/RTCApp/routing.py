from django.urls import path
from RTCApp.consumers import ClockConsumer

websocket_urlpatterns = [

    path("ws/clock/", ClockConsumer.as_asgi()),

]