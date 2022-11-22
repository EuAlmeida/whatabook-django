from rest_framework.serializers import ModelSerializer

from core.models import midia
from drf_extra_fields.fields import Base64ImageField

class midiaSerializer(ModelSerializer):
    imagem = Base64ImageField()
    class Meta:
        model = midia
        fields = "__all__"