from . import models


def create_booking(sender, created, instance, **kwargs):
    if created:
        models.Booking.objects.create(booking_date=instance.begin_date, booking_time=instance.begin_time,
                                      master=instance.master)
