# Generated by Django 4.2.11 on 2024-05-26 02:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0002_alter_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donor',
            old_name='doner',
            new_name='donor',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='certificate',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='points',
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certificate',
            name='Donor',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='donor.donor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='point',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donor.donor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bloodunit',
            name='Donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donor.donor'),
        ),
        migrations.AlterField(
            model_name='point',
            name='point_type',
            field=models.CharField(choices=[('app', 'app'), ('wapp', 'wapp')], default='app', max_length=4),
        ),
    ]