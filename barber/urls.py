from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('services', views.services, name='services'),
    path('faq', views.faq, name='faq')
]