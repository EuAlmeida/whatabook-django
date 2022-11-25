from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

from core.serializers.resenha import resenhaSerializer, resenhadetailSerializer
from core.models import livro


class livroSerializer(ModelSerializer):
    resenha = resenhaSerializer(many=True)
    class Meta:
        model = livro
        fields = "__all__"


class livrodetailSerializer(ModelSerializer):
    resenha = resenhaSerializer(many=True)
    medianota = SerializerMethodField()
    class Meta:
        model = livro
        fields = "__all__"
        depth = 1

    def get_medianota(self,instance):
        notas = []
        resenhas = instance.resenha.all()
        if resenhas: 
            for i in resenhas:
                notas.append(i.nota_resenha)
            return sum(notas) / len(notas)
        return 0