from django.urls import path
from donations import views

urlpatterns = [
    path("/received-donations", views.ReceivedDonationsListView.as_view()),
]
