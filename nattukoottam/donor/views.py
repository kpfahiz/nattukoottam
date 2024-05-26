from django.shortcuts import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSignUpSerializer, UserRegisterSerializer
from .models import User

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
                "username": phone_number
                }
            }

            return Response(contex, status=status.HTTP_200_OK)
        contex = {
            "status": "failure",
            "errorInfo": "Invalid credentials",
            "result": None
            }
        return Response(contex, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['POST'])
def user_register(request):
    if request.method == 'POST':
        serializer    = UserRegisterSerializer
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
                "errorInfo": "Something wrong please",
                "result": None
            }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
            

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