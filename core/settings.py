import os
import dj_database_url
from pathlib import Path

# Dirección base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# --- 🛰️ SEGURIDAD DE ACCESO ---
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-u=oy)$lfga_%!a*mhc&74#2t+&yo309ow5hw3h2ezm!@-4stor')

# DEBUG se apaga automáticamente en Render si no está en las variables de entorno
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = ['*']

# --- 📦 MÓDULOS DEL SISTEMA ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    'tasks', # Módulo de misiones principal
    
    # Protocolos de Autenticación
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
]

SITE_ID = 1

# --- ⚙️ CAPAS DE PROCESAMIENTO (MIDDLEWARE) ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Manejo de neones estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'core.urls' # Asegúrate que tu carpeta de proyecto se llame 'core'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'tasks' / 'templates'], # Ruta de interfaces
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# --- 🗄️ ALMACENAMIENTO DE DATOS (PSQL/SQLite) ---
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600
    )
}

# --- 🌍 LOCALIZACIÓN ---
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- ⚡ ENERGÍA ESTÁTICA (STATIC FILES) ---
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- 🔐 PROTOCOLO ALLAUTH (CORRECCIÓN v65.14) ---
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Parche definitivo para Advertencias Amarillas y Error 500
ACCOUNT_LOGIN_METHODS = {'username'} # Nuevo estándar
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_SESSION_REMEMBER = True
SOCIALACCOUNT_LOGIN_ON_GET = True
ACCOUNT_LOGOUT_ON_GET = True

# --- 🛠️ OTROS AJUSTES ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
