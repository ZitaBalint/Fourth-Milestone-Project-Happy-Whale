from django.contrib import admin
from django.urls import path, include
from . import views
from . import webhook

app_name = 'checkout'

urlpatterns = [
    path('', webhook.CheckoutView, name='cart'),
    path('ordered/', views.Ordered),
    path('ordersent/', views.order_sent),
    path('webhook/', webhook.stripe_webhook),
]
