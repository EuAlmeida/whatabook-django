from rest_framework.viewsets import ModelViewSet

from core.models import midia
from core.serializers import midiaSerializer


class midiaViewSet(ModelViewSet):
    queryset = midia.objects.all()
    serializer_class = midiaSerializer
    