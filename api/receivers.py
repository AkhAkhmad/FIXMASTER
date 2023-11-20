from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models


@receiver(post_save, sender=models.Order)
def create_booking(sender, created, instance, **kwargs):
    if created:
        models.Booking.objects.create(booking_date=instance.begin_date, booking_time=instance.begin_time,
                                      master=instance.master)
