from rest_framework.viewsets import ModelViewSet

from core.models import user
from core.serializers import userSerializer


class userViewSet(ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer

class UsuarioLogado(ModelViewSet):
    serializer_class = userSerializer
    def get_queryset(self):
        usuario = self.request.user.id
        queryset = user.objects.filter(id=usuario)
        return queryset