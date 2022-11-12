import environ
from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework_simplejwt.views import (
    TokenObtainPairView as TokenObtainPairViewNoExample,
)
from rest_framework.generics import RetrieveAPIView, ListAPIView
from users.models import User
from users.serializers import CurrentUserInfoSerializer, UserListSerializer
from rest_framework.permissions import AllowAny

env = environ.Env()
test_access_token = env.str("TEST_ACCESS_TOKEN", "")
test_refresh_token = env.str("TEST_REFRESH_TOKEN", "")


@extend_schema(
    examples=[
        OpenApiExample(
            "Тестовый токен",
            value={"access": test_access_token, "refresh": test_refresh_token},
            response_only=True,
        )
    ]
)
class TokenObtainPairView(TokenObtainPairViewNoExample):
    """
    Получение JWT для авторизации запросов.
    """


class CurrentUserInfoView(RetrieveAPIView):
    """
    Получение информации о текущем пользователе.
    """

    queryset = User.objects.all()
    serializer_class = CurrentUserInfoSerializer

    def get_object(self):
        return self.request.user


class UserListView(ListAPIView):
    """
    Получение списка пользователей, которым можно отправить донат.
    """

    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = (AllowAny,)
