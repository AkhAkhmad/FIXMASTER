from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Master, Salon
from .serializers import MasterSerializer, SalonSerializer


class SalonViewSet(viewsets.ViewSet):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer

    def list(self, request):
        queryset = Salon.objects.all()
        serializer = SalonSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SalonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        salon = get_object_or_404(self.queryset, pk=pk)
        serializer = SalonSerializer(salon)
        return Response(serializer.data)

    def update(self, request, pk=None):
        salon = Salon.objects.get(pk=pk)
        serializer = SalonSerializer(salon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        salon = Salon.objects.get(pk=pk)
        salon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MasterViewSet(viewsets.ViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

    def list(self, request):
        queryset = Master.objects.all()
        serializer = MasterSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        salon = get_object_or_404(self.queryset, pk=pk)
        serializer = MasterSerializer(salon)
        return Response(serializer.data)

    def update(self, request, pk=None):
        master = Salon.objects.get(pk=pk)
        serializer = MasterSerializer(master, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        master = Salon.objects.get(pk=pk)
        master.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
