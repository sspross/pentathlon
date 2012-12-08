import os
import sys
import site

PROJECT_NAME = 'pentathlon'
PROJECT_ROOT = os.path.dirname(__file__)
site_packages = os.path.join(PROJECT_ROOT, 'env/lib/python%i.%i/site-packages' % (sys.version_info[0], sys.version_info[1]))
site.addsitedir(os.path.abspath(site_packages))
sys.path.insert(0, PROJECT_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = PROJECT_NAME + '.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
