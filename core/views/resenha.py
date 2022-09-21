from rest_framework.viewsets import ModelViewSet

from core.models import resenha

from core.serializers import resenhaSerializer, resenhadetailSerializer

class resenhaViewSet(ModelViewSet):
    queryset = resenha.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return resenhadetailSerializer
        return resenhaSerializer
