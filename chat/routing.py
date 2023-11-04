from django.urls import path,re_path
from .consumers import DashboardConsumerView

websocket_urlpatterns = [    

    path("ws/view/<dashboard_slug>/", DashboardConsumerView.as_asgi()),
]

# quiero implementar una autenticacion en django channels
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
