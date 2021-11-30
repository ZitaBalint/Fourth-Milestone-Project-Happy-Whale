from django.urls import path

from . import views, webhook

app_name = 'checkout'

urlpatterns = [
    path('', views.CheckoutFormView.as_view(), name='cart'),
    path('ordered/', views.CheckoutFormView.as_view()),
    path('ordersent/', views.order_sent),
    path('webhook/', webhook.stripe_webhook),
]
