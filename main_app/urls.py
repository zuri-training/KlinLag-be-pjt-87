from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.index, name='home'),
    path('login/', views.login_request, name='login'),
    path('login-agency/', views.login_agency, name='login_agency'),
    path('signup/user/', views.signup_user, name='signup_user'),
    path('signup/agency/', views.signup_agency, name='signup_agency'),
    path('logout/', views.logout_request, name='logout')
]
