# Generated by Django 4.2.11 on 2024-05-26 06:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient', '0003_reciever_is_reciever'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reciever',
            new_name='Receiver',
        ),
    ]
