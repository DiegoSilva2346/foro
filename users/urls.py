from django.contrib import admin
from django.urls import path,include     
from . import views

urlpatterns = [    
    #path('', views.welcome),     
    path('', include(('newtemas.urls','newtemas'))), 
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
   
]