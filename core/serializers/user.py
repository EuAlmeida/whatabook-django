from rest_framework.serializers import ModelSerializer

from core.models import user


class userSerializer(ModelSerializer):
    class Meta:
        model = user
        fields = "__all__"