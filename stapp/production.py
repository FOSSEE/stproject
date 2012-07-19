from stapp.settings import *
DEBUG=False
TEMPLATE_DEBUG=DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'stapp', # Or path to database file if using sqlite3.
        'USER': 'stapp', # Not used with sqlite3.
        'PASSWORD': 'pp@ssw0rd', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}
