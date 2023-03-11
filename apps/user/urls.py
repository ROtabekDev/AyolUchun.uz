from django.urls import path

from .views import (
    RegisterAPIView, LoginAPIView, 
    UserProfileRetrieveAPIView
    )

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='user-register'),
    path('login/', LoginAPIView.as_view(), name='user-login'),
    
    path('profile/detail/', UserProfileRetrieveAPIView.as_view(), name='user-detail'),
]