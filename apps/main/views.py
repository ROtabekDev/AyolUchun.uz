from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView
)
from rest_framework.permissions import IsAuthenticated

from .serializers import CreateContactSerializer, NotificationListSerializer

from .models import Notification

class ContactCreateAPIView(CreateAPIView):
    serializer_class = CreateContactSerializer


class NotificationListAPIView(ListAPIView):
    serializer_class = NotificationListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Notification.objects.filter(user_id=self.request.user)
