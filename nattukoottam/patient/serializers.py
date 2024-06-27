from rest_framework import serializers
from donor.serializers import UserSerializer
from .models import Receiver, Donation, Request, Notification



class ReceiverIndexSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Receiver
        fields = ['user','is_receiver']     

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        field = '__all__'   

class BloodRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'receiver', 'blood_type', 'units_requested']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'donor', 'blood_request']

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'donor', 'blood_request', 'date_donated', 'approved_by_receiver']

