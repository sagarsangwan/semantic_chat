
from .base_settings import *
from dotenv import load_dotenv

load_dotenv('../.env')
# STATIC_ROOT

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEBUG = False
ALLOWED_HOSTS = ['*']
# added because of heroku giving error -app not found
