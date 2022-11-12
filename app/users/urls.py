from django.urls import path
from users import views

urlpatterns = [
    path("/current-user", views.CurrentUserInfoView.as_view()),
    path("/users", views.UserListView.as_view()),
]
