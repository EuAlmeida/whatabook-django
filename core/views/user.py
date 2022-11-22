from rest_framework.viewsets import ModelViewSet

from core.models import user
from core.serializers import userSerializer, userPostSerializer


class userViewSet(ModelViewSet):
    queryset = user.objects.all()
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve" or self.action == "update":
            return userSerializer
        return userPostSerializer

class UsuarioLogado(ModelViewSet):
    serializer_class = userSerializer
    def get_queryset(self):
        usuario = self.request.user.id
        queryset = user.objects.filter(id=usuario)
        return queryset