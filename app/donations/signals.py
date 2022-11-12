from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver
from donations.consumer import get_donation_consumer_group_name

from .models import Donation
from .serializers import ReceivedDonationSerializer


@receiver(post_save, sender=Donation)
def notify_new_donation(sender, instance: Donation, created: bool = False, **kwargs):
    if created:
        serializer = ReceivedDonationSerializer(instance)
        group_name = get_donation_consumer_group_name(instance.donated_to)
        async_to_sync(get_channel_layer().group_send)(
            group_name,
            {"type": "donation.new", "data": serializer.data},
        )
