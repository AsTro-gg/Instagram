from os.path import realpath
from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.transaction import mark_for_rollback_on_error


class User(AbstractUser):
    GENDER_CHOICES =[
        ('male','Male'),
        ('female','Female'),
        ('others','Others')
    ]
    email =models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile/',null=True)
    bio = models.TextField(null=True)
    fullname=models.CharField(max_length=100)
    birthdate = models.DateField()
    phone_number = models.IntegerField(null=True)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.Fullname}({self.username})"

class Friends(models.Model):
    status_choices= [
        ('friends','Friends'),
        ('pending','Pending'),
        ('declined','Declined')
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    friend = models.ForeignKey(User,on_delete=models.CASCADE,related_name='friend')
    status = models.CharField(max_length=30,choices=status_choices,default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s friend {self.friend}"

class Story(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    story = models.FileField(upload_to='story/')
    tags = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='tagged')
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s Story on {self.created_at}"

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='tags')
    post = models.FileField(upload_to='post/')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s Post on {self.created_at}"
