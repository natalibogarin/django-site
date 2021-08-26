# production.py
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'natalibogarin.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_site',
        'USER': 'name',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'',
    }
}

#STATIC_URL = 'https://nombreurlproyecto.com/static/'
#MEDIA_URL = 'https://nombreurlproyecto.com/media/'