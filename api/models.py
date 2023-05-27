from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth import authenticate


class User(AbstractUser):
    username= models.CharField(max_length=100, unique=True)
    password= models.CharField(max_length=100, unique=True)
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['password']
