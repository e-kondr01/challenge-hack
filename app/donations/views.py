from rest_framework.generics import ListAPIView
from donations.models import Donation
from donations.serializers import DonationSerializer


class ReceivedDonationsListView(ListAPIView):
    """
    Список донатов, которые получены текущим пользователем.
    """

    queryset = Donation.objects.none()
    serializer_class = DonationSerializer

    def get_queryset(self):
        return Donation.objects.filter(donated_to=self.request.user)
