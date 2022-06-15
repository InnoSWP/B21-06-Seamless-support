from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('dialog/', views.dialog),
    path('home/', views.home)
]
