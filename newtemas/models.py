from django.db import models       
from django.contrib.auth.models import User      
from django.shortcuts import render,redirect          
import datetime

# Create your models here.    
lista_categorias=[(1,'pasteles'),(2,"Deportes"),(3,"Ciencia"),(4,"Clima"),(5,"Pandemia"),(6,'Programaciòn')]     
#usuario=User.id      

class Temas(models.Model):           
   
    titulo=models.CharField("titulo",max_length=50,null=False,blank=False)         
    descripcion=models.CharField("descripcion",max_length=100,null=False,blank=False)
     
    texto=models.TextField()      
    elige_tu_categoria=models.IntegerField(null=False,blank=True,choices=lista_categorias,default=2)        
    fecha=models.DateTimeField(null=False,blank=True,default=datetime.datetime.now())           
    

    class Meta:    
        verbose_name="Tema"    
        verbose_name_plural="Temas"      
    def __str__(self):    
        
        return self.titulo              
             
