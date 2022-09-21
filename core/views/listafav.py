from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import listafav

from core.serializers import listafavSerializer,listafavdetailSerializer

class listafavViewSet(ModelViewSet):
    queryset = listafav.objects.all()
    serializer_class = listafavSerializer
    queryset = listafav.objects.all()
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return listafavdetailSerializer
        return listafavSerializer