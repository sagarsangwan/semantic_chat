from semantic_backend.settings.base_settings import BASE_DIR
import os

DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1", ".vercel.app", "vercel.app"]
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

DATABASES = {}


STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build", "static")
