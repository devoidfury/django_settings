try:
    import my_localsettings
except ImportError:
    raise Exception("You must create a my_localsettings.py file.")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',     # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': my_localsettings.db,         # Or path to database file if using sqlite3.
        'USER': my_localsettings.user,       # Not used with sqlite3.
        'PASSWORD': my_localsettings.passwd, # Not used with sqlite3.
        'HOST': '',                          # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                          # Set to empty string for default. Not used with sqlite3.
    }
}

ADMIN_MEDIA_PREFIX = '/admin-media/'
SERVE_STATIC_MEDIA = True

DEBUG = True

# Debug toolbar is wicked good, look into it.
LOCAL_INSTALLED_APPS = (
    'debug_toolbar',
)
LOCAL_MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

# Print emails to console.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
