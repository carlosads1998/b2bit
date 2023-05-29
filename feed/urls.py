from django.urls import path
from . import views

urlpatterns = [
   path('feed/', views.FeedListApi.as_view(), name='feed'),

]