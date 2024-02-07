from rest_framework import serializers
from .models import Company
from job.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ("id", "title", "description", "count_applicants")


class CompanySerializer(serializers.ModelSerializer):
    company_jobs = JobSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ("id", "name", "type", "payment_type", "company_jobs")

    def create(self, validated_data):
        return Company.objects.create(**validated_data)
