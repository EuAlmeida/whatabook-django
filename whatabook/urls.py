from django.contrib import admin
from django.urls import include,path
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from core.views import autorViewSet, categoriaViewSet, editoraViewSet, livroViewSet, resenhaViewSet, userViewSet, listafavViewSet
router = DefaultRouter()
router.register(r'categorias', categoriaViewSet)
router.register(r'editora', editoraViewSet)
router.register(r'livro', livroViewSet)
router.register(r'autor', autorViewSet)
router.register(r'user', userViewSet)
router.register(r'listafav', listafavViewSet)
router.register(r'resenha',resenhaViewSet)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)