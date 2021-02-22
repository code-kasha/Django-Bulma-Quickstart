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

**[Errno -2] Name or service not known : This error will be thrown if your email settings are not proper. fix them and restart the server to solve**

**Since we send an email verification, they absolutely need to have an email and a backend to handle it, tinker around accounts.py and docs to learn more**

**Inside the admin panel, change the site name and hosts!**

# Docs :

    - Django : https://docs.djangoproject.com/en/3.1/
    - Django Allauth : https://django-allauth.readthedocs.io/en/latest/
    - Django Ckeditor : https://pypi.org/project/django-ckeditor/
    - Django Widget Tweaks : https://pypi.org/project/django-widget-tweaks/
    - Pillow : https://pillow.readthedocs.io/en/stable/

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
