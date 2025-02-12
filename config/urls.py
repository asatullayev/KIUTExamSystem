# Django
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

# Project
from config.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.urls')),

    path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns += [
    path(r'i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += doc_urls

urlpatterns += tuple(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
urlpatterns += tuple(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
