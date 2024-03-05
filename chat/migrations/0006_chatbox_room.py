# Generated by Django 5.0.2 on 2024-03-05 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_room_mytimestamp_alter_room_user1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbox',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sender_id', to='chat.room'),
            preserve_default=False,
        ),
    ]