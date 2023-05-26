from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics, permissions

class PubliApi(generics.ListCreateAPIView):
    queryset=models.publi.objects.all()
    serializer_class= serializers.publiSerializers
    #permission_classes=(permissions.IsAuthenticated,)

class PubliView(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.publi.objects.all()
    serializer_class= serializers.publiSerializers
    #permission_classes=(permissions.IsAuthenticated,)
