from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import CreateContactSerializer, NotificationListSerializer, NotificationDetailSerializer

from .models import Notification

class ContactCreateAPIView(CreateAPIView):
    serializer_class = CreateContactSerializer


class NotificationListAPIView(ListAPIView):
    serializer_class = NotificationDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Notification.objects.filter(user_id=self.request.user)
    

class NotificationDetailAPIView(RetrieveAPIView):
    serializer_class = NotificationDetailSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'slug'

    def get_queryset(self): 
        return Notification.objects.filter(user_id=self.request.user)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        notification = Notification.objects.filter(id=instance.id)[0]
        notification.viewed = True  
        notification.save()  
         
        return Response(serializer.data)
