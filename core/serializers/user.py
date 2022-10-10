from rest_framework.serializers import ModelSerializer

from core.models import user


class userSerializer(ModelSerializer):
    class Meta:
        model = user
        fields = ['password', 'username', 'first_name', 'last_name', 'email', 'cpf', 'telefone']