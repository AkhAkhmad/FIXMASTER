from rest_framework import generics

from . import models, serializers


class BusinessListAPIView(generics.ListAPIView):
    queryset = models.Business.objects.all()
    serializer_class = serializers.BusinessSerializer


class BusinessCreateAPIView(generics.CreateAPIView):
    queryset = models.Business.objects.all()
    serializer_class = serializers.BusinessSerializer


class BusinessRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Business.objects.all()
    serializer_class = serializers.BusinessSerializer
    lookup_field = 'telegram_id'


class BusinessUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Business.objects.all()
    serializer_class = serializers.BusinessSerializer
    lookup_field = 'telegram_id'


class BusinessDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Business.objects.all()
    serializer_class = serializers.BusinessSerializer
    lookup_field = 'telegram_id'


class MasterListAPIView(generics.ListAPIView):
    queryset = models.Master.objects.all()
    serializer_class = serializers.MasterSerializer


class MasterCreateAPIView(generics.CreateAPIView):
    queryset = models.Master.objects.all()
    serializer_class = serializers.MasterSerializer


class MasterRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Master.objects.all()
    serializer_class = serializers.MasterSerializer


class MasterUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Master.objects.all()
    serializer_class = serializers.MasterSerializer


class MasterDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Master.objects.all()
    serializer_class = serializers.MasterSerializer


class ServiceListAPIView(generics.ListAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class ServiceCreateAPIView(generics.CreateAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class ServiceRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class ServiceUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class ServiceDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class OrderListAPIView(generics.ListAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class CustomerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    lookup_field = 'phone'
