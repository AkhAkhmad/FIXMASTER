from datetime import date
from django.db.models.signals import post_save
from .receivers import create_booking

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

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        post_save.connect(create_booking, sender=models.Order)
        return response


class OrderRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class CustomerListAPIView(generics.ListAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class CustomerCreateAPIView(generics.CreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class CustomerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    lookup_field = 'phone'


class CustomerUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    lookup_field = 'phone'


class CustomerDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    lookup_field = 'phone'


class BookingListApiView(generics.ListAPIView):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    lookup_field = 'master'

    def get_queryset(self):
        master_id = self.kwargs['master']
        today = date.today()
        queryset = super().get_queryset()
        queryset = queryset.filter(master=master_id, booking_date=today)
        return queryset
