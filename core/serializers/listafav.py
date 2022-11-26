from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault
from core.models import listafav


class listafavSerializer(ModelSerializer):
    user_lista = HiddenField(default=CurrentUserDefault())
    class Meta:
        model = listafav
        fields  = "__all__"

class listafavdetailSerializer(ModelSerializer):
    class Meta:
        model = listafav
        fields = "__all__"
        depth = 1
