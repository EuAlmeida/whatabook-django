from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from core.models import categoria, livro, editora, autor, user

from core.serializers import autorSerializer, categoriaSerializer, editoraSerializer, livroSerializer, livrodetailSerializer, userSerializer


class categoriaViewSet(ModelViewSet):
    queryset = categoria.objects.all()
    serializer_class = categoriaSerializer


class editoraViewSet(ModelViewSet):
    queryset = editora.objects.all()
    serializer_class = editoraSerializer

class livroViewSet(ModelViewSet):
    queryset = livro.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return livrodetailSerializer
        return livroSerializer


class autorViewSet(ModelViewSet):
    queryset = autor.objects.all()
    serializer_class = autorSerializer

class userViewSet(ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer