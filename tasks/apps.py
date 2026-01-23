from django.apps import AppConfig

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
    # ESTO CAMBIA EL NOMBRE EN EL PANEL DEL ADMIN
    verbose_name = 'OTTO-TASK'
