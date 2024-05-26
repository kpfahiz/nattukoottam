from rest_framework import serializers
from .models import User, Address, Donor
from patient.models import Reciever

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
        model   = Address
        fields  = '__all__'

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Donor
        fields  = ['wieght','dob','blood_group']

class RecieverSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Reciever
        fields  = '__all__'
class UserRegisterSerializer(serializers.ModelSerializer):

    address     = AddressSerializer()
    donor       = DonorSerializer()
    reciever    = RecieverSerializer()
    class Meta:
        model   = User
        fields  = ['username','email','first_name','last_name','address','donor','reciever']

        def create(self, validated_data):
            address_data    = validated_data.pop('address')
            if validated_data['is_donor']:
                validated_data.pop('is_donor')
                donor_data      = validated_data.pop('donor')
                user            = User.objects.create(**validated_data)
                Donor.objects.create(donor=user, **donor_data)
            else:
                validated_data.pop('is_donor')
                reciever_data   = validated_data.pop('reciever')
                user            = User.objects.create(**validated_data)
                Reciever.objects.create(user=user, **reciever_data)
            return user
            




            user = User.objects.create(**validated_data)
            Address.objects.create(user=user, **address_data)
            return user
        

            


        
