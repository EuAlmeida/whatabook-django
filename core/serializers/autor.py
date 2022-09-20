from rest_framework.serializers import ModelSerializer
from core.models import autor

class autorSerializer(ModelSerializer):
    class Meta:
        model = autor
        fields = "__all__"