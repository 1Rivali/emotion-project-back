from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .models import Job
from .serializer import JobSerializer, CreateJobSerializer
from rest_framework.response import Response


# Create your views here.


class JobCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = CreateJobSerializer
    permission_classes = [IsAdminUser]


class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobUpdateDestoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminUser]


class JobApplyView(generics.UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        try:
            job = self.get_object()
            job.apply(request.user)
            return Response(
                {"detail": "Application submitted successfully."},
                status=status.HTTP_200_OK,
            )
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
