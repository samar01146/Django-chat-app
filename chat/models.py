from django.db import models

# Create your models here.
STATUS_CHOICE = (
        ('online', 'online'),
        ('offline', 'offline'),
    )

class User(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to="profile", null=True, blank=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICE)
