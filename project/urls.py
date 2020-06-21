from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from project.views import IndexView

app_name = "project"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("api/", include("api.urls", namespace="api")),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
