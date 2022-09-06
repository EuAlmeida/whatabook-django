from django.contrib import admin
from django.urls import include,path
from rest_framework.routers import DefaultRouter

from core.views import categoriaViewSet, editoraViewSet, livroViewSet
router = DefaultRouter()
router.register(r'categorias', categoriaViewSet)
router.register(r'editora', editoraViewSet)
router.register(r'livro', livroViewSet)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
