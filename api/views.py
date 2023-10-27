from rest_framework import viewsets

from .models import Master, Business
from .serializers import MasterSerializer, SalonSerializer


class SalonViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = SalonSerializer


class MasterViewSet(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer
