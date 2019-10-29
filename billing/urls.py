from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('signup/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/registration/logout.html'), name='logout'),
]