from rest_framework.serializers import ModelSerializer

from core.models import editora


class editoraSerializer(ModelSerializer):
    class Meta:
        model = editora
        fields = "__all__"