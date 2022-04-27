from django.urls import path
from . import views

urlpatterns = [
    path('login', views.CustomLoginView.as_view(), name='login'),
    path('logout', views.logoutUser , name='logout'),
    path('register', views.RegisterPage.as_view(), name='register'),
    
    path('', views.main, name='main'),
    path('services', views.services, name='services'),
    path('faq', views.faq, name='faq'),
    path('booking', views.booking, name='booking'),
    path('join', views.join, name='join'),
    path('team', views.team, name='team'),
    path('about', views.about, name='about'),
    path('add_comment', views.addComment, name='add_comment'),
    
]