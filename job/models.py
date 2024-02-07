from django.db import models

from company.models import Company
from user.models import User


class Job(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="company_jobs"
    )
    count_applicants = models.IntegerField(null=False)
    applicants = models.ManyToManyField(User, blank=True)
