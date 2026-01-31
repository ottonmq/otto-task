import os
from pathlib import Path

# --- 1. RUTAS BASE ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- 2. SEGURIDAD ---
SECRET_KEY = 'django-insecure-wskp$fl8&frfe3=uk^ue+$5*(*sjpvmd#5f!2ac$k@y1g@r1q0'
DEBUG = True
ALLOWED_HOSTS = ['*'] # Para que funcione en Termux/Local sin líos

# --- 3. APLICACIONES (SISTEMA + OTTO-TASK) ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Tu App
    'marketapp',
    
    # Autenticación Cyberpunk (Allauth)
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google', 
]

# --- 4. MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'market.urls'

# --- 5. PLANTILLAS ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media', # NECESARIO PARA FOTOS
            ],
        },
    },
]

WSGI_APPLICATION = 'market.wsgi.application'

# --- 6. BASE DE DATOS ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- 7. INTERNACIONALIZACIÓN ---
LANGUAGE_CODE = 'es-es' # En español para vos
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- 8. ARCHIVOS ESTÁTICOS Y MEDIA (EL RADAR DE FOTOS) ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --- 9. AUTENTICACIÓN (ALLAUTH CONFIG) ---
SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email' # Más moderno

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'}
    }
}

# --- 10. OTROS ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# --- PROTOCOLO DE ACCESO OTTO-MARKET ---
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_EMAIL_VERIFICATION = "none"  # No pedir confirmación de correo
ACCOUNT_LOGIN_ON_GET = True          # Personalización que pediste antes
LOGIN_REDIRECT_URL = 'perfil'        # A dónde va tras loguearse
ACCOUNT_LOGOUT_REDIRECT_URL = 'home'




# settings.py - AL FINAL DEL ARCHIVO
import os
from django.core.files import locks

# PARCHE PARA ANDROID/TERMUX: Desactiva el bloqueo de archivos
locks.lock = lambda f, flags: True
locks.unlock = lambda f: True

# Asegura permisos de escritura en la memoria del celular
FILE_UPLOAD_PERMISSIONS = 0o644



# Saltarse la página de "¿Desea iniciar sesión con Google?"
SOCIALACCOUNT_LOGIN_ON_GET = True 

# A dónde ir después de loguearse con éxito
LOGIN_REDIRECT_URL = '/dashboard/' # O la URL de tu Home
