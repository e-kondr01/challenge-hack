from rest_framework import serializers
from users.models import User
from django.db import models
from django.db import transaction

from .models import Donation


class ReceivedDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = (
            "id",
            "amount",
            "currency",
            "author_name",
            "message",
            "created_at",
            "attachment_url",
        )


class MakeDonationSerializer(serializers.ModelSerializer):
    currency = serializers.HiddenField(default="Руб.")

    class Meta:
        model = Donation
        fields = (
            "id",
            "amount",
            "author_name",
            "message",
            "attachment_url",
            "donated_to",
            "currency",
        )

    def create(self, validated_data: dict):
        """
        При создании доната нужно увеличить баланс пользователя
        """
        with transaction.atomic():
            donation = super().create(validated_data)
            donated_to: User = validated_data.get("donated_to")
            donated_to.balance = models.F("balance") + validated_data["amount"]
            donated_to.save()
            return donation
