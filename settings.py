import os, sys
import os.path

# Get absolute path to this file's directory
PROJECT_DIR = os.path.dirname(__file__)

# Our site-specific settings
# This will load settings from PROJECT_NAME.localsettings.<FLAVOR>.settings
# Other site-specific configuration files should be stored in that directory
# as well to keep them source controlled.
#
# To change which site configuration PROJECT_NAME is using, set the environment
# variable PROJECT_NAME on the server, usually in the wsgiconf.
#
# This needs to be done explicitly on management commands if PROJECT_NAME is
# set to anything other than localdev.
#
# Example:
# PROJECT_DIR~$ PROJECT_NAME=<settings-you-need> python manage.py <command> <args>
# =============================================================================

FLAVOR = os.environ.get('PROJECT_NAME', 'localdev')

DEBUG = False
LOCAL_INSTALLED_APPS = None
LOCAL_MIDDLEWARE_CLASSES = None

def override_settings(dottedpath):
    try:
        _m = __import__(dottedpath, fromlist=[None])
        _thismodule = sys.modules[__name__]
        for _k in dir(_m):
            setattr(_thismodule, _k, getattr(_m, _k))
    except ImportError:
        pass

override_settings('PROJECT_NAME.localsettings.' + FLAVOR + '.settings')


# Web administrative/debug settings
# =============================================================================
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

SITE_ID = 1

# Make this unique, and don't share it with anybody.
# DON'T USE THIS KEY, MAKE YOUR OWN!
SECRET_KEY = 'dxb%w-_&!-5a-ntpioz(w)e3i^bs^ys9@@+x3cmccii-u12qf@'

# Internationalization settings
# =============================================================================

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True


# Relative absolute directory paths
# =============================================================================

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')


# Additional locations of static files
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, "templates"),
)

# URLS and the like
# =============================================================================

ROOT_URLCONF = 'PROJECT_NAME.urls'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/admin-media/'


# Loaders and middleware
# =============================================================================

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# Installed apps/logging
# =============================================================================

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# Auto-loader for any additional settings.
# Will silently fail if any problems encountered, should
# probably be improved.
# =======================================================
try:
    INSTALLED_APPS = LOCAL_INSTALLED_APPS + INSTALLED_APPS
except Exception:
    pass
try:
    MIDDLEWARE_CLASSES = LOCAL_MIDDLEWARE_CLASSES + MIDDLEWARE_CLASSES
except Exception:
    pass
