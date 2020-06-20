from typing import Dict, List, Type

import django.apps
from django.db.models import Model
from django.urls import URLPattern
from django_filters.filterset import filterset_factory
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.routers import DefaultRouter
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet


class ModelRegister:
    routers_for_apps: Dict[str, DefaultRouter]

    def __init__(self):
        self.routers_for_apps = {}
        for model in django.apps.apps.get_models():
            app_label = model._meta.app_label
            router = self.routers_for_apps.setdefault(app_label, DefaultRouter())
            prefix = ""
            if app_label != "api":
                prefix = f"{app_label}/"
            router.register(
                prefix=f"{prefix}{model._meta.model_name}",
                viewset=self._get_viewset(model),
            )

    def get_urls(self) -> List[URLPattern]:
        urls = []
        for router in self.routers_for_apps.values():
            urls.extend(router.urls)
        return urls

    def _get_serializer_class(self, model: Type[Model]) -> Type:
        return type(
            f"{model._meta.object_name}SerializerClass",
            (ModelSerializer,),
            {"Meta": self._get_static_meta(model)},
        )

    def _get_filter_class(self, model: Type[Model]) -> Type:
        return filterset_factory(model)

    def _get_static_meta(self, model: Type[Model]) -> Type:
        return type("Meta", (), {"fields": "__all__", "model": model})

    def _get_viewset(self, model: Type[Model]) -> Type:
        return type(
            f"{model._meta.object_name}ViewSet",
            (ModelViewSet,),
            {
                "serializer_class": self._get_serializer_class(model),
                "filter_class": self._get_filter_class(model),
                "ordering_fields": "__all__",
                "filter_backends": [DjangoFilterBackend, SearchFilter, OrderingFilter],
                "queryset": model.objects.all(),
            },
        )
