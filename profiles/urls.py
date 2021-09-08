from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('ordered/', views.ordered, name='ordered'),
]
