from .base import (
    SECRETS_DIR as SECRET,
)  # to avoid any issues relating to duplication, easily solved via enviornment variables in prod

"""Settings for mail backend, you might want to keep it seperate, in this context, it makes sense here"""

with open(SECRET / ".email_pass") as f:
    EMAIL_PASSWORD = f.read().strip()

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "YOUR EMAIL HOST HERE"

EMAIL_PORT = 465

EMAIL_USE_SSL = True  # EMAIL_USE_TLS = True (either one of two)

EMAIL_HOST_USER = "YOUR EMAIL ID HERE"

EMAIL_HOST_PASSWORD = EMAIL_PASSWORD

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

"""Settings from Allauth"""

ACCOUNT_ACTIVATION_DAYS = 7

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_CONFIRMATION_HMAC = False

ACCOUNT_EMAIL_VERIFICATION = "mandatory"  # can be none

ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN = 180

ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5

ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300

ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

ACCOUNT_SESSION_REMEMBER = None  # Because we use remember me value from user form
