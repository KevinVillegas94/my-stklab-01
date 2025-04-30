from datetime import timedelta
from pathlib import Path  # Si usas rutas con Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'apps.users',
    'apps.tasks',
]


# JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'login': '5/hour',  # Prevenir brute force
    }
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=120),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_COOKIE': 'stk_access',  # Cookie en lugar de localStorage
    'AUTH_COOKIE_SECURE': True,   # Solo HTTPS en producción
}

# CORS (Más seguro que ALLOWED_ORIGINS)
CORS_ORIGIN_WHITELIST = [
    "http://localhost:5173",
    "https://tudominio.com",
]
CORS_ALLOW_CREDENTIALS = True

# config/settings/__init__.py
from .settings.development import *