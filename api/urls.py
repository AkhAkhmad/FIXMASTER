from django.urls import path

from .views import MasterViewSet, SalonViewSet

salon_list = SalonViewSet.as_view({'get': 'list', 'post': 'create'})
master_list = MasterViewSet.as_view({'get': 'list', 'post': 'create'})
salon_detail = SalonViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})
master_detail = MasterViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

urlpatterns = [
    path('salon/', salon_list),
    path('master/', master_list),
    path('salon/<int:pk>/', salon_detail),
    path('master/<int:pk>/', master_detail),
]
