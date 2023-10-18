from django.contrib import admin
from .models import (Image, CollectionImage,
                     Salon, Master, Service, Customer,
                     Booking, MasterReview)

admin.site.register(Image)
admin.site.register(CollectionImage)
admin.site.register(Salon)
admin.site.register(Master)
admin.site.register(Service)
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(MasterReview)
