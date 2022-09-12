from .common import *

SECRET_KEY = 'django-insecure-pnwm+i#4t1bnbjs@ts02udssohda##7$=@koh*y+)u1^2)u8#n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
