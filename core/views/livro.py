from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.models import livro

from core.serializers import livroSerializer, livrodetailSerializer

class livroViewSet(ModelViewSet):
    queryset = livro.objects.all()
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return livrodetailSerializer
        return livroSerializer