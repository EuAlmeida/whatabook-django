from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.models import autor   

from core.serializers import autorSerializer

class autorViewSet(ModelViewSet):
    queryset = autor.objects.all()
    serializer_class = autorSerializer
    permission_classes = [IsAuthenticated]

