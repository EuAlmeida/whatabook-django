from django.contrib import admin
from django.urls import include,path
from rest_framework.routers import DefaultRouter

from core.views import categoriaViewSet, editoraViewSet
router = DefaultRouter()
router.register(r'categorias', categoriaViewSet)
router.register(r'editora', editoraViewSet)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
