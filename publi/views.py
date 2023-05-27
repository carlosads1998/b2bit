from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics, permissions

class PublicationListApi(generics.ListCreateAPIView):
    queryset=models.publi.objects.all()
    serializer_class= serializers.publiSerializers
    #permission_classes=(permissions.IsAuthenticated,)

class PublicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.publi.objects.all()
    serializer_class= serializers.publiSerializers
    #permission_classes=(permissions.IsAuthenticated,)
