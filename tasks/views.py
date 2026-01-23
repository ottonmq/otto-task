from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .models import Task 
from .forms import TaskForm 

# --- 🛰️ VISTA PRINCIPAL (ELIMINADO EL ERROR 500) ---
def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        # QUITAMOS EL 'tasks/' DE LA RUTA PARA QUE DJANGO LO ENCUENTRE
        return render(request, 'index.html', {'tasks': tasks})
    return render(request, 'index.html')

# --- 📝 GESTIÓN DE MISIONES ---
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

# --- 🔐 CIERRE DE SESIÓN SEGURO ---
def signout(request):
    auth_logout(request)
    return redirect('index') # Te manda al inicio neón sin romperse
