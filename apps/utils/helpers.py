import os
import random
import string
from django.utils.text import slugify

CHARS = string.ascii_lowercase + string.digits


def get_filename_ext(filepath):
    """ Returns a filename with extensions """
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def get_upload_path(instance, filename, destination="avatars"):
    """Renames a file/image on upload"""
    new_filename = str(random.randint(1, 33524642542))
    name, ext = get_filename_ext(filename)
    final_filename = f"{new_filename[:5]}-{name[:5]}{ext}"

    return f"{destination}/{final_filename}"


def random_string_generator(size=6, chars=CHARS):
    """Generates a random string"""
    return "".join(random.choice(CHARS) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """Generates a unique slug"""
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    qs_exists = instance.__class__.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = f"{slug}-{random_string_generator(size=4)}"
        return unique_slug_generator(instance, new_slug)
    return slug
