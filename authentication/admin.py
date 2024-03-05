from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'status', 'photo')