"""
WSGI config for alx_travel_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alx_travel_app.settings")
>>>>>>> d17f2c1 (Initial project setup)

application = get_wsgi_application()
