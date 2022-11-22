from rest_framework.serializers import ModelSerializer

from core.serializers.midia import midiaSerializer
from core.models import user

class userSerializer(ModelSerializer):
    midia = midiaSerializer()
    class Meta:
        model = user
        fields = ['id','password', 'username', 'email', 'telefone', 'biografia', 'localizacao', 'data_nascimento', 'midia']

class userPostSerializer(ModelSerializer):
    class Meta:
        model = user
        fields = ['id','password', 'username', 'email', 'data_nascimento']

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        # instance.groups.add(Group.objects.get(name="leitor"))
        return instance