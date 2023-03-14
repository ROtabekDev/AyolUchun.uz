from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView
)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import (
    CreateContactSerializer, NotificationListSerializer, 
    NotificationDetailSerializer, CertificateSerializer
)

from .models import Notification, Certificate

from apps.course.models import Course

class ContactCreateAPIView(CreateAPIView):
    serializer_class = CreateContactSerializer


class NotificationListAPIView(ListAPIView):
    serializer_class = NotificationListSerializer
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


class GetCertificateAPIView(APIView):

    def get(self, request, course_slug):
        try: 
            course = Course.objects.get(slug=course_slug)  
            certificate = Certificate.objects.get(course_id=course, user_id=request.user)
            serializer = CertificateSerializer(certificate) 
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:  
            return Response(data={'message: bu kursda sizda sertifikat mavjud emas!'}, status=status.HTTP_400_BAD_REQUEST)

        