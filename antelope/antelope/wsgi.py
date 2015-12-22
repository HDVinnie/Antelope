"""
WSGI config for antelope project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# DJANGO_SETTINGS_MODULE should be set to appropriate settings in your env
# This will make it fallback to production settings if it hasn't been set
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "antelope.settings.production")

application = get_wsgi_application()
