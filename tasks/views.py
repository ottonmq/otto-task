from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404

from .models import Task 
from .forms import TaskForm 





# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task

def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'tasks/index.html', {'tasks': tasks})
    return render(request, 'tasks/index.html')

@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        Task.objects.create(user=request.user, title=title)
    return redirect('index')



@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == "POST":
        task.completed = not task.completed # Esto marca como hecha/pendiente
        task.save()
    return redirect('index')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('index')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # EL ERROR ESTABA AQUÍ: Debe ser is_valid()
        if form.is_valid(): 
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})





def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/') # Regresa al index neón
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

def signout(request):
    auth_logout(request)
    return redirect('login') # Te manda directo al login Cyberpunk

def signout(request):
    auth_logout(request)
    return redirect('index') # Te manda al login que ya tiene el auto-ajuste