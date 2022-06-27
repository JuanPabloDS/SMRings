"""
WSGI config for projeto_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling # Cling apresenta os arquivos estáticos, MediaCling apresenta os arquivos da media

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_django.settings')

application = Cling(MediaCling(get_wsgi_application()))
