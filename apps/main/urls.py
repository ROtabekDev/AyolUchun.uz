from django.urls import path

from .views import (
    ContactCreateAPIView, NotificationListAPIView, NotificationDetailAPIView
)

urlpatterns = [
    path('create/contact/', ContactCreateAPIView.as_view()),
    path('notification/list/', NotificationListAPIView.as_view()),
    path('notification/detail/<str:slug>/', NotificationDetailAPIView.as_view()),
]