from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Donation
from .serializers import ReceivedDonationSerializer


@receiver(post_save, sender=Donation)
def notify_new_donation(sender, instance: Donation, created: bool = False, **kwargs):
    if created:
        serializer = ReceivedDonationSerializer(instance)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "donations", {"type": "new.donation", "data": serializer.data}
        )
