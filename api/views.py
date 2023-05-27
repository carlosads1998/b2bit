from django.shortcuts import render
from rest_framework import generics, serializers, permissions
from . import serializers
from . import models



class ProfileList(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class= serializers.ProfileSerializer
  #  permission_classes = (permissions.IsAuthenticated,)
