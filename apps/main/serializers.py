from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Contact, Notification, Certificate

class CreateContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = ('first_name', 'email', 'phone_number', 'message')


class NotificationListSerializer(ModelSerializer):

    class Meta:
        model = Notification
        fields = ('title', 'slug', 'message', 'created_at', 'viewed')


class NotificationDetailSerializer(ModelSerializer):

    class Meta:
        model = Notification
        fields = ('title', 'message', 'created_at')

    