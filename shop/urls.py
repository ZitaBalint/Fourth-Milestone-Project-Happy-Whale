from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop_items, name='shop'),
    path('accounts/', include('allauth.urls')),
    path('item/<slug:slug>', views.item_detail, name='item_detail'),
    path('category/<slug:category_slug>', views.items_category, name='items_category'),
    path('add/', views.add_item, name='add_item'),
    ]
