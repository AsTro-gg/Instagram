from django.db import models
from django.contrib.auth.models import AbstractUser

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
    phone_number = models.IntegerField(max_length=10,null=True)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.Fullname}({self.username})"