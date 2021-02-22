# Make a directory:

.secrets - Folder containing secret keys / auth credentials for email/redis/databases

## Create Secret Files (names should be pretty self explainatory) / Enviornment Variables.

- .django_secret_key
- .database_username
- .database_password
- .email_password
  - and so on..

---

# Update Settings:

Change your default email, and account activation configuration.

- base/
  - settings/
    - base.py : contains core settings.
    - accounts.py : contains settings related to account creation and email.
    - development.py : development settings, static and media mapping.

**Do not try to sign up without update to accounts.py in settings, it is bound to fail, use createsuperuser**

# Features:

    - Clean Looking Bulma Frontend! :D
    - Minimum (vanilla) JS for responsiveness.
    - User Profile Implemented with avatar.
    - Auto Generation of Profile using post_save signal.
    - Helpers for most common tasks. (rename image on upload / set slug)
        - Find them in apps/utils/helpers.py

# Usage:

1 Clone this repo / Download zip.

2 pip install requirements.txt.

3 python manage.py migrate.

4 python manage.py createsuperuser.

Happy Coding!
