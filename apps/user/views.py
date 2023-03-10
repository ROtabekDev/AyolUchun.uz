from rest_framework.generics import CreateAPIView

from .models import User

from .serializers import RegisterSerializer, LoginSerializer

class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer


class LoginAPIView(CreateAPIView): 
    serializer_class = LoginSerializer

    def perform_create(self, serializer):
        pass