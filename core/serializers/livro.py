from rest_framework.serializers import ModelSerializer
from core.models import livro

class livroSerializer(ModelSerializer):
    class Meta:
        model = livro
        fields = "__all__"
       
class livrodetailSerializer(ModelSerializer):
    class Meta:
        model = livro
        fields = "__all__"
        depth = 1