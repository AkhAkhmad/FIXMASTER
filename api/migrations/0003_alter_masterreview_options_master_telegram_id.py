# Generated by Django 4.2.6 on 2023-10-22 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_masterreview_options_salon_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='masterreview',
            options={},
        ),
        migrations.AddField(
            model_name='master',
            name='telegram_id',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
    ]
