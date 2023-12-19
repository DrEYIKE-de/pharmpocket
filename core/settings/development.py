from .base import *

# Database pharm_pocket

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "DBNAME": env("PG_DBNAME"),
        "USER": env("PG_USER"),
        "PASSWORD": env("PG_PASSWORD"),
        "HOST": env("PG_HOST"),
        "PORT": env("PG_PORT")
    }
}
