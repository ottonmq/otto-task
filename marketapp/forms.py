from django import forms
from .models import Publicacion

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['categoria', 'titulo', 'precio', 'descripcion', 'tipo_negocio', 'estado_fisico']
        
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tipo_negocio': forms.Select(attrs={'class': 'form-control'}),
            'estado_fisico': forms.Select(attrs={'class': 'form-control'}),
        }
