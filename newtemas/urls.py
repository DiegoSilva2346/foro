from django.contrib import admin
from django.urls import path              
from django.contrib.auth.decorators import login_required   
from . import views
from blogsilva3.settings import base   

urlpatterns = [    
    path('', login_required(views.welcome),name="welcome"),           
    path('creartemas/', login_required(views.CrearTema),name="CrearTema"),          
    path('editar/<int:id>', login_required(views.Editar),name="editar"), 
    path('eliminar/<int:id>', login_required(views.Eliminar),name="eliminar"),            
    path('temas/<int:id>',login_required(views.temas),name="temas")
   
]         
