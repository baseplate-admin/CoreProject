"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-mn19l@e%r^s&a^pa9%(bf173v-0c54^@3s(pb!ts_yuts0$+6p"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

MAL_CLIENT_ID = os.environ.get("MAL_CLIENT_ID")
MAL_CLIENT_SECRET = os.environ.get("MAL_CLIENT_SECRET")


# Application definition

INSTALLED_APPS = [
    "core",
    # Django stuff
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # Whitenoise
    "django.contrib.staticfiles",
    # Sites
    "django.contrib.sites",
    # Flatpages
    "django.contrib.flatpages",
    # Rest Framework
    "rest_framework",
    # 3rd party rest framework stuff
    "corsheaders",
    "rest_framework_simplejwt.token_blacklist",
    # 3rd party Django stuff
    "dbbackup",  # django-dbbackup
    "ckeditor",
    "ckeditor_uploader",
    "crispy_forms",
    "django_filters",
    "django_cleanup.apps.CleanupConfig",
    "huey.contrib.djhuey",
    # Pages
    "apps.anime",
    # Rest stuff
    "apps.__user__",
]
# Debug Toolbar Add
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#install-the-app
if DEBUG:
    INSTALLED_APPS += ("debug_toolbar",)


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # Whitenoise
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # Cors headers
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    # Flatpages
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
]
SITE_ID = 1
# https://docs.djangoproject.com/en/4.0/topics/cache/#the-per-site-cache-1
CACHE_MIDDLEWARE_SECONDS = 0

# Debug Toolbar Middleware
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#add-the-middleware
if DEBUG:
    MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)


# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#configure-internal-ips
if DEBUG:
    INTERNAL_IPS = [
        "127.0.0.1",
    ]
# Cookie override
CSRF_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_SAMESITE = "Strict"
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ASGI_APPLICATION = "core.asgi.application"

# Override the login url
# https://stackoverflow.com/questions/49532708/custom-login-url-in-django#49532812
LOGIN_URL = "login_page"

# Cache
# https://docs.djangoproject.com/en/4.0/topics/cache/#filesystem-caching

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Allow more fields to be deleted at once
# https://stackoverflow.com/questions/47585583/the-number-of-get-post-parameters-exceeded-settings-data-upload-max-number-field
DATA_UPLOAD_MAX_NUMBER_FIELDS = 50000


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Custom user model
# https://testdriven.io/blog/django-custom-user-model/

AUTH_USER_MODEL = "__user__.User"

# Username or Email backend
# https://stackoverflow.com/questions/25316765/log-in-user-using-either-email-address-or-username-in-django#35836674

AUTHENTICATION_BACKENDS = ["apps.__user__.backends.EmailOrUsernameModelBackend"]

# Password hashers
# https://docs.djangoproject.com/en/3.2/topics/auth/passwords/#using-argon2-with-django

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    Path(BASE_DIR, "static"),
]

STATIC_ROOT = Path(BASE_DIR, "staticfiles")
# STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = Path(BASE_DIR, "media")
CKEDITOR_UPLOAD_PATH = Path(MEDIA_ROOT, "upload")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Rest framework auth
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation
# https://www.django-rest-framework.org/api-guide/parsers/#setting-the-parsers

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    "MAX_PAGINATE_BY": 100,
}

# Settings override
# https://github.com/jazzband/djangorestframework-simplejwt/blob/3fc9110c7d0e5641b6eccb6dca321f44189bba01/rest_framework_simplejwt/settings.py#L12

SIMPLE_JWT = {
    "UPDATE_LAST_LOGIN": True,
}

# django-cors-headers settings
# https://pypi.org/project/django-cors-headers/

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "http://localhost:8000",
]

# settings.py -- alternative configuration method
# https://huey.readthedocs.io/en/latest/contrib.html#setting-things-up

from huey import PriorityRedisHuey
from redis import ConnectionPool

pool = ConnectionPool(host="localhost", port=6379, max_connections=20)
HUEY = PriorityRedisHuey(
    "my-app",
    use_zlib=True,
    compression=True,
    connection_pool=pool,
)

DBBACKUP_STORAGE = "django.core.files.storage.FileSystemStorage"
DBBACKUP_STORAGE_OPTIONS = {"location": os.path.join(BASE_DIR, "backup")}
