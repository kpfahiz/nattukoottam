from django.shortcuts import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import UserSignUpSerializer, UserRegistrationSerializer
from .models import User, Donor, Address
from patient.models import Receiver

@api_view(['POST'])
def user_signup(request):
    if request.method == 'POST':
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "status": "success",
                "errorInfo": None,
                "result": {
                "data":  serializer.data
                }
            }
            return Response(context, status=status.HTTP_201_CREATED)
        context = {
                "status": "failure",
                "errorInfo": "A user with same Mobile Number or Password already exist",
                "result": None
            }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        user = None   
        try:
            user = User.objects.get(phone_number=phone_number)
        except ObjectDoesNotExist:
            pass

        if not user:
            user = authenticate(phone_name=phone_number, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            contex = {
                "status": "success",
                "errorInfo": None,
                "result": {
                "token":  token.key,
                "phone_number": phone_number
                }
            }

            return Response(contex, status=status.HTTP_200_OK)
        contex = {
            "status": "failure",
            "errorInfo": "Invalid credentials",
            "result": None
            }
        return Response(contex, status=status.HTTP_401_UNAUTHORIZED)
    
  
class UserUpdateAPIView(APIView):
    def put(self, request):
        phone_number = request.data.get('phone_number')

        try:
            user = User.objects.get(phone_number=phone_number)
            print('User===',user)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserRegistrationSerializer(user, data=request.data)
        if serializer.is_valid():
            
            address_data        = serializer.validated_data['address']
            address             = Address.objects.create(**address_data)

            user.username       = serializer.validated_data.get('username')
            user.username       = serializer.validated_data.get('username')
            user.email          = serializer.validated_data.get('email')
            user.first_name     = serializer.validated_data.get('first_name')
            user.last_name      = serializer.validated_data.get('last_name')
            user.address        = address
            user.save()
            print(serializer.validated_data.get('username'))
            print('username===',serializer.validated_data.get('username'))

            if serializer.validated_data['receiver']['is_receiver']:
                receiver_data   = serializer.validated_data['receiver']
                Receiver.objects.create(user=user, **receiver_data)
            elif serializer.validated_data['donor'] is not None:
                donor_data      = serializer.validated_data['donor']
                donor=Donor.objects.create(donor=user, 
                                     weight=donor_data['weight'],
                                     dob=donor_data['dob'],
                                     blood_group=donor_data['blood_group']
                                     )
            context = {
                "status": "success",
                "errorInfo": None,
                "result": {
                "data":  serializer.data
                }
            }
            return Response(context, status=status.HTTP_201_CREATED)
        else:
            context = {
                "status": "failure",
                "errorInfo": "Something wrong please",
                "result": serializer.errors
            }
            print(serializer.errors)  # Print serializer errors for debugging
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                 

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            contex = {
            "status": "failure",
            "errorInfo": None,
            "result": {
                    'message': 'Successfully logged out.'
                }
            }
            return Response(contex, status=status.HTTP_200_OK)
        except Exception as e:
            contex = {
            "status": "failure",
            "errorInfo": str(e),
            "result": None
            }
            return Response(contex, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
def index(request):
     return HttpResponse("Http request is: "+request.method)  