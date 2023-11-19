from datetime import date

from rest_framework import generics
from rest_framework.exceptions import ValidationError

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
        order_date = vars(request).get('_full_data')['begin_date']
        order_time = vars(request).get('_full_data')['begin_time']
        master_id = vars(request).get('_full_data')['master']
        master_instance = models.Master.objects.filter(pk=master_id).first()
        existing_booking = models.Booking.objects.filter(master=master_id, booking_date=order_date,
                                                         booking_time=order_time).first()
        if existing_booking:
            raise ValidationError({"error": "Бронь уже существует"})
        response = super().create(request, *args, **kwargs)
        models.Booking.objects.create(booking_date=order_date, booking_time=order_time,
                                      master=master_instance)
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


class CustomerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    lookup_field = 'phone'


class BookingListApiView(generics.ListAPIView):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer

    def get_queryset(self):
        today = date.today()
        queryset = super().get_queryset()
        queryset = queryset.filter(booking_date=today)
        return queryset
