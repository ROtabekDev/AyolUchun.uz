from rest_framework.generics import (
    CreateAPIView
)

from .serializers import CreateContactSerializer


class ContactCreateAPIView(CreateAPIView):
    serializer_class = CreateContactSerializer