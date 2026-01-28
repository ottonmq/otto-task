[app]
title = Otto-Task
package.name = ottotask
package.domain = com.otto.cyberpunk
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Requisitos para que el escáner funcione
requirements = python3,kivy,android

# Orientación (Cyberpunk siempre se ve bien en Vertical)
orientation = portrait

# Permisos para conectar con Onrender
android.permissions = INTERNET

# (bool) Pantalla completa para máxima inmersión
fullscreen = 1
