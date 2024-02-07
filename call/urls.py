from django.urls import path

from .views import CallListCreateAPIView, CallUpdateDestoryAPIView


urlpatterns = [
    path("", CallListCreateAPIView.as_view()),
    path("<int:pk>/", CallUpdateDestoryAPIView.as_view()),
]
