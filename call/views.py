from .serializer import CallSerializer
from .models import Call
from rest_framework.permissions import IsAdminUser
from rest_framework import generics


# Create your views here.


class CallListCreateAPIView(generics.ListCreateAPIView):
    queryset = Call.objects.all()
    serializer_class = CallSerializer
    permission_classes = [IsAdminUser]


class CallUpdateDestoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Call.objects.all()
    serializer_class = CallSerializer
    permission_classes = [IsAdminUser]
