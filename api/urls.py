from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from api.views import ModelRegister

app_name = "api"

schema_view = get_schema_view(
    openapi.Info(
        title="Ubex AutoAPI",
        default_version="v1",
        description="Simple REST CRUD for all models in project",
        terms_of_service="https://github.com/NickSablukov/ubex_autoapi",
        contact=openapi.Contact(email="dessanndes@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(r"", schema_view.with_ui("swagger", cache_timeout=0), name="index"),
] + ModelRegister().get_urls()
