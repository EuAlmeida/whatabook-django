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
        model = editora
        fields = "__all__"

