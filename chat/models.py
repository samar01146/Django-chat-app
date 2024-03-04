from django.db import models
from authentication.models import *

class ChatBox(models.Model):
    senders_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reciepients_user = models.CharField(max_length=100, null=True, blank=True)
    mytimestamp = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.username