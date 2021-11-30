from django.urls import include, path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop_items, name='shop'),
    path('accounts/', include('allauth.urls')),
    path('<slug:slug>', views.item_detail, name='item_detail'),
    path('category/<slug:category_slug>', views.items_category, name='items_category'),
    path('upload/', views.upload_item, name='upload_item'),
    path('edit/<slug:slug>', views.edit_item, name='edit_item'),
    path('delete/<slug:slug>', views.delete_item, name='delete_item'),
    ]
