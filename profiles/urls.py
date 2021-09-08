from django.urls import path
from . import views

app_name = 'ordered'

urlpatterns = [
    path('ordered/', views.ordered, name='ordered'),
]
