from django.shortcuts import render
from .models import *
import json
 
# Create your views here.
def index(request, room_name):
    my_contact_lists = User.objects.all()
    context = {"room_name":str(room_name), "my_contact_lists":my_contact_lists, "first_obj":my_contact_lists.first()}
    return render(request, 'chat.html', context)