import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        print("_____________________connected")
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
        print("data recieved")
        json_text = json.loads(text_data)
        message = json_text['message']
        # self.send(text_data=json.dumps({"message": message})) ////////////without type method
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            {
                "type": "chat_message", 
                "message": message
            }
        )
    # send data from frontend to backend
    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({"message": message}))