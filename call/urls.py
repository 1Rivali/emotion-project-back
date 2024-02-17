from django.urls import path

from .views import CallListAPIView, CallUpdateDestoryAPIView, CallCreateAPIView

urlpatterns = [
    path("", CallListAPIView.as_view()),
    path("create/", CallCreateAPIView.as_view()),
    path("<int:pk>/", CallUpdateDestoryAPIView.as_view()),
]
