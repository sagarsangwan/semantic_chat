from .base_settings import *

<<<<<<< HEAD
STATIC_URL = 'static/'
=======
STATIC_URL = 'static'
>>>>>>> d0a7b053752a107a3d895ecf4cc0917ece72e92f
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEBUG = True
