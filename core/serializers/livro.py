from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault
from rest_framework.fields import SerializerMethodField
from drf_extra_fields.fields import Base64ImageField

from core.serializers.resenha import resenhaSerializer, resenhadetailSerializer
from core.models import livro


class livroSerializer(ModelSerializer):
    resenha = resenhaSerializer(many=True)
    class Meta:
        model = livro
        fields = "__all__"


class livrodetailSerializer(ModelSerializer):
    resenha = resenhaSerializer(many=True)
    medianota = SerializerMethodField()
    class Meta:
        model = livro
        fields = "__all__"
        depth = 1

    def get_medianota(self,instance):
        notas = []
        resenhas = instance.resenha.all()
        if resenhas: 
            for i in resenhas:
                notas.append(i.nota_resenha)
            return sum(notas) / len(notas)
        return 0

class livroPostSerializer(ModelSerializer):
    editora_livro = HiddenField(default=CurrentUserDefault())
    capa_livro = Base64ImageField()
    class Meta:
        model = livro
        fields = ("editora_livro" ,"ano_lancamento", "autor_livros", "capa_livro", "categoria_livro", "isbn", "qtd_paginas", "sinopse_livro", "titulo_livro", "url_compra")