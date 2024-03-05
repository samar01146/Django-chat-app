from django.shortcuts import render
from authentication.models import *
from .models import *
from django.http import JsonResponse
import json
# Create your views here.
def chat(request):
    if request.user != None:
        my_contact_lists = CustomUser.objects.all().exclude(username__in=[request.user, "admin"])
        context = {"my_contact_lists":my_contact_lists, "first_obj":my_contact_lists.first()}
        return render(request, 'chat.html', context)
    else:
        return render(request, 'login.html')
    


def CreateRoom(request):
    sender_name = request.GET.get('sender_name')
    receiver_name = request.GET.get('receiver_name')
    sender_obj = CustomUser.objects.get(username=sender_name)
    reciever_obj = CustomUser.objects.get(username=receiver_name)
    room_obj = Room.objects.filter(user1__in=[sender_obj.id, reciever_obj.id], user2__in=[reciever_obj.id, sender_obj.id])
    if not room_obj.exists():
        Room.objects.get_or_create(user1=sender_obj, user2=reciever_obj)
        message, token = "Room created sucessfully", room_obj.first().room_id
    else:
        message, token = "Room already created", room_obj.first().room_id   
    return JsonResponse({"message": message, "token":token})