from rest_framework.viewsets import ModelViewSet

from core.models import livro
from core.serializers import livrodetailSerializer, livroSerializer


class livroViewSet(ModelViewSet):
    queryset = livro.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return livrodetailSerializer
        return livroSerializer