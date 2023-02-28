
from .base_settings import *
from dotenv import load_dotenv

load_dotenv('../.env')
# STATIC_ROOT

INSTALLED_APPS += [

    'whitenoise.runserver_nostatic'
]
MIDDLEWARE += [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ...
]

STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEBUG = True
WHITENOISE_USE_FINDERS = True

DEBUG = False
ALLOWED_HOSTS = ['*']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
