from django.db import models
from company.models import Company

# Create your models here.


class Payment(models.Model):
    amount = models.IntegerField(null=False)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="company_payment"
    )
