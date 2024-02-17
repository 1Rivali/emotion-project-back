from rest_framework import serializers
from company.models import Company
from .models import Call
from user.models import User


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "email",
            "is_superuser",
        )


class CallSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    company = CompanySerializer()

    class Meta:
        model = Call
        fields = ["id", "url", "started_at", "user", "company"]


class CallCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = "__all__"
