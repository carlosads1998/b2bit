from django.urls import path
from . import views

urlpatterns = [
    path('publi/', views.PubliApi.as_view(), name='Publicação'),
    path('publi/<int:pk>', views.PubliView.as_view(), name='Publicações'),
]
