# Generated by Django 5.0.2 on 2024-03-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('online', 'online'), ('offline', 'offline')], default='online', max_length=8),
        ),
    ]