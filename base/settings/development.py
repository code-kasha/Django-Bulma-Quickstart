from .base import *  # noqa
from .accounts import *  # noqa

DEBUG = True

ALLOWED_HOSTS = []

CKEDITOR_UPLOAD_PATH = "ckeditor_uploads"

CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_FORCE_JPEG_COMPRESSION = True

CKEDITOR_BROWSE_SHOW_DIRS = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa
    }
}


STATIC_URL = "/static/"

STATICFILES_DIRS = [BASE_DIR / "static"]  # noqa

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"  # noqa

SITE_ID = 1
