from django.contrib import admin
from django.urls import include, path

from project.views import IndexView

app_name = "project"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("api/", include("api.urls", namespace="api")),
    path("admin/", admin.site.urls),
]
