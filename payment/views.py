from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from .serializer import PaymentSerializer
from .models import Payment
from rest_framework import generics, authentication


class PaymentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = [IsAdminUser]


class PaymentUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = [IsAdminUser]
