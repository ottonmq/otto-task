from django import forms
from .models import Publicacion

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        # Conexión exacta con los puertos de tu modelo
        fields = [
            'categoria', 'titulo', 'marca', 'modelo', 'precio', 
            'descripcion', 'telefono', 'foto', 'tipo_negocio', 'estado_fisico'
        ]
        
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control bg-dark text-primary border-primary'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control bg-dark text-white', 'placeholder': 'ID_OBJETO...'}),
            'marca': forms.TextInput(attrs={'class': 'form-control bg-dark text-white', 'placeholder': 'FABRICANTE...'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control bg-dark text-white', 'placeholder': 'SERIE_MODELO...'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control bg-dark text-success', 'placeholder': '0.00'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control bg-dark text-white', 'rows': 3, 'placeholder': 'ESPECIFICACIONES_TÉCNICAS...'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control bg-dark text-info', 'placeholder': 'LINEA_COMUNICACIÓN...'}),
            'foto': forms.FileInput(attrs={'class': 'form-control bg-dark text-white'}),
            'tipo_negocio': forms.Select(attrs={'class': 'form-control bg-dark text-warning'}),
            'estado_fisico': forms.Select(attrs={'class': 'form-control bg-dark text-info'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Etiquetas estilo Terminal para OTTO-MARKET
        self.fields['categoria'].label = ">> SECTOR_SISTEMA"
        self.fields['titulo'].label = ">> NOMBRE_UNIDAD"
        self.fields['marca'].label = ">> FABRICANTE"
        self.fields['modelo'].label = ">> MODELO_SERIE"
        self.fields['precio'].label = ">> VALOR_CRÉDITOS"
        self.fields['descripcion'].label = ">> DATA_ADICIONAL"
        self.fields['telefono'].label = ">> CANAL_CONTACTO"
        self.fields['foto'].label = ">> ARCHIVO_VISUAL"
        self.fields['tipo_negocio'].label = ">> PROTOCOLO"
        self.fields['estado_fisico'].label = ">> INTEGRIDAD"
