from .base import *  # noqa: F403
from .secrets import *  # noqa: F403


DEBUG = False
TEMPLATE_DEBUG = DEBUG
# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = DEBUG

DATABASES = {
    "default": DATABASES_DEFAULT,       # noqa: F405
}

SITE_ID = 1

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
SECURE_SSL_REDIRECT = True
