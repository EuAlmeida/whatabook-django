from rest_framework.serializers import ModelSerializer
from core.models import listafav

class listafavSerializer(ModelSerializer):
    class Meta:
        model = listafav
        fields  = "__all__"

class listafavdetailSerializer(ModelSerializer):
    class Meta:
        model = listafav
        fields = "__all__"
        depth = 1
