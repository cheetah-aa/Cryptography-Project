from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('caesar/', views.caesar, name='caesar'),
    path('vigenere/', views.vigenere, name='vigenere'),
]