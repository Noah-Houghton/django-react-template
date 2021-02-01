"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

import environ
from configurations.wsgi import get_wsgi_application

environ.Env.read_env(env_file="config/.env")  # Source the .env file into os.environ
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "LocalConfiguration")

application = get_wsgi_application()
