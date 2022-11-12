from rest_framework.generics import ListAPIView, CreateAPIView
from donations.models import Donation
from donations.serializers import ReceivedDonationSerializer, MakeDonationSerializer
from rest_framework.permissions import AllowAny


class ReceivedDonationsListView(ListAPIView):
    """
    Список донатов, которые получены текущим пользователем.
    """

    queryset = Donation.objects.none()
    serializer_class = ReceivedDonationSerializer

    def get_queryset(self):
        return Donation.objects.filter(donated_to=self.request.user)


class MakeDonationView(CreateAPIView):
    """
    Внести донат.
    """

    queryset = Donation.objects.none()
    serializer_class = MakeDonationSerializer
    permission_classes = (AllowAny,)
