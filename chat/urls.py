from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'chat'
urlpatterns = [
    
    path("", views.register_view, name="register_view"),
    path("chat/", views.index_view, name="index_view"),
    path("chat/<room_name>", views.room_view, name="room_view"),
    path('signoff/',views.SignOff,name='signoff'),
]
