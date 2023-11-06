from django.urls import path

from . import views

urlpatterns = [
    path('business/', views.BusinessListAPIView.as_view()),
    path('business/create', views.BusinessCreateAPIView.as_view()),
    path('business/update/<int:pk>', views.BusinessUpdateAPIView.as_view()),
    path('business/delete/<int:pk>', views.BusinessDestroyAPIView.as_view()),
    path('master/', views.MasterListAPIView.as_view()),
    path('master/create', views.MasterCreateAPIView.as_view()),
    path('master/update/<int:pk>', views.MasterUpdateAPIView.as_view()),
    path('master/delete/<int:pk>', views.MasterDestroyAPIView.as_view()),
    path('service/', views.ServiceListAPIView.as_view()),
    path('service/create', views.ServiceCreateAPIView.as_view()),
    path('service/update/<int:pk>', views.ServiceUpdateAPIView.as_view()),
    path('service/delete/<int:pk>', views.ServiceDestroyAPIView.as_view()),
    path('order/', views.ServiceListAPIView.as_view()),
    path('order/create', views.ServiceCreateAPIView.as_view()),
    path('order/update/<int:pk>', views.ServiceUpdateAPIView.as_view()),
    path('order/delete/<int:pk>', views.ServiceDestroyAPIView.as_view()),
]
