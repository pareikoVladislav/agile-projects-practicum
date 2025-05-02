from rest_framework.generics import CreateAPIView

from projects.models import User
from projects.serializers.user import RegisterUserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()