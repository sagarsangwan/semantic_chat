
from .base_settings import *
from dotenv import load_dotenv

load_dotenv('../.env')
# STATIC_ROOT

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

DEBUG = False
ALLOWED_HOSTS = ['*']
# added because of heroku giving error -app not found
