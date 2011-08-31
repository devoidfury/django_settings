import os, sys
sys.path.append('/path/to/folder_contiaining_project_folder/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'PROJECT_NAME.settings'
os.environ['PROJECT_NAME'] = 'production'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
