from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth import authenticate


class User(AbstractUser):
    pass


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)