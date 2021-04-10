from django.db import models       
from django.contrib.auth.models import User      
from django.shortcuts import render,redirect          
from django.utils import timezone
import pytz


# Create your models here.    
#lista_categorias=[(1,'pasteles'),(2,"Deportes"),(3,"Ciencia"),(4,"Clima"),(5,"Pandemia"),(6,'Programaciòn')]     
#usuario=User.id      

class Categoria(models.Model):   
    nombre=models.CharField(max_length=50)              
    
    created=models.DateTimeField(auto_now_add=True)   
    updated=models.DateTimeField(auto_now_add=True)      
    class Meta:  
        verbose_name="categoria"   
        verbose_name_plural="categorias"    
    def __str__(self):  
        return self.nombre 
class Temas(models.Model):           
   
    titulo=models.CharField("titulo",max_length=50,null=False,blank=False)         
    descripcion=models.CharField("descripcion",max_length=100,null=False,blank=False)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)   
    texto=models.TextField()      
    #elige_tu_categoria=models.IntegerField(null=False,blank=True,choices=lista_categorias,default=2)        
    fecha=models.DateTimeField(null=False,blank=False)           
    

    class Meta:    
        verbose_name="Tema"    
        verbose_name_plural="Temas"      
    def __str__(self):    
        
        return self.titulo              
             





class Respuesta(models.Model):        
    id = models.AutoField(primary_key=True)       
    id_tema=models.ForeignKey(Temas,on_delete=models.CASCADE,unique=False)     
    usuario=models.CharField("usuario",max_length=100,null=False,blank=False)       
    fecha=models.DateTimeField(null=False,blank=False)        
    respuesta=models.TextField()           
    class Meta:  
        verbose_name="respuesta"   
        verbose_name_plural="respuestas"    
    def __str__(self):  
        return self.id_tema           



class Visualizacion(models.Model):          
    id = models.AutoField(primary_key=True)         
    id_tema=models.ForeignKey(Temas,on_delete=models.CASCADE,unique=False)        
    usuario=models.CharField("descripcion",max_length=100,null=False,blank=False)            
    class Meta:  
        verbose_name="vizualisacion"   
        verbose_name_plural="visualizaciones"    
    def __str__(self):  
        return self.id_tema    
