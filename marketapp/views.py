
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Publicacion, Categoria
from django import forms

# --- 1. EL FORMULARIO ---
# Lo definimos aquí mismo para que no tengas que crear otro archivo forms.py
class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['categoria', 'titulo', 'precio', 'descripcion', 'tipo_negocio', 'estado_fisico']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control bg-dark text-info border-info'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-info', 'placeholder': 'Ej: Toyota Supra 2024'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control bg-dark text-white border-info'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control bg-dark text-white border-info', 'rows': 3}),
            'tipo_negocio': forms.Select(attrs={'class': 'form-control bg-dark text-info border-info'}),
            'estado_fisico': forms.Select(attrs={'class': 'form-control bg-dark text-info border-info'}),
        }

# --- 2. VISTAS PÚBLICAS (ESTILO INSTAGRAM) ---

def home(request):
    # El feed principal de Otto-task
    anuncios = Publicacion.objects.filter(vendido=False).order_by('-fecha_creacion')
    return render(request, 'home.html', {'vehiculos': anuncios})

def detalle_anuncio(request, pk):
    # Ver la info completa de un producto
    anuncio = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'detalle.html', {'anuncio': anuncio})

# --- 3. VISTAS PRIVADAS (USUARIO LOGUEADO) ---

@login_required
def perfil(request):
    # El panel donde el usuario ve sus propias porquerías
    mis_anuncios = Publicacion.objects.filter(vendedor=request.user).order_by('-fecha_creacion')
    return render(request, 'perfil.html', {'mis_anuncios': mis_anuncios})

@login_required
def gestionar_anuncio(request, pk=None):
    # Esta función hace TODO: Si no hay ID crea uno nuevo, si hay ID lo edita
    anuncio = None
    if pk:
        anuncio = get_object_or_404(Publicacion, pk=pk, vendedor=request.user)
    
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES, instance=anuncio)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.vendedor = request.user
            nuevo.save()
            return redirect('perfil')
    else:
        form = PublicacionForm(instance=anuncio)
    
    return render(request, 'form_generico.html', {'form': form, 'editando': pk is not None})

@login_required
def eliminar_anuncio(request, pk):
    # Borrar un anuncio permanentemente
    anuncio = get_object_or_404(Publicacion, pk=pk, vendedor=request.user)
    anuncio.delete()
    return redirect('perfil')

@login_required
def marcar_vendido(request, pk):
    # Cambiar estado a VENDIDO (Cyberpunk Status)
    anuncio = get_object_or_404(Publicacion, pk=pk, vendedor=request.user)
    anuncio.vendido = True
    anuncio.save()
    return redirect('perfil')
