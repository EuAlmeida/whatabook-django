from rest_framework.viewsets import ModelViewSet

from core.models import listafav
from core.serializers import listafavdetailSerializer, listafavSerializer


class listafavViewSet(ModelViewSet):
    def get_queryset(self):
        queryset = listafav.objects.filter(user_lista=self.request.user)
        return queryset 
    
    serializer_class = listafavSerializer
    queryset = listafav.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return listafavdetailSerializer
        return listafavSerializer