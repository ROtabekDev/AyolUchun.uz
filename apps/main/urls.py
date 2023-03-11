from django.urls import path

from .views import (
    ContactCreateAPIView, NotificationListAPIView
)

urlpatterns = [
    path('create/contact/', ContactCreateAPIView.as_view()),
    path('notification/list/', NotificationListAPIView.as_view())
]