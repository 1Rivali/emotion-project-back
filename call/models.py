from django.db import models
from company.models import Company

from user.models import User

# Create your models here.


class Call(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id")
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="company"
    )
    url = models.TextField()
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = (models.DateTimeField(),)
