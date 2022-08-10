from django.urls import path
from .views import *



urlpatterns = [
    path('chats/', ChatView.as_view(), name="chats"),
    path('create-thread/', creatThread, name="create-thread"),
]
