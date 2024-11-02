from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name='home.html'), name='home'),
    path("admin/", admin.site.urls),
    path('localidades/',include('localidades.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
    )