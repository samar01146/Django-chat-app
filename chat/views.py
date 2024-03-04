from django.shortcuts import render
from authentication.models import *
import json
 
# Create your views here.
def chat(request):
    if request.user != None:
        my_contact_lists = CustomUser.objects.all().exclude(username__in=[request.user, "admin"])
        context = {"my_contact_lists":my_contact_lists, "first_obj":my_contact_lists.first()}
        return render(request, 'chat.html', context)
    else:
        return render(request, 'login.html')