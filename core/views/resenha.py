from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.models import resenha

from core.serializers import resenhaSerializer, resenhadetailSerializer

class resenhaViewSet(ModelViewSet):
    queryset = resenha.objects.all()
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return resenhadetailSerializer
        return resenhaSerializer
