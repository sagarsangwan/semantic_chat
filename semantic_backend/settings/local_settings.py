from semantic_backend.settings.base_settings import BASE_DIR

DEBUG = True

ALLOWED_HOSTS = []
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
