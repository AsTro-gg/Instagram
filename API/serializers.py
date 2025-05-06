from  rest_framework import serializers
from  .models import *

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['email','username','password','birthdate','phone_number','fullname','gender']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            birthdate=validated_data['birthdate'],
            phone_number=validated_data['phone_number'],
            fullname=validated_data['fullname'],
            gender=validated_data['gender']
        )
        return user


