from django.contrib import admin
from .models import Perfil, Categoria, Publicacion, Imagen

# Para que podás subir varias fotos desde el mismo anuncio
class ImagenInline(admin.TabularInline):
    model = Imagen
    extra = 3

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'precio', 'vendedor', 'categoria', 'vendido')
    list_filter = ('categoria', 'tipo_negocio', 'vendido')
    search_fields = ('titulo', 'descripcion')
    inlines = [ImagenInline]

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefono', 'fecha_unido')

admin.site.register(Categoria)
