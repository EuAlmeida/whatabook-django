from rest_framework.serializers import ModelSerializer

from core.models import midia
from drf_extra_fields.fields import Base64ImageField

class midiaSerializer(ModelSerializer):
    model = midia
    fields = "__all__"