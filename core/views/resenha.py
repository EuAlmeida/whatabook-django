from rest_framework.viewsets import ModelViewSet

from core.models import resenha
from core.serializers import resenhadetailSerializer, resenhaSerializer
from core.paginations import ResenhaPagination


class resenhaViewSet(ModelViewSet):
    pagination_class = ResenhaPagination
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return resenhadetailSerializer
        return resenhaSerializer

    def get_queryset(self):
        queryset = resenha.objects.all()
        livro = self.request.query_params.get('livro')
        if livro is not None:
            queryset = queryset.filter(livro_resenha=livro)
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = queryset.filter(user_resenha=user)
        
        return queryset 
