# tasks/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']  # <--- ÚNICO CAMPO REAL EN TU MODELO
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'cyber-input', 
                'placeholder': 'INGRESE TAREA...',
                'autocomplete': 'off'
            }),
        }
