# Generated by Django 4.2.11 on 2024-05-26 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_rename_reciever_receiver'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receiver',
            old_name='is_reciever',
            new_name='is_receiver',
        ),
    ]
