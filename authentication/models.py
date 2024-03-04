from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
STATUS_CHOICE = (
        ('online', 'online'),
        ('offline', 'offline'),
    )
class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to="profile", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICE, default="online")

    def __str__(self):
        return self.username