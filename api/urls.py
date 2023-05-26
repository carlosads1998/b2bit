from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.ProfileList.as_view(), name='registro'),
    path('registro/<int:pk>', views.ProfileList.as_view(), name='registro'),
]
