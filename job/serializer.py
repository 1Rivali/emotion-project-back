from rest_framework import serializers

from company.models import Company
from user.serializer import UserSerializer
from .models import Job


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    applicants = UserSerializer(many=True)

    class Meta:
        model = Job
        fields = (
            "id",
            "title",
            "description",
            "count_applicants",
            "company",
            "applicants",
        )

    def create(self, validated_data):
        return Job.objects.create(**validated_data)
