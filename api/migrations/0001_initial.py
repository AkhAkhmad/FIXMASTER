# Generated by Django 4.2.6 on 2023-11-06 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='business', verbose_name='Изображение')),
                ('telegram_id', models.CharField(max_length=30, verbose_name='Айди Телеграм-аккаунта')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('address', models.CharField(max_length=30, verbose_name='Адрес')),
                ('contact_phone', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('status', models.BooleanField(verbose_name='Статус')),
                ('time_begin', models.TimeField(verbose_name='Начальное время')),
                ('time_end', models.TimeField(verbose_name='Конечное время')),
                ('work_schedule', models.CharField(max_length=30, verbose_name='График работы')),
                ('type', models.CharField(choices=[('SALON', 'Салон Красоты'), ('BEAUTY', 'Парикмахерская')], max_length=20, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Салон',
                'verbose_name_plural': 'Салоны',
            },
        ),
        migrations.CreateModel(
            name='CollectionImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('business', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.business', verbose_name='Бизнесс')),
            ],
            options={
                'verbose_name': 'Коллекция изображений',
                'verbose_name_plural': 'Коллекция изображений',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=30, verbose_name='Айди Телеграм-аккаунта')),
                ('phone', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('username', models.CharField(max_length=30, verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=30, verbose_name='Айди Телеграм-аккаунта')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('image', models.ImageField(upload_to='master', verbose_name='Изображние')),
                ('gender', models.CharField(choices=[('MEN', 'Мужчина'), ('WOMEN', 'Женщина')], default='WOMEN', max_length=30, verbose_name='Пол')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.business', verbose_name='Бизнесс')),
            ],
            options={
                'verbose_name': 'Мастер',
                'verbose_name_plural': 'Мастера',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('min_time', models.IntegerField(verbose_name='Минимальное время')),
                ('master', models.ManyToManyField(to='api.master', verbose_name='Мастер')),
            ],
            options={
                'verbose_name': 'Сервис',
                'verbose_name_plural': 'Сервисы',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateField(verbose_name='Дата начала')),
                ('begin_time', models.TimeField(verbose_name='Время начала')),
                ('status', models.CharField(choices=[('New', 'Новый'), ('InProgress', 'В прогрессе'), ('Done', 'Закончено')], max_length=20, verbose_name='Статус')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer', verbose_name='Клиент')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.master', verbose_name='Мастер')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('image', models.ImageField(upload_to='image', verbose_name='Изображение')),
                ('priority', models.IntegerField(verbose_name='Приоритет')),
                ('collection_Images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.collectionimages', verbose_name='Коллекция Изображений')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField()),
                ('booking_time', models.TimeField()),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.master', verbose_name='Мастер')),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронирование',
            },
        ),
    ]