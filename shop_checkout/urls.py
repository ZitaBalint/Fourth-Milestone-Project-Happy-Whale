from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.CheckoutView, name='cart'),
    path('ordersent/', views.order_sent)
]
