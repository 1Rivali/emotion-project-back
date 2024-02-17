from django.urls import path
from .views import (
    UserCreateAPIView,
    CreateTokenView,
    ManageUserView,
    ListUsersView,
    DeleteView,
)

urlpatterns = [
    path("register/", UserCreateAPIView.as_view()),
    path("login/", CreateTokenView.as_view()),
    path("user/<pk>", ManageUserView.as_view()),
    path("user/list/", ListUsersView.as_view()),
    path("user/<pk>/", DeleteView.as_view()),
]
