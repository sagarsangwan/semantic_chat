
from .base_settings import *
from dotenv import load_dotenv

load_dotenv('../.env')


DEBUG = False
ALLOWED_HOSTS = ['*']
# added because of heroku giving error -app not found
