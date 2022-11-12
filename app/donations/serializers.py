from rest_framework import serializers

from .models import Donation


class DonationSerializer(serializers.ModelSerializer):
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
