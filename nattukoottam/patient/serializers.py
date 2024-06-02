from rest_framework import serializers
from donor.serializers import UserSerializer
from .models import Receiver, Donation



class ReceiverIndexSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Receiver
        fields = ['user','is_receiver']     

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        field = '__all__'   