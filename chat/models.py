from django.db import models
from authentication.models import *
import uuid

class Room(models.Model):
    room_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='User1')
    user2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='User2')
    mytimestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.room_id)
    

class ChatBox(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender_id')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='sender_id')
    message = models.TextField(max_length=250, null=True, blank=True)
    mytimestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user) 
    