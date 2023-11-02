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
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


class Image(models.Model):
    title = models.CharField(max_length=30)
    file = models.ImageField()
    priority = models.IntegerField()
    collection_Images = models.ForeignKey('CollectionImages', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class CollectionImages(models.Model):
    business = models.OneToOneField(Business, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item)

    class Meta:
        verbose_name = 'Коллекция изображений'
        verbose_name_plural = 'Коллекция изображений'


class Service(models.Model):
    title = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    min_time = models.IntegerField()
    master = models.ManyToManyField(Master)

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
    master = models.OneToOneField(Master, on_delete=models.CASCADE)
    business = models.OneToOneField(Business, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
