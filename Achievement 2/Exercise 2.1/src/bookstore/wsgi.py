"""
WSGI config for bookstore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')

application = get_wsgi_application()

# sales/views.py
from django.shortcuts import render

# Function-Based View (FBV)
def home(request):
    """
    Home page view for sales app
    - Accepts HttpRequest object
    - Returns HttpResponse with rendered template
    - Is callable directly via URL
    """
    return render(request, 'sales/home.html')
