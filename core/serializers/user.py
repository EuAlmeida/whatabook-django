from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import Group
from .midia import midiaSerializer

from core.models import user


class userSerializer(ModelSerializer):
    midia = midiaSerializer()
    class Meta:
        model = user
        fields = ['id','password', 'username', 'email', 'telefone', 'biografia', 'localizacao', 'data_nascimento', 'midia', 'is_editora', 'livros']
        depth = 1

class userPostSerializer(ModelSerializer):
    class Meta:
        model = user
        fields = ['id','password', 'username', 'email', 'data_nascimento', 'biografia', 'localizacao', 'is_editora']

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        editora = validated_data.pop("is_editora", None)
        if editora:
            instance.groups.add(Group.objects.get(name="Editora"))
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            instance.set_password(password)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.biografia = validated_data.get('biografia', instance.biografia)
        instance.localizacao = validated_data.get('localizacao', instance.localizacao)
        instance.data_nascimento = validated_data.get('data_nascimento', instance.data_nascimento)
        instance.save()
        return instance