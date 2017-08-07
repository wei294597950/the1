"""
WSGI config for the1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application
sys.path.append('C:/Users/roobo/test627/Scripts/test2/Scripts/the1')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "the1.settings")

application = get_wsgi_application()
