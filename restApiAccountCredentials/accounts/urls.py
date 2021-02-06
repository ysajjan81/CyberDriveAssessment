from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("register", views.register, name='register'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("resetpassword", views.resetpassword, name='resetpassword'),
    path("resetusername", views.resetusername, name='resetusername'),
    path("resetemail", views.resetemail, name='resetemail'),
    path('gettoken/', obtain_auth_token),
    ]
