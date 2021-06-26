from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'klin_api'

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('create-user/', views.UserCreate.as_view(), name='account-create'),
    path('create-agency/', views.AgencyCreate.as_view(), name= 'agent-create')
]



