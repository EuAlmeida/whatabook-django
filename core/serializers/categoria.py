from rest_framework.serializers import ModelSerializer

from core.serializers.livro import livroSerializer
from core.models import categoria


class categoriaSerializer(ModelSerializer):
    livros = livroSerializer
    class Meta:
        model = categoria
        fields = ("id", "nome_categoria", "livros")
        depth = 1