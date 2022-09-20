from rest_framework.viewsets import ModelViewSet

from core.models import editora

from core.serializers import editoraSerializer

class editoraViewSet(ModelViewSet):
    queryset = editora.objects.all()
    serializer_class = editoraSerializer
    