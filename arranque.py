import os
import sys
import time
from django.core.management import execute_from_command_line

def efecto_escritura(texto, velocidad=0.03):
    """Hace que el texto aparezca letra por letra."""
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    print() # Salto de línea al terminar

def iniciar_otto_task():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    
    # El encabezado aparece con efecto
    efecto_escritura("\n" + "═"*45, 0.01)
    efecto_escritura("   OTTO-TASK // SISTEMA DE ARRANQUE", 0.05)
    efecto_escritura("   HOLA OTTO NMQ", 0.08)
    efecto_escritura("   PROYECTO: convercion pwa ->  .exe", 0.05)
    efecto_escritura("   PROYECTO: para que funcione en windows", 0.05)
    efecto_escritura("   PROYECTO: para que funcione en mac ", 0.05)
    efecto_escritura("   ESTADO: ESCANEANDO...", 0.1)
    efecto_escritura(">> DIRECCIÓN: http://127.0.0.1:8000/", 0.02)
    efecto_escritura("═"*45 + "\n", 0.01)

    try:
        # Pausa dramática antes de lanzar el servidor
        time.sleep(0.5)
        print(">> NÚCLEO ESTABLE. LANZANDO INSTANCIA...\n")
        execute_from_command_line([sys.argv[0], "runserver", "0.0.0.0:8000", "--noreload"])
    except Exception as e:
        print(f"!! ERROR DE NÚCLEO: {e}")

if __name__ == "__main__":
    iniciar_otto_task()
