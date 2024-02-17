from django.core.exceptions import ValidationError
from django.db import models

from company.models import Company
from user.models import User


class Job(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="company_jobs"
    )
    count_applicants = models.IntegerField(default=0)
    applicants = models.ManyToManyField(User, null=True, blank=True)

    def apply(self, user):
        if not self.applicants.filter(pk=user.pk).exists():
            self.applicants.add(user)
            self.count_applicants += 1
            self.save()
        else:
            raise ValidationError("User has already applied to this job.")
