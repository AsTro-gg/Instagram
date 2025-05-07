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

from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['user', 'text', 'story', 'tags']
        read_only_fields = ['created_at', 'updated_at', 'user']  # user is set from request

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def validate_story(self, value): # Validate(field_name) which needs to be validated
        if value.size > 50 * 1024 * 1024:
            raise serializers.ValidationError("Maximum file size is 50 MB.")
        if not value.name.lower().endswith(('.mp4', '.jpeg', '.png','jpg')):
            raise serializers.ValidationError("Unsupported file format. Only mp4, jpeg, png are allowed.")
        return value

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['user','tags','post','text']
        read_only_fields = ['user','created_at','updated_at']

    def create(self, validated_data):
        validated_data['user']=self.context['request'].user
        return super().create(validated_data)

    def validate_story(self, value):
        if value.size > 50 * 1024 * 1024:
            raise serializers.ValidationError("Maximum file size is 50 MB.")
        if not value.name.lower().endswith(('.mp4', '.jpeg', '.png', 'jpg')):
            raise serializers.ValidationError("Unsupported file format. Only mp4, jpeg, png are allowed.")
        return value