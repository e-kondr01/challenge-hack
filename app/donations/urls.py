from django.urls import path
from donations import views

urlpatterns = [
    path("", views.DonationListAPIView.as_view()),
]
