
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # <--- ESTO ES LO QUE NECESITA EL CORE

urlpatterns = [
    path('admin/', admin.site.urls),          # El que ya te funciona
    path('accounts/', include('allauth.urls')), # Evita el error al cerrar sesión
    path('', include('tasks.urls')),           # ¡ESTO ES LO QUE FALTA! Conecta tu app
    path('sw.js', TemplateView.as_view(
        template_name="sw.js", 
        content_type='application/javascript'
    ), name='sw.js'),
]










