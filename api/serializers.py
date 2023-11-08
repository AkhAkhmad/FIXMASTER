from rest_framework import serializers

from . import models


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


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'
