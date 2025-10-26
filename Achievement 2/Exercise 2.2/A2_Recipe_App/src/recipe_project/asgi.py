import os
from django.core.asgi import get_asgi_application

# Use explicit DJANGO_SETTINGS_MODULE when provided; default to local settings.
# In production, set the environment variable DJANGO_SETTINGS_MODULE to point to
# your production settings module before starting the ASGI server (e.g., with Uvicorn/Daphne).
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_project.settings_local')

application = get_asgi_application()
