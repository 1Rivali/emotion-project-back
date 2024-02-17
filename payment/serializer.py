from rest_framework import serializers

from company.models import Company
from payment.models import Payment


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Payment
        fields = ("id", "amount", "company")

    def create(self, validated_data):
        return Payment.objects.create(**validated_data)
