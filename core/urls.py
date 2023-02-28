from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

from django.urls import include
from django.shortcuts import render
app_name = 'chat'
urlpatterns = [
    path('', home, name='home'),
    path('new_chat_room/<int:user_id>/', new_chat_room, name='new_chat_room'),
    path('<slug:slug>/', chat_room, name='chat_room'),
    # path('login/', login, name='login'),
    # path('accounts/', include('allauth.urls')),
]
