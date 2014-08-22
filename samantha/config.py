import os


def get(key):
    """Retrieves env vars and makes Python boolean replacements"""

    value = os.environ.get(key)

    if value == 'true':
        value = True
    elif value == 'false':
        value = False

    return value
