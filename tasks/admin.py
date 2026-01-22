from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task

# PERSONALIZACIÓN DEL TÍTULO DEL PANEL (ESTILO OTTO-APP)
admin.site.site_header = "OTTO-TASK-// ADMIN_PANEL"
admin.site.site_title = "OTTO_TASK_TERMINAL"
admin.site.index_title = "GESTIÓN DE TAREAS Y USUARIOS"

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Columnas que verás en la tabla principal
    list_display = ('title', 'user', 'created_at', 'completed_status')
    
    # Filtros rápidos en la derecha
    list_filter = ('user', 'created_at')
    
    # Buscador por título de tarea
    search_fields = ('title', 'user__username')
    
    # Para que las tareas se ordenen de la más nueva a la más vieja
    ordering = ('-created_at',)

    # Función para que el estado de "Completado" se vea con estilo en el admin
    @admin.display(description="ESTADO", boolean=True)
    def completed_status(self, obj):
        # Aquí puedes añadir lógica si quieres que se vea distinto, 
        # por ahora usa el check estándar de Django
        return False # Cambiar a True si añades el campo 'completed' al modelo
