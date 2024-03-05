 
from django.urls import path, include
from chat import views as chat_views
from .views import *


 
 
urlpatterns = [
    path('', chat, name='chat'),
    path('create_room/', CreateRoom, name='create_room'),
]