from re import template
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
     path('', views.home, name='home'),
     path('login/', auth_views.LoginView.as_view(template_name= "home/signin.html"),   name='login' ),
     path('login/home/', views.home, name='home'), 
     path('addphoto/', views.addphoto, name='addphoto'),
     path('profile/', views.profile, name='profile'),


    
]
