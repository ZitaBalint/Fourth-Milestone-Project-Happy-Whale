from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Profile, name='profile'),
    path('order_history/<order_key', views.order_history, name='order_history'),
]
