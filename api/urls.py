from django.urls import path

from .views import MasterViewSet, SalonViewSet

urlpatterns = [
    path('salon/', SalonViewSet.as_view({'get': 'list'})),
    path('master/', MasterViewSet.as_view({'get': 'list'})),
    path('salon/<int:pk>/', SalonViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('master/<int:pk>/', MasterViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
