import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from authentication.models import *
from .models import *

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print("_____________________connected")
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # JOIN ROOM GROUP
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()
    
    def disconnect(self):
        print("_____________________disconnect")
        # LEAVE ROOM GROUP
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.room_name
        )
    # recieved data from frontend to backend
    def receive(self, text_data):
        json_text = json.loads(text_data)
        message = json_text['message']
        user = json_text['user']
        room_id = json_text['room_id']
        
        # self.send(text_data=json.dumps({"message": message})) ////////////without type method
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            {
                "type": "chat_message", 
                "message": message,
                "user":user,
                "room_id":room_id
            }
        )
    # send data from frontend to backend
    def chat_message(self, event):
        user = event['user']
        room_id = event['room_id']
        message = event['message']
        user_obj = CustomUser.objects.get(username=user)
        room_obj = Room.objects.get(room_id=room_id)
        ChatBox.objects.create(user=user_obj,room=room_obj, message=message)
        self.send(text_data=json.dumps({"message": message}))