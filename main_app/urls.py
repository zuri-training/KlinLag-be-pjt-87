from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'main_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('login/', views.login_request, name='login'),
    path('login-agency/', views.login_agency, name='login_agency'),
    path('signup/user/', views.signup_user, name='signup_user'),
    path('signup/agency/', views.signup_agency, name='signup_agency'),
    path('logout/', views.logout_request, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('about/', views.about, name='about'),
    path('recycle-pickup/', views.recycle_pickup, name= 'recycle-pickup'),
    path('recycle-dropoff/', views.recycle_drop_off, name= 'recycle-dropoff'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
