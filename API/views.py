from http.client import responses

from django.shortcuts import render
from rest_framework.fields import empty
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from  rest_framework import status
from  .models import *
from .serializers import *
from rest_framework import  generics
from  rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import authenticate

class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def loginview(request):
    if request.data.get('email')=="" or request.data.get('password')=="":
        return Response({'Invalid':'Please fill all the required fields'},status=400)
    else:
        email =request.data.get('email')
        password = request.data.get('password')

        user=authenticate(username=email,password=password)

        if user is not None:
            refresh =RefreshToken.for_user(user)
            return Response({
                'user':str(email),
                'refresh':str(refresh),
                'access':str(refresh.access_token)
            },status=200
            )
        else:
            return Response({'Invalid':'Check email or password'},status=400)




