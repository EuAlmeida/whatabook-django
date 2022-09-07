from xml.parsers.expat import model
from rest_framework.serializers import ModelSerializer

from core.models import categoria, editora, livro, autor, user


class categoriaSerializer(ModelSerializer):
    class Meta:
        model = categoria
        fields = "__all__"

class editoraSerializer(ModelSerializer):
    class Meta:
        model = editora
        fields = "__all__"

class livroSerializer(ModelSerializer):
    class Meta:
        model = livro
        fields = "__all__"
class livrodetailSerializer(ModelSerializer):
    class Meta:
        model = livro
        fields = "__all__"
        depth = 1

class autorSerializer(ModelSerializer):
    class Meta:
        model = autor
        fields = "__all__"

class userSerializer(ModelSerializer):
    class Meta:
        model = user
        fields = "__all__"


