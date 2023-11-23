from django.db import models

from . import data


class Business(models.Model):
    telegram_id = models.CharField('Айди Телеграм-аккаунта', max_length=30)
    title = models.CharField('Название', max_length=30)
    image = models.ImageField('Изображение', upload_to='business')
    address = models.CharField('Адрес', max_length=30)
    contact_phone = models.CharField('Номер телефона', max_length=30)
    status = models.BooleanField('Статус')
    time_begin = models.TimeField('Начальное время')
    time_end = models.TimeField('Конечное время')
    work_schedule = models.CharField('График работы', max_length=30)
    type = models.CharField('Тип', max_length=20,
                            choices=data.ESTABLISHMENT_TYPE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'


class Master(models.Model):
    telegram_id = models.CharField('Айди Телеграм-аккаунта', max_length=30, null=True, blank=True)
    name = models.CharField('Имя', max_length=30, null=True, blank=True)
    surname = models.CharField('Фамилия', max_length=30, null=True, blank=True)
    image = models.ImageField('Изображние', upload_to='master', null=True, blank=True)
    gender = models.CharField(
        'Пол',
        max_length=30,
        choices=data.CHOICES_GENDER,
        default='WOMEN',
        null=True, blank=True
    )
    business = models.ForeignKey(Business, on_delete=models.CASCADE, verbose_name='Бизнесс', null=True, blank=True)
    service = models.ManyToManyField('Service', verbose_name='Сервис', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


class Image(models.Model):
    title = models.CharField('Название', max_length=30, null=True, blank=True)
    image = models.ImageField('Изображение', upload_to='image', null=True, blank=True)
    priority = models.IntegerField('Приоритет', null=True, blank=True)
    collection_Images = models.ForeignKey(
        'CollectionImages', on_delete=models.CASCADE,
        verbose_name='Коллекция Изображений', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class CollectionImages(models.Model):
    title = models.CharField('Название', max_length=50, null=True, blank=True)
    business = models.OneToOneField(Business, on_delete=models.CASCADE, verbose_name='Бизнес', null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Коллекция изображений'
        verbose_name_plural = 'Коллекция изображений'


class Service(models.Model):
    title = models.CharField('Название', max_length=30, null=True, blank=True)
    price = models.PositiveIntegerField('Цена', null=True, blank=True)
    min_time = models.IntegerField('Минимальное время', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'


class Customer(models.Model):
    telegram_id = models.CharField('Айди Телеграм-аккаунта', max_length=30, null=True, blank=True)
    phone = models.CharField('Номер телефона', max_length=30, null=True, blank=True)
    username = models.CharField('Имя пользователя', max_length=30, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Booking(models.Model):
    booking_date = models.DateField(null=True, blank=True)
    booking_time = models.TimeField(null=True, blank=True)
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name='Мастер', null=True, blank=True)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'

    def __str__(self):
        return str(self.master)


class Order(models.Model):
    begin_date = models.DateField('Дата начала', null=True, blank=True)
    begin_time = models.TimeField('Время начала', null=True, blank=True)
    status = models.CharField('Статус', max_length=20, choices=data.CHOICES_STATUS, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент', null=True, blank=True)
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name='Мастер', null=True, blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return str(self.master)
