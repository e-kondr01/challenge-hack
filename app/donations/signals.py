from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver
from donations.consumers import BalanceConsumer, DonationConsumer

from .models import Donation
from .serializers import ReceivedDonationSerializer


@receiver(post_save, sender=Donation)
def notify_new_donation(sender, instance: Donation, created: bool = False, **kwargs):
    if created:
        serializer = ReceivedDonationSerializer(instance)
        group_name = DonationConsumer.get_group_name(instance.donated_to)
        async_to_sync(get_channel_layer().group_send)(
            group_name,
            {"type": "donation.new", "data": serializer.data},
        )

        balance = str(instance.donated_to.balance)
        group_name = BalanceConsumer.get_group_name(instance.donated_to)
        async_to_sync(get_channel_layer().group_send)(
            group_name,
            {"type": "balance.changed", "data": {"balance": balance}},
        )
