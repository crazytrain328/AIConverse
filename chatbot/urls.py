from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('', views.home, name= 'home'),
    path('login', views.login, name= 'login'),
    path('register', views.register, name= 'register'),
    path('logout', views.logout, name= 'logout'),
    path('clear_chat', views.clear_chat, name= 'clear_chat'),

]