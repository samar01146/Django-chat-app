from django.contrib import admin
from .models import *
# Register your models here.
# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'user1', 'user2', 'mytimestamp')
    
@admin.register(ChatBox)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('user', 'room_id', 'message', 'mytimestamp')