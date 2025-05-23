from http.client import responses
from turtledemo.sorting_animate import start_ssort

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


class StoryAPIview(generics.GenericAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_class =[IsAuthenticated]

    def get_queryset(self):
        return Story.objects.filter(user=self.request.user)

    def get(self,request):
        model = self.get_queryset()
        serializer = self.get_serializer(model,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StoryDynamicAPIview(generics.GenericAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def delete(self, request,*args,**kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'Successfully Deleted'},status=status.HTTP_204_NO_CONTENT)

    def put(self,request,*args,**kwargs):
        instance = self.get_object()
        serializers = self.get_serializer(instance,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)



class PostAPIview(generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

    def get(self, request):
        model = self.get_queryset()
        serializer = self.get_serializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDynamicAPIview(generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def delete(self,request,*args,**kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'Successfully Deleted'},status=status.HTTP_204_NO_CONTENT)

    def put(self,request,*args,**kwargs):
        instance = self.get_object()
        serializers = self.get_serializer(instance,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)