from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

from django.urls import include
from django.shortcuts import render
urlpatterns = [
    path('', home, name='home'),
    path('<str:room_name>/', chat_room, name='chat_room'),
    # path('login/', login, name='login'),
    # path('accounts/', include('allauth.urls')),
]
