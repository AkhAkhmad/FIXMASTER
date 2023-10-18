from django.urls import include, path

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'salons', views.SalonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
