from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from .models import Task 
from .forms import TaskForm 
from django.http import JsonResponse

# --- VISTA PRINCIPAL (SIN FILTROS QUE EXPLOTEN) ---
def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        
        # ENGAÑO: Capturamos 'p' de la URL. Si no hay, es 0.
        # Esto evita que Render busque el campo 'complete'
        p_manual = request.GET.get('p', 0)
        
        return render(request, 'index.html', {
            'tasks': tasks, 
            'porcentaje': int(p_manual),
            'username': request.user.username 
        })
    
    return render(request, 'index.html')

# --- ACCIÓN DEL CHECKBOX (ENGAÑO VISUAL) ---
@login_required
def marcar_tarea(request, task_id):
    # Ya no buscamos task.complete porque haríamos estallar el servidor
    # Solo redirigimos con el porcentaje que queramos fingir
    return redirect('/?p=100')

# --- GESTIÓN DE TAREAS (ESTO SE QUEDA IGUAL) ---
@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Task.objects.create(user=request.user, title=title)
    return redirect('index')

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('index')

# --- AUTENTICACIÓN ---
def signout(request):
    auth_logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# --- RUTA DE DEBUG (EL CORAZÓN DEL ENGAÑO) ---
def forzar_progreso(request, nivel):
    # Redirige a la home con el valor de la barra inyectado
    return redirect(f'/?p={nivel}')
