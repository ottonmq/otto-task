from django.contrib import admin
from .models import Perfil, Categoria, Publicacion, Imagen

# Personalización del Header del Admin
admin.site.site_header = "OTTO-MARKET // CENTRAL_CORE"
admin.site.site_title = "OTTO-MARKET ADMIN"
admin.site.index_title = "PANEL_DE_CONTROL_DE_INVENTARIO"

class ImagenInline(admin.TabularInline):
    model = Imagen
    extra = 2

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('id_tag', 'titulo', 'marca', 'precio', 'vendedor', 'vendido')
    list_filter = ('categoria', 'tipo_negocio', 'vendido')
    search_fields = ('titulo', 'marca', 'modelo')
    inlines = [ImagenInline]
    
    # Esto es para que el ID se vea como un tag de sistema en la lista
    def id_tag(self, obj):
        return f"UNIT-{obj.id}"
    id_tag.short_description = 'SERIAL_ID'

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefono', 'fecha_unido')

admin.site.register(Categoria)
