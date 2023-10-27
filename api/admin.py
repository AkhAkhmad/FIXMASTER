from django.contrib import admin

from .models import (Booking, Business, CollectionImage, Customer, Image,
                     Master, Service)

admin.site.register(Image)
admin.site.register(CollectionImage)
admin.site.register(Business)
admin.site.register(Master)
admin.site.register(Service)
admin.site.register(Customer)
admin.site.register(Booking)
