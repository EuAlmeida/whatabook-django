from rest_framework.viewsets import ModelViewSet

from core.models import livro
from core.serializers import livrodetailSerializer, livroSerializer


class livroViewSet(ModelViewSet):
    queryset = livro.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return livrodetailSerializer
        return livroSerializer

    # def get_queryset(self):
    #     queryset = livro.objects.all()
    #     maiornota = self.request.query_params.get('nota')
    #     if maiornota is not None:
    #         queryset = livro.objects.filter(medianota=5).first()
    #     return queryset