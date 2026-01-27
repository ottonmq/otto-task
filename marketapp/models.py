from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# 1. PERFIL: El área personal del usuario
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    telefono = models.CharField(max_length=20)
    foto_perfil = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    fecha_unido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Área Personal de {self.usuario.username}"

# 2. CATEGORÍAS PROFESIONALES (Propiedades, Vehículos, etc.)
class Categoria(models.Model):
    nombre = models.CharField(max_length=100) # Propiedades, Vehículos, Tecnología, etc.
    def __str__(self): return self.nombre

# 3. PUBLICACIÓN: El motor de ventas
class Publicacion(models.Model):
    # Tipos de trato para Propiedades y Otros
    TIPO_NEGOCIO = [
        ('VENTA', 'Venta'),
        ('ALQUILER', 'Alquiler'),
        ('CAMBIO', 'Cambio / Permuta'),
    ]
    
    # Estado del ítem (Opcional)
    ESTADO_ITEM = [
        ('NUEVO', 'Nuevo'),
        ('USADO', 'Usado'),
    ]

    # Vínculo total con el Usuario
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mis_publicaciones')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # Datos del Anuncio
    titulo = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    
    # Lógica que pediste: Venta/Alquiler y Nuevo/Usado/Cambio
    tipo_negocio = models.CharField(max_length=10, choices=TIPO_NEGOCIO)
    estado_fisico = models.CharField(max_length=10, choices=ESTADO_ITEM, blank=True, null=True)
    
    # CONTROL DE VISIBILIDAD (Lo que pediste)
    vendido = models.BooleanField(default=False) # Si es True, desaparece del Market pero sigue en el Perfil
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = "VENDIDO" if self.vendido else "ACTIVO"
        return f"{self.titulo} - {status} ({self.vendedor.username})"

# 4. FOTOS (Galería de cada anuncio)
class Imagen(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='fotos')
    archivo = models.ImageField(upload_to='productos/')
