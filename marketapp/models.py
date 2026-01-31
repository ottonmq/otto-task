from django.db import models
from django.contrib.auth.models import User

# 1. PERFIL: Datos del operador
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    telefono = models.CharField(max_length=20, blank=True)
    foto_perfil = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    fecha_unido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Operador: {self.usuario.username}"

# 2. CATEGORÍAS (Vehículos, Propiedades, etc.)
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self): return self.nombre

# 3. PUBLICACIÓN: El núcleo del sistema
class Publicacion(models.Model):
    TIPO_NEGOCIO = [
        ('VENTA', 'Venta'),
        ('ALQUILER', 'Alquiler'),
        ('CAMBIO', 'Cambio / Permuta'),
    ]
    ESTADO_ITEM = [
        ('NUEVO', 'Nuevo'),
        ('USADO', 'Usado'),
    ]

    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mis_publicaciones')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # DATOS REQUERIDOS POR TU HTML
    titulo = models.CharField(max_length=255)
    marca = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True) # Tu HTML pedía esto
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True) # Para el botón de WhatsApp
    
    # IMAGEN PRINCIPAL (Para que cargue rápido en el Home)
    foto = models.ImageField(upload_to='productos/', blank=True, null=True)
    
    tipo_negocio = models.CharField(max_length=10, choices=TIPO_NEGOCIO)
    estado_fisico = models.CharField(max_length=10, choices=ESTADO_ITEM, blank=True, null=True)
    
    vendido = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {'VENDIDO' if self.vendido else 'ACTIVO'}"

# 4. GALERÍA ADICIONAL (Opcional)
class Imagen(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='fotos')
    archivo = models.ImageField(upload_to='productos/')
