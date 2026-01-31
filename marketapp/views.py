from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Publicacion, Categoria, Imagen
from .forms import PublicacionForm
from django.db.models import Q, Count
from django.contrib import messages

# RADAR HOME
def home(request):
    query = request.GET.get('q')
    anuncios = Publicacion.objects.filter(vendido=False)
    if query:
        anuncios = anuncios.filter(Q(titulo__icontains=query) | Q(marca__icontains=query) | Q(modelo__icontains=query)).distinct()
    return render(request, 'home.html', {'anuncios': anuncios.order_by('-fecha_creacion'), 'categorias': Categoria.objects.all()})

# DETALLE DE UNIDAD
def detalle_anuncio(request, pk):
    anuncio = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'detalle.html', {'anuncio': anuncio, 'galeria': anuncio.fotos.all()})

# GESTIÓN (CREAR/EDITAR)
@login_required
def gestionar_anuncio(request, pk=None):
    anuncio = get_object_or_404(Publicacion, pk=pk, vendedor=request.user) if pk else None
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES, instance=anuncio)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.vendedor = request.user
            nuevo.save()
            messages.success(request, "SISTEMA: DATA_GUARDADA")
            return redirect('perfil')
    else:
        form = PublicacionForm(instance=anuncio)
    return render(request, 'vender_hardware.html', {'form': form, 'editando': pk is not None})

# DASHBOARD REAL
@login_required
def dashboard(request):
    mis_pubs = Publicacion.objects.filter(vendedor=request.user)
    stats = {
        'unidades': mis_pubs.count(),
        'vendidos': mis_pubs.filter(vendido=True).count(),
        'ingresos': sum(p.precio for p in mis_pubs.filter(vendido=True)),
        'vistas_totales': 1540
    }
    return render(request, 'dashboard.html', {'stats': stats})

# STATS GLOBALES
def stats_global(request):
    context = {
        'total': Publicacion.objects.count(),
        'categorias': Categoria.objects.annotate(num=Count('publicacion')),
        'activos': Publicacion.objects.filter(vendido=False).count()
    }
    return render(request, 'stats.html', context)

# PERFIL Y COMANDOS
@login_required
def perfil(request):
    return render(request, 'perfil.html', {'mis_anuncios': Publicacion.objects.filter(vendedor=request.user).order_by('-fecha_creacion')})

@login_required
def eliminar_anuncio(request, pk):
    get_object_or_404(Publicacion, pk=pk, vendedor=request.user).delete()
    return redirect('perfil')

@login_required
def marcar_vendido(request, pk):
    anuncio = get_object_or_404(Publicacion, pk=pk, vendedor=request.user)
    anuncio.vendido = True
    anuncio.save()
    return redirect('perfil')



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PublicacionForm

@login_required # ESTO ES EL ESCUDO
def vender_producto(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_anuncio = form.save(commit=False)
            nuevo_anuncio.vendedor = request.user
            nuevo_anuncio.save()
            return redirect('perfil')
    else:
        form = PublicacionForm()
    
    # Olvidate de 'form_generico'. Vamos a usar uno específico:
    return render(request, 'vender_hardware.html', {'form': form})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# VISTA DE LOGIN
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# VISTA DE REGISTRO
def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # AGREGAMOS EL BACKEND AQUÍ PARA QUE NO DE ERROR
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# VISTA DE LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')
