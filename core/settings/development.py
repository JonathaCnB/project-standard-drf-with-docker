from pathlib import Path

import environ

from .base import *  # noqa

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(BASE_DIR / '.env')

EMAIL_BACKEND = env("EMAIL_BACKEND")
EMAIL_HOST = env("SENDGRID_HOST")
EMAIL_USE_TLS = True
EMAIL_PORT = env("SENDGRID_PORT")
EMAIL_HOST_USER = env("SENDGRID_USER")
EMAIL_HOST_PASSWORD = env("HOST_MAIL_KEY")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM")
DOMAIN = env("DOMAIN")
SITE_NAME = "Project Standard"

DATABASES = {
    "default": {
        "ENGINE": env("POSTGRES_ENGINE"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}
