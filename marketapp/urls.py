
from django.urls import path
from . import views

urlpatterns = [
    # Pantalla principal (El Instagram Cyberpunk)
    path('', views.home, name='home'),
    
    # Perfil del usuario y sus publicaciones
    path('perfil/', views.perfil, name='perfil'),
    
    # Ver un anuncio a pantalla completa
    path('detalle/<int:pk>/', views.detalle_anuncio, name='detalle_anuncio'),
    
    # Sistema de Gestión (Crear, Editar, Borrar)
    path('vender/', views.gestionar_anuncio, name='vender'),
    path('editar/<int:pk>/', views.gestionar_anuncio, name='editar_anuncio'),
    path('eliminar/<int:pk>/', views.eliminar_anuncio, name='eliminar_anuncio'),
    
    # Acción rápida para marcar como vendido
    path('marcar-vendido/<int:pk>/', views.marcar_vendido, name='marcar_vendido'),
]
