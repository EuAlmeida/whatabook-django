from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.models import user

from core.serializers import userSerializer

class userViewSet(ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer
    permission_classes = [IsAuthenticated]