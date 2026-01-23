
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # El que ya te funciona
    path('accounts/', include('allauth.urls')), # Evita el error al cerrar sesión
    path('', include('tasks.urls')),           # ¡ESTO ES LO QUE FALTA! Conecta tu app
]
