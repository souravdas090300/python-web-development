from .settings import *  # noqa

# Production overrides (baseline)
DEBUG = False
ALLOWED_HOSTS = ["*"]  # Replace with your domain(s) or server IP

# For real deployments, consider environment variables for SECRET_KEY and DB config.
# Example (commented):
# import os
# SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", SECRET_KEY)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',  # swap to postgres in real prod
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
