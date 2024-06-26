# Generated by Django 4.2.11 on 2024-06-29 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0002_alter_user_managers_remove_bloodunit_donor_and_more'),
        ('patient', '0002_remove_request_donors_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiver',
            name='fcm_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='fulfilled',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('blood_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.request')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donor.donor')),
            ],
        ),
    ]
