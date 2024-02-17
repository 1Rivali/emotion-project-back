from django.urls import path
from .views import PaymentListCreateAPIView, PaymentUpdateDestroyAPIView

urlpatterns = [
    path("", PaymentListCreateAPIView.as_view()),
    path("payment/<pk>/", PaymentUpdateDestroyAPIView.as_view()),
]
