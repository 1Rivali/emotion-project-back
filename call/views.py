from .serializer import CallSerializer, CallCreateUpdateSerializer
from .models import Call
from rest_framework.permissions import IsAdminUser
from rest_framework import generics


# Create your views here.


class CallListAPIView(generics.ListAPIView):
    queryset = Call.objects.all()
    serializer_class = CallSerializer
    permission_classes = [IsAdminUser]


class CallCreateAPIView(generics.CreateAPIView):
    queryset = Call.objects.all()
    serializer_class = CallCreateUpdateSerializer
    permission_classes = [IsAdminUser]


class CallUpdateDestoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Call.objects.all()
    serializer_class = CallCreateUpdateSerializer
    permission_classes = [IsAdminUser]
