from django.db import models

from .data import CHOICES_GENDER, ESTABLISHMENT_TYPE


class Business(models.Model):
    image = models.ImageField('Изображение')
    telegram_id = models.CharField('Айди Телеграм-аккаунта', max_length=30)
    title = models.CharField('Название', max_length=30)
    address = models.CharField('Адрес', max_length=30)
    contact_phone = models.CharField('Номер телефона', max_length=30)
    status = models.BooleanField('Статус')
    time_begin = models.TimeField('Начальное время')
    time_end = models.TimeField('Конечное время')
    work_schedule = models.CharField('График работы', max_length=30)
    type = models.CharField('Тип', max_length=20,
                            choices=ESTABLISHMENT_TYPE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'


class Master(models.Model):
    telegram_id = models.CharField('Айди Телеграм-аккаунта', max_length=30)
    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    image = models.ImageField('Изображние')
    gender = models.CharField(
        'Пол',
        max_length=30,
        choices=CHOICES_GENDER,
        default='WOMEN'
    )
    business = models.ForeignKey(Business, on_delete=models.CASCADE, verbose_name='Бизнесс')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


class Image(models.Model):
    title = models.CharField('Название', max_length=30)
    image = models.ImageField('Изображение')
    priority = models.IntegerField('Приоритет')
    collection_Images = models.ForeignKey(
        'CollectionImages', on_delete=models.CASCADE,
        verbose_name='Коллекция Изображений')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class CollectionImages(models.Model):
    title = models.CharField('Название', max_length=50)
    business = models.OneToOneField(Business, on_delete=models.CASCADE, verbose_name='Бизнесс')

    def __str__(self):
        return str(self.item)

    class Meta:
        verbose_name = 'Коллекция изображений'
        verbose_name_plural = 'Коллекция изображений'


class Service(models.Model):
    title = models.CharField('Название', max_length=30)
    price = models.PositiveIntegerField('Цена')
    min_time = models.IntegerField('Минимальное время')
    master = models.ManyToManyField(Master, verbose_name='Мастер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'


class Customer(models.Model):
    telegram_id = models.CharField('Айди Телеграм-аккаунта', max_length=30)
    phone = models.CharField('Номер телефона', max_length=30)
    username = models.CharField('Имя пользователя', max_length=30)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Booking(models.Model):
    booking_date = models.DateField()
    booking_time = models.TimeField()
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name='Мастер')

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'


class Order(models.Model):
    begin_date = models.DateField('Дата начала')
    begin_time = models.TimeField('Время начала')
    status = models.CharField('Статус', max_length=20, choices=None)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name='Мастер')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
