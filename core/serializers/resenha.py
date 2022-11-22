from rest_framework.serializers import ModelSerializer

from core.serializers.user import userSerializer
from core.models import resenha


class resenhaSerializer(ModelSerializer):
    class Meta:
        model = resenha
        fields = "__all__"

class resenhadetailSerializer(ModelSerializer):
    user_resenha = userSerializer()
    class Meta:
        model = resenha
        fields = "__all__"