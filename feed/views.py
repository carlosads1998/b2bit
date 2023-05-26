from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class feedApi(generics.ListAPIView):
    queryset= models.publi.objects.all()
    serializer_class=serializers.feedSerializer
    filter_backends= [DjangoFilterBackend]
    filterset_fields=['user']
    