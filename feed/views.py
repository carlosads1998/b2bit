from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from . import models
from publi.models import publi


class FeedListApi(generics.ListAPIView):
    serializer_class=serializers.feedSerializer
    filter_backends= [DjangoFilterBackend]
    filterset_fields=['author']
    permission_classes=(permissions.IsAuthenticated,)
    
    def get_queryset(self):
        user = self.request.user
        queryset = publi.objects.exclude(author=user)
        return queryset