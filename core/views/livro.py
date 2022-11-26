from rest_framework.viewsets import ModelViewSet

from core.models import livro
from core.serializers import livrodetailSerializer, livroSerializer
from core.paginations import ResenhaPagination


class livroViewSet(ModelViewSet):
    # queryset = livro.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return livrodetailSerializer
        return livroSerializer
    queryset = livro.objects.all()
    
class livrosAutorView(ModelViewSet):
    serializer_class = livrodetailSerializer
    pagination_class = ResenhaPagination
    def get_queryset(self):
        queryset = livro.objects.all()
        autor = self.request.query_params.get('autor')
        if autor is not None:
            queryset = livro.objects.filter(autor_livros=autor)
        return queryset