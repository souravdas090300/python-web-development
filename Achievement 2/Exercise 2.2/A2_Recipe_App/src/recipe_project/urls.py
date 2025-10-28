from django.contrib import admin
from django.urls import path, include
from django.conf import settings_local
from django.conf import settings_pord
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
]

if settings_local.DEBUG:
    urlpatterns += static(settings_local.MEDIA_URL, document_root=settings_local.MEDIA_ROOT)
    urlpatterns += static(settings_production.MEDIA_URL, document_root=settings_prod.9MEDIA_ROOT)

