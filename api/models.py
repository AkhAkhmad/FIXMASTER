from django.contrib.auth.models import User
from django.db import models

from .data import CHOICES_GENDER, ESTABLISHMENT_TYPE


class Business(models.Model):
    image = models.ImageField()
    telegram_id = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    contact_phone = models.CharField(max_length=30)
    status = models.BooleanField()
    time_begin = models.TimeField()
    time_end = models.TimeField()
    work_schedule = models.CharField(max_length=30)
    type = models.CharField(max_length=20,
                            choices=ESTABLISHMENT_TYPE)
    collection_image = models.OneToOneField('CollectionImage', on_delete=models.CASCADE)
    master = models.ForeignKey('Master', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'


class Master(models.Model):
    telegram_id = models.IntegerField()
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    image = models.ImageField()
    gender = models.CharField(
        max_length=30,
        choices=CHOICES_GENDER,
        default='WOMEN'
    )
    service = models.ManyToManyField('Service', through='MasterItem')
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


class MasterItem(models.Model):
    master_item = models.ForeignKey(Master, on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)


class Image(models.Model):
    title = models.CharField(max_length=30)
    file = models.ImageField()
    alt = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class CollectionImage(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    priority = models.IntegerField()
    
    def __str__(self):
        return str(self.item)

    class Meta:
        verbose_name = 'Коллекция изображений'
        verbose_name_plural = 'Коллекция изображений'


class Service(models.Model):
    title = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    min_time = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'


class Customer(models.Model):
    telegram_id = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Booking(models.Model):
    date_booking = models.DateTimeField()
    username = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    comment = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    int = models.IntegerField()

    def __str__(self):
        return self.username
