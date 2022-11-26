from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import (
    autorViewSet,
    categoriaViewSet,
    editoraViewSet,
    listafavViewSet,
    listafavPKView,
    livroViewSet,
    resenhaViewSet,
    userViewSet,
    UsuarioLogado,
    midiaViewSet,
    livrosAutorView
)

router = DefaultRouter()
router.register(r'categorias', categoriaViewSet)
router.register(r'editora', editoraViewSet)
router.register(r'livro', livroViewSet)
router.register(r'livros-autor', livrosAutorView, basename='livro')
router.register(r'autor', autorViewSet)
router.register(r'user', userViewSet)
router.register(r'listafav', listafavViewSet)
router.register(r'listafavPK', listafavPKView, basename="lista")
router.register(r'resenha',resenhaViewSet, basename="resenha")
router.register(r'detail-user', UsuarioLogado, basename="usuariologado")
router.register(r'midia', midiaViewSet)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

