import os
import dj_database_url
from pathlib import Path

# Dirección base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURIDAD
SECRET_KEY = 'django-insecure-u=oy)$lfga_%!a*mhc&74#2t+&yo309ow5hw3h2ezm!@-4stor'

# DEBUG se apaga automáticamente en Render si configuras la variable de entorno
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# Permitir todos los hosts en desarrollo, pero Render lo manejará en producción
ALLOWED_HOSTS = ['*']

# APPS INSTALADAS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    'tasks',
    
    # Autenticación
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
]

SITE_ID = 1

# MIDDLEWARE (Orden crítico para seguridad y archivos estáticos)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Maneja el neón en la nube
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'tasks' / 'templates'],
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

# 🗄️ BASE DE DATOS HÍBRIDA (La clave de la V2)
# Si Render detecta una base de datos Postgres, la usa. Si no, usa tu SQLite local.
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600
    )
}

# VALIDACIÓN DE CONTRASEÑAS
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# INTERNACIONALIZACIÓN
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ⚡ ARCHIVOS ESTÁTICOS (CONFIGURACIÓN ÚNICA)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Esto permite que Django sirva CSS/JS sin necesidad de Nginx/Apache
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# AUTENTICACIÓN
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SOCIALACCOUNT_LOGIN_ON_GET = True
ACCOUNT_LOGOUT_ON_GET = True

# CONFIGURACIÓN DE PROVEEDORES SOCIALES
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': ['user', 'read:user', 'user:email'],
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'FIELDS': ['id', 'email', 'name', 'picture'],
        'VERIFIED_EMAIL': False,
        'VERSION': 'v13.0',
    }
}

SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'username'

# DEFAULT AUTO FIELD
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
