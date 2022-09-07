from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from core.models import categoria, listafav, livro, editora, autor, resenha, user

from core.serializers import autorSerializer, categoriaSerializer, editoraSerializer, listafavSerializer, listafavdetailSerializer, livroSerializer, livrodetailSerializer, resenhaSerializer, resenhadetailSerializer, userSerializer


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

class listafavViewSet(ModelViewSet):
    queryset = listafav.objects.all()
    serializer_class = listafavSerializer
    queryset = listafav.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return listafavdetailSerializer
        return listafavSerializer

class resenhaViewSet(ModelViewSet):
    queryset = resenha.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return resenhadetailSerializer
        return resenhaSerializer
