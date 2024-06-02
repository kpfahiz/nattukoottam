from rest_framework import serializers
from .models import User, Address, Donor
from patient.models import Receiver

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            phone_number = validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ['weight', 'dob', 'status', 'blood_group']

class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiver
        fields = ['is_receiver']


class UserRegistrationSerializer(serializers.ModelSerializer):

    address     = AddressSerializer()
    donor       = DonorSerializer(required=False)
    receiver    = ReceiverSerializer(write_only=True)
    class Meta:
        model   = User
        fields  = ['phone_number','username','email','first_name','last_name','address','donor','receiver']
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class DonorIndexSerializer(serializers.ModelSerializer):
    donor = UserSerializer()

    class Meta:
        model = Donor
        fields = ['donor', 'weight', 'dob', 'status', 'blood_group']            


        
