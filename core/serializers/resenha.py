from rest_framework.serializers import ModelSerializer
from core.models import resenha

class resenhaSerializer(ModelSerializer):
    class Meta:
        model = resenha
        fields = "__all__"
class resenhadetailSerializer(ModelSerializer):
    class Meta:
        model = resenha
        fields = "__all__"
        depth = 1