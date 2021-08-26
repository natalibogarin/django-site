# production.py
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#STATIC_URL = 'https://nombreurlproyecto.com/static/'
#MEDIA_URL = 'https://nombreurlproyecto.com/media/'