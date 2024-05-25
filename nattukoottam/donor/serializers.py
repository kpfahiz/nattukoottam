from rest_framework import serializers
from .models import User, Address, Donor
from patient.models import Reciever

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username= validated_data['username'],
            phone_number = validated_date['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model1 = Address
        fields1 = ['address1','address_2','town','district','state','pincode']

        model2 = Donor
        fields2 = ['place','blood_group','phone_number','weight','dob','date_last_donation']

        model3 = Reciever
        fields3 = ['user']
        

        def create(self, validation_data):
            Address(
                address1 = validation_data['address1'],
                address_2 = validation_data['address_2'],
                town = validation_data['town'],
                district = validation_data['district'],
                state = validation_data['state'],
                pincode = validation_data['pincode']
            )

            


        
