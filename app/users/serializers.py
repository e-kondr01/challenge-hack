from rest_framework import serializers
from users.models import User


class CurrentUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "balance", "profile_picture_url")


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "profile_picture_url")
