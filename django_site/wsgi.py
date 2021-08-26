"""
WSGI config for django_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhitenoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_site.settings')

application = get_wsgi_application()
application = DjangoWhitenoise(application)
