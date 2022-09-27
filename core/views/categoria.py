from rest_framework.viewsets import ModelViewSet

from core.models import categoria
from core.serializers import categoriaSerializer


class categoriaViewSet(ModelViewSet):
    queryset = categoria.objects.all()
    serializer_class = categoriaSerializer