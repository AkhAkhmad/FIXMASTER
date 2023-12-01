from rest_framework import viewsets

from .serializers import SalonSerializer
from .models import Salon


class SalonViewSet(viewsets.ModelViewSet):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer
