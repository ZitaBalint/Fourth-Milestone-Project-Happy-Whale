from django.contrib import admin
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_total, name='cart_total'),
    path('', views.cart_add, name='cart_add')
]
