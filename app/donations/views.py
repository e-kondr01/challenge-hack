from rest_framework.generics import ListAPIView
from donations.models import Donation
from donations.serializers import DonationSerializer


class DonationListAPIView(ListAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
