from django.contrib import admin
from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.shop_items, name='shop'),
    path('item/<slug:slug>', views.item_detail, name='item_detail'),
    path('category/<slug:category_slug>', views.items_category, name='items_category'),
]
