from celery import shared_task
from django.utils import timezone

from . import models


@shared_task
def update_business_status():
    current_time = timezone.now().time()
    businesses = models.Business.objects.all()

    for business in businesses:
        if business.time_begin and business.time_end:
            if business.time_begin <= current_time < business.time_end:
                business.status = True
            else:
                business.status = False
        else:
            business.status = False

        business.save()
