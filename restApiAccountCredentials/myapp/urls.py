from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    # path('about',views.about, name='about'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    # path('home',views.home, name = 'home'),
]
