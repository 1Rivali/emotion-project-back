from rest_framework import serializers

from company.models import Company
from .models import Job


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Job
        fields = ("id", "title", "description", "count_applicants", "company")

    def create(self, validated_data):
        return Job.objects.create(**validated_data)
