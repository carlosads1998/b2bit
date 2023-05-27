from django.urls import path
from . import views

urlpatterns = [
    path('publi/', views.PublicationListApi.as_view(), name='Publicação'),
    path('publi/<int:pk>', views.PublicationDetailView.as_view(), name='Publicações'),
]
