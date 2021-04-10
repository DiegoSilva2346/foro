from django import forms   
from .models import Temas       

class FormularioCrearTema(forms.ModelForm):     
    class Meta:   
        model = Temas    
        fields=["titulo","categoria","texto"]    
       
    