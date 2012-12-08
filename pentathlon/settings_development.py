# Django settings for pentathlon project.
from settings_default import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db.sqlite',  # Or path to database file if using sqlite3.
        'USER': '',  # Not used with sqlite3.
        'PASSWORD': '',  # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    }
}

INSTALLED_APPS = INSTALLED_APPS + ('django.contrib.sessions',)


class IP:
    def __contains__(self, x):
        return True


INTERNAL_IPS = IP()

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


import mimetypes
mimetypes.add_type('text/css', '.less')  # ensure .less files are served with correct mime-type
# needed for iOS fullscreen webapps with less.js inorder to refresh less files on reload
