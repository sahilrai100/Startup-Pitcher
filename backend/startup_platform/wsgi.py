"""
WSGI config for startup_platform project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

# On Vercel the function runs from the repo root, so put backend/ on the path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'startup_platform.settings')

application = get_wsgi_application()

# Vercel looks for a module-level "app"
app = application
