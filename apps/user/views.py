from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, UpdateAPIView
)
from rest_framework.permissions import AllowAny

from .models import UserProfile


from .serializers import (
    RegisterSerializer, LoginSerializer, UserDetailSerializer,
    UserProfileUpdateSerializer
)

class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,) 


class LoginAPIView(CreateAPIView): 
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,) 

    def perform_create(self, serializer):
        pass

class UserProfileRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserDetailSerializer 

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj


class UserProfileUpdateAPIView(UpdateAPIView):
    serializer_class = UserProfileUpdateSerializer
    
    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj
