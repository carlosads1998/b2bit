from django.shortcuts import render
from rest_framework import generics, serializers, permissions

from . import models


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username', 'password')


class ProfileList(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class= ProfileSerializer
  #  permission_classes = (permissions.IsAuthenticated,)
