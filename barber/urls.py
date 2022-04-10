from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('services', views.services, name='services')
]