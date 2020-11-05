from django.shortcuts import render,redirect     
from django.contrib.auth import logout as do_logout      
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login    
from django.contrib.auth.forms import UserCreationForm
from .models import Temas       
from .formulario import FormularioCrearTema         
from django.utils import timezone
  
from django.contrib.auth.models import User   
# Create your views here.             
def Editar(request,id):     
  tema=Temas.objects.get(id=id)       
  if request.method =="GET":       
    autor_form=FormularioCrearTema(instance=tema)              
    
  else:          
    
    autor_form=FormularioCrearTema(request.POST,instance=tema)           
          
    if autor_form.is_valid():     
      autor_form.save()        
          
      return redirect("/")

  return render(request,"editar.html",{"form":autor_form})   

def welcome(request):     
       # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:            
        #temas=Temas.objects.all()    
        temas=Temas.objects.order_by('fecha').reverse()        
            


        return render(request, "welcome.html",{"temas":temas})
    # En otro caso redireccionamos al login
    return redirect("/login")              
def CrearTema(request):            
  if request.user.is_authenticated:      
    if request.method=="POST":        
         #miformulario=FormularioCrearTema(request.POST)      
         #print(type(miformulario))         
         descripccion=Temas()      
         descripccion.descripcion=request.user.username      
         descripccion.titulo=request.POST["titulo"]    
         descripccion.texto=request.POST["texto"]           
         descripccion.fecha=timezone.now()
            
        
             
         if descripccion.titulo != "" and descripccion.texto != "":
            #miformulario.save()           
            descripccion.save()   
              

            return redirect("/")   
             
                 
              

         
    else:
        miformulario=FormularioCrearTema()          
        #miformulario.descripcion=request.user.username       
        #print(miformulario.descripcion)           
    return render(request,"creartema.html",{"form":miformulario})           
  else: 
    return redirect("/login")                    
              
         
def Eliminar(request,id):           
        
  tema=Temas.objects.get(id=id)       
  tema.delete()
  return redirect("/")