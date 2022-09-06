from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from core.models import categoria, livro, user, editora, autor

from core.serializers import categoriaSerializer, editoraSerializer, livroSerializer


class categoriaViewSet(ModelViewSet):
    queryset = categoria.objects.all()
    serializer_class = categoriaSerializer


class editoraViewSet(ModelViewSet):
    queryset = editora.objects.all()
    serializer_class = editoraSerializer

class livroViewSet(ModelViewSet):
    queryset = livro.objects.all()
    serializer_class = livroSerializer
