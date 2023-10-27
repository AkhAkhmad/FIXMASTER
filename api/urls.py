from django.urls import path

from .views import MasterViewSet, BusinessViewSet

urlpatterns = [
    path('business/', BusinessViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('master/', MasterViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('business/<int:pk>/', BusinessViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('master/<int:pk>/', MasterViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
