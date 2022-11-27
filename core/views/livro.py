from rest_framework.viewsets import ModelViewSet

from core.models import livro
from core.serializers import livrodetailSerializer, livroSerializer, livroPostSerializer
from core.paginations import LivrosAutorPagination


class livroViewSet(ModelViewSet):
    # queryset = livro.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return livrodetailSerializer
        elif self.action == 'create':
            return livroPostSerializer
        return livroSerializer
    queryset = livro.objects.all()
    
class livrosAutorView(ModelViewSet):
    serializer_class = livrodetailSerializer
    pagination_class = LivrosAutorPagination
    def get_queryset(self):
        queryset = livro.objects.all()
        autor = self.request.query_params.get('autor')
        if autor is not None:
            queryset = livro.objects.filter(autor_livros=autor)
        return queryset