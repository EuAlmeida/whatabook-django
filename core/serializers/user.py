from rest_framework.serializers import ModelSerializer

from core.models import user
from drf_extra_fields.fields import Base64ImageField

class userSerializer(ModelSerializer):
    class Meta:
        model = user
        fields = ['id','password', 'username', 'email', 'telefone', 'biografia', 'localizacao', 'data_nascimento']