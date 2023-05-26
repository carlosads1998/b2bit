from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feedApi.as_view(), name='feed'),
]