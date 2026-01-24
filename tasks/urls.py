from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    
    # --- ESTA ES LA RUTA QUE FALTABA PARA EL CHECKBOX ---
    path('marcar/<int:task_id>/', views.marcar_tarea, name='marcar_tarea'),
    
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.signout, name='logout'),
    
    # Tu ruta de debug para forzar la barra manualmente
    path('debug-barra/<int:nivel>/', views.forzar_progreso, name='forzar_progreso'),
]
