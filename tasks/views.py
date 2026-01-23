from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from .models import Task 
from .forms import TaskForm 

def index(request):
    try:
        if request.user.is_authenticated:
            tasks = Task.objects.filter(user=request.user)
            total = tasks.count()
            
            # REPARACIÓN: Usamos un campo que SÍ existe
            # Por ahora contará todas como completadas para que no dé error
            completadas = tasks.count() 
            
            porcentaje = (completadas / total * 100) if total > 0 else 0
            
            return render(request, 'index.html', {
                'tasks': tasks, 
                'porcentaje': int(porcentaje)
            })
        
        return render(request, 'index.html')
        
    except Exception as e:
        # Esto te mostrará el error exacto en la pantalla amarilla
        raise e


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
