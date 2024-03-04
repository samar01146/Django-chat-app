 
from django.urls import path, include
from chat import views as chat_views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

 
 
urlpatterns = [
    path('chat/<str:room_name>/', index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)