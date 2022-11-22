from rest_framework.viewsets import ModelViewSet

from core.models import resenha
from core.serializers import resenhadetailSerializer, resenhaSerializer


class resenhaViewSet(ModelViewSet):
    queryset = resenha.objects.all()
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return resenhadetailSerializer
        return resenhaSerializer
