from rest_framework.serializers import ModelSerializer

from core.serializers.user import userSerializer
from core.models import resenha, livro


class resenhaSerializer(ModelSerializer):
    class Meta:
        model = resenha
        fields = "__all__"

class livroSerializer(ModelSerializer):
    resenha = resenhaSerializer(many=True)
    class Meta:
        model = livro
        fields = "__all__"
        
class resenhadetailSerializer(ModelSerializer):
    user_resenha = userSerializer()
    livro_resenha = livroSerializer()
    class Meta:
        model = resenha
        fields = "__all__"