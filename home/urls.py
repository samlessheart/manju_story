from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
     path('', views.home, name='home'),
     path('login/', auth_views.LoginView.as_view(template_name= "home/signin.html"), name='login' ),
     path('logout/', views.logout_view, name="logout"),
     path('login/home/', views.home, name='home'), 
     path('addphoto/', views.addphoto, name='addphoto'),
     path('addstory/', views.addstory, name='addstory'),
     path('addvideo/', views.addvideo, name='addvideo'),
     path('profile/', views.profile, name='profile'),
     path('storylist/', views.storylist, name='storylist'),
     path('photolist/', views.photolist, name='photolist'),
     path('videolist/', views.videolist, name='videolist'),
     path('photodet/<int:pk>', views.photodet, name='photodet'),

    
]
