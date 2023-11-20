from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models
from .receivers import create_booking


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Business
        fields = '__all__'


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Master
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'

    def validate(self, data):
        master, begin_date, begin_time = data.get('master'), data.get('begin_date'), data.get('begin_time')
        existing_booking = models.Booking.objects.filter(
            master=master,
            booking_date=begin_date,
            booking_time=begin_time
        ).first()

        if existing_booking:
            raise ValidationError({"error": "Бронь уже существует"})

        return data

    def create(self, validated_data):
        instance = super().create(validated_data)
        create_booking(sender=models.Order, created=True, instance=instance)
        return instance


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'
