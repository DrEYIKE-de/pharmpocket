import environ
from pathlib import Path
import logging 
import logging.config
from django.utils.log import DEFAULT_LOGGING


env = environ.Env(
    DEBUG=(bool, False)
)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

environ.Env.read_env(BASE_DIR / ".env")


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

SITE_ID = 1

THIRD_PARTY_APPS = ["rest_framework", "django_filters", "django_countries", "phonenumber_field",]
LOCAL_APPS = ["apps.users", "apps.posts", "apps.establishments", "apps.profiles", "apps.utils",]

INSTALLED_APPS = DJANGO_APPS+THIRD_PARTY_APPS+LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "core.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators


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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Kigali"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/staticfiles/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIR = []

MEDIA_URL = "/mediafiles/"

MEDIA_ROOT = BASE_DIR / "mediafiles"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTH_USER_MODEL = "users.User"

# logging

logger = logging.getLogger(__name__)

LOG_LEVEL = "INFO"

logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "%(asctime)s %(name)-8s %(levelname)-12s %(message)s"
        },
        "file": {
            "format": "%(asctime)s %(name)-8s %(levelname)-12s %(message)s"
        },
        "django.server": DEFAULT_LOGGING["formatters"]["django.server"]
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "file",
            "filename": "logs/pharm_pocket.log"
        }, 
        "django.server": DEFAULT_LOGGING["handlers"]["django.server"]
    },
    "loggers": {
        "": {"level": "INFO", "handlers": ["console", "file"], "propagate": False},
        "apps": {"level": "INFO", "handlers": ["console"], "propagate": False},
        "django.server": DEFAULT_LOGGING["loggers"]["django.server"]
    }
})